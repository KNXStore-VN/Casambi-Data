---
# ================================================================
# BLOCK 1 — FILE IDENTIFICATION
# ================================================================
file_type: "integration_guide"
ecosystem: "Casambi"
version: "1.0"
last_updated: "2026-05-08"
last_verified_by: "knxstore-marketing"
confidence_level: "high"

# ================================================================
# BLOCK 2 — ECOSYSTEM OVERVIEW
# ================================================================
ecosystem_type: "wireless_standard"

primary_use_cases:
  - "lighting_control"
  - "dali_control"
  - "scene_automation"
  - "daylight_harvesting"
  - "occupancy_control"
  - "hvac_integration"
  - "blind_control"

typical_project_scale: ["small", "medium", "large"]

key_strengths:
  - "Bluetooth Mesh — không cần hub trung gian, hoạt động offline hoàn toàn"
  - "Hơn 2000 sản phẩm tương thích từ 200+ thương hiệu"
  - "Hỗ trợ DALI, DMX, 0-10V, Triac native qua các CBU module"
  - "Casambi App miễn phí, không subscription cho hệ cơ bản"

# ================================================================
# BLOCK 3 — INTEGRATION MAP
# ================================================================
can_integrate_with:
  dali: "native"
  dali_2: "native"
  knx: "gateway"
  matter: "bridge"
  bacnet: "gateway_ip"
  modbus: "gateway_rs485"
  dmx: "gateway"
  hvac_dali: "native_via_dali"
  artnet: "gateway_ip"
  mqtt: "gateway_ip"
  0_10v: "native_via_cbu"
  triac: "native_via_cbu"

cannot_integrate_with:
  - "KNX RF (chỉ hỗ trợ KNX TP qua gateway)"
  - "Zigbee native (không có bridge trực tiếp)"
  - "Z-Wave native"

requires_gateway_for:
  - "KNX"
  - "Matter"
  - "BACnet"
  - "Modbus"
  - "DMX (nếu không dùng CBU module)"
  - "ArtNet"
  - "MQTT"

native_integration_with:
  - "DALI / DALI-2 (qua CBU-DA, CBU-DCS, SAL series)"
  - "0-10V (qua CBU-A2D)"
  - "Triac / Phase cut (qua CBU-TED, CBU-PWM)"
  - "PWM (qua CBU-PWM4)"
  - "EnOcean (qua module tương thích)"

# ================================================================
# BLOCK 4 — CHATBOT BEHAVIOR
# ================================================================
chatbot_priority: "high"

related_product_files:
  - "product_CBU-DA-1P.md"
  - "product_CBU-DCS.md"
  - "product_CGW-001.md"
  - "product_VBU-K2C-W-BI.md"
  - "product_MTB10.md"
  - "product_Lithernet.md"

related_integration_files:
  - "integration_knx.md"
  - "integration_dali.md"
  - "integration_matter.md"
---

# Casambi Integration Guide – Kết nối với các hệ khác

## Tổng quan về Casambi

Casambi là hệ điều khiển chiếu sáng không dây sử dụng Bluetooth Low Energy Mesh (BLE Mesh), phát triển bởi Casambi Technologies (Phần Lan). Toàn bộ logic điều khiển lưu trong mạng lưới thiết bị — không cần hub trung gian, không phụ thuộc internet, hoạt động offline hoàn toàn.

Điểm mạnh chính của Casambi là tính mở ở biên: hệ core chạy BLE Mesh độc lập, nhưng thông qua các gateway và module chuyển đổi, Casambi có thể kết nối với DALI, KNX, Matter, BACnet, Modbus, DMX, MQTT và nhiều chuẩn khác. Hơn 200 thương hiệu với 2000+ sản phẩm tương thích trong hệ sinh thái Casambi.

Trong danh mục KNXStore, Casambi tích hợp được với: DALI (native), KNX (qua gateway), Matter (qua bridge), BACnet/Modbus (qua gateway IP), DMX (qua gateway), 0-10V và Triac (native qua CBU module).

---

## Quy tắc tích hợp chung

### Nguyên tắc cơ bản

