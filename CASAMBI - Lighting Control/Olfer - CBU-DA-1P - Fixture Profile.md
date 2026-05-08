---
# === IDENTIFICATION ===
sku: "CBU-DA-1P"
product_name: "Olfer CBU-DA-1P - Fixture Profiles Reference"
brand: "Olfer"
manufacturer_part_number: "CBU-DA-1P"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p"
status: "active"

# === CLASSIFICATION ===
category_primary: "DALI Controllers"
category_secondary: ["Fixture Profiles", "Lighting Control", "Casambi"]
protocols: ["CASAMBI", "DALI", "BLE"]

# === SHORT DESCRIPTION ===
short_description_vi: "Tài liệu tham chiếu đầy đủ các Fixture Profile của bộ điều khiển DALI Casambi Olfer CBU-DA-1P, bao gồm DT6, DT8, Broadcast, Short Address, Tunable White, RGB/RGBW và các chế độ cảm biến mở rộng."
short_description_en: "Complete fixture profile reference for the Olfer CBU-DA-1P Casambi DALI controller, covering DT6, DT8, Broadcast, Short Address, Tunable White, RGB/RGBW, and extended sensor modes."

# === SEARCH OPTIMIZATION ===
aliases: ["CBU-DA-1P", "CBUDA1P", "CBU DA 1P", "Olfer DALI Casambi"]
search_keywords_vi:
  - "fixture profile CBU-DA-1P"
  - "profile DALI Casambi Olfer"
  - "DT6 DT8 DALI profile"
  - "tunable white DALI profile"
  - "DALI broadcast short address"
  - "DALI RGB RGBW profile"
  - "cấu hình fixture DALI"
  - "profile chiếu sáng DALI Casambi"
  - "DALI gateway push button"
  - "dimming curve linear logarithmic DALI"
search_keywords_en:
  - "CBU-DA-1P fixture profiles"
  - "Olfer DALI Casambi profiles"
  - "DALI DT6 DT8 fixture profile"
  - "Casambi DALI broadcast short address"
  - "tunable white DALI profile"
  - "DALI RGB RGBW profile"
  - "linear logarithmic dimming"
  - "DALI gateway profile"
  - "DALI push button profile"
  - "Casambi fixture profile list"

# === DECISION CRITERIA ===
use_case_tags:
  - "lighting_control"
  - "dali_control"
  - "tunable_white"
  - "rgb_lighting"
  - "sensor_integration"
  - "group_control"
  - "broadcast_control"
target_segment: ["system_integrator", "lighting_designer"]
project_scale: ["small", "medium", "large"]
complexity_level: "advanced"
not_suitable_for:
  - "non-DALI lighting systems"
  - "0-10V only drivers"
  - "standalone dimmer use without DALI bus"

# === RELATIONSHIPS ===
replaces_sku: []
replaced_by_sku: null
equivalent_skus: []
accessories_required:
  - "DALI-compatible LED drivers"
  - "Casambi App (iOS/Android)"
accessories_recommended:
  - "CBU-DA-1P (main product)"
  - "DALI-2 motion sensors"
  - "DALI-2 light sensors"
  - "DALI-2 push button input devices"
bundle_with: []
upsell_to: []

# === CASAMBI INTEGRATION ===
casambi_network_type: ["Classic", "Evolution"]
casambi_pro_compatible: true
fixture_profile_default_id: "33477"
fixture_profile_default_name: "DALI Lin* (Broadcast)"
fixture_profile_alternatives:
  - "DALI Log (Broadcast)"
  - "DALI Lin* 1xDIM SA"
  - "DALI Lin* DT8 TW 3-5K BC"
  - "DALI Lin* DT6 RGB SA"
  - "DALI Gateway"
  - "DALI Push Button x8"

# === COMMERCIAL REFERENCE ===
pricing_visibility: "sales_only"
stock_visibility: "sales_only"
moq_hint: "Liên hệ sales để biết MOQ và bậc giá theo số lượng"
warranty_months: 24
origin_country: "Spain"
hs_code_vn: ""

# === ASSETS ===
images:
  main: ""
  wiring: ""
  dimensions: ""
datasheet_url: "https://www.olfer.com/olfer-cbu-da-1p.html"
manual_url_en: "https://www.olfer.com/olfer-cbu-da-1p.html"
manual_url_vi: null

