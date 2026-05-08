---
# === IDENTIFICATION ===
sku: "CBU-A2D"
product_name: "Casambi CBU-A2D - Bộ điều khiển 2 kênh 0-10V/DALI Bluetooth"
brand: "Casambi"
manufacturer_part_number: "CBU-A2D"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/casambi-bo-dieu-khien-2-kenh-0-10v-dali-bluetooth-cbu-a2d"
status: "active"

# === CLASSIFICATION ===
category_primary: "Dimmers"
category_secondary: ["DALI Controllers", "0-10V Controllers", "Lighting Control", "Casambi"]
protocols: ["CASAMBI", "DALI", "BLE"]

# === SHORT DESCRIPTION ===
short_description_vi: "Bộ điều khiển chiếu sáng Casambi 2 kênh 0-10V/DALI tích hợp Bluetooth, hỗ trợ điều chỉnh độ sáng, Tunable White, DALI DT8 RGB/RGBW và kết nối cảm biến, input 100-240VAC."
short_description_en: "Casambi Bluetooth 2-channel 0-10V/DALI controller supporting dimming, tunable white, DALI DT8 RGB/TW, sensor input, 100-240VAC universal input."

# === SEARCH OPTIMIZATION ===
aliases: ["CBU-A2D", "CBUA2D", "CBU A2D", "Casambi 2ch 0-10V DALI"]
search_keywords_vi:
  - "bộ điều khiển 2 kênh 0-10V DALI Casambi"
  - "CBU-A2D Casambi Bluetooth"
  - "dimmer 0-10V Casambi"
  - "điều khiển tunable white 0-10V"
  - "DALI DT8 Casambi controller"
  - "bộ điều khiển 2 kênh chiếu sáng thông minh"
  - "Casambi standalone DALI"
  - "0-10V dimmer Bluetooth mesh"
  - "điều khiển đèn LED 0-10V Casambi"
  - "bộ điều khiển màu sắc RGB DALI Casambi"
search_keywords_en:
  - "CBU-A2D Casambi 2 channel 0-10V DALI"
  - "Casambi Bluetooth 0-10V dimmer"
  - "DALI DT8 Casambi controller"
  - "tunable white 0-10V Casambi"
  - "standalone DALI Casambi"
  - "2 channel LED driver controller"
  - "Casambi mesh 0-10V"
  - "RGB RGBW DALI Casambi"
  - "push button 0-10V relay controller"
  - "CBU-A2D data sheet"

# === DECISION CRITERIA ===
use_case_tags:
  - "lighting_control"
  - "dali_control"
  - "0_10v_control"
  - "tunable_white"
  - "rgb_lighting"
  - "sensor_integration"
  - "relay_control"
  - "push_button_integration"
target_segment: ["system_integrator", "smart_home_diy", "lighting_designer"]
project_scale: ["small", "medium"]
complexity_level: "intermediate"
not_suitable_for:
  - "hệ thống cần hơn 2 kênh điều khiển độc lập"
  - "lắp đặt ngoài trời (IP20, chỉ dùng trong nhà)"
  - "driver không hỗ trợ 0-10V hoặc DALI"
  - "vỏ kim loại (chặn tín hiệu Bluetooth)"

# === RELATIONSHIPS ===
replaces_sku: []
replaced_by_sku: null
equivalent_skus: []
accessories_required:
  - "Driver LED tương thích 0-10V hoặc DALI"
  - "Casambi App (iOS/Android)"
accessories_recommended:
  - "Nút nhấn momentary (push button N.O.)"
  - "Relay 12VDC coil (cho ứng dụng on/off channel 2)"
  - "Cảm biến hiện diện/ánh sáng DALI thụ động"
bundle_with: []
upsell_to: ["CBU-ASD", "CBU-DA-1P"]

