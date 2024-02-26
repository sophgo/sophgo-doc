MIPI Rx
-------

概述
~~~~

MIPI Rx (Mobile Industry Processor Interface Receiver) 模块主要功能为接收由 CMOS sensor 所传送的视频数据，支持 MIPI D-PHY、sub-LVDS (Low-Voltage Differential Signal)、HiSPi (High-Speed Serial Pixel Interface) 等不同的串行视频信号输入，并将其处理转化为内部视频时序，传递给下一级的视频处理模块 (ISP)。

MIPI Rx 模块中可细分为 PHY 和 Controller 两部分，其中 PHY 模块集成了模拟和数字两个部分，主要将串行信号转换为并行信号，而 Controller 模块则负责解码不同的视频数据格式，传送给后端的视频处理模块 (ISP)。功能框图及在系统中的位置如图表 :ref:`diagram_mipi_rx_block` 所示。

.. _diagram_mipi_rx_block:
.. figure:: ../../../../media/image44.png
	:align: center

	MIPI Rx 功能框图及在系统中的位置

特点
~~~~

- 支持 MIPI DPHY-ver2.1

- 可同时支持 2 路 sensor 输入

- 单一 sensor 最大支持 5M(2688x1944, 2880x1620) @30fps HDR or @60fps 线性输入

- 双路 sensor 最大支持 FHD(1920x1080) @60fps HDR or linear 输入

- 单路最多支持 4-Lane MIPI D-PHY 接口，最大支持 1.5Gbps/Lane

- 单路最多支持 4-Lane sub-LVDS/ HiSPi 接口，最大支持 1.5Gbps/Lane

- 支持 RAW8/RAW10/RAW12/RAW16 数据类型的解析

- 支持 YUV422 8-bit / YUV422 10-bit 数据类型的解析

- 最多支持 2 帧 WDR, 支持多种 WDR 时序

- 支持 sub-LVDS/HiSPi 模式像素/同步码大小端配置

- 支持 Lane 数和 Lane 顺序可配置

功能描述
~~~~~~~~

典型应用
^^^^^^^^

在使用图像传感器的应用中，可根据不同的接口选择 (MIPI/Sub-LVDS/HiSPi)，设置 MIPI Rx 模块寄存器，同时 MIPI Rx 也支持不同速度和不同分辨率的传输需求，并兼容多种图像传感器格式。

MIPI Rx 模块中包含 1 组 D-PHY, 每组分别有六个差分对，一个 D-PHY 可支持一对差分时钟，最多配上四对数据差分信号，或同时支持两组一对差分时钟配上两对数据差分信号，因此 MIPI Rx 可以同时支持 2 路 Sensor输入。另外 MIPI Rx可支持不同的差分对排序以及时钟差分对位置，可以通过寄存器配置时钟的来源和差分对排序方式。

MIPI Rx 只针对接口的时序转换和解码, 不处理影像处理的部分。所以在满足带宽的前提下可支持任意分辨率和帧率。MIPI Rx 的带宽有两部分限制：PHY的接口数据率和内部处理速度。输入接口最大支持 1.5Gbps/Lane, 内部处理速度最大为 600M*1pixels/s。

.. 这个表比较小，就不单独放文件中 include 了

.. _table_mipi_rx_inf_type:
.. table:: MIPI Rx Interface Type
	:widths: 1 1 1 1 1

	+-----------+--------------+-------------+-------------+-------------+
	|           | Common mode  | D\          | Maximum     | Maximum     |
	|           | voltage      | ifferential | clock       | data rate   |
	|           |              | mode        | frequency   | per lane    |
	|           |              | voltage     |             |             |
	+===========+==============+=============+=============+=============+
	| MIPI DPHY | 200mV        | 200mV       | 750MHz      | 1.5Gbps     |
	+-----------+--------------+-------------+-------------+-------------+
	| Sub-LVDS  | 900mV        | 150mV       | 750MHz      | 1.5Gbps     |
	+-----------+--------------+-------------+-------------+-------------+
	| HiS       | 900mV        | 280mV       | 750MHz      | 1.5Gbps     |
	| Pi(HiVCM) |              |             |             |             |
	+-----------+--------------+-------------+-------------+-------------+
	| HiS       | 200mV        | 200mV       | 750MHz      | 1.5Gbps     |
	| Pi(SLVDS) |              |             |             |             |
	+-----------+--------------+-------------+-------------+-------------+

