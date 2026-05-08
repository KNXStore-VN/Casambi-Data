# [BRAND] [MODEL] – [Tên sản phẩm ngắn gọn]
<!-- 
  KNXSTORE PRODUCT KNOWLEDGE FILE
  Template version: 2.0
  Dùng cho: chatbot RAG, product page, sales support
  Cập nhật: điền last_updated mỗi lần chỉnh sửa
-->

---
# ================================================================
# BLOCK 1 — IDENTIFICATION (bắt buộc)
# ================================================================
sku: ""                          # Lấy từ cột sku_extracted trong casambi_full_sku.csv
product_name: ""                 # Tên đầy đủ VD: "Olfer CBU-DA-1P DALI Controller"
brand: ""                        # VD: "Olfer" | "Schneider" | "MDT" | "Casambi"
manufacturer_part_number: ""
hubspot_product_id: ""
website_url: ""                  # https://knxstore.vn/products/...
status: "active"                 # active | discontinued | coming_soon

# ================================================================
# BLOCK 2 — CLASSIFICATION (bắt buộc)
# ================================================================
product_type: ""
# Chọn 1: controller | gateway | sensor | driver | power_supply
#          panel | actuator | input_device | accessory | software

category_primary: ""
# VD: "DALI Controllers" | "KNX Sensors" | "Casambi Gateways"

category_secondary: []
# VD: ["Lighting Control", "Casambi", "Building Automation"]

# --- PROTOCOL LAYER (quan trọng) ---
# Phân biệt rõ:
# - ecosystem: hệ sinh thái chính của sản phẩm (KNX, Casambi, Matter...)
# - control_bus: chuẩn điều khiển đèn/thiết bị (DALI, 0-10V, RS485, PWM...)
# - connectivity: kết nối vật lý hoặc wireless (BLE, Ethernet, RS232...)

ecosystem: []
# VD: ["Casambi"] | ["KNX"] | ["Matter"] | ["Casambi", "KNX"]

control_bus: []
# VD: ["DALI"] | ["0-10V"] | ["DALI", "0-10V"] | ["RS485"]
# Để trống nếu không có (VD: sensor thuần KNX không điều khiển đèn)

connectivity: []
# VD: ["BLE"] | ["Ethernet", "RS485"] | ["KNX TP", "BACnet IP"]

# ================================================================
# BLOCK 3 — SEARCH & DISCOVERY (bắt buộc)
# ================================================================
aliases: []
# VD: ["CBU-DA-1P", "CBUDA1P", "CBU DA 1P"]

search_keywords_vi: []
# Từ khóa như khách hàng Việt hay gõ, ưu tiên câu hỏi thực tế
# VD: "điều khiển đèn dali bằng casambi", "bộ điều khiển dali không dây"

search_keywords_en: []
# VD: "DALI Casambi controller", "wireless DALI gateway"

# ================================================================
# BLOCK 4 — TARGET & USE CASE (bắt buộc)
# ================================================================
target_segment: []
# Chọn từ: end_user | system_integrator | lighting_designer
#           me_contractor | electrical_installer | architect

project_type: []
# VD: ["residential_premium", "office", "hotel", "retail", "industrial"]

project_scale: []
# small (< 20 thiết bị) | medium (20–100) | large (100+)

complexity_level: ""
# basic | intermediate | advanced | expert_only

use_case_tags: []
# VD: ["dimming", "tunable_white", "rgb_lighting", "daylight_harvesting",
#      "occupancy_control", "energy_monitoring", "hvac_integration"]

not_suitable_for: []
# Rõ ràng về giới hạn — giúp chatbot không tư vấn sai
# VD: "standalone use without DALI bus", "non-DALI LED drivers"

# ================================================================
# BLOCK 5 — CHATBOT BEHAVIOR (bắt buộc)
# ================================================================
chatbot_priority: "high"         # high | medium | low

# --- GIÁ SẢN PHẨM ---
# Giá KHÔNG lưu trong file — chatbot fetch live từ website_url mỗi lần khách hỏi.
# Lý do: giá thay đổi thường xuyên, hardcode sẽ bị stale.
price_display: "fetch"
# fetch        → chatbot gọi web_fetch lên website_url, lấy giá hiển thị live
# contact_only → không fetch, hiển thị "Liên hệ báo giá" (dùng khi sản phẩm POA)

# --- FORMAT HIỂN THỊ ---
# Flowise widget mặc định chỉ render Markdown — không có card UI native.
display_mode_technical: "text"
# Khi hỏi kỹ thuật → trả lời text + link datasheet + link sản phẩm