# === FAQ EMBEDDED ===
common_questions:
  - q: "CBU-DA-1P có bao nhiêu Fixture Profile?"
    a: "CBU-DA-1P hỗ trợ hơn 100 Fixture Profile khác nhau, bao gồm DALI DT6 và DT8 với các chế độ Broadcast, Short Address, Group, Tunable White, RGB, RGBW, XY và các kết hợp cảm biến mở rộng."
  - q: "Profile mặc định của CBU-DA-1P là gì?"
    a: "Profile mặc định là DALI Lin* (Fixture ID 33477), sử dụng chế độ Broadcast với đường cong điều chỉnh tuyến tính (Linear). Đây là profile phổ biến nhất cho hệ thống chiếu sáng DALI cơ bản."
  - q: "Sự khác biệt giữa DALI DT6 và DT8 là gì?"
    a: "DT6 là chuẩn DALI điều chỉnh độ sáng cơ bản (dimming), trong khi DT8 hỗ trợ điều khiển màu sắc nâng cao (Tunable White, RGB, RGBW, XY) trực tiếp qua giao thức DALI mà không cần bộ điều khiển màu riêng."
  - q: "Linear (Lin*) và Logarithmic (Log) dimming khác nhau như thế nào?"
    a: "Linear dimming (Lin*) điều chỉnh độ sáng theo tỷ lệ tuyến tính, phù hợp với hầu hết ứng dụng. Logarithmic dimming (Log) điều chỉnh theo thang logarithm, tạo cảm giác mượt mà hơn khi giảm sáng xuống mức thấp, phù hợp với không gian cần hiệu ứng mờ dần tự nhiên."
  - q: "Có thể kết nối cảm biến DALI-2 với CBU-DA-1P không?"
    a: "Có, CBU-DA-1P hỗ trợ cảm biến DALI-2 (chuyển động và ánh sáng) thông qua các Fixture Profile BC + Ext. Presence, BC + Ext. Light, và BC + Ext. Sensors. Cảm biến DALI-2 sẽ xuất hiện như một Casambi sensor trong App."

# === HANDOFF TRIGGERS ===
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

# === DATA GOVERNANCE ===
last_updated: "2026-04-17"
last_verified_by: "auto_converter"
content_version: "1.0"
source_of_truth: "DALI - Olfer CBU-DA-1P - Fixture Profile.md"
confidence_level: "high"
chatbot_priority: "high"

# === RAG OPTIMIZATION ===
chunk_strategy: "by_section"
priority_sections:
  - "Danh sách Fixture Profile"
  - "Fixture Profile mặc định"
  - "DALI DT8 - Tunable White"
  - "FAQ"
exclude_from_chunks:
  - "Bảo hành & Hỗ trợ"
  - "Tài liệu kỹ thuật"
---

# Olfer CBU-DA-1P – Fixture Profiles Reference

## Tổng quan

Tài liệu này liệt kê toàn bộ Fixture Profile có sẵn cho bộ điều khiển **Olfer CBU-DA-1P** – thiết bị cầu nối Casambi sang DALI. Phiên bản tài liệu: **EN-V1.2, ngày 02/05/2024**.

CBU-DA-1P hỗ trợ hơn **100 Fixture Profile** khác nhau, bao phủ các chế độ điều khiển từ cơ bản (Broadcast, Single Address) đến nâng cao (Tunable White DT8, RGB/RGBW, XY, tích hợp cảm biến DALI-2, push button). Việc chọn đúng Fixture Profile là bước then chốt để hệ thống chiếu sáng DALI hoạt động đúng với ứng dụng thực tế.

Profile được chọn trong Casambi App sẽ xác định giao diện điều khiển (slider, màu sắc, nhiệt độ màu…), chế độ đánh địa chỉ DALI (Broadcast, Short Address, Group), và cách CBU-DA-1P giao tiếp với driver DALI.

---

## Fixture Profile mặc định

| Fixture ID | Tên Profile | Chế độ |
|:---|:---|:---|
| **33477** ⭐ | DALI Lin\* | Broadcast – Đường cong tuyến tính (mặc định) |

---

## Danh sách Fixture Profile

### 1. DALI DT6 – Broadcast (BC)

Điều khiển toàn bộ DALI bus cùng lúc (Broadcast). Không cần đánh địa chỉ riêng lẻ.

