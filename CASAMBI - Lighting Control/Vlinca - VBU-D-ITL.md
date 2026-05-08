---
sku: "VBU-D-ITL"
product_name: "Vlinca VBU-D-ITL - Casambi to DALI Controller"
brand: "Vlinca"
manufacturer_part_number: "VBU-D-ITL"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/casambi-dali-lap-ray-nam-cham-48vdc-vlinca-vbu-d-itl"
status: "active"

category_primary: "DALI Controllers"
category_secondary: []
protocols: ["CASAMBI", "DALI", "DT6", "DT8"]

short_description_vi: "Bộ điều khiển Casambi to DALI với power supply tích hợp 48VDC, hỗ trợ tối đa 8 drivers DT6/DT8, điều khiển individual/group qua Bluetooth"
short_description_en: "Casambi to DALI controller with integrated 48VDC power supply, supports up to 8 DALI DT6/DT8 drivers, individual/group control via Bluetooth"

aliases: ["VBU-D-ITL", "Vlinca DALI", "Vlinca D-ITL"]
search_keywords_vi: ["Casambi", "DALI", "DT6", "DT8", "8 drivers", "group control", "Bluetooth", "power supply tích hợp", "magnetic latch relay"]
search_keywords_en: ["Casambi", "DALI", "DT6", "DT8", "8 channels", "group", "Bluetooth", "integrated power", "relay"]

use_case_tags: ["dali_control", "small_dali_system", "group_control", "dt6_dt8_support"]
target_segment: ["system_integrator", "smart_home_diy"]
project_scale: ["small", "medium"]
complexity_level: "intermediate"
not_suitable_for: ["large_dali_systems", "64_address_dali"]

replaces_sku: []
replaced_by_sku: null
equivalent_skus: []
accessories_required: []
accessories_recommended: []
bundle_with: []
upsell_to: []

casambi_network_type: ["standard", "mesh"]
casambi_pro_compatible: false
fixture_profile_default_id: "VBU-D-ITL (8 ID-DT6)"
fixture_profile_default_name: "8 Individual Dimmers DT6"
fixture_profile_alternatives: ["1-7 ID-DT6", "1-8 Group-DT6", "1 Group-DT8"]

pricing_visibility: "sales_only"
stock_visibility: "sales_only"
moq_hint: "Liên hệ sales để biết MOQ và bậc giá theo số lượng"
warranty_months: 24
origin_country: "China"
hs_code_vn: ""

images:
  main: ""
  wiring: ""
  dimensions: ""
datasheet_url: ""
manual_url_en: ""
manual_url_vi: null

common_questions:
  - question_vi: "VBU-D-ITL có thể điều khiển bao nhiêu driver DALI?"
    answer_vi: "Tối đa 8 DALI drivers hoặc 8 groups của drivers. Có nhiều profile để lựa chọn (1-8 individual, 1-8 groups)"
  - question_vi: "Cần cấp điện bên ngoài không?"
    answer_vi: "Có, cần 48VDC bên ngoài. Bộ điều khiển có power supply tích hợp (14-16VDC) cho DALI bus với 20mA guaranteed + 60mA max"
  - question_vi: "Hỗ trợ DALI nào?"
    answer_vi: "Hỗ trợ DALI DT6 (dimming) và DALI DT8 (color control). Có thể điều khiển individual (short address) hoặc groups"
  - question_vi: "Có thể thay đổi fixture profile sau khi lắp không?"
    answer_vi: "Có, nhưng phải unpair device từ network trước. Dùng app để change profile, sau đó update lại"
  - question_vi: "Phạm vi Bluetooth của VBU-D-ITL là bao xa?"
    answer_vi: "VBU-D-ITL hoạt động trong Casambi mesh network. Phạm vi phụ thuộc vào network setup và vật cản"

