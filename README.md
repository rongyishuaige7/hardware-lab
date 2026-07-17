# Hardware Lab

我独立完成的软硬件原型索引。这里优先展示源码、可复现构建、实物/媒体证据和当前真机复测范围，不把“编译通过”写成“硬件已验证”。

> **状态日期：2026-07-17。** 当前收录 13 个公开项目。每个固定 Actions 链接都对应所列默认分支 HEAD；Actions Artifact 仅保留 14 天，不是永久下载。

## 命名规范

索引名称统一采用毕业设计常见的表述：**“基于{核心平台/技术}的{功能对象}”**。其中“系统”“终端”“游戏”“花盆”等后缀按原型实际形态保留；名称只说明技术范围与功能主题，不扩大真机、性能或安全结论。仓库 URL、构建证据、真机状态和公开边界均保持不变。

## 项目

### [基于ESP32-S3的视觉猜拳游戏](https://github.com/rongyishuaige7/ESP32_RPS_Game)

基于摄像头手势识别的剪刀石头布硬件游戏，包含 OLED、音频、RGB 反馈与可选 MJPEG 推流。

- **平台：** ESP32-S3 · C++ · PlatformIO · OV3660
- **构建证据：** [`7cc39bd4ace7`](https://github.com/rongyishuaige7/ESP32_RPS_Game/commit/7cc39bd4ace77febee17320fe8a2efd8ac06b205) · [Actions 成功](https://github.com/rongyishuaige7/ESP32_RPS_Game/actions/runs/29339478819)
- **真机状态：** 当前默认分支已完成固件编译验证；未发现与当前提交绑定的日期化真机复测记录。
- **公开范围：** 当前仓库未公开实物照片、演示视频或 EDA/制造文件。
- **边界：** CI 只证明固定配置下的固件构建和 Artifact 上传；板型、引脚或摄像头配置变化后仍需重新烧录核对。

### [基于ESP32-S3的多模态交互桌面智能花盆](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot)

多模态桌面智能花盆原型，覆盖环境感知、双泵灌溉、本地彩屏、局域网控制、语音与手势交互。

- **平台：** ESP32-S3 · C++ · PlatformIO · FreeRTOS · EasyEDA
- **构建证据：** [`aacb1c0c3beb`](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/commit/aacb1c0c3beb4add79a740d838166c63cf95b10c) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/actions/runs/29518255431)
- **真机状态：** 2026-04-16 的历史照片显示定制 PCB、传感器读数、本地彩屏和配套 App 界面；当前公开提交未重新刷写并逐项真机验收。
- **公开范围：** 两张去除 EXIF/GPS 的历史实物照片，以及原理图 PDF、EasyEDA PCB JSON、BOM 和 Gerber/钻孔文件；没有演示视频，App 源码未找回。
- **边界：** 历史照片不证明当前提交已真机复测；EDA 引脚和 Flash 配置与当前公开固件仍有已披露的版本边界。

### [基于STM32的多传感器数据采集系统](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition)

多传感器数据采集教学原型，包含 Flash 历史与离线缓存、ESP-01S AT 联网、TCP JSON 工具、OLED 与告警。

- **平台：** STM32F103 · C · PlatformIO · STM32Cube HAL · W25Q64 · ESP-01S
- **构建证据：** [`850fb32b667f`](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/commit/850fb32b667f43c4f7ecdb5ebbb014b91b70a96f) · [Actions 成功](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/actions/runs/29521309526)
- **真机状态：** Source-confirmed · Build-verified · Current hardware re-test not run。
- **公开范围：** 当前没有实物照片、演示视频、EDA、PCB 或制造文件；公开 BOM 和接线边界图，接线图不是 PCB 原理图。
- **边界：** ESP/调试串口是源码级裁决，传感器电气接口仍需实物确认；TCP 无认证和 TLS，只面向可信局域网。

### [基于LoRa和ESP32的仓库物品追踪定位系统](https://github.com/rongyishuaige7/lora-warehouse-tracking-system)

仓库区域追踪教学原型，包含 LoRa 标签/网关固件、Flask/SQLite 服务与 Kotlin Android 客户端。

- **平台：** ESP32 · LoRa/SX1278 · C++ · PlatformIO · Flask · SQLite · Kotlin
- **构建证据：** [`81975420ff15`](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/commit/81975420ff15182fd412b978c79acdf2279d608e) · [Actions 成功](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/actions/runs/29525240951)
- **真机状态：** Source-confirmed · Tag/Gateway build-verified · Server tests passed · Android build-verified · Current end-to-end hardware re-test not run。
- **公开范围：** 当前没有实物照片、演示视频、App 截图、EDA、PCB 或制造文件；公开 BOM 和接线边界图，接线图不是 PCB 原理图。
- **边界：** QUERY 不能唤醒深睡标签，定位只确认命令下发到网关；HTTP 与 LoRa 均无认证或加密，仅限隔离可信局域网教学环境。

