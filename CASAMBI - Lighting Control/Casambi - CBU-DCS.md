---
sku: "CBU-DCS"
product_name: "Casambi CBU-DCS - DALI Controller with Bluetooth"
brand: "Casambi"
manufacturer_part_number: "CBU-DCS"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs"
status: "active"

category_primary: "DALI Controllers"
category_secondary: []
protocols: ["CASAMBI", "DALI"]

short_description_vi: "Bộ điều khiển DALI Casambi nhỏ gọn với Bluetooth, cấp điện từ DALI bus, hỗ trợ cảm biến DALI và 50+ fixture profiles"
short_description_en: "Compact Casambi DALI controller with Bluetooth, powered directly from DALI bus, supports DALI sensors and 50+ fixture profiles"

aliases: ["CBU-DCS", "DALI Casambi Controller", "DCS"]
search_keywords_vi: ["Casambi", "DALI", "bộ điều khiển", "Bluetooth", "cảm biến", "daylight harvesting", "presence detection", "mesh network"]
search_keywords_en: ["Casambi", "DALI", "controller", "Bluetooth", "sensor", "daylight", "presence", "mesh"]

use_case_tags: ["dali_control", "sensor_integration", "presence_detection", "daylight_harvesting"]
target_segment: ["system_integrator", "smart_home_diy"]
project_scale: ["small", "medium", "large"]
complexity_level: "intermediate"
not_suitable_for: ["non_dali_systems", "standalone_operation_without_dali_bus"]

replaces_sku: []
replaced_by_sku: null
equivalent_skus: []
accessories_required: []
accessories_recommended: []
bundle_with: []
upsell_to: []

casambi_network_type: ["standard", "mesh"]
casambi_pro_compatible: true
fixture_profile_default_id: "8079"
fixture_profile_default_name: "Broadcast"
fixture_profile_alternatives: ["1CH", "1CH + Sensors", "2CH Dim Mixer", "2CH TW", "4xDim", "8CH", "BC+Sensors", "DALI8/Dim,TW", "DALI8/Dim,RGB", "DALI8/Dim,RGBW", "DALI8/Dim,XY"]

pricing_visibility: "sales_only"
stock_visibility: "sales_only"
moq_hint: "Liên hệ sales để biết MOQ và bậc giá theo số lượng"
warranty_months: 24
origin_country: "Finland"
hs_code_vn: ""

images:
  main: ""
  wiring: ""
  dimensions: ""
datasheet_url: ""
manual_url_en: "https://www.casambi.com"
manual_url_vi: null

common_questions:
  - question_vi: "CBU-DCS có cần power supply riêng không?"
    answer_vi: "Không, CBU-DCS cấp điện trực tiếp từ DALI bus (9.5-22.5VDC). Tuy nhiên, DALI bus phải được cấp điện bên ngoài hoặc từ driver LED/cảm biến DALI có power supply tích hợp"
  - question_vi: "Điện từ DALI bus có đủ để CBU-DCS hoạt động không?"
    answer_vi: "Có, CBU-DCS chỉ tiêu thụ 5mA ở chế độ idle và 30mA peak, tối đa 250mA từ DALI bus - rất tiết kiệm"
  - question_vi: "CBU-DCS có thể điều khiển bao nhiêu DALI device?"
    answer_vi: "CBU-DCS có thể điều khiển tối đa 64 DALI address (0-63). Phạm vi điều khiển tùy thuộc vào cấu hình Fixture Profile"
  - question_vi: "Cảm biến DALI (presence/daylight) có tương thích không?"
    answer_vi: "Có, CBU-DCS hỗ trợ DALI sensor cho presence detection (phát hiện người) và daylight harvesting (tối ưu ánh sáng). Cảm biến phải là DALI controllable hoặc có DALI power supply tích hợp"
  - question_vi: "Phạm vi Bluetooth của CBU-DCS là bao xa?"
    answer_vi: "Tối đa 50m trong không gian mở thoáng. Với vật cản (tường, vật liệu), phạm vi giảm xuống ~30m. Casambi mesh network giúp mở rộng phạm vi qua repeater"

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
source_of_truth: "DALI - Casambi CBU-DCS.md"
confidence_level: "high"
chatbot_priority: "high"

