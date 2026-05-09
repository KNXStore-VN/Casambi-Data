---
# ================================================================
# BLOCK 1 — IDENTIFICATION
# ================================================================
sku: "CBU-ASD-LR"                # Lấy từ cột sku_extracted trong casambi_full_sku.csv
product_name: "Casambi CBU-ASD-LR – Bộ điều khiển LED Driver DALI & 0-10V"
brand: "Casambi"
manufacturer_part_number: "CBU-ASD-LR"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/casambi-bo-dieu-khien-led-drivers-dali-0-10v-bluetooth-cbu-asd"
status: "active"

# ================================================================
# BLOCK 2 — CLASSIFICATION
# ================================================================
product_type: "controller"

category_primary: "Điều khiển 0-10V"
category_secondary: ["DALI Controllers", "Lighting Control", "Casambi"]

ecosystem: ["Casambi"]
control_bus: ["DALI", "0-10V"]
connectivity: ["BLE"]

# ================================================================
# BLOCK 3 — SEARCH & DISCOVERY
# ================================================================
aliases: ["CBU-ASD-LR", "CBU-ASD", "ASD-LR", "Casambi ASD"]

search_keywords_vi:
  - "bộ điều khiển LED driver DALI 0-10V Casambi"
  - "CBU-ASD-LR Casambi long range"
  - "dimmer DALI 0-10V Casambi"
  - "điều khiển đèn LED Bluetooth long range"
  - "Casambi standalone DALI SSR relay"
  - "bộ điều khiển RGB tunable white DALI"
  - "CBU-ASD Casambi controller"
  - "long range Bluetooth dimmer Casambi"

search_keywords_en:
  - "CBU-ASD-LR Casambi long range DALI"
  - "Casambi LED driver controller 0-10V DALI"
  - "standalone DALI Casambi SSR relay"
  - "long range BLE DALI controller"
  - "Casambi RGB tunable white DALI"
  - "CBU-ASD datasheet"

# ================================================================
# BLOCK 4 — TARGET & USE CASE
# ================================================================
target_segment: ["system_integrator", "lighting_designer"]

project_type: ["office", "hotel", "retail", "residential_premium", "industrial"]

project_scale: ["small", "medium", "large"]

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
  - "long_range_mesh"

not_suitable_for:
  - "Dùng độc lập không có LED driver DALI hoặc 0-10V"
  - "Lắp đặt ngoài trời (IP20)"
  - "Lắp trong vỏ kim loại (chặn tín hiệu Bluetooth)"
  - "Kết nối trực tiếp nguồn mains vào relay output (SSR chỉ dùng cho external relay)"

# ================================================================
# BLOCK 5 — CHATBOT BEHAVIOR
# ================================================================
chatbot_priority: "high"

price_display: "fetch"
display_mode_technical: "text"
display_mode_purchase: "markdown_card"

product_link_text: "👉 [Casambi CBU-ASD-LR – Bộ điều khiển LED Driver DALI & 0-10V](https://knxstore.vn/products/casambi-bo-dieu-khien-led-drivers-dali-0-10v-bluetooth-cbu-asd)"

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
  - "user_asks_custom_profile"

# ================================================================
# BLOCK 6 — RELATIONSHIPS
# ================================================================
replaces_sku: []
replaced_by_sku: null
equivalent_skus: []

accessories_required:
  - "LED driver tương thích DALI hoặc 0-10V"
  - "Casambi App (iOS/Android)"

accessories_recommended:
  - "Cảm biến PIR (presence/daylight harvesting)"
  - "Công tắc wall switch (push on/off)"
  - "External relay (nếu dùng SSR relay output)"

compare_with_skus: ["CBU-A2D", "CBU-DA-1P"]
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
  main: "https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-led-drivers-dali-0-10v-bluetooth-cbu-asd_3.jpg"
  wiring: ""
  dimensions: ""
  installation: ""
datasheet_url: "https://knxstore.vn/assets/image/catalog/casambi-bo-dieu-khien-led-drivers-dali-0-10v-bluetooth-cbu-asd.pdf"
manual_url_en: "https://knxstore.vn/assets/image/catalog/casambi-bo-dieu-khien-led-drivers-dali-0-10v-bluetooth-cbu-asd.pdf"
manual_url_vi: null
certification_docs: ["CE", "Casambi certified"]