### [基于多路ESP32-CAM的车流量自适应交通信号控制系统](https://github.com/rongyishuaige7/adaptive-traffic-signal-system)

四路 ESP32-CAM 车流量自适应交通信号教学原型，包含 YOLOv8 跟踪/过线计数、FastAPI、Vue 3、WebSocket、12 路信号灯和四块 OLED。

- **平台：** ESP32-CAM × 4 · ESP32 · YOLOv8 · FastAPI · Vue 3 · WebSocket
- **构建证据：** [`9526890934fa`](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/commit/9526890934fa5488677493333e2637bd717141e5) · [Actions 成功](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/actions/runs/29563350321)
- **真机状态：** 源码已确认；后端测试、Vue 前端构建、东南西北四路 ESP32-CAM 和 ESP32 主控构建已通过；当前五板实物与端到端链路尚未重新真机复测。
- **公开范围：** FastAPI/Vue 源码、双固件、模拟器、BOM 和接线边界图；当前没有真实实物照片、演示视频、界面截图、EDA 或制造文件。
- **边界：** 模拟器和构建不证明检测准确率、物理灯态或道路安全；接口无认证/TLS，仅限隔离可信局域网桌面教学模型，不能用于真实道路信号控制。

### [基于ESP32-S3的健康科普语音交互终端](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal)

基于本地唤醒、讯飞流式 ASR/TTS、DeepSeek SSE、双 I²S 音频和 LVGL 显示的健康科普语音终端教学原型。

- **平台：** ESP32-S3 · ESP-IDF · ESP-SR · 讯飞 · DeepSeek · LVGL · FreeRTOS
- **构建证据：** [`d7b6d8d48945`](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/commit/d7b6d8d48945fc149f0df3e0ca44e16c1e31252d) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/actions/runs/29563950558)
- **真机状态：** 源码、硬件无关契约与 ESP-IDF 5.5.2 干净构建已验证；当前 ESP32-S3、INMP441、MAX98357A、ST7789 与真实云端链路尚未重新真机复测。
- **公开范围：** 当前未公开真实实物照片、演示视频、EDA、PCB 或制造文件；已公开 BOM、接线边界图、协议、来源与验证说明。
- **边界：** CI 使用空凭据，构建和源码契约不证明真实讯飞/DeepSeek 调用、ASR/TTS、首包延迟、语音质量或硬件行为；这不是医疗器械、诊断、处方或急救系统，Actions Artifact 仅保留 14 天。

### [基于树莓派和RFID的房卡管理系统](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system)

双 RC522 房卡管理教学原型，包含树莓派 Python 服务、MariaDB、Qt/C++ 管理端、服务端角色权限、房态与审计记录。

- **平台：** Raspberry Pi · Python · Qt/C++ · MariaDB · RC522 · SG90
- **构建证据：** [`9880b7d9de71`](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/commit/9880b7d9de71cfa75376a3720fde270359ffedbe) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/actions/runs/29551405935)
- **真机状态：** Source-confirmed · Python tests passed · Qt 5/6 client build-verified · Historical UI demonstrated on 2026-04-03 · Current Raspberry Pi and end-to-end hardware re-test not run。
- **公开范围：** 四张去元数据并遮盖私网 IP/UID 的历史界面截图、BOM、接线边界图、服务端、Qt 客户端和数据库 schema；当前没有实物照片、演示视频、EDA 或制造文件。
- **边界：** 自定义 TCP 无 TLS，RC522 UID 可复制，SG90 无位置反馈；仅限隔离可信局域网教学原型，不是生产门禁系统。

### [基于STM32的触摸与隔空手势控制系统](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system)

使用四路电容触摸和 APDS-9960 隔空手势控制四路 LED，并通过 ESP-01S 本地热点展示状态与诊断的教学原型。

