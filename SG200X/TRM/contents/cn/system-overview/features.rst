特性介绍
--------

处理器内核
~~~~~~~~~~

- 主处理器 RISCV C906 @ 1.0Ghz

  - 32KB I-cache, 64KB D-Cache

  - 集成矢量(Vector)及浮点运算单元 (FPU)

- 主处理器 ARM Cortex-A53 @ 1.0Ghz

  - 32KB I-cache, 32KB D-Cache

  - 128KB L2 cache

  - 支持 Neon 以及浮点运算 FPU

- 协处理器 RISCV C906 @ 700Mhz

  - 集成浮点运算单元 (FPU)

TPU
~~~

- 内建 TPU , 算力达到 ~1.0TOPS INT8。

- 支持主流的神经网络架构: Caffe，Pytorch，TensorFlow(Lite)，ONNX 和 MXNet。

- 可实现行人侦测 (Pedestrian Detection) , 人脸侦测 (Face Detection), 人脸识别 (Face recognition) , 活体侦测 (Face anti-spoofing) 及其他视频结构化应用。

视频编解码
~~~~~~~~~~

- H.264 Baseline/Main/High profile

- H.265 Main profile

- H.264/H.265 均支援 I 帧及 P 帧

- MJPEG/JPEG baseline

- H.264编解码最大分辨率 : 2880x1620 (5M)

- H.265 编码最大分辨率 : 2880x1620 (5M)

- H.264 编解码性能

  - 2880x1620@30fps + 720x576@30fps

  - 1920x1080@30fps 编码 + 1920x1080@30fps 解码

- H.265 编码性能

  - 2880x1620@30fps + 720x576@30fps

- JPEG 最大编解码性能

  - 2880x1620@30fps

- 支持 CBR/VBR/FIXQP 等多种码率控制模式.

- 支持感兴趣区域 (ROI) 编码

视频接口
~~~~~~~~

- 输入

  - 支持同时两路视频输入 (mipi 2L + 1L)

  - 支持 MIPI, Sub-LVDS, HiSPI 等串行接口

  - 支持 8/10/12 bit RGB Bayer 视频输入

  - 支持 BT.656

  - 支持 AHD 多路混合 BT 格式

  - 支持 SONY, OnSemi, OmniVision 等高清 CMOS sensor

  - 提供可编程频率输出供 sensor 作为参考时钟

  - 支持最大宽度为 2880 , 最大分辨率 5M (2688x1944, 2880x1620)

- 输出

  - 支持多种串行与并行屏显规格

  - 支持 MIPI 等串行接口

  - 支持 BT656, BT601 (8bit), BT1120, 8080 等并行接口

  - 支持 SPI 输出接口

ISP 与图像处理
~~~~~~~~~~~~~~

- 图像视频 90 度、180 度、270 度旋转

- 图像视频 Mirror、Flip功能

- 视频 2 层 OSD 叠加

- 视频 1/32 ~ 32x 缩放功能

- 3A（AE/AWB/AF）算法

- 固定模式噪声消除、坏点校正

- 镜头阴影校正、镜头畸变校正、紫边校正

- 方向自适应 demosaic

- Gamma 校正、(区域/全域)动态对比度增强、颜色管理和增强

- 区域自适应去雾

- Bayer 降噪、3D 降噪、细节增强及锐化增强

- Local Tone mapping

- Sensor 自带宽动态和2帧宽动态

- 两轴数字图像防抖

- 镜头畸变校正

- 提供 PC 端 ISP tuning tools

硬件加速引擎
~~~~~~~~~~~~

- 软硬体混合模式支持部分 OpenCV 库

- 软硬体混合模式支持部分 IVE 库

音频编解码
~~~~~~~~~~

- 集成 Audio CODEC, 支持 16 bit 音源/语音 输入和输出

- 集成单声道麦克风输入

- 集成单声道输出. (需要外挂功放才能推动喇叭)

- 内部集成另一路的麦克风直连輸出声道, 方便实现 AEC

- 软件音频编解码协议 (G.711, G.726, ADPCM)

- 软件支持音频 3A (AEC, ANR, AGC) 功能

网络接口
~~~~~~~~

- 以太网模块提供 1 个 Ethernet MAC , 实现网路数据的接收与发送。

- Ethernet MAC 搭配内建 10/100Mbps Fast Ethernet Transceiver
  可工作在 10/100Mbps 全双工或半双工模式。

安全系统模块
~~~~~~~~~~~~

- 硬件实现 AES/DES/SM4 多种加解密算法

- 硬件实现 HASH (SHA1/SHA256) 哈希算法

- 硬件实现随机数发生器

- 内部集成 2Kbit eFuse 逻辑空间

智能安全运行环境
~~~~~~~~~~~~~~~~

- 支持信任链建立: 提供安全环境的基础，为可信环境的根本，如硬件安全设置、信任根。

- 支持安全启动，提供安全硬件、软件保护功能。

- 支持资料加密安全: 数据加密程序，运算核心加密。

- 支持软、固件验签流程:碉认软件可信性及完整性，包括 开机及载入验签程序。

- 支持安全储存及传输:保护外部数据储存及交换。

- 支持安全更新。

外围接口
~~~~~~~~

- 集成 POR, Power sequence。

- 4 个单端 ADC (3 in No-die domain)。

- 6 个 I2C (1 in No-die domain)。

- 3 个 SPI。

- 5 组 UART (1 in No-die domain)。

- 4 组 (15 通道) PWM。

- 2 个 SDIO 接口：

  - 一个支持 3V 连接 SD 3.0 Card (支持最大容量 SDXC 2TB, 支持速度为 UHS-I)。

  - 一个支持 1.8V / 3.0V 连接其他 SDIO 3.0 设备 (支持速度为 UHS-I)。

- 66 GPIO 接口 (14 in No-die domain)。

- 集成 keyscan 及 Wiegand。

- 集成 MAC PHY 支援 10/100Mbps 全双工或半双工模式。

- 一个 USB Host / device 接口。

**注**: 有关 No-die domain 的概念，参考 :ref:`section_power` 章节。

外部存储器接口
~~~~~~~~~~~~~~

- 内建 DRAM。

  - DDR3 16bitx1, 最高速率达 1866Mbps, 容量 2Gbit (256MB)。

- SPI NOR flash 接口 (1.8V / 3.0V)。

  - 支持 1, 2, 4 线模式。

  - 最大支持 256MByte。

- SPI Nand flash 接口 (1.8V / 3.0V)。

  - 支持 1KB/2KB/4KB page (对应的最大容量 16GB/32GB/64GB)。

  - 使用器件本身内建的 ECC 模块。

- eMMC 4.5 接口 (1.8V/3.0V) SD0 EMMC 共电. 因为 SD卡 default 3V, 所以有 SD 卡时, 不适合接 1.8V eMMC。

  - 4 bit 接口。

  - 支持 HS200。

  - 最大支持容量 2TB。

芯片物理规格
~~~~~~~~~~~~

- 功耗

  - 1080P + Video encode + AI : ~ 500mW

- 工作电压

  - 内核电压为 0.9V

  - IO 电压为 1.8V 及 3.0V

  - DDR 电压如下表

    -  1.35V

- 封装

  - 使用 QFN 封装, 封装尺寸为 9mmx9mmx0.9mm. 管脚间距为 0.35mm. 管脚总数为 88 个。
