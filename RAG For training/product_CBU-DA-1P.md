---
# ================================================================
# BLOCK 1 — IDENTIFICATION
# ================================================================
sku: "CBU-DA-1P"                 # Lấy từ cột sku_extracted trong casambi_full_sku.csv
product_name: "Olfer CBU-DA-1P – Bộ điều khiển DALI Casambi"
brand: "Olfer"
manufacturer_part_number: "CBU-DA-1P"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p"
status: "active"

# ================================================================
# BLOCK 2 — CLASSIFICATION
# ================================================================
product_type: "controller"

category_primary: "Dimmer DALI"
category_secondary: ["Bộ điều khiển trung tâm", "Điều khiển Casambi", "Điều khiển chiếu sáng"]

ecosystem: ["Casambi"]
control_bus: ["DALI", "DALI-2"]
connectivity: ["BLE 4.0/5.0"]

# ================================================================
# BLOCK 3 — SEARCH & DISCOVERY
# ================================================================
aliases: ["CBU-DA-1P", "CBUDA1P", "CBU DA 1P", "Olfer DALI Casambi", "Olfer CBU-DA-1P"]

search_keywords_vi:
  - "bộ điều khiển DALI Casambi"
  - "điều khiển đèn DALI bằng bluetooth"
  - "DALI master Casambi"
  - "điều khiển 50 driver DALI"
  - "Casambi DALI gateway"
  - "dimmer DALI không dây"
  - "CBU-DA-1P Olfer"
  - "điều khiển tunable white DALI"
  - "DALI DT6 DT8 controller"
  - "bộ điều khiển DALI tích hợp nguồn"

search_keywords_en:
  - "Casambi DALI controller"
  - "wireless DALI master"
  - "CBU-DA-1P Olfer"
  - "DALI DT6 DT8 Casambi"
  - "BLE DALI gateway"
  - "Casambi DALI-2 controller"
  - "tunable white DALI Casambi"
  - "DALI 50 drivers controller"

# ================================================================
# BLOCK 4 — TARGET & USE CASE
# ================================================================
target_segment: ["system_integrator", "lighting_designer", "me_contractor"]

project_type: ["office", "hotel", "retail", "residential_premium", "industrial"]

project_scale: ["small", "medium", "large"]

complexity_level: "advanced"

use_case_tags:
  - "dimming"
  - "tunable_white"
  - "rgb_lighting"
  - "rgbw_lighting"
  - "dali_control"
  - "occupancy_control"
  - "daylight_harvesting"
  - "group_control"
  - "broadcast_control"
  - "sensor_integration"

not_suitable_for:
  - "Driver không hỗ trợ DALI (chỉ có 0-10V hoặc Triac)"
  - "Dùng độc lập không có DALI bus"
  - "Hệ thống cần điều khiển trên 50 driver trong một network"
  - "Ứng dụng không có smartphone hoặc tablet để vận hành Casambi App"

# ================================================================
# BLOCK 5 — CHATBOT BEHAVIOR
# ================================================================
chatbot_priority: "high"

price_display: "fetch"
# fetch       → chatbot tự lấy giá từ website_url khi khách hỏi
# hidden      → không hiển thị giá, luôn redirect sang sales
# contact_only → hiển thị "Liên hệ báo giá", không fetch

display_mode_technical: "text"
display_mode_purchase: "markdown_card"

product_link_text: "👉 [Olfer CBU-DA-1P – Bộ điều khiển DALI Casambi](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p)"

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
equivalent_skus: ["CBU-DCS"]

accessories_required:
  - "Driver LED tương thích DALI DT6 hoặc DT8"
  - "Casambi App (iOS/Android)"

accessories_recommended:
  - "Cảm biến chuyển động DALI-2 (CBU-PIR-CR-DA)"
  - "Cảm biến ánh sáng DALI-2"
  - "DALI-2 push button input devices"
  - "Hộp đấu nối chống nước CBU BOX IP66 (nếu lắp ngoài trời)"

compare_with_skus: ["CBU-DCS", "SAL-1016", "SAL-1032"]
# Chatbot retrieve file từng SKU này và tự tạo bảng so sánh — không cần bảng cứng trong file

bundle_with: []
upsell_to: ["SAL-1016", "SAL-1032"]

# ================================================================
# BLOCK 7 — COMMERCIAL
# ================================================================
pricing_visibility: "sales_only"
stock_visibility: "sales_only"
warranty_months: 24
origin_country: "Spain"
hs_code_vn: ""
moq_hint: "Liên hệ sales để biết MOQ và bậc giá theo số lượng"

