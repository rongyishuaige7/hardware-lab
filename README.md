# Hardware Lab

我独立完成的软硬件项目作品集，收录源码、项目介绍、构建记录和可公开的项目资料。

> **更新日期：2026-07-19。** 当前收录 22 个公开项目。每个“Actions 成功”链接均对应所列默认分支的最新提交；部分项目提供短期 Actions Artifact。

## 项目

### [基于ESP32-S3的视觉猜拳游戏](https://github.com/rongyishuaige7/ESP32_RPS_Game)

基于摄像头手势识别的剪刀石头布硬件游戏，包含 OLED、音频、RGB 反馈与可选 MJPEG 推流。

- **技术栈：** ESP32-S3 · C++ · PlatformIO · OV3660
- **构建证据：** [`2a403fceabe9`](https://github.com/rongyishuaige7/ESP32_RPS_Game/commit/2a403fceabe998a7481da2ee4ae556c663d590ed) · [Actions 成功](https://github.com/rongyishuaige7/ESP32_RPS_Game/actions/runs/29658176252)
- **项目资料：** 原理图资料

### [基于ESP32-S3的多模态交互桌面智能花盆](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot)

多模态桌面智能花盆原型，覆盖环境感知、双泵灌溉、本地彩屏、局域网控制、语音与手势交互。

- **技术栈：** ESP32-S3 · C++ · PlatformIO · FreeRTOS · EasyEDA
- **构建证据：** [`3436184ea476`](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/commit/3436184ea4763dc6541dd8ef4cd3e14a1cc3066e) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/actions/runs/29658003504)
- **项目资料：** 项目照片、PCB 与制造资料

### [基于STM32的多传感器数据采集系统](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition)

多传感器数据采集教学原型，包含 Flash 历史与离线缓存、ESP-01S AT 联网、TCP JSON 工具、OLED 与告警。

- **技术栈：** STM32F103 · C · PlatformIO · STM32Cube HAL · W25Q64 · ESP-01S
- **构建证据：** [`f4513869538c`](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/commit/f4513869538c8a55a9b39479c0c219753ab7bd75) · [Actions 成功](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/actions/runs/29658004607)
- **项目资料：** 项目照片

### [基于LoRa和ESP32的仓库物品追踪定位系统](https://github.com/rongyishuaige7/lora-warehouse-tracking-system)

仓库区域追踪教学原型，包含 LoRa 标签/网关固件、Flask/SQLite 服务与 Kotlin Android 客户端。

- **技术栈：** ESP32 · LoRa/SX1278 · C++ · PlatformIO · Flask · SQLite · Kotlin
- **构建证据：** [`8bc1b566a566`](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/commit/8bc1b566a566963a8538535b3e13d0f32d30b566) · [Actions 成功](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/actions/runs/29658005560)
- **项目资料：** 项目照片与原理图资料

### [基于多路ESP32-CAM的车流量自适应交通信号控制系统](https://github.com/rongyishuaige7/adaptive-traffic-signal-system)

四路 ESP32-CAM 车流量自适应交通信号教学原型，包含 YOLOv8 跟踪/过线计数、FastAPI、Vue 3、WebSocket、12 路信号灯和四块 OLED。

- **技术栈：** ESP32-CAM × 4 · ESP32 · YOLOv8 · FastAPI · Vue 3 · WebSocket
- **构建证据：** [`61e839e16481`](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/commit/61e839e164812b395f289788a3abf214688256ef) · [Actions 成功](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/actions/runs/29658006499)
- **项目资料：** 项目照片、界面截图与 PCB 资料

### [基于ESP32-S3的健康科普语音交互终端](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal)

基于本地唤醒、讯飞流式 ASR/TTS、DeepSeek SSE、双 I²S 音频和 LVGL 显示的健康科普语音终端教学原型。

- **技术栈：** ESP32-S3 · ESP-IDF · ESP-SR · 讯飞 · DeepSeek · LVGL · FreeRTOS
- **构建证据：** [`0b7a24659826`](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/commit/0b7a246598265480f0da6912bb89f285b6aa7230) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/actions/runs/29658129899)
- **项目资料：** 项目照片

### [基于树莓派和RFID的房卡管理系统](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system)

双 RC522 房卡管理教学原型，包含树莓派 Python 服务、MariaDB、Qt/C++ 管理端、服务端角色权限、房态与审计记录。

- **技术栈：** Raspberry Pi · Python · Qt/C++ · MariaDB · RC522 · SG90
- **构建证据：** [`79e9511ddd31`](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/commit/79e9511ddd3115f908302f6ce963606e52c6e6d4) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/actions/runs/29658008602)
- **项目资料：** 项目照片与界面截图

### [基于STM32的触摸与隔空手势控制系统](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system)

使用四路电容触摸和 APDS-9960 隔空手势控制四路 LED，并通过 ESP-01S 本地热点展示状态与诊断的教学原型。

- **技术栈：** STM32F103 · C++ · PlatformIO · STM32Cube HAL · TTP223 · APDS-9960 · ESP-01S
- **构建证据：** [`a4373083d9da`](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system/commit/a4373083d9da4a99b58389d9c2fae7d6544e41e8) · [Actions 成功](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system/actions/runs/29658131455)
- **项目资料：** 项目照片与原理图资料