chunk_strategy: "by_section"
priority_sections:
  - "Thông số kỹ thuật"
  - "Sơ đồ nối dây"
  - "Profile Casambi"
  - "Ứng dụng"
  - "FAQ"

---

# Casambi CBU-DCS - Bộ Điều Khiển DALI với Bluetooth

## Đặc điểm nổi bật

✅ **Cấp điện từ DALI bus** - Không cần power supply riêng, tiêu thụ điện cực thấp (5mA idle)

✅ **Bluetooth Casambi** - Điều khiển qua app, mesh network tự động tối đa 250 units

✅ **Hỗ trợ DALI sensor** - Presence detection & daylight harvesting tích hợp

✅ **Kích thước siêu nhỏ** - 40.4 × 36.3 × 14 mm, chỉ 15g

✅ **50+ Fixture profiles** - 1CH, 2CH TW, RGB, RGBW, broadcast, sensor modes

✅ **2 kết nối DALI song song** - DALI bus có thể xuyên qua thiết bị

✅ **IP20 Reinforced insulation** - Cách ly tăng cường giữa vỏ và DALI

✅ **Mesh repeater** - Mỗi unit là repeater, mở rộng phạm vi tự động

## Thông số kỹ thuật

### Nguồn - DALI Bus

| Thông số | Giá trị |
|---------|--------|
| Phạm vi điện áp | 9.5-22.5 VDC (from DALI bus) |
| Dòng idle | 5 mA |
| Dòng peak | 30 mA |
| Max DALI bus current | 250 mA |
| Standby power | <0.1 W |

### Casambi (Bluetooth)

| Thông số | Giá trị |
|---------|--------|
| Tần số hoạt động | 2400-2480 MHz |
| Công suất phát tối đa | +4 dBm |
| Phạm vi ngoài trời | Tối đa 50m |
| Phạm vi với vật cản | ~30m |
| Network | Mesh - mỗi unit là repeater |

### Kết nối dây

| Thông số | Giá trị |
|---------|--------|
| Tiết diện dây | 0.5-1.5 mm² (solid) / 16-20 AWG |
| Chiều dài tuốt dây | 6-8 mm |
| Connector type | Push-button press terminal |
| Cấu hình | 2 sets DALI terminals (internally parallel) |

### Điều kiện môi trường

| Thông số | Giá trị |
|---------|--------|
| Nhiệt độ hoạt động | -20°C đến +55°C |
| Nhiệt độ vỏ tối đa (Tc) | +65°C |
| Nhiệt độ lưu kho | -25°C đến +75°C |
| Độ ẩm tối đa | 0-80% không kết tụ |
| IP Protection | IP20 (dùng trong nhà) |

### Kỹ thuật cơ học

| Thông số | Giá trị |
|---------|--------|
| Kích thước | 40.4 × 36.3 × 14.0 mm |
| Trọng lượng | 15g |
| Insulation | Reinforced (casing to DALI) |
| Lỗ lắp đặt | Ø 3.5 mm |

### Chứng chỉ

- EU WEEE Directive 2002/96/EC compliant
- Casambi certified

## Fixture Profiles

### DALI Sensor Profiles

| Profile | Mô tả |
|---------|-------|
| Sensors (Daylight, Presence) | Presence & daylight sensing, pass-through mode |
| Sensors (daylight control) | Daylight control only, pass-through mode |
| Sensors (Lux, Presence) | Presence & lux sensing, pass-through mode |

### DALI Dimmer Profiles

| Profile | Mô tả | Ghi chú |
|---------|-------|---------|
| **1CH** | Basic 1-channel DALI dimmer | Address #0 |
| 1CH + Sensors | 1-channel dimmer + sensors | Address #0 |
| 2CH Dim Mixer | 2-channel dimmer with ratio | Tổng = mức sáng |
| 2CH TW | 2-channel warm/cool mixer | Tunable White |
| 4xDim | 4-channel DALI dimmer | Addresses #0-3 |
| 8CH [Evo] | 8-channel with custom elements | Evolution |
| **8079** (Default) | Broadcast DALI dimmer | No addressing needed |

