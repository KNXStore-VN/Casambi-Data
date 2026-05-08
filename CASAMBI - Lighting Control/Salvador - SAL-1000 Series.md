---
sku: "SAL-1000 Series"
product_name: "Salvador SAL-1000 Series - DALI Master Controller for Casambi"
brand: "Salvador"
manufacturer_part_number: "SAL-1016 / SAL-1032 / SAL-1064"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/bo-dieu-khien-32-dia-chi-driver-dali-master-salvador-casambi-sal-1032"
status: "active"

category_primary: "DALI Master Controllers"
category_secondary: []
protocols: ["DALI", "CASAMBI", "D4i", "DT6", "DT8"]

short_description_vi: "Bộ điều khiển DALI Master Casambi Salvador Series với 3 phiên bản (16/32/64 địa chỉ), tích hợp mạng lưới DALI dây vào hệ thống Casambi không dây"
short_description_en: "Salvador Series 1000 DALI Master Controller for Casambi with 3 variants (16/32/64 addresses), integrates wired DALI networks into wireless Casambi mesh"

aliases: ["SAL-1000", "SAL-1016", "SAL-1032", "SAL-1064", "Salvador DALI"]
search_keywords_vi: ["DALI master", "Casambi", "16 địa chỉ", "32 địa chỉ", "64 địa chỉ", "hybrid network", "DALI Evolution", "wired DALI", "wireless Casambi"]
search_keywords_en: ["DALI master", "Casambi", "16 address", "32 address", "64 address", "Salvador", "hybrid", "DALI DT8", "mesh network"]

use_case_tags: ["dali_integration", "hybrid_network", "dali_master", "lighting_control", "wired_wireless_bridge"]
target_segment: ["system_integrator", "lighting_designer"]
project_scale: ["medium", "large"]
complexity_level: "advanced"
not_suitable_for: ["dali_controls_switches_sensors", "non_evolution_networks"]

replaces_sku: []
replaced_by_sku: null
equivalent_skus: ["SAL-1016", "SAL-1032", "SAL-1064"]
accessories_required: []
accessories_recommended: []
bundle_with: []
upsell_to: []

casambi_network_type: ["evolution"]
casambi_pro_compatible: true
fixture_profile_default_id: "1064"
fixture_profile_default_name: "Salvador 1000 Generic"
fixture_profile_alternatives: []

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
  - question_vi: "Có bao nhiêu model Salvador SAL-1000?"
    answer_vi: "Có 3 model: SAL-1016 (16 addresses), SAL-1032 (32 addresses), SAL-1064 (64 addresses - maximum DALI)"
  - question_vi: "Salvador có thể điều khiển bao nhiêu driver DALI?"
    answer_vi: "SAL-1016 tối đa 16, SAL-1032 tối đa 32, SAL-1064 tối đa 64 driver DALI. Có thể dùng multiple Salvadors trong một mạng (tối đa 250 nodes)"
  - question_vi: "Có cần DALI power supply riêng không?"
    answer_vi: "Có, Salvador cấp điện từ DALI bus (9.5-22.5VDC bên ngoài). Nếu chỉ dùng drivers có power supply tích hợp, vẫn cần cấp điện cho bus"
  - question_vi: "Salvador có hỗ trợ DALI sensor không?"
    answer_vi: "Không, chỉ có thể kết nối DALI drivers. DALI controls (switches, sensors) phải được chuyển đổi thành Casambi Ready bằng CBU hoặc devices khác"
  - question_vi: "Phạm vi Bluetooth của Salvador là bao xa?"
    answer_vi: "Tối đa 50m trong nhà, lên tới 200m ngoài trời (trong long-range mode). Casambi mesh network mở rộng phạm vi qua repeater"

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
source_of_truth: "DALI - Salvador SAL-1000 Series.md"
confidence_level: "high"
chatbot_priority: "high"

chunk_strategy: "by_section"
priority_sections:
  - "Thông số kỹ thuật"
  - "Các model"
  - "Sơ đồ nối dây"
  - "Ứng dụng"
  - "FAQ"

