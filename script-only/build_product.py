"""
KNXStore Product Builder
========================
Tạo file product_SKU.md chuẩn RAG từ 2 nguồn:

  Mode A — URL sản phẩm:
    python build_product.py --url https://knxstore.vn/products/ten-san-pham
    python build_product.py --url https://... https://...   (nhiều URL)

  Mode B — File .md cũ + CSV (merge):
    python build_product.py --md product_CBU-DA-1P.md --csv casambProduct.csv

  Mode C — Batch toàn bộ CSV:
    python build_product.py --csv casambProduct.csv --batch

Output: RAG For training/product_SKU.md

Yêu cầu: pip install requests beautifulsoup4
"""

import argparse
import csv
import os
import re
import sys
import time
from datetime import date
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ Thiếu thư viện. Chạy: pip install requests beautifulsoup4")
    sys.exit(1)

# ================================================================
# CẤU HÌNH — chỉnh đường dẫn cho phù hợp với workspace của bạn
# ================================================================
TEMPLATE_PATH   = "productTemplate.md"          # file template
OUTPUT_DIR      = "RAG For training"             # thư mục output
ZALO_LINK       = "https://zalo.me/0918918755"
DELAY_SECONDS   = 0.8
BASE_URL        = "https://knxstore.vn"
CATALOG_BASE    = f"{BASE_URL}/assets/image/catalog/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Brand map: keyword trong tên → brand chuẩn
BRAND_MAP = {
    "Olfer": "Olfer", "Olfer": "Olfer",
    "Vlinca": "Vlinca",
    "Salvador": "Salvador",
    "Tridonic": "Tridonic",
    "Sunricher": "Sunricher",
    "Vadsbo": "Vadsbo",
    "Maintronic": "Maintronic",
    "AIMOTION": "AIMOTION",
    "Danlers": "Danlers",
    "Remotec": "Remotec",
    "Siqitech": "Siqitech",
    "Moorgen": "Moorgen",
    "Bticino": "Bticino",
    "Versaan": "Versaan",
    "Scemtec": "Scemtec",
    "DALCNET": "DALCNET",
    "Rayrun": "Rayrun",
    "Protopixel": "Protopixel",
    "Ebelong": "Ebelong",
    "Lithernet": "Lithernet",
    "Carus": "Carus",
}


# ================================================================
# SCRAPE
# ================================================================
def scrape_product(url: str) -> dict:
    """Scrape thông tin sản phẩm từ trang knxstore.vn"""
    data = {
        "url": url,
        "title": "", "brand": "", "sku": "",
        "image_url": "", "price": "",
        "pdf_datasheet": "", "pdf_profiles": "", "pdf_all": "",
        "specs": {},        # dict key→value từ bảng thông số
        "description": "",  # mô tả sản phẩm
        "status": "error",
    }

    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        r.raise_for_status()
        html = r.text
        soup = BeautifulSoup(html, "html.parser")

        # Tên & ảnh từ og tags
        og_title = soup.find("meta", property="og:title")
        og_image = soup.find("meta", property="og:image")
        data["title"] = og_title["content"].strip() if og_title else ""
        data["image_url"] = og_image["content"].strip() if og_image else ""

        # PDF
        pdf_names = re.findall(r'view_catalogue\([\'"]([^\'"]+)[\'"]\)', html)
        pdf_urls  = [f"{CATALOG_BASE}{n}" for n in pdf_names]
        if pdf_urls:
            data["pdf_datasheet"] = pdf_urls[0]
        if len(pdf_urls) >= 2:
            data["pdf_profiles"] = pdf_urls[1]
        data["pdf_all"] = " | ".join(pdf_urls)

        # Giá — tìm pattern số + đ
        price_m = re.search(r'([\d\.]+)\s*[đĐ₫]', html)
        if price_m:
            raw = price_m.group(1).replace(".", "")
            if len(raw) >= 6:   # tránh số lẻ không phải giá
                data["price"] = price_m.group(0).strip()

        # Specs table
        for row in soup.select("table tr"):
            cells = row.find_all(["td", "th"])
            if len(cells) == 2:
                k = cells[0].get_text(separator=" ", strip=True)
                v = cells[1].get_text(separator=" ", strip=True)
                if k and v and len(k) < 80:
                    data["specs"][k] = v

        # Mô tả
        for sel in ["div.product-description", "div.description",
                    "div#product-description", "div.tab-content"]:
            el = soup.select_one(sel)
            if el:
                data["description"] = el.get_text(separator="\n", strip=True)[:1500]
                break

        # Brand & SKU từ tên
        data["brand"] = extract_brand(data["title"])
        data["sku"]   = extract_sku(data["title"])

        data["status"] = "ok"

    except requests.exceptions.HTTPError as e:
        data["status"] = f"HTTP {e.response.status_code}"
    except Exception as e:
        data["status"] = f"error: {str(e)[:60]}"

    return data


