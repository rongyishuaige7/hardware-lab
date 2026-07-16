# Hardware Lab

我独立完成的软硬件原型索引。这里优先展示源码、可复现构建、实物/媒体证据和当前真机复测范围，不把“编译通过”写成“硬件已验证”。

> **状态日期：2026-07-17。** 当前收录 3 个公开项目。每个固定 Actions 链接都对应所列默认分支 HEAD；Actions Artifact 仅保留 14 天，不是永久固件下载。

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