---

# Salvador SAL-1000 Series - DALI Master Controller for Casambi

## Đặc điểm nổi bật

✅ **Tích hợp DALI vào Casambi mesh** - Chuyển đổi wired DALI thành wireless Casambi Evolution

✅ **3 phiên bản linh hoạt** - 16/32/64 địa chỉ DALI tùy nhu cầu dự án

✅ **Hỗ trợ DALI D4i, DT6, DT8** - Tương thích toàn bộ tiêu chuẩn DALI hiện đại

✅ **Hybrid network** - Kết hợp DALI drivers với Casambi Ready devices trong 1 hệ thống

✅ **Cấp điện từ DALI bus** - Tiêu thụ cực thấp (5mA idle, 30mA peak), không cần power riêng

✅ **Casambi Evolution exclusive** - Chỉ hỗ trợ Casambi Evolution networks

✅ **Multiple Salvador support** - Có thể dùng multiple Salvadors (tối đa 250 nodes total)

✅ **Mesh repeater** - Mỗi Salvador là repeater, mở rộng coverage tự động

## Các Model Khả Dụng

| Model | DALI Addresses | Ứng dụng |
|-------|----------------|---------|
| **SAL-1016** | 16 | Dự án nhỏ, renovations, thay thế standalone DALI |
| **SAL-1032** | 32 | Dự án vừa, văn phòng, khách sạn |
| **SAL-1064** | 64 | Dự án lớn, DALI network lớn, maximum DALI addresses |

**Chọn model dựa vào số driver DALI cần điều khiển. Không thể vượt quá limit của từng model trong discovery process.**

## Thông số kỹ thuật

### Nguồn - DALI Bus

| Thông số | Giá trị |
|---------|--------|
| Phạm vi điện áp | 9.5-22.5 VDC (from external DALI power supply) |
| Dòng idle | 5 mA |
| Dòng peak | 30 mA |
| Max DALI bus current | 250 mA ⚠️ (tổng từ tất cả power supplies) |
| Standby power | <0.2 W |

### DALI Output

| Thông số | Giá trị |
|---------|--------|
| SAL-1016 | 16 DALI addresses (0-15) |
| SAL-1032 | 32 DALI addresses (0-31) |
| SAL-1064 | 64 DALI addresses (0-63) - Maximum DALI |
| Tiêu chuẩn hỗ trợ | DALI D4i, DT6, DT8 |

### Casambi (Bluetooth)

| Thông số | Giá trị |
|---------|--------|
| Tần số hoạt động | 2402-2480 MHz |
| Công suất phát tối đa | +8 dBm |
| Phạm vi trong nhà | Tối đa 50m |
| Phạm vi ngoài trời | Tối đa 200m (long-range mode) |
| Network type | Casambi Evolution only |
| Radio modes | Balanced, Better Performance, Long Range |
| Mesh repeater | Có |

### Kết nối dây

| Thông số | Giá trị |
|---------|--------|
| Tiết diện dây | 0.5-1.5 mm² (solid) / 16-20 AWG |
| Chiều dài tuốt dây | 6-8 mm |
| Connector type | Push-button press terminal |
| Cấu hình | 2 sets DALI terminals (internally parallel) |
| Polarity | DA1/DA2 không quan trọng (bất cứ hướng nào) |

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

- CE (EU)
- WEEE Directive 2002/96/EC compliant
- Casambi certified

## Ứng dụng

**Văn phòng:** SAL-1032 + DALI drivers → Tunable white, dimming, scene control qua Casambi app

**Khách sạn:** Multiple SAL-1032 tại các tầng → Hybrid network centralized qua Casambi Cloud

**Bảo tàng/Gallery:** SAL-1064 + DALI DT8 RGB drivers → Điều khiển màu sắc chính xác, tạo ambience

**Công trình công cộng:** SAL-1064 → Thay thế legacy DALI system, nâng cấp lên wireless Casambi