# ================================================================
# BLOCK 8 — ASSETS
# ================================================================
images:
  main: "https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-dali-cbu-da-1p_10.jpg"
  slide_2: "https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-dali-cbu-da-1p_11.jpg"
  slide_3: "https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-dali-cbu-da-1p_12.jpg"
  wiring: "https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-dali-cbu-da-1p_13.jpg"
  dimensions: ""
  installation: ""
datasheet_url: "https://knxstore.vn/assets/image/catalog/DALI_Casambi_Olfer_CBU-DA-1P_KNXStore_vn.pdf"
manual_url_en: "https://knxstore.vn/assets/image/catalog/DALI_Casambi_Olfer_CBU-DA-1P_KNXStore_vn.pdf"
manual_url_vi: null
profiles_url: "https://knxstore.vn/assets/image/catalog/CBU-DA-1P_Casambi_fixture_profiles_EN-V1_2_KNXStore_vn.pdf"
certification_docs: ["CE", "DALI-2 certified", "Casambi certified"]

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
content_version: "1.1"
source_of_truth: "knxstore.vn product page + knxstore.vn/assets/image/catalog/"
confidence_level: "high"
---

# Olfer CBU-DA-1P – Bộ điều khiển DALI Casambi

## Tổng quan sản phẩm

CBU-DA-1P là bộ điều khiển DALI master của Olfer (Tây Ban Nha), tích hợp giao thức Casambi qua Bluetooth Low Energy. Thiết bị đóng vai trò cầu nối giữa mạng Casambi không dây và bus DALI có dây, cho phép điều khiển tối đa 50 driver LED DALI từ smartphone hoặc tablet mà không cần thêm gateway hay hub trung gian.

CBU-DA-1P phù hợp với các dự án chiếu sáng thương mại và dân dụng cao cấp — văn phòng, khách sạn, showroom, căn hộ — nơi cần điều khiển linh hoạt theo nhóm, lịch trình, hoặc kết hợp cảm biến DALI-2.

👉 [Xem sản phẩm trên KNXStore](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p)

---

## Thông số kỹ thuật

| Thông số | Giá trị |
|:---|:---|
| Điện áp đầu vào | 110–277 Vac |
| Tần số đầu vào | 47–63 Hz |
| Dòng điện đầu vào | 40 mA |
| Công suất tiêu thụ | ≤ 2,5 W |
| Công suất chờ | < 0,3 W |
| Nhiệt độ hoạt động | -20°C đến +50°C |
| Kích thước (D×R×C) | 44 × 57 × 25 mm |
| Trọng lượng | 58 g |
| Xuất xứ | Tây Ban Nha |
| Bảo hành | 24 tháng |

**Thông số DALI bus**

| Thông số | Giá trị |
|:---|:---|
| DALI Bus Voltage | 12–14 VDC |
| Dòng điện đảm bảo DALI | 100 mA |
| Số driver tối đa | 50 thiết bị |
| Chuẩn hỗ trợ | DALI DT6, DALI DT8, DALI-2 |

**Thông số Casambi / BLE**

| Thông số | Giá trị |
|:---|:---|
| Công nghệ kết nối | Bluetooth Low Energy 4.0/5.0 |
| Giao thức | Casambi (Classic & Evolution) |
| Dải tần số | 2402–2483 MHz |
| Công suất phát tối đa | +7 dBm |

---

## Chức năng chính

### Điều khiển DALI không dây qua Casambi

CBU-DA-1P nhận lệnh từ mạng Casambi qua BLE và phát lệnh DALI xuống bus đèn. Người dùng điều khiển hoàn toàn qua Casambi App trên smartphone hoặc tablet — không cần bảng điều khiển có dây, không cần hub trung gian. Toàn bộ logic (scene, lịch trình, cảm biến) được lưu trong network Casambi, không phụ thuộc internet.

### Hỗ trợ hơn 100 Fixture Profile

Thiết bị hỗ trợ đầy đủ các chế độ điều khiển DALI: Broadcast, Short Address, Group Address, DT6 (dimming cơ bản), DT8 (màu sắc nâng cao), Tunable White, RGB, RGBW, XY. Profile mặc định là DALI Lin\* Broadcast (ID 33477) — phù hợp với hầu hết ứng dụng dimming đơn giản. Xem chi tiết tại file `profiles_CBU-DA-1P.md`.

### Tích hợp cảm biến DALI-2

