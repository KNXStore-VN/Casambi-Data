# [ECOSYSTEM] Integration Guide – Kết nối với các hệ khác
<!-- 
  KNXSTORE INTEGRATION KNOWLEDGE FILE
  Template version: 1.0
  Mục đích: Mô tả toàn bộ cách [ECOSYSTEM] kết nối với các hệ sinh thái khác
  File này là kiến thức nền — chatbot đọc để trả lời câu hỏi tích hợp đa hệ
  Đặt tên file: [ecosystem]-integrations.md
  VD: knx-integrations.md | casambi-integrations.md | matter-integrations.md
-->

---
# ================================================================
# BLOCK 1 — FILE IDENTIFICATION
# ================================================================
file_type: "integration_guide"
ecosystem: ""
# Hệ sinh thái chủ thể của file này
# VD: "KNX" | "Casambi" | "Matter" | "Modbus"

version: "1.0"
last_updated: ""
last_verified_by: ""
confidence_level: "high"        # high | medium | low

# ================================================================
# BLOCK 2 — ECOSYSTEM OVERVIEW (cho RAG context)
# ================================================================
ecosystem_type: ""
# "wired_standard" | "wireless_standard" | "control_bus" | "iot_platform"

primary_use_cases: []
# VD: ["building_automation", "lighting_control", "hvac", "access_control"]

typical_project_scale: []
# VD: ["medium", "large"] — KNX thường dùng cho dự án từ vừa trở lên

key_strengths: []
# VD: ["reliability", "interoperability", "decades_of_support"]

# ================================================================
# BLOCK 3 — INTEGRATION MAP (chatbot dùng để routing câu hỏi)
# ================================================================
can_integrate_with:
  # Danh sách hệ có thể kết nối, dùng để chatbot biết trước khi đọc chi tiết
  # Format: ecosystem_name: method
  # VD:
  # casambi: "gateway"
  # dali: "native_or_gateway"
  # matter: "ip_bridge"
  # modbus: "gateway"
  # bacnet: "ip_gateway"

cannot_integrate_with: []
# Liệt kê rõ những hệ KHÔNG thể kết nối — quan trọng để chatbot không tư vấn sai
# VD: ["Zigbee native", "Z-Wave native"]

requires_gateway_for: []
# Những hệ cần gateway trung gian mới kết nối được
# VD: ["Casambi", "Matter", "Modbus"]

native_integration_with: []
# Những hệ kết nối được trực tiếp không cần gateway
# VD: ["DALI", "0-10V", "KNX IP"]

# ================================================================
# BLOCK 4 — CHATBOT BEHAVIOR
# ================================================================
chatbot_priority: "high"
related_product_files: []
# Danh sách file sản phẩm liên quan — chatbot cross-reference khi cần
# VD: ["knx-ip-router.md", "cbu-da-1p.md", "knx-casambi-gateway.md"]

related_integration_files: []
# File integration khác liên quan
# VD: ["casambi-integrations.md", "dali-integrations.md"]
---

<!-- ============================================================
  PHẦN NỘI DUNG
  Mỗi ## heading = 1 integration pair = 1 chunk độc lập
  Viết mỗi section đủ nghĩa khi đứng một mình — chatbot có thể
  retrieve đúng 1 section mà không cần đọc cả file
============================================================ -->

# [ECOSYSTEM] Integration Guide

## Tổng quan về [ECOSYSTEM]

<!--
  3–5 câu: hệ này là gì, dùng để làm gì, điểm mạnh là gì.
  Không đi sâu kỹ thuật — section này để chatbot trả lời câu hỏi
  "KNX là gì?" hoặc "Casambi hoạt động như thế nào?"
  Luôn kết thúc bằng: hệ này tích hợp được với những gì.
-->

[ECOSYSTEM] là [định nghĩa ngắn gọn]. Hệ này phù hợp nhất cho [loại dự án / quy mô / ứng dụng].

Điểm mạnh chính: [2–3 điểm, cụ thể].

Trong hệ sinh thái KNXStore, [ECOSYSTEM] có thể kết nối với: [liệt kê nhanh các hệ tích hợp được].

---

## Quy tắc tích hợp chung

<!--
  QUAN TRỌNG: Section này chatbot dùng để trả lời câu hỏi tổng quát
  về tích hợp, trước khi đi vào từng cặp cụ thể.
  Viết các nguyên tắc đúng với MỌI integration của hệ này.
-->

