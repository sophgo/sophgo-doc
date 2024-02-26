HLPERIOD0
^^^^^^^^^

.. _table_hlperiod0:
.. table:: HLPERIOD0, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 29:0 | HLPERIOD0            | R/W   | PWM0 Number of low     | 0x1  |
	|      |                      |       | level taps (in clk_pwm)|      |
	|      |                      |       |                        |      |
	|      |                      |       | When POLARITY[0] is 0, |      |
	|      |                      |       | this value is the      |      |
	|      |                      |       | number of low level    |      |
	|      |                      |       | beats, when POLARITY[0]|      |
	|      |                      |       | is 1, this value is the|      |
	|      |                      |       | number of high level   |      |
	|      |                      |       | beats.                 |      |
	+------+----------------------+-------+------------------------+------+

PERIOD0
^^^^^^^

.. _table_period0:
.. table:: PERIOD0, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 29:0 | PERIOD0              | R/W   | PWM0 Square wave period| 0x2  |
	|      |                      |       | beats (in clk_pwm)     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note The PERIOD value  |      |
	|      |                      |       | must be greater than   |      |
	|      |                      |       | the HLPERIOD value.    |      |
	+------+----------------------+-------+------------------------+------+

HLPERIOD1
^^^^^^^^^

.. _table_hlperiod1:
.. table:: PERIOD0, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 29:0 | HLPERIOD1            | R/W   | PWM1 Number of low     | 0x1  |
	|      |                      |       | level taps (in clk_pwm)|      |
	|      |                      |       |                        |      |
	|      |                      |       | When POLARITY[1] is 0, |      |
	|      |                      |       | this value is the      |      |
	|      |                      |       | number of low level    |      |
	|      |                      |       | beats, when POLARITY[1]|      |
	|      |                      |       | is 1, this value is the|      |
	|      |                      |       | number of high level   |      |
	|      |                      |       | beats.                 |      |
	+------+----------------------+-------+------------------------+------+

PERIOD1
^^^^^^^

.. _table_period1:
.. table:: PERIOD1, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 29:0 | PERIOD1              | R/W   | PWM1 Square wave period| 0x2  |
	|      |                      |       | beats (in clk_pwm)     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note The PERIOD value  |      |
	|      |                      |       | must be greater than   |      |
	|      |                      |       | the HLPERIOD value.    |      |
	+------+----------------------+-------+------------------------+------+

HLPERIOD2
^^^^^^^^^

.. _table_HLPERIOD2:
.. table:: PERIOD1, Offset Address: 0x010
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 29:0 | HLPERIOD2            | R/W   | PWM2 Number of low     | 0x1  |
	|      |                      |       | level taps (in clk_pwm)|      |
	|      |                      |       |                        |      |
	|      |                      |       | When POLARITY[2] is 0, |      |
	|      |                      |       | this value is the      |      |
	|      |                      |       | number of low level    |      |
	|      |                      |       | beats, when POLARITY[2]|      |
	|      |                      |       | is 1, this value is the|      |
	|      |                      |       | number of high level   |      |
	|      |                      |       | beats.                 |      |
	+------+----------------------+-------+------------------------+------+

PERIOD2
^^^^^^^^^

.. _table_period2:
.. table:: PERIOD2, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 29:0 | PERIOD2              | R/W   | PWM2 Square wave period| 0x2  |
	|      |                      |       | beats (in clk_pwm)     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note The PERIOD value  |      |
	|      |                      |       | must be greater than   |      |
	|      |                      |       | the HLPERIOD value.    |      |
	+------+----------------------+-------+------------------------+------+

HLPERIOD3
^^^^^^^^^