Khi chọn đúng Fixture Profile (Ext. Presence / Ext. Light / Ext. Sensors), cảm biến DALI-2 kết nối trên bus sẽ xuất hiện như Casambi sensor trong App. Điều này cho phép thiết lập automation daylight harvesting và occupancy control hoàn toàn trong Casambi mà không cần controller bổ sung.

### Tích hợp nguồn DALI bus

CBU-DA-1P tích hợp sẵn nguồn cấp cho DALI bus (100 mA), đủ cho hầu hết hệ thống 50 driver. Không cần bộ nguồn DALI riêng trong phần lớn ứng dụng — giảm chi phí và đơn giản hóa tủ điện.

### Bảo vệ và giám sát nhiệt độ

Thiết bị tích hợp bảo vệ quá áp, quá nhiệt, và cho phép giám sát nhiệt độ bên trong theo thời gian thực qua Casambi App — tính năng quan trọng cho dự án lắp đặt trong tủ điện hoặc môi trường khắc nghiệt.

---

## Integration & Compatibility

### Hoạt động trong hệ Casambi

Trong hệ Casambi, CBU-DA-1P là một node BLE hoạt động như DALI master. Thiết bị tham gia vào Casambi network (Classic hoặc Evolution), nhận lệnh broadcast từ App hoặc từ các node Casambi khác, và phát lệnh DALI tương ứng xuống bus.

Mỗi Casambi network hỗ trợ tối đa 127 node — CBU-DA-1P chiếm 1 node. Các driver DALI trên bus không chiếm node Casambi; chúng được quản lý thông qua Fixture Profile của CBU-DA-1P.

**Yêu cầu:** Casambi App (iOS/Android), ít nhất 1 tài khoản Casambi để tạo network.
**Giới hạn:** Tối đa 50 driver DALI trên 1 CBU-DA-1P. Nếu cần hơn 50 driver, dùng nhiều CBU-DA-1P hoặc nâng lên SAL-1016/SAL-1032.

### Điều khiển qua DALI bus

CBU-DA-1P là DALI master — nó phát lệnh, không nhận lệnh từ DALI master khác. Trên cùng một bus DALI chỉ được có 1 master. Thiết bị hỗ trợ toàn bộ chuẩn DALI-2 bao gồm DT6, DT8, và các input device DALI-2 (cảm biến, push button).

**Tương thích:** Mọi driver LED có chuẩn DALI DT6 hoặc DT8, cảm biến DALI-2, push button DALI-2.
**Không tương thích:** Driver chỉ hỗ trợ 0-10V, Triac, PWM, hoặc DMX — không có DALI interface.

### Kết hợp với hệ khác

| Hệ khác | Có thể kết nối? | Phương thức | Yêu cầu thêm |
|:---|:---|:---|:---|
| KNX | ✅ Có | Gateway KNX–Casambi | VBU-K2C-W-BI hoặc tương đương |
| Matter | ✅ Có | Casambi–Matter Bridge | Rayrun MTB10 hoặc tương đương |
| Modbus | ⚠️ Gián tiếp | Qua Casambi Cloud API + middleware | Cần lập trình tích hợp |
| BACnet | ⚠️ Gián tiếp | Qua gateway BACnet–Casambi | Lithernet Gateway |
| DMX | ✅ Có | Bộ chuyển đổi DMX–Casambi | SceneDMXcas hoặc casDMX |
| 0-10V | ❌ Không trực tiếp | — | Cần dùng CBU-A2D thay thế |

> 💡 **Lưu ý tích hợp đa hệ:** Khi KNX và Casambi cùng điều khiển một vùng đèn qua gateway, Casambi luôn ưu tiên lệnh local (BLE) hơn lệnh từ KNX. Độ trễ từ KNX → Casambi → DALI thường trong khoảng 300–500ms.

---

## Hướng dẫn chọn sản phẩm

### Chọn CBU-DA-1P khi

- Dự án có hệ Casambi và cần điều khiển driver DALI (không quá 50 driver trên 1 bus).
- Cần tích hợp cảm biến DALI-2 (chuyển động, ánh sáng) vào Casambi network.
- Muốn điều khiển Tunable White, RGB hoặc RGBW qua DALI DT8 mà không cần bộ điều khiển màu riêng.
- Cần lắp đặt nhanh, không muốn kéo thêm bus điều khiển — chỉ cần đấu nguồn AC và DALI bus.

### Không nên chọn CBU-DA-1P khi