def extract_brand(title: str) -> str:
    for keyword, brand in BRAND_MAP.items():
        if keyword.lower() in title.lower():
            return brand
    return ""


def extract_sku(title: str) -> str:
    title = title.strip()
    if title.startswith("[Combo]"):
        return ""
    sku_pattern = re.compile(r'^[A-Z0-9][A-Z0-9\-\.\/]{2,}$')
    parts = [p.strip() for p in re.split(r'\s[–\-]\s', title)]
    candidates = [parts[-1], parts[0]] if len(parts) > 1 else parts
    for c in candidates:
        c = re.sub(r'\s*\(.*?\)', '', c).strip()
        if sku_pattern.match(c):
            return c
    return ""


# ================================================================
# CSV
# ================================================================
def load_csv(csv_path: str) -> list[dict]:
    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    return rows


def find_csv_row(rows: list[dict], sku: str = "", url: str = "") -> dict | None:
    for row in rows:
        if sku and row.get("sku_extracted", "").strip() == sku.strip():
            return row
        if url and row.get("product_url", "").strip() == url.strip():
            return row
    return None


# ================================================================
# TEMPLATE BUILDER
# ================================================================
def load_template(template_path: str) -> str:
    p = Path(template_path)
    if not p.exists():
        # tìm trong cùng thư mục script
        alt = Path(__file__).parent / template_path
        if alt.exists():
            p = alt
        else:
            print(f"❌ Không tìm thấy template: {template_path}")
            sys.exit(1)
    return p.read_text(encoding="utf-8")


def build_specs_table(specs: dict) -> str:
    if not specs:
        return (
            "| Thông số | Giá trị |\n|:---|:---|\n"
            "| Nguồn cấp | Xem datasheet |\n"
            "| Công suất tiêu thụ | Xem datasheet |\n"
            "| Nhiệt độ hoạt động | Xem datasheet |\n"
            "| Kích thước (mm) | Xem datasheet |"
        )
    lines = ["| Thông số | Giá trị |", "|:---|:---|"]
    for k, v in specs.items():
        lines.append(f"| {k} | {v} |")
    return "\n".join(lines)