MIPI 接口数据格式
^^^^^^^^^^^^^^^^^

MIPI 规范由不同的工作组负责开发和维护, 分别对应不同领域的应用。MIPI Rx 支持 D-PHY 和 CSI-2 (Camera Serial Interface)。D-PHY 规定了物理层的传输规范, CSI-2 规定了 Camera 输出数据包的格式和协议。

- D-PHY

  D-PHY 是 MIPI 联盟发布的高速物理层标准, 规定了接口层的物理特性和传输协议。D-PHY 采用了 200mV 源同步的低压差分信号技术, 每个Lane 的数据绿率范围支持到 2500Mbps。D-PHY 可以工作在低功耗 (Low Power, LP) 和高速 (High Speed, HS) 两种模式下。

- CSI-2

  CSI-2 是针对摄像头的数据协议，规定了主机与外设通信的数据包格式。

  CSI-2 可以支持不同像素格式的图像应用，数据传输的最小粒度是字节。为增加 CSI-2 的性能，可以选择数据 Lane 的数量, CSI-2 协议规订了发送端将像素数据打包成字节的机制，并指明多个数据 Lane 分配和管理的方式。字节数据以数据包的形式组织，数据包在 SoT 与 EoT 之间传输。接收端根据协议解析相应的数据包，恢复出原始的像素数据。

  MIPI Rx 支持 RAW8/RAW10/RAW12/RAW16/YUV422-8bit/YUV422-10bit 数据类型的解析。

  CSI-2 的数据包分为长包和短包两种，包含有校验码，能进行误码纠正和错误检测。

长包和短包都是在 SoT 和 EoT 之间传输，在数据传送的间隙, D-PHY 处于 LP 模式。

CSI-2 数据包的传输机制如图所示。 PH 和 PF 分别表示 Packet Header 和 Packet Footer。

.. _diagram_csi2_datapacket_transfer:
.. figure:: ../../../../media/image45.png
	:align: center

	数据包的传输机制

长包用于传输有效像素数据, 分为五个部分: Data ID, Word Count, ECC, PAYLOAD, CHECKSUM。

- Data ID 包含 Virtual Channel 和 Data Type。Virtual Channel 控制传输所用的通道, 可以使用不同的通道传输不童的数据。Data Type 则指定传输数据的类型。

- Word Count 表示接收端需要接收到的数据量。

- ECC 是纠错码，可以纠正或检测 Data Type 和 Word Count 的误码。

- PAYLOAD 为实际需要传输的像素数据。

- CHECKSUM 是利用线性反馈移位寄存器所产生的校验和，用于 PAYLOAD 资料的校验。

长包的结构如图表 :ref:`diagram_csi2_long_package_format` 所示。

.. _diagram_csi2_long_package_format:
.. figure:: ../../../../media/image46.png
	:align: center

	CSI-2 长包格式

短包的作用是同步传输信息，包含 Data ID, Data Field 和 ECC 三个部分，其格式如图表 :ref:`diagram_csi2_short_package_format` 所示。

.. _diagram_csi2_short_package_format:
.. figure:: ../../../../media/image47.png
	:align: center

	CSI-2 短包格式

MIPI Rx 共支持六种视频资料格式的传输，包含 YUV422-8bit、YUV422-10bit、RAW8、RAW10、RAW12 和 RAW16。不同的资料格式的传输方式如下所述。

YUV422-8bit 的传输模式为 UYVY 的形式，如图表 :ref:`diagram_yuv422_8bit_transfer_sequence`。

.. _diagram_yuv422_8bit_transfer_sequence:
.. figure:: ../../../../media/image48.png
	:align: center

	YUV422 8-bit 资料传输顺序

封包相对于视频信号的对应则如图表 :ref:`diagram_yuv422_8bit_transfer_map` 所示。

.. _diagram_yuv422_8bit_transfer_map:
.. figure:: ../../../../media/image49.png
	:align: center

	YUV422-8bit 资料封包传输对应

整张 Frame 的传输格式就会成为如图表 :ref:`diagram_yuv422_8bit_frame_format` 所示。

.. _diagram_yuv422_8bit_frame_format:
.. figure:: ../../../../media/image50.png
	:align: center

	YUV422 8-bit Frame 格式