- Driver không có cổng DALI (chỉ có 0-10V, Triac, PWM) → dùng CBU-A2D (0-10V) hoặc CBU-TED (Triac).
- Cần điều khiển hơn 50 driver trên 1 network → nâng lên SAL-1016 hoặc SAL-1032.
- Dự án không dùng Casambi → xem xét DALI master thuần (không BLE).

---

## Ví dụ ứng dụng thực tế

### Scenario 1: Văn phòng 300m² – Casambi + DALI + cảm biến tiết kiệm điện

**Bài toán:** Văn phòng cần điều chỉnh độ sáng theo vùng, tự tắt khi không có người, và điều chỉnh nhiệt độ màu theo giờ làm việc (Human Centric Lighting).

**Giải pháp:** CBU-DA-1P kết nối với driver DALI DT8 của các đèn panel, cảm biến chuyển động DALI-2 và cảm biến ánh sáng tự nhiên. Toàn bộ lịch trình và automation được cài đặt trong Casambi App. Nhân viên điều chỉnh độ sáng qua App hoặc công tắc Casambi gắn tường.

**Thiết bị cần có:**
- CBU-DA-1P × 2–3 (tùy số lượng driver và zone)
- Driver LED DALI DT8 (cho từng đèn panel)
- Cảm biến chuyển động DALI-2 CBU-PIR-CR-DA × 1 mỗi zone
- Công tắc Casambi (tùy chọn) × theo số vị trí

### Scenario 2: Showroom – Điều khiển màu sắc RGBW qua DALI DT8

**Bài toán:** Showroom nội thất cần thay đổi không khí ánh sáng theo từng khu vực trưng bày, hỗ trợ điều khiển RGBW và lưu scene sẵn để nhân viên kích hoạt nhanh.

**Giải pháp:** CBU-DA-1P với Fixture Profile DT8 RGBW BC điều khiển driver RGBW DALI. Scene được lưu trong Casambi App, nhân viên kích hoạt bằng 1 chạm. Có thể thêm remote Casambi không dây để không cần smartphone.

**Thiết bị cần có:**
- CBU-DA-1P × 1–2
- Driver RGBW DALI DT8 (tương thích từng loại đèn)
- Remote Casambi Xpress (tùy chọn)

---

## Lắp đặt & Commissioning

### Yêu cầu lắp đặt

- Nguồn AC 110–277V tại vị trí lắp CBU-DA-1P.
- Bus DALI 2 dây kết nối đến tất cả driver LED (không phân cực).
- Không cần nguồn DALI riêng — CBU-DA-1P cấp nguồn bus tích hợp (100 mA).
- Smartphone/tablet có Casambi App để commissioning.

### Các bước cơ bản

1. Đấu nguồn AC vào terminal L/N của CBU-DA-1P.
2. Kết nối bus DALI (2 dây DA+/DA-) đến tất cả driver LED trên cùng bus.
3. Mở Casambi App, tạo network mới hoặc thêm vào network hiện có.
4. CBU-DA-1P sẽ xuất hiện trong App — chọn Fixture Profile phù hợp.
5. Đánh địa chỉ DALI (tự động hoặc thủ công tùy profile).
6. Tạo scene, lịch trình, và cấu hình cảm biến trong App.

