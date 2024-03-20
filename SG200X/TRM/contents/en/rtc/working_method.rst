Way of working
--------------

Count clock frequency
~~~~~~~~~~~~~~~~~~~~~

RTC second counter, the maximum counting time is:

    2^32 = 49710 days = 136 years

RTC reset
~~~~~~~~~

As a chip power-on and power-off control unit, RTC itself cannot be soft-reset alone. In addition to the POR for the first power-on, it can support a forced full-chip reset (including RTC) by pressing the RSTN button in case of an abnormality. After the RSTN button is released, all RTC registers are restored to their default values, and the state machine returns to its initial state. If the state machine detects that the battery voltage is in a normal state, it starts to complete the chip power-on process according to the default value sequence and releases the system reset signal.

RTC initialization
~~~~~~~~~~~~~~~~~~

After the chip is powered on for the first time, the system needs to initialize the RTC. However, before initialization, the 32KHz oscillator clock and second time need to be calibrated. The calibration module uses a 25MHz crystal oscillator clock to sample a 32KHz clock, and cooperates with the software process operation. In the coarse tune mode, a 32KHz clock cycle is sampled with a 25MHz crystal oscillator clock. The software adjusts the configuration register RTC_ANA_CALIB[8:0] according to the number of sampling pulses, speeding up or slowing down the 32KHz oscillation clock cycle time to improve 32KHz clock accuracy. After completing the coarse adjustment, you can further enter the fine tune mode. The default value is to sample 256 32KHz clock cycles with a 25MHz crystal oscillator clock. The software averages the number of sampled pulses to obtain the number of pulses required for counting the 32KHz clock in 1 second. And write the value to the register RTC_SEC_PULSE_GEN_INT, RTC_SEC_PULSE_GEN_FRAC to complete the second calibration.

The 32KHz clock coarse adjustment software process is as follows:

1. Set register RTC_ANA_SEL_FTUNE to 0, and the initial value of RTC_ANA_CALIB is 0x100

2. The following uses the bindary search method to achieve calibration:
   
    FTUNE = RTC_ANA_CALIB; offset = 0x80

3. Set the configuration register RTC_FC_COARSE_EN to 1 and start coarse adjustment. Poll the value of RTC_FC_COARSE_TIME until it is greater than the previous read value, configure RTC_FC_COARSE_EN to 0

4. Read RTC_FC_COARSE_VALUE and obtain the count value of a 32KHz clock cycle sampled by a 25MHz clock.
   
    if (RTC_FC_COARSE_VALUE > 770) FTUNE = FTUNE + offset;

    if (RTC_FC_COARSE_VALUE < 755) FTUNE = FTUNE - offset;
   
    Write FTUNE value back to register RTC_ANA_CALIB
   
    offset = offset >> 1;

5. When the value of RTC_FC_COARSE_VALUE is between 755~770, the 32KHz clock accuracy has reached 32,768Hz ± 1%. Finish coarse adjustment. Otherwise, wait for 0.5ms and repeat steps 3 ~ 5, up to 8 times to complete.

The 32KHz clock fine adjustment calibration software process is as follows:

1. Set register RTC_SEL_SEC_PULSE to 0. Set RTC_FC_FINE_EN to 1 and start fine tuning.

2. Poll the value of RTC_FC_FINE_TIME until it is greater than the previous read value

3. Read RTC_FC_FINE_VALUE and obtain the count value of 256 32KHz clock cycles sampled by 25MHz clock.

4. The 32KHz clock frequency can be obtained by the following formula:

    Frequency = 256 / (RTC_FC_FINE_VALUE x 40ns)

    For example: 256 / (195310 x 40) = 32768.4194357

5. Take the integer part 32768, write it into the register RTC_SEC_PULSE_GEN_INT, take the decimal part 8-bit = 0.4194357 x 256 = 107, write it into the register RTC_SEC_PULSE_GEN_FRAC

6. Configure RTC_FC_FINE_EN to 0 to end fine tuning

The clock calibration process can be executed once or periodically by the software depending on the needs of the system. In addition to the software calibration process, RTC also supports hardware to perform automatic calibration periodically.

