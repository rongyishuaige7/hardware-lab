# Hardware Lab

我独立完成的软硬件原型索引，展示项目源码、可复现构建、公开资料和实际使用注意事项。

> **更新日期：2026-07-19。** 当前收录 22 个公开项目。每个固定 Actions 链接都对应所列默认分支 HEAD；若项目上传 Actions Artifact，则保留 14 天；部分项目不上传构建产物，以项目条目为准。

## 命名规范

索引名称统一采用毕业设计常见的表述：**“基于{核心平台/技术}的{功能对象}”**。其中“系统”“终端”“游戏”“花盆”等后缀按原型实际形态保留；名称只说明技术范围与功能主题。仓库 URL、构建证据和公开资料会随项目更新同步维护。

## 项目

### [基于ESP32-S3的视觉猜拳游戏](https://github.com/rongyishuaige7/ESP32_RPS_Game)

基于摄像头手势识别的剪刀石头布硬件游戏，包含 OLED、音频、RGB 反馈与可选 MJPEG 推流。

- **平台：** ESP32-S3 · C++ · PlatformIO · OV3660
- **构建证据：** [`2a403fceabe9`](https://github.com/rongyishuaige7/ESP32_RPS_Game/commit/2a403fceabe998a7481da2ee4ae556c663d590ed) · [Actions 成功](https://github.com/rongyishuaige7/ESP32_RPS_Game/actions/runs/29658176252)
- **公开范围：** 公开一份已移除 PDF 元数据的历史原理图导出；未公开实物照片或演示视频。
- **边界：** CI 只证明固定配置下的固件构建和 Artifact 上传。 板型、引脚或摄像头配置变化后仍需重新烧录并核对实物。 Actions Artifact 会按 14 天保留策略过期，不是永久下载。

### [基于ESP32-S3的多模态交互桌面智能花盆](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot)

多模态桌面智能花盆原型，覆盖环境感知、双泵灌溉、本地彩屏、局域网控制、语音与手势交互。

- **平台：** ESP32-S3 · C++ · PlatformIO · FreeRTOS · EasyEDA
- **构建证据：** [`3436184ea476`](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/commit/3436184ea4763dc6541dd8ef4cd3e14a1cc3066e) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/actions/runs/29658003504)
- **公开范围：** 公开两张去除 EXIF/GPS 的历史实物照片，以及原理图 PDF、EasyEDA PCB JSON、BOM 和 Gerber/钻孔文件；没有演示视频，App 源码未找回。
- **边界：** 项目照片展示拍摄时的原型外观。EDA 的 JSN-SR04T 引脚与公开固件不一致。 EDA 控制器标注与当前 PlatformIO 4 MB Flash 配置存在版本边界。 局域网 HTTP 控制无认证和加密，不应直接暴露公网。

### [基于STM32的多传感器数据采集系统](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition)

多传感器数据采集教学原型，包含 Flash 历史与离线缓存、ESP-01S AT 联网、TCP JSON 工具、OLED 与告警。

- **平台：** STM32F103 · C · PlatformIO · STM32Cube HAL · W25Q64 · ESP-01S
- **构建证据：** [`f4513869538c`](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/commit/f4513869538c8a55a9b39479c0c219753ab7bd75) · [Actions 成功](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/actions/runs/29658004607)
- **公开范围：** 公开两张已去除 EXIF/GPS 并缩放的 2026-05-02 历史原型照片；未公开演示视频或 EDA/制造文件。
- **边界：** ESP-01S=USART1、调试串口=USART2 是源码级裁决，仍需实物确认。 E3Z-LS63、A1104、FSR402 和蜂鸣器接口仍有待实物确认的电气边界。 TCP 仅面向可信局域网，无认证和 TLS。 Actions Artifact 会按 14 天保留策略过期，不是永久下载。

### [基于LoRa和ESP32的仓库物品追踪定位系统](https://github.com/rongyishuaige7/lora-warehouse-tracking-system)

