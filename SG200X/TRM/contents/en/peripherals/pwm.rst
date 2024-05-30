PWM
---

Overview
~~~~~~~~

The chip provides 4 PWM controllers PWM0, PWM1, PWM2 and PWM3.

Each controller provides 4 independent PWM signal outputs. They are:

- PWM0 includes PWM[0], PWM[1], PWM[2], PWM[3].

- PWM1 includes PWM[4], PWM[5], PWM[6], PWM[7].

- PWM2 includes PWM[8], PWM[9], PWM[10], PWM[11].

- PWM3 includes PWM[12], PWM[13], PWM[14], PWM[15].

Features
~~~~~~~~

The PWM clock source can be selected from 100MHz or 148.5MHz, and the default is 100MHz.

- There is an internal 30-bit counter, the output period and the number of high/low level beats are configurable.

- Supports up to 50MHz (100MHz/2) or 74.25MHz (148.5MHz/2) output, and the lowest is about 0.093Hz (100MHz/(2^30-1)) or 0.138Hz (148.5MHz/(2^32-1)) .

- Supports two modes: continuous output (PWMMODE = 0) and fixed pulse number output (PWMMODE = 1).

- Supports 4-channel PWM synchronous output mode (SHIFTMODE = 1), and the phase difference of the 4-channel PWM output can be controlled through the configuration register.

Way of Working
~~~~~~~~~~~~~~

The basic configuration process of PWM is as follows (taking PWM[0] as an example):

1. Based on the selected clock source, calculate the square wave period and low-level beat number to be output.

2. Write the corresponding values to registers HLPERIOD0 and PERIOD0.

3. To operate in continuous output mode, configure PWMMODE to 0, set PWMSTART[0] to 1, and PWM[0] starts to output until PWMSTART[0] is set to 0 to end the output.

4. If you want to operate in the fixed pulse number output mode, configure PWMMODE as 1, and write the number of square waves to be output into the register PCOUNT0. After setting PWMSTART[0] to 1, PWM[0] starts to output and ends automatically after reaching the set square wave number, and the status register PWMDONE changes from 0 to 1.

.. _diagram_pwm_continuous_mode:
.. figure:: ../../../../media/image133.png
	:align: center

	PWM Continuous mode

.. _diagram_pwm_pulse_count_mode:
.. figure:: ../../../../media/image134.png
	:align: center

	PWM Pulse count mode

For example: To output a waveform with a frequency of 1MHz, a low level ratio of 75%, and a pulse number of 16

1. Using the default 100MHz clock source, the period number (PERIOD0) is configured as 100MHz / 1MHz = 100, and the low level number (HLPERIOD0) is configured as 100 x 75% = 75. The number of pulses (PCOUNT0) is configured as 16.

2. Write 1 to PWMSTART[0] to start outputting the waveform.

3. Read the register PWMDONE[0] until the value is 1, indicating that the output is completed.

4. The register PULSECOUNT0 can be read to confirm the output pulse number status value.

To enable PWM again, you need to write 0 and then 1 to PWMSTART[0] to reset the counter and status register.

When the 4-channel PWM is to operate in synchronous output mode, first configure SHIFTMODE to 1. The process is as follows:

1. Configure HLPERIOD0/PERIOD0, HLPERIOD1/PERIOD1, HLPERIOD2/PERIOD2, HLPERIOD3/PERIOD3 to the same value.

2. According to the phase difference that the four square wave waveforms need to be staggered, configure appropriate values into the registers SHIFTCOUNT0, SHIFTCOUNT1, SHIFTCOUNT2, and SHIFTCOUNT3.

3. Configure PWMSTART[3:0] to 4'hF, and set SHIFTSTART to 1. The 4-channel counter will start counting at the same time, and output the n-th PWM waveform when the counter value is equal to SHIFTCOUNTn.

.. _diagram_pwm_continuous_shift_mode:
.. figure:: ../../../../media/image135.png
	:align: center

	PWM Continuous Shift Mode

For example: To output 4 channels of square waves with a frequency of 1KHz and a low level of 75% at the same time, the waveforms of each channel should be staggered by 1/4 cycle.

1. Using the default 100MHz clock source, the cycle number is configured as 100MHz / 1KHz = 100,000, and the low level number is configured as 100,000 x 75% = 75,000.

2. Configure SHIFTCOUNT0 = 0, SHIFTCOUNT1 = 100,000 x 1/4 = 25,000, SHIFTCOUNT2 = 100,000 x 2/4 = 50,000, SHIFTCOUNT3 = 100,000 x 3/4 = 75,000.

3. Set PWMSTART[3:0] to 4'hF, and set SHIFTSTART to 1, and the 4 PWM channels will output the first pulse in sequence.

Set SHIFTSTART to 0 to end the output, and read the register PWMDONE[3:0] until the value is 4'hF, which means that all 4 channels are output.

PWM Register Overview
~~~~~~~~~~~~~~~~~~~~~

An overview of the PWM registers is shown in table :ref:`table_pwm_register_overview`. Here take PWM0 controller as an example, the other 3 controllers are similar.

.. include:: ../../contents-share/peripherals/pwm_registers_overview.table.rst

PWM Register Description
~~~~~~~~~~~~~~~~~~~~~~~~

Here take PWM0 controller as an example, the other 3 controllers are similar.

.. include:: ../../contents-share/peripherals/pwn_registers_description.table.rst
