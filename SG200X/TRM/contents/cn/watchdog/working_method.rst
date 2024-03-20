工作方式
--------

计数时钟频率配置
~~~~~~~~~~~~~~~~

WatchDog 计数时钟为 25MHz/32KHz 时钟。使用 reg_wdt_clk_sel 做选择。

系统初始化配置
~~~~~~~~~~~~~~

系统上电复位后 WatchDog 计数器处于停止计数状态，在系统初始化过程中需要将 WatchDog 初始化并启动其运行。WatchDog 的初始化过程如下：

- 步骤 1: 写寄存器 WDT_TORR, 设置 WatchDog 计数初值。

- 步骤 2: 写寄存器 WDT_CR[1]，设置 WatchDog 计数超时响应模式。

- 步骤 3: 写寄存器 WDT_CR[0]，启动 WatchDog 计数。

中断处理过程
~~~~~~~~~~~~

系统收到 WatchDog 发出的中断后，应及时清除其中断状态。

WatchDog 中断处理的过程如下：

- 步骤 1: 读寄存器 WDT_EOI, 清除 WatchDog 的中断状态。

- 步骤 2: 向寄存器 WDT_CRR 写入 0x76, 重启 WatchDog。

关闭 WatchDog
~~~~~~~~~~~~~

向寄存器 WDT_CR[0] 写入 0 或 1 控制 WatchDog的状态:

-  0: WDT 关闭。

-  1: WDT 开启。启动后只有系统复位能够使 WDT 关闭。

