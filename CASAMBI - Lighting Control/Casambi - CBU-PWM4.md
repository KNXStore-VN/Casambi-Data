---
sku: "CBU-PWM4"
product_name: "Casambi CBU-PWM4 - 4 Channel PWM Dimmer"
brand: "Casambi"
manufacturer_part_number: "CBU-PWM4"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/casambi-bo-dieu-khien-chieu-sang-rgbw-tunable-white-bluetooth-cbu-pwm4"
status: "active"

category_primary: "LED Strip Controllers"
category_secondary: []
protocols: ["CASAMBI", "PWM"]

short_description_vi: "Bộ điều khiển PWM 4 kênh Casambi cho dải LED hằng áp 12-24VDC, hỗ trợ RGBW/RGB/Tunable White, max 6A tổng công suất"
short_description_en: "Casambi 4-channel PWM dimmer for 12-24VDC constant voltage LED strips, supports RGBW/RGB/TW, max 6A total output"

aliases: ["CBU-PWM4", "PWM Dimmer", "RGBW Controller"]
search_keywords_vi: ["Casambi", "PWM", "LED strip", "RGBW", "RGB", "Tunable White", "4 kênh", "Bluetooth", "dimmer"]
search_keywords_en: ["Casambi", "PWM", "LED strip", "RGBW", "RGB", "tunable white", "4 channel", "Bluetooth", "dimmer"]

use_case_tags: ["led_strip_control", "rgbw_lighting", "color_control", "tunable_white"]
target_segment: ["system_integrator", "smart_home_diy"]
project_scale: ["small", "medium"]
complexity_level: "beginner"
not_suitable_for: ["high_power_led", "constant_current_drivers", "ac_led"]

replaces_sku: []
replaced_by_sku: null
equivalent_skus: []
accessories_required: []
accessories_recommended: []
bundle_with: []
upsell_to: []

casambi_network_type: ["standard", "mesh"]
casambi_pro_compatible: true
fixture_profile_default_id: "4027"
fixture_profile_default_name: "RGBW"
fixture_profile_alternatives: ["1xDIM", "2xDIM", "3xDIM", "4xDIM", "RGB", "RGB 625Hz", "RGB/White", "Sliders/RGBW", "TW", "TW (WW-CW dimmer)", "3CH (White, Cold, Warm)"]

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
  - question_vi: "CBU-PWM4 có thể điều khiển bao nhiêu LED strip?"
    answer_vi: "4 kênh độc lập, tối đa 6A tổng cộng. Có thể chia đều hoặc tùy cụm (VD: 2A + 2A + 1A + 1A)"
  - question_vi: "Hỗ trợ những loại LED strip nào?"
    answer_vi: "Chỉ hỗ trợ LED strip hằng áp (constant voltage) 12-24VDC. KHÔNG hỗ trợ constant current drivers"
  - question_vi: "Có thể dùng cho RGB + White (RGBW) không?"
    answer_vi: "Có, RGBW là profile mặc định. Có thể điều khiển 3-channel RGB + 1-channel White, hoặc custom ratio bằng mixer"
  - question_vi: "Tunable White (TW) là gì?"
    answer_vi: "Tunable White dùng 2 kênh: warm (2700K) + cool (6000K). CBU-PWM4 hỗ trợ profile 'TW' để điều khiển màu sắc nhiệt độ"
  - question_vi: "Có bảo vệ chống lỗi không?"
    answer_vi: "Có bảo vệ chống quá áp, quá dòng, short circuit. NHƯNG KHÔNG bảo vệ chống đảo cực - phải nối đúng polarity"

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
source_of_truth: "DIMMER - Casambi CBU-PWM4.md"
confidence_level: "high"
chatbot_priority: "high"

chunk_strategy: "by_section"
priority_sections:
  - "Thông số kỹ thuật"
  - "Fixture Profiles"
  - "Sơ đồ nối dây"
  - "Ứng dụng"
  - "FAQ"

---

# Casambi CBU-PWM4 - 4 Channel PWM Dimmer

## Đặc điểm nổi bật

✅ **4 kênh PWM độc lập** - Điều khiển RGBW, RGB, TW hoặc 1-4 channels riêng biệt

✅ **Max 6A output** - Linh hoạt chia đều hoặc theo nhu cầu (VD: 2A + 2A + 1A + 1A)

