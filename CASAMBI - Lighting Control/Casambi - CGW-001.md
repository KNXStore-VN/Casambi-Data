---
# === IDENTIFICATION ===
sku: "CGW-001"
product_name: "Casambi CGW-001 - Cloud Gateway"
brand: "Casambi"
manufacturer_part_number: "CGW-001"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/casambi-cloud-gateway-cgw-001"
status: "active"

# === CLASSIFICATION ===
category_primary: "Gateways"
category_secondary: ["Remote Control", "Cloud Integration"]
protocols: ["Casambi", "Ethernet", "WiFi", "BLE"]

# === SHORT DESCRIPTION ===
short_description_vi: "Gateway điều khiển Casambi qua internet, hỗ trợ 2 phương thức kết nối PSU/PoE, dựa trên Raspberry Pi 4"
short_description_en: "Casambi Cloud Gateway for remote internet control of Casambi networks, supports PSU and PoE variants, based on Raspberry Pi 4"

# === SEARCH OPTIMIZATION ===
aliases: ["CGW-001-PSU", "CGW-001-POE", "Casambi Gateway", "Cloud Gateway"]
search_keywords_vi: ["Casambi", "gateway", "cloud", "remote control", "internet", "WiFi", "Ethernet", "PoE"]
search_keywords_en: ["Casambi", "gateway", "cloud", "remote control", "internet", "WiFi", "Ethernet", "PoE", "CGW-001"]

# === DECISION CRITERIA ===
use_case_tags: ["remote_control", "cloud_integration", "network_gateway", "system_control"]
target_segment: ["system_integrator", "commercial_installation"]
project_scale: ["medium", "large"]
complexity_level: "intermediate"
not_suitable_for: ["standalone_device", "single_luminaire_control"]

# === RELATIONSHIPS ===
replaces_sku: []
replaced_by_sku: null
equivalent_skus: []
accessories_required: ["Casambi Network", "Internet Connection"]
accessories_recommended: ["Separate Network for Gateway"]
bundle_with: []
upsell_to: []

# === CASAMBI INTEGRATION ===
casambi_network_type: ["all"]
casambi_pro_compatible: true
fixture_profile_default_id: "gateway"
fixture_profile_default_name: "Cloud Gateway"
fixture_profile_alternatives: []

# === COMMERCIAL REFERENCE ===
pricing_visibility: "sales_only"
stock_visibility: "sales_only"
moq_hint: "Liên hệ sales để biết MOQ và bậc giá theo số lượng"
warranty_months: 24
origin_country: "Finland"
hs_code_vn: ""

# === ASSETS ===
images:
  main: ""
  connectivity: ""
  installation: ""
datasheet_url: "https://www.casambi.com"
manual_url_en: "https://www.casambi.com"
manual_url_vi: null

# === FAQ EMBEDDED ===
common_questions:
  - question_vi: "CGW-001 là gì?"
    answer_vi: "Gateway điều khiển mạng Casambi qua internet. Cho phép điều khiển và giám sát mạng Casambi từ xa thông qua ứng dụng Casambi"
  - question_vi: "Có bao nhiêu loại CGW-001?"
    answer_vi: "2 loại: PSU (kèm adapter 100-240VAC) và PoE (cấp nguồn qua Ethernet)"
  - question_vi: "Cần mấy Gateway cho một mạng Casambi?"
    answer_vi: "Chỉ 1 Gateway cho mỗi mạng Casambi. Không cần nhiều"
  - question_vi: "Gateway kết nối internet như thế nào?"
    answer_vi: "Hỗ trợ Ethernet (Gigabit) hoặc WiFi 2.4GHz/5.0GHz. Tất cả kết nối được mã hóa HTTPS"
  - question_vi: "CGW-001 hỗ trợ những tính năng gì?"
    answer_vi: "Tạo scene, animation, điều khiển nhóm/toàn mạng, đổi màu/nhiệt độ, tạo timer, điều khiển từ Casambi App"