### DALI DT8 Profiles (Color)

| Profile | Mô tả |
|---------|-------|
| DALI8/Dim,TW | DT8 Tunable White (driver does warm/cool mix) |
| DALI8/Dim[WarmCool] | Single dimmer + color temp control |
| DALI8/Dim,RGB | 3-channel RGB RGBWAF input |
| DALI8/Dim,RGBW | 4-channel RGBW RGBWAF input |
| DALI8/Dim,RGB,TW | RGB hoặc TC loại trừ lẫn nhau |
| DALI8/Dim,XY [Evolution] | Multichannel XY color type |
| DALI8/Dim,XY,TW [Evolution] | XY color + temperature |
| DALI PushButton Coupler [Evolution] | Scene selection + light regulation |

## Sơ đồ nối dây

### Mode: DALI Sensor

```
DALI Bus (9.5-22.5VDC) ──┬── CBU-DCS (DA1/DA2)
                         └── DALI Sensor
                         └── Control signal output to Casambi App
```

### Mode: DALI Driver (with integrated DALI power)

```
DALI Bus ──┬── CBU-DCS
           └── DALI LED Driver (with integrated DALI power supply)
           
CBU-DCS điều khiển driver qua DALI, cơ chế dimming tùy thuộc Fixture Profile
```

**Lưu ý:**
- Polarity của DA1/DA2 không quan trọng (bất cứ hướng nào cũng được)
- 2 connector DALI nối song song trong thiết bị → DALI bus có thể xuyên qua
- Chỉ cấu hình solid conductor 0.5-1.5mm², tuốt 6-8mm

## Lắp đặt & Chú ý

⚠️ **An toàn:**
- Chỉ chuyên gia mới nối dây
- DALI bus phải được cấp điện bên ngoài hoặc từ driver/sensor có power supply tích hợp
- Không đặt trong vỏ kim loại (chặn Bluetooth)
- Test kỹ độ phủ sóng sau lắp đặt

✅ **Đặc tính:**
- CBU-DCS chỉ tiêu thụ 5mA ở idle, không gây tải cho DALI bus
- Hỗ trợ DALI broadcast (không cần addressing) hoặc short address (0-63)
- Mesh network tự động: mỗi CBU-DCS là repeater

## Ứng dụng

**Văn phòng:** Kết hợp DALI sensor cho daylight harvesting + presence detection → tối ưu năng lượng

**Bảo tàng/Gallery:** DALI DT8 RGB/TW profiles → điều khiển ánh sáng màu sắc chính xác

**Khách sạn:** Multiple CBU-DCS + sensor → tự động tắt đèn khi không có người, điều chỉnh theo thời gian

**Công trình công cộng:** Broadcast mode → điều khiển toàn bộ DALI system không cần địa chỉ

## Sản phẩm tương thích

**Bắt buộc:**
- DALI driver hoặc DALI sensor
- Casambi App (iOS 10+ / Android 4.4+)

**Khuyến nghị:**
- DALI sensor có DALI power supply tích hợp
- Cấu hình Fixture Profile phù hợp với DALI device

## Tài liệu kỹ thuật

📄 **Tài liệu chi tiết:**

👉 [Trang sản phẩm CBU-DCS](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs)

👉 [Hướng dẫn Casambi](https://www.casambi.com)

## Bảo hành & Hỗ trợ

- **Bảo hành:** 24 tháng
- **Hỗ trợ:** knxstore.vn
- **Xuất xứ:** Finland (Casambi Technologies Oy)

---

**Ghi chú:** CBU-DCS là lựa chọn tối ưu cho hệ thống DALI nhỏ đến trung bình. Để hệ thống DALI lớn hơn (50+ devices), xem xét CBU-ASD hoặc CBU-DA-1P.
