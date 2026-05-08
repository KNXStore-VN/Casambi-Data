---
sku: "RUNNING-LIGHT-CASAMBI"
product_name: "DALCNET RUNNING-LIGHT-CASAMBI - SPI Pixel-to-Pixel LED Controller"
brand: "DALCNET"
manufacturer_part_number: "RUNNING-LIGHT-CASAMBI"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/bo-dieu-khien-led-pixel-spi-5-24v-casambi-running-light-casambi"
status: "active"

category_primary: "LED Controllers"
category_secondary: ["Addressable LED", "RGB Control", "RGBW Control", "Effect Generator"]
protocols: ["Casambi", "BLE", "SPI", "RS485"]

short_description_vi: "Bộ điều khiển SPI cho LED pixel-to-pixel RGB/RGBW/TW, 7A max, 8 effects, Casambi BLE"
short_description_en: "DALCNET SPI controller for addressable LED strips (RGB/RGBW/TW), 7A max output, 8 dynamic effects, Casambi Bluetooth"

aliases: ["RUNNING-LIGHT-CASAMBI", "SPI LED Controller", "Pixel LED Controller"]
search_keywords_vi: ["SPI", "pixel", "addressable", "LED", "RGB", "RGBW", "Casambi"]
search_keywords_en: ["SPI", "addressable LED", "pixel control", "RGB", "RGBW", "effect"]

use_case_tags: ["dynamic_effects", "color_control", "addressable_led"]
target_segment: ["system_integrator", "luminaire_designer"]
project_scale: ["small", "medium", "large"]
complexity_level: "advanced"
not_suitable_for: ["standard_dimming_only"]

replaces_sku: []
replaced_by_sku: null
equivalent_skus: []
accessories_required: ["5-12-24VDC SELV power supply", "Digital-LED strip (RGB/RGBW/TW)"]
accessories_recommended: ["PIXEL-REPEATER module", "Push button", "RS485 shielded cable"]
bundle_with: []
upsell_to: []

casambi_network_type: ["all"]
casambi_pro_compatible: true
fixture_profile_default_id: "multi_effect_rgb"
fixture_profile_default_name: "Multi Effect RGB (Default)"
fixture_profile_alternatives: ["Fill", "Fill-Partial", "Static", "Rainbow", "Wave", "Plasma", "Fire", "Horse Race"]

pricing_visibility: "sales_only"
stock_visibility: "sales_only"
moq_hint: "Liên hệ sales"
warranty_months: 60
origin_country: "Italy"
hs_code_vn: ""

images:
  main: ""
  effects: ""
  wiring: ""
datasheet_url: ""
manual_url_en: ""
manual_url_vi: null

common_questions:
  - question_vi: "RUNNING-LIGHT-CASAMBI là gì?"
    answer_vi: "Bộ điều khiển SPI cho LED addressable (pixel-to-pixel). Hỗ trợ RGB/RGBW/TW, 8 effects, điều khiển qua Casambi app"
  - question_vi: "Dòng tối đa bao nhiêu?"
    answer_vi: "7A max output (5-12-24VDC input). Size power supply theo load. Có OVP, UVP, reverse polarity protection"
  - question_vi: "Có bao nhiêu effect?"
    answer_vi: "8 effects: Fill, Fill-Partial, Static, Rainbow, Wave, Plasma, Fire, Horse Race. Mỗi effect fully customizable"
  - question_vi: "Điều khiển khoảng cách?"
    answer_vi: "Local: push button max 10m (relay cho >10m). Remote: Casambi BLE 10-50m. BUS Extender: 250m (RS485)"

handoff_to_sales_when:
  - "user_asks_price"
  - "user_asks_stock"
  - "user_asks_quotation"
  - "user_asks_custom_effect"

last_updated: "2026-04-21"
last_verified_by: "auto_converter"
content_version: "1.0"
source_of_truth: "SPECIAL - DALCNET RUNNING-LIGHT-CASAMBI.md"
confidence_level: "high"
chatbot_priority: "high"

chunk_strategy: "by_section"
priority_sections:
  - "Thông số kỹ thuật"
  - "Effects"
  - "Control Options"
  - "Compatible ICs"

