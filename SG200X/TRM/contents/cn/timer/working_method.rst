工作方式 
---------

初始化
~~~~~~

- 步骤 1: 写 TimerNLoadCount (N=1~8) 寄存器，为 Timer 载入计数初值。

- 步骤 2: 设置 TimerNControlReg[2:0] (N=1~8) 寄存器，选择 Timer 计数模式，屏蔽 Timer 中断，启动 Timer 开始计数。

中断处理
~~~~~~~~

定时器产生中断时，操作步骤如下：

- 步骤 1: 读 TimerNEOI (N=1~8) 寄存器，清除 TimerN 中断。

- 步骤 2: 执行等待该中断的进程。

- 步骤 3: 进程完成后，恢复执行执行被中断的程序。

时钟选择
~~~~~~~~

系统 Timer 可选 25MHz /32KHz 计数时钟。使用 reg_timer_clk_sel 做选择。

