---
# === IDENTIFICATION ===
sku: "Lithernet-GW"
product_name: "Lithernet - Casambi Gateway"
brand: "Lichtmanufaktur"
manufacturer_part_number: "Lithernet-GW"
hubspot_product_id: ""
website_url: "https://knxstore.vn/products/lithernet-gateway-tich-hop-casambi-dua-tren-ethernet"
status: "active"

# === CLASSIFICATION ===
category_primary: "Gateways"
category_secondary: ["Protocol Integration", "Building Automation"]
protocols: ["Casambi", "Ethernet", "Bluetooth", "ArtNet", "BacNet/IP", "MQTT", "KNX/IP", "HomeAssistant", "HelvarNet", "Netcomposer"]

# === SHORT DESCRIPTION ===
short_description_vi: "Gateway đa giao thức Lithernet tích hợp Casambi với Ethernet PoE, hỗ trợ ArtNet, BacNet/IP, MQTT, KNX/IP, HomeAssistant"
short_description_en: "Lithernet Casambi Gateway with multi-protocol integration, PoE Ethernet, supports ArtNet, BacNet/IP, MQTT, KNX/IP, HomeAssistant, and more"

# === SEARCH OPTIMIZATION ===
aliases: ["Lithernet", "Lithernet Gateway", "Casambi Multi-Protocol Gateway", "Intelligent Lighting Gateway"]
search_keywords_vi: ["Lithernet", "gateway", "Casambi", "ArtNet", "BacNet", "MQTT", "KNX", "Ethernet", "PoE", "tích hợp"]
search_keywords_en: ["Lithernet", "gateway", "Casambi", "ArtNet", "BacNet/IP", "MQTT", "KNX/IP", "multi-protocol", "Ethernet", "PoE"]

# === DECISION CRITERIA ===
use_case_tags: ["multi_protocol_gateway", "building_automation", "lighting_integration", "system_bridge"]
target_segment: ["system_integrator", "commercial_installation", "smart_building"]
project_scale: ["large", "enterprise"]
complexity_level: "advanced"
not_suitable_for: ["standalone_device", "simple_dimmer", "diy_residential"]

# === RELATIONSHIPS ===
replaces_sku: []
replaced_by_sku: null
equivalent_skus: []
accessories_required: ["Casambi Network", "Ethernet Connection", "PoE Power"]
accessories_recommended: ["IP Network Infrastructure", "Building Automation System"]
bundle_with: []
upsell_to: []

# === CASAMBI INTEGRATION ===
casambi_network_type: ["all"]
casambi_pro_compatible: true
fixture_profile_default_id: "gateway"
fixture_profile_default_name: "Lithernet Gateway"
fixture_profile_alternatives: ["gateway_REV0", "gateway_REV1", "gateway_REV2", "gateway_REV2.5"]

# === COMMERCIAL REFERENCE ===
pricing_visibility: "sales_only"
stock_visibility: "sales_only"
moq_hint: "Liên hệ sales để biết MOQ và bậc giá theo số lượng"
warranty_months: 24
origin_country: "Germany"
hs_code_vn: ""

# === ASSETS ===
images:
  main: ""
  hardware: ""
  led_panel: ""
datasheet_url: "https://archiv.intelligent-lighting.de"
manual_url_en: "https://intelligent-lighting.de"
manual_url_vi: null

# === FAQ EMBEDDED ===
common_questions:
  - question_vi: "Lithernet là gì?"
    answer_vi: "Lithernet là gateway chuyên nghiệp tích hợp mạng Casambi với các hệ thống building automation khác (ArtNet, BacNet, MQTT, KNX, HomeAssistant)"
  - question_vi: "Lithernet cần mấy kết nối?"
    answer_vi: "Chỉ cần 1 cổng Ethernet RJ-45. Cấp nguồn qua PoE (Power over Ethernet), không cần adapter riêng"
  - question_vi: "Hỗ trợ những giao thức nào?"
    answer_vi: "ArtNet, BacNet/IP, MQTT, KNX/IP, HomeAssistant, HelvarNet, Netcomposer, UDP/TCP commands, Casambi Bridge"
  - question_vi: "Firmware Lithernet là gì?"
    answer_vi: "4 phiên bản firmware: 1.XX (Classic), 2.XX (Evolution 33.22+), 3.XX (Evolution 34.50+), 4.XX (Evolution 39.50+). Mỗi phiên bản cần setup lại"
  - question_vi: "Có bao nhiêu hardware revision?"
    answer_vi: "4 revision: REV0, REV1, REV2, REV2.5. Mỗi revision hỗ trợ firmware khác nhau. Có thể nâng cấp REV2 ↔ REV2.5"

# === HANDOFF TRIGGERS ===
handoff_to_sales_when:
  - "user_asks_price"
  - "user_asks_stock"
  - "user_asks_quotation"
  - "user_asks_discount"
  - "user_asks_lead_time"
  - "user_asks_payment_terms"
  - "user_asks_delivery"
  - "user_asks_custom_integration"
  - "user_asks_protocol_mapping"
  - "user_asks_firmware_support"