仓库区域追踪教学原型，包含 LoRa 标签/网关固件、Flask/SQLite 服务与 Kotlin Android 客户端。

- **平台：** ESP32 · LoRa/SX1278 · C++ · PlatformIO · Flask · SQLite · Kotlin
- **构建证据：** [`8bc1b566a566`](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/commit/8bc1b566a566963a8538535b3e13d0f32d30b566) · [Actions 成功](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/actions/runs/29658005560)
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放的 2026-04-08 历史原型照片，以及一份已移除 PDF 元数据的两页历史原理图；未公开演示视频。
- **边界：** QUERY 只能请求清醒标签立即上报，不能唤醒当前深睡实现。 定位只确认向网关下发命令，不确认标签收到或 JQ6500 实际播放。 API、网关控制 HTTP 和 LoRa 均无认证或加密，只面向隔离可信局域网教学环境。 电池采样未实现，DHT 失败与不可用数据使用 null/N/A；Actions Artifact 仅保留 14 天。

### [基于多路ESP32-CAM的车流量自适应交通信号控制系统](https://github.com/rongyishuaige7/adaptive-traffic-signal-system)

四路 ESP32-CAM 车流量自适应交通信号教学原型，包含 YOLOv8 跟踪/过线计数、FastAPI、Vue 3、WebSocket、12 路信号灯和四块 OLED。

- **平台：** ESP32-CAM × 4 · ESP32 · YOLOv8 · FastAPI · Vue 3 · WebSocket
- **构建证据：** [`61e839e16481`](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/commit/61e839e164812b395f289788a3abf214688256ef) · [Actions 成功](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/actions/runs/29658006499)
- **公开范围：** 公开 2026-05-14 的历史桌面模型照片和仪表盘截图，以及已脱敏的历史原理图、PCB 预览、UTF-8 BOM CSV 和解包后的 Gerber/Drill；未上传原 Gerber ZIP。
- **边界：** 模拟器与构建证据不证明车辆检测准确率、物理灯态或道路安全。 HTTP、MJPEG 与 WebSocket 无认证或 TLS，仅限隔离可信局域网教学环境。 设备 WebSocket 客户数不是设备身份、命令 ACK 或物理灯态反馈。 不能用于真实道路信号控制；Actions Artifact 仅保留 14 天。

### [基于ESP32-S3的健康科普语音交互终端](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal)

基于本地唤醒、讯飞流式 ASR/TTS、DeepSeek SSE、双 I²S 音频和 LVGL 显示的健康科普语音终端教学原型。

- **平台：** ESP32-S3 · ESP-IDF · ESP-SR · 讯飞 · DeepSeek · LVGL · FreeRTOS
- **构建证据：** [`0b7a24659826`](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/commit/0b7a246598265480f0da6912bb89f285b6aa7230) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/actions/runs/29658129899)
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放的 2026-04-26 历史终端原型照片；未公开演示视频或 EDA/制造文件。
- **边界：** CI 使用空凭据；构建和源码契约不证明真实讯飞或 DeepSeek 在线调用。 不证明 ASR/TTS、首包延迟、语音质量、内容安全或硬件行为。 这不是医疗器械、诊断、处方或急救系统，不能把关键词场景检查写成医学准确率或临床安全证据。 真实服务商凭据彼此独立且会编译进本地固件；Actions Artifact 仅保留 14 天。

### [基于树莓派和RFID的房卡管理系统](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system)

双 RC522 房卡管理教学原型，包含树莓派 Python 服务、MariaDB、Qt/C++ 管理端、服务端角色权限、房态与审计记录。

