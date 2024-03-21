GPIO
----

系统包括 4 组 Active Domain 下的 GPIO (General Purpose Input/Output) , GPIO0 ~ GPIO3 和 1 组 No-die Domain 下的 GPIO, RTCSYS_GPIO。每组 GPIO 提供 32 个可编程的输入输出管脚。

注：本手册中也经常使用 GPIOA 代替 GPIO0, GPIOB 代替 GPIO1, GPIOC 代替 GPIO2, GPIOD 代替 GPIO3。

每一个管脚的方向可以任意设置为输入或者输出, 用于生成特定应用的输出信号或收集特定应用的输入信号。设置为输入管脚时，GPIO 可用作中断源；设置为输出管脚时，每一个 GPIO 都可以独立地输出 0 或 1。

GPIO 可以根据输入信号的电平或跳变值产生可屏蔽的中断。GPIOx_INTR_FLAG (x = 0 ~ 3) 信号给中断控制器一个指示，表示有中断发生。

特点
~~~~

每一个管脚的方向可以任意设置为输入或者输出。

-  设置为输入管脚时, GPIO 可用作中断源。

-  设置为输出管脚时，每一个 GPIO 都可以独立地输出 0 或 1。


工作方式
~~~~~~~~

接口复位
^^^^^^^^

在芯片上电或系统复位时, 4 个 GPIO 模块会同时被复位, GPIO 管脚在复位之后默认处于输入状态。

通用输入输出
^^^^^^^^^^^^

每个管脚可以任意设置为输入或者输出，步骤如下：

- 步骤 1: 配置寄存器 GPIO_SWPORTA_DDR, 设置 GPIO 是作为输入还是输出。

- 步骤 2: 配置成输入管脚时，读取 GPIO_EXT_PORTA 寄存器可查看输入信号值；配置成输出管脚时，向 GPIO_SWPORTA_DR 寄存器写入输出值可控制 GPIO 输出电平。

中断操作
^^^^^^^^

每一个 GPIO 都可以用作中断源，通过 GPIO_INTEN 等 9 个寄存器进行控制。通过这些寄存器用户可以选择中断来源、中断电平极性以及边沿触发特性。

多个 GPIO 中断同时发生时，将会统一汇集成一个中断进行上报 ( 4 组 GPIO 各自会有一个汇集中断旗标上报) 。

中断源的特性和中断触发类别由 GPIO_INTTYPE_LEVEL、GPIO_INT_POLARITY、GPIO_INTMASK、GPIO_DEBOUNCE、GPIO_LS_SYNC 五个寄存器决定。

中断的原始状态和屏蔽后的状态通过 GPIO_RAW_INTSTATUS 和 GPIO_INTSTATUS读取。通过设置 GPIO_PORTA_EOI 可控制中断状态的清除。

每一个 GPIO 都可以支持中断，设置步骤如下：

- 步骤 1: 配置寄存器 GPIO_INTTYPE_LEVEL, 选择电平触发或边沿触发。

- 步骤 2: 配置寄存器 GPIO_INT_POLARITY, 选择低电平/高电平触发和下降沿/上升沿触发。

- 步骤 3: 对寄存器 GPIO_PORTA_EOI 写入 0xFFFFFFFF, 清除中断。

- 步骤 4: 配置 GPIO_INTEN 寄存器；使能 GPIO 管脚中断功能。

.. _section_gpio_register_overview:

GPIO 寄存器概览
~~~~~~~~~~~~~~~

芯片包括 4 组 Active Domain 下的 GPIO 和 1 组 No-die Domain 下的 GPIO。基地址如表格 :ref:`table_gpio_module_baseaddress` 所示。

.. 这个表比较小，所以不单独放文件 include

.. _table_gpio_module_baseaddress:
.. table:: Base addresses of GPIO modules
	:widths: 1 1

	+----------------------------------+----------------------------------+
	| GPIO Module                      | Base Address                     |
	+==================================+==================================+
	| GPIO0                            | 0x03020000                       |
	+----------------------------------+----------------------------------+
	| GPIO1                            | 0x03021000                       |
	+----------------------------------+----------------------------------+
	| GPIO2                            | 0x03022000                       |
	+----------------------------------+----------------------------------+
	| GPIO3                            | 0x03023000                       |
	+----------------------------------+----------------------------------+
	| RTCSYS_GPIO                      | 0x05021000                       |
	+----------------------------------+----------------------------------+

表格 :ref:`table_gpio0_registers_overview` 是第 1 组 GPIO 模块 (GPIO0) 寄存器的偏移地址以及定义, 其他组的 GPIO 具有相同的寄存器定义。

.. 这个表比较小，所以不单独放文件 include

.. _table_gpio0_registers_overview:
.. table:: GPIO Registers Overview
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| GPIO_SWPORTA_DR      | 0x000   | Port A data register               |
	+----------------------+---------+------------------------------------+
	| GPIO_SWPORTA_DDR     | 0x004   | Port A data direction register     |
	+----------------------+---------+------------------------------------+
	| GPIO_INTEN           | 0x030   | Interrupt enable register          |
	+----------------------+---------+------------------------------------+
	| GPIO_INTMASK         | 0x034   | Interrupt mask register            |
	+----------------------+---------+------------------------------------+
	| GPIO_INTTYPE_LEVEL   | 0x038   | Interrupt level register           |
	+----------------------+---------+------------------------------------+
	| GPIO_INT_POLARITY    | 0x03c   | Interrupt polarity register        |
	+----------------------+---------+------------------------------------+
	| GPIO_INTSTATUS       | 0x040   | Interrupt status of Port A         |
	+----------------------+---------+------------------------------------+
	| GPIO_RAW_INTSTATUS   | 0x044   | Raw interrupt status of Port A     |
	|                      |         | (pre-masking)                      |
	+----------------------+---------+------------------------------------+
	| GPIO_DEBOUNCE        | 0x048   | Debounce enable register           |
	+----------------------+---------+------------------------------------+
	| GPIO_PORTA_EOI       | 0x04c   | Port A clear interrupt register    |
	+----------------------+---------+------------------------------------+
	| GPIO_EXT_PORTA       | 0x050   | Port A external port register      |
	+----------------------+---------+------------------------------------+
	| GPIO_LS_SYNC         | 0x060   | Level-sensitive synchronization    |
	|                      |         | enable register                    |
	+----------------------+---------+------------------------------------+

GPIO 寄存器描述
~~~~~~~~~~~~~~~

.. include:: ./gpio_registers_description.table.rst