> 📄 Hướng dẫn đầy đủ: [Datasheet CBU-DA-1P](https://knxstore.vn/assets/image/catalog/DALI_Casambi_Olfer_CBU-DA-1P_KNXStore_vn.pdf)

---

## FAQ

**CBU-DA-1P điều khiển được tối đa bao nhiêu đèn?**
Tối đa 50 driver DALI trên một bus. Nếu dự án cần nhiều hơn, có thể dùng nhiều CBU-DA-1P (mỗi cái quản lý 1 bus riêng) hoặc chuyển sang SAL-1016/SAL-1032 cho các dự án quy mô lớn hơn.

**CBU-DA-1P có cần internet để hoạt động không?**
Không. Casambi hoạt động hoàn toàn qua Bluetooth Mesh — điều khiển local không cần internet, không cần cloud. Internet chỉ cần nếu muốn điều khiển từ xa qua Casambi Cloud Gateway.

**CBU-DA-1P có hỗ trợ đèn Tunable White không?**
Có, theo hai cách: DT8 TW (driver hỗ trợ DALI DT8 — điều khiển nhiệt độ màu trực tiếp qua DALI) hoặc DT6 TW (dùng 2 kênh DT6 riêng cho Warm/Cool). Dải nhiệt độ màu hỗ trợ từ 2200K đến 7000K tùy driver.

**Sự khác biệt giữa CBU-DA-1P và CBU-DCS là gì?**
CBU-DA-1P hỗ trợ tối đa 50 driver, CBU-DCS hỗ trợ tối đa 64 driver. Cả hai đều dùng Casambi và hỗ trợ DALI DT6/DT8. Với dự án nhỏ đến vừa (< 50 driver), CBU-DA-1P là lựa chọn tiêu chuẩn.

**Cảm biến DALI-2 có hoạt động với CBU-DA-1P không?**
Có. Khi chọn Fixture Profile có "Ext. Presence", "Ext. Light" hoặc "Ext. Sensors", cảm biến DALI-2 trên bus sẽ xuất hiện như Casambi sensor trong App. Bạn có thể thiết lập automation hoàn toàn trong Casambi.

**CBU-DA-1P có thể tích hợp với KNX không?**
Có, thông qua gateway KNX–Casambi (VD: VBU-K2C-W-BI). KNX gửi lệnh đến gateway, gateway dịch sang Casambi, Casambi điều khiển CBU-DA-1P và bus DALI. Tích hợp hai chiều cũng khả thi nhưng cần cấu hình thêm.

**Giá CBU-DA-1P là bao nhiêu?**
Vui lòng liên hệ KNXStore để được báo giá chính xác và kiểm tra tồn kho.
👉 Zalo: [0918.918.755](https://zalo.me/0918918755)

---

## Hiển thị sản phẩm

### Khi trả lời câu hỏi kỹ thuật

> 📄 [Datasheet CBU-DA-1P](https://knxstore.vn/assets/image/catalog/DALI_Casambi_Olfer_CBU-DA-1P_KNXStore_vn.pdf) | 📄 [Fixture Profiles](https://knxstore.vn/assets/image/catalog/CBU-DA-1P_Casambi_fixture_profiles_EN-V1_2_KNXStore_vn.pdf) | 🛒 [Xem sản phẩm trên KNXStore](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p)

### Khi tư vấn mua hàng — render Markdown card

Khi có giá:
```
![Olfer CBU-DA-1P](https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-dali-cbu-da-1p_10.jpg)
**[Olfer CBU-DA-1P – Bộ điều khiển DALI Casambi](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p)**
DALI master tích hợp Casambi BLE, điều khiển tối đa 50 driver, hỗ trợ DT6/DT8/TW/RGB/RGBW.
💰 [GIÁ FETCH TỪ TRANG] (Giá đã bao gồm VAT)
👉 [Xem sản phẩm](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p) | 📞 [Nhận báo giá](https://zalo.me/0918918755)
```

Khi không có giá / Make to order:
```
![Olfer CBU-DA-1P](https://knxstore.vn/assets/image/product/casambi-bo-dieu-khien-dali-cbu-da-1p_10.jpg)
**[Olfer CBU-DA-1P – Bộ điều khiển DALI Casambi](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p)**
DALI master tích hợp Casambi BLE, điều khiển tối đa 50 driver, hỗ trợ DT6/DT8/TW/RGB/RGBW.
💰 Liên hệ báo giá
👉 [Xem sản phẩm](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p) | 📞 [Nhận báo giá](https://zalo.me/0918918755)
```

### Khi khách hỏi báo giá dự án

Thu thập: loại công trình, quy mô, hệ thống dự kiến, thời gian triển khai. Sau đó:

> "Cảm ơn bạn đã cung cấp thông tin. Giá dự án phụ thuộc vào số lượng và loại khách hàng nên đội ngũ KNXStore sẽ tư vấn trực tiếp để đảm bảo bạn nhận được mức giá tốt nhất.
>
> 👉 Liên hệ sales qua Zalo: **[0918.918.755](https://zalo.me/0918918755)**
> hoặc để lại số điện thoại / email, KNXStore sẽ chủ động liên hệ lại."

---

## Tài liệu kỹ thuật

📄 [Datasheet – Olfer CBU-DA-1P](https://knxstore.vn/assets/image/catalog/DALI_Casambi_Olfer_CBU-DA-1P_KNXStore_vn.pdf)
📄 [Fixture Profile Reference – CBU-DA-1P](https://knxstore.vn/assets/image/catalog/CBU-DA-1P_Casambi_fixture_profiles_EN-V1_2_KNXStore_vn.pdf)
🛒 [Trang sản phẩm KNXStore](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p)

---

## Bảo hành & Hỗ trợ

- Bảo hành: 24 tháng từ ngày xuất hóa đơn
- Hỗ trợ kỹ thuật: knxstore.vn hoặc Zalo [0918.918.755](https://zalo.me/0918918755)