| Tên Profile | Mô tả | Dimmer |
|:---|:---|:---|
| DALI Lin\* | Broadcast, đường cong tuyến tính. **Profile mặc định** | BC |
| DALI Log | Broadcast, đường cong logarithm | BC |
| DALI Lin\* BC + Ext. Presence | Broadcast + cảm biến chuyển động DALI-2 trên bus | BC |
| DALI Log BC + Ext. Presence | Broadcast log + cảm biến chuyển động DALI-2 | BC |
| DALI Lin\* BC + Ext. Light | Broadcast + cảm biến ánh sáng DALI-2 | BC |
| DALI Log BC + Ext. Light | Broadcast log + cảm biến ánh sáng DALI-2 | BC |
| DALI Lin\* BC + Ext. Sensors | Broadcast + cảm biến chuyển động & ánh sáng DALI-2 | BC |
| DALI Log BC + Ext. Sensors | Broadcast log + cảm biến chuyển động & ánh sáng DALI-2 | BC |
| DALI Lin\* BC + Ext. Buttons | Broadcast + DALI-2 push button (tối đa 8 instances) | BC |
| DALI Log BC + Ext. Buttons | Broadcast log + DALI-2 push button (tối đa 8 instances) | BC |
| DALI Lin\* BC + Ext. Devices | Broadcast + cảm biến chuyển động/ánh sáng + push button | BC |
| DALI Log BC + Ext. Devices | Broadcast log + cảm biến + push button | BC |

> 💡 **Lưu ý:** Khi sử dụng profile có "Ext. Presence/Light/Sensors", cảm biến DALI-2 kết nối trên bus DALI sẽ xuất hiện như một Casambi sensor trong App. Khi có "Ext. Buttons", PUSH input sẽ bị vô hiệu hóa.

---

### 2. DALI DT6 – Short Address (SA) – Dimmer đơn/nhiều kênh

Điều khiển từng driver riêng lẻ qua địa chỉ ngắn DALI. Đánh địa chỉ tự động (Automatic DALI addressing).

#### 2.1 Dimmer đơn (1 kênh)

| Tên Profile | Mô tả | Dimmer |
|:---|:---|:---|
| DALI Lin\* 1xDIM SA | 1 Dimmer DT6, đường cong tuyến tính, đánh địa chỉ tự động | A0 |
| DALI Log 1xDIM SA | 1 Dimmer DT6, đường cong logarithm | A0 |

#### 2.2 Nhiều dimmer (2–8 kênh)

| Tên Profile | Mô tả | Dimmers |
|:---|:---|:---|
| DALI Lin\* 2xDIM SA | 2 Dimmers DT6, tuyến tính | A0, A1 |
| DALI Log 2xDIM SA | 2 Dimmers DT6, logarithm | A0, A1 |
| DALI Lin\* 3xDIM SA | 3 Dimmers DT6, tuyến tính | A0, A1, A2 |
| DALI Log 3xDIM SA | 3 Dimmers DT6, logarithm | A0, A1, A2 |
| DALI Lin\* 4xDIM SA | 4 Dimmers DT6, tuyến tính | A0–A3 |
| DALI Log 4xDIM SA | 4 Dimmers DT6, logarithm | A0–A3 |
| DALI Lin\* 5xDIM SA | 5 Dimmers DT6, tuyến tính | A0–A4 |
| DALI Log 5xDIM SA | 5 Dimmers DT6, logarithm | A0–A4 |
| DALI Lin\* 6xDIM SA | 6 Dimmers DT6, tuyến tính | A0–A5 |
| DALI Log 6xDIM SA | 6 Dimmers DT6, logarithm | A0–A5 |
| DALI Lin\* 7xDIM SA | 7 Dimmers DT6, tuyến tính | A0–A6 |
| DALI Log 7xDIM SA | 7 Dimmers DT6, logarithm | A0–A6 |
| DALI Lin\* 8xDIM SA | 8 Dimmers DT6, tuyến tính | A0–A7 |
| DALI Log 8xDIM SA | 8 Dimmers DT6, logarithm | A0–A7 |

> 💡 **Lưu ý:** Với profile nhiều dimmer, khi kéo slider trên icon App, tất cả mức slider riêng lẻ sẽ bị ghi đè.

---

### 3. DALI DT6 – Group Control (1–8 nhóm)

Điều khiển theo nhóm DALI (Group Address). Phù hợp khi cần điều khiển nhiều nhóm đèn độc lập trong cùng một bus.

