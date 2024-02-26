工作方式
--------

计数时钟频率
~~~~~~~~~~~~

RTC 的秒计数器，计数最大时间为：

   2^32 = 49710 天 = 136 年

RTC 复位
~~~~~~~~

RTC 作为芯片上电、下电控制单元，本身并无法单独被软复位，除了首次上电的 POR 外，可支持在异常时，通过按键 RSTN 强制全芯片复位 (包含RTC)，RSTN 按键解除后，RTC 所有寄存器恢复为默认值，状态机也回到初始。若状态机检测到电池电压处于正常状态，则开始依默认值时序完成芯片上电流程并解除系统复位信号。

RTC 初始化
~~~~~~~~~~

在芯片第一次上电后，系统需要将 RTC 初始化。不过在初始化之前，需要先对 32KHz 振荡器时钟及秒时间进行校准。校准模块使用 25MHz 晶振时钟采样 32KHz 时钟，配合软件流程操作，在粗调 (coarse tune) 模式下，以 25MHz 晶振时钟采样一个 32KHz 时钟周期，软件依采样脉冲数调整配置寄存器 RTC_ANA_CALIB[8:0]，加快或减慢 32KHz 振荡时钟周期时间，以提高 32KHz 时钟精准度。完成粗调后可进一步进入细调 (fine tune) 模式，默认值以 25MHz 晶振时钟采样 256 个 32KHz 时钟周期，软件依采样脉冲数取平均值，可取得1秒钟计数 32KHz 时钟所需脉冲数，并将值写入寄存器 RTC_SEC_PULSE_GEN_INT、RTC_SEC_PULSE_GEN_FRAC，完成秒校准。

32KHz 时钟粗调校准软件流程如下：

1. 配置寄存器 RTC_ANA_SEL_FTUNE 为 0，RTC_ANA_CALIB 初始值为 0x100

2. 以下利用 bindary search 方式实现校准：
   
   FTUNE = RTC_ANA_CALIB; offset = 0x80

3. 配置寄存器 RTC_FC_COARSE_EN 为 1，开始粗调。轮询 RTC_FC_COARSE_TIME 的值，直到大于前一次读取值后，配置 RTC_FC_COARSE_EN 为 0

4. 读取 RTC_FC_COARSE_VALUE，取得 25MHz 时钟采样一个 32KHz 时钟周期的计数值。
   
   if (RTC_FC_COARSE_VALUE > 770) FTUNE = FTUNE + offset;

   if (RTC_FC_COARSE_VALUE < 755) FTUNE = FTUNE - offset;
   
   将 FTUNE 值写回寄存器 RTC_ANA_CALIB
   
   offset = offset >> 1;

5. 当 RTC_FC_COARSE_VALUE 的值介于 755~770 之间时，32KHz 时钟精度已达到 32,768Hz ±
   1% 之内，结束粗调。否则等待 0.5ms，重复步骤 3 ~ 5，最多重复 8 次即可完成


32KHz 时钟细调校准软件流程如下：

1. 配置寄存器 RTC_SEL_SEC_PULSE 为 0。配置 RTC_FC_FINE_EN 为 1，开始细调

2. 轮询 RTC_FC_FINE_TIME 的值，直到大于前一次读取值

3. 读取 RTC_FC_FINE_VALUE，取得 25MHz 时钟采样 256 个 32KHz 时钟周期的计数值

4. 32KHz 时钟频率可由以下算式取得：

   Frequency = 256 / (RTC_FC_FINE_VALUE x 40ns)

   例如：256 / (195310 x 40) = 32768.4194357

5. 取整数部份 32768，写入寄存器 RTC_SEC_PULSE_GEN_INT，小数部份取 8-bit = 0.4194357 x 256 = 107，写入寄存器 RTC_SEC_PULSE_GEN_FRAC

6. 配置 RTC_FC_FINE_EN 为0，结束细调

时钟校准流程可视系统需要，由软件做一次性执行或周期性执行。除了软件校准流程外，RTC也同时支持硬件周期性执行自动校准。

