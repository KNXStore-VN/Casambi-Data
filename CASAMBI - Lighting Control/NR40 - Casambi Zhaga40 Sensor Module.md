---
sku: "NR40"
product_name: "NR40 - Casambi Bluetooth Zhaga 40 Sensor Module"
brand: "NR40"
manufacturer_part_number: "NR40"
hubspot_product_id: ""
website_url: ""
status: "active"

category_primary: "Sensors"
category_secondary: ["Zhaga Integration", "Light Control"]
protocols: ["Casambi", "Bluetooth", "0-10V"]

short_description_vi: "Module cảm biến Zhaga 40 với Casambi Bluetooth, thay thế cảm biến IR truyền thống, đo ánh sáng & nhiệt độ"
short_description_en: "Casambi Bluetooth Zhaga 40 sensor module with light & temperature sensors, replaces traditional IR sensors, 0-10V analog output"

aliases: ["NR40", "Zhaga 40 Sensor", "Casambi Sensor Module"]
search_keywords_vi: ["NR40", "Zhaga", "sensor", "ánh sáng", "Casambi", "Bluetooth", "cảm biến"]
search_keywords_en: ["NR40", "Zhaga 40", "sensor", "light", "Casambi", "Bluetooth"]

use_case_tags: ["light_sensor", "temperature_sensor", "zhaga_integration"]
target_segment: ["system_integrator", "luminaire_manufacturer"]
project_scale: ["small", "medium", "large"]
complexity_level: "beginner"
not_suitable_for: ["standalone_control"]

replaces_sku: []
replaced_by_sku: null
equivalent_skus: []
accessories_required: ["Casambi Network", "Luminaire with Zhaga 40 socket"]
accessories_recommended: []
bundle_with: []
upsell_to: []

casambi_network_type: ["all"]
casambi_pro_compatible: true
fixture_profile_default_id: "zhaga40_sensor"
fixture_profile_default_name: "Zhaga 40 Sensor"
fixture_profile_alternatives: []

pricing_visibility: "sales_only"
stock_visibility: "sales_only"
moq_hint: "Liên hệ sales"
warranty_months: 24
origin_country: "EU"
hs_code_vn: ""

images:
  main: ""
  connector: ""
  installation: ""
datasheet_url: ""
manual_url_en: ""
manual_url_vi: null

common_questions:
  - question_vi: "NR40 là gì?"
    answer_vi: "Module cảm biến Zhaga 40 hỗ trợ Casambi Bluetooth, thay thế cảm biến IR. Có cảm biến ánh sáng (Lux) và nhiệt độ"
  - question_vi: "Tương thích với những loại đèn nào?"
    answer_vi: "Bất kỳ đèn nào có socket Zhaga 40 (Zhaga Book 18). Yêu cầu driver LED 12-24VDC"
  - question_vi: "Cảm biến nào được hỗ trợ?"
    answer_vi: "Light sensor (đo Lux), Temperature sensor (an toàn 80-90°C). Tự động tắt nếu quá nóng"
  - question_vi: "Cài đặt có khó không?"
    answer_vi: "Rất đơn giản: Cắm vào socket Zhaga 40 → Pair với Casambi App → Cấu hình scene/automation"

handoff_to_sales_when:
  - "user_asks_price"
  - "user_asks_stock"
  - "user_asks_quotation"
  - "user_asks_lead_time"
  - "user_asks_bulk_order"

last_updated: "2026-04-21"
last_verified_by: "auto_converter"
content_version: "1.0"
source_of_truth: "ONOFF - NR40.md"
confidence_level: "high"
chatbot_priority: "medium"

chunk_strategy: "by_section"
priority_sections:
  - "Thông số kỹ thuật"
  - "Cài đặt"
  - "Cảm biến"
  - "FAQ"

---

# NR40 - Casambi Bluetooth Zhaga 40 Sensor Module

## Đặc điểm

✅ **Zhaga 40 Form Factor** - Plug & play, không cần dây thêm

✅ **Casambi Bluetooth Mesh** - CBM003B, 2.4GHz, repeater trong mạng

