# Casambi CBU-BLIND-2P – Bộ Điều Khiển Động Cơ Rèm
<!-- 
  KNXSTORE PRODUCT KNOWLEDGE FILE
  Template version: 2.0
  Dùng cho: chatbot RAG, product page, sales support
  Cập nhật: 2026-05-08
-->

---
# ================================================================
# BLOCK 1 — IDENTIFICATION
# ================================================================
sku: "CBU-BLIND-2P"
product_name: "Casambi CBU-BLIND-2P – Bộ Điều Khiển Động Cơ Rèm 2 Kênh 2A"
brand: "Casambi"
manufacturer_part_number: "CBU-BLIND-2P"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/bo-dieu-khien-dong-co-rem-casambi-2-kenh-2a-casambi-cbu-blind-2p"
status: "active"

# ================================================================
# BLOCK 2 — CLASSIFICATION
# ================================================================
product_type: "actuator"

category_primary: "Motor Controllers"
category_secondary: ["Blind & Shutter Control", "Casambi", "Home Automation"]

ecosystem: ["Casambi"]
control_bus: []
connectivity: ["BLE"]

# ================================================================
# BLOCK 3 — SEARCH & DISCOVERY
# ================================================================
aliases: ["CBU-BLIND", "Blind Controller 2P", "CBUBLIND2P"]

search_keywords_vi:
  - "điều khiển rèm Casambi"
  - "bộ điều khiển động cơ rèm Bluetooth"
  - "cửa cuốn Casambi"
  - "motor rèm smart home"
  - "2 kênh 2A rèm"
  - "điều khiển rèm không dây"

search_keywords_en:
  - "Casambi blind motor controller"
  - "shutter controller Bluetooth"
  - "wireless blind control 2 channel"
  - "Casambi BLE motor actuator"

# ================================================================
# BLOCK 4 — TARGET & USE CASE
# ================================================================
target_segment:
  - "system_integrator"
  - "smart_home_diy"
  - "me_contractor"

project_type:
  - "residential_premium"
  - "office"
  - "hotel"

project_scale: ["small", "medium", "large"]
complexity_level: "intermediate"

use_case_tags:
  - "blind_control"
  - "motor_control"
  - "home_automation"
  - "smart_shutter"

not_suitable_for:
  - "DC motors"
  - "high_power_loads (trên 2A mỗi kênh)"
  - "lắp đặt trong hộp kim loại kín không có khe thoát RF"

# ================================================================
# BLOCK 5 — CHATBOT BEHAVIOR
# ================================================================
chatbot_priority: "high"
price_display: "fetch"
display_mode_technical: "text"
display_mode_purchase: "markdown_card"
product_link_text: "👉 [Casambi CBU-BLIND-2P – Bộ điều khiển động cơ rèm](https://knxstore.vn/products/bo-dieu-khien-dong-co-rem-casambi-2-kenh-2a-casambi-cbu-blind-2p)"

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

accessories_required: []
accessories_recommended:
  - "Casambi App (iOS/Android — miễn phí)"
  - "Nút bấm thường mở (N.O.) để điều khiển tay"

compare_with_skus: []
bundle_with: []
upsell_to: []

# ================================================================
# BLOCK 7 — COMMERCIAL
# ================================================================
pricing_visibility: "sales_only"
stock_visibility: "sales_only"
warranty_months: 24
origin_country: "EU"
hs_code_vn: ""
moq_hint: "Liên hệ sales để biết MOQ và bậc giá theo số lượng"

# ================================================================
# BLOCK 8 — ASSETS
# ================================================================
images:
  main: "https://knxstore.vn/assets/image/product/bo-dieu-khien-dong-co-rem-casambi-2-kenh-2a-casambi-cbu-blind-2p2.jpg"
  wiring: ""
  dimensions: ""
  installation: ""
datasheet_url: "https://knxstore.vn/assets/image/catalog/Olfer_CBU_BLIND_2P_Datasheet_KNXStore.pdf"
manual_url_en: "https://www.olfer.com/olfer-cbu-blind-2p.html"
manual_url_vi: null
certification_docs: ["CE (LVD 2014/35/EU, EMC 2014/30/EU)", "RED 2014/53/EU", "RoHS 2011/65/EU", "REACH 1907/2006"]