- **Casambi là hệ độc lập trên BLE Mesh:** mọi thiết bị hệ khác muốn giao tiếp với Casambi đều cần gateway hoặc bridge — không có cách kết nối trực tiếp ngoại trừ các chuẩn native như DALI, 0-10V, Triac.
- **Casambi ưu tiên lệnh local:** khi có xung đột lệnh từ gateway bên ngoài và lệnh từ Casambi App/switch local, lệnh local luôn được thực thi ngay lập tức. Lệnh từ gateway có độ trễ tùy loại gateway.
- **Hai phiên bản network với giới hạn node khác nhau:**
  - **Classic:** tối đa 127 nodes — tương thích với thiết bị cũ hơn, ít tính năng hơn.
  - **Evolution:** tối đa 250 nodes — tính năng nâng cao, hỗ trợ Long Range mode, DALI-2 input device, remote commissioning. Tất cả thiết bị mới từ KNXStore đều là Evolution.
  - Classic và Evolution devices **không thể mix** trong cùng một network.
- **Gateway chiếm 1 node** trong network. Với SAL series, mỗi DALI driver được đánh địa chỉ cũng chiếm 1 node Casambi riêng — cần tính kỹ khi dùng SAL trong dự án nhiều driver.

### Các phương thức tích hợp phổ biến

| Phương thức | Mô tả | Ưu điểm | Giới hạn |
|:---|:---|:---|:---|
| CBU module native | Thiết bị Casambi tích hợp sẵn giao thức khác (DALI, 0-10V...) | Không cần thiết bị thêm, latency thấp nhất | Chỉ cho các chuẩn được hỗ trợ native |
| Gateway vật lý | Thiết bị chuyển đổi giao thức (KNX↔Casambi, BACnet↔Casambi) | Ổn định, không phụ thuộc cloud | Chi phí thêm, cần cấu hình |
| IP Bridge | Kết nối qua mạng LAN (Lithernet, AIMOTION Gateway) | Linh hoạt, hỗ trợ nhiều giao thức cùng lúc | Cần network ổn định, có thể phụ thuộc cloud |
| Matter Bridge | Expose Casambi devices lên Matter ecosystem | Tích hợp với Apple Home, Google Home, Alexa | Chỉ một chiều (Matter điều khiển Casambi) |
| Casambi Cloud API | Tích hợp qua internet thông qua Cloud Gateway | Dễ setup cho remote access | Phụ thuộc internet và cloud Casambi |

---

## Casambi ↔ DALI Integration

### Tổng quan

DALI là chuẩn điều khiển bus có dây phổ biến nhất cho đèn thương mại. Casambi tích hợp DALI theo cách native — các CBU module (CBU-DA-1P, CBU-DCS, SAL series) vừa là node Casambi vừa là DALI master, không cần gateway trung gian.

**Khả năng tích hợp:** ✅ Native — được hỗ trợ đầy đủ

**Chiều tích hợp:**
- Casambi → DALI: ✅ Đầy đủ (dimming, scene, group, sensor automation)
- DALI → Casambi: ✅ Có (DALI-2 input devices — cảm biến, push button — xuất hiện như Casambi sensor/switch)
- Hai chiều: ✅ Với DALI-2

### Cách thực hiện

**Phương án duy nhất (native): Dùng CBU module**

CBU module đóng vai trò DALI master, nhận lệnh từ Casambi BLE Mesh và phát lệnh DALI xuống bus. Không cần gateway bổ sung.

Thiết bị cần có:
- CBU-DA-1P (tối đa 50 DALI driver) hoặc CBU-DCS (tối đa 64 driver)
- SAL-1016 / SAL-1032 cho dự án nhiều zone DALI lớn hơn
- Driver LED tương thích DALI DT6 hoặc DT8

Bước thực hiện:
1. Đấu nguồn AC và kết nối bus DALI vào CBU module.
2. Thêm CBU module vào Casambi network qua App.
3. Chọn Fixture Profile phù hợp (Broadcast, Short Address, Group, DT8 TW, RGBW...).
4. Cảm biến DALI-2 trên bus sẽ tự xuất hiện như Casambi sensor nếu chọn đúng profile Ext.Sensors.

### Giới hạn & Lưu ý

- **1 DALI master per bus:** CBU module là DALI master — không thể có thêm DALI master khác trên cùng bus.
- **Driver không phải DALI:** CBU-DA-1P không điều khiển được driver chỉ có 0-10V, Triac, hay PWM — cần dùng CBU-A2D (0-10V) hoặc CBU-TED (Triac) thay thế.
- **DALI-2 vs DALI:** DALI-2 input devices (cảm biến, push button) hoạt động tốt hơn, có thể tích hợp thành Casambi sensor. DALI-1 thuần chỉ hỗ trợ dimming cơ bản.