完成时钟校准后，进一步初始化 RTC。以下只列出必要的初始化过程，其余大部份参数寄存器，仅在需要优化芯片上下电或开关机时序时才有必要配置，一般建议使用默认值。

1. 配置寄存器 RTC_POR_DB_MAGIC_KEY 值 0x5AF0，使能 POR 去抖动 (debounce)，以防止 RTC 模块供电电压因发生短暂压降而造成 POR 误触发。去抖动时间约 1ms

2. 配置 RTC_SET_SEC_CNTR_VALUE，设置 RTC 时间计数初始值

3. 对 RTC_SET_SEC_CNTR_TRIG 写入1，将计数初始值加载到 RTC 秒计数器

4. 轮询 RTC_SEC_CNTR_VALUE 寄存器值，直到读取值等于 RTC_SET_SEC_CNTR_VALUE 值

5. 配置 RTC_PWR_DET_COMP[0] 为 1，使能电池低压检测，并配置 RTC_PWR_DET_SEL[0] 为 1，以发出低压检测中断，当电池电压低于 threshold 值，状态信号进入低电平。可通过配置寄存器 RTC_PWR_DET_COMP[12:8] 调整 threshold 值。

6. RTC 首次上电后必须將寄存器 reg_rtcsys_rstn_src_sel 由默认值 0 改配置为 1，使 RTC子系統在芯片下电后 (suspend or powerdown) 维持在工作状态。此寄存器值若为 0，则 RTC子系統会随芯片下电被复位。

7. RTC 首次上电后必须將寄存器 RTC_EN_AUTO_POWER_UP 由默认值 1 改配置为 0，若維持默认值则当芯片进入下电状态 (powerdown)，RTC 检测 PWR_VBAT_DET 为高电平就会自动进入上电状态。

模拟秒时钟初始化
~~~~~~~~~~~~~~~~

1. 配置 RTC_MACRO_RG_DEFD = 16'hC80 (32000 个 32KHz 时钟周期)

2. 配置 RTC_MACRO_DA_SOC_READY 为 1

3. 配置 RTC_MACRO_DA_CLEAR_ALL 为 1

4. 配置 RTC_MACRO_DA_CLEAR_ALL 为 0

5. 配置 RTC_MACRO_RG_SET_T 为需求 Counter 值

6. 配置 RTC_MACRO_DA_LATCH_PASS 为 1

7. 配置 RTC_MACRO_DA_LATCH_PASS 为 0

8. 配置 RTC_MACRO_DA_SOC_READY 为 0

9. 读取 RTC_MACRO_RO_T 来得到 counter 值

中断处理
~~~~~~~~

RTC 会发出报警中断及低压检测中断的状态信号，当系统收到报警中断后，表示定时时间到，用户可以执行相对应的自定义操作。将寄存器 RTC_ALARM_ENABLE 设为0可清除中断状态。如果需要继续设定新的定时时间，则将新值写入寄存器 RTC_ALARM_TIME 后，再次将 RTC_ALARM_ENABLE 设为 1。

休眠与唤醒
~~~~~~~~~~

系统软件通过配置寄存器 req_suspend 为 1，可使芯片下电进入休眠状态 (suspend)，配置寄存器 RTC_EN_PWR_WAKEUP 选择可触发芯片唤醒 (wakeup) 的来源。需注意在配置 req_suspend 之前，必需先将寄存器 RTC_PG_REG 写 0，让 DDR IO 进入恒定状态 (retent)，以避免芯片在下电或上电过程中因误动作造成 DDR 资料遭到破坏。当芯片唤醒后，系统软件必需在执行 DDR 初始化流程之前，将寄存器 RTC_PG_REG 写 1，解除 DDR IO 的保护状态。

此外若要采用按键 (PWR_ON, PWR_BUTTON, PWR_WAKEUP) 唤醒，在进入休眠状态前，必需先配置相关 IO PINMUX寄存器，将 IO 锁定为 RTC input function。

关电与上电
~~~~~~~~~~

系统软件通过配置寄存器 req_shdn 为 1，可使芯片包含 DDR 下电进入关机状态 (poweroff)，配置寄存器RTC_EN_PWR_UP 选择可触发芯片上电开机 (powerup) 的来源。