| Tên Profile | Mô tả | Dimmers |
|:---|:---|:---|
| DALI Lin\* (1xGroup) | 1 Group, tuyến tính | G0 |
| DALI Log (1xGroup) | 1 Group, logarithm | G0 |
| DALI Lin\* (2xGroup) | 2 Groups, tuyến tính | G0, G1 |
| DALI Log (2xGroup) | 2 Groups, logarithm | G0, G1 |
| DALI Lin\* (3xGroup) | 3 Groups, tuyến tính | G0–G2 |
| DALI Log (3xGroup) | 3 Groups, logarithm | G0–G2 |
| DALI Lin\* (4xGroup) | 4 Groups, tuyến tính | G0–G3 |
| DALI Log (4xGroup) | 4 Groups, logarithm | G0–G3 |
| DALI Lin\* (5xGroup) | 5 Groups, tuyến tính | G0–G4 |
| DALI Log (5xGroup) | 5 Groups, logarithm | G0–G4 |
| DALI Lin\* (6xGroup) | 6 Groups, tuyến tính | G0–G5 |
| DALI Log (6xGroup) | 6 Groups, logarithm | G0–G5 |
| DALI Lin\* (7xGroup) | 7 Groups, tuyến tính | G0–G6 |
| DALI Log (7xGroup) | 7 Groups, logarithm | G0–G6 |
| DALI Lin\* (8xGroup) | 8 Groups, tuyến tính | G0–G7 |
| DALI Log (8xGroup) | 8 Groups, logarithm | G0–G7 |

---

### 4. DALI DT6 – Tunable White (TW)

Điều khiển đèn trắng có thể điều chỉnh nhiệt độ màu (Warm/Cool).

| Tên Profile | Mô tả | Dimmer | Nhiệt độ màu |
|:---|:---|:---|:---|
| DALI Lin\* DT6 TW Warm-Cool SA | Generic Warm/Cool (không có giá trị CCT), tuyến tính | A0+A1 | Warm/Cool mixer |
| DALI Log DT6 TW Warm-Cool SA | Generic Warm/Cool, logarithm | A0+A1 | Warm/Cool mixer |
| DALI Lin\* DT6 TW 3-5K SA | Tunable White 3000K–5000K, tuyến tính | A0+A1 | 3000K–5000K |
| DALI Log DT6 TW 3-5K SA | Tunable White 3000K–5000K, logarithm | A0+A1 | 3000K–5000K |
| DALI Lin\* DT6 Dim to Warm SA | Dim to Warm – mờ hơn thì ấm hơn, tuyến tính | A0+A1 | Tự động theo độ sáng |
| DALI Log DT6 Dim to Warm SA | Dim to Warm, logarithm | A0+A1 | Tự động theo độ sáng |

---

### 5. DALI DT6 – RGB / RGBW / RGB+W

Điều khiển đèn màu qua DALI DT6. Phù hợp với các driver LED màu.

| Tên Profile | Mô tả | Dimmers |
|:---|:---|:---|
| DALI Lin\* DT6 RGB SA | RGB, tuyến tính. Palette + Saved Colours (tối đa 10) | A0 (R), A1 (G), A2 (B) |
| DALI Log DT6 RGB SA | RGB, logarithm | A0 (R), A1 (G), A2 (B) |
| DALI Lin\* DT6 RGBW SA | RGBW, slider White riêng, tuyến tính | A0–A2 (RGB), A3 (W) |
| DALI Log DT6 RGBW SA | RGBW, logarithm | A0–A2 (RGB), A3 (W) |
| DALI Lin\* DT6 RGB/W SA | RGB/W – slider cân bằng White/Colour, tuyến tính | A0–A2 (RGB), A3 (W) |
| DALI Log DT6 RGB/W SA | RGB/W, logarithm | A0–A2 (RGB), A3 (W) |
| DALI Lin\* DT6 RGB/W+dW SA | RGB/W + kênh White2 bán độc lập, tuyến tính | A0–A2 (RGB), A3 (W1), A4 (W2) |
| DALI Log DT6 RGB/W+dW SA | RGB/W + White2, logarithm | A0–A2 (RGB), A3 (W1), A4 (W2) |
| DALI Lin\* DT6 RGB/W+W SA | RGB/W + White độc lập (Evolution), tuyến tính | A0–A2 (RGB), A3 (W/Colour), A4 (W độc lập) |
| DALI Log DT6 RGB/W+W SA | RGB/W + White độc lập (Evolution), logarithm | A0–A2 (RGB), A3 (W/Colour), A4 (W độc lập) |

---

### 6. DALI DT8 – Tunable White (Broadcast)

DALI DT8 hỗ trợ điều khiển nhiệt độ màu và màu sắc nâng cao trực tiếp qua giao thức DALI, không cần bộ điều khiển màu riêng.