✅ **12-24VDC constant voltage** - Tương thích rộng với LED strips thương mại

✅ **Bluetooth Casambi** - App control, mesh network, tối đa 250 units

✅ **10+ fixture profiles** - RGBW, RGB, TW, 1-4 DIM, RGB/White, 3CH...

✅ **PWM dimming** - Smooth, flicker-free dimming (Pulse Width Modulation)

✅ **Compact size** - 72.6 x 30 x 18 mm, dễ tích hợp vào enclosure

✅ **Bảo vệ tích hợp** - Overvoltage, overcurrent, short circuit protection

## Thông số kỹ thuật

### Đầu vào

| Thông số | Giá trị |
|---------|--------|
| Điện áp vào | 12-24 VDC |
| Dòng vào tối đa | 6 A |
| Tiêu thụ chờ | <0.3 W |

### Đầu ra

| Thông số | Giá trị |
|---------|--------|
| Điện áp ra | Same as input (12-24VDC) |
| Công suất tối đa | 144 W @ 24VDC, 72 W @ 12VDC |
| Dòng ra tối đa | 6 A (chia tự do giữa 4 kênh) |
| Số kênh | 4 (independently PWM controlled) |
| Phương pháp dimming | PWM (Pulse Width Modulation) |
| Tải tối thiểu | 0 W (no minimum load required) |

### Kết nối

| Thông số | Giá trị |
|---------|--------|
| Tiết diện dây | 0.75-1.5 mm² (solid & stranded) / 14-22 AWG |
| Chiều dài tuốt dây | 6-7 mm |
| Mô men siết | 0.4 Nm |
| Dây vào tối đa | 3 m |
| Dây tải khuyến nghị | Max 3 m |

### Casambi (Bluetooth)

| Thông số | Giá trị |
|---------|--------|
| Tần số hoạt động | 2400-2480 MHz |
| Công suất phát tối đa | +4 dBm |
| Phạm vi | Tối đa 50m ngoài trời, 30m trong nhà (mesh network) |
| Network | Mesh support, mỗi unit là repeater |

### Điều kiện môi trường

| Thông số | Giá trị |
|---------|--------|
| Nhiệt độ hoạt động | -20°C đến +45°C |
| Nhiệt độ vỏ tối đa (Tc) | +75°C |
| Nhiệt độ lưu kho | -25°C đến +75°C |
| Độ ẩm tối đa | 0-80% không kết tụ |
| IP Protection | IP20 (indoor use only) |

### Kỹ thuật cơ học

| Thông số | Giá trị |
|---------|--------|
| Kích thước | 72.6 x 30.0 x 18.0 mm |
| Trọng lượng | 23g |
| Certifications | Casambi certified |

## Fixture Profiles

### Basic Dimming Profiles

| Profile | Mô tả | Channels |
|---------|-------|----------|
| **1xDIM** | 1 kênh dimmer cơ bản | CH1 |
| 2xDIM | 2 kênh dimmer độc lập | CH1, CH2 |
| 3xDIM | 3 kênh dimmer | CH1, CH2, CH3 |
| 4xDIM | 4 kênh dimmer | CH1-CH4 |

### Color Profiles

| Profile | Mô tả | Channels | Ghi chú |
|---------|-------|----------|---------|
| **RGBW** (Default) | 4-channel RGBW with mixer | R, G, B, W | Tỷ lệ RGB/White tunable |
| RGB | 3-channel RGB | R, G, B | Basic RGB |
| RGB 625Hz | 3-channel RGB (625Hz PWM) | R, G, B | Higher frequency |
| RGB/White | RGB + White fixture | R, G, B, W | RGB always present |
| Sliders/RGBW | RGBW with custom sliders | R, G, B, W | Custom elements control |

### Tunable White Profiles

| Profile | Mô tả | Channels |
|---------|-------|----------|
| **TW** | 2-channel warm/cool mixer | Warm (2700K), Cool (6000K) |
| TW (WW-CW dimmer) | Single dimmer + color temp | WW + CW channels |
| 3CH (White, Cold, Warm) | 3-channel tunable white | White, Cold, Warm |

## Sơ đồ nối dây

### RGBW LED Strip

```
12-24VDC Power Supply
        ↓
    CBU-PWM4
    ├─ + (Common positive)
    ├─ 1: Red (-)
    ├─ 2: Green (-)
    ├─ 3: Blue (-)
    └─ 4: White (-)
        ↓
    RGBW LED Strip
```

