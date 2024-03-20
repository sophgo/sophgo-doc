Temperature Sensor
------------------

Overview
~~~~~~~~

Because the chip junction temperature is too high, it may cause thermal run-away and cause permanent damage. Therefore, the chip needs to be temperature controlled.

The first stage is software behavior. The temperature sensor can automatically detect whether the temperature exceeds a specific temperature at regular intervals and issue an overheating interrupt. After the software receives the overheating interrupt, it can reduce power consumption and temperature by limiting the frequency or voltage of high-power modules, starting fans, etc. the goal of. If the temperature returns to a safe range, the restrictions are lifted.

The second stage is hardware behavior. If the temperature continues to rise after the software is activated, the hardware will intervene to perform thermal shut-down emergency response. However, this function is turned off by default. You need to set the relevant settings after starting the software and then enable it.

This chip has two built-in temperature sensors, and the CPU can periodically monitor the chip temperature. When the chip is overheated and unresponsive, the power management module can be triggered to shut down and reset the system to avoid the risk of overheating.

Way of Working
~~~~~~~~~~~~~~

- Single measurement time configuration: reg_tempsen_accsel = 1 (1024T) configuration, the required single measurement time is (1/(25M/12)*(1024+2+64) ~ 523.2us.

- Cycle measurement time configuration: reg_tempsen_auto_prediv is defaulted to 24, making each unit of reg_tempsen_auto_cycle 1us. The period between two measurement times needs to be configured with reg_tempsen_auto_cycle greater than 524. For example, to measure once per second, configure reg_tempsen_auto_cycle = 1000000.

- Measurement channel configuration: If reg_tempsen_sel = 3 is configured, two temperature sensors will be triggered to measure simultaneously.

- Configure high and low temperature monitoring temperature: Configure the temperature tempsen_chx_temp_th that triggers high temperature alarm and low temperature recovery.

- Configuration interruption.

- Enable the temperature sensor for measurement: configure reg_tempsen_en = 1 to perform measurement and wait for interrupt.

.. include:: ../../contents-share/peripherals/temperature_interrupt_description.table.rst

.. _diagram_temperature_measure:
.. figure:: ../../../../media/image132.png
	:align: center

	Temperature measurement time, count and interrupt occurrence relationship diagram

- View temperature measurement results: sta_tempsen_chX_result records the previously completed temperature measurement results, sta_tempsen_chX_max_result records the maximum temperature value ever measured, tempsen_chX_temp_th_cnt records the number of consecutive high and low temperatures.

- Configure the overheat protection temperature reg_tempsen_overheat_th, overheat reset request countdown time reg_tempsen_overheat_cycle and enable reg_overheat_reset_en.

Refer to the RTC register chapter again to configure the RTC registers hw_thm_shdn_en, RTC_EN_THM_SHDN, RTC_THM_SHDN_AUTO_REBOOT to enable overheating to trigger power off or restart. When overheating occurs, the tempsensor controller will first issue an interrupt and start counting down. When sta_tempsen_overheat_countdown is equal to 1, the RTC's power-off protection request will be triggered. If the software intervenes before and performs temperature control, you can configure reg_overheat_reset_clr to clear the countdown. However, when the next measurement result is still overheated, the overheat protection interrupt will still be triggered and countdown again.

Temperature sensor Register Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/peripherals/temperature_registers_overview.table.rst

Temperature sensor Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/peripherals/temperature_registers_description.table.rst
