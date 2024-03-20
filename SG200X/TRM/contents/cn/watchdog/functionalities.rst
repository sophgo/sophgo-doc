功能描述
--------

系统通过系统总线给 WatchDog 配置寄存器参数值。WatchDog 定时发出 WDT_INTR 中断请求给系统，并在系统没有响应中断的情况下（如：死机），发出 WDT_SYS_RST 复位信号，使系统复位，达到监控系统运行的目的。

应用框图
~~~~~~~~

.. _diagram_watchdog_block:
.. figure:: ../../../../media/image13.png

	WatchDog 应用框图

功能原理
~~~~~~~~

WatchDog 的计数初值由寄存器 WDT_TORR 载入，运行基于 1个 32bit 减法计数器。

在 WatchDog 时钟使能情况下，计数值在每个计数时钟的上升沿减 1。当计数值递减到 0, WatchDog 将产生一个中断。然后在下一个计数时钟上升沿，计数器又从寄存器 WDT_TORR 中重新载入计数初值，开始递减计数。

如果计数器的计数值第二次计数递减到 0 时, CPU还没有清除 WatchDog 中断，则 WatchDog 将发出复位信号WDT_SYS_RST, 计数器停止计数。

用户可以通过设置寄存器 WDT_CR[1] 决定是否在计数器的计数值第一次计数递减到 0 时立刻发出复位信号 WDT_SYS_RST。