handoff_to_sales_when:
  - "user_asks_price"
  - "user_asks_stock"
  - "user_asks_quotation"
  - "user_asks_discount"
  - "user_asks_lead_time"
  - "user_asks_payment_terms"
  - "user_asks_delivery"
  - "user_mentions_project_above_50_units"
  - "user_asks_custom_integration"
  - "user_asks_warranty_claim"

last_updated: "2026-04-21"
last_verified_by: "auto_converter"
content_version: "1.0"
source_of_truth: "DALI - Vlinca VBU-D-ITL.md"
confidence_level: "high"
chatbot_priority: "medium"

chunk_strategy: "by_section"
priority_sections:
  - "Thông số kỹ thuật"
  - "Fixture Profiles"
  - "Sơ đồ nối dây"
  - "Ứng dụng"
  - "FAQ"

---

# Vlinca VBU-D-ITL - Casambi to DALI Controller

## Đặc điểm nổi bật

✅ **Power supply tích hợp** - 48VDC input, DALI bus 14-16VDC 20mA guaranteed (max 60mA)

✅ **Bluetooth Casambi** - Điều khiển qua app, mesh network support

✅ **Tối đa 8 drivers** - Điều khiển individual (short address) hoặc groups

✅ **DALI DT6 & DT8** - Hỗ trợ dimming và color control

✅ **Nhiều fixture profiles** - 1-8 individual, 1-8 groups, DT8 broadcast

✅ **Compact size** - 98 x 38 x 19.3 mm, dễ lắp đặt

✅ **Reset button** - Dễ unpair và reconfigure

✅ **OTA firmware update** - Cập nhật qua app

## Thông số kỹ thucircuit

### Nguồn & Tiêu thụ

| Thông số | Giá trị |
|---------|--------|
| Input voltage | 48 VDC |
| Input current | ≤10 mA |
| Standby power | <0.5 W |

### DALI Bus (Tích hợp)

| Thông số | Giá trị |
|---------|--------|
| Bus voltage | 14-16 VDC |
| Guaranteed current | 20 mA |
| Maximum current | 60 mA |
| Max drivers | 8 (individual or groups) |
| Tiêu chuẩn | DT6, DT8 |

### Casambi (Bluetooth)

| Thông số | Giá trị |
|---------|--------|
| Communication | BLE (Bluetooth Low Energy) |
| Tần số | 2402-2480 MHz |
| Công suất phát | +7 dBm |
| Network | Mesh support |
| Firmware update | OTA (Over the Air) |

### Bảo vệ & Điều kiện

| Thông số | Giá trị |
|---------|--------|
| Protections | Short circuit, Overload, No-load |
| Operating temperature | -20°C to +40°C |
| Case temperature max | +50°C |
| Storage temperature | -20°C to +80°C |
| IP Protection | IP20 |
| Dimensions | 98 x 38 x 19.3 mm |
| Certifications | CE, Directive 2014/53/EU |

## Fixture Profiles

### Individual Address Profiles (DT6)

| Profile | Mô tả | DALI Addresses |
|---------|-------|-----------------|
| **VBU-D-ITL (8 ID-DT6)** (Default) | 8 individual dimmers | A0-A7 |
| VBU-D-ITL (1 ID-DT6) | 1 dimmer | A0 |
| VBU-D-ITL (2 ID-DT6) | 2 dimmers | A0, A1 |
| VBU-D-ITL (3 ID-DT6) | 3 dimmers | A0-A2 |
| VBU-D-ITL (4 ID-DT6) | 4 dimmers | A0-A3 |
| VBU-D-ITL (5 ID-DT6) | 5 dimmers | A0-A4 |
| VBU-D-ITL (6 ID-DT6) | 6 dimmers | A0-A5 |
| VBU-D-ITL (7 ID-DT6) | 7 dimmers | A0-A6 |

### Group Control Profiles (DT6)