YUV422-10bit 的传输模式同样为 UYVY, 传输顺序如图表 :ref:`diagram_yuv422_10bit_transfer_sequence` 所示。

.. _diagram_yuv422_10bit_transfer_sequence:
.. figure:: ../../../../media/image51.png
	:align: center

	YUV422-10bit 资料传输顺序

封包相对于视频信号的对应则如图表 :ref:`diagram_yuv422_10bit_transfer_map` 所示。

.. _diagram_yuv422_10bit_transfer_map:
.. figure:: ../../../../media/image52.png
	:align: center

	YUV422-10bit 资料封包传输对应

整张 Frame 的传输格式就会成为如图表 :ref:`diagram_yuv422_10bit_frame_format` 所示。

.. _diagram_yuv422_10bit_frame_format:
.. figure:: ../../../../media/image53.png
	:align: center

	YUV422-10bit Frame 格式

RAW8 的传输顺序如图表 :ref:`diagram_raw8_transfer_sequence` 所示。

.. _diagram_raw8_transfer_sequence:
.. figure:: ../../../../media/image54.png
	:align: center

	RAW8 资料传输顺序

整张 Frame 的传输格式就会成为如图表 :ref:`diagram_raw8_frame_format` 所示。

.. _diagram_raw8_frame_format:
.. figure:: ../../../../media/image55.png
	:align: center

	RAW8 Frame 格式

RAW10 的传输顺序如图表 :ref:`diagram_raw10_transfer_sequence` 所示。

.. _diagram_raw10_transfer_sequence:
.. figure:: ../../../../media/image56.png
	:align: center

	RAW10 资料传输顺序

整张 Frame 的传输格式就会成为如图表 :ref:`diagram_raw10_frame_format` 所示。

.. _diagram_raw10_frame_format:
.. figure:: ../../../../media/image57.png
	:align: center

	RAW10 Frame 格式

RAW12 的传输顺序如图表 :ref:`diagram_raw12_transfer_sequence` 所示。

.. _diagram_raw12_transfer_sequence:
.. figure:: ../../../../media/image58.png
	:align: center

	RAW12 资料传输顺序

整张 Frame 的传输格式就会成为如图表 :ref:`diagram_raw12_frame_format` 所示。

.. _diagram_raw12_frame_format:
.. figure:: ../../../../media/image59.png
	:align: center

	RAW12 Frame 格式

RAW16 的传输顺序如图表 :ref:`diagram_raw16_transfer_sequence` 所示。

.. _diagram_raw16_transfer_sequence:
.. figure:: ../../../../media/image60.png
	:align: center

	RAW16 资料传输顺序

整张 Frame 的传输格式就会成为如图表 :ref:`diagram_raw16_frame_format` 所示。

.. _diagram_raw16_frame_format:
.. figure:: ../../../../media/image61.png
	:align: center

	RAW16 Frame 格式

MIPI 接口线性模式
^^^^^^^^^^^^^^^^^

MIPI 接口的线性模式传输格式如图表 :ref:`diagram_mipi_inf_graphic_format` 所示。每张图的传输都是以短包 Frame Start (FS)作为起式，短包 Frame End (FE) 作为结束。中间的视频内容则是以行为单位，每个长包传输一条完整的视频行。长包格式如 MIPI 标准所规范每一行有 32bit 的数据包头 (PH, Pecket Header)，其中包含了当前行的 Virtual Channel 和 Data Type 等信息。

.. _diagram_mipi_inf_graphic_format:
.. figure:: ../../../../media/image62.png
	:align: center

	MIPI 接口图像格式


MIPI 接口宽动态模式
^^^^^^^^^^^^^^^^^^^

MIPI Rx 支持四种 MIPI 接口的宽动态 (WDR) 模式，分别为：

1. 使用 DT (Data Type) 区分长短曝光数据

2. 使用识别码 ID (Identification Code) 区分长短曝光数据

3. 利用寄存器设定长短曝光数据延迟区间

使用 DT 的 WDR 传输方式如图表 :ref:`diagram_mipi_inf_wide_dynamic_data_transfer_dt` 所示，不同曝光长度共用一组 FS/FE 短包，而长包的包头中包含有 DT 信息，可利用不同的 DT 来区分长短曝光数据，其中真正的数据格式 DT 和代表长短曝光数据的两组 DT 都可以利用寄存器来设定, MIPI Rx 便能够解析出正确的宽动态时序传送给后方的视频处理模块。

