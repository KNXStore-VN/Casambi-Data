---
# ================================================================
# BLOCK 1 — IDENTIFICATION
# ================================================================
sku: "CBU-A2D"                   # Lấy từ cột sku_extracted trong casambi_full_sku.csv
product_name: "Casambi CBU-A2D – Bộ điều khiển 2 kênh 0-10V/DALI Bluetooth"
brand: "Casambi"
manufacturer_part_number: "CBU-A2D"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/casambi-bo-dieu-khien-2-kenh-0-10v-dali-bluetooth-cbu-a2d"
status: "active"

# ================================================================
# BLOCK 2 — CLASSIFICATION
# ================================================================
product_type: "controller"

category_primary: "Điều khiển 0-10V"
category_secondary: ["DALI Controllers", "Lighting Control", "Casambi"]

ecosystem: ["Casambi"]
control_bus: ["0-10V", "DALI"]
connectivity: ["BLE"]

# ================================================================
# BLOCK 3 — SEARCH & DISCOVERY
# ================================================================
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

# ================================================================
# BLOCK 4 — TARGET & USE CASE
# ================================================================
target_segment: ["system_integrator", "lighting_designer", "electrical_installer"]

project_type: ["office", "hotel", "retail", "residential_premium"]

project_scale: ["small", "medium"]

complexity_level: "intermediate"

use_case_tags:
  - "dimming"
  - "tunable_white"
  - "rgb_lighting"
  - "dali_control"
  - "0_10v_control"
  - "occupancy_control"
  - "daylight_harvesting"
  - "relay_control"
  - "sensor_integration"

not_suitable_for:
  - "Hệ thống cần hơn 2 kênh điều khiển độc lập"
  - "Lắp đặt ngoài trời (IP20, chỉ dùng trong nhà)"
  - "Driver không hỗ trợ 0-10V hoặc DALI"
  - "Lắp trong vỏ kim loại (chặn tín hiệu Bluetooth)"

# ================================================================
# BLOCK 5 — CHATBOT BEHAVIOR
# ================================================================
chatbot_priority: "high"

price_display: "fetch"
display_mode_technical: "text"
display_mode_purchase: "markdown_card"

product_link_text: "👉 [Casambi CBU-A2D – Bộ điều khiển 2 kênh 0-10V/DALI](https://knxstore.vn/products/casambi-bo-dieu-khien-2-kenh-0-10v-dali-bluetooth-cbu-a2d)"

handoff_to_sales_when:
  - "user_asks_stock"
  - "user_asks_quotation"
  - "user_asks_discount"
  - "user_asks_lead_time"
  - "user_asks_payment_terms"
  - "user_asks_delivery"
  - "user_asks_project_quote"
  - "user_mentions_project_above_50_units"
  - "user_asks_custom_integration"
  - "user_asks_warranty_claim"

# ================================================================
# BLOCK 6 — RELATIONSHIPS
# ================================================================
replaces_sku: []
replaced_by_sku: null
equivalent_skus: []

accessories_required:
  - "Driver LED tương thích 0-10V (sinking) hoặc DALI"
  - "Casambi App (iOS/Android)"

accessories_recommended:
  - "Nút nhấn momentary N.O. (cho profile có PB)"
  - "Relay 12VDC có diode chống flyback (cho profile Relay)"
  - "Cảm biến DALI thụ động (hiện diện/ánh sáng)"

compare_with_skus: ["CBU-DA-1P", "CBU-TED"]
# Chatbot retrieve file từng SKU này và tự tạo bảng so sánh — không cần bảng cứng trong file

bundle_with: []
upsell_to: ["CBU-DA-1P"]

# ================================================================
# BLOCK 7 — COMMERCIAL
# ================================================================
pricing_visibility: "sales_only"
stock_visibility: "sales_only"
warranty_months: 24
origin_country: "Finland"
hs_code_vn: ""
moq_hint: "Liên hệ sales để biết MOQ và bậc giá theo số lượng"

# ================================================================
# BLOCK 8 — ASSETS
# ================================================================
images:
  main: "https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-2-kenh-0-10v-dali-bluetooth-cbu-a2d_2.jpg"
  wiring: ""
  dimensions: ""
  installation: ""