# === HANDOFF TRIGGERS ===
handoff_to_sales_when:
  - "user_asks_price"
  - "user_asks_stock"
  - "user_asks_quotation"
  - "user_asks_discount"
  - "user_asks_lead_time"
  - "user_asks_payment_terms"
  - "user_asks_delivery"
  - "user_mentions_project_above_10_units"
  - "user_asks_custom_integration"
  - "user_asks_network_setup"

# === DATA GOVERNANCE ===
last_updated: "2026-04-21"
last_verified_by: "auto_converter"
content_version: "1.0"
source_of_truth: "GATEWAY - Casambi CGW-001.md"
confidence_level: "high"
chatbot_priority: "high"

# === RAG OPTIMIZATION ===
chunk_strategy: "by_section"
priority_sections:
  - "Mô tả sản phẩm"
  - "Thông số kỹ thuật"
  - "Variants"
  - "Kết nối"
  - "Bảo mật"
  - "FAQ"

---

# Casambi CGW-001 - Cloud Gateway

## Đặc điểm nổi bật

✅ **Điều khiển qua internet** - Điều khiển mạng Casambi từ bất kỳ đâu qua Casambi App

✅ **2 phương thức cấp nguồn** - PSU (100-240VAC) hoặc PoE (Power over Ethernet)

✅ **Kết nối linh hoạt** - Ethernet Gigabit + WiFi 2.4GHz/5.0GHz

✅ **Bảo mật cao** - Mã hóa HTTPS, không có incoming connection

✅ **Dựa trên Raspberry Pi 4** - Quad-core ARM @ 1.5GHz, 4GB RAM, Bluetooth 5.0

✅ **Hỗ trợ Evolution** - Tương thích với firmware Evolution mới nhất

✅ **Quản lý tập trung** - 1 Gateway cho mỗi mạng Casambi, điều khiển 250+ devices

## Mô tả sản phẩm

Casambi Cloud Gateway (CGW-001) cho phép điều khiển và giám sát mạng Casambi từ xa qua internet. Dựa trên Raspberry Pi 4, hỗ trợ hai phiên bản:
- **PSU**: Cấp nguồn qua adapter 100-240VAC (phù hợp EU, UK, US, AU, PRC)
- **PoE**: Cấp nguồn qua Ethernet (yêu cầu splitter tách dữ liệu/nguồn)

## Thông số kỹ thuật

### Phần cứng

| Thông số | Giá trị |
|---------|--------|
| Processor | Broadcom BCM2711 Quad-core Cortex-A72 (ARM v8) @ 1.5GHz |
| RAM | 4GB LPDDR4-3200 |
| Lưu trữ | Flash memory SD card |
| Certifications | FCC, IC, CE, UK CA, KCC (47 tổng cộng) |

### Kết nối

| Thông số | Giá trị |
|---------|--------|
| Ethernet | Gigabit (RJ45) |
| WiFi | 2.4GHz / 5.0GHz IEEE 802.11ac |
| Bluetooth | 5.0, BLE |
| USB | USB-C |
| Cấp nguồn PSU | 5V DC via USB-C (min 3A), adapter 100-240VAC |
| Cấp nguồn PoE | Power over Ethernet (kèm splitter) |

### Môi trường

| Thông số | Giá trị |
|---------|--------|
| Nhiệt độ hoạt động | 0 - 50°C (32 - 122°F) |
| Loại sử dụng | Indoor only |
| Chứng chỉ | CE, FCC, IC, UK CA, KCC |

## Variants

### CGW-001-PSU (Power Supply Unit)

- Cấp nguồn: Adapter 100-240VAC
- Phù hợp: EU, UK, US, AU, PRC regions
- Cài đặt: Đơn giản, plug-and-play

### CGW-001-POE (Power over Ethernet)