# ================================================================
# BLOCK 9 — RAG OPTIMIZATION
# ================================================================
chunk_strategy: "by_section"
priority_sections:
  - "Tổng quan sản phẩm"
  - "Thông số kỹ thuật"
  - "Chế độ output"
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
source_of_truth: "knxstore.vn product page + CBU-ASD-LR source file"
confidence_level: "high"
---

# Casambi CBU-ASD-LR – Bộ điều khiển LED Driver DALI & 0-10V

## Tổng quan sản phẩm

CBU-ASD-LR là bộ điều khiển LED driver của Casambi (Phần Lan), tích hợp Bluetooth Long-Range, hỗ trợ cả DALI Standalone và 0-10V trong cùng một thiết bị. Điểm khác biệt so với các CBU thông thường là tầm phủ Bluetooth mở rộng — 50m trong nhà và lên đến 200m ngoài trời khoáng đãng khi dùng Long-Range mode.

CBU-ASD-LR phù hợp với các dự án chiếu sáng thương mại cần điều khiển RGB, Tunable White, đa kênh dimming, hoặc kết hợp cảm biến hiện diện và daylight harvesting. Tích hợp SSR relay output cho phép điều khiển on/off mains qua external relay mà không cần thêm module riêng.

👉 [Xem sản phẩm trên KNXStore](https://knxstore.vn/products/casambi-bo-dieu-khien-led-drivers-dali-0-10v-bluetooth-cbu-asd)

---

## Thông số kỹ thuật

| Thông số | Giá trị |
|:---|:---|
| Điện áp đầu vào | 220–240 VAC, 50 Hz |
| Dòng điện đầu vào tối đa | 0,6 A |
| Relay output (SSR) | 220–240 VAC phase switching |
| 0-10V output | 0–10 VDC, tối đa 6 mA (isolated) |
| DALI output | 9–12 VDC, tối đa 6 mA (standalone) |
| Nhiệt độ vận hành | -20°C đến +50°C |
| Nhiệt độ vỏ tối đa (Tc) | +75°C |
| Độ ẩm tối đa | 0–80%, không ngưng tụ |
| Kích thước (D×R×C) | 56,5 × 35,8 × 22,3 mm |
| Trọng lượng | 48 g |
| Cấp bảo vệ | IP20 (chỉ trong nhà) |
| Cấp bảo vệ điện | Class II |
| Xuất xứ | Phần Lan |
| Bảo hành | 24 tháng |

**Thông số Bluetooth**

| Thông số | Giá trị |
|:---|:---|
| Giao thức | Casambi (Bluetooth Low Energy) |
| Tần số hoạt động | 2402–2480 MHz |
| Công suất phát tối đa | +8 dBm |
| Tầm phủ trong nhà | 50 m |
| Tầm phủ ngoài trời (Long-Range) | 200 m |

---

## Chức năng chính

### DALI Standalone tích hợp nguồn bus

CBU-ASD-LR cấp nguồn bus DALI (9–12VDC, 6mA) trực tiếp — không cần nguồn DALI ngoài. Driver DALI kết nối thẳng vào thiết bị, đơn giản hóa sơ đồ đấu dây. Phù hợp cho 1 driver DALI đơn hoặc hệ thống nhỏ có ít driver.

### Long-Range Bluetooth

CBU-ASD-LR dùng chip BLE Long-Range (+8 dBm, hỗ trợ Coded PHY), tầm phủ tăng gấp 4 lần so với CBU thông thường — lên đến 200m ngoài trời. Phù hợp cho không gian rộng như nhà kho, kho lạnh, outdoor covered area, hoặc công trình có nhiều tầng cần mesh coverage tốt.

### SSR Relay output

Tích hợp SSR relay output (phase switching 220–240VAC) để kết nối external relay bật/tắt mains. Lưu ý quan trọng: relay output của CBU-ASD-LR chỉ dành cho external relay — không kết nối trực tiếp driver mains vào relay output này.

### 0-10V Isolated output

Kênh 0-10V được cách ly (isolated), tối đa 6mA — phù hợp cho driver LED 0-10V thương mại. Cách ly điện giúp tránh nhiễu trong hệ thống phức tạp có nhiều nguồn điện khác nhau.

### Dimming không cần App

Hỗ trợ flick method qua wall switch: tắt nhanh (<1 giây) rồi bật lại để tăng sáng dần, flick lần 2 để chốt mức sáng. Mức sáng được lưu tự động.

---

## Chế độ output

CBU-ASD-LR hoạt động theo 2 chế độ chính, cấu hình qua Fixture Profile trong Casambi App:

**Chế độ DALI Standalone** — CBU-ASD-LR là DALI master, cấp nguồn bus, hỗ trợ DT6 và DT8. Dùng cho RGB, Tunable White, đa kênh dimming.

**Chế độ 0-10V** — Điều chỉnh driver LED 0-10V qua analog signal cách ly. Dùng cho dimming đơn giản hoặc kết hợp với SSR relay để on/off hoàn toàn.

---

## Fixture Profiles

### DALI Profiles

| Profile | Mô tả |
|:---|:---|
| DALI Broadcast | Broadcast dimmer cơ bản, DT6 |
| DALI DT8 Tunable White | TW 2700–6500K hoặc 3000–5000K |
| DALI DT8 RGB | RGB color control |
| DALI DT8 RGB+TW | RGB kết hợp Tunable White |
| DALI DT8 RGBW | RGBW với slider White riêng |
| DALI 2xDim | 2 kênh dimmer độc lập (warm/cool mixer) |
| DALI 4xDim | 4 kênh dimmer độc lập |
| DALI Sensors | Broadcast + cảm biến presence/daylight |

### 0-10V Profile

| Profile | Mô tả |
|:---|:---|
| 0-10V Basic | 1 kênh dimming cơ bản |

---

## Integration & Compatibility

### Hoạt động trong hệ Casambi

CBU-ASD-LR hỗ trợ cả Casambi Classic và Evolution network. Với Long-Range mode, thiết bị hoạt động như một repeater mạnh trong mesh, đặc biệt hữu ích ở các vị trí xa hoặc khó phủ sóng. Long-Range mode chỉ khả dụng trên Evolution network.

**Yêu cầu:** Casambi App (iOS/Android). Long-Range mode cần Evolution network và thiết bị hỗ trợ CBM-003 chip (Bluetooth 5.0).
**Giới hạn:** DALI output 6mA — chỉ đủ cho 1 driver đơn. Nhiều driver DALI → dùng CBU-DA-1P.

### Kết hợp với hệ khác

| Hệ khác | Có thể kết nối? | Phương thức | Yêu cầu thêm |
|:---|:---|:---|:---|
| KNX | ✅ Có | Gateway KNX–Casambi | VBU-K2C-W-BI |
| Matter | ✅ Có | Matter Bridge | Rayrun MTB10 |
| Modbus / BACnet | ⚠️ Gián tiếp | Gateway IP | Lithernet Gateway |
| DMX | ✅ Có | DMX–Casambi converter | casDMX |

---

## Hướng dẫn chọn sản phẩm

### Chọn CBU-ASD-LR khi

- Cần tầm phủ Bluetooth xa hơn CBU thông thường — không gian rộng, nhà kho, outdoor covered.
- Dự án dùng Evolution network và muốn tận dụng Long-Range mesh.
- Cần kết hợp DALI + SSR relay trong 1 thiết bị.
- Điều khiển 1 driver DALI DT8 RGB/RGBW/TW đơn lẻ.

### Không nên chọn CBU-ASD-LR khi

- Cần điều khiển nhiều driver DALI (>1) → dùng CBU-DA-1P (50 driver).
- Chỉ cần tầm phủ thông thường và muốn tiết kiệm chi phí → CBU-A2D.
- Driver chỉ hỗ trợ Triac hoặc PWM → CBU-TED hoặc CBU-PWM4.
- Lắp ngoài trời hoặc trong vỏ kim loại (IP20, BLE bị chặn).

---

## Ví dụ ứng dụng thực tế

### Scenario 1: Nhà kho lớn – Long-Range mesh coverage

**Bài toán:** Nhà kho 5000m² cần điều khiển đèn LED công nghiệp theo vùng, kết hợp cảm biến hiện diện. Khoảng cách giữa các đèn xa, tín hiệu Bluetooth thông thường không đủ phủ.

**Giải pháp:** CBU-ASD-LR với Long-Range mode tạo mesh coverage rộng hơn, mỗi node phủ đến 50m trong nhà. Kết hợp profile DALI Sensors để tự tắt đèn khi không có người — tiết kiệm điện đáng kể.

**Thiết bị cần có:**
- CBU-ASD-LR × theo số lượng vùng
- Driver LED DALI tương thích
- Casambi Evolution network

### Scenario 2: Gallery / Bảo tàng – DALI DT8 RGB chính xác

**Bài toán:** Gallery cần ánh sáng màu sắc thay đổi linh hoạt theo từng khu trưng bày, điều khiển chính xác qua DALI DT8 RGB.

**Giải pháp:** CBU-ASD-LR với profile DALI DT8 RGB kết nối driver LED DALI DT8. Scene ánh sáng cài sẵn trong Casambi App, nhân viên kích hoạt bằng 1 chạm.

**Thiết bị cần có:**
- CBU-ASD-LR × 1 per khu
- Driver LED DALI DT8 RGB
- Casambi App

---

## Lắp đặt & Commissioning

### Yêu cầu lắp đặt

- Nguồn AC 220–240V tại vị trí lắp.
- Không lắp trong vỏ kim loại — Bluetooth bị chặn.
- SSR relay output chỉ dùng cho external relay — không kết nối trực tiếp driver mains vào relay output.
- DALI output 6mA — không kết nối nhiều driver DALI song song.

### Các bước cơ bản

1. Tắt nguồn, đấu dây AC 220–240V vào terminal L/N.
2. Kết nối driver DALI hoặc 0-10V vào output tương ứng.
3. Bật nguồn, mở Casambi App, thêm vào network.
4. Chọn Fixture Profile phù hợp với loại driver đang dùng.
5. Cấu hình scene, lịch, cảm biến trong App.

> 📄 Hướng dẫn đầy đủ: [Datasheet CBU-ASD-LR](https://knxstore.vn/assets/image/catalog/casambi-bo-dieu-khien-led-drivers-dali-0-10v-bluetooth-cbu-asd.pdf)

---

## FAQ

**CBU-ASD-LR khác gì so với CBU-A2D?**
CBU-ASD-LR có tầm phủ Bluetooth xa hơn (Long-Range, +8 dBm vs +4 dBm), hỗ trợ cả Classic và Evolution network, tích hợp SSR relay output. CBU-A2D có 2 kênh ra (vs 1 DALI + 1 0-10V của ASD-LR) nhưng chỉ hỗ trợ Classic network.

**Long-Range mode hoạt động như thế nào?**
CBU-ASD-LR dùng chip Bluetooth 5.0 hỗ trợ Coded PHY (Long-Range), tăng tầm phủ lên đến 200m ngoài trời. Long-Range mode chỉ khả dụng khi dùng Evolution network — không dùng được với Classic network.

**SSR relay output dùng để làm gì?**
SSR relay là phase switching output cho external relay — không kết nối trực tiếp driver hay tải mains vào đây. Dùng để bật/tắt hoàn toàn mạch điện qua relay ngoài khi driver không hỗ trợ tắt hoàn toàn qua DALI/0-10V.

**DALI output 6mA có đủ cho nhiều driver không?**
Không. 6mA chỉ đủ cho 1 driver DALI đơn. Nếu cần điều khiển nhiều driver DALI, dùng CBU-DA-1P (50 driver, 100mA DALI bus) thay thế.

**Có thể dùng CBU-ASD-LR ngoài trời không?**
Không. IP20 chỉ dành cho trong nhà. Ngoài trời cần IP65 trở lên. Tầm phủ 200m ngoài trời là khoảng cách giữa 2 node, không có nghĩa thiết bị được lắp ngoài trời.

**Giá CBU-ASD-LR là bao nhiêu?**
Vui lòng liên hệ KNXStore để được báo giá chính xác.
👉 Zalo: [0918.918.755](https://zalo.me/0918918755)