After completing the clock calibration, further initialize the RTC. Only the necessary initialization process is listed below. Most of the remaining parameter registers are only necessary to be configured when it is necessary to optimize the chip power-on and power-off or power-off timing. It is generally recommended to use the default values.

1. Configure the register RTC_POR_DB_MAGIC_KEY value to 0x5AF0 to enable POR debounce to prevent POR false triggering due to a brief voltage drop in the RTC module supply voltage. Debounce time is about 1ms.

2. Configure RTC_SET_SEC_CNTR_VALUE and set the initial value of RTC time count.

3. Write 1 to RTC_SET_SEC_CNTR_TRIG to load the initial count value into the RTC second counter.

4. Poll the RTC_SEC_CNTR_VALUE register value until the read value equals the RTC_SET_SEC_CNTR_VALUE value.

5. Configure RTC_PWR_DET_COMP[0] to 1 to enable battery low-voltage detection, and configure RTC_PWR_DET_SEL[0] to 1 to issue a low-voltage detection interrupt. When the battery voltage is lower than the threshold value, the status signal enters low level. The threshold value can be adjusted through the configuration register RTC_PWR_DET_COMP[12:8].

6. After the RTC is powered on for the first time, the register reg_rtcsys_rstn_src_sel must be configured from the default value 0 to 1 so that the RTC subsystem can remain in the working state after the chip is suspend or power-down. If the value of this register is 0, the RTC subsystem will be reset when the chip is powered off.

7. After the RTC is powered on for the first time, the register RTC_EN_AUTO_POWER_UP must be configured from the default value 1 to 0. If the default value is maintained, when the chip enters the power-down state, the RTC will automatically enter the power-on state when it detects that PWR_VBAT_DET is high level.

Analog seconds clock initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Configure RTC_MACRO_RG_DEFD = 16'hC80 (32000 clock cycles in 32KHz)

2. Configure RTC_MACRO_DA_SOC_READY to 1

3. Configure RTC_MACRO_DA_CLEAR_ALL to 1

4. Configure RTC_MACRO_DA_CLEAR_ALL to 0

5. Configure RTC_MACRO_RG_SET_T as the required Counter value

6. Configure RTC_MACRO_DA_LATCH_PASS to 1

7. Configure RTC_MACRO_DA_LATCH_PASS to 0

8. Configure RTC_MACRO_DA_SOC_READY to 0

9. Read RTC_MACRO_RO_T to get the counter value

Interrupt handling
~~~~~~~~~~~~~~~~~~

The RTC will send status signals of alarm interruption and low-voltage detection interruption. When the system receives the alarm interruption, it indicates that the scheduled time has expired, and the user can perform corresponding custom operations. Set register RTC_ALARM_ENABLE to 0 to clear the interrupt status. If you need to continue setting a new timing time, write the new value to the register RTC_ALARM_TIME and set RTC_ALARM_ENABLE to 1 again.

Sleep and wake up
~~~~~~~~~~~~~~~~~

The system software can power off the chip and enter the sleep state (suspend) by configuring the register req_suspend to 1. The configuration register RTC_EN_PWR_WAKEUP selects the source that triggers the chip wakeup. It should be noted that before configuring req_suspend, the register RTC_PG_REG must be written to 0 to allow the DDR IO to enter a constant state (retent) to avoid the DDR data to be damaged due to malfunction during power-off or power-on of the chip. When the chip wakes up, the system software must write 1 to the register RTC_PG_REG to release the protection state of the DDR IO before executing the DDR initialization process.

In addition, if you want to use buttons (PWR_ON, PWR_BUTTON, PWR_WAKEUP) to wake up, before entering the sleep state, you must first configure the relevant IO PINMUX register and lock the IO as RTC input function.

Power-Off and Powner-On
~~~~~~~~~~~~~~~~~~~~~~~

By configuring the register req_shdn to 1, the system software can make the chip including DDR power off and enter the shutdown state. The configuration register RTC_EN_PWR_UP selects the source that can trigger the chip power-on.