**Renovations:** SAL-1016 → Kết nối wired DALI cũ vào new Casambi mesh, tiết kiệm cost

## Lưu ý quan trọng

⚠️ **DALI Bus Design:**
- Tổng dòng từ tất cả DALI power supplies không được vượt quá 250mA
- Vượt limit → malfunction hoặc permanent damage

⚠️ **Chỉ DALI Drivers, Không DALI Controls:**
- Chỉ kết nối **DALI drivers** (luminaires)
- **KHÔNG kết nối** DALI controls (switches, sensors)
- Nếu cần DALI sensors → Phải convert thành Casambi Ready (dùng CBU)

⚠️ **Casambi Evolution Only:**
- Salvador Series 1000 chỉ hỗ trợ **Casambi Evolution networks** (không phải Classic)

✅ **Hybrid Network:**
- Wired DALI drivers và Casambi Ready devices có thể hoạt động trong 1 mesh network
- DALI luminaires appear like Casambi luminaires trong app
- Tối đa 250 nodes (Salvadors + DALI drivers + Casambi devices)

✅ **Multiple Salvadors:**
- Có thể wireless kết nối multiple Salvadors (mỗi = 1 node)
- Mỗi addressed DALI driver = 1 additional node
- Total = tối đa 250 nodes

## Sơ đồ nối dây

### Basic: DALI Bus → Salvador → Casambi App

```
External DALI Power Supply (9.5-22.5VDC, ≤250mA)
        ↓
DALI Bus (DA1/DA2)
        ├─ Salvador SAL-1016/32/64 ← Casambi App (Wireless)
        └─ DALI Drivers (16/32/64 addresses)
```

**Lưu ý:**
- 2 connector sets song song → DALI bus xuyên qua Salvador
- Polarity DA1/DA2 không quan trọng
- Solid 0.5-1.5mm², tuốt 6-8mm

## Lắp đặt & Test

1. **Kết nối DALI bus** từ external power supply qua Salvador (2 connector sets parallel)
2. **Kết nối DALI drivers** vào bus (2 kênh DA1/DA2)
3. **Mở Casambi App** → Discovery → Chọn Salvador model
4. **Auto-discovery** → Nhận diện tất cả DALI drivers
5. **Addressing** → App tự assign addresses (không cần DALI tool)
6. **Test connectivity** → Ensure good mesh coverage

⚠️ **Không được kết nối:**
- DALI switches, sensors, controls → phải convert thành Casambi Ready

## Sản phẩm tương thích

**Bắt buộc:**
- DALI drivers (luminaires) với DALI interface
- Casambi App (iOS 10+ / Android OS latest + 2 major versions)
- External DALI power supply (9.5-22.5VDC, ≤250mA)

**Khuyến nghị:**
- Nếu dùng DALI sensors → CBU (để convert thành Casambi Ready)
- Multiple Salvadors nếu >64 drivers cần điều khiển

## Fixture Profile

| Profile# | Tên | Mô tả |
|----------|-----|-------|
| **1064** (Default) | Salvador 1000 Generic | Cho SAL-1016, SAL-1032, SAL-1064 |

## Tài liệu kỹ thuật

📄 **Tài liệu chi tiết:**

👉 [SAL-1032 (32 addresses)](https://knxstore.vn/products/bo-dieu-khien-32-dia-chi-driver-dali-master-salvador-casambi-sal-1032)

👉 [SAL-1016 (16 addresses)](https://knxstore.vn/products/bo-dieu-khien-16-dia-chi-driver-dali-master-salvador-casambi-sal-1016)

👉 [Hướng dẫn Casambi](https://www.casambi.com)

## Bảo hành & Hỗ trợ

- **Bảo hành:** 24 tháng
- **Hỗ trợ:** knxstore.vn
- **Xuất xứ:** Finland (Casambi Technologies Oy)

---

**Ghi chú:** Salvador Series 1000 là giải pháp tối ưu để nâng cấp legacy DALI systems lên Casambi Evolution wireless mesh. Phù hợp cho hybrid networks có cả drivers dây và devices không dây.
