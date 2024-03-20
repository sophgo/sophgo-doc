VI
--

概述
~~~~

视频输入单元 VI (Video Input) 为芯片接收摄像头视频数据模块，可以支持通过 MIPI Rx (包含 MIPI、Sub-LVDS、HiSPi) 接口或 BT.656、BT.601、BT.1120 接口和 DC (Digital Camera) 接收视频数据，处理后送到下一级的视频处理模块 (ISP)。VI 的功能框图如图表 :ref:`diagram_vi_function` 所示。

VI 分为两个物理子模块，由移动行业处理器接口接收端模块 MIPI Rx 和视频输入处理模块 VI Proc 组成。MIPI Rx 模块接收处理不同的视频数据，而 VI Proc 模块则会将不同格式的视频信号统整为 ISP 模块所需的单一视频信号送出。

.. _diagram_vi_function:
.. figure:: ../../../../media/image29.png
	:align: center

	VI 功能框图

特点
~~~~

- MIPI Rx 最多同时支持两路 sensor数据输入。

  - 单一 sensor 最大支持 5M (2688x1944, 2880x1620) @60fps HDR 输入 or @30fps 线性输入。

  - 双路 sensor 最大支持 FHD (1920x1080) @60fps HDR or linear 输入。

- MIPI Rx 输入支持最大数据位宽为 12bit。

- 支持 BT.656、BT.601、BT.1120 (仅支持逐行模式)。

- 支持 BT.656/BT.1120 多通道融合输入 (1,2,4 通道, 仅支持逐行模式)。

DC 接口

- 支持 MIPI CSI-2、Sub-LVDS、HiSPi 接口。

- 支持 MIPI 接口输入 YUV422 格式。

- 支持两帧高动态范围 (HDR) 影像输入。

模式功能描述
~~~~~~~~~~~~

典型应用
^^^^^^^^

VI 可以支持多种时序输入以及不同接口，并针对不同编码方式做视频输入采集，系统可以利用寄存器配置不同的功能模式，使之适应不同的视频接口。

VI 模块最多可支持三路输入，典型输入如下

- 1 路 5M (2688x1944, 2880x1620) @60fps HDR 输入或是线性 @30fps 输入。

- 2 路 FHD (1920x1080) @60fps HDR or 线性输入 + 1 路 BT 输入 (BT.656, BT.601 or BT.1120)。

- 1 路 5M (2688x1944, 2880x1620) @60fps HDR or @30fps 线性输入 + 1 路 BT 输入。

功能原理
^^^^^^^^

BT.1120 接口时序
^^^^^^^^^^^^^^^^

VI 支持 Y/C 分开输入的 BT.1120 接口时序，传输视频信号之前会先传送同步码，同步码为数据流中使用特殊字节 SAV 和 EAV 分别表示有效行数据的开始和结束。同步码后使用 16bit 来传输视频信号，其中 8bit 用来传输亮度，另外 8bit 用来传输色度，如图表 :ref:`diagram_bt1120_horizontal_sequence` 和图表 :ref:`diagram_bt1120_vertical_sequence` 所示。

.. _diagram_bt1120_horizontal_sequence:
.. figure:: ../../../../media/image30.png
	:align: center

	BT.1120 水平接口时序

.. _diagram_bt1120_vertical_sequence:
.. figure:: ../../../../media/image31.png
	:align: center

	BT.1120 垂直接口时序

同步码格式为 4 个字节 (byte) 的组合，依序为 {0xFF, 0x00, 0x00, EAV/SAV}, 第四个字节详解如下， SG2002 只支持渐进式逐行扫描格式(Progressive)，故 bit 6 值为 0 。

.. 这个表格很小，就不单独做成文件 include 了

.. _table_sync_code_format:
.. table:: Sync code format
	:widths: 1 1 1 1 1 1 1 1 1

	+--------+--------------------+---------------------------+---------+
	|        | SAV/EAV bit        | Protection Bit            |         |
	+========+======+======+======+======+======+======+======+=========+
	| 7      | 6    | 5    | 4    | 3    | 2    | 1    | 0    | Comment |
	| (Fixed)| (F)  | (V)  | (H)  | (P3) | (P2) | (P1) | (P0) |         |
	+--------+------+------+------+------+------+------+------+---------+
	| 1      | 0    | 0    | 0    | 0    | 0    | 0    | 0    | SAV_VLD |
	+--------+------+------+------+------+------+------+------+---------+
	| 1      | 0    | 0    | 1    | 1    | 1    | 0    | 1    | EAV_VLD |
	+--------+------+------+------+------+------+------+------+---------+
	| 1      | 0    | 1    | 0    | 1    | 0    | 1    | 1    | SAV_BLK |
	+--------+------+------+------+------+------+------+------+---------+
	| 1      | 0    | 1    | 1    | 0    | 1    | 1    | 0    | EAV_BLK |
	+--------+------+------+------+------+------+------+------+---------+

SAV_VLD : 有效行区，行同步信号结束，有效画素开始。