- **平台：** Raspberry Pi · Python · Qt/C++ · MariaDB · RC522 · SG90
- **构建证据：** [`79e9511ddd31`](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/commit/79e9511ddd3115f908302f6ce963606e52c6e6d4) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/actions/runs/29658008602)
- **公开范围：** 保留四张已去元数据并遮盖私网 IP/UID 的 2026-04-03 历史界面截图，本批新增一张已去除 EXIF/GPS 并缩放的 2026-04-08 历史实物照片；本批其余 13 张旧截图和误投原理图未上传。
- **边界：** 历史界面截图不绑定当前公开提交，也不证明当前硬件已复测。 自定义 TCP 无 TLS 或重放保护，RC522 UID 可复制，只面向隔离可信局域网教学环境。 SG90 没有位置或门锁状态反馈，202 响应只表示 PWM 任务已下发。 当前 Raspberry Pi 型号、两块 RC522、舵机供电及可选 OLED 等仍需按实物确认；Actions Artifact 仅保留 14 天。

### [基于STM32的触摸与隔空手势控制系统](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system)

使用四路电容触摸和 APDS-9960 隔空手势控制四路 LED，并通过 ESP-01S 本地热点展示状态与诊断的教学原型。

- **平台：** STM32F103 · C++ · PlatformIO · STM32Cube HAL · TTP223 · APDS-9960 · ESP-01S
- **构建证据：** [`a4373083d9da`](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system/commit/a4373083d9da4a99b58389d9c2fae7d6544e41e8) · [Actions 成功](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system/actions/runs/29658131455)
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放的 2026-04-02 历史原型照片，以及一份已移除 PDF 元数据的历史原理图；未公开演示视频。
- **边界：** 构建和源码契约不证明触摸可靠性、APDS 识别率、ESP AT 兼容性或实际 LED 行为。 HTTP 无认证和 TLS，只面向隔离可信的教学热点。 GPIO 不得直接驱动继电器、灯带、电机或市电负载。 Actions Artifact 会按 14 天保留策略过期，不是永久下载。

### [基于ESP32的智能闹钟系统](https://github.com/rongyishuaige7/esp32-smart-alarm-clock)

基于 ESP32、OLED、DHT11、PIR、MAX98357A 与 Flutter 局域网客户端的智能闹钟教学原型。