.. _diagram_mipi_inf_wide_dynamic_data_transfer_dt:
.. figure:: ../../../../media/image63.png
	:align: center

	MIPI 接口宽动态数据传输 (使用DT)

使用 ID 的 WDR 传输方式如图表 :ref:`diagram_mipi_inf_wide_dynamic_data_transfer_id` 所示，不同曝光长度共用一组 FS/FE 短包，而传输数据中每个长包的前四个像素用来传输代表不同曝光长度的 ID (Identification Code)，代表长短曝光的 ID 可利用寄存器设置，MIPI Rx 会利用 ID 分别不同曝光视频信号，并将前四个像素去除后再传送给视频处理模块。

.. _diagram_mipi_inf_wide_dynamic_data_transfer_id:
.. figure:: ../../../../media/image64.png
	:align: center

	MIPI接口宽动态数据传输 (使用ID)

最后一种支持的 WDR 传输方式则是没有任何的 DT 或 ID 来表示传输的长包是长曝或短曝的内容, 使用者必须自行设定寄存器表明长曝和短曝之间的曝光行数差异, MIPI Rx 会解析出相对应的时序给视频处理模块，实际传输时序如图表 :ref:`diagram_mipi_inf_wide_dynamic_data_transfer_reg` 所示。

.. _diagram_mipi_inf_wide_dynamic_data_transfer_reg:
.. figure:: ../../../../media/image65.png
	:align: center

	MIPI 接口宽动态数据传输 (寄存器设定)

Sub-LVDS 接口数据格式
^^^^^^^^^^^^^^^^^^^^^

超低电压差分信号 sub-LVDS (Low-Voltage Differential Signal) 普遍应用于前端摄像头，通过同步码区分有效视频信号的区间以及宽动态模式的长短曝。

MIPI Rx 的 PHY 将差分串行数据转换为并行数据，接着 MIPI Rx 的控制器把并行数据根据不同的模式和同步码解码出像素数据。

MIPI Rx 支持 8bit、10bit 和 12bit 三种位元宽度的 Sub-LVDS 传输模式，接口数据格式如图表 :ref:`diagram_sub_lvds_inf_data_format` 所示，所有有效的视频信号都会在 SAV 和 EAV 同步码中间，其中同步码都是由四个字段构成，每个字段的位宽与后方的像素位宽相同, 而前三个字段为固定的基准码字, 第四个字段可用来区分有效区间的起始或结束, Sub-LVDS 同步码格式如图表 :ref:`table_sub_lvds_sync_code_example` 所示，同步码根据不同的厂商会使用不同的数值，图表 :ref:`table_sub_lvds_sync_code_example` 只是其中一种实现方式，不同的数值可以在寄存器中设置。

.. _diagram_sub_lvds_inf_data_format:
.. figure:: ../../../../media/image66.png
	:align: center

	Sub-LVDS 接口数据格式

.. 这个表比较小，就不单独放文件 include 了

.. _table_sub_lvds_sync_code_example:
.. table:: Sample of Sub-LVDS Sync Code
	:widths: 1 2 1 1 1 1

	+---------------------------------------------------------------------+
	| **12-bit**                                                          |
	+------------+---------------------+-------+--------+--------+--------+
	|            |                     | 1st   | 2nd    | 3rd    | 4th    |
	|            |                     | word  | word   | word   | word   |
	+------------+---------------------+-------+--------+--------+--------+
	| Blanking   | Start sync code     | FFFh  | 000h   | 000h   | AB0h   |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | B60h   |
	+------------+---------------------+       |        |        +--------+
	| Effective  | Start sync code     |       |        |        | 800h   |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | 9D0h   |
	+------------+---------------------+-------+--------+--------+--------+
	| **10-bit**                                                          |
	+------------+---------------------+-------+--------+--------+--------+
	|            |                     | 1st   | 2nd    | 3rd    | 4th    |
	|            |                     | word  | word   | word   | word   |
	+------------+---------------------+-------+--------+--------+--------+
	| Blanking   | Start sync code     | 3FFh  | 000h   | 000h   | 2ACh   |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | 2D8h   |
	+------------+---------------------+       |        |        +--------+
	| Effective  | Start sync code     |       |        |        | 200h   |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | 274h   |
	+------------+---------------------+-------+--------+--------+--------+
	| **8-bit**                                                           |
	+------------+---------------------+-------+--------+--------+--------+
	|            |                     | 1st   | 2nd    | 3rd    | 4th    |
	|            |                     | word  | word   | word   | word   |
	+------------+---------------------+-------+--------+--------+--------+
	| Blanking   | Start sync code     | FFh   | 00h    | 00h    | ABh    |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | B6h    |
	+------------+---------------------+       |        |        +--------+
	| Effective  | Start sync code     |       |        |        | 80h    |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | 9Dh    |
	+------------+---------------------+-------+--------+--------+--------+