display_mode_purchase: "markdown_card"
# Khi tư vấn mua → fetch giá live rồi render Markdown card

product_link_text: ""
# VD: "👉 [Olfer CBU-DA-1P – Bộ điều khiển DALI Casambi](https://knxstore.vn/products/...)"

# --- HANDOFF RULES ---
handoff_to_sales_when:
  - "user_asks_stock"
  - "user_asks_quotation"
  - "user_asks_discount"
  - "user_asks_lead_time"
  - "user_asks_payment_terms"
  - "user_asks_delivery"
  - "user_asks_project_quote"       # Báo giá dự án → thu thập info rồi handoff
  - "user_mentions_project_above_50_units"
  - "user_asks_custom_integration"
  - "user_asks_warranty_claim"
# Lưu ý: "user_asks_price" KHÔNG còn trong danh sách này vì chatbot sẽ tự fetch giá
# Thêm trigger đặc thù nếu có

# ================================================================
# BLOCK 6 — RELATIONSHIPS (bắt buộc)
# ================================================================
replaces_sku: []
replaced_by_sku: null
equivalent_skus: []              # SKU tương đương từ brand khác

accessories_required: []
# VD: ["DALI-compatible LED drivers", "Casambi App (iOS/Android)"]

accessories_recommended: []
# VD: ["DALI-2 motion sensors", "DALI-2 push button inputs"]

compare_with_skus: []
# SKU cùng loại để chatbot tự tổng hợp so sánh khi khách hỏi "nên chọn cái nào?"
# Chatbot retrieve file từng SKU này và tự tạo bảng so sánh — không cần bảng cứng trong file
# VD: ["CBU-DCS", "SAL-1016"]

bundle_with: []
upsell_to: []

# ================================================================
# BLOCK 7 — COMMERCIAL (sales-only)
# ================================================================
pricing_visibility: "sales_only"
stock_visibility: "sales_only"
warranty_months: 24
origin_country: ""
hs_code_vn: ""
moq_hint: "Liên hệ sales để biết MOQ và bậc giá theo số lượng"

# ================================================================
# BLOCK 8 — ASSETS
# ================================================================
images:
  main: ""
  wiring: ""
  dimensions: ""
  installation: ""
datasheet_url: ""
manual_url_en: ""
manual_url_vi: null
certification_docs: []
# VD: ["CE", "KNX certified", "DALI-2 certified"]

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
last_updated: ""                 # VD: "2026-05-08"
last_verified_by: ""             # VD: "nguyen.van.a" | "auto_converter"
content_version: "1.0"
source_of_truth: ""              # Tên file gốc hoặc URL datasheet
confidence_level: "high"         # high | medium | low
---

<!-- ============================================================
  PHẦN NỘI DUNG — ĐÂY LÀ PHẦN CHATBOT ĐỌC VÀ TRẢ LỜI
  Mỗi ## heading = 1 chunk độc lập khi dùng Markdown Text Splitter
  Viết mỗi section đủ nghĩa khi đứng một mình
============================================================ -->

# [BRAND] [MODEL] – [Tên sản phẩm]

## Tổng quan sản phẩm

<!-- 
  Viết 3–5 câu: sản phẩm là gì, dùng để làm gì, phù hợp với ai.
  Không liệt kê specs ở đây — để dành cho section Thông số kỹ thuật.
  Đây là chunk đầu tiên chatbot dùng để giới thiệu sản phẩm.
-->

[Tên sản phẩm] là [loại thiết bị] thuộc hệ [ecosystem], cho phép [chức năng chính]. Thiết bị phù hợp với [đối tượng] trong các dự án [loại công trình].

👉 [Xem sản phẩm trên KNXStore](URL)

---

## Thông số kỹ thuật

<!-- 
  Dùng bảng cho specs cứng. Giữ đơn vị nhất quán.
  Không bỏ trống dòng nếu không có thông tin — ghi "Xem datasheet" thay thế.
-->

| Thông số | Giá trị |
|:---|:---|
| Nguồn cấp | |
| Công suất tiêu thụ | |
| Nhiệt độ hoạt động | |
| Kích thước (mm) | |
| Lắp đặt | |
| Chứng nhận | |
| Bảo hành | tháng |

**Thông số giao tiếp**

| Giao thức / Bus | Chi tiết |
|:---|:---|
| Ecosystem | |
| Control bus | |
| Kết nối | |
| Số kênh / địa chỉ | |
| Tốc độ truyền | |

---

## Chức năng chính

<!--
  Mô tả những gì sản phẩm LÀM ĐƯỢC, theo góc nhìn người dùng.
  Dùng câu hoàn chỉnh, không dùng bullet lẻ tẻ thiếu ngữ cảnh.
  Section này chatbot dùng khi khách hỏi "cái này làm được gì?"