✅ **Dual Sensors** - Light sensor (Lux) + Temperature sensor

✅ **IP66 + IK09** - Dùng ngoài trời, chịu va đập

✅ **Thay thế cảm biến IR** - Module tích hợp, không chế dụng cổng cảm biến riêng

✅ **0-10V Output** - Tương thích với driver analog LED

## Thông số kỹ thuật

| Thông số | Giá trị |
|---------|--------|
| **Input** | 12-24VDC (SELV) |
| **Output** | 0-10V analog (Zhaga 40) |
| **Bluetooth** | CBM003B (Casambi Mesh) |
| **Tần số** | 2.4 GHz |
| **Công suất** | Máx 12W |
| **Tiêu thụ chờ** | <0.5mA |
| **Cảm biến** | Light (Lux), Temperature |
| **IP Protection** | IP66 |
| **IK Protection** | IK09 |
| **Connectors** | Zhaga 40 (4-pin, Book 18) |
| **Kích thước** | Ø48mm x 45mm |
| **Nhiệt độ** | -20~+70°C |
| **Certifications** | FCC, IC, CE, RoHS, RED, REACH |

## Cảm biến

### Light Sensor (Lux)

- Đo cường độ ánh sáng (Lux)
- Điều khiển tự động bật/tắt dựa trên light level
- Lập trình threshold từ Casambi App

### Temperature Sensor

- Đo nhiệt độ module
- Auto-shutdown nếu >80-90°C (bảo vệ)
- Hiển thị realtime trong App

## Cài đặt

### Bước 1: Lắp đặt cơ học

1. Tắt điện đèn
2. Cắm NR40 vào socket Zhaga 40 (không dùng lực)
3. Xoay nhẹ cho đến khi khóa
4. Cấp lại điện

### Bước 2: Pair với Casambi

1. Mở Casambi App, bật Bluetooth
2. Chờ NR40 xuất hiện trong "Available devices"
3. Thêm vào network
4. Cập nhật firmware nếu cần

### Bước 3: Cấu hình

**Điều khiển cơ bản:**
- Long press (2s): Điều chỉnh brightness realtime
- Double tap: Mở config panel (update, sensor values, delink)

**Scene & Automation:**
- Tạo scene trong App → Chọn NR40 → Cấu hình brightness
- Tạo schedule: bật/tắt theo giờ, dựa trên light/presence sensor

## Chế độ điều khiển

| Chế độ | Chi tiết |
|-------|---------|
| **Brightness** | 0-100% intensity, dimming smooth |
| **Manual ON/OFF** | Bật/tắt từ App |
| **Scenes** | Pre-defined scene với brightness cố định |
| **Schedules** | Timer theo giờ, sunset/sunrise |
| **Light sensor** | Auto dim dựa trên ambient light |
| **Circadian** | Điều chỉnh tự động theo nhịp sinh học |

## Lưu ý

⚠️ **Tắt điện trước khi cắm/tháo** - Tránh short circuit

⚠️ **Không cắm cứng** - Socket Zhaga phải smooth & aligned

⚠️ **Bluetooth signal** - Tránh metal structures (chặn sóng)

⚠️ **Auto shutdown >80-90°C** - Bình thường, bảo vệ module

⚠️ **Không có cáp thêm** - Zhaga 40 plug & play chỉ

## Ứng dụng

- **Nhà máy/Kho hàng:** Thay cảm biến IR, kiểm soát bật/tắt tự động
- **Ngoài trời:** IP66 & IK09, chịu thời tiết
- **Smart luminaire:** Tích hợp sensor vào đèn LED hiện đại
- **Scene control:** Pre-set brightness cho different areas

## Tài liệu

📄 **Manual (Spanish):** Included in packaging

## Bảo hành & Hỗ trợ

- **Bảo hành:** 24 tháng
- **Hỗ trợ:** knxstore.vn
- **Xuất xứ:** EU

---

⚠️ **URL không tìm thấy trong CSV.** Vui lòng cung cấp product URL để hoàn tất.