.. _table_hlperiod3:
.. table:: HLPERIOD3, Offset Address: 0x018
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 29:0 | HLPERIOD3            | R/W   | PWM3 Number of low     | 0x1  |
	|      |                      |       | level taps (in clk_pwm)|      |
	|      |                      |       |                        |      |
	|      |                      |       | When POLARITY[3] is 0, |      |
	|      |                      |       | this value is the      |      |
	|      |                      |       | number of low level    |      |
	|      |                      |       | beats, when POLARITY[3]|      |
	|      |                      |       | is 1, this value is the|      |
	|      |                      |       | number of high level   |      |
	|      |                      |       | beats.                 |      |
	+------+----------------------+-------+------------------------+------+

PERIOD3
^^^^^^^^^

.. _table_PERIOD3:
.. table:: HLPERIOD3, Offset Address: 0x01c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 29:0 | PERIOD3              | R/W   | PWM3 Square wave period| 0x2  |
	|      |                      |       | beats (in clk_pwm)     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note The PERIOD value  |      |
	|      |                      |       | must be greater than   |      |
	|      |                      |       | the HLPERIOD value.    |      |
	+------+----------------------+-------+------------------------+------+

POLARITY
^^^^^^^^^

.. _table_polarity:
.. table:: POLARITY, Offset Address: 0x040
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 3:0  | POLARITY             | R/W   | PWM0~3 signal polarity | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | [n] = 0: PWMn          |      |
	|      |                      |       | Default is low         |      |
	|      |                      |       | level output           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [n] = 1: PWMn          |      |
	|      |                      |       | Default is high        |      |
	|      |                      |       | level output           |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 11:8 | PWMMODE              | R/W   | PWM0~3 operating mode  | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | [n+8] = 0: PWMn        |      |
	|      |                      |       | Operation in Continuous|      |
	|      |                      |       | Out Mode               |      |
	|      |                      |       |                        |      |
	|      |                      |       | [n+8] = 1: PWMn        |      |
	|      |                      |       | Operation in fixed     |      |
	|      |                      |       | output mode            |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | SHIFTMODE            | R/W   | Enable PWM synchronous | 0x0  |
	|      |                      |       | phase output mode      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = PWM0~3             |      |
	|      |                      |       | operate in general mode|      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = PWM0~3 operate in  |      |
	|      |                      |       | 4-way synchronised     |      |
	|      |                      |       | output mode            |      |
	+------+----------------------+-------+------------------------+------+
	| 19:17| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | pclk_force_en        | R/W   | APB                    | 0x0  |
	|      |                      |       | Clock Gating Control   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Enable APB clock   |      |
	|      |                      |       | gating to automatically|      |
	|      |                      |       | turn off the clock when|      |
	|      |                      |       | turn off the clock when|      |
	|      |                      |       | idle                   |      |
	|      |                      |       | 1 = APB clock held     |      |
	|      |                      |       | constant on            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:21| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PWMSTART
^^^^^^^^^

.. _table_pwmstart:
.. table:: PWMSTART, Offset Address: 0x044
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 3:0  | PWMSTART             | R/W   | EnablePWM0~3           | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | [n] = 0: Stop PWMn     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [n] = 1: Output PWMn   |      |
	|      |                      |       |                        |      |
	|      |                      |       | When PWMMODE is set to |      |
	|      |                      |       | 0, write bit n to 0 and|      |
	|      |                      |       | then write 1 to start  |      |
	|      |                      |       | PWMn output, until bit |      |
	|      |                      |       | n is written to 0 to   |      |
	|      |                      |       | stop output. When      |      |
	|      |                      |       | PWMMODE is set to 1,   |      |
	|      |                      |       | write bit n to 1 to    |      |
	|      |                      |       | start PWMn output, and |      |
	|      |                      |       | stop output            |      |
	|      |                      |       | automatically when the |      |
	|      |                      |       | number of pulses output|      |
	|      |                      |       | output equals to the   |      |
	|      |                      |       | value of PCOUNTn.      |      |
	|      |                      |       | When SHIFTMODE is set  |      |
	|      |                      |       | to 1, PWMSTART[3:0]    |      |
	|      |                      |       | will be PWM0           |      |
	|      |                      |       | ~PWMSTART[3:0] will be |      |
	|      |                      |       | PWM0~ and will be      |      |
	|      |                      |       | controlled by          |      |
	|      |                      |       | SHIFTSTART             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PWMDONE