-->

### [Chức năng 1]

[Mô tả rõ ràng, 2–3 câu. Nêu giá trị thực tế, không chỉ nêu tính năng.]

### [Chức năng 2]

[Tương tự — mỗi sub-section là 1 chunk độc lập.]

---

## Integration & Compatibility

<!--
  ĐÂY LÀ SECTION QUAN TRỌNG NHẤT cho sản phẩm multi-protocol.
  Mỗi sub-section = 1 hệ / chuẩn tích hợp.
  Viết rõ: kết nối bằng gì, hoạt động theo chiều nào, giới hạn là gì.
-->

### Hoạt động trong hệ [Ecosystem chính]

[Mô tả sản phẩm đóng vai trò gì trong hệ này. VD: "Trong hệ Casambi, CBU-DA-1P hoạt động như một node BLE, nhận lệnh từ Casambi network và phát lệnh DALI xuống bus đèn."]

**Yêu cầu:** [App/gateway/thiết bị cần có để hoạt động]
**Giới hạn:** [Số thiết bị tối đa, tính năng không hỗ trợ...]

### Điều khiển qua [Control bus — VD: DALI]

[Mô tả sản phẩm giao tiếp với bus này như thế nào. Nêu rõ chiều tín hiệu: master hay slave? Số thiết bị tối đa? Chuẩn nào được hỗ trợ (DT6, DT8, DALI-2...)?]

**Tương thích:** [Loại thiết bị/driver trên bus này cần có]
**Không tương thích:** [Liệt kê rõ để tránh tư vấn sai]

### Kết hợp với hệ khác (Gateway / Bridge)

<!--
  Phần này trả lời câu hỏi: "Thiết bị này có kết nối được với KNX/Matter/Modbus không?"
  Nếu CÓ: mô tả rõ cơ chế (gateway vật lý, trigger, scene sharing...)
  Nếu KHÔNG: ghi rõ để chatbot không đoán mò.
-->

| Hệ khác | Có thể kết nối? | Phương thức | Yêu cầu thêm |
|:---|:---|:---|:---|
| KNX | | | |
| Matter | | | |
| Modbus | | | |
| BACnet | | | |
| [Hệ khác] | | | |

> 💡 **Lưu ý tích hợp:** [Ghi điểm quan trọng nhất khi tích hợp đa hệ — VD: "Khi dùng chung với KNX qua gateway, lệnh từ KNX có độ trễ ~200ms so với lệnh Casambi native."]

---

## Hướng dẫn chọn sản phẩm

<!--
  Section này giúp chatbot tư vấn đúng.
  Trả lời câu hỏi: "Khi nào nên chọn sản phẩm này thay vì sản phẩm khác?"
  Quan trọng: nêu cả trường hợp KHÔNG NÊN dùng.
-->

### Chọn [Model này] khi

- [Điều kiện 1 — cụ thể, có thể kiểm chứng được]
- [Điều kiện 2]
- [Điều kiện 3]

### Không nên chọn [Model này] khi

- [Giới hạn 1 — thành thật, tránh over-promise]
- [Giới hạn 2]

---

## Ví dụ ứng dụng thực tế

<!--
  1–2 scenario cụ thể. Đây là phần quan trọng cho cả B2B và B2C.
  Chatbot dùng để gợi ý khi khách mô tả bài toán của họ.
  Format: Bài toán → Giải pháp → Thiết bị cần thêm
-->

### Scenario 1: [Tên ngắn gọn — VD: "Văn phòng 200m² điều khiển DALI bằng smartphone"]

**Bài toán:** [Mô tả ngắn nhu cầu của khách]

**Giải pháp:** [Model này] kết hợp với [thiết bị khác] cho phép [kết quả cụ thể].

**Thiết bị cần có:**
- [Model này] × [số lượng]
- [Thiết bị bổ sung 1]
- [Thiết bị bổ sung 2]

### Scenario 2: [Tên ngắn gọn]

[Tương tự format trên]

---

## Lắp đặt & Commissioning

<!--
  Không cần viết manual đầy đủ — chỉ cần đủ để chatbot trả lời
  các câu hỏi phổ biến về lắp đặt.
  Luôn trỏ về datasheet/manual cho chi tiết.
-->

### Yêu cầu lắp đặt

- [Yêu cầu 1 — VD: "Cần DALI bus có nguồn 16–22VDC riêng"]
- [Yêu cầu 2]
- [Yêu cầu 3]

### Các bước cơ bản

1. [Bước 1 ngắn gọn]
2. [Bước 2]
3. [Bước 3]