### Sản phẩm KNXStore liên quan

| Vai trò | Sản phẩm | SKU | Link |
|:---|:---|:---|:---|
| DALI master (50 driver) | Olfer CBU-DA-1P | CBU-DA-1P | [Xem sản phẩm](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-da-1p) |
| DALI master (64 driver) | Olfer CBU-DCS | CBU-DCS | [Xem sản phẩm](https://knxstore.vn/products/casambi-bo-dieu-khien-dali-cbu-dcs) |
| DALI master nhiều zone | Salvador SAL-1016 | SAL-1016 | [Xem sản phẩm](https://knxstore.vn/products/bo-dieu-khien-16-dia-chi-driver-dali-master-salvador-casambi-sal-1016) |

> 💬 **Câu hỏi phổ biến:** "Cần bao nhiêu CBU-DA-1P cho dự án 200 đèn?"
> → Mỗi CBU-DA-1P quản lý 1 bus DALI tối đa 50 driver. Dự án 200 đèn cần tối thiểu 4 CBU-DA-1P (mỗi cái 1 bus riêng), hoặc dùng SAL-1032 cho kiến trúc tập trung hơn.

---

## Casambi ↔ KNX Integration

### Tổng quan

KNX là hệ bus có dây tiêu chuẩn quốc tế cho building automation, mạnh về độ tin cậy và tích hợp HVAC/rèm/bảo mật. Casambi và KNX là hai hệ độc lập hoàn toàn — KNX chạy trên bus TP có dây, Casambi chạy BLE Mesh không dây. Kết nối cần gateway vật lý.

**Khả năng tích hợp:** ✅ Có, qua gateway

**Chiều tích hợp:**
- KNX → Casambi: ✅ Có (KNX gửi lệnh on/off, dimming, scene trigger sang Casambi)
- Casambi → KNX: ✅ Có (trạng thái Casambi phản hồi về KNX — tùy gateway)
- Hai chiều: ✅ Bidirectional với VBU-K2C-W-BI, tối đa 32 channel + 32 scene

### Cách thực hiện

**Phương án chính: Gateway VBU-K2C-W-BI**

VBU-K2C-W-BI là gateway bridge KNX ↔ Casambi, kết nối vật lý vào bus KNX TP và tham gia vào Casambi network như 1 node BLE.

Thiết bị cần có:
- VBU-K2C-W-BI (gateway chính)
- KNX IP Interface hoặc KNX USB Interface để lập trình ETS
- ETS Software để cấu hình group address KNX

Bước thực hiện:
1. Kết nối VBU-K2C-W-BI vào bus KNX TP.
2. Thêm vào Casambi network qua App — xuất hiện dưới tab Gateways.
3. Map KNX group address với Casambi group/scene trong Casambi App.
4. Lập trình KNX trong ETS để gửi telegram đúng group address.

**Phương án thay thế: Lithernet Gateway (qua IP)**

Lithernet Gateway kết nối Casambi qua Ethernet, hỗ trợ KNX/IP (Loxone), BACnet/IP, Modbus, MQTT, ArtNet đồng thời trong 1 thiết bị — phù hợp dự án cần tích hợp nhiều hệ cùng lúc.

### Giới hạn & Lưu ý

- **Tối đa 32 KNX channel + 32 Casambi scene** với VBU-K2C-W-BI — đủ cho phần lớn dự án vừa.
- **Độ trễ:** lệnh từ KNX → Casambi → DALI thường 300–500ms — không phù hợp cho ứng dụng cần phản hồi tức thì như emergency lighting.
- **Casambi ưu tiên local:** nếu người dùng vừa tắt đèn qua Casambi App, KNX không tự biết — phản hồi trạng thái cần cấu hình riêng.
- **KNX RF không hỗ trợ:** VBU-K2C-W-BI chỉ kết nối KNX TP, không hỗ trợ KNX RF.

### Sản phẩm KNXStore liên quan

| Vai trò | Sản phẩm | SKU | Link |
|:---|:---|:---|:---|
| Gateway KNX↔Casambi | Vlinca VBU-K2C-W-BI | VBU-K2C-W-BI | [Xem sản phẩm](https://knxstore.vn/products/casambi-thiet-bi-chuyen-doi-knx-sang-casambi-vbu-k2c-w-bi) |
| Gateway đa giao thức | Lithernet Gateway | Lithernet | [Xem sản phẩm](https://knxstore.vn/products/lithernet-gateway-tich-hop-casambi-dua-tren-ethernet) |

> 💬 **Câu hỏi phổ biến:** "Casambi và KNX cùng điều khiển 1 đèn thì hệ nào ưu tiên?"
> → Lệnh nào đến sau thì thắng. Không có priority cứng — người dùng cần thiết kế logic để tránh xung đột, thường bằng cách chia zone riêng cho từng hệ.

---

## Casambi ↔ Matter Integration

### Tổng quan

Matter là chuẩn IoT mới do CSA Alliance phát triển (Apple, Google, Amazon, Samsung tham gia). Casambi là thành viên CSA Alliance từ 2022 và hỗ trợ Matter qua bridge device. Kết nối Matter cho phép điều khiển thiết bị Casambi từ Apple Home, Google Home, Amazon Alexa, Samsung SmartThings và các nền tảng Matter khác.

**Khả năng tích hợp:** ✅ Có, qua Matter Bridge

**Chiều tích hợp:**
- Matter → Casambi: ✅ Có (Apple Home, Google Home, Alexa điều khiển đèn Casambi)
- Casambi → Matter: ⚠️ Giới hạn (trạng thái đèn được mirror sang Matter, nhưng scene/schedule của Casambi không sync sang)
- Hai chiều: ⚠️ Một phần — control hai chiều được, nhưng config (tên, scene) phải thiết lập lại trong Matter platform

### Cách thực hiện

**Phương án chính: Rayrun MTB10**

MTB10 là Casambi Ecosystem device, tham gia Casambi network như 1 node, tự động map tất cả thiết bị Casambi tương thích sang Matter. Kết nối qua WiFi 2.4GHz, cấp nguồn USB-C 5V/1A.

Thiết bị cần có:
- Rayrun MTB10
- WiFi router 2.4GHz
- Matter controller (Apple HomePod, Google Nest Hub, Amazon Echo...)

Bước thực hiện:
1. Thêm MTB10 vào Casambi network qua App (xuất hiện dưới tab Gateways).
2. MTB10 tự động map toàn bộ thiết bị Casambi tương thích sang Matter — không cần cấu hình thêm trong Casambi.
3. Mở Apple Home / Google Home / Alexa → Add Accessory → Scan QR code trên MTB10.
4. Thiết bị Casambi xuất hiện như native Matter accessory trong platform đã chọn.

### Giới hạn & Lưu ý

- **Tên và scene không được transfer:** device names, groups, scenes đã tạo trong Casambi App không sang Matter — phải đặt lại tên trong Apple Home/Google Home.
- **Chỉ hỗ trợ thiết bị tương thích:** ON/OFF, dimmer, tunable white, RGB, RGB+CCT, presence sensor, light sensor — không phải tất cả Casambi device đều được map.
- **WiFi 2.4GHz bắt buộc:** MTB10 không hỗ trợ 5GHz. Đặt MTB10 gần router để đảm bảo tín hiệu ổn định.
- **Casambi vẫn là master:** commissioning và cấu hình kỹ thuật vẫn làm trong Casambi App — Matter chỉ là lớp điều khiển thêm.

### Sản phẩm KNXStore liên quan

| Vai trò | Sản phẩm | SKU | Link |
|:---|:---|:---|:---|
| Casambi–Matter Bridge | Rayrun MTB10 | MTB10 | [Xem sản phẩm](https://knxstore.vn/products/bo-dieu-khien-casambi-to-matter-bridge-rayrun-mtb10) |

> 💬 **Câu hỏi phổ biến:** "Dùng MTB10 thì có điều khiển Casambi bằng Siri được không?"
> → Được. Sau khi MTB10 map vào Apple Home, bạn dùng Siri điều khiển đèn bình thường. Scene của Apple Home cũng có thể include đèn Casambi.

---

## Casambi ↔ BACnet / Modbus Integration

### Tổng quan

BACnet và Modbus là hai giao thức phổ biến trong hệ thống BMS (Building Management System) của các tòa nhà thương mại, văn phòng, khách sạn. Kết nối Casambi với BMS cho phép giám sát và điều khiển chiếu sáng từ hệ thống quản lý tòa nhà tập trung.

**Khả năng tích hợp:** ✅ Có, qua gateway IP

**Chiều tích hợp:**
- BACnet/Modbus → Casambi: ✅ Có (BMS gửi lệnh điều khiển chiếu sáng)
- Casambi → BACnet/Modbus: ✅ Có (trạng thái đèn, sensor data phản hồi về BMS)
- Hai chiều: ✅ Bidirectional

### Cách thực hiện

**Phương án chính: Lithernet Gateway**

Lithernet Gateway kết nối Casambi qua Ethernet (LAN), hỗ trợ BACnet/IP, Modbus TCP/RTU, KNX/IP, MQTT, ArtNet đồng thời. Phù hợp cho dự án tòa nhà cần tích hợp nhiều giao thức cùng lúc.

Thiết bị cần có:
- Lithernet Gateway
- Kết nối LAN ổn định
- BMS hỗ trợ BACnet/IP hoặc Modbus TCP

**Phương án thay thế: Thermokon Gateway (RS485)**

Thermokon Casambi Gateway hỗ trợ BACnet MS/TP và Modbus RTU qua RS485 — phù hợp khi BMS dùng kết nối serial RS485 thay vì IP.

### Giới hạn & Lưu ý

- **Cần mạng LAN ổn định** cho Lithernet Gateway — Casambi network và BMS phải cùng subnet hoặc có routing phù hợp.
- **Cấu hình phức tạp hơn:** tích hợp BACnet/Modbus đòi hỏi kỹ sư có kinh nghiệm về cả BMS lẫn Casambi.
- **Latency cao hơn:** lệnh từ BMS → Lithernet → Casambi thường 500ms–1s tùy tải mạng.

### Sản phẩm KNXStore liên quan

| Vai trò | Sản phẩm | SKU | Link |
|:---|:---|:---|:---|
| Gateway đa giao thức IP | Lithernet Gateway | Lithernet | [Xem sản phẩm](https://knxstore.vn/products/lithernet-gateway-tich-hop-casambi-dua-tren-ethernet) |

---

## Casambi ↔ DMX Integration

### Tổng quan

DMX512 là chuẩn điều khiển chiếu sáng sân khấu và architectural lighting. Casambi kết nối DMX theo hai hướng: Casambi điều khiển fixture DMX (qua gateway DMX→Casambi), hoặc trigger DMX scene từ Casambi.

**Khả năng tích hợp:** ✅ Có, qua gateway

**Chiều tích hợp:**
- Casambi → DMX: ✅ Có (Casambi gửi lệnh dimming/scene sang thiết bị DMX)
- DMX → Casambi: ⚠️ Giới hạn (tùy gateway)
- Hai chiều: ⚠️ Phụ thuộc thiết bị

### Cách thực hiện

**Phương án chính: casDMX hoặc DMXcas module**

- `casDMX`: Casambi → DMX — nhận lệnh từ Casambi network, phát tín hiệu DMX512 ra 8 kênh.
- `SceneDMXcas`: cho phép trigger DMX scene từ Casambi network — phù hợp cho showroom, sân khấu, nhà hàng.

### Sản phẩm KNXStore liên quan

| Vai trò | Sản phẩm | SKU | Link |
|:---|:---|:---|:---|
| Casambi → DMX (đa kênh) | casDMX | casDMX | [Xem sản phẩm](https://knxstore.vn/products/bo-dieu-khien-dmx-da-kenh-casambi-voi-radio-tam-xa-casdmx) |
| Scene trigger DMX | SceneDMXcas | SceneDMXcas | [Xem sản phẩm](https://knxstore.vn/products/bo-chuyen-doi-dmx-sang-casambi-chon-ngu-canh-scenedmxcas) |
| DMX 8 kênh | DMXcas | DMXcas | [Xem sản phẩm](https://knxstore.vn/products/bo-dieu-khien-do-sang-dmx-casambi-8-kenh-dmxcas) |

---

## Bảng tóm tắt tích hợp Casambi

| Hệ tích hợp | Khả năng | Phương thức | Chiều | Sản phẩm cần thêm |
|:---|:---|:---|:---|:---|
| DALI / DALI-2 | ✅ Native | CBU module | Hai chiều | CBU-DA-1P / CBU-DCS / SAL |
| 0-10V | ✅ Native | CBU-A2D | Một chiều (out) | CBU-A2D |
| Triac / Phase | ✅ Native | CBU-TED | Một chiều (out) | CBU-TED |
| KNX TP | ✅ Gateway | Gateway vật lý | Hai chiều (32ch) | VBU-K2C-W-BI |
| Matter | ✅ Bridge | Matter Bridge | Hai chiều (giới hạn) | Rayrun MTB10 |
| BACnet/IP | ✅ Gateway | Gateway IP | Hai chiều | Lithernet Gateway |
| Modbus TCP | ✅ Gateway | Gateway IP | Hai chiều | Lithernet Gateway |
| Modbus RTU / RS485 | ✅ Gateway | Gateway RS485 | Hai chiều | Thermokon Gateway |
| DMX512 | ✅ Gateway | Gateway DMX | Một/hai chiều | casDMX / DMXcas |
| MQTT | ✅ Gateway | Gateway IP | Hai chiều | Lithernet Gateway |
| ArtNet | ✅ Gateway | Gateway IP | Một chiều (out) | Lithernet Gateway |
| KNX RF | ❌ Không hỗ trợ | — | — | — |
| Zigbee | ❌ Không trực tiếp | — | — | Cần middleware |
| Z-Wave | ❌ Không trực tiếp | — | — | Cần middleware |

**Chú thích:**
- ✅ Tích hợp đầy đủ, khuyến nghị sử dụng
- ⚠️ Tích hợp được nhưng có giới hạn kỹ thuật hoặc cần điều kiện
- ❌ Không thể tích hợp trực tiếp

---

## Câu hỏi thường gặp về tích hợp Casambi

**Casambi có cần internet để hoạt động không?**
Không. Casambi hoạt động hoàn toàn offline qua BLE Mesh. Internet chỉ cần cho remote access (qua Cloud Gateway CGW-001) hoặc khi dùng Matter Bridge MTB10 (cần WiFi cho MTB10, không phải cho Casambi core).

**Casambi có thể kết nối với hệ KNX đang có sẵn không?**
Có. Dùng gateway VBU-K2C-W-BI để bridge KNX TP ↔ Casambi. Tối đa 32 KNX channel và 32 Casambi scene. Cần lập trình ETS để map group address.

**Có thể điều khiển Casambi bằng giọng nói (Siri, Google, Alexa) không?**
Có, thông qua Matter Bridge Rayrun MTB10. Sau khi kết nối, đèn Casambi xuất hiện trong Apple Home / Google Home / Alexa và hỗ trợ điều khiển bằng giọng nói bình thường.

**Dự án có BMS BACnet, có tích hợp Casambi được không?**
Có. Lithernet Gateway hỗ trợ BACnet/IP bidirectional — BMS điều khiển và nhận trạng thái chiếu sáng từ Casambi. Cần kỹ sư có kinh nghiệm BMS để cấu hình.

**Casambi và KNX cùng điều khiển một vùng đèn, có xung đột không?**
Không xung đột kỹ thuật, nhưng lệnh nào đến sau sẽ thắng. Nên phân vùng rõ ràng hoặc thiết kế logic ưu tiên trong ETS để tránh hành vi không mong muốn.

**Tích hợp Casambi với BACnet/Modbus có phức tạp không?**
Phức tạp hơn so với KNX hoặc Matter. Cần kỹ sư hiểu cả hai phía: cấu hình Casambi network và cấu hình BMS. KNXStore có thể hỗ trợ tư vấn kỹ thuật — liên hệ qua Zalo [0918.918.755](https://zalo.me/0918918755).

---

## Lưu ý cho chatbot

Khi khách hỏi về tích hợp Casambi với hệ khác:

1. Xác định chiều tích hợp: hệ kia điều khiển Casambi, Casambi điều khiển hệ kia, hay hai chiều?
2. Xác định quy mô và môi trường: dự án nhà ở hay thương mại? Có BMS không? Cần remote access không?
3. Nếu tích hợp CÓ THỂ → nêu phương thức + sản phẩm cần + link sản phẩm KNXStore.
4. Nếu tích hợp KHÔNG THỂ trực tiếp → ghi rõ, đề xuất giải pháp thay thế.
5. Nếu câu hỏi phức tạp (nhiều hệ, dự án lớn, BMS) → handoff sang sales/kỹ thuật KNXStore qua Zalo [0918.918.755](https://zalo.me/0918918755).

Không đoán mò khả năng tích hợp nếu không có trong file này. Trả lời: "Trường hợp này cần xác nhận thêm, vui lòng liên hệ KNXStore để được tư vấn cụ thể."