# === CASAMBI INTEGRATION ===
casambi_network_type: ["Classic"]
casambi_pro_compatible: false
fixture_profile_default_id: "11503"
fixture_profile_default_name: "0-10V 2CH Dim, Temp (NoMix)"
fixture_profile_alternatives:
  - "0-10V TW"
  - "0-10V (on/off)"
  - "0-10V + Relay"
  - "2CH 0-10V"
  - "DALI/BC/Sensors"
  - "DALI DT8 TW"
  - "DALI DT8 RGB/TW"

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
  wiring: ""
  dimensions: ""
datasheet_url: "https://casambi.com"
manual_url_en: "https://casambi.com"
manual_url_vi: null

# === FAQ EMBEDDED ===
common_questions:
  - q: "CBU-A2D có thể điều khiển bao nhiêu driver?"
    a: "CBU-A2D có 2 kênh ra. Kênh 1 hỗ trợ tối đa 1 driver 0-10V hoặc 1 cảm biến/push button DALI. Kênh 2 hỗ trợ 1 driver 0-10V hoặc relay 12VDC. Ở chế độ DALI Standalone, có thể kết nối trực tiếp driver DALI mà không cần nguồn DALI ngoài."
  - q: "CBU-A2D có hỗ trợ Tunable White không?"
    a: "Có. CBU-A2D hỗ trợ Tunable White qua 2 cách: (1) Dùng profile '0-10V TW' với 2 kênh 0-10V warm/cool mixer, hoặc (2) Dùng profile 'DALI DT8 TW' nếu driver hỗ trợ DALI DT8 TC color model."
  - q: "Standalone DALI là gì và CBU-A2D có hỗ trợ không?"
    a: "Standalone DALI có nghĩa là CBU-A2D đóng vai trò vừa là controller vừa là nguồn cấp DALI (12VDC, max 20mA), không cần nguồn DALI riêng bên ngoài. Điều này giúp đơn giản hóa đi dây cho hệ thống đa kênh RGB/RGBW/CCT."
  - q: "Có thể dùng CBU-A2D mà không cần app không?"
    a: "Có. CBU-A2D hỗ trợ dimming không cần app bằng cách flick công tắc nguồn: tắt (<1 giây) rồi bật lại để bắt đầu tăng sáng dần, flick lần 2 để chốt mức sáng mong muốn. Mức sáng được lưu tự động."
  - q: "Tầm phủ sóng Bluetooth của CBU-A2D là bao nhiêu?"
    a: "Ngoài trời thoáng, khoảng cách giữa 2 CBU-A2D có thể trên 50m. Trong môi trường có vật cản hoặc cấu trúc kim loại, tầm phủ có thể giảm đáng kể. CBU-A2D hoạt động như một repeater trong mesh network Casambi, tăng độ phủ toàn hệ thống."

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
source_of_truth: "DALI - Casambi CBU-A2D.md"
confidence_level: "high"
chatbot_priority: "high"

# === RAG OPTIMIZATION ===
chunk_strategy: "by_section"
priority_sections:
  - "Thông số kỹ thuật"
  - "Chế độ hoạt động"
  - "Fixture Profiles"
  - "Ứng dụng"
  - "FAQ"
exclude_from_chunks:
  - "Bảo hành & Hỗ trợ"
  - "Tài liệu kỹ thuật"
---

# Casambi CBU-A2D – Bộ điều khiển 2 kênh 0-10V/DALI Bluetooth

## Tổng quan sản phẩm

**CBU-A2D** là bộ điều khiển chiếu sáng 2 kênh tích hợp Bluetooth Casambi, hỗ trợ cả giao thức **0-10V** và **DALI**. Thiết bị có dải điện áp đầu vào toàn cầu 100–240VAC (277VAC với chứng nhận UL/CSA), phù hợp cho các dự án tại Việt Nam và quốc tế.

