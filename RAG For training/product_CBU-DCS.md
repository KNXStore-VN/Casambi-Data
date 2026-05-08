---
# ================================================================
# BLOCK 1 — IDENTIFICATION
# ================================================================
sku: "CBU-DCS"
product_name: "Casambi CBU-DCS – Bộ điều khiển DALI Bluetooth"
brand: "Casambi"
manufacturer_part_number: "CBU-DCS"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs"
status: "active"

# ================================================================
# BLOCK 2 — CLASSIFICATION
# ================================================================
product_type: "controller"

category_primary: "DALI Controllers"
category_secondary: ["Điều khiển Casambi", "Điều khiển chiếu sáng", "Cảm biến DALI"]

ecosystem: ["Casambi"]
control_bus: ["DALI"]
connectivity: ["BLE"]

# ================================================================
# BLOCK 3 — SEARCH & DISCOVERY
# ================================================================
aliases: ["CBU-DCS", "CBUD-CS", "DCS", "Casambi DALI Controller DCS"]

search_keywords_vi:
  - "bộ điều khiển DALI Casambi"
  - "điều khiển đèn DALI bằng bluetooth"
  - "DALI Casambi cấp điện từ bus"
  - "điều khiển đèn DALI qua app"
  - "daylight harvesting DALI Casambi"
  - "presence detection DALI"
  - "mesh network đèn thông minh"
  - "CBU-DCS Casambi"
  - "DALI DT6 DT8 Casambi nhỏ gọn"

search_keywords_en:
  - "Casambi DALI controller"
  - "DALI bus powered Bluetooth controller"
  - "wireless DALI dimmer Casambi"
  - "DALI sensor integration Casambi"
  - "daylight harvesting DALI"
  - "CBU-DCS Casambi"
  - "DALI DT8 color controller BLE"

# ================================================================
# BLOCK 4 — TARGET & USE CASE
# ================================================================
target_segment: ["system_integrator", "lighting_designer", "me_contractor"]

project_type: ["office", "hotel", "retail", "museum_gallery", "public_building"]

project_scale: ["small", "medium", "large"]

complexity_level: "intermediate"

use_case_tags:
  - "dimming"
  - "tunable_white"
  - "rgb_lighting"
  - "dali_control"
  - "occupancy_control"
  - "daylight_harvesting"
  - "broadcast_control"
  - "sensor_integration"

not_suitable_for:
  - "Driver không hỗ trợ DALI (chỉ có 0-10V hoặc Triac)"
  - "Hệ DALI chưa có nguồn bus — cần dùng CBU-DA-1P thay thế"
  - "Lắp đặt trong vỏ kim loại kín (chặn tín hiệu BLE)"

# ================================================================
# BLOCK 5 — CHATBOT BEHAVIOR
# ================================================================
chatbot_priority: "high"

price_display: "fetch"

display_mode_technical: "text"
display_mode_purchase: "markdown_card"

product_link_text: "👉 [Casambi CBU-DCS – Bộ điều khiển DALI Bluetooth](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs)"

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
  - "user_asks_project_design_support"

# ================================================================
# BLOCK 6 — RELATIONSHIPS
# ================================================================
replaces_sku: []
replaced_by_sku: null
equivalent_skus: ["CBU-DA-1P"]

accessories_required:
  - "Driver LED tương thích DALI DT6 hoặc DT8 (bus phải có nguồn từ driver hoặc nguồn DALI ngoài)"
  - "Casambi App (iOS/Android)"

accessories_recommended:
  - "DALI sensor có DALI power supply tích hợp (presence + daylight)"
  - "DALI-2 push button input devices"

compare_with_skus: ["CBU-DA-1P", "CBU-ASD"]
# CBU-DA-1P: có tích hợp DALI power supply, kích thước lớn hơn, phù hợp khi bus chưa có nguồn
# CBU-ASD: gateway đa kênh, phù hợp hệ lớn 50+ device cần quản lý tập trung

bundle_with: []
upsell_to: ["CBU-DA-1P", "CBU-ASD"]

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
  main: "https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs_3.jpg"
  wiring: ""
  dimensions: ""
  installation: ""