# ================================================================
# BLOCK 9 — RAG OPTIMIZATION
# ================================================================
chunk_strategy: "by_section"
priority_sections:
  - "Tổng quan sản phẩm"
  - "Thông số kỹ thuật"
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
last_verified_by: "auto_converter"
content_version: "2.0"
source_of_truth: "BLIND - Casambi CBU-BLIND-2P.md"
confidence_level: "high"
---

<!-- ============================================================
  PHẦN NỘI DUNG — CHATBOT ĐỌC VÀ TRẢ LỜI
  Mỗi ## heading = 1 chunk độc lập
============================================================ -->

# Casambi CBU-BLIND-2P – Bộ Điều Khiển Động Cơ Rèm

## Tổng quan sản phẩm

CBU-BLIND-2P là bộ điều khiển động cơ rèm/cửa cuốn thuộc hệ sinh thái Casambi, cho phép điều khiển không dây qua Bluetooth Low Energy (BLE) mà không cần hub hay gateway riêng. Thiết bị có 2 đầu ra relay độc lập 2A, phù hợp cho động cơ AC 110–240Vac (cos φ > 0.9), đồng thời hỗ trợ 2 nút bấm vật lý để điều khiển tay. Module CBM tích hợp sẵn cho phép mở rộng sang mạng Casambi long range khi cần tăng phạm vi. CBU-BLIND-2P phù hợp cho các dự án nhà ở cao cấp, văn phòng, khách sạn và bất kỳ công trình nào cần điều khiển rèm/mành thông minh trong hệ Casambi.