EVA_VLD : 有效行区，行同步信号开始，有效画素结束。

SAV_BLK : 消隐行区，行同步信号结束。

EAV_BLK : 消隐行区，行同步信号开始。

BT.656 接口时序
^^^^^^^^^^^^^^^

VI 同样支持 Y/C 合并输入的 BT.656 接口时序，传输时同样利用同步码 SAV 和 EAV 表示有效行数据的开始和结束，但只利用 8bit 传输视频信号，并利用分时的方式传输亮度和色度，如图表 :ref:`diagram_bt656_horizontal_sequence` 所示。

.. _diagram_bt656_horizontal_sequence:
.. figure:: ../../../../media/image32.png
	:align: center

	BT.656 水平接口时序

BT.656 和 BT.1120 差别只在影像传输用 16 bit (BT.1120)和 8bit (BT.656), 其余垂直时序和同步码格式都一致。

BT.601 接口时序
^^^^^^^^^^^^^^^

除了利用同步码 BT.1120 和 BT.656, VI 支持利用多种不同的同步信号来传输的 BT.601 接口时序。实际的视频资料可利用寄存器设定为 Y/C 分开输入的 16bit 模式或是 Y/C 合并分时输入的 8bit 模式，而同步方式则可利用寄存器选择 vhs, vde, 或是 vsde 三种模式，详细时序如下图。

.. _diagram_bt601_vhs_symc_mode:
.. figure:: ../../../../media/image33.png
	:align: center

	BT.601 vhs 同步模式

vhs 模式输入同步信号为帧同步信号 (vs), 行同步信号 (hs)，系统必须设定帧后消隐行数 (vs_back_porch)，影像高度 (img_ht), 行后消隐像素数 (hs_back_porch) 和影像宽度 (img_wd)。

.. _diagram_bt601_vde_symc_mode:
.. figure:: ../../../../media/image34.png
	:align: center

	BT.601 vde 同步模式

vde 模式同步信号为行有效信号 (vde) 和 行有效信号 (hde)。在此模式下, 系统不用设置时序相序相关的参数。VI 模组会依据 hde/vde 信号收资料,以依 vde 信号做帧更新。

.. _diagram_bt601_vsde_symc_mode:
.. figure:: ../../../../media/image35.png
	:align: center

	BT.601 vsde 同步模式

vsde 模式同步信号为帧同步信号 (vs) 和有效像素旗标 (de)。在此模式下, 系统不用设置时序相序相关的参数。VI 模组会依据 de 信号收资料,以依 vs 信号做帧更新。

.. _diagram_bt601_yc_separate_16bit_mode:
.. figure:: ../../../../media/image36.png
	:align: center

	BT.601 Y/C 分开 16bit 模式


.. _diagram_bt601_yc_combine_8bit_mode:
.. figure:: ../../../../media/image37.png
	:align: center

	BT.601 Y/C 合并 8bit 模式

数字摄像头 (DC) 接口时序
^^^^^^^^^^^^^^^^^^^^^^^^

VI 支持传送 RAW 格式仿 BT 传输的数字摄像头 (DC) 接口时序，在 DC 接口可支持 8bit, 10bit, 12bit, 和 16bit 四种不同模式，也可利用寄存器设定利用接收同步码或是类似 BT.601 的三种不同同步模式来接收视频信号。

.. _diagram_dc_sync_code_mode:
.. figure:: ../../../../media/image38.png
	:align: center

	DC 同步码模式


.. _diagram_dc_sync_signal_mode_vhs:
.. figure:: ../../../../media/image33.png
	:align: center

	DC 同步信号模式 -vhs mode

.. _diagram_dc_sync_signal_mode_vde:
.. figure:: ../../../../media/image34.png
	:align: center

	DC 同步信号模式 -VDE mode

.. _diagram_dc_sync_signal_mode_vsde:
.. figure:: ../../../../media/image35.png
	:align: center

	DC 同步信号模式 -VSDE mode

图像储存模式
~~~~~~~~~~~~

储存在 DRAM 的图像区分为 Bayer 12bit 与 YCbCr 8bit 两种格式。其中 Y/Cb/Cr 为分开存储在三个不同的 DRAM 位置。两种 (12bit/8bit)格式的图像在 DRAM 的排列方式如下图所示。

.. _diagram_bayer_12bit_graphc_storage_format:
.. figure:: ../../../../media/image39.png
	:align: center

	Bayer 12 bit 图像储存方式


.. _diagram_ycbcr_8bit_graphc_storage_format:
.. figure:: ../../../../media/image40.png
	:align: center

	YCbCr 8bit 图像储存方式

VI 寄存器概览
~~~~~~~~~~~~~

芯片中有两套相同的 VI 模块，内部寄存器偏移地址都相同，而基址分别为 0x0A0C2000 和 0x0A0C4000。另外有一套只支持 BT 接口的 VI 模块，基址为 0x0A0C6000。

.. include:: ./vi_registers_overview.table.rst

VI 寄存器描述
~~~~~~~~~~~~~

.. include:: ./vi_registers_description.table.rst