CBU-A2D có thể được cấu hình linh hoạt: điều khiển 1 hoặc 2 driver 0-10V độc lập, điều khiển Tunable White qua 2 kênh 0-10V, hoặc chuyển sang chế độ DALI để kết nối driver DALI / cảm biến DALI. Một điểm nổi bật là **Standalone DALI** — CBU-A2D vừa là controller vừa là nguồn cấp bus DALI (12VDC, 20mA), giúp loại bỏ nhu cầu dùng nguồn DALI ngoài, đơn giản hóa đi dây cho hệ thống đa kênh màu sắc RGB/RGBW/CCT.

Thiết bị được điều khiển qua **Casambi App** (iOS/Android, miễn phí). Casambi sử dụng công nghệ mesh network — mỗi CBU-A2D cũng đóng vai trò repeater, tự động tạo mạng lưới thông minh tối đa 250 thiết bị mà không cần hub hay gateway trung tâm.

---

## Đặc điểm nổi bật

✅ Điều khiển Bluetooth Casambi, không cần hub/gateway trung tâm
✅ 2 kênh ra linh hoạt: 0-10V, DALI, relay 12VDC
✅ Hỗ trợ Standalone DALI — tích hợp nguồn bus DALI 12VDC/20mA
✅ Dải điện áp đầu vào rộng: 100–240VAC (277VAC UL/CSA)
✅ Hỗ trợ Tunable White, DALI DT8 RGB/RGBW/XY/TW
✅ Tích hợp cảm biến DALI (hiện diện & ánh sáng ban ngày)
✅ Dimming không cần app bằng flick công tắc
✅ Mesh network — tự động, không cần cấu hình thủ công
✅ OTA firmware update
✅ Kích thước nhỏ gọn: 76 × 26 × 23 mm

---

## Thông số kỹ thuật

### Nguồn đầu vào

| Thông số | Giá trị |
|:---|:---|
| Dải điện áp | 100–240 VAC (277 VAC UL/CSA) |
| Tần số | 50–60 Hz |
| Dòng điện đầu vào tối đa | 35 mA |
| Công suất chờ (standby) | < 0,5 W |

### Kênh 1 (CH1)

| Thông số | Giá trị |
|:---|:---|
| Điện áp ra 0-10V | 0–10 VDC, tối đa 7 mA (sinking) |
| Điện áp ra DALI | 12 VDC, tối đa 20 mA (sourcing) |
| Số driver tối đa | 1 driver hoặc 1 cảm biến/push button |

### Kênh 2 (CH2)

| Thông số | Giá trị |
|:---|:---|
| Điện áp ra 0-10V | 0–10 VDC, tối đa 7 mA (sinking) |
| Điện áp ra relay | 12 VDC, tối đa 100 mA (sourcing) |
| Số driver tối đa | 1 driver hoặc 1 relay 12VDC |

### Kết nối dây

| Thông số | Giá trị |
|:---|:---|
| Tiết diện dây | 0,5–1,5 mm² (Solid & Stranded) / 16–20 AWG |
| Chiều dài tuốt dây | 6–8 mm |
| Mô-men xiết | 0,4 Nm |

### RF / Bluetooth

| Thông số | Giá trị |
|:---|:---|
| Giao thức | Casambi (Bluetooth Low Energy) |
| Tần số hoạt động | 2400–2480 MHz |
| Công suất phát tối đa | +4 dBm |
| Tầm phủ ngoài trời | > 50 m (giữa 2 CBU-A2D) |

### Cơ khí & Môi trường

| Thông số | Giá trị |
|:---|:---|
| Kích thước | 76,0 × 26,0 × 23,0 mm |
| Trọng lượng | 40 g |
| Cấp bảo vệ | IP20 (chỉ dùng trong nhà) |
| Cấp bảo vệ điện | Class II Built-in |
| Nhiệt độ vận hành | -20°C đến +45°C |
| Nhiệt độ vỏ tối đa (Tc) | +70°C |
| Nhiệt độ lưu kho | -25°C đến +70°C |
| Độ ẩm tối đa | 0–80%, không ngưng tụ |

---

## Chế độ hoạt động