- Cấp nguồn: Power over Ethernet
- Kèm: PoE splitter (tách dữ liệu/nguồn)
- Ưu điểm: Tiết kiệm dây, phù hợp cài đặt chuyên nghiệp

## Chức năng & Điều khiển

### Tính năng cốt lõi

✅ **Tạo & Điều khiển Scene** - Tạo scene, animation, thời gian biểu

✅ **Điều khiển hàng loạt** - Bật/tắt/dim toàn mạng hoặc nhóm devices

✅ **Điều khiển màu sắc** - Đổi color temperature, hue, saturation

✅ **Hẹn giờ** - Tạo timer tự động

### Giao diện & Điều khiển

- **Casambi App**: iOS 10+, Android 4.4+
- **Giao diện**: Giống như điều khiển cầm tay, nhưng qua internet
- **Phạm vi**: Không giới hạn (qua internet)

## Bảo mật

⚠️ **Security Features:**
- ✅ Mã hóa HTTPS (TLS) tất cả kết nối internet
- ✅ Gateway khởi tạo tất cả traffic (outbound only, không incoming connections)
- ✅ Tuân theo best practices ngành

**Khuyến cáo:**
- Đặt Gateway trên mạng riêng biệt (separate from business-critical devices)
- Lưu trữ Gateway ở vị trí an toàn
- Theo dõi cài đặt mạng (hướng dẫn trong installation guide)

## Yêu cầu & Cài đặt

**Yêu cầu:**
- Mạng Casambi hoạt động bình thường (Casambi Coordinator/Repeaters)
- Kết nối internet ổn định (Ethernet hoặc WiFi)
- Casambi App trên iOS/Android để điều khiển

**Cài đặt:**
1. Kết nối Gateway vào mạng Casambi (Bluetooth)
2. Kết nối internet (Ethernet hoặc WiFi)
3. Cấp điện (PSU hoặc PoE)
4. Cấu hình trong Casambi App
5. Hoàn tất: Điều khiển qua App

## Lưu ý quan trọng

⚠️ **Một Gateway cho mỗi mạng:**
- Chỉ sử dụng 1 CGW-001 cho mỗi Casambi network
- Không cần nhiều gateway

⚠️ **Evolution Firmware:**
- CGW-001 hỗ trợ Evolution firmware
- Cập nhật firmware thông qua Casambi App

⚠️ **Không incoming connection:**
- Gateway chỉ khởi tạo kết nối outbound
- Không có server công khai, an toàn hơn

## Ứng dụng

**Văn phòng đa tầng:** Điều khiển hệ thống chiếu sáng từ trung tâm quản lý

**Bảo tàng/Trưng bày:** Remote control lighting scene từ phòng điều khiển

**Khách sạn:** Khách điều khiển phòng từ xa (nếu tích hợp Casambi App vào room app)

**Nhà thông minh:** Điều khiển mạng Casambi khi vắng nhà

**Sân khấu/Sự kiện:** Điều khiển lighting từ trung tâm, không cần vào từng vị trí

## Tài liệu kỹ thuật

📄 **Tài liệu chính thức:**

👉 [Trang sản phẩm CGW-001](https://knxstore.vn/products/casambi-cloud-gateway-cgw-001)

👉 [Hướng dẫn Casambi](https://www.casambi.com)

👉 [Installation Guide](https://www.casambi.com) - Chứa cài đặt mạng & kết nối internet

## Bảo hành & Hỗ trợ

- **Bảo hành:** 24 tháng
- **Hỗ trợ:** knxstore.vn
- **Xuất xứ:** Finland (Casambi Technologies Oy)
- **Certifications:** FCC, IC, CE, UK CA, KCC (47 total)

---

**Ghi chú:** CGW-001 là gateway cốt lõi để mở khóa điều khiển Casambi từ xa. Bắt buộc cho bất kỳ cài đặt Casambi nào cần điều khiển qua internet hoặc tích hợp hệ thống cao cấp.