### Nguyên tắc cơ bản

- **[Nguyên tắc 1]:** [Giải thích ngắn — VD: "KNX luôn là master trong mọi integration — thiết bị hệ khác phải expose API hoặc dùng gateway để nhận lệnh KNX."]
- **[Nguyên tắc 2]:** [VD: "Mọi integration qua IP đều cần KNX IP Router hoặc KNX IP Interface."]
- **[Nguyên tắc 3]:** [VD: "Tích hợp hai chiều (bidirectional) luôn phức tạp hơn một chiều và cần cấu hình thêm."]

### Các phương thức tích hợp phổ biến

| Phương thức | Mô tả | Ưu điểm | Giới hạn |
|:---|:---|:---|:---|
| Gateway vật lý | Thiết bị chuyển đổi giao thức | Ổn định, không phụ thuộc cloud | Chi phí thêm, cần cấu hình |
| IP Bridge | Kết nối qua mạng LAN | Linh hoạt, không cần thêm dây | Cần network ổn định |
| Scene trigger | Hệ A kích hoạt scene trên hệ B | Đơn giản, ít lỗi | Một chiều, không real-time feedback |
| Direct bus | Chia sẻ cùng bus vật lý | Latency thấp nhất | Giới hạn theo chuẩn bus |
| Cloud API | Tích hợp qua internet | Dễ setup | Phụ thuộc cloud, latency cao |

---

## [ECOSYSTEM] ↔ [HỆ 1] Integration

<!--
  MỖI CẶP TÍCH HỢP = 1 SECTION RIÊNG
  Đặt tên heading chuẩn: [ECOSYSTEM] ↔ [HỆ KIA]
  VD: "KNX ↔ Casambi Integration" | "KNX ↔ DALI Integration"
  
  Viết đủ để chatbot trả lời:
  - "KNX có kết nối được với Casambi không?"
  - "Cần thiết bị gì để KNX điều khiển đèn Casambi?"
  - "Có hạn chế gì khi dùng KNX với Casambi không?"
-->

### Tổng quan

[2–3 câu mô tả mối quan hệ giữa hai hệ. VD: "KNX và Casambi là hai hệ độc lập — KNX chạy trên bus có dây TP, Casambi chạy trên BLE. Để hai hệ giao tiếp cần gateway chuyển đổi giao thức."]

**Khả năng tích hợp:** ✅ Có thể / ⚠️ Có thể, với điều kiện / ❌ Không thể

**Phương thức chính:** [Gateway / IP Bridge / Native / Scene trigger]

**Chiều tích hợp:** 
- [ECOSYSTEM] → [HỆ 1]: ✅ / ❌
- [HỆ 1] → [ECOSYSTEM]: ✅ / ❌
- Hai chiều (bidirectional): ✅ / ❌ / ⚠️ Giới hạn

### Cách thực hiện

**Phương án 1: [Tên phương án — VD: "Qua KNX-Casambi Gateway"]**

[Mô tả rõ cơ chế hoạt động. Viết theo góc nhìn của người lắp đặt: làm gì trước, làm gì sau, cần cấu hình gì.]

Thiết bị cần có:
- [Thiết bị 1 — ghi rõ SKU nếu KNXStore đang bán]
- [Thiết bị 2]

Bước thực hiện cơ bản:
1. [Bước 1]
2. [Bước 2]
3. [Bước 3]

**Phương án 2: [Tên phương án thay thế nếu có]**

[Tương tự format trên. Nếu không có phương án 2, bỏ qua.]

### Giới hạn & Lưu ý

- **[Giới hạn 1]:** [Mô tả cụ thể — VD: "Số lượng group Casambi có thể map sang KNX tối đa là 16 group."]
- **[Giới hạn 2]:** [VD: "Feedback trạng thái từ Casambi về KNX có độ trễ ~500ms — không phù hợp cho ứng dụng cần real-time."]
- **[Lưu ý quan trọng]:** [VD: "Firmware gateway phải được cập nhật đúng phiên bản tương thích với Casambi Evolution."]

### Sản phẩm KNXStore liên quan

| Vai trò | Sản phẩm | SKU | Link |
|:---|:---|:---|:---|
| Gateway chính | [Tên sản phẩm] | [SKU] | [URL] |
| [Vai trò khác] | | | |

> 💬 **Câu hỏi phổ biến:** "[Câu hỏi khách hay hỏi nhất về integration này]?"
> → [Trả lời ngắn gọn, thực tế]