def build_md_from_scrape(scraped: dict, template: str) -> str:
    """Điền template từ data đã scrape"""
    sku          = scraped.get("sku", "")
    title        = scraped.get("title", "")
    brand        = scraped.get("brand", "")
    url          = scraped.get("url", "")
    image_url    = scraped.get("image_url", "")
    datasheet    = scraped.get("pdf_datasheet", "")
    profiles_url = scraped.get("pdf_profiles", "")
    specs        = scraped.get("specs", {})
    today        = date.today().isoformat()

    # Tên ngắn cho heading: bỏ brand nếu đã có ở đầu
    short_name = title
    if brand and title.lower().startswith(brand.lower()):
        short_name = title[len(brand):].strip(" -–")

    product_link = f"👉 [{brand} {sku} – {short_name}]({url})" if sku else f"👉 [{title}]({url})"

    content = template

    # ---- YAML frontmatter ----
    content = _set_yaml(content, "sku",                   f'"{sku}"')
    content = _set_yaml(content, "product_name",          f'"{brand} {sku} – {short_name}"'.strip())
    content = _set_yaml(content, "brand",                 f'"{brand}"')
    content = _set_yaml(content, "manufacturer_part_number", f'"{sku}"')
    content = _set_yaml(content, "website_url",           f'"{url}"')
    content = _set_yaml(content, "last_updated",          f'"{today}"')
    content = _set_yaml(content, "last_verified_by",      '"knxstore-marketing"')
    content = _set_yaml(content, "source_of_truth",       f'"{url}"')
    content = _set_yaml(content, "confidence_level",
                        '"high"' if (image_url and datasheet) else '"medium"')

    # assets
    content = content.replace('  main: ""',        f'  main: "{image_url}"')
    content = _set_yaml(content, "datasheet_url",  f'"{datasheet}"' if datasheet else '""')
    content = _set_yaml(content, "manual_url_en",  f'"{datasheet}"' if datasheet else '""')

    # profiles_url — thêm sau manual_url_en nếu chưa có
    if profiles_url and "profiles_url:" not in content:
        content = content.replace(
            'manual_url_vi: null',
            f'manual_url_vi: null\nprofiles_url: "{profiles_url}"'
        )

    # product_link_text
    content = _set_yaml(content, "product_link_text", f'"{product_link}"')

    # ---- Body heading ----
    content = content.replace(
        "# [BRAND] [MODEL] – [Tên sản phẩm]",
        f"# {brand} {sku} – {short_name}"
    )

    # ---- Tổng quan ----
    content = content.replace(
        "[Tên sản phẩm] là [loại thiết bị] thuộc hệ [ecosystem], cho phép [chức năng chính]. Thiết bị phù hợp với [đối tượng] trong các dự án [loại công trình].",
        f"*[Cần bổ sung mô tả tổng quan cho {sku}. Tham khảo trang sản phẩm và datasheet.]*"
    )
    content = content.replace(
        "👉 [Xem sản phẩm trên KNXStore](URL)",
        f"👉 [Xem sản phẩm trên KNXStore]({url})"
    )

    # ---- Thông số kỹ thuật ----
    specs_table = build_specs_table(specs)
    old_specs = (
        "| Thông số | Giá trị |\n|:---|:---|\n"
        "| Nguồn cấp | |\n"
        "| Công suất tiêu thụ | |\n"
        "| Nhiệt độ hoạt động | |\n"
        "| Kích thước (mm) | |\n"
        "| Lắp đặt | |\n"
        "| Chứng nhận | |\n"
        "| Bảo hành | tháng |"
    )
    content = content.replace(old_specs, specs_table)

    # ---- Hiển thị sản phẩm — điền URL thật ----
    content = content.replace("DATASHEET_URL", datasheet if datasheet else url)
    content = content.replace("WEBSITE_URL",   url)
    content = content.replace(
        "📄 [Datasheet chính thức](URL)",
        f"📄 [Datasheet – {sku}]({datasheet})" if datasheet else "📄 Datasheet: xem trang sản phẩm"
    )
    content = content.replace(
        "📄 [User Manual EN](URL)",
        f"📄 [User Manual EN]({datasheet})" if datasheet else ""
    )
    content = content.replace(
        "🔗 [Trang sản phẩm KNXStore](URL)",
        f"🛒 [Trang sản phẩm KNXStore]({url})"
    )

    # ---- Bảo hành ----
    content = content.replace(
        "- Hỗ trợ kỹ thuật: [email/phone/zalo]",
        f"- Hỗ trợ kỹ thuật: knxstore.vn | Zalo [{ZALO_LINK.split('/')[-1]}]({ZALO_LINK})"
    )

    # ---- Xóa HTML comments (không cần trong output) ----
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