- **平台：** ESP32 · Arduino · PlatformIO · Flutter · OLED · DHT11 · PIR · MAX98357A
- **构建证据：** [`599a1b88e8bc`](https://github.com/rongyishuaige7/esp32-smart-alarm-clock/commit/599a1b88e8bc1e7d2297bc81ace7dfc7a5ae7d8f) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-alarm-clock/actions/runs/29658133396)
- **公开范围：** 公开一张已去除元数据并遮盖私网 URL 的 2026-04-06 历史原型/App 照片，以及已脱敏的历史原理图和 UTF-8 BOM CSV；未分发原始 WAV。
- **边界：** AP 配网和 STA REST 都不是安全网络服务；HTTP 无认证和 TLS，只面向隔离可信局域网。 当前未分发 WAV；没有使用者自备的合法音频时，声音功能不会完成。 构建与源码契约不证明 NTP、传感器、OLED、I²S、按钮、Wi-Fi 或 App 端到端行为。 Actions Artifact 仅保留 14 天。

### [基于ESP32的智能药盒系统](https://github.com/rongyishuaige7/esp32-smart-pillbox)

基于 ESP32、双 PIR、双 HX711、RGB/蜂鸣器与 Flutter 局域网客户端的智能药盒教学原型。

- **平台：** ESP32 · Arduino · PlatformIO · Flutter · PIR · HX711 · SPIFFS · HTTP
- **构建证据：** [`880cf190e17d`](https://github.com/rongyishuaige7/esp32-smart-pillbox/commit/880cf190e17ddd57ffc9e9c8220bffa03ff1f9d2) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-pillbox/actions/runs/29658011421)
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放的 2026-04-08 历史原型照片，以及一份已移除 PDF 元数据的历史原理图；未公开演示视频或制造文件。
- **边界：** 原型状态机不构成服药确认、诊断、护理、医疗结论或紧急处置。 AP 配网和 STA REST 均使用无认证、无 TLS 的本地 HTTP，只限隔离可信局域网。 构建和源码契约不证明 PIR、HX711、RGB、蜂鸣器、SPIFFS、Wi-Fi、NTP 或 App 端到端行为。 Actions Artifact 会按 14 天保留策略过期，不是永久下载。

### [基于ESP32的天气时钟](https://github.com/rongyishuaige7/esp32-weather-clock)

基于 ESP32、DHT22、BH1750、DS3231、SSD1306 OLED 与本地 AP 配网的天气时钟教学原型。

- **平台：** ESP32 · Arduino · PlatformIO · DHT22 · BH1750 · DS3231 · SSD1306 · Wi-Fi
- **构建证据：** [`f8d6668774cf`](https://github.com/rongyishuaige7/esp32-weather-clock/commit/f8d6668774cf81e82c7409065f73b2daa73197fd) · [Actions 成功](https://github.com/rongyishuaige7/esp32-weather-clock/actions/runs/29658012825)
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放的 2026-03-28 历史原型照片，以及已脱敏的历史原理图、PCB 预览和 UTF-8 BOM CSV；未公开 Gerber 或演示视频。
- **边界：** AP 配网、/scan 和 /save 是无认证、无 TLS 的本地 HTTP；开放 AP 只限隔离可信环境。 EEPROM 保存 Wi-Fi 和天气 API 凭据，不是安全存储；天气请求当前使用 setInsecure()，不校验证书。 固件构建不证明传感器读数、OLED、RTC、Wi-Fi、NTP、天气数据、配置保存或长期稳定性。 Flash 构建占用为 79.1%；Actions Artifact 仅保留 14 天。

### [基于ESP32-S3的多传感器智能安全监测系统](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor)

ESP32-S3 多传感器监测教学原型，包含 MQ-2/MQ-5 原始采样、火焰与超声波输入、OLED、本地状态页和低压执行器分时逻辑。

- **平台：** ESP32-S3 · ESP-IDF · PlatformIO · FreeRTOS · MQ-2 · MQ-5 · SSD1306 · HC-SR04
- **构建证据：** [`c0764e822928`](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor/commit/c0764e822928c8bd0f6d44ebcd478caf8c13dbc9) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor/actions/runs/29658135574)
- **公开范围：** 公开已脱敏的历史原理图、PCB 预览、UTF-8 BOM CSV 和解包后的 Gerber/Drill；未上传原 Gerber ZIP。EDA 仅显示 GPIO9 一路 SG90，而当前源码定义 GPIO9/GPIO10 两路，故不能作为当前接线权威。
- **边界：** 历史 EDA 仅显示 GPIO9 一路 SG90，而当前源码定义 GPIO9/GPIO10 两路；EDA 不完整，不能作为当前接线权威。 固定热点密码不公开；本地启用 SoftAP/SSE 无认证、无 TLS，仅限隔离可信测试网络。 构建和源码契约不证明传感器准确、硬件动作或任何安全效果。 不能用于火灾/燃气报警、自动灭火、通风安全、生命安全或生产控制。 Flash 构建占用 82.3%，属于后续扩展边界；Actions Artifact 仅保留 14 天。

### [基于树莓派的多传感器小型气象站](https://github.com/rongyishuaige7/raspberry-pi-weather-station)

树莓派采集 DHT22 温湿度与 BH1750 光照，写入 MySQL，经 Flask REST API 供 Avalonia / C# 上位机查看、查询历史和维护阈值的教学原型。

- **平台：** Raspberry Pi · Python · Flask · MySQL · C# · Avalonia · DHT22 · BH1750
- **构建证据：** [`1e836128d79c`](https://github.com/rongyishuaige7/raspberry-pi-weather-station/commit/1e836128d79c0059daf0a4351740c21195abd441) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-weather-station/actions/runs/29658136769)
- **公开范围：** 公开三张已去元数据并按需遮盖终端用户名、路径和私网地址的 2026-04-07 历史界面/日志截图；未公开实物照片、演示视频或 EDA/制造文件。
- **边界：** CI 的 USE_MOCK_SENSORS=1 只生成随机模拟数据，不代表真实传感器、当前天气、设备在线或环境状态。 API /api/health 只说明 API 进程响应；devices.status 是人工维护字段；查询到最新记录不代表实时采样或采集器运行。 HTTP、Bearer JWT 与 MySQL 只适合隔离可信教学网络；没有 TLS、设备身份、细粒度权限、速率限制或生产级密钥管理。 本项目不是气象仪器、环境安全、消防/报警、医疗、生产控制或远程运维系统；构建与 mock 联调不能作为测量准确性、告警送达或安全效果证据。 Actions Artifact 会按 14 天保留策略过期，不是永久下载。

### [基于ESP32的婴儿状态监测原型](https://github.com/rongyishuaige7/esp32-baby-monitor)

两路距离、温湿度与声音幅度输入驱动 ESP32 中的演示级固定阈值分类、RGB/蜂鸣器本地反馈和可选可信局域网 JSON 接口。

- **平台：** ESP32 · Arduino · PlatformIO · HC-SR04 · DHT11 · 模拟声音输入 · WebServer
- **构建证据：** [`9936a30c19f8`](https://github.com/rongyishuaige7/esp32-baby-monitor/commit/9936a30c19f8f78988182a0ad017fa61c94ef659) · [Actions 成功](https://github.com/rongyishuaige7/esp32-baby-monitor/actions/runs/29658138692)
- **公开范围：** 公开两张已去除 EXIF/GPS 并缩放的 2026-04-08 历史原型照片，以及一份已移除 PDF 元数据的历史原理图；原理图不消除 HC-SR04 5 V ECHO 电平风险。
- **边界：** 两路距离组合不是人体、婴儿、姿态、睡姿或趴睡识别；声音幅度不是哭声识别，温湿度固定阈值不是安全、儿科或医疗标准。 reference、attention、high_threshold 和 unknown 只是本地演示级分类；LED、蜂鸣器、HTTP、CI 和 Artifact 不代表安全、医疗、告警送达、有人看护或设备在线。 HC-SR04 ECHO 常见为 5 V，必须经过正确的分压或电平转换后才可接入 ESP32；按钮外部上拉/下拉、RGB/蜂鸣器极性与驱动均待实物确认。 HTTP 无 TLS、认证、访问控制、审计或设备身份校验，只能用于隔离可信教学局域网；本项目不得用于婴儿看护、医疗、睡眠安全、紧急响应或生命安全场景。 Actions Artifact 会按 14 天保留策略过期，不是永久下载。

### [基于ESP32的蜂箱多传感器数据采集与局域网展示原型](https://github.com/rongyishuaige7/esp32-beehive-monitor)

ESP32 读取 DHT11、BH1750、BMP280、模拟声音幅度和 MQ-2 原始 ADC；使用者本地配置后，Flutter 客户端可在可信局域网请求一条本地 JSON 响应。

- **平台：** ESP32 · Arduino · PlatformIO · Flutter · DHT11 · BH1750 · BMP280 · 模拟 ADC · 本地 HTTP
- **构建证据：** [`4642d27154e7`](https://github.com/rongyishuaige7/esp32-beehive-monitor/commit/4642d27154e751d055b05aa9500d3232ff9a7444) · [Actions 成功](https://github.com/rongyishuaige7/esp32-beehive-monitor/actions/runs/29658140085)
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放但拍摄日期未知的历史原型照片，以及已脱敏的历史原理图、PCB 预览和 UTF-8 BOM CSV；未公开 Gerber 或演示视频。
- **边界：** MQ-2 原始 ADC 不代表烟雾、燃气、火灾或安全检测；声音幅度不代表蜂群健康或行为诊断；气压趋势不是天气预报。 HTTP 无认证和 TLS，仅限隔离可信局域网教学环境；项目不提供公网部署方案。 CI、Artifact 和构建不代表设备在线、传感器准确、蜂群状态、蜂箱安全、告警送达或有人处理。 本项目不是养蜂生产、动物健康、气象预报、烟雾/燃气/火灾报警、环境安全、应急响应或无人值守系统。 Actions Artifact 会按 14 天保留策略过期，不是永久下载。

### [基于ESP32的多路智能照明控制系统](https://github.com/rongyishuaige7/esp32-smart-light-controller)

基于 ESP32、四路低压 LED 与可选 BH1750 的本地智能照明教学原型，演示四路手动控制、倒计时与环境亮度触发的四路联动自动逻辑。

- **平台：** ESP32 · Arduino · PlatformIO · ESPAsyncWebServer · BH1750 · 低压 LED · 可选本地 HTTP
- **构建证据：** [`b6cee2eb66cc`](https://github.com/rongyishuaige7/esp32-smart-light-controller/commit/b6cee2eb66cc925ee1f17601cc4801252b2b1327) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-light-controller/actions/runs/29658141674)
- **公开范围：** 当前未公开实物照片、演示视频、原理图、PCB、Gerber 或制造文件；已公开固件、BOM、源码推导接线边界图、协议、来源、状态与验证说明。
- **边界：** 默认公开固件无 Wi-Fi 凭据，不创建接入点、不连接 Wi-Fi 且不启动 HTTP；仅本机忽略的凭据文件成功连接可信局域网后才提供明文、无认证的 HTTP。 四路 GPIO 只适用于经确认的低压 LED 逻辑/驱动，不能替代功率或电气安全设计；实际极性、限流、驱动、电流、供电和共地仍待实物确认。 构建、CI 和 HTTP 响应不代表实体 LED 已动作、设备在线、照度准确、控制必达或长期稳定。 本项目不适用于市电、继电器、公共/应急照明、安防、消防、医疗、生产控制或无人值守场景。 Actions Artifact 会按 14 天保留策略过期，不是永久下载。

### [基于ESP32的智能化妆品收纳与环境管理系统](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet)

基于 ESP32、DHT11、GUVA-S12SD、PIR、RC522 与 Flutter 的智能化妆品收纳与环境管理教学原型；公开默认不提供 Wi-Fi/HTTP 或实体输出。

- **平台：** ESP32 · Arduino · PlatformIO · Flutter · DHT11 · GUVA-S12SD · PIR · RC522 · SSD1306 · WS2812B · 可选本地 HTTP
- **构建证据：** [`d8358b403ae2`](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet/commit/d8358b403ae2b35eabf964c2ca0dd0f0c7119fd8) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet/actions/runs/29658142813) · CI 不上传构建产物。
- **公开范围：** 公开一张历史原型照片和三张历史界面截图，均为 2026-04-08 且已去除 EXIF/GPS 并缩放；未公开演示视频或 EDA/制造文件。
- **边界：** 默认公开源码不提供 Wi-Fi 凭据，不启动 Wi-Fi/HTTP；物理输出仅在本机两个实验开关均精确设为 1 时才进入对应路径，不能据此推断真实负载关闭或电气安全。 RFID UID 可复制且不是认证凭据；公开 HTTP 不回显 UID，刷卡不会自动命令插销。 CI 不上传构建产物。固定 Actions run 只证明公开范围扫描、仓库检查、源码契约和固定构建；不证明真机、网络、传感器、实体执行器、机械位置或电气安全。 本项目不是化妆品/皮肤/UV/健康判断、门禁/电子锁/防盗/认证、远程控制、安全或生产系统。

### [基于ESP32-C3的多传感器健康数据展示手环原型](https://github.com/rongyishuaige7/esp32-c3-smart-band)

基于 ESP32-C3、MAX30102、MPU6050、DS18B20、GPS、OLED 与 Flutter BLE 客户端的多传感器数据展示教学原型。

- **平台：** ESP32-C3 · Arduino · PlatformIO · NimBLE · Flutter · MAX30102 · MPU6050 · DS18B20 · GPS · SSD1306
- **构建证据：** [`d22e75c11d01`](https://github.com/rongyishuaige7/esp32-c3-smart-band/commit/d22e75c11d01272cc983a047180178f9411fff12) · [Actions 成功](https://github.com/rongyishuaige7/esp32-c3-smart-band/actions/runs/29658144412) · CI 不上传构建产物。
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放的 2026-04-29 历史原型照片，以及已脱敏的历史原理图、PCB 预览、UTF-8 BOM CSV 和解包后的 Gerber/Drill；未上传原 Gerber ZIP。
- **边界：** MAX30102 光学脉搏/血氧仅为未校准教学估算，DS18B20 仅表示温度模块读数，MPU6050 阈值事件不是跌倒检测；本项目不是医疗、健康监护、诊断、告警或消费级可穿戴产品。 GPS 坐标不向 App 传输或展示，但这不代表 GPS 模块不接收位置或没有位置隐私风险；不得用于人员、宠物、车辆或资产追踪。 BLE 服务 UUID 与广播名不是设备身份；公开代码没有 pairing、bonding、MITM、防重放、加密、认证或授权，通知不承诺可靠送达。 CI 不上传构建产物。固定 Actions run 只证明公开范围门禁和隔离构建，不证明烧录、传感器、OLED、GPS、BLE、Android、电池、马达、佩戴或电气安全。

### [基于Arduino的多传感器数据展示与音频联动教学原型](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo)

基于 Arduino Uno、MAX30100、DHT11、DS18B20、BH1750、MPU6050、HC-05、DFPlayer 与 Flutter Android 客户端的多传感器数据展示与音频联动教学原型。

- **平台：** Arduino Uno · PlatformIO · Flutter · Android · Classic Bluetooth SPP · HC-05 · MAX30100 · DHT11 · DS18B20 · BH1750 · MPU6050 · DFPlayer Mini
- **构建证据：** [`aa7b5430270c`](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo/commit/aa7b5430270c956982ea0b5cf643697889131982) · [Actions 成功](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo/actions/runs/29658146112) · CI 不上传构建产物。
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放的历史硬件照片，拍摄日期未知；误投到本项目的 RFID 原理图未上传。
- **边界：** 公开默认关闭模拟数据和 DFPlayer 音频；I2C、传感器、HC-05、蜂鸣器与状态 LED 仍可能初始化或产生 I/O，不代表无外设 I/O、外设断电、负载关闭或电气安全。 HC-05 文本协议没有应用层身份认证、授权、端到端加密、MITM 防护、防重放或可靠送达保证；公开远程控制仅保留尽力而为的 CMD:STOP，不代表对端已收到或已停止。 MAX30100、DS18B20、DHT11、BH1750、MPU6050、DFPlayer 音频与规则标签仅为教学路径，不构成人体体温、心率、血氧、睡眠、健康、治疗、姿态、跌倒、安全或紧急结论。 CI 不上传构建产物。固定 Actions run 只证明公开范围门禁和隔离构建，不证明烧录、传感器、HC-05、DFPlayer、音频、Android、接线、供电或电气安全。 本项目不适用于医疗器械、健康监护、睡眠监测、助眠治疗、跌倒/翻身识别、紧急告警、安全看护、消费级产品或生产系统。

### [基于ESP32-S3和Avalonia的智能农业环境监测系统](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system)

基于 ESP32-S3、DHT11、BH1750、ACD10、BMP280、OLED 与 Avalonia/.NET 8 示例数据界面的环境监测教学原型。

- **平台：** ESP32-S3 · Arduino · PlatformIO · Avalonia · .NET 8 · DHT11 · BH1750 · ACD10 · BMP280 · SSD1306
- **构建证据：** [`16dc1b83191b`](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system/commit/16dc1b83191be1b58e9f148c9cd1b3a0583d823a) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system/actions/runs/29658147751) · CI 不上传构建产物。
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放的 2026-03-24 历史原型照片，以及已脱敏的历史原理图、PCB 预览、UTF-8 BOM CSV 和解包后的 Gerber/Drill；未上传原 Gerber ZIP。
- **边界：** 默认公开固件不连接 Wi-Fi/TCP，GPIO5、GPIO6、GPIO38 为输入；传感器和 OLED 仍可能初始化，不代表无外设 I/O、外部负载物理关闭或电气安全。 网络和执行器仅为显式 compile-time opt-in；无设备身份、TLS、认证、授权、ACK、可靠投递或远程控制。 CI 不上传构建产物。固定 Actions run 只证明公开范围门禁和隔离构建，不证明烧录、传感器、OLED、网络、桌面界面、执行器、电气安全或真实环境效果。 本项目不是农业自动化、可靠告警、作物/空气质量/安全结论、远程控制、无人值守、生产或工业系统。



### [基于STM32F103的衣柜环境监测与自动通风控制系统](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system)

基于 STM32F103、DHT11、MQ135 原始 ADC、OLED 与默认关闭风扇输出的衣柜环境监测和通风控制教学原型。

- **平台：** STM32F103 · C · PlatformIO · STM32Cube · DHT11 · MQ135 · OLED
- **构建证据：** [`96abf5637041`](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system/commit/96abf563704169ecce5e0465fc29ecc4b16bbbb4) · [Actions 成功](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system/actions/runs/29658149071) · CI 不上传构建产物。
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放的 2026-05-25 历史衣柜监测原型照片；未公开演示视频或 EDA/制造文件。
- **边界：** CI 不上传构建产物。 MQ 原始 ADC 与 demo_index 不是空气质量、甲醛、CO₂、烟雾、污染物或气体浓度；控制阈值不是健康、安全或环境标准。 默认不把 PB0/PB1 配置为输出，也不执行历史启动风扇测试；PB0/PB1 不得直接驱动电机，MQ 模块模拟输出必须先核对并调理至 STM32 3.3 V ADC 安全范围。 构建和 CI 不证明烧录、传感器读数、OLED、串口、风扇动作、接线、电气安全或长期稳定；本项目不是空气质量仪、家电、量产设计、无人值守或生产系统。

### [基于树莓派的居家环境与活动状态监测教学原型](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo)

基于树莓派、Flask/MySQL 后端与 Android Compose 查看端的居家环境和活动状态监测教学原型。

- **平台：** Raspberry Pi · Python · Flask · Socket.IO · MySQL · Kotlin · Jetpack Compose
- **构建证据：** [`a27b5eaa4c05`](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo/commit/a27b5eaa4c05a3bf0aa7bcf0eb9536f29de2fbb9) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo/actions/runs/29658037876) · CI 不上传构建产物。
- **公开范围：** 公开一张已去除 EXIF/GPS 并缩放的 2026-03-17 历史教学原型照片；本批四张旧界面截图未上传，未公开 APK、演示视频或 EDA/制造文件。
- **边界：** CI 不上传构建产物。 MQ-7 数字 GPIO 只表示未标定教学阈值事件，不是 CO 浓度、燃气泄漏或安全报警；MPU6050 阈值不能可靠判断人员跌倒；图片路径不是身份认证。 继电器、蜂鸣器和摄像头默认关闭；HTTP/Socket.IO 共享 Token 仅适合隔离实验网络，不替代 TLS、账号、密钥轮换或可靠告警。 构建和 CI 不证明实体传感器、执行器、摄像头、MySQL 部署、通知送达、电气安全或长期稳定；本项目不是医疗、养老看护、燃气报警、生命安全、门禁认证、消费产品或生产系统。


## 索引维护

[`projects.yml`](projects.yml) 是机器可读索引，采用 JSON 兼容的 YAML 1.2 语法。CI 会核对：

- 仓库仍为 Public，默认分支仍为 `main`；
- 索引 SHA 等于远程默认分支 HEAD；
- 固定 Actions run 已成功并对应同一 HEAD；
- README 中的仓库、Actions 和短 SHA 与索引同步。
- 构建证据与 CI 构建产物范围（上传或不上传）保持同步。

本索引不展示手填 Star 数、访客计数、虚假在线状态或安装按钮。项目变更后，应先更新构建证据和公开资料。
