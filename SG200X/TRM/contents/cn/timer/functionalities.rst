功能描述 
---------

Timer 基于一个 32bit 减法计数器。计数器的值在每个计数时钟的上升沿减 1。当计数值递减到零，Timer 将产生一个中断。

Timer 有以下 2 种计数模式：

-  自由运行模式: 定时器持续计数，当计数值减到 0 时又自动回转到其最大值，并继续计数。计数长度最大值为 0xFFFF_FFFF。

-  用户定义计数模式: 定时器持续计数，当计数值减到 0 时从 TimerNLoadCount (N=1~8) 寄存器中再次载入初值并继续计数。

对定时器载入计数初值的方法如下：

通过写 TimerNLoadCount (N=1~8) 寄存器可对定时器载入计数初值。

