VDP (Video Display Processor)
-----------------------------

概述
~~~~

VDP 模块可迭加图形数据在视频数据之上，再经由不同的显示通道输出。视频数据可从内存读取或是接收 VPSS 模块输出的视频。图形数据则必须由内存读取。

架构描述
~~~~~~~~

VDP 的整体架构如图

.. _diagram_vdp_overview:
.. figure:: ../../../../media/image41.png
	:align: center

	VDP 功能框图

SG2002 仅支持一路 BT.656/BT.601/BT.1120/MCU-I80/MCU-M68/LVDS/MIPI DSI/serial TTL 输出

- 总线数据读取，数据处理，包含视频层 V, 图形层G。

- 视频层可接收不同的影像格式 (YUV422,YUV420,YUV444,RBG packet,NV12/NV21,YUYV-packet)，并将之转换成显示通道所需的时序及格式。

- 图形层支持 ARGB8888,ARGB4444, ARGB1555, 8-bit/4-bit LUT,font base 等格式的 OSD。

- 支持 OSD 压缩格式。

- Blend : 单层图形层 G 视频图形迭加器。

VDP 的特点如下 :

- MIPI Tx 输出接口 : 最大支持 1080P@60fps RGB24-bit 输出。

- LVDS 输出 : 最大支持 720P@60fps RGB24-bit 输出。

- 数字输出接口 : (BT format only support progressive mode)

  - 支持 ITU-R BT.1120 输出

  - 支持 ITU-R BT.656 输出

  - 支持 ITU-R BT.601 输出

  - MCU I80/M68 8-bit 输出

  - 支持 serial TTL 平行输出

- 视频层 : V 层。

- 图形层 : G 层。

- 迭加特性 : V/G 256 阶线性迭加, 并支持 Gamma 校正。

- VDP 包含一个显示通道，一个时序中断以及一个低带宽中断。

工作方式
~~~~~~~~

时钟配置
^^^^^^^^

VDP 搭配专属的时钟生成器，架构如下

.. _diagram_vdp_clock_generator:
.. figure:: ../../../../media/image42.png
	:align: center

	VDP 时钟生成器

- clk_syn : 1GHz or 1.2Ghz

- FREQ_SYN : 6-bit 整数, 26-bit 小数的频率生成器

- PLL : 产生 VDP 时钟及 MIPI Tx/ LVDS 串行所需时钟

复位
^^^^

VDP 复位包含一个硬件复位及一个软件复位。

在进行AXI总线复位之前 :

- 将所有 AXI 存取关闭。

- 确认 AXI 存取动作已结束，再配置总线复位。

输出接口
^^^^^^^^

VDP 支持下列三种接口输出

- MIPI DSI

- LVDS

- ITU-R BT.1120/ITU-R BT.656/ITU-R BT.601/MCU I80/MCU M68/Serial TTL输出

中断
^^^^

VDP 支持两类中断

- 垂直时序中断

- 低带宽中断

垂直时序中断
^^^^^^^^^^^^

VDP 包含一个显示通道，对应有一个垂直时序中断:

- 支持帧开始/结束中断。

- 支持中断屏蔽可配。

- 每个中断可写 1 清除。

低带宽中断
^^^^^^^^^^

VDP 支持 polling 方式提供低带宽状态:

- 中断屏蔽可配。

- 中断写 1 清除。

功能描述
~~~~~~~~

视频层功能
^^^^^^^^^^

视频层 V 特性
^^^^^^^^^^^^^

- 支持输入影像格式 : 400, planar-420,planar-422,planar-444, RGB packet。

- 最小输入分辨率为 64x64,最大输入分辨率为 1920x1080。

- 最小输出分辨率为 64x64,最大输出分辨率为 1920x1080。

- 支持输入数据位宽: 8-bit 。

- YUV420 水平/垂直分辨率为2的倍数。

- YUV422 水平分辨率为2的倍数。

- YUV400/Planar-444(RGB or YUV)/RGB packet 无分辨率限制。

- 源起始地址可配，地址 32-byte 对齐。

  - 源 stride 可配, 32-byte对齐。

