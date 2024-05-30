PWM
---

概述
~~~~

芯片提供 4 个 PWM 控制器 PWM0、PWM1、PWM2 和 PWM3。

每个控制器提供 4 路独立的 PWM 信号输出。它们是：

- PWM0 包括 PWM[0], PWM[1], PWM[2], PWM[3]。

- PWM1 包括 PWM[4], PWM[5], PWM[6], PWM[7]。

- PWM2 包括 PWM[8], PWM[9], PWM[10], PWM[11]。

- PWM3 包括 PWM[12], PWM[13], PWM[14], PWM[15]。

特点
~~~~

PWM 的时钟来源为 100MHz 和 148.5MHz 二选一，默认为 100MHz。

- 内部有 30-bit 计数器, 输出周期和高/低电平拍数皆可配置。

- 支持最高 50MHz (100MHz/2) 或 74.25MHz (148.5MHz/2) 输出，最低约 0.093Hz (100MHz/(2^30-1)) 或 0.138Hz (148.5MHz/(2^32-1))。

- 支持连续输出 (PWMMODE = 0) 和固定脉冲个数输出 (PWMMODE = 1) 两种模式。

- 支持 4 路 PWM 同步输出模式 (SHIFTMODE = 1), 4 路 PWM 输出可通过配置寄存器调控相差。

工作方式
~~~~~~~~

PWM 基本配置流程如下 (以 PWM[0] 为例):

1. 基于选定的时钟源，通过计算得到需输出的方波周期和低电平拍数。

2. 将对应值写入寄存器 HLPERIOD0、PERIOD0。

3. 若要操作在连续输出模式，配置 PWMMODE 为 0, 将 PWMSTART[0] 设 1 后, PWM[0] 开始输出，直到 PWMSTART[0] 设 0 后结束输出。

4. 若要操作在固定脉冲个数输出模式，配置 PWMMODE 为 1, 需输出的方波数目写入寄存器 PCOUNT0。将 PWMSTART[0] 设 1 后, PWM[0] 开始输出，达到设定的方波数后自动结束，状态寄存器 PWMDONE 由 0 转 1。

.. _diagram_pwm_continuous_mode:
.. figure:: ../../../../media/image133.png
	:align: center

	PWM Continuous mode

.. _diagram_pwm_pulse_count_mode:
.. figure:: ../../../../media/image134.png
	:align: center

	PWM Pulse count mode

例如：要输出一个频率为 1MHz, 低电平占比 75%，脉冲个数为 16 的波形

1. 使用默认 100MHz 时钟源，周期数 (PERIOD0) 配置为 100MHz / 1MHz = 100, 低电平数 (HLPERIOD0) 配置为 100 x 75% = 75。脉冲数 (PCOUNT0) 配置为 16。

2. PWMSTART[0] 写 1 后开始输出波形。

3. 读取寄存器 PWMDONE[0] 直到值为 1, 表示输出完成。

4. 可读取寄存器 PULSECOUNT0, 确认输出脉冲数状态值。

若要再次使能 PWM, 需要先将 PWMSTART[0] 写 0 再写 1, 以将计数器与状态寄存器复位。

当 4 路 PWM 要操作在同步输出模式时，首先配置 SHIFTMODE 为 1, 流程如下:

1. 配置 HLPERIOD0/PERIOD0, HLPERIOD1/PERIOD1, HLPERIOD2/PERIOD2, HLPERIOD3/PERIOD3为相同值。

2. 依 4 路方波波形需要错开的 phase 差，配置适当值到寄存器 SHIFTCOUNT0, SHIFTCOUNT1, SHIFTCOUNT2, SHIFTCOUNT3。

3. 配置 PWMSTART[3:0] 为 4'hF, 并将 SHIFTSTART 设 1, 4 路的计数器同时开始计数，并在计数器值等于 SHIFTCOUNTn 时输出第 n 路的 PWM 波形。

.. _diagram_pwm_continuous_shift_mode:
.. figure:: ../../../../media/image135.png
	:align: center

	PWM Continuous Shift Mode

例如：要同时输出 4 路频率皆为 1KHz, 低电平占比 75% 的方波，每路波形依序错开 1/4 周期

1. 使用默认 100MHz 时钟源，周期数配置为 100MHz / 1KHz = 100,000, 低电平数配置为 100,000 x 75% = 75,000。

2. 配置 SHIFTCOUNT0 = 0, SHIFTCOUNT1 = 100,000 x 1/4 = 25,000, SHIFTCOUNT2 = 100,000 x 2/4 = 50,000, SHIFTCOUNT3 = 100,000 x 3/4 = 75,000。

3. PWMSTART[3:0] 设为 4'hF, 并将 SHIFTSTART 设 1, 4 路 PWM 依序输出第一个脉冲。

将 SHIFTSTART 设 0 后结束输出，读取寄存器 PWMDONE[3:0] 直到值为 4'hF, 表示 4 路皆输出完成。

PWM 寄存器概览
~~~~~~~~~~~~~~

PWM 寄存器概览如表格 :ref:`table_pwm_register_overview` 所示，这里以 PWM0 控制器为例，其他 3 个控制器类似。

.. include:: ./pwm_registers_overview.table.rst

PWM 寄存器描述
~~~~~~~~~~~~~~

以 PWM0 控制器为例，其他 3 个控制器类似。

.. include:: ./pwn_registers_description.table.rst