# === DATA GOVERNANCE ===
last_updated: "2026-04-21"
last_verified_by: "auto_converter"
content_version: "1.0"
source_of_truth: "GATEWAY - Casambi Lithernet.md"
confidence_level: "high"
chatbot_priority: "high"

# === RAG OPTIMIZATION ===
chunk_strategy: "by_section"
priority_sections:
  - "Mô tả sản phẩm"
  - "Thông số kỹ thuật"
  - "Giao thức hỗ trợ"
  - "Hardware Revision"
  - "Firmware Version"
  - "Cài đặt & Tích hợp"
  - "FAQ"

---

# Lithernet - Casambi Gateway

## Đặc điểm nổi bật

✅ **Đa giao thức** - ArtNet, BacNet/IP, MQTT, KNX/IP, HomeAssistant, HelvarNet, Netcomposer, và nhiều hơn

✅ **PoE Ethernet duy nhất** - Chỉ cần 1 cổng RJ-45, cấp nguồn tích hợp (không cần adapter)

✅ **Bluetooth Casambi tích hợp** - Kết nối trực tiếp mạng Casambi (CBM-002A/CBM-003B module)

✅ **LED Status Display** - 4 LED hiển thị trạng thái hoạt động, mạng, UDP, TCP/IP

✅ **Phiên bản firmware linh hoạt** - 4 phiên bản: 1.XX, 2.XX, 3.XX, 4.XX (tương thích Casambi Classic & Evolution)

✅ **Hardware Revision 0-2.5** - Hỗ trợ nhiều phiên bản, có thể nâng cấp REV2 ↔ REV2.5

✅ **Watchdog tự động** - Restart tự động nếu cần (90s timeout)

## Mô tả sản phẩm

Lithernet là gateway chuyên nghiệp được phát triển bởi Lichtmanufaktur Berlin GmbH, cho phép tích hợp mạng Casambi với các hệ thống building automation và điều khiển chiếu sáng khác nhau. Thiết bị sử dụng kết nối Ethernet PoE duy nhất, giảm độ phức tạp cài đặt và bảo trì.

**Ứng dụng chính:**
- Gateway tới hệ thống điều khiển lighting hiện có (Netcomposer, Helvar)
- Cầu nối giữa các mạng Casambi riêng biệt
- Tích hợp hệ thống đánh giá / visualization
- ArtNet gateway cho thiết bị DMX/lighting
- BacNet/IP gateway cho building management systems
- MQTT broker cho IoT integration
- KNX/IP gateway cho hệ thống KNX
- HomeAssistant integration cho smart home

## Thông số kỹ thuật

### Kết nối & Nguồn

| Thông số | Giá trị |
|---------|--------|
| Kết nối mạng | 1x RJ-45 Ethernet (duy nhất) |
| Cấp nguồn | Power over Ethernet (PoE) |
| Bluetooth | CBM-002A (REV0/1) hoặc CBM-003B (REV2/2.5) |
| Tần số BLE | 2.4 GHz |

### LED Status Display

| LED | Vị trí | Trạng thái |
|-----|--------|----------|
| 1. Operating | Dưới cùng | Green: Hoạt động (nhấp nháy 1s) |
| 2. Network | | Yellow: Mạng cắm |
| 3. UDP | | Red: Không có UDP, Green: UDP OK |
| 4. TCP/IP | Trên cùng | Red: Không có TCP/IP, Green: TCP/IP OK |

### Hardware Revision

| Revision | Firmware | Casambi | Bluetooth Module | Notes |
|----------|----------|---------|-----------------|-------|
| **REV 0** | 1.XX | Classic + Evolution <33.22 | CBM-002A | Cũ nhất |
| **REV 1** | 1.XX, 2.XX, 3.XX | Classic + Evolution | CBM-002A | Dùng được nhiều phiên bản |
| **REV 2** | 3.XX, 4.XX | Evolution ≥34.50 | CBM-003B | Mới, có thể up REV2.5 |
| **REV 2.5** | 4.XX only | Evolution ≥39.50 | CBM-003B | Mới nhất |

**Upgrade/Downgrade REV2 ↔ REV2.5:**
- Có thể chuyển đổi qua Casambi App bằng cách đổi profile
- Cần unpair → change profile → re-pair → update firmware

### Firmware Compatibility

| Firmware | Casambi Version | Status |
|----------|-----------------|--------|
| 1.XX | Classic + Evolution <33.22 | Cũ |
| 2.XX | Evolution ≥33.22 | Cũ |
| 3.XX | Evolution ≥34.50 | Phổ biến |
| 4.XX | Evolution ≥39.50 | Mới nhất (beta 4.41) |

**⚠️ Quan trọng:** Backup files không tương thích giữa phiên bản firmware. Phải setup lại khi cập nhật.

### Nút Reset & Watchdog

| Chức năng | Chi tiết |
|-----------|---------|
| **Reset Button** | Trên circuit board (mở 4 vít dưới) - chỉ hoạt động với devices mfg date >03/2022 |
| | 0-15s: LED test program |
| | 15-30s: Soft reset (IP settings + login) |
| | >30s: Hard reset (toàn bộ settings + memory) |
| **Watchdog** | 90s timeout, restart tự động nếu cần |