- **平台：** STM32F103 · C++ · PlatformIO · STM32Cube HAL · TTP223 · APDS-9960 · ESP-01S
- **构建证据：** [`92ab1128ac3a`](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system/commit/92ab1128ac3a106ff52550d7375e8c6d20cdface) · [Actions 成功](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system/actions/runs/29566341512)
- **真机状态：** 源码来源、硬件无关源码契约与 PlatformIO 干净构建已验证；当前 STM32、TTP223、APDS-9960、ESP-01S 与 LED 整机尚未重新真机复测。
- **公开范围：** 当前没有实物照片、演示视频、EDA、PCB 或制造文件；已公开 BOM、接线边界图、协议、来源与验证说明。
- **边界：** 构建和源码契约不证明触摸可靠性、APDS 识别率、ESP AT 兼容性或实际 LED 行为；HTTP 无认证和 TLS，仅限隔离可信的教学热点，GPIO 不得直接驱动大电流或市电负载。


### [基于ESP32的智能闹钟系统](https://github.com/rongyishuaige7/esp32-smart-alarm-clock)

基于 ESP32、OLED、DHT11、PIR、MAX98357A 与 Flutter 局域网客户端的智能闹钟教学原型。

- **平台：** ESP32 · Arduino · PlatformIO · Flutter · OLED · DHT11 · PIR · MAX98357A
- **构建证据：** [`7aeb1a23b6a2`](https://github.com/rongyishuaige7/esp32-smart-alarm-clock/commit/7aeb1a23b6a28f8d5efe5da63c3561bf003da676) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-alarm-clock/actions/runs/29569475061)
- **真机状态：** 源码来源、硬件无关源码契约、ESP32 固件与 Flutter 客户端构建已验证；当前 ESP32、OLED、DHT11、PIR、MAX98357A、实体按键及 Flutter App 端到端链路尚未重新真机复测。
- **公开范围：** 当前没有实物照片、演示视频、EDA、PCB 或制造文件；已公开 BOM、接线边界图、协议、来源与验证说明。原始 WAV 的再分发许可未逐一确认，当前仓库不分发音频素材。
- **边界：** AP 配网和 STA REST 均使用无认证、无 TLS 的本地 HTTP，只限隔离可信局域网；没有使用者自备的合法 WAV 时，声音功能不会完成。构建不等同于 NTP、传感器、OLED、I²S、按钮、Wi-Fi 或 App 端到端验证。

### [基于ESP32的天气时钟](https://github.com/rongyishuaige7/esp32-weather-clock)

基于 ESP32、DHT22、BH1750、DS3231、SSD1306 OLED 与本地 AP 配网的天气时钟教学原型。

- **平台：** ESP32 · Arduino · PlatformIO · DHT22 · BH1750 · DS3231 · SSD1306 · Wi-Fi
- **构建证据：** [`73533ee4ebf3`](https://github.com/rongyishuaige7/esp32-weather-clock/commit/73533ee4ebf3e78b7613afe50b9128df80a00353) · [Actions 成功](https://github.com/rongyishuaige7/esp32-weather-clock/actions/runs/29575555202)
- **真机状态：** 源码来源、公开凭据净化、无硬件源码契约与 ESP32 PlatformIO 构建已验证；当前 ESP32、DHT22、BH1750、DS3231、OLED、Wi-Fi、NTP、EEPROM 与天气 API 端到端链路尚未重新真机复测。
- **公开范围：** 当前没有公开实物照片、演示视频、原理图、PCB、Gerber 或制造文件；已公开 BOM、源码推导接线边界图、来源、协议与验证说明。
- **边界：** AP 配网、`/scan` 和 `/save` 是无认证、无 TLS 的本地 HTTP；EEPROM 不是安全存储，天气请求当前使用 `setInsecure()` 而不校验证书。固件构建不证明传感器、OLED、RTC、Wi-Fi、NTP、天气数据或长期稳定性；Flash 占用 79.1%，Actions Artifact 仅保留 14 天。

### [基于ESP32的智能药盒系统](https://github.com/rongyishuaige7/esp32-smart-pillbox)

基于 ESP32、双 PIR、双 HX711、RGB/蜂鸣器与 Flutter 局域网客户端的智能药盒教学原型。

- **平台：** ESP32 · Arduino · PlatformIO · Flutter · PIR · HX711 · SPIFFS · HTTP
- **构建证据：** [`aab0b8d1dc0d`](https://github.com/rongyishuaige7/esp32-smart-pillbox/commit/aab0b8d1dc0da455468df41eb3920dd677b4cefe) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-pillbox/actions/runs/29573085427)
- **真机状态：** 源码来源、硬件无关源码契约、ESP32 固件与 Flutter 客户端构建已验证；当前 ESP32、两个 PIR、两个 HX711、RGB、蜂鸣器、SPIFFS、Wi-Fi、NTP 与 Flutter App 端到端链路尚未重新真机复测。
- **公开范围：** 当前没有公开实物照片、演示视频、原理图、PCB、Gerber 或制造文件；已公开 BOM、源码推导接线边界图、协议、来源与验证说明。
- **边界：** 原型状态机不构成服药确认、诊断、护理、医疗结论或紧急处置。AP 配网和 STA REST 均使用无认证、无 TLS 的本地 HTTP，只限隔离可信局域网；构建不等同于 PIR、HX711、RGB、蜂鸣器、SPIFFS、Wi-Fi、NTP 或 App 端到端验证。

### [基于ESP32-S3的多传感器智能安全监测系统](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor)

ESP32-S3 多传感器监测教学原型，包含 MQ-2/MQ-5 原始采样、火焰与超声波输入、OLED、本地状态页和低压执行器分时逻辑。

- **平台：** ESP32-S3 · ESP-IDF · PlatformIO · FreeRTOS · MQ-2 · MQ-5 · SSD1306 · HC-SR04
- **构建证据：** [`b39f55f16181`](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor/commit/b39f55f1618184df5ae9bb6c7a611d3a6129ab36) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor/actions/runs/29577699732)
- **真机状态：** 源码来源、公开净化、无硬件源码契约与 ESP32-S3 固件构建已验证；当前开发板、MQ-2、MQ-5、火焰、HC-SR04、OLED、蜂鸣器、泵、风扇、舵机与本地网络状态页尚未按当前公开提交重新真机复测。
- **公开范围：** 当前未公开实物照片、演示视频、EDA、PCB、Gerber 或制造文件；已公开 BOM、源码推导接线边界图、来源、协议、状态与验证说明。
- **边界：** 固定热点密码不公开；启用后的 SoftAP/SSE 无认证、无 TLS，只限隔离可信测试网络。构建不证明传感器准确、硬件动作或安全效果，不能用于火灾/燃气报警、自动灭火、通风安全、生命安全或生产控制；Flash 占用 82.3%，Actions Artifact 仅保留 14 天。


### [基于树莓派的多传感器小型气象站](https://github.com/rongyishuaige7/raspberry-pi-weather-station)

树莓派采集 DHT22 温湿度与 BH1750 光照，写入 MySQL，经 Flask REST API 供 Avalonia / C# 上位机查看、查询历史和维护阈值的教学原型。

- **平台：** Raspberry Pi · Python · Flask · MySQL · C# · Avalonia · DHT22 · BH1750
- **构建证据：** [`8eecf90294ac`](https://github.com/rongyishuaige7/raspberry-pi-weather-station/commit/8eecf90294ac53c9915ec6b430a80b519917a34c) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-weather-station/actions/runs/29580328463)
- **真机状态：** 源码来源、公开净化、Python/API/隔离 MySQL mock 联调与 Avalonia 构建已验证；当前 Raspberry Pi、DHT22、BH1750、真实 MySQL 部署与 LAN 端到端链路尚未按当前公开提交重新真机复测。
- **公开范围：** 当前未公开实物照片、演示视频、EDA、PCB、Gerber、制造文件、系统镜像或真实数据库；已公开源码、BOM、接线边界、协议、来源与验证说明。
- **边界：** `USE_MOCK_SENSORS=1` 只生成随机模拟数据；API `/api/health`、人工 `devices.status` 与最新记录均不代表真实传感器、实时采样或设备在线。HTTP、Bearer JWT 与 MySQL 只适合隔离可信教学网络；本项目不是气象仪器、环境安全或生产控制系统。

## 状态口径

| 状态 | 含义 |
|:--|:--|
| Source-confirmed | 能力或引脚可由当前公开源码确认 |
| Build-verified | 当前默认分支在记录的 CI 中完成可复现构建 |
| Historically demonstrated | 日期化历史素材能证明画面中可见的原型表面，但不绑定当前提交 |
| Hardware re-verified | 当前提交已在实物上按日期化清单重新验收 |

## 索引维护

[`projects.yml`](projects.yml) 是机器可读索引，采用 JSON 兼容的 YAML 1.2 语法。CI 会核对：

- 仓库仍为 Public，默认分支仍为 `main`；
- 索引 SHA 等于远程默认分支 HEAD；
- 固定 Actions run 已成功并对应同一 HEAD；
- README 中的仓库、Actions 和短 SHA 与索引同步；
- 真机、媒体和 Artifact 保留范围没有被静默省略。

本索引不展示手填 Star 数、访客计数、虚假在线状态或安装按钮。项目变更后，应先更新证据再改状态文案。