datasheet_url: "https://casambi.com/product/cbu-a2d/"
manual_url_en: "https://casambi.com/product/cbu-a2d/"
manual_url_vi: null
certification_docs: ["CE", "UL", "CSA", "Casambi certified"]

# ================================================================
# BLOCK 9 — RAG OPTIMIZATION
# ================================================================
chunk_strategy: "by_section"
priority_sections:
  - "Tổng quan sản phẩm"
  - "Thông số kỹ thuật"
  - "Chế độ hoạt động"
  - "Fixture Profiles"
  - "Integration & Compatibility"
  - "FAQ"
exclude_from_chunks:
  - "Bảo hành & Hỗ trợ"
  - "Tài liệu kỹ thuật"

# ================================================================
# BLOCK 10 — DATA GOVERNANCE
# ================================================================
last_updated: "2026-05-08"
last_verified_by: "knxstore-marketing"
content_version: "2.0"
source_of_truth: "knxstore.vn product page + casambi.com datasheet"
confidence_level: "high"
---

# Casambi CBU-A2D – Bộ điều khiển 2 kênh 0-10V/DALI Bluetooth

## Tổng quan sản phẩm

CBU-A2D là bộ điều khiển chiếu sáng 2 kênh của Casambi (Phần Lan), tích hợp Bluetooth Low Energy, hỗ trợ cả giao thức 0-10V và DALI trong cùng một thiết bị. Dải điện áp đầu vào toàn cầu 100–277VAC giúp CBU-A2D phù hợp cho cả dự án trong nước và quốc tế.

CBU-A2D linh hoạt ở chỗ có thể cấu hình thành nhiều chế độ khác nhau tùy fixture profile: điều khiển 2 driver 0-10V độc lập, Tunable White qua 2 kênh 0-10V, DALI Standalone (tích hợp sẵn nguồn bus DALI), hoặc DALI DT8 cho RGB/RGBW/XY. Thiết bị phù hợp với các dự án vừa và nhỏ cần điều khiển linh hoạt mà không muốn đầu tư vào hệ thống bus phức tạp.