## Giao thức hỗ trợ

### Network Protocols

✅ **UDP/TCP** - Lệnh ASCII tự do

✅ **ArtNet** - DMX to Casambi, Casambi to DMX (512+ channels)

✅ **BacNet/IP** - Building automation integration, sensors & commands

✅ **MQTT** - IoT integration, publish/subscribe control

✅ **KNX/IP** - European standard building automation

✅ **HomeAssistant** - Smart home platform integration

✅ **HelvarNet (TCP)** - Helvar lighting systems

✅ **Netcomposer** - Netcomposer lighting systems

✅ **Casambi Bridge** - Bridge mode (UDP), network bridge

✅ **Casambi Command** - UDP/TCP Casambi protocol

### Sensor Support

- Light sensors (Lux)
- Presence sensors (PIR)
- Custom elements & button events
- Scene status
- Target status & color

## Lắp đặt & Cấu hình

### Bước cài đặt cơ bản

1. **Kết nối Ethernet:** RJ-45 vào switch/router (PoE)
2. **Cấp điện:** Tự động qua PoE (không cần adapter)
3. **Kết nối Casambi:** Pair device vào mạng Casambi qua App
4. **Cấu hình Giao thức:** 
   - Vào web interface của gateway
   - Đăng nhập (default credentials)
   - Chọn giao thức (ArtNet, BacNet, MQTT, KNX, etc.)
   - Cấu hình protocol-specific settings

### Network Settings

- **IP Configuration:** DHCP hoặc Static IP
- **Webserver Login:** Username/Password
- **NTP Client:** Đồng bộ thời gian
- **Restart:** Reboot từ web interface

### Casambi Settings

- **Profile Selection:** Chọn REV0/1/2/2.5 phù hợp
- **Behave as:**
  - Lamp (thiết bị chiếu sáng)
  - Button (nút điều khiển)
  - PIR Sensor (cảm biến chuyển động)
  - Lux Sensor (cảm biến ánh sáng)
- **Identify:** Flash LED 10s để xác định thiết bị
- **Firmware Update:** OTA via web interface

## Lưu ý quan trọng

⚠️ **Firmware Compatibility:**
- Cập nhật firmware phải phù hợp với hardware revision
- Backup từ phiên bản cũ không dùng được với phiên bản mới
- Phải setup lại toàn bộ khi nâng cấp

⚠️ **LED Status (lên đến 60s để hiển thị):**
- LED 3 & 4 (UDP/TCP) có thể mất 60s để hiển thị đúng sau restart
- Đây là bình thường, không phải lỗi

⚠️ **Protocol Configuration:**
- Mỗi giao thức có cài đặt riêng (ArtNet, BacNet, MQTT, KNX, etc.)
- Sử dụng "Control System Wizard" để tìm cài đặt phù hợp
- Hỗ trợ ánh xạ (mapping) từ giao thức này sang giao thức khác

⚠️ **PoE Power Requirement:**
- Cần PoE power source hỗ trợ đủ dòng
- Dùng Ethernet duy nhất (không cần dây riêng)

## Tính năng nâng cao

### Automation

- Tạo automation rules từ web interface
- Trigger: Time-based, sensor-based, scene-based
- Actions: Control scenes, groups, dimming, colors

### Console / Debug

- Web-based console để monitor hoạt động
- UDP Debug Port để test commands
- Đi kèm LanLog.exe tool để logging

### Button & Sensor Simulation

- Có thể simulate button press/release
- Test presence/light sensor values
- Useful cho commissioning & testing

## Ứng dụng

**Tòa nhà cao tầng:** Bridge Casambi with BacNet/IP building management system

**Nhà hát/Sân khấu:** ArtNet gateway để điều khiển DMX fixtures từ Casambi

**Smart Home:** HomeAssistant integration cho control toàn bộ hệ thống

**Retail/Museum:** Bridge giữa Casambi networks trong các phòng khác nhau

**Office/Campus:** KNX/IP gateway để tích hợp với existing KNX infrastructure

## Tài liệu kỹ thuật

📄 **Tài liệu chính thức:**

👉 [Trang sản phẩm Lithernet](https://knxstore.vn/products/lithernet-gateway-tich-hop-casambi-dua-tren-ethernet)

👉 [User Manual (PDF)](https://archiv.intelligent-lighting.de)

👉 [Intelligent Lighting](https://intelligent-lighting.de) - Nhà sản xuất

## Bảo hành & Hỗ trợ

- **Bảo hành:** 24 tháng
- **Hỗ trợ:** knxstore.vn
- **Xuất xứ:** Germany (Lichtmanufaktur Berlin GmbH)
- **Certifications:** CE, FCC, IC, UK CA, KCC (REV2)

---

**Ghi chú:** Lithernet là gateway đa giao thức chuyên nghiệp cho các cài đặt building automation phức tạp. Thích hợp cho integrator và những dự án yêu cầu tích hợp Casambi với các hệ thống điều khiển chiếu sáng/building automation khác.