而 Sub-LVDS 的同步码和像素资讯在不同 Lane 的传输模式如图表 :ref:`diagram_sub_lvds_multilane_transfer` 所示，每一条 Lane 都会传输相同的同步码，紧接着才是像素数据，像素数据会根据使用的通道数以像素位宽为单位照顺序排列。

.. _diagram_sub_lvds_multilane_transfer:
.. figure:: ../../../../media/image67.png
	:align: center

	Sub-LVDS Multi Lane 传输模式

Sub-LVDS 中同步码和像素数据是串行的，而 MIPI Rx 支持数据的大小端可利用寄存器设置，以大端模式为例，输出单个像素点的时序如图表 :ref:`diagram_sub_lvds_single_pixel_sequence` 所示。

.. _diagram_sub_lvds_single_pixel_sequence:
.. figure:: ../../../../media/image68.png
	:align: center

	Sub-LVDS 单个像素时序图

Sub-LVDS 接口线性模式
^^^^^^^^^^^^^^^^^^^^^

Sub-LVDS 在线性模式中, 利用同步码标明一张图像数据中每条线的起始和结束, 而在同步码SAV和EAV以外的就不是有效视频数据, 如图表 :ref:`diagram_sub_lvds_liner_sequence` 所示。

.. _diagram_sub_lvds_liner_sequence:
.. figure:: ../../../../media/image69.png
	:align: center

	Sub-LVDS 线性模式时序图

Sub-LVDS 接口宽动态模式
^^^^^^^^^^^^^^^^^^^^^^^

MIPI Rx 可支持两种 Sub-LVDS 接口宽动态模式，第一种模式中如图表 :ref:`diagram_sub_lvds_wide_dynamic_mode_1`，长短曝的视频信号分别都有 SAV 和 EAV 同步码包住, MIPI Rx 可利用不同的同步码解析出该视频信号是长曝还是短曝。第二种模式则是如图表 :ref:`diagram_sub_lvds_wide_dynamic_mode_2` 将长曝和短曝用同一组 SAV 和 EAV 包住，必须在寄存器中设置每条线的宽度和 blanking 长度, MIPI Rx 必须利用这些寄存器的设定和同步码解析出长曝和短曝分别的时序，接着再传送到视频处理模块。

.. _diagram_sub_lvds_wide_dynamic_mode_1:
.. figure:: ../../../../media/image70.png
	:align: center

	Sub-LVDS 宽动态模式一

.. _diagram_sub_lvds_wide_dynamic_mode_2:
.. figure:: ../../../../media/image71.png
	:align: center

	Sub-LVDS 宽动态模式二

HiSPi 接口数据格式
^^^^^^^^^^^^^^^^^^

High-Speed Serial Pixel (HiSPi) 接口也被使用于某些摄像头，和 Sub-LVDS 类似使用同步码来区分有效的视频信息和在宽动态模式中区分长短曝。HiSPi 规范中定义了四种不同的打包模式，分别为 Packetized-SP、Streaming-SP、Streaming-S 和 ActiveStart-SP8 四种不同的传输模式。

MIPI Rx 支持其中较为常见的 Packetized-SP 和 Streaming-SP 两种传输方式。

HiSPi 接口线性模式
^^^^^^^^^^^^^^^^^^

MIPI Rx 支持两种不同的 HiSPi模式, 在 Packetized-SP 模式中如图表 :ref:`diagram_hispi_packateized_sp_mode` 所示，图像传感器使用 SOF 表示有效视频信号的第一行，并用 EOF 表示有效视频信号最后一行的结束。其他有效视频信号则是使用 SOL 和 EOL 作为一行的起始和结束。

.. _diagram_hispi_packateized_sp_mode:
.. figure:: ../../../../media/image72.png
	:align: center

	HiSPi Packetized-SP 模式

