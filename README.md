# Hardware Lab

我独立完成的软硬件项目作品集，收录源码、项目介绍、构建记录和可公开的项目资料。

> **更新日期：2026-07-19。** 当前收录 22 个公开项目。每个“Actions 成功”链接均对应所列默认分支的最新提交；部分项目提供短期 Actions Artifact。

## 项目

### [基于ESP32-S3的视觉猜拳游戏](https://github.com/rongyishuaige7/ESP32_RPS_Game)

基于摄像头手势识别的剪刀石头布硬件游戏，包含 OLED、音频、RGB 反馈与可选 MJPEG 推流。

- **技术栈：** ESP32-S3 · C++ · PlatformIO · OV3660
- **构建证据：** [`3730095b6dda`](https://github.com/rongyishuaige7/ESP32_RPS_Game/commit/3730095b6ddacd8bf00196251ae8aaa334730fbb) · [Actions 成功](https://github.com/rongyishuaige7/ESP32_RPS_Game/actions/runs/29669939600)
- **项目资料：** 原理图资料

### [基于ESP32-S3的多模态交互桌面智能花盆](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot)

多模态桌面智能花盆原型，覆盖环境感知、双泵灌溉、本地彩屏、局域网控制、语音与手势交互。

- **技术栈：** ESP32-S3 · C++ · PlatformIO · FreeRTOS · EasyEDA
- **构建证据：** [`bf0cbe5b75a9`](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/commit/bf0cbe5b75a9a3568b0e1aec9cc7ce97bc196beb) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/actions/runs/29669976115)
- **项目资料：** 项目照片、PCB 与制造资料

### [基于STM32的多传感器数据采集系统](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition)

多传感器数据采集教学原型，包含 Flash 历史与离线缓存、ESP-01S AT 联网、TCP JSON 工具、OLED 与告警。

- **技术栈：** STM32F103 · C · PlatformIO · STM32Cube HAL · W25Q64 · ESP-01S
- **构建证据：** [`08edc84efa6a`](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/commit/08edc84efa6afbebc2b0d51f57634c16bcdf6c82) · [Actions 成功](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/actions/runs/29670054376)
- **项目资料：** 项目照片

### [基于LoRa和ESP32的仓库物品追踪定位系统](https://github.com/rongyishuaige7/lora-warehouse-tracking-system)

仓库区域追踪教学原型，包含 LoRa 标签/网关固件、Flask/SQLite 服务与 Kotlin Android 客户端。

- **技术栈：** ESP32 · LoRa/SX1278 · C++ · PlatformIO · Flask · SQLite · Kotlin
- **构建证据：** [`31b0cfd7d227`](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/commit/31b0cfd7d2276fef1f69f3a005032fa6f4ba87ee) · [Actions 成功](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/actions/runs/29670049908)
- **项目资料：** 项目照片与原理图资料

### [基于多路ESP32-CAM的车流量自适应交通信号控制系统](https://github.com/rongyishuaige7/adaptive-traffic-signal-system)

四路 ESP32-CAM 车流量自适应交通信号教学原型，包含 YOLOv8 跟踪/过线计数、FastAPI、Vue 3、WebSocket、12 路信号灯和四块 OLED。

- **技术栈：** ESP32-CAM × 4 · ESP32 · YOLOv8 · FastAPI · Vue 3 · WebSocket
- **构建证据：** [`9cc93c3c82e1`](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/commit/9cc93c3c82e12c2e9d69a0800d7c6a1257e8a2f6) · [Actions 成功](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/actions/runs/29669940796)
- **项目资料：** 项目照片、界面截图与 PCB 资料

### [基于ESP32-S3的健康科普语音交互终端](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal)

基于本地唤醒、讯飞流式 ASR/TTS、DeepSeek SSE、双 I²S 音频和 LVGL 显示的健康科普语音终端教学原型。

- **技术栈：** ESP32-S3 · ESP-IDF · ESP-SR · 讯飞 · DeepSeek · LVGL · FreeRTOS
- **构建证据：** [`f64e9a089c56`](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/commit/f64e9a089c5629b58125d97543bf4c7a4444e3f1) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/actions/runs/29669975332)
- **项目资料：** 项目照片

### [基于树莓派和RFID的房卡管理系统](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system)

双 RC522 房卡管理教学原型，包含树莓派 Python 服务、MariaDB、Qt/C++ 管理端、服务端角色权限、房态与审计记录。

- **技术栈：** Raspberry Pi · Python · Qt/C++ · MariaDB · RC522 · SG90
- **构建证据：** [`4016d0d0d25c`](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/commit/4016d0d0d25c41254e1677843c7f05dc59f6ab50) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/actions/runs/29670052065)
- **项目资料：** 项目照片与界面截图

### [基于STM32的触摸与隔空手势控制系统](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system)

使用四路电容触摸和 APDS-9960 隔空手势控制四路 LED，并通过 ESP-01S 本地热点展示状态与诊断的教学原型。