👉 [Xem sản phẩm trên KNXStore](https://knxstore.vn/products/bo-dieu-khien-dong-co-rem-casambi-2-kenh-2a-casambi-cbu-blind-2p)

---

## Thông số kỹ thuật

### Điện – Đầu vào

| Thông số | Giá trị |
|:---|:---|
| Điện áp danh định | 110–240 Vac |
| Phạm vi điện áp | 99–264 Vac |
| Tần số | 47–63 Hz |
| Dòng điện vào | ≤ 15 mA |
| Công suất tiêu thụ | ≤ 0.5 W |
| Công suất chờ (standby) | < 0.25 W |

### Điều khiển – Đầu ra

| Thông số | Giá trị |
|:---|:---|
| Tải tối đa mỗi đầu ra | 2 A |
| Dòng xung kích tối đa | 40 A / 4 ms mỗi đầu ra |
| Loại đầu ra | 2 relay thường mở (N.O.) độc lập |
| Input nút bấm | 2 × nút bấm thường mở (N.O.) |

### RF – Bluetooth Low Energy

| Thông số | Giá trị |
|:---|:---|
| Hệ sinh thái | Casambi |
| Giao thức BLE | 4.0 / 5.0 |
| Tần số hoạt động | 2402–2483 MHz |
| Công suất phát tối đa | +7 dBm |
| Cập nhật firmware | OTA (Over the Air) |
| Phạm vi tối đa | 150 m (không vật cản); lớn hơn với mạng long range |

### Điều kiện môi trường & Cơ khí

| Thông số | Giá trị |
|:---|:---|
| Nhiệt độ hoạt động | −20°C đến +50°C |
| Độ ẩm tương đối | 0–80%, không kết tụ |
| Cấp bảo vệ | IP20 |
| Vật liệu vỏ | Nhựa UL94-V0 |
| Kích thước thiết bị | 44 × 57 × 25 mm |
| Trọng lượng | 48 g |

### Nối dây

| Thông số | Giá trị |
|:---|:---|
| Tiết diện dây (solid) | 0.2–3.3 mm² / 30–12 AWG |
| Chiều dài thoát dây | 6.5 mm |
| Loại đầu kết nối | Screw terminals, mô men tối đa 0.5 Nm |

### Chứng nhận

- EN 60669-2-1:2022
- EN 61000-3-2, EN 61000-3-3
- EN 301489-1, EN 301489-17, EN 300328
- CE (LVD 2014/35/EU, EMC 2014/30/EU)
- RED 2014/53/EU
- RoHS 2011/65/EU
- REACH 1907/2006

---

## Chức năng chính

### Điều khiển động cơ rèm qua Casambi

CBU-BLIND-2P nhận lệnh từ mạng Casambi qua BLE và điều khiển 2 đầu ra relay độc lập để vận hành động cơ AC lên/xuống. Hai đầu ra hoàn toàn tách biệt, cho phép điều khiển 2 rèm riêng lẻ hoặc 1 rèm theo kiểu đổi chiều (tùy sơ đồ đấu dây và profile được chọn).

### Điều khiển tay qua nút bấm vật lý

Hai đầu vào nút bấm (N.O.) cho phép điều khiển rèm trực tiếp mà không cần điện thoại hay app, phù hợp cho những người dùng ưu tiên phương án backup vật lý. Khoảng cách tối đa từ nút bấm đến thiết bị là 100 m; nên dùng cáp shielded nếu có nhiễu điện từ trong môi trường lắp đặt.

### Hỗ trợ mạng Casambi Long Range

Module CBM tích hợp sẵn giúp CBU-BLIND-2P tham gia vào mạng Casambi long range, cho phép mở rộng phạm vi phủ sóng vượt quá 150 m tiêu chuẩn — phù hợp cho công trình lớn hoặc có cấu trúc phức tạp.

### Profile Casambi linh hoạt

Thiết bị hỗ trợ nhiều profile Casambi để phù hợp với từng kịch bản điều khiển:

- **Toggle** (default — #45972): bật/tắt đơn giản
- **Independent Toggle**: 2 đầu ra hoạt động độc lập
- **Press / Pulse**: phù hợp điều khiển từng nhịp ngắn
- **Presence**: tích hợp với cảm biến hiện diện
- **Push Buttons**: ánh xạ nút bấm vật lý vào lệnh Casambi
- **Repeater**: dùng làm điểm lặp tín hiệu trong mạng lớn
- Các profile khác theo yêu cầu dự án

---

## Integration & Compatibility

### Hoạt động trong hệ Casambi

Trong hệ Casambi, CBU-BLIND-2P hoạt động như một node BLE — nhận lệnh từ mạng Casambi và phát tín hiệu relay xuống động cơ. Không cần gateway vật lý; điện thoại cài app Casambi (iOS/Android, miễn phí) đóng vai trò điều phối trực tiếp qua BLE.

**Yêu cầu:** App Casambi (iOS/Android); không cần hub riêng cho mạng cơ bản.  
**Giới hạn:** Chỉ điều khiển được động cơ AC có cos φ > 0.9, tải ≤ 2A/kênh. Không hỗ trợ động cơ DC.

### Kết hợp với hệ khác (Gateway / Bridge)

| Hệ khác | Có thể kết nối? | Phương thức | Yêu cầu thêm |
|:---|:---|:---|:---|
| KNX | Có | Qua Casambi–KNX gateway (VD: CBU-ASD hoặc tương đương) | Gateway vật lý riêng |
| Matter | Có hạn chế | Qua Casambi Matter Bridge (nếu firmware hỗ trợ) | Xác nhận phiên bản firmware |
| Modbus | Không trực tiếp | Không hỗ trợ native | — |
| BACnet | Không trực tiếp | Không hỗ trợ native | — |

> 💡 **Lưu ý tích hợp:** Khi tích hợp với KNX qua gateway, lệnh từ KNX đến rèm sẽ đi qua lớp Casambi trước — cần kiểm tra độ trễ trong các kịch bản tự động hóa thời gian thực.

---

## Hướng dẫn chọn sản phẩm

### Chọn CBU-BLIND-2P khi

- Cần điều khiển 1–2 động cơ rèm AC trong hệ Casambi hiện có.
- Dự án yêu cầu điều khiển không dây BLE, không cần chạy dây bus thêm.
- Muốn giữ nút bấm vật lý song song với điều khiển qua app.
- Công trình dùng mạng Casambi long range cần thêm node rèm.

### Không nên chọn CBU-BLIND-2P khi

- Động cơ rèm là loại DC — thiết bị chỉ hỗ trợ AC.
- Tải vượt quá 2A mỗi kênh — cần actuator công suất cao hơn.
- Lắp đặt bắt buộc trong hộp kim loại kín hoàn toàn — tín hiệu BLE sẽ bị chặn (xem lưu ý lắp đặt bên dưới).
- Dự án không dùng hệ Casambi và không có kế hoạch tích hợp.

---

## Ví dụ ứng dụng thực tế

### Scenario 1: Căn hộ cao cấp — điều khiển rèm 2 phòng qua app

**Bài toán:** Chủ nhà muốn điều khiển rèm phòng khách và phòng ngủ từ điện thoại, đồng thời vẫn giữ nút bấm tường để dùng khi không có điện thoại trong tay.

**Giải pháp:** 1 × CBU-BLIND-2P cấp nguồn AC, kết nối 2 động cơ rèm vào 2 đầu ra relay độc lập, đấu 2 nút bấm N.O. vào 2 đầu vào. Toàn bộ điều khiển qua app Casambi — không cần hub riêng.

**Thiết bị cần có:**
- CBU-BLIND-2P × 1
- Nút bấm thường mở (N.O.) × 2
- App Casambi (miễn phí, iOS/Android)

### Scenario 2: Văn phòng — điều khiển rèm theo cảm biến ánh sáng

**Bài toán:** Văn phòng muốn rèm tự động đóng/mở theo mức ánh sáng tự nhiên, không cần can thiệp thủ công.

**Giải pháp:** CBU-BLIND-2P kết hợp với cảm biến ánh sáng Casambi; thiết lập automation trực tiếp trên app Casambi — khi cường độ sáng vượt ngưỡng, lệnh đóng rèm được gửi tự động qua mạng BLE.

**Thiết bị cần có:**
- CBU-BLIND-2P × (số lượng theo số vùng rèm)
- Cảm biến ánh sáng tương thích Casambi
- App Casambi với cấu hình automation

---

## Lắp đặt & Commissioning

### Yêu cầu lắp đặt

- Nguồn cấp bắt buộc 110–240 Vac qua đầu vào thiết bị — đây không phải thiết bị không dây hoàn toàn, chỉ phần điều khiển mới dùng BLE.
- Không đặt trong hộp kim loại kín — nếu bắt buộc, cần cắt khe xung quanh vị trí ăng-ten (đánh dấu màu vàng ở bên phải thiết bị) để tín hiệu RF thoát ra ngoài.
- Khoảng cách tối đa từ nút bấm đến thiết bị là 100 m; dùng cáp shielded khi có nhiễu điện từ.
- Tránh lắp gần các cấu trúc kim loại lớn làm suy giảm tín hiệu BLE.

### Các bước cơ bản

1. Đấu dây nguồn AC vào đầu vào, đấu dây động cơ vào 2 đầu ra relay theo sơ đồ nối dây chính thức.
2. Đấu nút bấm N.O. (nếu có) vào 2 đầu vào nút bấm.
3. Cấp điện và thêm thiết bị vào mạng Casambi qua app (iOS/Android).
4. Chọn profile phù hợp (mặc định: Toggle #45972); cấu hình automation nếu cần.
5. Cập nhật firmware OTA nếu có phiên bản mới từ Casambi.

> 📄 Sơ đồ nối dây và hướng dẫn chi tiết: [Hướng dẫn chính thức Olfer](https://www.olfer.com/olfer-cbu-blind-2p.html)

---

## FAQ

**CBU-BLIND-2P điều khiển được loại động cơ nào?**  
Thiết bị hỗ trợ động cơ AC 110–240 Vac với tải tối đa 2A mỗi đầu ra và hệ số công suất cos φ > 0.9. Không hỗ trợ động cơ DC.

**Có thể điều khiển 2 rèm độc lập bằng 1 thiết bị không?**  
Có, với profile "Independent Toggle", 2 đầu ra relay hoạt động hoàn toàn tách biệt, cho phép điều khiển 2 rèm riêng lẻ với lệnh khác nhau từ app hoặc nút bấm.

**Có cần gateway hay hub riêng để dùng Casambi không?**  
Không cần cho điều khiển cơ bản — điện thoại cài app Casambi (miễn phí) là đủ. Gateway chỉ cần khi muốn tích hợp với hệ thống khác (KNX, BACnet…) hoặc khi cần kiểm soát từ xa qua cloud.

**Phạm vi Bluetooth của thiết bị là bao nhiêu?**  
Tối đa 150 m trong không gian mở không có vật cản. Với mạng Casambi long range (module CBM tích hợp sẵn), phạm vi có thể lớn hơn đáng kể tùy cấu hình mạng.

**Có lắp trong tủ điện kim loại được không?**  
Không nên đặt trong hộp kim loại kín vì BLE sẽ bị chặn. Nếu bắt buộc, cần cắt khe thông thoáng xung quanh vị trí ăng-ten (cạnh phải, đánh dấu vàng) để tín hiệu RF thoát ra.

**Firmware có thể cập nhật không?**  
Có, CBU-BLIND-2P hỗ trợ cập nhật firmware OTA (Over the Air) trực tiếp qua app Casambi — không cần tháo thiết bị.

**Giá và tình trạng hàng hiện tại?**  
Giá và tồn kho cập nhật liên tục. Vui lòng liên hệ KNXStore để được báo giá chính xác và kiểm tra tình trạng hàng.