^^^^^^^^^

.. _table_pwmdone:
.. table:: PWMDONE, Offset Address: 0x048
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 3:0  | PWMDONE              | RO    | PWM0~3 End output state|      |
	|      |                      |       |                        |      |
	|      |                      |       | [n] = 1: PWMn          |      |
	|      |                      |       | Closed Output          |      |
	|      |                      |       |                        |      |
	|      |                      |       | When PWMSTART[n] is set|      |
	|      |                      |       | to 1 from 0, the       |      |
	|      |                      |       | register value is      |      |
	|      |                      |       | cleared to 0.          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PWMUPDATE
^^^^^^^^^

.. _table_pwmupdate:
.. table:: PWMUPDATE, Offset Address: 0x04c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 3:0  | PWMUPDATE            | R/W   | Dynamically loaded     | 0x0  |
	|      |                      |       | PWM parameters         |      |
	|      |                      |       |                        |      |
	|      |                      |       | When PWMSTART is       |      |
	|      |                      |       | written from 0 to 1,   |      |
	|      |                      |       | the register values    |      |
	|      |                      |       | (HLPERIODn,PERIODn) are|      |
	|      |                      |       | held temporarily inside|      |
	|      |                      |       | the PWM. If you want to|      |
	|      |                      |       | change the waveform    |      |
	|      |                      |       | dynamically in the     |      |
	|      |                      |       | PWM output, write the  |      |
	|      |                      |       | new value to HLPERIODn |      |
	|      |                      |       | and PERIODn, then write|      |
	|      |                      |       | 1 to PWMUPDATE[n] and  |      |
	|      |                      |       | then write 0 to make   |      |
	|      |                      |       | new value effective.   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PCOUNT0
^^^^^^^^^

.. _table_pcount0:
.. table:: PCOUNT0, Offset Address: 0x050
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | PCOUNT0              | R/W   | Number of PWM0 pulses  | 0x1  |
	|      |                      |       | (set value must be     |      |
	|      |                      |       | greater than 0)        |      |
	|      |                      |       |                        |      |
	|      |                      |       | Valid only when        |      |
	|      |                      |       | PWMMODE[0] is set to 1.|      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PCOUNT1
^^^^^^^^^

.. _table_pcount1:
.. table:: PCOUNT1, Offset Address: 0x054
	:widths: 1 2 1 4 1


	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | PCOUNT1              | R/W   | Number of PWM1 pulses  | 0x1  |
	|      |                      |       | (set value must be     |      |
	|      |                      |       | greater than 0)        |      |
	|      |                      |       |                        |      |
	|      |                      |       | Valid only when        |      |
	|      |                      |       | PWMMODE[1] is set to 1.|      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PCOUNT2
^^^^^^^^^

.. _table_pcount2:
.. table:: PCOUNT2, Offset Address: 0x058
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | PCOUNT2              | R/W   | Number of PWM2 pulses  | 0x1  |
	|      |                      |       | (set value must be     |      |
	|      |                      |       | greater than 0)        |      |
	|      |                      |       |                        |      |
	|      |                      |       | Valid only when        |      |
	|      |                      |       | PWMMODE[2] is set to 1.|      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PCOUNT3
^^^^^^^^^

.. _table_pcount3:
.. table:: PCOUNT3, Offset Address: 0x05c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | PCOUNT3              | R/W   | Number of PWM3 pulses  | 0x1  |
	|      |                      |       | (set value must be     |      |
	|      |                      |       | greater than 0)        |      |
	|      |                      |       |                        |      |
	|      |                      |       | Valid only when        |      |
	|      |                      |       | PWMMODE[3] is set to 1.|      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PULSECOUNT0
^^^^^^^^^^^