- **技术栈：** STM32F103 · C++ · PlatformIO · STM32Cube HAL · TTP223 · APDS-9960 · ESP-01S
- **构建证据：** [`939edc50d73e`](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system/commit/939edc50d73e2990bab5277a25bc284c4a5e76b9) · [Actions 成功](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system/actions/runs/29670055624)
- **项目资料：** 项目照片与原理图资料

### [基于ESP32的智能闹钟系统](https://github.com/rongyishuaige7/esp32-smart-alarm-clock)

基于 ESP32、OLED、DHT11、PIR、MAX98357A 与 Flutter 局域网客户端的智能闹钟教学原型。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · OLED · DHT11 · PIR · MAX98357A
- **构建证据：** [`e0ddaf58116b`](https://github.com/rongyishuaige7/esp32-smart-alarm-clock/commit/e0ddaf58116b65ba757c33f407d8cc567f3662ca) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-alarm-clock/actions/runs/29669978454)
- **项目资料：** 项目照片、界面截图与原理图资料

### [基于ESP32的智能药盒系统](https://github.com/rongyishuaige7/esp32-smart-pillbox)

基于 ESP32、双 PIR、双 HX711、RGB/蜂鸣器与 Flutter 局域网客户端的智能药盒教学原型。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · PIR · HX711 · SPIFFS · HTTP
- **构建证据：** [`de8efb73bab2`](https://github.com/rongyishuaige7/esp32-smart-pillbox/commit/de8efb73bab2d2166c73d7a7e2ceff6b9e5ce47d) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-pillbox/actions/runs/29670326912)
- **项目资料：** 项目照片与原理图资料

### [基于ESP32的天气时钟](https://github.com/rongyishuaige7/esp32-weather-clock)

基于 ESP32、DHT22、BH1750、DS3231、SSD1306 OLED 与本地 AP 配网的天气时钟教学原型。

- **技术栈：** ESP32 · Arduino · PlatformIO · DHT22 · BH1750 · DS3231 · SSD1306 · Wi-Fi
- **构建证据：** [`ff0fbc8521fd`](https://github.com/rongyishuaige7/esp32-weather-clock/commit/ff0fbc8521fd9e19763a88c659a49dc4cbc549e1) · [Actions 成功](https://github.com/rongyishuaige7/esp32-weather-clock/actions/runs/29670048579)
- **项目资料：** 项目照片、原理图与 PCB 资料

### [基于ESP32-S3的多传感器智能安全监测系统](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor)

ESP32-S3 多传感器监测教学原型，包含 MQ-2/MQ-5 原始采样、火焰与超声波输入、OLED、本地状态页和低压执行器分时逻辑。

- **技术栈：** ESP32-S3 · ESP-IDF · PlatformIO · FreeRTOS · MQ-2 · MQ-5 · SSD1306 · HC-SR04
- **构建证据：** [`91c959bd5aaa`](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor/commit/91c959bd5aaa170ab8152e9ea2f8cfff380fe08b) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor/actions/runs/29669977716)
- **项目资料：** 原理图、PCB 与制造资料

### [基于树莓派的多传感器小型气象站](https://github.com/rongyishuaige7/raspberry-pi-weather-station)

树莓派采集 DHT22 温湿度与 BH1750 光照，写入 MySQL，经 Flask REST API 供 Avalonia / C# 上位机查看、查询历史和维护阈值的教学原型。

- **技术栈：** Raspberry Pi · Python · Flask · MySQL · C# · Avalonia · DHT22 · BH1750
- **构建证据：** [`975b6d57379b`](https://github.com/rongyishuaige7/raspberry-pi-weather-station/commit/975b6d57379b0622ba944a7108ee79a9de3ad0c8) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-weather-station/actions/runs/29670053262)
- **项目资料：** 界面与日志截图

### [基于ESP32的婴儿状态监测原型](https://github.com/rongyishuaige7/esp32-baby-monitor)

两路距离、温湿度与声音幅度输入驱动 ESP32 中的演示级固定阈值分类、RGB/蜂鸣器本地反馈和可选可信局域网 JSON 接口。

- **技术栈：** ESP32 · Arduino · PlatformIO · HC-SR04 · DHT11 · 模拟声音输入 · WebServer
- **构建证据：** [`bbcac0c86ccd`](https://github.com/rongyishuaige7/esp32-baby-monitor/commit/bbcac0c86ccdeaef1997d4f2633ca6c962f526db) · [Actions 成功](https://github.com/rongyishuaige7/esp32-baby-monitor/actions/runs/29669971693)
- **项目资料：** 项目照片与原理图资料

### [基于ESP32的蜂箱多传感器数据采集与局域网展示原型](https://github.com/rongyishuaige7/esp32-beehive-monitor)

ESP32 读取 DHT11、BH1750、BMP280、模拟声音幅度和 MQ-2 原始 ADC；使用者本地配置后，Flutter 客户端可在可信局域网请求一条本地 JSON 响应。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · DHT11 · BH1750 · BMP280 · 模拟 ADC · 本地 HTTP
- **构建证据：** [`7444d1726686`](https://github.com/rongyishuaige7/esp32-beehive-monitor/commit/7444d17266862ada2c2020ad8013b31d6282a718) · [Actions 成功](https://github.com/rongyishuaige7/esp32-beehive-monitor/actions/runs/29669972717)
- **项目资料：** 项目照片、原理图与 PCB 资料

### [基于ESP32的多路智能照明控制系统](https://github.com/rongyishuaige7/esp32-smart-light-controller)

基于 ESP32、四路低压 LED 与可选 BH1750 的本地智能照明教学原型，演示四路手动控制、倒计时与环境亮度触发的四路联动自动逻辑。

- **技术栈：** ESP32 · Arduino · PlatformIO · ESPAsyncWebServer · BH1750 · 低压 LED · 可选本地 HTTP
- **构建证据：** [`622c1e5ed125`](https://github.com/rongyishuaige7/esp32-smart-light-controller/commit/622c1e5ed1256ff64788673263f5c15955685f69) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-light-controller/actions/runs/29669979237)
- **项目资料：** 固件、BOM 与接线说明

### [基于ESP32的智能化妆品收纳与环境管理系统](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet)

基于 ESP32、DHT11、GUVA-S12SD、PIR、RC522 与 Flutter 的智能化妆品收纳与环境管理教学原型；公开默认不提供 Wi-Fi/HTTP 或实体输出。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · DHT11 · GUVA-S12SD · PIR · RC522 · SSD1306 · WS2812B · 可选本地 HTTP
- **构建证据：** [`f6247c52537b`](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet/commit/f6247c52537b3f4c4ba06e7fa47682923e843bc4) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet/actions/runs/29670325600)
- **项目资料：** 项目照片与界面截图

### [基于ESP32-C3的多传感器健康数据展示手环原型](https://github.com/rongyishuaige7/esp32-c3-smart-band)

基于 ESP32-C3、MAX30102、MPU6050、DS18B20、GPS、OLED 与 Flutter BLE 客户端的多传感器数据展示教学原型。

- **技术栈：** ESP32-C3 · Arduino · PlatformIO · NimBLE · Flutter · MAX30102 · MPU6050 · DS18B20 · GPS · SSD1306
- **构建证据：** [`4c7683f500e4`](https://github.com/rongyishuaige7/esp32-c3-smart-band/commit/4c7683f500e4262ef49f631e7102a0422f291e4c) · [Actions 成功](https://github.com/rongyishuaige7/esp32-c3-smart-band/actions/runs/29669973669)
- **项目资料：** 项目照片、原理图、PCB 与制造资料

### [基于Arduino的多传感器数据展示与音频联动教学原型](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo)

基于 Arduino Uno、MAX30100、DHT11、DS18B20、BH1750、MPU6050、HC-05、DFPlayer 与 Flutter Android 客户端的多传感器数据展示与音频联动教学原型。

- **技术栈：** Arduino Uno · PlatformIO · Flutter · Android · Classic Bluetooth SPP · HC-05 · MAX30100 · DHT11 · DS18B20 · BH1750 · MPU6050 · DFPlayer Mini
- **构建证据：** [`983560336b73`](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo/commit/983560336b7312cdbac5b0569ac140a407712d50) · [Actions 成功](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo/actions/runs/29669942031)
- **项目资料：** 项目照片

### [基于ESP32-S3和Avalonia的智能农业环境监测系统](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system)

基于 ESP32-S3、DHT11、BH1750、ACD10、BMP280、OLED 与 Avalonia/.NET 8 示例数据界面的环境监测教学原型。

- **技术栈：** ESP32-S3 · Arduino · PlatformIO · Avalonia · .NET 8 · DHT11 · BH1750 · ACD10 · BMP280 · SSD1306
- **构建证据：** [`986900de1487`](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system/commit/986900de1487801f6889b4e269215608803a5623) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system/actions/runs/29670303834)
- **项目资料：** 项目照片、原理图、PCB 与制造资料

### [基于STM32F103的衣柜环境监测与自动通风控制系统](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system)

基于 STM32F103、DHT11、MQ135 原始 ADC、OLED 与默认关闭风扇输出的衣柜环境监测和通风控制教学原型。

- **技术栈：** STM32F103 · C · PlatformIO · STM32Cube · DHT11 · MQ135 · OLED
- **构建证据：** [`5ebccbd8d879`](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system/commit/5ebccbd8d879ee82576c7e9937539a50283b9af9) · [Actions 成功](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system/actions/runs/29670057922)
- **项目资料：** 项目照片

### [基于树莓派的居家环境与活动状态监测教学原型](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo)

基于树莓派、Flask/MySQL 后端与 Android Compose 查看端的居家环境和活动状态监测教学原型。

- **技术栈：** Raspberry Pi · Python · Flask · Socket.IO · MySQL · Kotlin · Jetpack Compose
- **构建证据：** [`d2991515dd86`](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo/commit/d2991515dd86e63fa69cec0c17fd9023ed341523) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo/actions/runs/29670051197)
- **项目资料：** 项目照片

## 索引维护

[`projects.yml`](projects.yml) 是机器可读索引。CI 会核对公开仓库、默认分支、提交 SHA、固定 Actions 链接与 README 同步。

项目的接线、供电、网络和使用注意事项以各项目 README 为准。
