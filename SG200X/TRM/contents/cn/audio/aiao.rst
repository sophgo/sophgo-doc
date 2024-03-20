AIAO
----

概述
~~~~

音频输入输出接口 (Audio Input/Audio Output) 用于和芯片内置 Audio Codec 或芯片外置的 Audio Codec 及数位麦克风做对接，完成音频数据的发送和接收，实现录音、放音、对讲等功能。芯片内部将 AIAO 相关模块集成在一个子系统内，内置的 Audio Codec ADC/DAC, 支持立体声输入和输出。对外支持两组 I2S 接口，内部则集成 4 组 I2S TX/RX 模块，可同时接收发送音频数据，并可支持多声道数据同时收送。基本模块框图如下图所示：

.. _diagram_aiao_block:
.. figure:: ../../../../media/image83.png
	:align: center

	AIAO 框图

特点
~~~~

AIAO 接口支持主模式 (Master-mode)、从模式 (Slave-mode) I2S 和 PCM 模式, 并支持多通道 TDM 模式。接收和发送音频数据通过 DMA 方式存取 DDR 空间。具体特点如下：

- 高弹性化可配置的时序参数，帧周期、帧同步信号持续时间和极性 (polarity) 皆可配置

- 信号发出和采样的时钟缘可配置

- 支持主模式和从模式立体声I2S模式音频数据的发送和接收

- 支持主模式和从模式单声道和立体声 PCM 模式音频数据的发送和接收

- 支持主模式和从模式多声道 TDM 模式音频数据的发送和接收

- 接收和发送可以单独或同时使能

- 数据采用 DMA 操作，可通过软件开辟的缓冲区做循环存取

PCM 接口
^^^^^^^^

- 支持 16-bit 线性 PCM 编码的发送和接收

- PCM 接口帧同步信号可支持短脉冲 (1 个时钟周期) 和长脉冲 (时钟周期数可配置)

- 接口时序支持标准模式和左对齐模式

I2S 接口
^^^^^^^^

- 支持 16/24-bit 数据的发送和接收

- 支持 8kHz ~ 192kHz 采样率

- I2S 接口帧同步信号可支持低电平左声道或高电平左声道

- 接口时序支持标准模式和左对齐模式

功能描述
~~~~~~~~

AIAO 子系统通过内部 PINMUX 将内置 Audio codec、I2S 管脚和 TX/RX 模块做连接，通过软件方式根据应用需求适当配置寄存器，达到不同的连接方式。

典型应用
^^^^^^^^

典型应用如下：

- 支持 I2S 从模式对接内置 Audio Codec ADC, 或者 I2S/PCM/TDM 主/从模式对接外部 ADC 作音频采集。

- 支持 I2S 主模式对接内置 Audio Codec DAC, 或者 I2S/PCM/TDM 主/从模式对接外部 DAC 作音频播放。

.. _diagram_i2s_internal_audio_codec_interconnect:
.. figure:: ../../../../media/image84.png
	:align: center

	通过 I2S 接口与内置 Audio Codec 连接示意图

.. _diagram_i2s_external_audio_codec_interconnect_master:
.. figure:: ../../../../media/image85.png
	:align: center

	AIAO 以主模式通过 I2S 接口与外置 Audio Codec 连接示意图

.. _diagram_i2s_external_audio_codec_interconnect_slave:
.. figure:: ../../../../media/image86.png
	:align: center

	AIAO 以从模式通过 I2S 接口与外置 Audio Codec 连接示意图

功能原理
^^^^^^^^

音源经由内置或外置 Audio Codec ADC 进行 Analog-to-Digital 转换成音频数据，通过 I2S 或 PCM 接口由对接的 RX 模块接收，并经由 DMA 存入循环缓冲区，再由 CPU 取走做存储, 从而完成录音功能。TX 模块则经由 DMA 从循环缓冲区读取音频数据，通过 I2S 或 PCM 接口将音频数据传送给对接的内置或外置 Audio
Codec DAC, 进行 Digital-to-Analog 转换进行音源播放。