def merge_csv_into_md(md_content: str, csv_row: dict) -> str:
    """Merge CSV data vào file .md đã có — chỉ điền field trống"""

    def fill_if_empty(content, yaml_key, value):
        pattern = rf'({yaml_key}:\s*)""\s*'
        if re.search(pattern, content) and value:
            content = re.sub(pattern, f'{yaml_key}: "{value}"', content)
        return content

    image_url    = csv_row.get("image_url", "")
    datasheet    = csv_row.get("pdf_datasheet", "")
    profiles_url = csv_row.get("pdf_profiles", "")
    sku          = csv_row.get("sku_extracted", "")
    url          = csv_row.get("product_url", "")

    md_content = fill_if_empty(md_content, "sku",          sku)
    md_content = fill_if_empty(md_content, "website_url",  url)
    md_content = fill_if_empty(md_content, "datasheet_url", datasheet)
    md_content = fill_if_empty(md_content, "manual_url_en", datasheet)

    # images.main
    if '  main: ""' in md_content and image_url:
        md_content = md_content.replace('  main: ""', f'  main: "{image_url}"')

    # profiles_url
    if profiles_url and "profiles_url:" not in md_content:
        md_content = md_content.replace(
            'manual_url_vi: null',
            f'manual_url_vi: null\nprofiles_url: "{profiles_url}"'
        )

    # last_updated
    if 'last_updated: ""' in md_content:
        md_content = md_content.replace(
            'last_updated: ""',
            f'last_updated: "{date.today().isoformat()}"'
        )

    return md_content


def _set_yaml(content: str, key: str, value: str) -> str:
    """Thay thế giá trị của 1 YAML key (chỉ thay dòng có giá trị trống hoặc placeholder)"""
    pattern = rf'^({key}:\s*)(".+?"|\'.*?\'|\[\]|null|"")(\s*(#.*)?)$'
    replacement = rf'\g<1>{value}\g<4>'
    return re.sub(pattern, replacement, content, flags=re.MULTILINE)


# ================================================================
# OUTPUT
# ================================================================
def make_filename(sku: str, title: str) -> str:
    if sku:
        return f"product_{sku}.md"
    # Fallback: dùng slug từ title
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[\s]+', '-', slug)[:60]
    return f"product_{slug}.md"


def save_output(content: str, filename: str, output_dir: str) -> Path:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / filename

    if path.exists():
        backup = path.with_suffix(f".bak{date.today().strftime('%Y%m%d')}.md")
        path.rename(backup)
        print(f"   ⚠️  File đã tồn tại → backup: {backup.name}")

    path.write_text(content, encoding="utf-8")
    return path


def print_summary(scraped: dict, out_path: Path):
    s = scraped
    print(f"\n{'='*55}")
    print(f"✅  {out_path}")
    print(f"    SKU        : {s.get('sku') or '⚠️  trống — điền thủ công'}")
    print(f"    Brand      : {s.get('brand') or '⚠️  trống'}")
    print(f"    Ảnh        : {'✅' if s.get('image_url') else '❌ không có'}")
    print(f"    Datasheet  : {'✅ PDF' if s.get('pdf_datasheet') else '⚠️  không có'}")
    print(f"    Profiles   : {'✅ PDF' if s.get('pdf_profiles') else '—'}")
    print(f"    Specs      : {len(s.get('specs', {}))} thông số")
    confidence = "high" if (s.get('image_url') and s.get('pdf_datasheet')) else "medium"
    print(f"    Confidence : {confidence}")
    if not s.get('sku'):
        print(f"\n    ⚠️  Cần điền thủ công: sku, brand (nếu chưa đúng)")


# ================================================================
# MODES
# ================================================================
def run_url_mode(urls: list[str], template: str, output_dir: str):
    print(f"\n🔍 Mode A — Scrape {len(urls)} URL\n")
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {url.split('/products/')[-1]}")
        scraped = scrape_product(url)

        if scraped["status"] != "ok":
            print(f"   ❌ {scraped['status']}")
            continue

        md = build_md_from_scrape(scraped, template)
        filename = make_filename(scraped["sku"], scraped["title"])
        out_path = save_output(md, filename, output_dir)
        print_summary(scraped, out_path)

        if i < len(urls):
            time.sleep(DELAY_SECONDS)


