工作方式
--------

.. _section_8051_power_domain_control:

Power domain 控制流程
~~~~~~~~~~~~~~~~~~~~~

RTCSYS 子系统内分成两个 power domain: AO (Always-On) domain 和 MCU domain。可以通过配置寄存器对 MCU domain进行上下电流程, 流程如下:

MCU power_off:

1. 软复位寄存器 = 0

2. 配置寄存器 reg_mcu_iso_en = 1

3. 配置寄存器 reg_mcu_pwr_req = 0

MCU power_on:

1. 配置寄存器 reg_mcu_pwr_req = 1

2. 轮询寄存器 reg_mcu_pwr_ack = 1

3. 配置寄存器 reg_mcu_iso_en = 0

4. 软复位寄存器 = 1

8051 初始化
~~~~~~~~~~~

8051 在系统初始是处于复位状态, 使用 8051 可以透过 ACPU 来完成下面的软件流程:

1. 8051 复位状态处于复位状态 (寄存器 reg_soft_rstn_mcu = 0)。

2. 配置寄存器 reg_mcu_rom_addr_size 来决定指令 TCM size。

3. 配置寄存器 reg_51irom_ioffset 来决定 TCM 执行在 AHB SRAM 上的位置。

4. 配置寄存器 reg_soft_rstn_mcu =1 解除 8051 复位状态。

.. _section_8051_interrupt:

中断处理
~~~~~~~~

8051 可以透过 int0_n, int1_n 接口接收外部电平触发中断, int0_n/int1_n 分别从 ictl (中断控制) 和配置寄存器 reg_51_int1_src_mask 来选择输出中断信号给 8051。

.. include:: ./8051_interrupts.table.rst

.. _section_8051_mailbox:

MAILBOX
~~~~~~~

Mailbox 提供 2 组 spinlock 功能栏位，和 4 组 32bit 信息栏位，让 ACPU/8051 可以相互传输信息。