| Profile | Mô tả | DALI Groups |
|---------|-------|-------------|
| VBU-D-ITL (1 Group-DT6) | 1 group control | G0 |
| VBU-D-ITL (2 Group-DT6) | 2 group control | G0, G1 |
| VBU-D-ITL (3 Group-DT6) | 3 group control | G0-G2 |
| VBU-D-ITL (4 Group-DT6) | 4 group control | G0-G3 |
| VBU-D-ITL (5 Group-DT6) | 5 group control | G0-G4 |
| VBU-D-ITL (6 Group-DT6) | 6 group control | G0-G5 |
| VBU-D-ITL (7 Group-DT6) | 7 group control | G0-G6 |
| VBU-D-ITL (8 Group-DT6) | 8 group control | G0-G7 |

### DT8 Profiles (Color)

| Profile | Mô tả | Control mode |
|---------|-------|--------------|
| VBU-D-ITL (1 Group-DT8) | 1 group DT8 | Brightness + Color temp (broadcast) |

## Lắp đặt & Cấu hình

### Wiring

1. **48VDC power supply** → VBU-D-ITL input
2. **DALI bus** (DA1/DA2) → DALI drivers (tối đa 8 cái)
3. **Casambi App** → Tìm "Nearby devices" → Select VBU-D-ITL

### Pairing & Fixture Profile

1. **Default profile:** VBU-D-ITL (8 ID-DT6)
2. **Change profile:** 
   - Unpair device từ network
   - Tap "Nearby devices"
   - Select "VBU-D-ITL" → "Change profile"
   - Chọn profile mong muốn
   - Refresh display từ app

### Scan DALI Devices

1. **After pairing:** Luminaires tab → VBU-D-ITL → Details
2. **Scan:** Quét lại DALI devices để update addresses, groups, types
3. **Verify:** Đảm bảo addresses/groups match với fixture profile
   - Nếu profile = "4 DT6" → Chỉ A0-A3 được control
   - Nếu profile = "4 Group DT6" → Chỉ G0-G3 được control

### Reset Button

- **Location:** Inside reset button (phía trên)
- **Dùng:** Needle/paperclip để bấm
- **Hiệu lực:** Switch OFF và ON lại (unpair khỏi network)

## Lưu ý quan trọng

⚠️ **DALI Bus:**
- Tổng current từ tất cả power supplies không được vượt quá recommended limits
- Do not assign a DALI driver to multiple groups

⚠️ **Profile Configuration:**
- Chỉ có thể control đến số addresses/groups theo fixture profile
- Nếu gán driver vượt quá limit → Không được control qua app

✅ **DT6 vs DT8:**
- DT6: Dimming only (brightness)
- DT8 (broadcast): Brightness + color temperature control

## Ứng dụng

**Văn phòng nhỏ:** 4-8 zones với DT6 dimming → Individual control qua Casambi app

**Showroom:** 8 groups của DT8 drivers → Preset scenes, color temp adjustment

**Retail:** Mix individual + group control → Linh hoạt theo layout cửa hàng

**Sân khấu/Studio:** DT8 group → Điều chỉnh intensity + color temperature từ xa

## Sản phẩm tương thích

**Bắt buộc:**
- DALI DT6 hoặc DT8 drivers (tối đa 8 cái)
- 48VDC external power supply
- Casambi App (iOS/Android)

**Khuyến nghị:**
- Power supply đủ capacity (≥150mA để chắc chắn)
- Test DALI address/group assignments sau khi wire

## Tài liệu kỹ thuật

📄 **Tài liệu chi tiết:**

👉 [Trang sản phẩm VBU-D-ITL](https://knxstore.vn/products/casambi-dali-lap-ray-nam-cham-48vdc-vlinca-vbu-d-itl)

## Bảo hành & Hỗ trợ

- **Bảo hành:** 24 tháng
- **Hỗ trợ:** knxstore.vn
- **Xuất xứ:** China (Vlinca)

---

**Ghi chú:** VBU-D-ITL là giải pháp tối ưu cho hệ thống DALI nhỏ đến vừa (1-8 drivers). Cho phép điều khiển linh hoạt theo individual drivers hoặc groups. Phù hợp cho renovation, small office, retail.