CBU-A2D hỗ trợ nhiều chế độ hoạt động thông qua cấu hình Fixture Profile trong Casambi App:

**Chế độ 0-10V (một hoặc hai kênh):** Điều khiển 1–2 driver LED 0-10V độc lập. Phù hợp cho hệ thống đèn đơn sắc hoặc đa vùng.

**Chế độ Tunable White (0-10V):** Kênh 1 điều khiển mức sáng (dim), kênh 2 điều khiển nhiệt độ màu (CCT). Phù hợp với các driver Warm/Cool 0-10V.

**Chế độ 0-10V + Relay:** Kênh 1 điều chỉnh độ sáng 0-10V, kênh 2 điều khiển relay 12VDC để bật/tắt hoàn toàn khi driver không thể tắt qua giao tiếp 0-10V.

**Chế độ DALI Standalone:** CBU-A2D cấp nguồn bus DALI (12VDC, 20mA) cho driver DALI, không cần nguồn DALI ngoài. Hỗ trợ DALI DT6 và DT8 (TW, RGB, RGBW, XY).

**Chế độ DALI + Cảm biến:** Kết nối cảm biến DALI thụ động (passive DALI sensor) để tích hợp chức năng hiện diện (presence) và thu hoạch ánh sáng ban ngày (daylight harvesting).

---

## Fixture Profiles

### 0-10V Profiles

