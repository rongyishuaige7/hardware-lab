# Hardware Lab

我独立完成的软硬件原型索引。这里优先展示源码、可复现构建、实物/媒体证据和当前真机复测范围，不把“编译通过”写成“硬件已验证”。

> **状态日期：2026-07-17。** 当前收录 7 个公开项目。每个固定 Actions 链接都对应所列默认分支 HEAD；Actions Artifact 仅保留 14 天，不是永久下载。

## 项目

### [ESP32 RPS Game](https://github.com/rongyishuaige7/ESP32_RPS_Game)

基于摄像头手势识别的剪刀石头布硬件游戏，包含 OLED、音频、RGB 反馈与可选 MJPEG 推流。

- **平台：** ESP32-S3 · C++ · PlatformIO · OV3660
- **构建证据：** [`7cc39bd4ace7`](https://github.com/rongyishuaige7/ESP32_RPS_Game/commit/7cc39bd4ace77febee17320fe8a2efd8ac06b205) · [Actions 成功](https://github.com/rongyishuaige7/ESP32_RPS_Game/actions/runs/29339478819)
- **真机状态：** 当前默认分支已完成固件编译验证；未发现与当前提交绑定的日期化真机复测记录。
- **公开范围：** 当前仓库未公开实物照片、演示视频或 EDA/制造文件。
- **边界：** CI 只证明固定配置下的固件构建和 Artifact 上传；板型、引脚或摄像头配置变化后仍需重新烧录核对。

### [Multimodal Smart Pot](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot)

多模态桌面智能花盆原型，覆盖环境感知、双泵灌溉、本地彩屏、局域网控制、语音与手势交互。

- **平台：** ESP32-S3 · C++ · PlatformIO · FreeRTOS · EasyEDA
- **构建证据：** [`aacb1c0c3beb`](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/commit/aacb1c0c3beb4add79a740d838166c63cf95b10c) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/actions/runs/29518255431)
- **真机状态：** 2026-04-16 的历史照片显示定制 PCB、传感器读数、本地彩屏和配套 App 界面；当前公开提交未重新刷写并逐项真机验收。
- **公开范围：** 两张去除 EXIF/GPS 的历史实物照片，以及原理图 PDF、EasyEDA PCB JSON、BOM 和 Gerber/钻孔文件；没有演示视频，App 源码未找回。
- **边界：** 历史照片不证明当前提交已真机复测；EDA 引脚和 Flash 配置与当前公开固件仍有已披露的版本边界。

### [STM32 Multisensor Data Acquisition](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition)

多传感器数据采集教学原型，包含 Flash 历史与离线缓存、ESP-01S AT 联网、TCP JSON 工具、OLED 与告警。

- **平台：** STM32F103 · C · PlatformIO · STM32Cube HAL · W25Q64 · ESP-01S
- **构建证据：** [`850fb32b667f`](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/commit/850fb32b667f43c4f7ecdb5ebbb014b91b70a96f) · [Actions 成功](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/actions/runs/29521309526)
- **真机状态：** Source-confirmed · Build-verified · Current hardware re-test not run。
- **公开范围：** 当前没有实物照片、演示视频、EDA、PCB 或制造文件；公开 BOM 和接线边界图，接线图不是 PCB 原理图。
- **边界：** ESP/调试串口是源码级裁决，传感器电气接口仍需实物确认；TCP 无认证和 TLS，只面向可信局域网。

### [LoRa Warehouse Tracking System](https://github.com/rongyishuaige7/lora-warehouse-tracking-system)

仓库区域追踪教学原型，包含 LoRa 标签/网关固件、Flask/SQLite 服务与 Kotlin Android 客户端。