.. _table_pulsecount0:
.. table:: PULSECOUNT0, Offset Address: 0x060
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | PULSECOUNT0          | RO    | PWM0                   |      |
	|      |                      |       | Number of Output       |      |
	|      |                      |       | Pulses Status          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PULSECOUNT1
^^^^^^^^^^^

.. _table_pulsecount1:
.. table:: PULSECOUNT1, Offset Address: 0x064
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | PULSECOUNT1          | RO    | PWM1                   |      |
	|      |                      |       | Number of Output       |      |
	|      |                      |       | Pulses Status          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PULSECOUNT2
^^^^^^^^^^^

.. _table_pulsecount2:
.. table:: PULSECOUNT2, Offset Address: 0x068
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | PULSECOUNT2          | RO    | PWM2                   |      |
	|      |                      |       | Number of Output       |      |
	|      |                      |       | Pulses Status          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PULSECOUNT3
^^^^^^^^^^^

.. _table_pulsecount3:
.. table:: PULSECOUNT3, Offset Address: 0x06c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | PULSECOUNT3          | RO    | PWM3                   |      |
	|      |                      |       | Number of Output       |      |
	|      |                      |       | Pulses Status          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SHIFTCOUNT0
^^^^^^^^^^^

.. _table_shiftcount0:
.. table:: SHIFTCOUNT0, Offset Address: 0x080
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | SHIFTCOUNT0          | R/W   | PWM0                   | 0x0  |
	|      |                      |       | Phase difference of    |      |
	|      |                      |       | the first pulse output |      |
	|      |                      |       | (in clk_pwm)           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Valid only when        |      |
	|      |                      |       | SHIFTMODE is set to 1. |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SHIFTCOUNT1
^^^^^^^^^^^

.. _table_shiftcount1:
.. table:: SHIFTCOUNT1, Offset Address: 0x084
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | SHIFTCOUNT1          | R/W   | PWM1                   | 0x0  |
	|      |                      |       | Phase difference of    |      |
	|      |                      |       | the first pulse output |      |
	|      |                      |       | (in clk_pwm)           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Valid only when        |      |
	|      |                      |       | SHIFTMODE is set to 1. |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SHIFTCOUNT2
^^^^^^^^^^^

.. _table_shiftcount2:
.. table:: SHIFTCOUNT2, Offset Address: 0x088
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | SHIFTCOUNT2          | R/W   | PWM2                   | 0x0  |
	|      |                      |       | Phase difference of    |      |
	|      |                      |       | the first pulse output |      |
	|      |                      |       | (in clk_pwm)           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Valid only when        |      |
	|      |                      |       | SHIFTMODE is set to 1. |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SHIFTCOUNT3
^^^^^^^^^^^

.. _table_shiftcount3:
.. table:: SHIFTCOUNT3, Offset Address: 0x08c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | SHIFTCOUNT3          | R/W   | PWM3                   | 0x0  |
	|      |                      |       | Phase difference of    |      |
	|      |                      |       | the first pulse output |      |
	|      |                      |       | (in clk_pwm)           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Valid only when        |      |
	|      |                      |       | SHIFTMODE is set to 1. |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SHIFTSTART
^^^^^^^^^^

.. _table_shiftstart:
.. table:: SHIFTSTART, Offset Address: 0x090
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | SHIFTSTART           | R/W   | Enable PWM output in   | 0x0  |
	|      |                      |       | synchronous mode       |      |
	|      |                      |       |                        |      |
	|      |                      |       | When SHIFTMODE is set  |      |
	|      |                      |       | to 1, this register    |      |
	|      |                      |       | starts to output PWM0~3|      |
	|      |                      |       | after writing 1.       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PWM_OE
^^^^^^

.. _table_pwm_oe:
.. table:: PWM_OE, Offset Address: 0x0d0
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 3:0  | PWM_OE               | R/W   | PWM0~3 IO output       | 0x0  |
	|      |                      |       | enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = IO is output,      |      |
	|      |                      |       | 0 = IO is input.       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