- 支持色彩空间转换，支持对比度/亮度调节。

- 支持视频层 BT.601, BT.709 色域转换。

- 支持显示位置/大小可配，在屏幕任意位置显示。

图形层 G 特性
^^^^^^^^^^^^^

- 支持输入像素格式: ARGB8888,ARGB4444,ARGB1555,LUT8,LUT4,LUT1。

- 最小输入分辨率为 64x64,最大输入分辨率为 1920x1080。

- 源起始地址可配，地址 32-byte 对齐。

  - 源 stride 可配, 32-byte对齐。

  - 支持色彩空间转换。

  - 支持显示位置可配，在屏幕任意位置显示。

  - 支持 0~255 alpha。

  - 支持 colorkey 处理。

叠加处理
^^^^^^^^

VDP 只支持 一层视频层，一层图形层迭加。

叠加特性
^^^^^^^^

支持 8 window 迭加。

显示通道特性
^^^^^^^^^^^^

- 可做为高清，标清的输出通道。

  - 只能选择一个输出接口输出。

  - 支持典型 1080P@60fps, 720P@60fps 输出时序。

时序配置
^^^^^^^^

VDP 输出接口可依不同对接芯片接口，支持配置各种典型及非典型时序。

所有时序参数必须在接口打开之前完成配置。

高清输出接口 MIPI Tx
^^^^^^^^^^^^^^^^^^^^

- 支持 RGB666,RGB565,RGB10-10-10 输出。

- 支持 1080P@60fps 4-channel 显示。

- 支持 720P@60fps 2/4-channel 显示。

高清输出接口 BT.1120 特性
^^^^^^^^^^^^^^^^^^^^^^^^^

- 支持 YUV422 8bit 输出。

- 支持数据钳位的 clip, 根据接口协议, Y 钳位范围 16~235, C 钳位范围 16~240。

- 支持以下典型输出时序: 720P、1080P。

- 16 bit 数据, 默认Y 在高位, C 在低位, YC 位置可互换。

- 支持色彩信号 Cb/Cr 时序互换。

- 支持输出随路时钟反相。

- 只支持 Progressive 时序。

标清输出接口 BT.656 特性
^^^^^^^^^^^^^^^^^^^^^^^^

- 支持 YUV422 8bit 输出。

- 支持数据钳位的 clip, 根据接口协议, Y 钳位范围 16~235, C 钳位范围 16~240。

- 支持 Y/C 时序互换，色彩信号 Cb/Cr 时序互换。

- 只支持 Progressive 时序。

BT.601 特性
^^^^^^^^^^^

- 支持 YUV422 8-bit输出。

- YC 数据范围 0 ~ 255。

- 支持 VS/HS 同步信号输出。

- 支持 Y/C 时序互换，色彩信号 Cb/Cr 时序互换。

- 只支持 Progressive 时序。

MCU 特性
^^^^^^^^

- 支持 8-bit data, 4-bit control 输出。

- 支持 I80/M68 格式输出。

LCD LVDS 输出接口
^^^^^^^^^^^^^^^^^

- 支持 1-link LVDS 输出。

- 支持 6-bit/8-bit RGB 串行输出。

- 支持 VESA/JEIDA 格式输出。

.. _diagram_data_format_lvds_jeida_vesa_mode:
.. figure:: ../../../../media/image43.png
	:align: center

	LVDS JEIDA/VESA mode 的 data format

VDP 寄存器概览
~~~~~~~~~~~~~~

VDP DISP 寄存器位置为 0X0A08_8000 ~ 0x0A08_83FF

.. include:: ./vdp_disp_registers_overview.table.rst

VDP OSD 寄存器位置为 0X0A08_8800 ~ 0x0A08_89FF

.. include:: ./vdp_osd_registers_overview.table.rst

VDP 寄存器描述
~~~~~~~~~~~~~~

VDP DISP 寄存器
^^^^^^^^^^^^^^^

.. include:: ./vdp_disp_registers_description.table.rst

VDP_OSD 寄存器描述
^^^^^^^^^^^^^^^^^^

.. include:: ./vdp_osd_registers_description.table.rst