👉 [Xem sản phẩm trên KNXStore](https://knxstore.vn/products/casambi-bo-dieu-khien-2-kenh-0-10v-dali-bluetooth-cbu-a2d)

---

## Thông số kỹ thuật

**Nguồn đầu vào**

| Thông số | Giá trị |
|:---|:---|
| Dải điện áp | 100–240 VAC (277 VAC với UL/CSA) |
| Tần số | 50–60 Hz |
| Dòng điện đầu vào tối đa | 35 mA |
| Công suất chờ | < 0,5 W |

**Kênh 1 (CH1)**

| Thông số | Giá trị |
|:---|:---|
| Điện áp ra 0-10V | 0–10 VDC, tối đa 7 mA (sinking) |
| Điện áp ra DALI | 12 VDC, tối đa 20 mA (sourcing) |
| Số driver tối đa | 1 driver hoặc 1 cảm biến/push button |

**Kênh 2 (CH2)**

| Thông số | Giá trị |
|:---|:---|
| Điện áp ra 0-10V | 0–10 VDC, tối đa 7 mA (sinking) |
| Điện áp ra relay | 12 VDC, tối đa 100 mA (sourcing) |
| Số driver tối đa | 1 driver hoặc 1 relay 12VDC |

**Kết nối dây**

| Thông số | Giá trị |
|:---|:---|
| Tiết diện dây | 0,5–1,5 mm² / 16–20 AWG |
| Chiều dài tuốt dây | 6–8 mm |
| Mô-men xiết | 0,4 Nm |

**RF / Bluetooth**

| Thông số | Giá trị |
|:---|:---|
| Giao thức | Casambi (Bluetooth Low Energy) |
| Tần số hoạt động | 2400–2480 MHz |
| Công suất phát tối đa | +4 dBm |
| Tầm phủ ngoài trời | > 50 m (giữa 2 CBU-A2D) |

**Cơ khí & Môi trường**

| Thông số | Giá trị |
|:---|:---|
| Kích thước (D×R×C) | 76 × 26 × 23 mm |
| Trọng lượng | 40 g |
| Cấp bảo vệ | IP20 (chỉ trong nhà) |
| Nhiệt độ vận hành | -20°C đến +45°C |
| Nhiệt độ vỏ tối đa (Tc) | +70°C |
| Độ ẩm tối đa | 0–80%, không ngưng tụ |
| Xuất xứ | Phần Lan |
| Bảo hành | 24 tháng |

---

## Chức năng chính

### Điều khiển 2 kênh linh hoạt

CBU-A2D có 2 kênh ra độc lập, mỗi kênh cấu hình được thành 0-10V dimmer, DALI master, hoặc relay 12VDC. Điều này cho phép 1 thiết bị xử lý nhiều scenario: 2 vùng đèn riêng, Tunable White warm/cool, hay kết hợp dimming + relay on/off.

### Standalone DALI tích hợp

CBU-A2D có thể vừa là DALI master vừa cấp nguồn bus DALI (12VDC, 20mA) mà không cần nguồn DALI riêng bên ngoài. Tính năng này giúp đơn giản hóa đáng kể sơ đồ đấu dây cho hệ thống đa kênh màu RGB/RGBW/CCT.

### Hỗ trợ DALI DT8

Ở chế độ DALI, CBU-A2D hỗ trợ DALI DT8 — chuẩn điều khiển màu sắc nâng cao gồm Tunable White (TC), RGB, RGBW, và XY — cho phép điều khiển màu sắc chính xác trực tiếp qua giao thức DALI mà không cần bộ điều khiển màu riêng.

### Dimming không cần App

CBU-A2D hỗ trợ điều chỉnh độ sáng bằng flick công tắc nguồn: tắt nhanh (<1 giây) rồi bật lại để bắt đầu tăng sáng dần, flick lần 2 để chốt mức sáng mong muốn. Mức sáng được lưu tự động — hữu ích cho người dùng không quen dùng App.

### Mesh network tự động

Mỗi CBU-A2D tự động đóng vai trò repeater trong mạng Casambi BLE Mesh. Không cần hub hay cấu hình thủ công — các node tự tìm nhau và tạo mạng lưới, tối đa 127 node (Classic) hoặc 250 node (Evolution).

---

## Chế độ hoạt động

CBU-A2D được cấu hình qua Fixture Profile trong Casambi App. Mỗi profile xác định cách 2 kênh hoạt động:

**Chế độ 0-10V đơn/đôi kênh** — điều khiển 1–2 driver LED 0-10V độc lập, phù hợp chiếu sáng đơn sắc hoặc đa vùng.

**Chế độ Tunable White** — kênh 1 điều chỉnh mức sáng, kênh 2 điều chỉnh nhiệt độ màu (CCT). Phù hợp với driver Warm/Cool 0-10V.

**Chế độ 0-10V + Relay** — kênh 1 dimming 0-10V, kênh 2 relay 12VDC bật/tắt hoàn toàn khi driver không tắt được qua 0-10V.

**Chế độ DALI Standalone** — CBU-A2D cấp nguồn bus DALI 12VDC/20mA, hỗ trợ DALI DT6 và DT8 (TW, RGB, RGBW, XY). Không cần nguồn DALI ngoài.

**Chế độ DALI + Cảm biến** — kết nối cảm biến DALI thụ động để tích hợp presence detection và daylight harvesting trực tiếp vào Casambi network.

---

## Fixture Profiles

### 0-10V Profiles

| Profile | Mô tả | Ghi chú |
|:---|:---|:---|
| 0-10V 2CH Dim, Temp (NoMix) ⭐ | 2 kênh TW: CH0 = dimmer, CH1 = CCT, không mix | Mặc định (ID 11503) |
| 0-10V TW | 2 kênh warm/cool mixer tự động | Tunable White |
| 0-10V (on/off) | 1 kênh 0-10V dimmer cơ bản | Đơn giản |
| 0-10V + Relay | 1 kênh 0-10V + relay CH2 | Khi driver không tắt qua 0-10V |
| 2CH 0-10V | 2 kênh 0-10V dimmer độc lập | 2 vùng riêng |

### DALI Profiles

| Profile | Mô tả |
|:---|:---|
| DALI/BC/Sensors | Broadcast DALI dimmer cơ bản + cảm biến DALI |
| DALI DT8 TW | DT8 Tunable White — driver thực hiện mix warm/cool |
| DALI DT8 RGB/TW | DT8 RGB hoặc CCT (loại trừ lẫn nhau) |
| DALI DT8 XY/TW | DT8 đa kênh hỗ trợ XY color type (Evolution) |
| DALI TW | 2 kênh warm/cool mixer qua DALI DT6 |

Profile mặc định là **0-10V 2CH Dim, Temp (NoMix)** — gửi trực tiếp giá trị dimmer sang kênh 0 và nhiệt độ màu sang kênh 1, không thực hiện trộn warm/cool.

---

## Integration & Compatibility

### Hoạt động trong hệ Casambi

CBU-A2D là node Casambi Classic — tham gia network như bất kỳ node Casambi nào khác, nhận lệnh từ App hoặc switch Casambi, và phát tín hiệu 0-10V/DALI xuống driver. CBU-A2D chỉ tương thích với **Casambi Classic network**, không tương thích Evolution.

**Yêu cầu:** Casambi App (iOS/Android), Casambi Classic network.
**Giới hạn:** Chỉ 2 kênh ra — không phù hợp cho hệ thống cần nhiều kênh độc lập hơn.

### Điều khiển qua 0-10V

CBU-A2D là nguồn sinking 0-10V — nó kéo điện áp xuống thấp để điều chỉnh driver. Driver phải có nguồn 0-10V riêng (thường 10VDC nội bộ). Không phải driver nào cũng tương thích — cần kiểm tra driver có hỗ trợ 0-10V sinking không.

**Tương thích:** Driver LED có cổng 0-10V sinking (phổ biến ở driver thương mại).
**Không tương thích:** Driver chỉ có 0-10V sourcing, hay DALI, Triac, PWM thuần.

### Điều khiển qua DALI (Standalone)

Ở chế độ DALI, CBU-A2D là DALI master cấp nguồn bus 12VDC/20mA — đủ cho 1 driver DALI đơn hoặc hệ thống nhỏ. Không nên kết nối nhiều driver DALI song song vì nguồn bus chỉ 20mA.

**Tương thích:** Driver DALI DT6 và DT8.
**Không tương thích:** Hệ thống nhiều driver DALI — dùng CBU-DA-1P thay thế.

### Kết hợp với hệ khác

| Hệ khác | Có thể kết nối? | Phương thức | Yêu cầu thêm |
|:---|:---|:---|:---|
| KNX | ✅ Có | Gateway KNX–Casambi | VBU-K2C-W-BI |
| Matter | ✅ Có | Matter Bridge | Rayrun MTB10 |
| Modbus / BACnet | ⚠️ Gián tiếp | Gateway IP | Lithernet Gateway |
| DMX | ✅ Có | DMX–Casambi converter | casDMX |

---

## Hướng dẫn chọn sản phẩm

### Chọn CBU-A2D khi

- Cần điều khiển 1–2 driver 0-10V qua Casambi, không cần DALI bus phức tạp.
- Muốn làm Tunable White với driver 0-10V Warm/Cool.
- Cần DALI cho 1 driver đơn lẻ mà không muốn đầu tư nguồn DALI riêng.
- Dự án nhỏ, cần thiết bị gọn nhẹ, dễ lắp đặt.

### Không nên chọn CBU-A2D khi

- Cần điều khiển nhiều hơn 2 driver độc lập → dùng CBU-DA-1P (50 driver DALI).
- Driver chỉ có Triac hoặc PWM → dùng CBU-TED (Triac) hoặc CBU-PWM4 (PWM).
- Cần Evolution network (CBU-A2D chỉ hỗ trợ Classic).
- Lắp ngoài trời hoặc trong vỏ kim loại (IP20, BLE bị chặn).

---

## Ví dụ ứng dụng thực tế

### Scenario 1: Phòng họp – Tunable White 0-10V

**Bài toán:** Phòng họp cần điều chỉnh nhiệt độ màu theo giờ — buổi sáng ánh sáng trắng mát để tập trung, chiều tối ấm hơn để thư giãn.

**Giải pháp:** CBU-A2D với profile 0-10V TW kết nối 2 kênh warm/cool của driver Tunable White. Lịch trình tự động cài trong Casambi App, nhân viên cũng có thể điều chỉnh thủ công qua App hoặc công tắc Casambi.

**Thiết bị cần có:**
- CBU-A2D × 1
- Driver LED Tunable White có 2 cổng 0-10V (warm + cool)
- Đèn LED Tunable White tương thích

### Scenario 2: Showroom – DALI DT8 RGB lighting

**Bài toán:** Showroom cần thay đổi màu sắc ánh sáng theo từng khu trưng bày, điều khiển chính xác qua DALI DT8.

**Giải pháp:** CBU-A2D ở chế độ DALI Standalone với profile DALI DT8 RGB/TW, kết nối 1 driver DALI DT8 RGB. Không cần nguồn DALI ngoài — CBU-A2D tự cấp nguồn bus.

**Thiết bị cần có:**
- CBU-A2D × 1 (mỗi khu 1 thiết bị)
- Driver LED DALI DT8 RGB tương thích

---

## Lắp đặt & Commissioning

### Yêu cầu lắp đặt

- Nguồn AC 100–240V tại vị trí lắp.
- Dây 0,5–1,5 mm², tuốt 6–8 mm, xiết 0,4 Nm.
- Không lắp trong vỏ kim loại — Bluetooth bị chặn.
- Không đấu song song 2 kênh ra — hỏng thiết bị vĩnh viễn.
- Relay ở kênh 2 phải có diode chống flyback tích hợp.

### Các bước cơ bản

1. Tắt nguồn, đấu dây AC vào terminal L/N.
2. Đấu driver 0-10V hoặc DALI vào kênh tương ứng.
3. Bật nguồn, mở Casambi App, tạo hoặc vào network.
4. CBU-A2D xuất hiện trong danh sách thiết bị — chọn fixture profile phù hợp.
5. Cấu hình scene, lịch, cảm biến trong App.

> 📄 Hướng dẫn đầy đủ: [casambi.com/product/cbu-a2d](https://casambi.com/product/cbu-a2d/)

---

## FAQ

**CBU-A2D khác gì so với CBU-DA-1P?**
CBU-A2D hỗ trợ cả 0-10V và DALI nhưng chỉ 2 kênh, phù hợp cho hệ thống nhỏ. CBU-DA-1P chỉ hỗ trợ DALI nhưng điều khiển được tối đa 50 driver — phù hợp dự án quy mô lớn hơn.

**CBU-A2D có hỗ trợ Tunable White không?**
Có, theo 2 cách: dùng profile 0-10V TW với 2 kênh warm/cool mixer, hoặc dùng profile DALI DT8 TW nếu driver hỗ trợ DALI DT8 TC color model.

**Standalone DALI nghĩa là gì?**
CBU-A2D vừa là DALI master vừa cấp nguồn bus DALI (12VDC/20mA) — không cần nguồn DALI riêng bên ngoài. Phù hợp cho 1 driver DALI đơn, không phù hợp cho nhiều driver song song.

**Có thể điều khiển CBU-A2D mà không cần App không?**
Có. Flick công tắc nguồn tắt nhanh (<1 giây) rồi bật lại để tăng sáng dần, flick lần 2 để chốt mức sáng. Mức sáng được lưu tự động.

**CBU-A2D có tương thích với Casambi Evolution không?**
Không. CBU-A2D chỉ hoạt động trên Casambi Classic network (tối đa 127 node). Nếu cần Evolution, xem xét các thiết bị Casambi mới hơn có hỗ trợ Evolution firmware.

**Tầm phủ Bluetooth là bao nhiêu?**
Ngoài trời thoáng >50m giữa 2 CBU-A2D. Trong nhà có vật cản hoặc kim loại tầm phủ giảm đáng kể. CBU-A2D đóng vai repeater trong mesh — mỗi node tăng độ phủ toàn hệ thống.

**Giá CBU-A2D là bao nhiêu?**
Vui lòng liên hệ KNXStore để được báo giá chính xác.
👉 Zalo: [0918.918.755](https://zalo.me/0918918755)