| Tên Profile | Mô tả | Dimmer | Nhiệt độ màu |
|:---|:---|:---|:---|
| DALI Lin\* DT8 TW 3-5K BC | TW Broadcast, tuyến tính | BC | 3000K–5000K |
| DALI Log DT8 TW 3-5K BC | TW Broadcast, logarithm | BC | 3000K–5000K |
| DALI Lin\* DT8 TW 2.7-6K BC | TW Broadcast, tuyến tính | BC | 2700K–6000K |
| DALI Log DT8 TW 2.7-6K BC | TW Broadcast, logarithm | BC | 2700K–6000K |
| DALI Lin\* DT8 TW 2.2-7K BC | TW Broadcast, tuyến tính | BC | 2200K–7000K |
| DALI Log DT8 TW 2.2-7K BC | TW Broadcast, logarithm | BC | 2200K–7000K |
| DALI Lin\* DT8 Dim to Warm BC | Dim to Warm Broadcast, tuyến tính | BC | Tự động |
| DALI Log DT8 Dim to Warm BC | Dim to Warm Broadcast, logarithm | BC | Tự động |

#### DT8 TW – Short Address / Group (Evolution)

| Tên Profile | Mô tả | Dimmer |
|:---|:---|:---|
| DALI Lin\* DT8 TW 2.7-6.5K (2xSA) | 2 Short Address TW, slider riêng cho từng địa chỉ | A0, A1 |
| DALI Log DT8 TW 2.7-6.5K (2xSA) | 2 SA TW, logarithm | A0, A1 |
| DALI Lin\* DT8 TW 2.7-6.5K (3xSA) | 3 SA TW, slider nhiệt độ màu chung | A0, A1, A2 |
| DALI Log DT8 TW 2.7-6.5K (3xSA) | 3 SA TW, logarithm | A0, A1, A2 |
| DALI Lin\* DT8 TW 2.7-6.5K (2xGroup) | 2 Group TW, Evolution | G0, G1 |
| DALI Log DT8 TW 2.7-6.5K (2xGroup) | 2 Group TW, logarithm | G0, G1 |
| DALI Lin\* DT8 TW 2.7-6.5K (3xGroup) | 3 Group TW, slider nhiệt độ màu chung | G0, G1, G2 |
| DALI Log DT8 TW 2.7-6.5K (3xGroup) | 3 Group TW, logarithm | G0, G1, G2 |

---

### 7. DALI DT8 – RGB / RGBW / RGB+W / XY (Broadcast)

| Tên Profile | Mô tả | Dimmer |
|:---|:---|:---|
| DALI Lin\* DT8 RGB BC | RGB Broadcast, tuyến tính. Palette + Saved Colours (10) | BC |
| DALI Log DT8 RGB BC | RGB Broadcast, logarithm | BC |
| DALI Lin\* DT8 RGBW BC | RGBW Broadcast, slider White riêng, tuyến tính | BC |
| DALI Log DT8 RGBW BC | RGBW Broadcast, logarithm | BC |
| DALI Lin\* DT8 RGB/W BC | RGB/W Broadcast – White/Colour balance, tuyến tính | BC |
| DALI Log DT8 RGB/W BC | RGB/W Broadcast, logarithm | BC |
| DALI Lin\* DT8 RGB/TW BC | RGB/TC Broadcast, tuyến tính (2700K–6500K) | BC |
| DALI Log DT8 RGB/TW BC | RGB/TC Broadcast, logarithm | BC |
| DALI Lin\* DT8 RGBW/TW BC | RGBW/TC Broadcast, tuyến tính | BC |
| DALI Log DT8 RGBW/TW BC | RGBW/TC Broadcast, logarithm | BC |
| DALI Lin\* DT8 XY BC | XY Colour Broadcast, tuyến tính. XY Palette | BC |
| DALI Log DT8 XY BC | XY Colour Broadcast, logarithm | BC |
| DALI Lin\* DT8 XY/TW BC | XY/TC Broadcast, tuyến tính | BC |
| DALI Log DT8 XY/TW BC | XY/TC Broadcast, logarithm | BC |

---

### 8. Misc – Gateway & Push Button

| Tên Profile | Mô tả | Ghi chú |
|:---|:---|:---|
| DALI Gateway | Gateway giữa bus DALI có dây và mạng Casambi không dây | Xuất hiện dưới tab "Gateways" |
| DALI Push Button x7 | 7 instances push button DALI-2 (iN0–iN6) | Không xuất hiện dưới tab Lamps; xuất hiện dưới "Switches" |
| DALI Push Button x8 | 8 instances push button DALI-2 (iN0–iN7). PUSH input bị vô hiệu | Xuất hiện dưới "Switches" |
| Push Button | 1 nút nhấn N.O. kết nối vào terminal PUSH | Xuất hiện dưới "Switches" |
| Push Button x2 | 2 nút nhấn N.O. – PUSH terminal + DALI (DA+/DA-) | Xuất hiện dưới "Switches" |