datasheet_url: "https://knxstore.vn/assets/image/catalog/CBU_DCS_Data-Sheet_EU_EN_2_KNXStore_vn.pdf"
manual_url_en: "https://knxstore.vn/assets/image/catalog/CBU_DCS_Data-Sheet_EU_EN_2_KNXStore_vn.pdf"
manual_url_vi: null
profiles_url: ""
certification_docs: ["Casambi certified", "EU WEEE Directive 2002/96/EC"]

# ================================================================
# BLOCK 9 — RAG OPTIMIZATION
# ================================================================
chunk_strategy: "by_section"
priority_sections:
  - "Tổng quan sản phẩm"
  - "Thông số kỹ thuật"
  - "Chức năng chính"
  - "Integration & Compatibility"
  - "Hướng dẫn chọn sản phẩm"
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
source_of_truth: "knxstore.vn product page + knxstore.vn/assets/image/catalog/"
confidence_level: "high"
---

# Casambi CBU-DCS – Bộ điều khiển DALI Bluetooth

## Tổng quan sản phẩm

CBU-DCS là bộ điều khiển DALI của Casambi Technologies (Phần Lan), tích hợp giao thức Casambi qua Bluetooth Low Energy. Thiết bị kết nối mạng Casambi không dây với bus DALI có dây, cho phép điều khiển tối đa 64 địa chỉ DALI từ smartphone hoặc tablet mà không cần gateway hay hub trung gian.

Điểm khác biệt cốt lõi của CBU-DCS so với các bộ điều khiển DALI Casambi khác là nó lấy điện trực tiếp từ DALI bus (9.5–22.5 VDC) — không cần nguồn AC riêng, tiêu thụ chỉ 5 mA ở idle. Kích thước siêu nhỏ (40.4 × 36.3 × 14 mm) cho phép gắn trực tiếp bên trong đèn hoặc fixture mà không chiếm không gian lắp đặt. CBU-DCS phù hợp với các dự án chiếu sáng thương mại và dân dụng cao cấp — văn phòng, khách sạn, bảo tàng, công trình công cộng — đặc biệt khi DALI bus đã có sẵn nguồn từ driver.

👉 [Xem sản phẩm trên KNXStore](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs)

---

## Thông số kỹ thuật

| Thông số | Giá trị |
|:---|:---|
| Điện áp đầu vào | 9.5–22.5 VDC (từ DALI bus) |
| Dòng điện idle | 5 mA |
| Dòng điện peak | 30 mA |
| Dòng DALI bus tối đa | 250 mA |
| Công suất chờ | < 0.1 W |
| Nhiệt độ hoạt động | −20°C đến +55°C |
| Nhiệt độ vỏ tối đa (Tc) | +65°C |
| Kích thước | 40.4 × 36.3 × 14.0 mm |
| Trọng lượng | 15 g |
| Cấp bảo vệ | IP20 |
| Cách ly | Reinforced (vỏ đến DALI bus) |
| Xuất xứ | Finland (Casambi Technologies Oy) |
| Bảo hành | 24 tháng |

**Thông số DALI bus**

| Thông số | Giá trị |
|:---|:---|
| Loại terminal | Push-button press terminal (không dùng tua vít) |
| Tiết diện dây | 0.5–1.5 mm² (solid) / 16–20 AWG |
| Chiều dài thoát dây | 6–8 mm |
| Cấu hình kết nối | 2 bộ terminal song song nội bộ — DALI bus xuyên qua thiết bị |
| Số địa chỉ DALI tối đa | 64 (short address 0–63) |
| Chuẩn hỗ trợ | DALI DT6, DALI DT8 |

**Thông số Casambi / BLE**

| Thông số | Giá trị |
|:---|:---|
| Công nghệ kết nối | Bluetooth Low Energy |
| Giao thức | Casambi (Classic & Evolution) |
| Dải tần số | 2400–2480 MHz |
| Công suất phát tối đa | +4 dBm |
| Phạm vi ngoài trời | Tối đa 50 m |
| Phạm vi có vật cản | ~30 m |
| Kiến trúc mạng | Mesh — mỗi unit là repeater tự động |

---

## Chức năng chính

### Điều khiển DALI không dây qua Casambi