def run_merge_mode(md_path: str, csv_path: str, output_dir: str):
    print(f"\n🔀 Mode B — Merge CSV vào {md_path}\n")
    md_file = Path(md_path)
    if not md_file.exists():
        print(f"❌ Không tìm thấy file: {md_path}")
        sys.exit(1)

    md_content = md_file.read_text(encoding="utf-8")

    # Lấy SKU và URL từ file .md
    sku_m   = re.search(r'^sku:\s*["\']?([^"\'#\n]+)["\']?', md_content, re.MULTILINE)
    url_m   = re.search(r'^website_url:\s*["\']?([^"\'#\n]+)["\']?', md_content, re.MULTILINE)
    sku_val = sku_m.group(1).strip() if sku_m else ""
    url_val = url_m.group(1).strip() if url_m else ""

    csv_rows = load_csv(csv_path)
    row = find_csv_row(csv_rows, sku=sku_val, url=url_val)

    if row:
        print(f"   ✅ Tìm thấy CSV row cho: {sku_val or url_val}")
        md_content = merge_csv_into_md(md_content, row)
    else:
        print(f"   ⚠️  Không tìm thấy CSV row cho SKU='{sku_val}' URL='{url_val}'")
        print(f"       File sẽ được lưu không thay đổi.")

    filename  = make_filename(sku_val, md_file.stem)
    out_path  = save_output(md_content, filename, output_dir)
    print(f"\n✅  {out_path}")


def run_batch_mode(csv_path: str, template: str, output_dir: str):
    csv_rows = load_csv(csv_path)
    urls = [r["product_url"] for r in csv_rows if r.get("product_url")]
    print(f"\n📋 Mode C — Batch {len(urls)} sản phẩm từ CSV\n")

    ok = skip = 0
    for i, url in enumerate(urls, 1):
        # Tìm row CSV tương ứng
        row = next((r for r in csv_rows if r.get("product_url") == url), {})
        slug = url.split("/products/")[-1] if url else f"product_{i}"
        print(f"[{i:03d}/{len(urls)}] {slug[:60]}")

        scraped = scrape_product(url)
        if scraped["status"] != "ok":
            print(f"   ❌ {scraped['status']}")
            skip += 1
            continue

        # Ưu tiên sku_extracted từ CSV
        if row.get("sku_extracted"):
            scraped["sku"] = row["sku_extracted"]

        md = build_md_from_scrape(scraped, template)
        filename = make_filename(scraped["sku"], scraped["title"])
        out_path = save_output(md, filename, output_dir)
        print(f"   ✅ → {filename}")
        ok += 1

        if i < len(urls):
            time.sleep(DELAY_SECONDS)

    print(f"\n{'='*55}")
    print(f"✅ Hoàn tất: {ok}/{len(urls)} file | ❌ Lỗi: {skip}")
    print(f"📁 Output: {output_dir}/")


# ================================================================
# MAIN
# ================================================================
def main():
    parser = argparse.ArgumentParser(
        description="KNXStore Product Builder — tạo file product_SKU.md cho RAG"
    )
    parser.add_argument("--url",   nargs="+", help="URL sản phẩm knxstore.vn (1 hoặc nhiều)")
    parser.add_argument("--md",    help="File .md sản phẩm đã có (Mode B)")
    parser.add_argument("--csv",   help="File CSV (casambi_full_sku.csv)")
    parser.add_argument("--batch", action="store_true", help="Batch toàn bộ URL trong CSV")
    parser.add_argument("--template", default=TEMPLATE_PATH, help=f"Template path (mặc định: {TEMPLATE_PATH})")
    parser.add_argument("--output",   default=OUTPUT_DIR,    help=f"Thư mục output (mặc định: {OUTPUT_DIR})")
    args = parser.parse_args()

    template = load_template(args.template)

    if args.url:
        run_url_mode(args.url, template, args.output)

    elif args.md and args.csv:
        run_merge_mode(args.md, args.csv, args.output)

    elif args.csv and args.batch:
        run_batch_mode(args.csv, template, args.output)

    else:
        parser.print_help()
        print("\nVí dụ:")
        print("  python build_product.py --url https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p")
        print("  python build_product.py --md product_CBU-DA-1P.md --csv casambProduct.csv")
        print("  python build_product.py --csv casambProduct.csv --batch")


if __name__ == "__main__":
    main()