### [基于ESP32的智能闹钟系统](https://github.com/rongyishuaige7/esp32-smart-alarm-clock)

基于 ESP32、OLED、DHT11、PIR、MAX98357A 与 Flutter 局域网客户端的智能闹钟教学原型。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · OLED · DHT11 · PIR · MAX98357A
- **构建证据：** [`599a1b88e8bc`](https://github.com/rongyishuaige7/esp32-smart-alarm-clock/commit/599a1b88e8bc1e7d2297bc81ace7dfc7a5ae7d8f) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-alarm-clock/actions/runs/29658133396)
- **项目资料：** 项目照片、界面截图与原理图资料

### [基于ESP32的智能药盒系统](https://github.com/rongyishuaige7/esp32-smart-pillbox)

基于 ESP32、双 PIR、双 HX711、RGB/蜂鸣器与 Flutter 局域网客户端的智能药盒教学原型。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · PIR · HX711 · SPIFFS · HTTP
- **构建证据：** [`880cf190e17d`](https://github.com/rongyishuaige7/esp32-smart-pillbox/commit/880cf190e17ddd57ffc9e9c8220bffa03ff1f9d2) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-pillbox/actions/runs/29658011421)
- **项目资料：** 项目照片与原理图资料

### [基于ESP32的天气时钟](https://github.com/rongyishuaige7/esp32-weather-clock)

基于 ESP32、DHT22、BH1750、DS3231、SSD1306 OLED 与本地 AP 配网的天气时钟教学原型。

- **技术栈：** ESP32 · Arduino · PlatformIO · DHT22 · BH1750 · DS3231 · SSD1306 · Wi-Fi
- **构建证据：** [`f8d6668774cf`](https://github.com/rongyishuaige7/esp32-weather-clock/commit/f8d6668774cf81e82c7409065f73b2daa73197fd) · [Actions 成功](https://github.com/rongyishuaige7/esp32-weather-clock/actions/runs/29658012825)
- **项目资料：** 项目照片、原理图与 PCB 资料

### [基于ESP32-S3的多传感器智能安全监测系统](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor)

ESP32-S3 多传感器监测教学原型，包含 MQ-2/MQ-5 原始采样、火焰与超声波输入、OLED、本地状态页和低压执行器分时逻辑。

- **技术栈：** ESP32-S3 · ESP-IDF · PlatformIO · FreeRTOS · MQ-2 · MQ-5 · SSD1306 · HC-SR04
- **构建证据：** [`c0764e822928`](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor/commit/c0764e822928c8bd0f6d44ebcd478caf8c13dbc9) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor/actions/runs/29658135574)
- **项目资料：** 原理图、PCB 与制造资料

### [基于树莓派的多传感器小型气象站](https://github.com/rongyishuaige7/raspberry-pi-weather-station)

树莓派采集 DHT22 温湿度与 BH1750 光照，写入 MySQL，经 Flask REST API 供 Avalonia / C# 上位机查看、查询历史和维护阈值的教学原型。

- **技术栈：** Raspberry Pi · Python · Flask · MySQL · C# · Avalonia · DHT22 · BH1750
- **构建证据：** [`1e836128d79c`](https://github.com/rongyishuaige7/raspberry-pi-weather-station/commit/1e836128d79c0059daf0a4351740c21195abd441) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-weather-station/actions/runs/29658136769)
- **项目资料：** 界面与日志截图

### [基于ESP32的婴儿状态监测原型](https://github.com/rongyishuaige7/esp32-baby-monitor)

两路距离、温湿度与声音幅度输入驱动 ESP32 中的演示级固定阈值分类、RGB/蜂鸣器本地反馈和可选可信局域网 JSON 接口。

- **技术栈：** ESP32 · Arduino · PlatformIO · HC-SR04 · DHT11 · 模拟声音输入 · WebServer
- **构建证据：** [`9936a30c19f8`](https://github.com/rongyishuaige7/esp32-baby-monitor/commit/9936a30c19f8f78988182a0ad017fa61c94ef659) · [Actions 成功](https://github.com/rongyishuaige7/esp32-baby-monitor/actions/runs/29658138692)
- **项目资料：** 项目照片与原理图资料

### [基于ESP32的蜂箱多传感器数据采集与局域网展示原型](https://github.com/rongyishuaige7/esp32-beehive-monitor)

ESP32 读取 DHT11、BH1750、BMP280、模拟声音幅度和 MQ-2 原始 ADC；使用者本地配置后，Flutter 客户端可在可信局域网请求一条本地 JSON 响应。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · DHT11 · BH1750 · BMP280 · 模拟 ADC · 本地 HTTP
- **构建证据：** [`4642d27154e7`](https://github.com/rongyishuaige7/esp32-beehive-monitor/commit/4642d27154e751d055b05aa9500d3232ff9a7444) · [Actions 成功](https://github.com/rongyishuaige7/esp32-beehive-monitor/actions/runs/29658140085)
- **项目资料：** 项目照片、原理图与 PCB 资料

### [基于ESP32的多路智能照明控制系统](https://github.com/rongyishuaige7/esp32-smart-light-controller)

基于 ESP32、四路低压 LED 与可选 BH1750 的本地智能照明教学原型，演示四路手动控制、倒计时与环境亮度触发的四路联动自动逻辑。

- **技术栈：** ESP32 · Arduino · PlatformIO · ESPAsyncWebServer · BH1750 · 低压 LED · 可选本地 HTTP
- **构建证据：** [`b6cee2eb66cc`](https://github.com/rongyishuaige7/esp32-smart-light-controller/commit/b6cee2eb66cc925ee1f17601cc4801252b2b1327) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-light-controller/actions/runs/29658141674)
- **项目资料：** 固件、BOM 与接线说明

### [基于ESP32的智能化妆品收纳与环境管理系统](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet)

基于 ESP32、DHT11、GUVA-S12SD、PIR、RC522 与 Flutter 的智能化妆品收纳与环境管理教学原型；公开默认不提供 Wi-Fi/HTTP 或实体输出。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · DHT11 · GUVA-S12SD · PIR · RC522 · SSD1306 · WS2812B · 可选本地 HTTP
- **构建证据：** [`d8358b403ae2`](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet/commit/d8358b403ae2b35eabf964c2ca0dd0f0c7119fd8) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet/actions/runs/29658142813)
- **项目资料：** 项目照片与界面截图

### [基于ESP32-C3的多传感器健康数据展示手环原型](https://github.com/rongyishuaige7/esp32-c3-smart-band)

基于 ESP32-C3、MAX30102、MPU6050、DS18B20、GPS、OLED 与 Flutter BLE 客户端的多传感器数据展示教学原型。

- **技术栈：** ESP32-C3 · Arduino · PlatformIO · NimBLE · Flutter · MAX30102 · MPU6050 · DS18B20 · GPS · SSD1306
- **构建证据：** [`d22e75c11d01`](https://github.com/rongyishuaige7/esp32-c3-smart-band/commit/d22e75c11d01272cc983a047180178f9411fff12) · [Actions 成功](https://github.com/rongyishuaige7/esp32-c3-smart-band/actions/runs/29658144412)
- **项目资料：** 项目照片、原理图、PCB 与制造资料

### [基于Arduino的多传感器数据展示与音频联动教学原型](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo)

基于 Arduino Uno、MAX30100、DHT11、DS18B20、BH1750、MPU6050、HC-05、DFPlayer 与 Flutter Android 客户端的多传感器数据展示与音频联动教学原型。

- **技术栈：** Arduino Uno · PlatformIO · Flutter · Android · Classic Bluetooth SPP · HC-05 · MAX30100 · DHT11 · DS18B20 · BH1750 · MPU6050 · DFPlayer Mini
- **构建证据：** [`aa7b5430270c`](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo/commit/aa7b5430270c956982ea0b5cf643697889131982) · [Actions 成功](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo/actions/runs/29658146112)
- **项目资料：** 项目照片

### [基于ESP32-S3和Avalonia的智能农业环境监测系统](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system)

基于 ESP32-S3、DHT11、BH1750、ACD10、BMP280、OLED 与 Avalonia/.NET 8 示例数据界面的环境监测教学原型。

- **技术栈：** ESP32-S3 · Arduino · PlatformIO · Avalonia · .NET 8 · DHT11 · BH1750 · ACD10 · BMP280 · SSD1306
- **构建证据：** [`16dc1b83191b`](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system/commit/16dc1b83191be1b58e9f148c9cd1b3a0583d823a) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system/actions/runs/29658147751)
- **项目资料：** 项目照片、原理图、PCB 与制造资料

### [基于STM32F103的衣柜环境监测与自动通风控制系统](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system)

基于 STM32F103、DHT11、MQ135 原始 ADC、OLED 与默认关闭风扇输出的衣柜环境监测和通风控制教学原型。

- **技术栈：** STM32F103 · C · PlatformIO · STM32Cube · DHT11 · MQ135 · OLED
- **构建证据：** [`96abf5637041`](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system/commit/96abf563704169ecce5e0465fc29ecc4b16bbbb4) · [Actions 成功](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system/actions/runs/29658149071)
- **项目资料：** 项目照片

### [基于树莓派的居家环境与活动状态监测教学原型](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo)

基于树莓派、Flask/MySQL 后端与 Android Compose 查看端的居家环境和活动状态监测教学原型。

- **技术栈：** Raspberry Pi · Python · Flask · Socket.IO · MySQL · Kotlin · Jetpack Compose
- **构建证据：** [`a27b5eaa4c05`](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo/commit/a27b5eaa4c05a3bf0aa7bcf0eb9536f29de2fbb9) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo/actions/runs/29658037876)
- **项目资料：** 项目照片

## 索引维护

[`projects.yml`](projects.yml) 是机器可读索引。CI 会核对公开仓库、默认分支、提交 SHA、固定 Actions 链接与 README 同步。

项目的接线、供电、网络和使用注意事项以各项目 README 为准。