| Profile | Mô tả | Ghi chú |
|:---|:---|:---|
| **0-10V 2CH Dim, Temp (NoMix)** ⭐ | 2 kênh TW: kênh 0 = dimmer, kênh 1 = nhiệt độ màu. Không mix warm/cool | **Mặc định** (Profile# 11503) |
| 0-10V TW | 2 kênh warm/cool mixer tự động | Tunable White |
| 0-10V (on/off) | 1 kênh 0-10V dimmer cơ bản | Đơn giản |
| 0-10V (PB) | 1 kênh 0-10V dimmer + push button | Có nút nhấn |
| 0-10V + Relay | 1 kênh 0-10V + relay CH2 | Khi driver không tắt được qua 0-10V |
| 2CH 0-10V | 2 kênh 0-10V dimmer độc lập | 2 vùng riêng |
| 2CH Dim, Vertical | 2 kênh dimmer + vertical ratio (tổng 2 kênh = mức sáng chung) | Đèn 2 kênh |
| Control PushButton + Relay | Push button + relay on/off qua custom element | Nút nhấn LV + relay |

### DALI Profiles

| Profile | Mô tả | Địa chỉ |
|:---|:---|:---|
| DALI 2CH | 2 kênh DALI | Dimmer 1: #0, Dimmer 2: #1 |
| DALI 8CH | 4 kênh DALI (đặt tên 8CH theo codebase) | #0, #1, #2, #3 |
| DALI/BC/Sensors | Broadcast DALI dimmer cơ bản + cảm biến | Không cần địa chỉ ngắn |
| DALI DT8 RGB/TW | DT8 với điều khiển RGB hoặc CCT (loại trừ lẫn nhau) | DT8 |
| DALI DT8 TW | DT8 Tunable White — driver thực hiện mix warm/cool | DT8 TC |
| DALI DT8 XY/TW (Evo) | DT8 đa kênh hỗ trợ XY color type (Evolution) | DT8 XY |
| DALI TW | 2 kênh warm/cool mixer qua DALI | DT6 |

> 💡 **Lưu ý:** Profile mặc định **11503 – 0-10V 2CH Dim, Temp (NoMix)** không thực hiện trộn warm/cool mà gửi trực tiếp giá trị dimmer sang kênh 0 và giá trị nhiệt độ màu sang kênh 1.

---

## Ứng dụng

CBU-A2D phù hợp với nhiều kịch bản chiếu sáng thông minh từ đơn giản đến phức tạp. Ở mức cơ bản, một thiết bị có thể điều khiển trực tiếp một bóng đèn hay dải đèn LED qua 0-10V. Ở mức đầy đủ, nhiều CBU-A2D tự động kết nối với nhau thành mesh network Casambi thông minh (tối đa 250 node), hỗ trợ cảnh (scenes), lịch (schedules), tự động hóa theo cảm biến, và điều khiển từ xa qua Cloud.

Các ứng dụng điển hình bao gồm: văn phòng dùng Tunable White để điều chỉnh nhiệt độ màu theo giờ làm việc, bảo tàng/gallery dùng DALI DT8 RGB để tạo hiệu ứng màu sắc chính xác, khách sạn dùng nhiều CBU-A2D với cảm biến DALI để tự động tắt đèn khi không có người, và không gian thương mại dùng chế độ relay để kiểm soát bật/tắt hoàn toàn khi cần.

---

## Sản phẩm tương thích

### Bắt buộc
- Smartphone/Tablet có Casambi App (iOS 10+ / Android 4.4+)
- Driver LED tương thích 0-10V (sinking) hoặc DALI

### Khuyến nghị
- Nút nhấn momentary N.O. (cho profile có PB)
- Relay 12VDC có diode chống flyback (cho profile Relay)
- Cảm biến DALI thụ động (hiện diện/ánh sáng, cho DALI/BC/Sensors)
- CBU-ASD (nâng cấp cho hệ thống DALI lớn hơn)
- CBU-DA-1P (nếu cần điều khiển tối đa 50 driver DALI)

---

## Hướng dẫn lắp đặt cơ bản

Tắt nguồn điện trước khi đấu dây. Dùng dây 0,5–1,5 mm² (solid hoặc stranded), tuốt dây 6–8 mm, xiết vít đầu nối với lực 0,4 Nm. Không đấu nối song song 2 kênh ra — có thể gây hỏng thiết bị vĩnh viễn.

Để relay hoạt động đúng ở kênh 2, chọn fixture configuration phù hợp trong Casambi App và đảm bảo relay có diode chống flyback tích hợp (không dùng relay PCB không có diode).

---

## Dimming không cần App

CBU-A2D hỗ trợ điều chỉnh độ sáng bằng công tắc nguồn (không cần app):

1. Bật đèn từ công tắc tường.
2. Flick công tắc tắt nhanh (< 1 giây) rồi bật lại — đèn bắt đầu tăng sáng dần.
3. Flick lần 2 ở mức sáng mong muốn — mức sáng được lưu tự động.
4. Nếu không flick lần 2 trong vòng 8 giây, đèn tăng đến mức tối đa.
5. Flick công tắc có thể dùng để chuyển đổi giữa các scene đã cài sẵn.

---

## Lưu ý quan trọng

### An toàn
⚠️ Điện áp nguy hiểm. Chỉ thợ điện có chuyên môn mới được đấu dây. Ngắt nguồn và kiểm tra vắng điện trước khi lắp đặt.

⚠️ **Không đấu song song 2 kênh ra** — có thể gây hỏng thiết bị vĩnh viễn.

### Vị trí lắp đặt
- Chỉ dùng trong nhà (IP20).
- Không lắp trong vỏ kim loại hoặc gần cấu trúc kim loại lớn — kim loại chặn tín hiệu Bluetooth.
- Kiểm tra kỹ độ phủ sóng tại công trình sau khi lắp đặt.
- Trong mesh network, kiểm tra mỗi node có thể nhìn thấy ít nhất 1 node khác.

---

## Tài liệu kỹ thuật

📄 **Để xem tài liệu chi tiết, vui lòng truy cập:**
👉 [Trang sản phẩm CBU-A2D](https://knxstore.vn/products/casambi-bo-dieu-khien-2-kenh-0-10v-dali-bluetooth-cbu-a2d)

---

## Bảo hành & Hỗ trợ

- **Bảo hành:** 24 tháng
- **Hỗ trợ kỹ thuật:** Liên hệ qua website knxstore.vn
