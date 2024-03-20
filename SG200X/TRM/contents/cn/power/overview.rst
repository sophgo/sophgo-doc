概述
----

Power Domain
~~~~~~~~~~~~

芯片支持两种主要的电源 Domain。

- Active Domain

- No-die Domain

Active Domain
^^^^^^^^^^^^^

即普通的 SoC 供电方式。

No-die Domain
^^^^^^^^^^^^^

针对此 Domain 需要提供 VDDIO_RTC 电源 (VDDIO_SD1 视情况)。

在 SoC 内部，该 power domain 由一个称之为 RTCSYS 的子系统实现。

.. _diagram_8051_block:
.. figure:: ../../../../media/image15.png
	:align: center

	RTCSYS 子系统架构

RTCSYS 子系统内部又分成两个 sub power domain: AO (Always-On) domain 和 MCU domain ( VDDC_SW_MCU 区域)。系统可以通过寄存器来选择关闭 MCU 所属 power domain 来达到省电需求。具体参考 :ref:`section_8051_power_domain_control` 章节。

在系统休眠状态下, 可以通过 MCU 处理中断并且通过配置寄存器唤醒系统, 也可以通过 I2C/UART 与外部装置沟通。

RTCSYS 子系统具体组成如下:

- AO (Always-On) domain

  - 1 组 WDT, 用于系统发生异常情况下, 于一定时间后发出中断或复位信号，以中断或复位整个系统。相关控制寄存器参考 :ref:`section_wdt_register_overview` 章节的 RTCSYS_WDT 部分。

  - RTC (Real Time Clock), 详细介绍参考 :ref:`section_rtc` 章节。

  - 1 组中断控制器，用于管理中断来源 (ictrl)。具体介绍参考 :ref:`section_8051_interrupt` 章节。

  - 1 组 GPIO, 相关控制寄存器参考 :ref:`section_gpio_register_overview` 章节的 RTCSYS_GPIO 部分。 

  - 1 组 SARADC, 相关控制寄存器参考 :ref:`section_saradc_register_overview` 章节的 RTCSYS_SARADC 部分。

  - 1 组 IRRX, 相关控制寄存器参考 :ref:`section_irrx_register_overview` 章节。

- MCU domain

  - 一个 8051 微处理器 (MCU), 详细介绍参考 :ref:`section_8051` 章节。

  - 8KB 空间 AHB SRAM, 可被 8051 当成指令 TCM 或暂存数据。

  - 2 组 32bit 计数器，用作定时、计数功能, 可以供应用程序实现定时和计数，也可以供操作系统实现系统时钟。

  - 1 组片外 SPINOR 控制。

  - 2 组 Mailbox, 让 ACPU 和 8051 可以互相沟通。具体介绍参考 :ref:`section_8051_mailbox` 章节。

  - 1 组 I2C, 相关控制寄存器参考 :ref:`section_i2c_register_overview` 章节的 RTCSYS_I2C 部分。

  - 1 组 UART, 相关控制寄存器参考 :ref:`section_uart_register_overview` 章节的 RTCSYS_UART 部分。

电源工作模式
~~~~~~~~~~~~

在 Power Domain 的基础上，芯片支持两种主要的电源工作模式：

- MCU-Only (32k-less) Mode: 

  仅 No-die Domain 工作。在这个 No-die domain 里有一个 MCU 的小系统, 有自己的 clock, timer, uart, i2c, gpio, adc 等外设，能够取代 SoC 外置的 MCU。No-die Domain 中的 MCU 能够在收到及过滤外部输入后, 唤醒主系统回到 Active Mode。

  系统中有校准过的 oscillator 可以快速醒来, 快速睡着。以进一步节省每次被唤醒所使用的功耗.

  MCU 在 Idle 状态时，功耗约为 200uA。

- Active Mode

  Active mode 是芯片完全醒来的工作的状态。此时只要供电正常, No-die Domain 和 Active Domain 中的设备都正常工作。但仍有其他如 dynamic frequency scalling 或是 dynamic clock gating 的省电技巧。