> 📄 Hướng dẫn lắp đặt đầy đủ: [Link datasheet/manual]

---

## FAQ

<!--
  Viết theo đúng cách khách hay hỏi — không viết theo góc nhìn sản phẩm.
  Mỗi cặp Q/A là 1 chunk nhỏ — rất quan trọng cho RAG accuracy.
  Tối thiểu 5 câu, tối đa 10 câu.
  Bao gồm: câu hỏi kỹ thuật, câu hỏi so sánh, câu hỏi tích hợp.
-->

**[Câu hỏi kỹ thuật cơ bản nhất mà khách hay hỏi đầu tiên]?**
[Trả lời ngắn gọn, đủ để khách hiểu mà không cần đọc thêm.]

**[Câu hỏi về giới hạn / khả năng]?**
[Trả lời thành thật — bao gồm cả giới hạn nếu có.]

**[Câu hỏi so sánh — VD: "Khác gì với [Model khác]?"]?**
[Trả lời trực tiếp vào điểm khác biệt chính.]

**[Câu hỏi tích hợp — VD: "Có dùng được với KNX không?"]?**
[Trả lời có/không + điều kiện cụ thể.]

**[Câu hỏi về lắp đặt / commissioning]?**
[Trả lời, nếu cần kỹ sư thì nói rõ.]

**[Câu hỏi về giá / đặt hàng]?**
Giá và tình trạng hàng cập nhật theo từng thời điểm. Vui lòng liên hệ KNXStore để được báo giá chính xác và kiểm tra tồn kho.

---

## Hiển thị sản phẩm

<!--
  Section này cho chatbot biết CÁCH và KHI NÀO hiển thị sản phẩm.
  Không xóa — chatbot đọc để biết format và logic giá.
  Flowise widget mặc định chỉ render Markdown, không có card UI native.
-->

### Khi trả lời câu hỏi kỹ thuật

Trả lời xong, kết thúc bằng 1 dòng:
> 📄 [Datasheet](DATASHEET_URL) | 🛒 [Xem sản phẩm trên KNXStore](WEBSITE_URL)

### Khi tư vấn mua hàng — render Markdown card

**Bước 1 — Fetch giá live:** Gọi `web_fetch` lên `website_url` để lấy giá hiện tại.
- Tìm thấy giá → hiển thị kèm "Giá đã bao gồm VAT".
- Không tìm thấy hoặc "Make to order" → hiển thị "Liên hệ báo giá".
- Lý do fetch live: giá thay đổi thường xuyên, không lưu giá trong file knowledge.

**Bước 2 — Render theo format chuẩn:**

```
![TÊN SẢN PHẨM](IMAGE_URL)
**[BRAND MODEL – Tên ngắn](WEBSITE_URL)**
Mô tả 1 dòng — chức năng chính, phù hợp với ai.
💰 [GIÁ FETCH LIVE] (Giá đã bao gồm VAT) | hoặc: 💰 Liên hệ báo giá
👉 [Xem sản phẩm](WEBSITE_URL) | 📞 [Nhận báo giá](https://zalo.me/0918918755)
```

### Khi khách hỏi báo giá dự án

Thu thập trước khi handoff sang sales:
- Loại công trình (văn phòng, khách sạn, căn hộ, trường học...)
- Quy mô (số phòng / số zone / diện tích)
- Hệ thống dự kiến (Casambi, KNX, DALI...)
- Thời gian triển khai dự kiến

Sau đó handoff với message chuẩn:
> "Cảm ơn bạn đã cung cấp thông tin. Giá dự án phụ thuộc vào số lượng và loại khách hàng nên đội ngũ KNXStore sẽ tư vấn trực tiếp để đảm bảo bạn nhận được mức giá tốt nhất.
>
> 👉 Liên hệ sales qua Zalo: **[0918.918.755](https://zalo.me/0918918755)**
> hoặc để lại số điện thoại / email, KNXStore sẽ chủ động liên hệ lại."

Lưu ý cho chatbot: không tự estimate giá dự án, không gợi ý mức chiết khấu cụ thể — mọi thông tin giá dự án do sales quyết định.

---

## Tài liệu kỹ thuật

📄 [Datasheet chính thức](URL)
📄 [User Manual EN](URL)
📄 [User Manual VI](URL nếu có)
🔗 [Trang sản phẩm KNXStore](URL)

---

## Bảo hành & Hỗ trợ

- Bảo hành: [X] tháng từ ngày xuất hóa đơn
- Hỗ trợ kỹ thuật: [email/phone/zalo]
- Chính sách bảo hành: [link nếu có]