---

## [ECOSYSTEM] ↔ [HỆ 2] Integration

<!-- Lặp lại format trên cho mỗi cặp hệ -->

### Tổng quan

**Khả năng tích hợp:** ✅ / ⚠️ / ❌

**Phương thức chính:**

**Chiều tích hợp:**
- [ECOSYSTEM] → [HỆ 2]: 
- [HỆ 2] → [ECOSYSTEM]: 
- Hai chiều: 

### Cách thực hiện

### Giới hạn & Lưu ý

### Sản phẩm KNXStore liên quan

| Vai trò | Sản phẩm | SKU | Link |
|:---|:---|:---|:---|
| | | | |

---

## [ECOSYSTEM] ↔ [HỆ 3] Integration

<!-- Tiếp tục thêm section cho mỗi hệ tích hợp -->

---

## Bảng tóm tắt tích hợp

<!--
  Đây là chunk quan trọng nhất của file — chatbot dùng khi khách hỏi overview.
  VD: "KNX kết nối được với những hệ nào?"
  Bảng này phải luôn nhất quán với các section chi tiết ở trên.
-->

| Hệ tích hợp | Khả năng | Phương thức | Chiều | Sản phẩm cần thêm |
|:---|:---|:---|:---|:---|
| [HỆ 1] | ✅ Native | Direct bus | Hai chiều | — |
| [HỆ 2] | ✅ Qua gateway | Gateway vật lý | Hai chiều | [SKU gateway] |
| [HỆ 3] | ⚠️ Giới hạn | Scene trigger | Một chiều | [SKU] |
| [HỆ 4] | ❌ Không hỗ trợ | — | — | — |

**Chú thích:**
- ✅ Tích hợp đầy đủ, khuyến nghị sử dụng
- ⚠️ Tích hợp được nhưng có giới hạn kỹ thuật hoặc cần điều kiện
- ❌ Không thể tích hợp trực tiếp — cần giải pháp khác

---

## Câu hỏi thường gặp về tích hợp

<!--
  Tập trung vào câu hỏi TÍCH HỢP — không lặp lại FAQ sản phẩm.
  Format: câu hỏi viết như cách khách thật sự hỏi.
-->

**[ECOSYSTEM] có thể điều khiển đèn của hệ [HỆ KHÁC] không?**
[Trả lời có/không + điều kiện + thiết bị cần thêm nếu có.]

**Tích hợp [ECOSYSTEM] với [HỆ KHÁC] có phức tạp không?**
[Trả lời thực tế — đừng understate độ phức tạp nếu thật sự phức tạp.]

**Khi [ECOSYSTEM] và [HỆ KHÁC] cùng điều khiển một đèn, hệ nào được ưu tiên?**
[Trả lời rõ ràng — đây là câu hỏi quan trọng trong thực tế thi công.]

**Có thể hiển thị trạng thái thiết bị [HỆ KHÁC] trên giao diện [ECOSYSTEM] không?**
[Trả lời + điều kiện nếu có.]

**Chi phí tích hợp thêm [HỆ KHÁC] vào hệ [ECOSYSTEM] đang có là bao nhiêu?**
Chi phí phụ thuộc vào quy mô dự án và thiết bị gateway cụ thể. Liên hệ KNXStore để được tư vấn và báo giá phù hợp với bài toán của bạn.

---

## Lưu ý cho chatbot

<!--
  Section này KHÔNG hiển thị cho người dùng cuối.
  Chatbot đọc để biết cách xử lý câu hỏi tích hợp.
-->

Khi khách hỏi về tích hợp [ECOSYSTEM] với hệ khác:

1. Xác định chiều tích hợp: khách muốn [ECOSYSTEM] điều khiển hệ kia, hay ngược lại, hay hai chiều?
2. Xác định quy mô: số lượng điểm điều khiển ảnh hưởng đến lựa chọn gateway.
3. Nếu tích hợp CÓ THỂ → nêu phương thức + sản phẩm cần + link.
4. Nếu tích hợp KHÔNG THỂ → nói rõ, đề xuất giải pháp thay thế nếu có.
5. Nếu câu hỏi phức tạp (nhiều hệ, dự án lớn) → handoff sang sales/kỹ thuật KNXStore.

Không đoán mò khả năng tích hợp nếu không có trong file này — trả lời "Trường hợp này cần xác nhận thêm, liên hệ KNXStore để được tư vấn cụ thể."