在 Streaming-SP 模式中如图表 :ref:`diagram_hispi_streaming_sp_mode` 所示，图像传感器并不传送代表结束的 EOL 或是 EOF, 因此 MIPI Rx 控制器必须利用寄存器的设置得知有效视频信号的数量，才能解析出正确的视频信号传送给视频处理模块 (ISP)。另外 Streaming-SP 模式也支持表示空白行数的 SAV 信号，两种不同传输方式所支持的同步码整理如图表 :ref:`table_hispi_sync_code_support_mode` 所示。

.. _diagram_hispi_streaming_sp_mode:
.. figure:: ../../../../media/image72.png
	:align: center

	HiSPi Streaming-SP 模式

.. 这个表比较小，就不单独放文件 include 了

.. _table_hispi_sync_code_support_mode:
.. table:: HiSPi Sync Code Support Mode
	:widths: 1 1 1

	+-----------------+-------------------------+-------------------------+
	| Sync Code       | Packetized-SP           | Streaming-SP            |
	+=================+=========================+=========================+
	| SOF             | Required                | Required                |
	+-----------------+-------------------------+-------------------------+
	| SOL             | Required                | Required                |
	+-----------------+-------------------------+-------------------------+
	| EOF             | Required                | Unsupported             |
	+-----------------+-------------------------+-------------------------+
	| EOL             | Required                | Unsupported             |
	+-----------------+-------------------------+-------------------------+
	| SAV             | Unsupported             | Required                |
	+-----------------+-------------------------+-------------------------+

HiSPi 接口宽动态模式
^^^^^^^^^^^^^^^^^^^^

HiSPi 接口宽动态模式同样分为两种不同的模式，第一种 Packetized-SP 如图表 :ref:`diagram_hispi_packetized_sp_width_dynamic_transfer` 所示，长曝和短曝会利用不同的同步码来区别，其中在 SOF_L 和 EOF_L 中的才是有效的长曝视频信号，同样在 SOF_S 和 EOF_S 中的才是有效的短曝视频信号。在长曝的最后和短曝的起始几行并不是有效的像素区，而是以固定值填充。

.. _diagram_hispi_packetized_sp_width_dynamic_transfer:
.. figure:: ../../../../media/image74.png
	:align: center

	HiSPi Packetized-SP 宽动态传输

第二种 Streaming-SP 的宽动态传输则如图表 :ref:`diagram_hispi_streaming_sp_width_dynamic_transfer` 所示，其中长曝和短曝的同步码和线性模式相同，因此需要利用寄存器设置长曝短曝之间的曝光行数差距, MIPI Rx 才能解析出正确的宽动态视频信号。

.. _diagram_hispi_streaming_sp_width_dynamic_transfer:
.. figure:: ../../../../media/image75.png
	:align: center

	HiSPi Streaming-SP 宽动态传输

MIPI Rx 寄存器概览
~~~~~~~~~~~~~~~~~~

在芯片中最多可以同时使用两组 MIPI Rx 模块，其中主要分为三组寄存器，第一个部分是控制 PHY 模块的寄存器，基址为 0x0A0D0000, 第二部分是控制 CSI 模块的寄存器，基址为 0x0A0C2400 和 0x0A0C4400, 第三部分则是控制 Sub-LVDS 和 HiSPi 模块的寄存器，基址为 0x0A0C2200 和 0x0A0C4200。

.. include:: ./mipi_rx_phy_registers_overview.table.rst

MIPI Rx 寄存器描述
~~~~~~~~~~~~~~~~~~

MIPI Rx PHY 寄存器描述
^^^^^^^^^^^^^^^^^^^^^^

基址: 0x0A0D0000
''''''''''''''''

.. include:: ./mipi_rx_phy_registers_description_0x0a0d0000.table.rst

基址: 0x0A0D0300
''''''''''''''''

.. include:: ./mipi_rx_phy_registers_description_0x0a0d0300.table.rst

基址: 0x0A0D0600
''''''''''''''''

.. include:: ./mipi_rx_phy_registers_description_0x0a0d0600.table.rst

MIPI Rx CSI 控制器寄存器
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ./mipi_rx_csi_registers_description.table.rst

MIPI Rx Sub-LVDS 控制寄存器
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ./mipi_rx_sub_lvds_registers_description.table.rst