---

# DALCNET RUNNING-LIGHT-CASAMBI - SPI Pixel-to-Pixel LED Controller

## Đặc điểm

✅ **8 Dynamic Effects** - Fill, Static, Rainbow, Wave, Plasma, Fire, Horse Race, Fill-Partial

✅ **RGB/RGBW/TW Support** - Full color control, tunable white (2700-6500K)

✅ **7A Max Output** - 5-12-24VDC input, up to 2000 pixel LEDs per strip

✅ **Casambi BLE Control** - Remote via app, local via push button

✅ **RS485 BUS Extender** - Control 2nd strip up to 250m away (PIXEL-REPEATER)

✅ **16 Million Colors** - Full RGB color palette, customizable animations

✅ **Protection** - OVP, UVP, reverse polarity, input fuse, thermal

## Thông số kỹ thuật

| Thông số | Giá trị |
|---------|--------|
| **Power Input** | 5-12-24VDC (SELV) |
| **Max Output Current** | 7A (depends on ambient temp) |
| **Output Voltage** | = Input voltage |
| **Digital-LED Type** | RGB, RGBW, Tunable White |
| **Max Pixels** | 2000 per strip |
| **IC Compatibility** | WS2811-2815, UCS1903-1904, TM1804-1903, SK6812 |
| **Color Resolution** | 16 million (8-bit per channel) |
| **Effects** | 8 (Fill, Static, Rainbow, Wave, Plasma, Fire, Horse Race, Multi) |
| **Local Control** | N.O. pushbutton (≤10m, or relay for longer) |
| **Remote Control** | Casambi BLE 2.4GHz, 10-50m typical |
| **BUS Extender** | RS485, up to 250m (PIXEL-REPEATER) |
| **Operating Temp** | -10°C to +60°C |
| **Protections** | IFP, OVP, UVP, RVP, thermal |
| **Dimensions** | Compact DIN-rail mount |
| **Warranty** | 5 years |

## 8 Dynamic Effects

| Effect | RGB | RGBW | TW | Customizable Parameters |
|--------|-----|------|-----|------------------------|
| **Multi Effect** | ✓ | ✓ | ✓ | Preview multiple effects, basic params |
| **Fill** | ✓ | ✓ | ✓ | Speed, direction, start point, color |
| **Fill-Partial** | ✓ | ✓ | ✓ | Sector length, direction, animation |
| **Static** | ✓ | ✓ | ✓ | Up to 8 color sectors, sequence |
| **Rainbow** | ✓ | ✓ | ✗ | Number of rainbows, sequence, direction |
| **Wave** | ✓ | ✓ | ✓ | Number of waves, speed, min level |
| **Plasma** | ✓ | ✓ | ✗ | Bubble animation, color, speed |
| **Fire** | ✓ | ✓ | ✗ | Flame direction, speed (SIDE A/B/A+B) |
| **Horse Race** | ✓ | ✓ | ✗ | Sector length, fade, speed, direction |

## Control Options

**Local:** Push button (toggle ON/OFF, dimming, scene cycling)  
**Remote:** Casambi app (full effect customization, scheduling)  
**Extended:** PIXEL-REPEATER module for 2nd strip (RS485 bus)

## Compatible IC LEDs

WS2811, WS2812, WS2812B, WS2813, WS2815, UCS1903, UCS1904, TM1804, TM1903, GS8206, SK6812, and others (refer to manual Table 5)

## Ứng dụng

- Dynamic color lighting installations
- Architectural accent lighting
- Interactive RGB/RGBW displays
- Tunable white pixel effects
- Event/entertainment lighting
- Custom animation scenarios

## Tài liệu

👉 [Trang sản phẩm RUNNING-LIGHT-CASAMBI](https://knxstore.vn/products/bo-dieu-khien-led-pixel-spi-5-24v-casambi-running-light-casambi)

## Bảo hành & Hỗ trợ

- **Bảo hành:** 5 năm
- **Hỗ trợ:** info@dalcnet.com, https://www.dalcnet.com
- **Xuất xứ:** Italy (DALCNET)
- **Certifications:** EN 55015, EN 61547, CE