对接外部 I2S 接口时，支持的 I2S 时序如图表 :ref:`diagram_i2s_inf_timesequence`。

.. _diagram_i2s_inf_timesequence:
.. figure:: ../../../../media/image87.png
	:align: center

	I2S 接口时序

图表 :ref:`diagram_i2s_inf_timesequence` 以音频数据宽度 24-bit 为例，数据采用 MSB First 方式传输, MSB 相对 LRCK 信号延迟一个 BCLK 周期，数据和 LRCK 信号使用 BCLK 的下降缘发出，在 BCLK 的上升缘采样 (tx_sample_edge = 0, rx_sample_edge = 1)。

对接外部 PCM 接口时，支持 PCM 标准时序和数据左对齐时序，标准模式时序如图表 :ref:`diagram_pcm_inf_standard_timesequence`, 左对齐模式时序如图表 :ref:`diagram_pcm_inf_leftalign_timesequence`。

.. _diagram_pcm_inf_standard_timesequence:
.. figure:: ../../../../media/image88.png
	:align: center

	PCM 接口标准模式时序

图表 :ref:`diagram_pcm_inf_standard_timesequence` 以立体声音频数据宽度 16-bit 为例，数据采用 MSB First 方式传输, MSB 相对 LRCK 信号延迟一个 BCLK 周期，数据和 LRCK 信号使用 BCLK 的下降缘发出，在 BCLK 的上升缘采样 (tx_sample_edge = 0, rx_sample_edge = 1)。

.. _diagram_pcm_inf_leftalign_timesequence:
.. figure:: ../../../../media/image89.png
	:align: center

	PCM 接口左对齐模式时序

左对齐模式时，数据和 LRCK 信号在同拍开始发出。

工作方式
~~~~~~~~

AIAO 内部集成的 Audio Codec 与外部通过 I2S 接口对接的 Audio Codec 能通过软件配置同时工作，连接方式如图 :ref:`diagram_i2s_internal_audio_codec_interconnect`, :ref:`diagram_i2s_external_audio_codec_interconnect_master` 和 :ref:`diagram_i2s_external_audio_codec_interconnect_slave`。软件根据应用需要在使能数据传输前，需优先配置 AIAO 子系统寄存器 i2s_tdm_sclk_in_sel, i2s_tdm_fs_in_sel, i2s_tdm_sdi_in_sel, i2s_tdm_sdo_out_sel，以连接各接口与对应操作的 TX/RX 模块 (I2S_TDM_0~I2S_TDM_3)。

时钟门控及时钟配置
^^^^^^^^^^^^^^^^^^

若 AIAO 操作在主模式，必须先将做为 MCLK/BCLK 时钟来源的 TX/RX 模块寄存器 maste_mode 设为 1, 视采样率配置分频寄存器 I2S_CLK_CTRL1(mclk_div, bclk_div)，再将寄存器 I2S_CLK_CTRL0(aud_en) 设为 1, 打开时钟门控。

软复位
^^^^^^

AIAO 集成的 4 个 TX/RX 模块皆有独立的软复位，当使能 TX/RX 模块进行数据传输前，必须先配置寄存器 FIFO_RESET 和 I2S_RESET 进行软复位。

AIAO 寄存器概览
~~~~~~~~~~~~~~~

AIAO 子系统寄存器概览如表格 :ref:`table_aiao_registers_overview` 所示。

.. include:: ./aiao_registers_overview.table.rst

I2S_TDM_0 ~ I2S_TDM_3 模块寄存器概览如表格 :ref:`table_i2s_tdb_registers_overview` 所示。

.. include:: ./i2s_tdb_registers_overview.table.rst

AIAO 寄存器描述
~~~~~~~~~~~~~~~

AIAO 子系统寄存器描述
^^^^^^^^^^^^^^^^^^^^^

.. include:: ./aiao_subsystem_registers_description.table.rst

I2S_TDM 模块寄存器描述
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ./i2s_tdm_module_registers_description.table.rst