CBU-DCS nhận lệnh từ mạng Casambi qua BLE và phát lệnh DALI xuống bus đèn. Người dùng điều khiển qua Casambi App trên smartphone hoặc tablet — không cần bảng điều khiển có dây, không cần hub trung gian. Toàn bộ logic (scene, lịch trình, cảm biến) lưu trong Casambi network, hoạt động hoàn toàn offline không phụ thuộc internet.

### Hỗ trợ 50+ Fixture Profile

Thiết bị hỗ trợ đầy đủ các chế độ điều khiển DALI: Broadcast, Short Address, DT6 (dimming cơ bản), DT8 (màu sắc nâng cao — Tunable White, RGB, RGBW, XY), và các profile cảm biến. Profile mặc định là Broadcast (#8079) — không cần addressing, phù hợp triển khai nhanh toàn bus.

### Tích hợp cảm biến DALI

Khi chọn đúng Fixture Profile (ví dụ "Sensors (Daylight, Presence)" hoặc "BC+Sensors"), cảm biến DALI kết nối trên bus sẽ xuất hiện như Casambi sensor trong App. Điều này cho phép thiết lập automation daylight harvesting và occupancy control hoàn toàn trong Casambi — điều kiện là cảm biến có DALI power supply tích hợp.

### Cấp điện từ DALI bus, không cần nguồn riêng

CBU-DCS chỉ tiêu thụ 5 mA ở idle và 30 mA ở peak — không gây tải đáng kể cho DALI bus. Không cần kéo thêm dây nguồn AC đến vị trí lắp; chỉ cần 2 dây DA1/DA2 từ bus là đủ. Đây là lợi thế lớn khi gắn trực tiếp bên trong fixture hoặc tại các vị trí hạn chế không gian.

### Mesh repeater tự động

Mỗi CBU-DCS đồng thời đóng vai trò repeater trong mạng Casambi mesh — tự động mở rộng phủ sóng khi thêm thiết bị vào network mà không cần cấu hình riêng. Mạng Casambi hỗ trợ tối đa 250 node.

---

## Fixture Profiles

### Profile Broadcast & Dimming cơ bản

| Profile | Mô tả |
|:---|:---|
| **Broadcast** (default #8079) | Phát DALI broadcast — không cần địa chỉ, điều khiển toàn bus cùng lúc |
| 1CH | Dimmer 1 kênh, địa chỉ DALI #0 |
| 1CH + Sensors | Dimmer 1 kênh kết hợp đọc cảm biến DALI |
| 2CH Dim Mixer | 2 kênh dimmer, tổng công suất = mức sáng cài đặt |
| 4xDim | 4 kênh dimmer độc lập, địa chỉ #0–3 |
| 8CH [Evolution] | 8 kênh với custom elements, yêu cầu Casambi Evolution |

### Profile Tunable White & Màu (DT8)

| Profile | Mô tả |
|:---|:---|
| 2CH TW | 2 kênh warm/cool — tunable white qua 2 driver riêng |
| DALI8/Dim,TW | DT8 Tunable White — driver tự mix warm/cool |
| DALI8/Dim,RGB | DT8 RGB — 3 kênh màu theo chuẩn DALI DT8 |
| DALI8/Dim,RGBW | DT8 RGBW — 4 kênh màu |
| DALI8/Dim,RGB,TW | DT8 RGB hoặc TC, loại trừ lẫn nhau |
| DALI8/Dim,XY [Evolution] | DT8 XY color — yêu cầu Casambi Evolution |
| DALI8/Dim,XY,TW [Evolution] | DT8 XY color + temperature — yêu cầu Evolution |

### Profile Cảm biến DALI

| Profile | Mô tả |
|:---|:---|
| Sensors (Daylight, Presence) | Đọc cảm biến hiện diện + ánh sáng, chế độ pass-through |
| Sensors (daylight control) | Chỉ đọc ánh sáng, pass-through |
| Sensors (Lux, Presence) | Đọc lux + hiện diện, pass-through |
| BC+Sensors | Broadcast kết hợp đọc cảm biến |
| DALI PushButton Coupler [Evolution] | Scene selection + điều chỉnh ánh sáng, yêu cầu Evolution |

---

## Integration & Compatibility

### Hoạt động trong hệ Casambi

Trong hệ Casambi, CBU-DCS là một node BLE hoạt động như DALI master. Thiết bị tham gia vào Casambi network (Classic hoặc Evolution), nhận lệnh từ App hoặc từ các node Casambi khác, và phát lệnh DALI tương ứng xuống bus.

Mỗi Casambi network hỗ trợ tối đa 250 node — CBU-DCS chiếm 1 node. Các driver DALI trên bus không chiếm node Casambi; chúng được quản lý thông qua Fixture Profile của CBU-DCS.

**Yêu cầu:** Casambi App (iOS/Android); DALI bus phải có nguồn cấp từ driver LED tích hợp DALI power supply hoặc nguồn DALI ngoài.  
**Giới hạn:** Tối đa 64 địa chỉ DALI (0–63) trên một CBU-DCS. Các profile Evolution yêu cầu Casambi Evolution license.

### Điều khiển qua DALI bus

CBU-DCS là DALI master — phát lệnh xuống bus và đọc phản hồi từ cảm biến DALI. Hai đầu kết nối DALI nối song song bên trong thiết bị, cho phép DALI bus đi xuyên qua mà không cần đấu nối thêm. Trên cùng một bus DALI chỉ được có 1 master.

**Tương thích:** Driver DALI DT6 (dimming cơ bản), DT8 (color/tunable white), cảm biến DALI có DALI power supply tích hợp.  
**Không tương thích:** Driver 0-10V, PWM, Triac, hoặc bất kỳ chuẩn non-DALI nào.

### Kết hợp với hệ khác

| Hệ khác | Có thể kết nối? | Phương thức | Yêu cầu thêm |
|:---|:---|:---|:---|
| KNX | ✅ Có | Gateway KNX–Casambi | VBU-K2C-W-BI hoặc tương đương |
| Matter | ✅ Có | Casambi–Matter Bridge | Rayrun MTB10 hoặc tương đương |
| Modbus | ⚠️ Gián tiếp | Qua Casambi Cloud API + middleware | Cần lập trình tích hợp |
| BACnet | ⚠️ Gián tiếp | Qua gateway BACnet–Casambi | Lithernet Gateway |
| 0-10V | ❌ Không trực tiếp | — | Cần dùng CBU-A2D thay thế |

> 💡 **Lưu ý tích hợp đa hệ:** Khi KNX và Casambi cùng điều khiển một vùng đèn qua gateway, Casambi luôn ưu tiên lệnh local (BLE) hơn lệnh từ KNX. Độ trễ từ KNX → Casambi → DALI thường trong khoảng 300–500 ms.

---

## Hướng dẫn chọn sản phẩm

### Chọn CBU-DCS khi

- DALI bus đã có nguồn cấp từ driver LED hoặc nguồn DALI ngoài — không cần kéo thêm nguồn AC đến vị trí lắp.
- Cần thiết bị nhỏ gọn để gắn trực tiếp bên trong đèn hoặc fixture (40.4 × 36.3 × 14 mm, 15 g).
- Dự án tích hợp cảm biến DALI (presence, daylight) vào hệ Casambi.
- Cần điều khiển màu sắc DT8 (tunable white, RGB, RGBW) qua Casambi.
- Quy mô dưới 64 DALI device và ưu tiên lắp đặt gọn, ít dây.

### Không nên chọn CBU-DCS khi

- DALI bus chưa có nguồn cấp — dùng CBU-DA-1P thay thế (tích hợp DALI power supply 100 mA, cấp nguồn cho cả bus từ nguồn AC).
- Cần quản lý hơn 64 DALI device trên cùng một network — xem xét CBU-ASD.
- Thiết bị bắt buộc lắp trong vỏ kim loại kín — BLE sẽ bị suy giảm hoặc mất tín hiệu.
- Hệ thống dùng chuẩn điều khiển khác DALI (0-10V, PWM, Triac).

---

## Ví dụ ứng dụng thực tế

### Scenario 1: Văn phòng – Tiết kiệm năng lượng với daylight harvesting và presence detection

**Bài toán:** Văn phòng muốn đèn tự động điều chỉnh theo ánh sáng tự nhiên và tắt khi không có người, trong khi hệ DALI đã lắp sẵn với driver có tích hợp DALI power supply.

**Giải pháp:** Gắn CBU-DCS trực tiếp vào DALI bus hiện có — lấy điện từ bus, không thêm nguồn. Kết hợp cảm biến DALI (presence + lux), chọn profile "Sensors (Daylight, Presence)" trong Casambi App, cài automation dim đèn theo lux và tắt sau 5 phút không có người.

**Thiết bị cần có:**
- CBU-DCS × (số zone)
- DALI sensor có DALI power supply tích hợp × (1 sensor/zone)
- App Casambi (miễn phí)

### Scenario 2: Bảo tàng / Gallery – Điều khiển nhiệt độ màu theo từng bộ sưu tập

**Bài toán:** Phòng trưng bày cần thay đổi linh hoạt từ warm white (3000K) sang neutral white (4000K) tùy bộ sưu tập, curator điều khiển từ iPad mà không cần can thiệp hạ tầng điện.

**Giải pháp:** CBU-DCS với profile "DALI8/Dim,TW" kết hợp driver DALI DT8 tunable white. Curator tạo và lưu scene trong Casambi App, kích hoạt bằng 1 chạm — thay đổi toàn bộ không gian tức thời mà không cần thợ điện hỗ trợ.

**Thiết bị cần có:**
- CBU-DCS × (số zone)
- DALI DT8 LED driver (tunable white)
- App Casambi (miễn phí)

---

## Lắp đặt & Commissioning

### Yêu cầu lắp đặt

- DALI bus phải được cấp nguồn trước — từ driver LED DALI có DALI power supply tích hợp hoặc nguồn DALI riêng biệt. CBU-DCS không tự cấp nguồn cho bus.
- Không đặt trong vỏ kim loại kín — BLE sẽ bị suy giảm hoặc mất tín hiệu hoàn toàn.
- Polarity DA1/DA2 không quan trọng — đấu theo chiều nào cũng hoạt động.
- Chỉ dùng dây solid 0.5–1.5 mm², thoát dây 6–8 mm; terminal kiểu push-button, không dùng tua vít.
- Chỉ thợ điện có chuyên môn mới thực hiện đấu nối.

### Các bước cơ bản

1. Xác nhận DALI bus đã có nguồn (kiểm tra điện áp DA1/DA2 trong khoảng 9.5–22.5 VDC).
2. Đấu 2 dây DA1/DA2 từ bus vào terminal tương ứng trên CBU-DCS (không phân cực).
3. Cấp điện — đèn LED trên thiết bị nháy xác nhận khởi động.
4. Mở Casambi App, thêm CBU-DCS vào network, chọn Fixture Profile phù hợp.
5. Đánh địa chỉ DALI nếu dùng profile Short Address (tự động hoặc thủ công tùy profile).
6. Tạo scene, lịch trình và cấu hình cảm biến trong App.
7. Kiểm tra phủ sóng BLE sau lắp đặt — bổ sung CBU-DCS thêm nếu vùng nào yếu tín hiệu.

> 📄 Hướng dẫn đầy đủ: [Datasheet CBU-DCS](https://knxstore.vn/assets/image/catalog/CBU_DCS_Data-Sheet_EU_EN_2_KNXStore_vn.pdf)

---

## FAQ

**CBU-DCS có cần nguồn AC riêng không?**  
Không — thiết bị lấy điện trực tiếp từ DALI bus (9.5–22.5 VDC), tiêu thụ chỉ 5 mA ở idle. Tuy nhiên, DALI bus phải được cấp nguồn từ driver LED có tích hợp DALI power supply hoặc nguồn DALI ngoài. CBU-DCS không tự tạo ra nguồn bus.

**Sự khác biệt giữa CBU-DCS và CBU-DA-1P là gì?**  
CBU-DA-1P có tích hợp DALI power supply (100 mA) — tự cấp nguồn cho cả DALI bus, lấy điện từ nguồn AC 110–277V. CBU-DCS không có tính năng này; bù lại, nó nhỏ hơn đáng kể (15 g vs 58 g) và phù hợp gắn trực tiếp trong fixture. Nếu bus đã có nguồn, CBU-DCS là lựa chọn gọn hơn. Nếu bus chưa có nguồn, dùng CBU-DA-1P.

**CBU-DCS điều khiển được tối đa bao nhiêu đèn?**  
Tối đa 64 địa chỉ DALI (short address 0–63) trên một CBU-DCS. Với profile Broadcast, không cần addressing — điều khiển toàn bộ thiết bị trên bus cùng lúc mà không bị giới hạn số lượng theo địa chỉ.

**CBU-DCS có hoạt động với cảm biến DALI không?**  
Có, với điều kiện cảm biến là loại DALI controllable và có DALI power supply tích hợp. Chọn đúng profile trong App (ví dụ "Sensors (Daylight, Presence)") để CBU-DCS đọc dữ liệu cảm biến và tích hợp vào automation Casambi.

**CBU-DCS có cần internet để hoạt động không?**  
Không. Casambi hoạt động hoàn toàn qua Bluetooth Mesh — điều khiển local không cần internet, không cần cloud. Internet chỉ cần nếu muốn điều khiển từ xa qua Casambi Cloud Gateway.

**CBU-DCS có thể tích hợp với KNX không?**  
Có, thông qua gateway KNX–Casambi (ví dụ: VBU-K2C-W-BI). KNX gửi lệnh đến gateway, gateway dịch sang Casambi, Casambi điều khiển CBU-DCS và bus DALI. Độ trễ từ KNX → DALI thường 300–500 ms.

**Giá CBU-DCS là bao nhiêu?**  
Vui lòng liên hệ KNXStore để được báo giá chính xác và kiểm tra tồn kho.  
👉 Zalo: [0918.918.755](https://zalo.me/0918918755)

---

## Hiển thị sản phẩm

### Khi trả lời câu hỏi kỹ thuật

> 📄 [Datasheet CBU-DCS](https://knxstore.vn/assets/image/catalog/CBU_DCS_Data-Sheet_EU_EN_2_KNXStore_vn.pdf) | 🛒 [Xem sản phẩm trên KNXStore](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs)

### Khi tư vấn mua hàng — render Markdown card

Khi có giá:
```
![Casambi CBU-DCS](https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs_3.jpg)
**[Casambi CBU-DCS – Bộ điều khiển DALI Bluetooth](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs)**
DALI master Casambi BLE, cấp điện từ bus, kích thước siêu nhỏ, hỗ trợ DT6/DT8/TW/RGB/RGBW và cảm biến DALI.
💰 [GIÁ FETCH TỪ TRANG] (Giá đã bao gồm VAT)
👉 [Xem sản phẩm](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs) | 📞 [Nhận báo giá](https://zalo.me/0918918755)
```

Khi không có giá / Make to order:
```
![Casambi CBU-DCS](https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs_3.jpg)
**[Casambi CBU-DCS – Bộ điều khiển DALI Bluetooth](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs)**
DALI master Casambi BLE, cấp điện từ bus, kích thước siêu nhỏ, hỗ trợ DT6/DT8/TW/RGB/RGBW và cảm biến DALI.
💰 Liên hệ báo giá
👉 [Xem sản phẩm](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs) | 📞 [Nhận báo giá](https://zalo.me/0918918755)
```

### Khi khách hỏi báo giá dự án

Thu thập: loại công trình, số zone / số driver DALI, driver đang dùng (DT6 hay DT8, có DALI power supply không), thời gian triển khai. Sau đó:

> "Cảm ơn bạn đã cung cấp thông tin. Giá dự án phụ thuộc vào số lượng và loại khách hàng nên đội ngũ KNXStore sẽ tư vấn trực tiếp để đảm bảo bạn nhận được mức giá tốt nhất.
>
> 👉 Liên hệ sales qua Zalo: **[0918.918.755](https://zalo.me/0918918755)**
> hoặc để lại số điện thoại / email, KNXStore sẽ chủ động liên hệ lại."

---

## Tài liệu kỹ thuật

📄 [Datasheet – Casambi CBU-DCS](https://knxstore.vn/assets/image/catalog/CBU_DCS_Data-Sheet_EU_EN_2_KNXStore_vn.pdf)  
🛒 [Trang sản phẩm KNXStore](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-bluetooth-cbu-dcs)

---

## Bảo hành & Hỗ trợ

- Bảo hành: 24 tháng từ ngày xuất hóa đơn
- Hỗ trợ kỹ thuật: knxstore.vn hoặc Zalo [0918.918.755](https://zalo.me/0918918755)