### Tunable White LED Strip

```
12-24VDC Power Supply
        ↓
    CBU-PWM4
    ├─ + (Common positive)
    ├─ 1: Warm (-) [2700K]
    └─ 2: Cool (-) [6000K]
        ↓
    TW LED Strip
```

### 4 Independent Channels

```
12-24VDC Power Supply
        ↓
    CBU-PWM4
    ├─ + (Common)
    ├─ 1: CH1 (-)
    ├─ 2: CH2 (-)
    ├─ 3: CH3 (-)
    └─ 4: CH4 (-)
        ↓
    4 separate LED loads
```

**Lưu ý:**
- ✅ CORRECT: (+) chung, mỗi kênh (-) riêng biệt (Anode common)
- ❌ WRONG: Đảo polarity → Hư hỏng LED strip vĩnh viễn
- ⚠️ NO: Không có bảo vệ chống đảo cực

## Lắp đặt & Cấu hình

### Wiring Steps

1. **Power supply** (12-24VDC Class 2) → CBU-PWM4 input
2. **LED strip common (+)** → CBU-PWM4 (+)
3. **LED strip channels (-)** → CBU-PWM4 outputs (1-4)
4. **Verify polarity** trước khi cấp điện

### Configuration via Casambi App

1. **Default:** RGBW profile
2. **Change profile:** 
   - Mở Casambi App
   - Tìm "CBU-PWM4"
   - Select "Fixture profile"
   - Chọn profile mong muốn (RGB, TW, 1-4 DIM, etc.)

## Lưu ý quan trọng

⚠️ **Chỉ Constant Voltage:**
- Tương thích **CHỈ** với LED strip hằng áp 12-24VDC
- KHÔNG dùng với constant current drivers
- KHÔNG dùng với AC LED

⚠️ **Đảo Cực:**
- CBU-PWM4 **KHÔNG** bảo vệ chống đảo cực
- Đảo polarity → Hư hỏng LED strip **vĩnh viễn**
- Kiểm tra kỹ trước khi cấp điện

⚠️ **Không đặt trong kim loại:**
- Tránh đặt trong vỏ kim loại (chặn Bluetooth)
- Nếu phải đặt → Cắt khe mở xung quanh antenna

✅ **Bảo vệ tích hợp:**
- Overvoltage, overcurrent, short circuit protection
- Thermal protection (case temp max +75°C)

## Ứng dụng

**Trang trí nhà:** 1-2 RGBW strips → Điều khiển toàn bộ từ app, tạo ambience

**Văn phòng:** 2 TW strips (warm + cool) → Điều chỉnh màu sắc theo giờ làm việc

**Bảo tàng/Retail:** 4 independent channels → Spotlight các vùng, tạo scene

**Karaoke/Bar:** RGBW profiles → Preset color scenes, dynamic lighting effects

**Sân khấu:** Multiple CBU-PWM4 + app → Synchronized color control, mesh network

## Sản phẩm tương thích

**Bắt buộc:**
- LED strip hằng áp 12-24VDC (RGBW / RGB / TW)
- 12-24VDC Class 2 power supply (dòng đủ để cấp cho LED strip)
- Casambi App (iOS 10+ / Android 4.4+)

**Khuyến nghị:**
- Power supply dòng ≥ (LED strip rated current)
- Dây nối ≤ 3m (để tránh voltage drop)
- Kabel tiếp địa nếu dây rất dài

## Tài liệu kỹ thuật

📄 **Tài liệu chi tiết:**

👉 [Trang sản phẩm CBU-PWM4](https://knxstore.vn/products/casambi-bo-dieu-khien-chieu-sang-rgbw-tunable-white-bluetooth-cbu-pwm4)

👉 [Hướng dẫn Casambi](https://www.casambi.com)

## Bảo hành & Hỗ trợ

- **Bảo hành:** 24 tháng
- **Hỗ trợ:** knxstore.vn
- **Xuất xứ:** Finland (Casambi Technologies Oy)

---

**Ghi chú:** CBU-PWM4 là lựa chọn tối ưu cho các ứng dụng LED strip RGBW, RGB, tunable white. Dễ lắp đặt, nhiều profile, hỗ trợ mesh network. Phù hợp cho DIY, smart home, retail, sân khấu.