---

## Bảng viết tắt

| Ký hiệu | Ý nghĩa |
|:---|:---|
| A0, A1, A2... | Địa chỉ ngắn DALI (Short Address) |
| G0, G1, G2... | Địa chỉ nhóm DALI (Group Address) |
| BC | Broadcast – phát lệnh đến toàn bộ bus |
| SA | Short Address – địa chỉ ngắn riêng lẻ |
| Lin\* | Đường cong điều chỉnh tuyến tính tối ưu (Optimized Linear) |
| Log | Đường cong điều chỉnh logarithm |
| DT6 | DALI Device Type 6 – Dimmer cơ bản |
| DT8 | DALI Device Type 8 – Điều khiển màu sắc nâng cao |
| TW | Tunable White – điều chỉnh nhiệt độ màu |
| OHI | Over-Heat Indication – cảnh báo quá nhiệt |
| HWTemp | Hardware Temperature monitoring |

---

## Hướng dẫn chọn Fixture Profile

Để chọn profile phù hợp, cần xác định:

**1. Loại driver DALI đang dùng là gì?**
Nếu driver chỉ hỗ trợ dimming → dùng DT6. Nếu driver hỗ trợ TW/RGB/RGBW theo chuẩn DALI → dùng DT8.

**2. Chế độ đánh địa chỉ?**
Broadcast (BC) điều khiển tất cả đèn cùng lúc. Short Address (SA) hoặc Group cho phép điều khiển từng đèn/nhóm riêng.

**3. Cần tích hợp cảm biến?**
Chọn profile "Ext. Presence/Light/Sensors" nếu có cảm biến DALI-2 trên bus.

**4. Đường cong mờ?**
Linear (Lin\*) cho hầu hết ứng dụng. Logarithmic (Log) tạo cảm giác mờ mượt mà hơn ở mức thấp.

---

## Sản phẩm tương thích

### Bắt buộc
- Smartphone/Tablet có Casambi App (iOS/Android)
- Driver LED tương thích DALI (DALI DT6 hoặc DT8)

### Khuyến nghị
- Cảm biến chuyển động DALI-2 (cho profile Ext. Presence/Sensors)
- Cảm biến ánh sáng DALI-2 (cho profile Ext. Light/Sensors)
- Thiết bị push button DALI-2 (tối đa 8 instances, cho profile Ext. Buttons/Devices)

---

## FAQ

**CBU-DA-1P có bao nhiêu Fixture Profile?**
Hơn 100 Fixture Profile, bao gồm DT6 và DT8 với đầy đủ chế độ Broadcast, Short Address, Group, TW, RGB, RGBW, XY và tích hợp cảm biến DALI-2.

**Profile nào là mặc định?**
Fixture ID **33477 – DALI Lin\*** (Broadcast, đường cong tuyến tính). Đây là profile factory default, phù hợp với hầu hết ứng dụng dimming DALI đơn giản.

**Sự khác nhau giữa DT6 và DT8?**
DT6 dành cho dimming cơ bản, DT8 hỗ trợ điều khiển màu sắc nâng cao (TW, RGB, RGBW, XY) trực tiếp qua DALI mà không cần bộ điều khiển màu ngoài.

**Linear và Logarithmic dimming khác nhau như thế nào?**
Linear cho cảm giác dimming đồng đều theo tỷ lệ. Logarithmic tạo hiệu ứng mờ tự nhiên, mượt mà hơn ở mức sáng thấp, phù hợp cho không gian cao cấp.

**Cảm biến DALI-2 có thể tích hợp không?**
Có. Cảm biến DALI-2 kết nối trên bus DALI sẽ xuất hiện như Casambi sensor trong App khi dùng các profile có "Ext. Presence", "Ext. Light" hoặc "Ext. Sensors".

---

## Tài liệu kỹ thuật

📄 **Để xem tài liệu và firmware mới nhất, vui lòng truy cập:**
👉 [Trang sản phẩm CBU-DA-1P](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p)

---

## Bảo hành & Hỗ trợ

- **Bảo hành:** 24 tháng
- **Hỗ trợ kỹ thuật:** Liên hệ qua website knxstore.vn