- **平台：** ESP32 · LoRa/SX1278 · C++ · PlatformIO · Flask · SQLite · Kotlin
- **构建证据：** [`81975420ff15`](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/commit/81975420ff15182fd412b978c79acdf2279d608e) · [Actions 成功](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/actions/runs/29525240951)
- **真机状态：** Source-confirmed · Tag/Gateway build-verified · Server tests passed · Android build-verified · Current end-to-end hardware re-test not run。
- **公开范围：** 当前没有实物照片、演示视频、App 截图、EDA、PCB 或制造文件；公开 BOM 和接线边界图，接线图不是 PCB 原理图。
- **边界：** QUERY 不能唤醒深睡标签，定位只确认命令下发到网关；HTTP 与 LoRa 均无认证或加密，仅限隔离可信局域网教学环境。

### [车流量自适应交通信号控制系统](https://github.com/rongyishuaige7/adaptive-traffic-signal-system)

四路 ESP32-CAM 车流量自适应交通信号教学原型，包含 YOLOv8 跟踪/过线计数、FastAPI、Vue 3、WebSocket、12 路信号灯和四块 OLED。

- **平台：** ESP32-CAM × 4 · ESP32 · YOLOv8 · FastAPI · Vue 3 · WebSocket
- **构建证据：** [`9526890934fa`](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/commit/9526890934fa5488677493333e2637bd717141e5) · [Actions 成功](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/actions/runs/29563350321)
- **真机状态：** 源码已确认；后端测试、Vue 前端构建、东南西北四路 ESP32-CAM 和 ESP32 主控构建已通过；当前五板实物与端到端链路尚未重新真机复测。
- **公开范围：** FastAPI/Vue 源码、双固件、模拟器、BOM 和接线边界图；当前没有真实实物照片、演示视频、界面截图、EDA 或制造文件。
- **边界：** 模拟器和构建不证明检测准确率、物理灯态或道路安全；接口无认证/TLS，仅限隔离可信局域网桌面教学模型，不能用于真实道路信号控制。

### [ESP32-S3 健康科普语音终端](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal)

基于本地唤醒、讯飞流式 ASR/TTS、DeepSeek SSE、双 I²S 音频和 LVGL 显示的健康科普语音终端教学原型。

- **平台：** ESP32-S3 · ESP-IDF · ESP-SR · 讯飞 · DeepSeek · LVGL · FreeRTOS
- **构建证据：** [`d7b6d8d48945`](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/commit/d7b6d8d48945fc149f0df3e0ca44e16c1e31252d) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/actions/runs/29563950558)
- **真机状态：** 源码、硬件无关契约与 ESP-IDF 5.5.2 干净构建已验证；当前 ESP32-S3、INMP441、MAX98357A、ST7789 与真实云端链路尚未重新真机复测。
- **公开范围：** 当前未公开真实实物照片、演示视频、EDA、PCB 或制造文件；已公开 BOM、接线边界图、协议、来源与验证说明。
- **边界：** CI 使用空凭据，构建和源码契约不证明真实讯飞/DeepSeek 调用、ASR/TTS、首包延迟、语音质量或硬件行为；这不是医疗器械、诊断、处方或急救系统，Actions Artifact 仅保留 14 天。

### [Raspberry Pi RFID Room-card System](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system)

双 RC522 房卡管理教学原型，包含树莓派 Python 服务、MariaDB、Qt/C++ 管理端、服务端角色权限、房态与审计记录。

- **平台：** Raspberry Pi · Python · Qt/C++ · MariaDB · RC522 · SG90
- **构建证据：** [`9880b7d9de71`](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/commit/9880b7d9de71cfa75376a3720fde270359ffedbe) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/actions/runs/29551405935)
- **真机状态：** Source-confirmed · Python tests passed · Qt 5/6 client build-verified · Historical UI demonstrated on 2026-04-03 · Current Raspberry Pi and end-to-end hardware re-test not run。
- **公开范围：** 四张去元数据并遮盖私网 IP/UID 的历史界面截图、BOM、接线边界图、服务端、Qt 客户端和数据库 schema；当前没有实物照片、演示视频、EDA 或制造文件。
- **边界：** 自定义 TCP 无 TLS，RC522 UID 可复制，SG90 无位置反馈；仅限隔离可信局域网教学原型，不是生产门禁系统。

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
