RTC_CORE_REG
~~~~~~~~~~~~

RTC_ANA_CALIB
^^^^^^^^^^^^^

.. _table_rtc_ana_calib:
.. table:: RTC_ANA_CALIB, Offset Address: 0x000
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_ANA_CALIB        | R/W   |Adjust analog module    | 0x100|
	|      |                      |       |32K oscillator frequency|      |
	+------+----------------------+-------+------------------------+------+
	| 17:16| RTC_ANA_ISEL         | R/W   |Adjust analog module 32K| 0x3  |
	|      |                      |       |XTAL current            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 00 = 2uA, 01 = 1.5uA,  |      |
	|      |                      |       | 11 = 0.5uA             |      |
	+------+----------------------+-------+------------------------+------+
	| 30:18| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | RTC_ANA_SEL_FTUNE    | R/W   | Select 32K OSC         | 0x1  |
	|      |                      |       | calibration value      |      |
	|      |                      |       | source                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 =  Controlled by     |      |
	|      |                      |       | register RTC_ANA_CALIB |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Controlled by      |      |
	|      |                      |       | hardware circuit       |      |
	+------+----------------------+-------+------------------------+------+

RTC_SEC_PULSE_GEN
^^^^^^^^^^^^^^^^^

.. _table_rtc_sec_pulse_gen:
.. table:: RTC_SEC_PULSE_GEN, Offset Address: 0x004
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | RT\                  | R/W   | Decimal part of        | 0x0  |
	|      | C_SEC_PULSE_GEN_FRAC |       | second pulse generator |      |
	+------+----------------------+-------+------------------------+------+
	| 23:8 | R\                   | R/W   | second pulse generator |0x8000|
	|      | TC_SEC_PULSE_GEN_INT |       | integer part           |      |
	|      |                      |       |                        |      |
	|      |                      |       | When the counter       |      |
	|      |                      |       | increment value is     |      |
	|      |                      |       | greater than the       |      |
	|      |                      |       | integer bit value,     |      |
	|      |                      |       | a second pulse signal  |      |
	|      |                      |       | is generated to        |      |
	|      |                      |       | increase the second    |      |
	|      |                      |       | counter by 1.          |      |
	+------+----------------------+-------+------------------------+------+
	| 30:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | RTC_SEL_SEC_PULSE    | R/W   | Select second pulse    | 0x1  |
	|      |                      |       | signal source          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = signal generated   |      |
	|      |                      |       | internally             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = signal generated   |      |
	|      |                      |       | by an external         |      |
	|      |                      |       | hardware circuit       |      |
	|      |                      |       | When set as 1          |      |
	|      |                      |       | RTC_SEL_PULSE_GEN_FRAC |      |
	|      |                      |       | &                      |      |
	|      |                      |       | RTC_SEL_P              |      |
	|      |                      |       | ULSE_GEN_INThas no     |      |
	|      |                      |       | effect                 |      |
	+------+----------------------+-------+------------------------+------+

RTC_ALARM_TIME
^^^^^^^^^^^^^^

.. _table_rtc_alarm_time:
.. table:: RTC_ALARM_TIME, Offset Address: 0x008
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RTC_ALARM_TIME       | R/W   | Set scheduled          | 0x\  |
	|      |                      |       | alarm time             | ffff\|
	|      |                      |       |                        | ffff |
	+------+----------------------+-------+------------------------+------+

RTC_ALARM_ENABLE
^^^^^^^^^^^^^^^^

.. _table_rtc_alarm_enable:
.. table:: RTC_ALARM_ENABLE, Offset Address: 0x00c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC_ALARM_ENABLE     | R/W   | Alarm enable           | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = enable the alarm   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable the alarm  |      |
	|      |                      |       | or clear the alarm     |      |
	|      |                      |       | interrupt status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_SET_SEC_CNTR_VALUE
^^^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_set_sec_cntr_value:
.. table:: RTC_SET_SEC_CNTR_VALUE, Offset Address: 0x010
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RT\                  | R/W   | Set seconds            | 0x0  |
	|      | C_SET_SEC_CNTR_VALUE |       | counter value          |      |
	+------+----------------------+-------+------------------------+------+

RTC_SET_SEC_CNTR_TRIG
^^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_set_sec_cntr_trig:
.. table:: RTC_SET_SEC_CNTR_TRIG, Offset Address: 0x014
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | R\                   | W1C   | Load seconds           |      |
	|      | TC_SET_SEC_CNTR_TRIG |       | counter value          |      |
	|      |                      |       | 1 = make the value of  |      |
	|      |                      |       | RTC_SET_SEC_CN         |      |
	|      |                      |       | TR_VALUE effective,    |      |
	|      |                      |       | then the register will |      |
	|      |                      |       | be cleared to 0        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_SEC_CNTR_VALUE
^^^^^^^^^^^^^^^^^^

.. _table_rtc_sec_cntr_value:
.. table:: RTC_SEC_CNTR_VALUE, Offset Address: 0x018
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RTC_SEC_CNTR_VALUE   | RO    | Read the current       |      |
	|      |                      |       | seconds counter value  |      |
	+------+----------------------+-------+------------------------+------+

RTC_INFO0
^^^^^^^^^

.. _table_rtc_info0:
.. table:: RTC_INFO0, Offset Address: 0x01c
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RTC_INFO0            | R/W   | Information register 0 | 0x\  |
	|      |                      |       |                        | ABCD\|
	|      |                      |       |                        | 1234 |
	+------+----------------------+-------+------------------------+------+

RTC_INFO1
^^^^^^^^^

.. _table_rtc_info1:
.. table:: RTC_INFO1, Offset Address: 0x020
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RTC_INFO1            | R/W   | Information register 1 | 0x\  |
	|      |                      |       |                        | DEAD\|
	|      |                      |       |                        | BEEF\|
	+------+----------------------+-------+------------------------+------+

RTC_INFO2
^^^^^^^^^

.. _table_rtc_info2:
.. table:: RTC_INFO2, Offset Address: 0x024
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RTC_INFO2            | R/W   | Information register 2 | 0x\  |
	|      |                      |       |                        | ABCD\|
	|      |                      |       |                        | 1234 |
	+------+----------------------+-------+------------------------+------+

RTC_INFO3
^^^^^^^^^

.. _table_rtc_info3:
.. table:: RTC_INFO3, Offset Address: 0x028
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RTC_INFO3            | R/W   | Information register 3 | 0x\  |
	|      |                      |       |                        | DEAD\|
	|      |                      |       |                        | BEEF |
	+------+----------------------+-------+------------------------+------+

RTC_NOPOR_INFO0
^^^^^^^^^^^^^^^

.. _table_rtc_nopor_info0:
.. table:: RTC_NOPOR_INFO0, Offset Address: 0x02c
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RTC_NOPOR_INFO0      | R/W   | No reset               | Ra\  |
	|      |                      |       | information register 0 |      |
	|      |                      |       |                        | ndom |
	+------+----------------------+-------+------------------------+------+

RTC_NOPOR_INFO1
^^^^^^^^^^^^^^^

.. _table_rtc_nopor_info1:
.. table:: RTC_NOPOR_INFO1, Offset Address: 0x030
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RTC_NOPOR_INFO1      | R/W   | No reset               | Ra\  |
	|      |                      |       | information register 1 |      |
	|      |                      |       |                        | ndom |
	+------+----------------------+-------+------------------------+------+

RTC_NOPOR_INFO2
^^^^^^^^^^^^^^^

.. _table_rtc_nopor_info2:
.. table:: RTC_NOPOR_INFO2, Offset Address: 0x034
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RTC_NOPOR_INFO2      | R/W   | No reset               | Ra\  |
	|      |                      |       | information register 2 |      |
	|      |                      |       |                        | ndom |
	+------+----------------------+-------+------------------------+------+

RTC_NOPOR_INFO3
^^^^^^^^^^^^^^^

.. _table_rtc_nopor_info3:
.. table:: RTC_NOPOR_INFO3, Offset Address: 0x038
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RTC_NOPOR_INFO3      | R/W   | No reset               | Ra\  |
	|      |                      |       | information register 3 | ndom |
	+------+----------------------+-------+------------------------+------+

RTC_APB_BUSY_SEL
^^^^^^^^^^^^^^^^

.. _table_rtc_apb_busy_sel:
.. table:: RTC_APB_BUSY_SEL, Offset Address: 0x03c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             | R/W   |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | rtc_apb_32k_busy_sel | R/W   | Select rtc pclk busy   | 0x0  |
	|      |                      |       | as signal source       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = pclk busy signal   |      |
	|      |                      |       | generated by           |      |
	|      |                      |       | hardware circuits      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = pclk busy signal   |      |
	|      |                      |       | controlled by rtc\_\   |      |
	|      |                      |       | apb_32k_force_busy     |      |
	+------+----------------------+-------+------------------------+------+
	| 7:5  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | rt\                  | R/W   | 1 = pclk               | 0x0  |
	|      | c_apb_32k_force_busy |       | Always operates at     |      |
	|      |                      |       | full speed             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = pclk               |      |
	|      |                      |       | only operates at full  |      |
	|      |                      |       | speed during psel      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DB_PWR_VBAT_DET
^^^^^^^^^^^^^^^^^^^

.. _table_rtc_db_pwr_vbat_det:
.. table:: RTC_DB_PWR_VBAT_DET, Offset Address: 0x040
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_DB_PWR_VBAT_DET  | R/W   | PWR_VBAT_DET debounce  | 0x2  |
	|      |                      |       | time(unit: 32K clock)  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DB_BUTTON1
^^^^^^^^^^^^^^

.. _table_rtc_db_button1:
.. table:: RTC_DB_BUTTON1, Offset Address: 0x048
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_DB_BUTTON1       | R/W   | PWR_BUTTON debounce    | 0x100|
	|      |                      |       | time(unit: 32K clock)  |      |
	|      |                      |       |                        |      |
	|      |                      |       | default value 0x100    |      |
	|      |                      |       | is about 8ms           |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DB_PWR_ON
^^^^^^^^^^^^^

.. _table_rtc_db_pwr_on:
.. table:: RTC_DB_PWR_ON, Offset Address: 0x04c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_DB_PWR_ON        | R/W   | PWR_ON debounce        | 0x100|
	|      |                      |       | time(unit: 32K clock)  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_7SEC_RESET
^^^^^^^^^^^^^^

.. _table_rtc_7sec_reset:
.. table:: RTC_7SEC_RESET, Offset Address: 0x050
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | RTC_7SEC_RESET       | R/W   | Long press PWR_BUTTON1 | 0x7  |
	|      |                      |       | reset debounce time    |      |
	|      |                      |       | (unit:second)          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| RTC_7SEC_UNLOCK_KEY  | WO    | Writing 0xDC78 at the  | 0x0  |
	|      |                      |       | same time, releasing   |      |
	|      |                      |       | RTC_7SEC_RESET         |      |
	|      |                      |       | write protection       |      |
	+------+----------------------+-------+------------------------+------+

RTC_THM_SHDN_AUTO_REBOOT
^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_thm_shdn_auto_reboot:
.. table:: RTC_THM_SHDN_AUTO_REBOOT, Offset Address: 0x064
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC\_\               | R/W   | When choosing to       | 0x0  |
	|      | THM_SHDN_AUTO_REBOOT |       | receive REQ_THM_SHDN:  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Start the          |      |
	|      |                      |       | power-off process      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 =                    |      |
	|      |                      |       | Start the power-cycle  |      |
	|      |                      |       | process                |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_POR_DB_MAGIC_KEY
^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_por_db_magic_key:
.. table:: RTC_POR_DB_MAGIC_KEY, Offset Address: 0x068
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_POR_DB_MAGIC_KEY | R/W   | Writing 0x5AF0,  will  | Ra\  |
	|      |                      |       | cause POR debounce     | ndom |
	|      |                      |       | (about 1ms)            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DB_SEL_PWR
^^^^^^^^^^^^^^

.. _table_rtc_db_sel_pwr:
.. table:: RTC_DB_SEL_PWR, Offset Address: 0x06c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | DB_SEL_PWR_BUTTON1   | R/W   | Choose PWR_BUTTON1     | 0x1  |
	|      |                      |       | debounce mode          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = The state machine  |      |
	|      |                      |       | is triggered by the    |      |
	|      |                      |       | falling edge of        |      |
	|      |                      |       | PWR_BUTTON1            |      |
	|      |                      |       | debounce signal        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = The state machine  |      |
	|      |                      |       | is triggered by the    |      |
	|      |                      |       | low level of           |      |
	|      |                      |       | PWR_BUTTON1            |      |
	|      |                      |       | debounce signal        |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | DB_SEL_PWR_ON        | R/W   | Choose PWR_ON          | 0x1  |
	|      |                      |       | debounce mode          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = The state machine  |      |
	|      |                      |       | is triggered by the    |      |
	|      |                      |       | rising edge of         |      |
	|      |                      |       | PWR_ON                 |      |
	|      |                      |       | debounce signal        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = The state machine  |      |
	|      |                      |       | is triggered by the    |      |
	|      |                      |       | high level of          |      |
	|      |                      |       | PWR_ON                 |      |
	|      |                      |       | debounce signal        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | DB_SEL_PWR_WAKEUP0   | R/W   | Choose                 | 0x1  |
	|      |                      |       | PWR_WAKEUP0            |      |
	|      |                      |       | debounce mode          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = The state machine  |      |
	|      |                      |       | is triggered by the    |      |
	|      |                      |       | rising edge of         |      |
	|      |                      |       | PWR_WAKEUP0            |      |
	|      |                      |       | debounce signal        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = The state machine  |      |
	|      |                      |       | is triggered by the    |      |
	|      |                      |       | high level of          |      |
	|      |                      |       | PWR_WAKEUP0            |      |
	|      |                      |       | debounce signal        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | DB_SEL_PWR_WAKEUP1   | R/W   | Choose                 | 0x1  |
	|      |                      |       | PWR_WAKEUP1            |      |
	|      |                      |       | debounce mode          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = The state machine  |      |
	|      |                      |       | is triggered by the    |      |
	|      |                      |       | rising edge of         |      |
	|      |                      |       | PWR_WAKEUP1            |      |
	|      |                      |       | debounce signal        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = The state machine  |      |
	|      |                      |       | is triggered by the    |      |
	|      |                      |       | high level of          |      |
	|      |                      |       | PWR_WAKEUP1            |      |
	|      |                      |       | debounce signal        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:5 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_UP_SEQ0
^^^^^^^^^^^

.. _table_rtc_up_seq0:
.. table:: RTC_UP_SEQ0, Offset Address: 0x070
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_UP_SEQ0          | R/W   | Required time for      | 0x0  |
	|      |                      |       | PWR_SEQ0 process       |      |
	|      |                      |       | output change from     |      |
	|      |                      |       | 0 to 1                 |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_UP_SEQ1
^^^^^^^^^^^

.. _table_rtc_up_seq1:
.. table:: RTC_UP_SEQ1, Offset Address: 0x074
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_UP_SEQ1          | R/W   | Required time for      | 0x40 |
	|      |                      |       | PWR_SEQ1 process       |      |
	|      |                      |       | output change from     |      |
	|      |                      |       | 0 to 1                 |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_UP_SEQ2
^^^^^^^^^^^

.. _table_rtc_up_seq2:
.. table:: RTC_UP_SEQ2, Offset Address: 0x078
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_UP_SEQ2          | R/W   | Required time for      | 0x80 |
	|      |                      |       | PWR_SEQ2 process       |      |
	|      |                      |       | output change from     |      |
	|      |                      |       | 0 to 1                 |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_UP_SEQ3
^^^^^^^^^^^

.. _table_rtc_up_seq3:
.. table:: RTC_UP_SEQ3, Offset Address: 0x07c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_UP_SEQ3          | R/W   | Required time for      | 0xc0 |
	|      |                      |       | PWR_SEQ3 process       |      |
	|      |                      |       | output change from     |      |
	|      |                      |       | 0 to 1                 |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_UP_IF_EN
^^^^^^^^^^^^

.. _table_rtc_up_if_en:
.. table:: RTC_UP_IF_EN, Offset Address: 0x080
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_UP_IF_EN         | R/W   | Power-on process       | 0x100|
	|      |                      |       | releases the power-off |      |
	|      |                      |       | area ISO time          |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_UP_RSTN
^^^^^^^^^^^

.. _table_rtc_up_rstn:
.. table:: RTC_UP_RSTN, Offset Address: 0x084
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_UP_RSTN          | R/W   | Power-on process       | 0x140|
	|      |                      |       | system reset release   |      |
	|      |                      |       | time                   |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_UP_MAX
^^^^^^^^^^

.. _table_rtc_up_max:
.. table:: RTC_UP_MAX, Offset Address: 0x088
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_UP_MAX           | R/W   | Complete power-on      | 0x180|
	|      |                      |       | process completion     |      |
	|      |                      |       | time                   |      |
	|      |                      |       | (unit:32K clock)       |      |
	|      |                      |       |                        |      |
	|      |                      |       | RT\                    |      |
	|      |                      |       | C_UP_SEQ0~RTC_UP_MAX   |      |
	|      |                      |       | is the absolute        |      |
	|      |                      |       | time of each stage of  |      |
	|      |                      |       | the power-on process.  |      |
	|      |                      |       | It is recommended to   |      |
	|      |                      |       | use the default value  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DN_SEQ0
^^^^^^^^^^^

.. _table_rtc_dn_seq0:
.. table:: RTC_DN_SEQ0, Offset Address: 0x090
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_DN_SEQ0          | R/W   | Required time for      | 0x140|
	|      |                      |       | PWR_SEQ0 process       |      |
	|      |                      |       | output change from     |      |
	|      |                      |       | 1 to 0                 |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DN_SEQ1
^^^^^^^^^^^

.. _table_rtc_dn_seq1:
.. table:: RTC_DN_SEQ1, Offset Address: 0x094
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_DN_SEQ1          | R/W   | Required time for      | 0x100|
	|      |                      |       | PWR_SEQ1 process       |      |
	|      |                      |       | output change from     |      |
	|      |                      |       | 1 to 0                 |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DN_SEQ2
^^^^^^^^^^^

.. _table_rtc_dn_seq2:
.. table:: RTC_DN_SEQ2, Offset Address: 0x098
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_DN_SEQ2          | R/W   | Required time for      | 0xc0 |
	|      |                      |       | PWR_SEQ2 process       |      |
	|      |                      |       | output change from     |      |
	|      |                      |       | 1 to 0                 |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DN_SEQ3
^^^^^^^^^^^

.. _table_rtc_dn_seq3:
.. table:: RTC_DN_SEQ3, Offset Address: 0x09c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_DN_SEQ3          | R/W   | Required time for      | 0x80 |
	|      |                      |       | PWR_SEQ3 process       |      |
	|      |                      |       | output change from     |      |
	|      |                      |       | 1 to 0                 |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DN_IF_EN
^^^^^^^^^^^^

.. _table_rtc_dn_if_en:
.. table:: RTC_DN_IF_EN, Offset Address: 0x0a0
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_DN_IF_EN         | R/W   | Power-off process      | 0x40 |
	|      |                      |       | releases the power-off |      |
	|      |                      |       | area ISO time          |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DN_RSTN
^^^^^^^^^^^

.. _table_rtc_dn_rstn:
.. table:: RTC_DN_RSTN, Offset Address: 0x0a4
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_DN_RSTN          | R/W   | Power-off process      | 0x0  |
	|      |                      |       | system reset release   |      |
	|      |                      |       | time                   |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DN_MAX
^^^^^^^^^^

.. _table_rtc_dn_max:
.. table:: RTC_DN_MAX, Offset Address: 0x0a8
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_DN_MAX           | R/W   | Complete power-off     | 0x180|
	|      |                      |       | process completion     |      |
	|      |                      |       | time                   |      |
	|      |                      |       | (unit:32K clock)       |      |
	|      |                      |       |                        |      |
	|      |                      |       | RT\                    |      |
	|      |                      |       | C_DN_SEQ0~RTC_DN_MAX   |      |
	|      |                      |       | is the absolute        |      |
	|      |                      |       | time of each stage of  |      |
	|      |                      |       | the power-OFF process. |      |
	|      |                      |       | It is recommended to   |      |
	|      |                      |       | use the default value  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_PWR_CYC_MAX
^^^^^^^^^^^^^^^

.. _table_rtc_pwr_cyc_max:
.. table:: RTC_PWR_CYC_MAX, Offset Address: 0x0b0
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RTC_PWR_CYC_MAX      | R/W   | Complete power-cycle   |0x4000|
	|      |                      |       | process completion     |      |
	|      |                      |       | time                   |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_WARM_RST_MAX
^^^^^^^^^^^^^^^^

.. _table_rtc_warm_rst_max:
.. table:: RTC_WARM_RST_MAX, Offset Address: 0x0b4
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RRTC_WARM_RST_MAX    | R/W   | Complete WARM_RESET    | 0x40 |
	|      |                      |       | process completion     |      |
	|      |                      |       | time                   |      |
	|      |                      |       | (unit:32K clock)       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_EN_7SEC_RST
^^^^^^^^^^^^^^^

.. _table_rtc_en_7sec_rst:
.. table:: RTC_EN_7SEC_RST, Offset Address: 0x0b8
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC_EN_7SEC_RST      | R/W   | Enable long press      | 0x0  |
	|      |                      |       | PWR_BUTTON1 to         |      |
	|      |                      |       | trigger 7-second       |      |
	|      |                      |       | RTC forced reset       |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | RTC_7SEC_RST_MODE    | R/W   | 7-second forced        | 0x0  |
	|      |                      |       | reset mode             |      |
	|      |                      |       | 0 = Low level mode,    |      |
	|      |                      |       | 1 = Short pulse mode   |      |
	|      |                      |       | When 7-second forced   |      |
	|      |                      |       | reset occurs, select   |      |
	|      |                      |       | to generate a short    |      |
	|      |                      |       | reset signal or hold   |      |
	|      |                      |       | reset until releasing  |      |
	|      |                      |       | PWR_BUTTON1            |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | DB\_\                | R/W   | 0 = If PWR_BUTTON1     | 0x0  |
	|      | SEL_PWR_BUTTON1_7SEC |       | is triggered by the    |      |
	|      |                      |       | power-on current after |      |
	|      |                      |       | PWR_BUTTON1 is         |      |
	|      |                      |       | triggered, reset the   |      |
	|      |                      |       | 7-sec reset counter    |      |
	|      |                      |       | 1 = NOP                |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | SEL_7SEC_RST_RTCSYS  | R/W   | 0 = 7-second forced    | 0x1  |
	|      |                      |       | reset signal will      |      |
	|      |                      |       | reset the RTC          |      |
	|      |                      |       | subsystem sec reset    |      |
	|      |                      |       | will not reset         |      |
	|      |                      |       | rtcsys                 |      |
	|      |                      |       | 1 = 7-second forced    |      |
	|      |                      |       | reset signal will not  |      |
	|      |                      |       | reset RTC subsystem    |      |
	+------+----------------------+-------+------------------------+------+
	| 15:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| RTC_EN_7SEC_UNLOCK_KEY | WO  | Simultaneously write   | 0x0  |
	|      |                      |       | 0xDC78 to unlock       |      |
	|      |                      |       | [3:0] write protection |      |
	+------+----------------------+-------+------------------------+------+

RTC_EN_PWR_WAKEUP
^^^^^^^^^^^^^^^^^

.. _table_rtc_en_pwr_wakeup:
.. table:: RTC_EN_PWR_WAKEUP, Offset Address: 0x0bc
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 6:0  | RTC_EN_PWR_WAKEUP    | R/W   | Set the sources        | 0x0  |
	|      |                      |       | capable of waking      |      |
	|      |                      |       | up from sleep mode     |      |
	|      |                      |       | 0 = Cannot trigger     |      |
	|      |                      |       | wakeup                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Can trigger        |      |
	|      |                      |       | wakeup                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] = PWR_WAKEUP0      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] = PWR_WAKEUP1      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] = PWR_ON           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] = REQ_POWERUP      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4] = PWR_BUTTON1      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5] = Alarm            |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6] = REQ_WAKEUP       |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 14:8 | RTC_EN_PWR_UP        | R/W   | Set the sources        | 0x14 |
	|      |                      |       | capable of power       |      |
	|      |                      |       | up from off state      |      |
	|      |                      |       | 0 = Cannot trigger     |      |
	|      |                      |       | power on               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Can trigger        |      |
	|      |                      |       | power on               |      |
	|      |                      |       |                        |      |
	|      |                      |       | [8] = PWR_WAKEUP0      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [9] = PWR_WAKEUP1      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [10] = PWR_ON          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [11] = REQ_POWERUP     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [12] = PWR_BUTTON1     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [13] = Alarm           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [14] = REQ_WAKEUP      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:15| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_EN_SHDN_REQ
^^^^^^^^^^^^^^^

.. _table_rtc_en_shdn_req:
.. table:: RTC_EN_SHDN_REQ, Offset Address: 0x0c0
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC_EN_SHDN_REQ      | R/W   | Enable software to     | 0x0  |
	|      |                      |       | equest power-off       |      |
	|      |                      |       | =(REQ_SHDN)            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_EN_THM_SHDN
^^^^^^^^^^^^^^^

.. _table_rtc_en_thm_shdn:
.. table:: RTC_EN_THM_SHDN, Offset Address: 0x0c4
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC_EN_THM_SHDN      | R/W   | Enable request         | 0x0  |
	|      |                      |       | thermal shutdown       |      |
	|      |                      |       | or reboot (REQ_THM_SHDN|      |
	|      |                      |       | )                      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_EN_PWR_CYC_REQ
^^^^^^^^^^^^^^^^^^

.. _table_rtc_en_pwr_cyc_req:
.. table:: RTC_EN_PWR_CYC_REQ, Offset Address: 0x0c8
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC_EN_PWR_CYC_REQ   | R/W   | Enable request Power-  | 0x0  |
	|      |                      |       | cycle (REQ_PWR_CYC)    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_EN_WARM_RST_REQ
^^^^^^^^^^^^^^^^^^^

.. _table_rtc_en_warm_rst_req:
.. table:: RTC_EN_WARM_RST_REQ, Offset Address: 0x0cc
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC_EN_WARM_RST_REQ  | R/W   | Enable system          | 0x0  |
	|      |                      |       | warm reset request     |      |
	|      |                      |       | (REQ_WARM_RST)         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_EN_PWR_VBAT_DET
^^^^^^^^^^^^^^^^^^^

.. _table_rtc_en_pwr_vbat_det:
.. table:: RTC_EN_PWR_VBAT_DET, Offset Address: 0x0d0
	:widths: 1 4 1 4 1

	+------+----------------------+-------+--------------------------------+------+
	| Bits | Name                 |Access | Description                    |Reset |
	+======+======================+=======+================================+======+
	| 0    | RTC_EN_PWR_VBAT_DET  | R/W   | Enable battery low voltage     | 0x1  |
	|      | _UP                  |       | state machine reference        |      |
	|      | C_EN_PWR_VBAT_DET_UP |       | detection status               |      |
	|      |                      |       | (PWR_VBAT_DET)                 |      |
	|      |                      |       |                                |      |
	|      |                      |       | 0 = disable, 1 = enable        |      |
	|      |                      |       |                                |      |
	|      |                      |       | If set to 1, when any key      |      |
	|      |                      |       | attempts to power up or wake   |      |
	|      |                      |       | up, the state machine will     |      |
	|      |                      |       | check the low voltage          |      |
	|      |                      |       | detection output value. If     |      |
	|      |                      |       | the low voltage detection      |      |
	|      |                      |       | output is low (battery voltage |      |
	|      |                      |       | too low or no power source),   |      |
	|      |                      |       | the RTC state machine will     |      |
	|      |                      |       | maintain the current state.    |      |
	+------+----------------------+-------+--------------------------------+------+
	| 1    | RTC_EN_PWR_VBAT_DET  | R/W   | Enable battery low voltage     | 0x1  |
	|      | _DN                  |       | state trigger down power       |      |
	|      | C_EN_PWR_VBAT_DET_DN |       |                                |      |
	|      |                      |       | 0 = disable, 1 = enable        |      |
	|      |                      |       |                                |      |
	|      |                      |       | If set to 1, when the chip     |      |
	|      |                      |       | is in normal power up or       |      |
	|      |                      |       | has entered sleep, the RTC     |      |
	|      |                      |       | state machine will check the   |      |
	|      |                      |       | low voltage detection output.  |      |
	|      |                      |       | If the low voltage detection   |      |
	|      |                      |       | output changes from high to    |      |
	|      |                      |       | low (battery voltage too low   |      |
	|      |                      |       | or power loss), the state      |      |
	|      |                      |       | machine will trigger the       |      |
	|      |                      |       | down power process.            |      |
	+------+----------------------+-------+--------------------------------+------+
	| 2    | RTC_EN_AUTO_POWER_UP | R/W   | Enable RTC state machine       | 0x1  |
	|      |                      |       | automatic entry into power up  |      |
	|      |                      |       | state                          |      |
	|      |                      |       | 1 = When entering power down   |      |
	|      |                      |       | and PWR_VBAT_DET is high,      |      |
	|      |                      |       | automatically power up         |      |
	|      |                      |       |                                |      |
	|      |                      |       | 0 = Stay in this state when    |      |
	|      |                      |       | entering power down, until     |      |
	|      |                      |       | any power source is triggered  |      |
	+------+----------------------+-------+--------------------------------+------+
	| 31:3 | Reserved             |       |                                |      |
	+------+----------------------+-------+--------------------------------+------+

FSM_STATE
^^^^^^^^^

.. _table_fsm_state:
.. table:: FSM_STATE, Offset Address: 0x0d4
	:widths: 1 3 1 4 1

	+------+----------------------+-------+--------------------------------+------+
	| Bits | Name                 |Access | Description                    |Reset |
	+======+======================+=======+================================+======+
	| 3:0  | FSM_STATE            | RO    | RTC state machine value        |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h0 = ST_OFF                  |      |
	|      |                      |       | (System power off completed)   |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h1 = ST_UP                   |      |
	|      |                      |       | (Power-up process ongoing)     |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h2 = ST_DN                   |      |
	|      |                      |       | (Power-down process ongoing)   |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h3 = ST_ON                   |      |
	|      |                      |       | (System power on completed)    |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h4 = ST_PWR_CYC2             |      |
	|      |                      |       | (Power-cycle power down        |      |
	|      |                      |       | process completed)             |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h6 = ST_PWR_CYC              |      |
	|      |                      |       | (Power-cycle power down        |      |
	|      |                      |       | in progress)                   |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h7 = ST_WARM_RESET           |      |
	|      |                      |       | (System reset in progress)     |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h9 = ST_SUSP                 |      |
	|      |                      |       | (System suspended)             |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'hB = ST_PRE_SUSP             |      |
	|      |                      |       | (Suspend power-down process    |      |
	|      |                      |       | ongoing)                       |      |
	+------+----------------------+-------+--------------------------------+------+
	| 31:4 | Reserved             |       |                                |      |
	+------+----------------------+-------+--------------------------------+------+


RTC_EN_WDG_RST_REQ
^^^^^^^^^^^^^^^^^^

.. _table_rtc_en_wdg_rst_req:
.. table:: RTC_EN_WDG_RST_REQ, Offset Address: 0x0e0
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC_EN_WDG_RST_REQ   | R/W   | Enable Watchdog reset  | 0x0  |
	|      |                      |       | request (REQ_WDG_RST)  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | RT\                  | R/W   | Enable Watchdog reset  | 0x1  |
	|      | C_EN_SUS_WDG_RST_REQ |       | request when in sleep  |      |
	|      |                      |       | state                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


RTC_EN_SUSPEND_REQ
^^^^^^^^^^^^^^^^^^

.. _table_rtc_en_suspend_req:
.. table:: RTC_EN_SUSPEND_REQ, Offset Address: 0x0e4
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC_EN_SUSPEND_REQ   | R/W   | Enable request sleep   | 0x0  |
	|      |                      |       | (REQ_SUSPEND)          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_PG_REG
^^^^^^^^^^

.. _table_rtc_pg_reg:
.. table:: RTC_PG_REG, Offset Address: 0x0f0
	:widths: 1 3 1 4 1

	+------+----------------------+--------+------------------------+-------+
	| Bits | Name                 | Access | Description            | Reset |
	+======+======================+========+========================+=======+
	| 3:0  | RTC_PG_REG           | R/W    | Chip Power Good Status | 0xF   |
	|      |                      |        |                        |       |
	|      |                      |        | 1 = Chip has power     |       |
	|      |                      |        | (Power Good), IO signal|       |
	|      |                      |        | can pass               |       |
	|      |                      |        |                        |       |
	|      |                      |        | 0 = Chip power down,   |       |
	|      |                      |        | IO signal retains state|       |
	|      |                      |        | (retent)               |       |
	|      |                      |        |                        |       |
	|      |                      |        | [0] = Control DDR IO   |       |
	|      |                      |        |                        |       |
	|      |                      |        | [3:1] = reserved       |       |
	|      |                      |        |                        |       |
	|      |                      |        | This register signal is|       |
	|      |                      |        | used to control whether|       |
	|      |                      |        | the chip IO interface  |       |
	|      |                      |        | with DDR is normal pass|       |
	|      |                      |        | or retent state. Before|       |
	|      |                      |        | the system enters sleep|       |
	|      |                      |        | the software must set  |       |
	|      |                      |        | this register value to |       |
	|      |                      |        | 0 to keep DDR IO in a  |       |
	|      |                      |        | fixed state. After the |       |
	|      |                      |        | system wakes up from   |       |
	|      |                      |        | sleep, it must set this|       |
	|      |                      |        | register value to 1 to |       |
	|      |                      |        | allow DDR to resume    |       |
	|      |                      |        | normal operation. When |       |
	|      |                      |        | entering power down    |       |
	|      |                      |        | state, this register   |       |
	|      |                      |        | value will be          |       |
	|      |                      |        | automatically cleared  |       |
	|      |                      |        | to all 1s.             |       |
	+------+----------------------+--------+------------------------+-------+
	| 31:4 | Reserved             |        |                        |       |
	+------+----------------------+--------+------------------------+-------+

RTC_ST_ON_REASON
^^^^^^^^^^^^^^^^

.. _table_rtc_st_on_reason:
.. table:: RTC_ST_ON_REASON, Offset Address: 0x0f8
	:widths: 1 4 1 4 1

	+------+----------------------+-------+--------------------------------+------+
	| Bits | Name                 |Access | Description                    |Reset |
	+======+======================+=======+================================+======+
	| 3:0  | ST\_\                | RO    | RTC state machine return to    |      |
	|      | ON_REASON_LAST_STATE |       | on from the following states:  |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h0 = ST_OFF                  |      |
	|      |                      |       | (Power-off to on)              |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h3 = ST_PWR_CYC              |      |
	|      |                      |       | (Power-cycle or Warm-reset     |      |
	|      |                      |       | to on)                         |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h9 = ST_SUSP                 |      |
	|      |                      |       | (Suspended to on)              |      |
	|      |                      |       |                                |      |
	|      |                      |       | After system restart, the      |      |
	|      |                      |       | software can determine the     |      |
	|      |                      |       | chip boot-up reason by reading |      |
	|      |                      |       | this register.                 |      |
	+------+----------------------+-------+--------------------------------+------+
	| 15:4 | Reserved             |       |                                |      |
	+------+----------------------+-------+--------------------------------+------+
	| 31:16| ST\_\                | RO    | The reason (recorded signal    |      |
	|      | ON_REASON_LAST_INPUT |       | state) for returning to the    |      |
	|      |                      |       | on state of state machine      |      |
	|      |                      |       |                                |      |
	|      |                      |       | [0] = PWR_VBAT_DET (0: Power-  |      |
	|      |                      |       | off triggered)                 |      |
	|      |                      |       |                                |      |
	|      |                      |       | [1] = PWR_ON (1: Key triggered |      |
	|      |                      |       | power-on)                      |      |
	|      |                      |       |                                |      |
	|      |                      |       | [2] = RTC_EN_AUTO_POWER_UP     |      |
	|      |                      |       |                                |      |
	|      |                      |       | [3] = PWR_BUTTON1 (0: Key      |      |
	|      |                      |       | triggered power-on)            |      |
	|      |                      |       |                                |      |
	|      |                      |       | [4] = PWR_BUTTON1_7SEC         |      |
	|      |                      |       |                                |      |
	|      |                      |       | [5] = PWR_WAKEUP0 (1: Key      |      |
	|      |                      |       | triggered wake-up)             |      |
	|      |                      |       |                                |      |
	|      |                      |       | [6] = PWR_WAKEUP1 (1: Key      |      |
	|      |                      |       | triggered wake-up)             |      |
	|      |                      |       |                                |      |
	|      |                      |       | [7] = Alarm (1: Timed alarm)   |      |
	|      |                      |       |                                |      |
	|      |                      |       | [8] = REQ_PWR_CYC (1: Software |      |
	|      |                      |       | triggered power-cycle)         |      |
	|      |                      |       |                                |      |
	|      |                      |       | [9] = REQ_THM_SHDN (1:         |      |
	|      |                      |       | Software triggered power-off/  |      |
	|      |                      |       | power-cycle)                   |      |
	|      |                      |       |                                |      |
	|      |                      |       | [10] = REQ_WARM_RST (1:        |      |
	|      |                      |       | Software triggered reset)      |      |
	|      |                      |       |                                |      |
	|      |                      |       | [11] = REQ_WDG_RST (1:         |      |
	|      |                      |       | Watchdog triggered reset)      |      |
	|      |                      |       |                                |      |
	|      |                      |       | [12] = REQ_SHDN (1: Software   |      |
	|      |                      |       | triggered power-off)           |      |
	|      |                      |       |                                |      |
	|      |                      |       | [13] = REQ_SUSPEND (1:         |      |
	|      |                      |       | Software triggered sleep)      |      |
	|      |                      |       |                                |      |
	|      |                      |       | [14] = REQ_WAKEUP (1: Event    |      |
	|      |                      |       | triggered wake-up)             |      |
	|      |                      |       |                                |      |
	|      |                      |       | [15] = REQ_POWERUP             |      |
	+------+----------------------+-------+--------------------------------+------+

  
RTC_ST_OFF_REASON
^^^^^^^^^^^^^^^^^

.. _table_rtc_st_off_reason:
.. table:: RTC_ST_OFF_REASON, Offset Address: 0x0fc
	:widths: 1 4 1 4 1

	+------+----------------------+-------+--------------------------------+------+
	| Bits | Name                 |Access | Description                    |Reset |
	+======+======================+=======+================================+======+
	| 3:0  | ST_O\                | RO    | The RTC state machine          |      |
	|      | FF_REASON_LAST_STATE |       | transitioned to off (ST_OFF)   |      |
	|      |                      |       | from the following states:     |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h3 = ST_ON                   |      |
	|      |                      |       | (Transitioned from on to off)  |      |
	|      |                      |       |                                |      |
	|      |                      |       | 4'h9 = ST_SUSP                 |      |
	|      |                      |       | (Transitioned from suspend to  |      |
	|      |                      |       | off)                           |      |
	|      |                      |       |                                |      |
	|      |                      |       | Other = 7-second forced reset  |      |
	|      |                      |       | occurred                       |      |
	|      |                      |       |                                |      |
	|      |                      |       | After system restart, software |      |
	|      |                      |       | can determine the chip's last  |      |
	|      |                      |       | power-off reason by reading    |      |
	|      |                      |       | this register.                 |      |
	+------+----------------------+-------+--------------------------------+------+
	| 15:4 | Reserved             |       |                                |      |
	+------+----------------------+-------+--------------------------------+------+
	| 31:16| ST_O\                | RO    | The reason (recorded signal    |      |
	|      | FF_REASON_LAST_INPUT |       | state) for entering the off    |      |
	|      |                      |       | state of the state machine     |      |
	|      |                      |       |                                |      |
	|      |                      |       | [14:0]                         |      |
	|      |                      |       | Same as ST_ON_REASON_LAST_INPUT|      |
	|      |                      |       |                                |      |
	|      |                      |       | [15] = 0:                      |      |
	|      |                      |       | 7-second forced reset occurred |      |
	+------+----------------------+-------+--------------------------------+------+

RTC_EN_WAKEUP_REQ
^^^^^^^^^^^^^^^^^

.. _table_rtc_en_wakeup_req:
.. table:: RTC_EN_WAKEUP_REQ, Offset Address: 0x120
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC_EN_WAKEUP_REQ    | R/W   | Enable                 | 0x0  |
	|      |                      |       | Wakeup request from    |      |
	|      |                      |       | sleep state            |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | RTC_EN_POWERUP_REQ   | R/W   | Enable power-up event  | 0x0  |
	|      |                      |       | request                |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_PWR_WAKEUP_POLARITY
^^^^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_pwr_wakeup_polarity:
.. table:: RTC_PWR_WAKEUP_POLARITY, Offset Address: 0x128
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RTC_EN_WAKEUP_REQ    | R/W   | Enable                 | 0x0  |
	|      |                      |       | Wakeup request event   |      |
	|      |                      |       | from sleep state       |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | RTC_EN_POWERUP_REQ   | R/W   | Enable event request   | 0x0  |
	|      |                      |       | power up               |      |
	|      |                      |       | 0 = disable, 1 =       |      |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_DB_SEL_REQ
^^^^^^^^^^^^^^

.. _table_rtc_db_sel_req:
.. table:: RTC_DB_SEL_REQ, Offset Address: 0x130
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | DB_SEL_REQ_SHDN      | R/W   | Select software        | 0x1  |
	|      |                      |       | signal REQ_SHDN        |      |
	|      |                      |       | debounce mode          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Rising edge of     |      |
	|      |                      |       | register value triggers|      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Pulse signal of    |      |
	|      |                      |       | register triggers      |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | DB_SEL_REQ_THM_SHDN  | R/W   | Select signal          | 0x1  |
	|      |                      |       | REQ_THM_SHDN debounce  |      |
	|      |                      |       | mode                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = High level of      |      |
	|      |                      |       | signal triggers        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Rising edge of     |      |
	|      |                      |       | signal triggers        |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | DB_SEL_REQ_PWR_CYC   | R/W   | Select software signal | 0x1  |
	|      |                      |       | REQ_PWR_CYC debounce   |      |
	|      |                      |       | mode                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Rising edge of     |      |
	|      |                      |       | register value triggers|      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Pulse signal of    |      |
	|      |                      |       | register triggers      |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | DB_SEL_REQ_WARM_RST  | R/W   | Select software signal | 0x1  |
	|      |                      |       | REQ_WARM_RST debounce  |      |
	|      |                      |       | mode                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Rising edge of     |      |
	|      |                      |       | register value triggers|      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Pulse signal of    |      |
	|      |                      |       | register triggers      |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | DB_SEL_REQ_WDG_RST   | R/W   | Select signal          | 0x1  |
	|      |                      |       | REQ_WDG_RST debounce   |      |
	|      |                      |       | mode                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = High level of      |      |
	|      |                      |       | signal triggers        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Rising edge of     |      |
	|      |                      |       | signal triggers        |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | DB_SEL_REQ_SUSPEND   | R/W   | Select software signal | 0x1  |
	|      |                      |       | REQ_SUSPEND debounce   |      |
	|      |                      |       | mode                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Rising edge of     |      |
	|      |                      |       | register value triggers|      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Pulse signal of    |      |
	|      |                      |       | register triggers      |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | DB_SEL_REQ_WAKEUP    | R/W   | Select signal          | 0x1  |
	|      |                      |       | REQ_WAKEUP debounce    |      |
	|      |                      |       | mode                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = High level of      |      |
	|      |                      |       | signal triggers        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Rising edge of     |      |
	|      |                      |       | signal triggers        |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | DB_SEL_REQ_POWERUP   | R/W   | Select signal          | 0x1  |
	|      |                      |       | REQ_POWERUP debounce   |      |
	|      |                      |       | mode                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = High level of      |      |
	|      |                      |       | signal triggers        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Rising edge of     |      |
	|      |                      |       | signal triggers        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_PWR_DET_SEL
^^^^^^^^^^^^^^^

.. _table_rtc_pwr_det_sel:
.. table:: RTC_PWR_DET_SEL, Offset Address: 0x140
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | pwr_det_o_sel_comp   | R/W   | Select low voltage     | 0x0  |
	|      |                      |       | detection status signal|      |
	|      |                      |       | output source          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Direct from IO     |      |
	|      |                      |       | PWR_VBAT_DET           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 =                    |      |
	|      |                      |       | From analog low        |      |
	|      |                      |       | voltage detection      |      |
	|      |                      |       | circuit output         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Low voltage detection  |      |
	|      |                      |       | status value can be    |      |
	|      |                      |       | read from register     |      |
	|      |                      |       | TC_CTRL_STATUS0[0]     |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | pwr_det_i_sel_comp   | R/W   | Select RTC state       | 0x0  |
	|      |                      |       | machine low voltage    |      |
	|      |                      |       | triggered power off    |      |
	|      |                      |       | signal source          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Direct from IO     |      |
	|      |                      |       | PWR_VBAT_DET           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 =                    |      |
	|      |                      |       | From analog low        |      |
	|      |                      |       | voltage detection      |      |
	|      |                      |       | circuit output         |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_REG
~~~~~~~~~~~~~

RTC_PWR_DET_COMP
^^^^^^^^^^^^^^^^

.. _table_rtc_pwr_det_comp:
.. table:: RTC_PWR_DET_COMP, Offset Address: 0x44
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | pwr_det_comp_enable  | R/W   | Enable analog module   | 0x0  |
	|      |                      |       | low voltage detection  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 7:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12:8 | pwr_det_comp_sel     | R/W   | Set low voltage        | 0xf  |
	|      |                      |       | detection voltage      |      |
	|      |                      |       | comparison threshold   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Threshold = 1.20V +    |      |
	|      |                      |       | (pwr_det_comp_sel *    |      |
	|      |                      |       | 12.5mV)                |      |
	+------+----------------------+-------+------------------------+------+
	| 31:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_DA_CLEAR_ALL
^^^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_macro_da_clear_all:
.. table:: RTC_MACRO_DA_CLEAR_ALL, Offset Address: 0x080
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | DA_CLEAR_ALL         | R/W   |                        | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_DA_SET_ALL
^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_macro_da_set_all:
.. table:: RTC_MACRO_DA_SET_ALL, Offset Address: 0x084
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | DA_SEL_ALL           | R/W   |                        | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_DA_LATCH_PASS
^^^^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_macro_da_latch_pass:
.. table:: RTC_MACRO_DA_LATCH_PASS, Offset Address: 0x088
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | DA_LATCH_PASS        | R/W   |                        | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_DA_SOC_READY
^^^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_macro_da_soc_ready:
.. table:: RTC_MACRO_DA_SOC_READY, Offset Address: 0x08c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | DA_SOC_READY         | R/W   |                        | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_PD_SLDO
^^^^^^^^^^^^^^^^^

.. _table_rtc_macro_pd_sldo:
.. table:: RTC_MACRO_PD_SLDO, Offset Address: 0x090
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | PD_SLDO              | R/W   |                        | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_RG_DEFD
^^^^^^^^^^^^^^^^^

.. _table_rtc_macro_rg_defd:
.. table:: RTC_MACRO_RG_DEFD, Offset Address: 0x094
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RG_DEFD              | R/W   |                        |0x7fff|
	|      |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_RG_SET_T
^^^^^^^^^^^^^^^^^^

.. _table_rtc_macro_rg_set_t:
.. table:: RTC_MACRO_RG_SET_T, Offset Address: 0x098
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RG_SET_T             | R/W   |                        | 0x0  |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_RO_CLK_STOP
^^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_macro_ro_clk_stop:
.. table:: RTC_MACRO_RO_CLK_STOP, Offset Address: 0x0a0
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RO_CLK_STOP          | RO    |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_RO_DEFQ
^^^^^^^^^^^^^^^^^

.. _table_rtc_macro_ro_defq:
.. table:: RTC_MACRO_RO_DEFQ, Offset Address: 0x0a4
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | RO_DEFQ              | RO    |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_MACRO_RO_T
^^^^^^^^^^^^^^

.. _table_rtc_macro_ro_t:
.. table:: RTC_MACRO_RO_T, Offset Address: 0x0a8
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RO_T                 | RO    |                        |      |
	+------+----------------------+-------+------------------------+------+

.. _section_rtc_ctrl_register_description:

RTC_CTRL_REG
~~~~~~~~~~~~

RTC_CTRL0_UNLOCKKEY
^^^^^^^^^^^^^^^^^^^

.. _table_rtc_ctrl0_unlockkey:
.. table:: RTC_CTRL0_UNLOCKKEY, Offset Address: 0x004
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | rtc_ctrl0_unlockkey  | R/W   | To configure the       |0x0000|
	|      |                      |       | RTC_CTRL0 register,    |      |
	|      |                      |       | you must first write   |      |
	|      |                      |       | the value 0xAB18 to    |      |
	|      |                      |       | unlock it from write   |      |
	|      |                      |       | protection.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | If unlockkey_clear is  |      |
	|      |                      |       | set to 1, after writing|      |
	|      |                      |       | to RTC_CTRL0 once, this|      |
	|      |                      |       | register will          |      |
	|      |                      |       | automatically clear to |      |
	|      |                      |       | 0, and RTC_CTRL0 will  |      |
	|      |                      |       | revert to write        |      |
	|      |                      |       | protection.            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_CTRL0
^^^^^^^^^

.. _table_rtc_ctrl0:
.. table:: RTC_CTRL0, Offset Address: 0x008
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | req_shdn             | R/W   | Request Power Off      | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = No action, 1 =     |      |
	|      |                      |       | Request to RTC         |      |
	|      |                      |       |                        |      |
	|      |                      |       | The RTC_EN_SHDN_REQ    |      |
	|      |                      |       | register must be set   |      |
	|      |                      |       | to 1 to take effect.   |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | req_sw_thm_shdn      | R/W   | Software mode request  | 0x0  |
	|      |                      |       | for overheat shutdown  |      |
	|      |                      |       | or reboot              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = No action, 1 =     |      |
	|      |                      |       | Request to RTC         |      |
	|      |                      |       |                        |      |
	|      |                      |       | The RTC_EN_THM_SHDN    |      |
	|      |                      |       | register must be set   |      |
	|      |                      |       | to 1 to take effect.   |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | hw_thm_shdn_en       | R/W   | Enable hardware mode   | 0x0  |
	|      |                      |       | request for overheat   |      |
	|      |                      |       | shutdown or reboot     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable, 1 = enable|      |
	+------+----------------------+-------+------------------------+------+
	| 3    | req_pwr_cyc          | R/W   | Request Power-cycle    | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = No action, 1 =     |      |
	|      |                      |       | Request to RTC         |      |
	|      |                      |       |                        |      |
	|      |                      |       | The RTC_EN_PWR_CYC_REQ |      |
	|      |                      |       | register must be set   |      |
	|      |                      |       | to 1 to take effect.   |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | req_warm_rst         | R/W   | Request Warm-reset     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = No action, 1 =     |      |
	|      |                      |       | Request to RTC         |      |
	|      |                      |       |                        |      |
	|      |                      |       | The RTC_EN_WARM_RST_REQ|      |
	|      |                      |       | register must be set   |      |
	|      |                      |       | to 1 to take effect.   |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | req_sw_wdg_rst       | R/W   | Software mode request  | 0x0  |
	|      |                      |       | for Watchdog reset     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = No action, 1 =     |      |
	|      |                      |       | Request to RTC         |      |
	|      |                      |       |                        |      |
	|      |                      |       | The RTC_EN_WDG_RST_REQ |      |
	|      |                      |       | register must be set   |      |
	|      |                      |       | to 1 to take effect.   |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | hw_wdg_rst_en        | R/W   | Enable hardware mode   | 0x0  |
	|      |                      |       | request for Watchdog   |      |
	|      |                      |       | reset                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable, 1 = enable|      |
	+------+----------------------+-------+------------------------+------+
	| 7    | req_suspend          | R/W   | Request Suspend        | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = No action, 1 =     |      |
	|      |                      |       | Request to RTC         |      |
	|      |                      |       |                        |      |
	|      |                      |       | The RTC_EN_SUSPEND_REQ |      |
	|      |                      |       | register must be set   |      |
	|      |                      |       | to 1 to take effect.   |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | unlockkey_clear      | R/W   | Enable automatic clear | 0x0  |
	|      |                      |       | of register unlock     |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | reg_rtc_mode         | R/W   | 32K Clock Source       | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = OSC32K, 1 = XTAL32K|      |
	+------+----------------------+-------+------------------------+------+
	| 11   | reg_clk32k_cg_en     | R/W   | 32K Clock Switch       | 0x1  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Off, 1 = On        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_CTRL_STATUS0
^^^^^^^^^^^^^^^^

.. _table_rtc_ctrl_status0:
.. table:: RTC_CTRL_STATUS0, Offset Address: 0x00c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | rtc_pwr_vbat_det_o   | RO    | Low Voltage Detection  |      |
	|      |                      |       | Status Signal Output   |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | rtc_pwr_button0_o    | RO    | PWR_BUTTON0 IO Signal  |      |
	|      |                      |       | Output                 |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | rtc_pwr_button1_o    | RO    | PWR_BUTTON1 IO Signal  |      |
	|      |                      |       | Output                 |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | rtc_pwr_on_o         | RO    | PWR_ON IO Signal Output|      |
	+------+----------------------+-------+------------------------+------+
	| 5    | rtc_pwr_wakeup0_o    | RO    | PWR_WAKEUP0 IO Signal  |      |
	|      |                      |       | Output                 |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | rtc_pwr_wakeup1_o    | RO    | PWR_WAKEUP1 IO Signal  |      |
	|      |                      |       | Output                 |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | rtc_mode_o           | RO    | RTC_MODE IO Signal     |      |
	|      |                      |       | Output                 |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | rtc_alarm_o          | RO    | Alarm Status           |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | hw_thm_shdn_sta_i    | RO    | Overheat Restart       |      |
	|      |                      |       | Status Signal          |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | hw_wdg_rst_sta_i     | RO    | Watchdog Reset Status  |      |
	|      |                      |       | Signal                 |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | sys_reset_x_i        | RO    |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | cg_en_out_clk_32k    | RO    |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 29:26| rtc_fsm_st           | RO    | RTC State Machine Value|      |
	+------+----------------------+-------+------------------------+------+
	| 31:30| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RTC_CTRL_STATUS1
^^^^^^^^^^^^^^^^

.. _table_rtc_ctrl_status1:
.. table:: RTC_CTRL_STATUS1, Offset Address: 0x010
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | rtc_sec_value_o      | RO    | RTC seconds counter    |      |
	|      |                      |       | value                  |      |
	+------+----------------------+-------+------------------------+------+

rtc_ctrl_status2gpio
^^^^^^^^^^^^^^^^^^^^

.. _table_rtc_ctrl_status2gpio:
.. table:: rtc_ctrl_status2gpio, Offset Address: 0x014
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | status2gpio_en       | R/W   |                        | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_rst_ctrl
^^^^^^^^^^^^^^^

.. _table_rtcsys_rst_ctrl:
.. table:: rtcsys_rst_ctrl, Offset Address: 0x018
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_soft_rstn_mcu    | R/W   | 0 : reest MCU          | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg_soft_rstn_sdio   | R/W   | 0 : reset SD1          | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg_soft_rstn_uart   | R/W   | 0 : reset Uart         | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_soft_rstn_spinor | R/W   | 0 : reset spinor1      | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 5    | reg_soft_rstn_ictl   | R/W   | 0 : reset dw_ictl      | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 6    | reg_soft_rstn_mbox   | R/W   | 0 : reset mbox         | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 7    | reg\_\               | R/W   | 0 : reset hs2rtc       | 0x1  |
	|      | soft_rstn_fab_hs2rtc |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg\_\               | R/W   | 0 : reset rtc2ap       | 0x1  |
	|      | soft_rstn_fab_rtc2ap |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | re\                  | R/W   | 0 : reset ahb sram     | 0x1  |
	|      | g_soft_rstn_fab_sram |       | logic                  |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | reg_soft_rstn_apb    | R/W   | no load                | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 11   | reg\                 | R/W   | 0 : reset dw timer apb | 0x1  |
	|      | _soft_rstn_apb_timer |       | logic                  |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | reg_soft_rstn_timer0 | R/W   | 0 : reset dw timer0    | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 13   | reg_soft_rstn_timer1 | R/W   | 0 : reset dw timer1    | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 14   | reg_soft_rstn_osc    | R/W   | 0 : reset osc          | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 15   | reg_soft_rstn_gpio   | R/W   | 0 : reset gpio         | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg_soft_rstn_i2c    | R/W   | 0 : reset i2c          | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 17   | reg_soft_rstn_saradc | R/W   | 0 : reset saradc       | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 18   | reg_soft_rstn_wdt    | R/W   | 0 : reset wdt          | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 19   | reg_soft_rstn_irrx   | R/W   | 0 : reset irrx         | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 20   | re\                  | R/W   | 0: reset f32kless      | 0x1  |
	|      | g_soft_rstn_f32kless |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:21| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_clkmux
^^^^^^^^^^^^^

.. _table_rtcsys_clkmux:
.. table:: rtcsys_clkmux, Offset Address: 0x01c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_sdio_clk_mux     | R/W   | clk_sd1_pre            | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : fpll/4 1: osc_div  |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | reg_fab_clk_mux      | R/W   | clk_fab_pre            | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : 32K, 1: fpll/5, 2: |      |
	|      |                      |       | osc_div                |      |
	+------+----------------------+-------+------------------------+------+
	| 9:8  | reg_timer0_clk_mux   | R/W   | 0: xtal                | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1: 32K                 |      |
	+------+----------------------+-------+------------------------+------+
	| 11:10| reg_timer1_clk_mux   | R/W   | 0: xtal                | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1: 32K                 |      |
	+------+----------------------+-------+------------------------+------+
	| 13:12| reg_apb_clk_mux      | R/W   | 00 : cgdiv and refer   | 0x1  |
	|      |                      |       | to apbactive           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 01 : force clk_apb,    |      |
	|      |                      |       | clk_fab 1:1 (default)  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 10 : force clk_apb,    |      |
	|      |                      |       | clk_fab 1:2            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 11 : force clk_apb,    |      |
	|      |                      |       | clk_fab 1:4            |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 17:16| reg_i2c_clk_mux      | R/W   | 0: xtal                | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1: osc div             |      |
	+------+----------------------+-------+------------------------+------+
	| 19:18| reg_sd_mclk_clk_mux  | R/W   | 0: 100Khz from OSC, 1: | 0x0  |
	|      |                      |       | 32K                    |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | reg_saradc_clk_mux   | R/W   | 0 : XTAL, 1: OSC DIV   | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 21   | reg_irrx_clk_mux     | R/W   | 0 : XTAL, 1: OSC DIV   | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:22| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_mcu51_ctrl0
^^^^^^^^^^^^^^^^^^

.. _table_rtcsys_mcu51_ctrl0:
.. table:: rtcsys_mcu51_ctrl0, Offset Address: 0x020
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 4:0  | reg_51_rom_addr_size | R/W   | Determines how many of | 0xc  |
	|      |                      |       | the sixteen internal   |      |
	|      |                      |       | ROM address bits       |      |
	|      |                      |       | (irom_addr)            |      |
	|      |                      |       | are used (0 = no       |      |
	|      |                      |       | internal ROM present); |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | reg_51_mem_ea_n      | R/W   | 0 : external rom       | 0x0  |
	|      |                      |       | exist, 1: external rom |      |
	|      |                      |       | not exist              |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | reg_51_xdata_mode    | R/W   | 0 : fetch xdata with   | 0x0  |
	|      |                      |       | clock gating           |      |
	|      |                      |       | 1 : fetch xdata wo     |      |
	|      |                      |       | clock gating (to       |      |
	|      |                      |       | support 51 timer and   |      |
	|      |                      |       | 51 uart)               |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | reg_51_rom_addr_def  | R/W   | 0: mercury define ,    | 0x0  |
	|      |                      |       | max internal rom =     |      |
	|      |                      |       | 2^reg_51_rom_addr_size |      |
	|      |                      |       | -1                     |      |
	|      |                      |       | internal rom offset =  |      |
	|      |                      |       | 4K*reg_51irom_ioffset  |      |
	|      |                      |       | 1: mars define , max   |      |
	|      |                      |       | internal rom =         |      |
	|      |                      |       | 2                      |      |
	|      |                      |       | K*reg_51_rom_addr_size |      |
	|      |                      |       | -1                     |      |
	|      |                      |       | internal rom offset =  |      |
	|      |                      |       | 2K*reg_51irom_ioffset  |      |
	+------+----------------------+-------+------------------------+------+
	| 10:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:11| reg_51xdata_ioffset0 | R/W   | Set offset             | 0x0\ |
	|      |                      |       | address[31:12] to      | 5200 |
	|      |                      |       | select mcu8051 boot    |      |
	|      |                      |       | device                 |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_mcu51_ctrl1
^^^^^^^^^^^^^^^^^^

.. _table_rtcsys_mcu51_ctrl1:
.. table:: rtcsys_mcu51_ctrl1, Offset Address: 0x024
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 4:0  | reg_51irom_ioffset   | R/W   | boot rom offset to     | 0x0  |
	|      |                      |       | rtcsys_sram            |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 9:6  | reg_51_pf_mode       | R/W   | reg_51_pf_mode         | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 10   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:11| reg_51xdata_doffset0 | R/W   | Set offset             | 0x0\ |
	|      |                      |       | address[31:12] to      | 5200 |
	|      |                      |       | select mcu8051 xdata   |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_pmu
^^^^^^^^^^

.. _table_rtcsys_pmu:
.. table:: rtcsys_pmu, Offset Address: 0x028
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_dis_pmu_ldo_ctrl | R/W   | disable pmu ldo ctrl   | 0x0  |
	|      |                      |       | 0: enable pmu to ctrl  |      |
	|      |                      |       | RTC_LDO sleep mode     |      |
	|      |                      |       | 1: disable pmu to ctrl |      |
	|      |                      |       | RTC_LDO sleep mode     |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | r\                   | R/W   | wdt_clk gate by pmu    | 0x0  |
	|      | eg_wdt_clkoff_by_pmu |       | when mcu into idle     |      |
	|      |                      |       | mode                   |      |
	|      |                      |       | 1. wdt clock gate by   |      |
	|      |                      |       | pmu                    |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | reg_force_osc_off    | R/W   | 1 : force osc off      | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 7    | reg_force_osc_on     | R/W   | 1 : force osc on       | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg_pmu_sleep_mode   | R/W   | pmu enter light sleep  | 0x0  |
	|      |                      |       | mode when mcu idle     |      |
	|      |                      |       | 1 : enable pmu light   |      |
	|      |                      |       | sleep mode when mcu    |      |
	|      |                      |       | idle                   |      |
	|      |                      |       | (pmu control osc_req/  |      |
	|      |                      |       | sram slp)              |      |
	|      |                      |       | 0 disable pmu light    |      |
	|      |                      |       | sleep mode             |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | reg_pmu_lowpwr_mode  | R/W   | mcu_pmu into sleep     | 0x0  |
	|      |                      |       | state when rtc at      |      |
	|      |                      |       | suspend state & mcu    |      |
	|      |                      |       | idle &                 |      |
	|      |                      |       | reg_pmu_sleep_mode     |      |
	|      |                      |       | enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : enable mcu_pmu     |      |
	|      |                      |       | into sleep mode        |      |
	|      |                      |       | (trigger rtc ldo step  |      |
	|      |                      |       | down power)            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 disable mcu_pmu      |      |
	|      |                      |       | sleep mode             |      |
	+------+----------------------+-------+------------------------+------+
	| 13:10| reg_pmu_stable_cnt   | R/W   | Stable timer when      | 0x3  |
	|      |                      |       | mcu_pmu leave sleep    |      |
	|      |                      |       | state,                 |      |
	|      |                      |       | clock unit : 31.25us   |      |
	|      |                      |       | (32khz), wait for 1~16 |      |
	|      |                      |       | tick cycle             |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | reg_xtal_off_by_pmu  | R/W   | pmu control xtal       | 0x0  |
	|      |                      |       | request                |      |
	|      |                      |       | 1: xtal request        |      |
	|      |                      |       | disable by pmu sleep   |      |
	|      |                      |       | mode                   |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | r\                   | R/W   | xtal request1 for      | 0x1  |
	|      | eg_rtcsys_clk25m_req |       | rtcsys                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: disable 25m xtal    |      |
	|      |                      |       | request1(rtcsys)       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: enable 25m xtal     |      |
	|      |                      |       | request1 (rtcsys)      |      |
	+------+----------------------+-------+------------------------+------+
	| 19:16| reg\                 | R/W   | vbat det int debounce  | 0x2  |
	|      | _rtc_vbat_det_db_cnt |       | time (cycle unit :     |      |
	|      |                      |       | 32K)                   |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | re\                  | R/W   | 0: disable vbat det    | 0x1  |
	|      | g_rtc_vbat_det_db_en |       | int debounce           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: enable vbat det int |      |
	|      |                      |       | debounce               |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | reg\_\               | R/W   | 1: enable ahb sram     | 0x0  |
	|      | ahb_sram_auto_slp_en |       | into slp md when bus   |      |
	|      |                      |       | idle                   |      |
	+------+----------------------+-------+------------------------+------+
	| 23:22| r\                   | R/W   | 2'd0: cs \| cs_d1      | 0x0  |
	|      | eg_ahb_sram_busy_sel |       |                        |      |
	|      |                      |       | 2'd1: cs \| cs_d1 \|   |      |
	|      |                      |       | cs_d2                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2'd2: cs \| cs_d1 \|   |      |
	|      |                      |       | cs_d2 \| cs_d3         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'd3: cs \| cs_d1 \|   |      |
	|      |                      |       | cs_d2 \| cs_d3 \|      |      |
	|      |                      |       | cs_d4                  |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | reg_rtc_stint_clr    | W1P   | clear rtc state change |      |
	|      |                      |       | interrupt              |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | reg_vbat_det_int_clr | W1P   | clear vbet det         |      |
	|      |                      |       | interrupt              |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | reg\_\               | R/W   | xtal request1 for      | 0x0  |
	|      | rtcsys_clk25m_hw_req |       | rtcsys from hw ip      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: disable 25m xtal    |      |
	|      |                      |       | request1 from hw       |      |
	|      |                      |       | ip(rtcsys)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: enable 25m xtal     |      |
	|      |                      |       | request1 from hw       |      |
	|      |                      |       | ip(rtcsys)             |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_rtcsys_pmu_2:
.. table:: rtcsys_pmu, Offset Address: 0x028 (continued)
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 28   | re\                  | R/W   | 1: when vbat det       | 0x0  |
	|      | g_vbat_det_force_clk |       | happen, change rtcsys  |      |
	|      |                      |       | bus clock to OSC       |      |
	+------+----------------------+-------+------------------------+------+
	| 29   | r\                   | R/W   | mcu_clk gate by pmu    | 0x1  |
	|      | eg_mcu_clkoff_by_pmu |       | when into idle mode    |      |
	|      |                      |       | 1. mcu clock gate by   |      |
	|      |                      |       | pmu                    |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | reg_xtal_off_by_susp | R/W   | ISO off control xtal   | 0x0  |
	|      |                      |       | request                |      |
	|      |                      |       | 1: xtal request        |      |
	|      |                      |       | disable by ISO_OFF     |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | reg_osc_off_by_susp  | R/W   | ISO off control osc    | 0x0  |
	|      |                      |       | request                |      |
	|      |                      |       | 1: osc request disable |      |
	|      |                      |       | by ISO_OFF             |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_status
^^^^^^^^^^^^^

.. _table_rtcsys_status:
.. table:: rtcsys_status, Offset Address: 0x02c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | reg_rtcsys_status    | RO    | [0] enable rtc2apb ahb |      |
	|      |                      |       | path                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: rtcsys ip can only  |      |
	|      |                      |       | access 0x05000000+16MB |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: rtcsys ip can       |      |
	|      |                      |       | access full range      |      |
	|      |                      |       | address                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] flag of            |      |
	|      |                      |       | vbat_det_force_clk     |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_clkbyp
^^^^^^^^^^^^^

.. _table_rtcsys_clkbyp:
.. table:: rtcsys_clkbyp, Offset Address: 0x030
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | reg_clk_byp          | R/W   | [0] : clk_fab , 0:     | 0x\  |
	|      |                      |       | clk_fab_pre, 1: xtal   | ffff |
	|      |                      |       | (default)              | ffff |
	|      |                      |       |                        |      |
	|      |                      |       | [1] : clk_sdio, 1:     |      |
	|      |                      |       | clk_sd1_pre, 1: xtal   |      |
	|      |                      |       | (default)              |      |
	|      |                      |       |                        |      |
	|      |                      |       | [31:2]: NA             |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_clk_en
^^^^^^^^^^^^^

.. _table_rtcsys_clk_en:
.. table:: rtcsys_clk_en, Offset Address: 0x034
	:widths: 1 3 1 3 2

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | reg_clk_en           | R/W   | [0]: NA                | 0x\  |
	|      |                      |       |                        | ffff\|
	|      |                      |       | [1]: clk_sd1 (sd1 card | ffff |
	|      |                      |       | clock)                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2]: clk_fab_sd1 (sd1  |      |
	|      |                      |       | core clock)            |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3]: clk_mcu           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4]: clk_hs2rtc_mst    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5]: clk_rtc2ap_slv    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6]: clk_spinor1       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7]: clk_fab_sram (AHB |      |
	|      |                      |       | sram)                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [8]: NA                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [9]: clk_apb_timer     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [10]: clk_timer0       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [11]: clk_timer1       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [12]: clk_apb_uart     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [13]: clk_uart         |      |
	|      |                      |       |                        |      |
	|      |                      |       | [14]: clk_apb_ictrl    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [15]: clk_apb_mbox     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [16]: clk_apb_gpio     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [17]: clk_apb_osc      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [18]: clk_gpio_db      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [19]: clk_apb_i2c      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [20]: clk_i2c          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [21]: NA               |      |
	|      |                      |       |                        |      |
	|      |                      |       | [22]: clk_sd1_tmclk    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [23]: clk_apb_saradc   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [24]: clk_saradc       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [25]: clk_apb_wdt      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [26]: clk_wdt          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [27]: clk_irrx         |      |
	|      |                      |       |                        |      |
	|      |                      |       | [31:28]: NA            |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_wkup_ctrl
^^^^^^^^^^^^^^^^

.. _table_rtcsys_wkup_ctrl:
.. table:: rtcsys_wkup_ctrl, Offset Address: 0x038
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 14:0 | r\                   | R/W   | mask int to            | 0xff |
	|      | eg_rtcsys_wkint_mask |       | RTC_CORE.REQ_WAKEUP/   |      |
	|      |                      |       | MCU_PMU                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0]: irrrx_intr        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1]: gpio_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2]: timer0_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3]: timer1_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4]: saradc_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5]: rtcsys_ictrl_int  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6]: wdt_int           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7]: irrx_wakeup       |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | re\                  | R/W   | 1: mask vbat det int   | 0x1  |
	|      | g_vbat_det_wkup_mask |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg_sw_wkint_req     | R/W   | mcu sw wakeup          | 0x0  |
	|      |                      |       | interrupt to RTC_CORE  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: interrupt active    |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Reserved             |       |                        |      |
	| 3:17 |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | reg_wkint2rtc_mask   | R/W   | 1: mask wakeup int     | 0x1  |
	|      |                      |       | (rtcsys int) to RTC    |      |
	|      |                      |       | core                   |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Reserved             |       |                        |      |
	| 1:25 |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_clkdiv
^^^^^^^^^^^^^

.. _table_rtcsys_clkdiv:
.. table:: rtcsys_clkdiv, Offset Address: 0x03c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_div\             | R/W   | Clock Divider Factor   | 0x1  |
	|      | _clk_osc_fab_div_val |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg\                 | R/W   | Clock gate             | 0x0  |
	|      | _div_clk_osc_fab_dis |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | reg_d\               | R/W   | Select High Wide       | 0x0  |
	|      | iv_clk_osc_fab_hwide |       | Control (when Divider  |      |
	|      |                      |       | Factor is odd) 0: Low  |      |
	|      |                      |       | level of the clock is  |      |
	|      |                      |       | wider 1: High level of |      |
	|      |                      |       | the clock is wider     |      |
	+------+----------------------+-------+------------------------+------+
	| 15:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 19:16| reg_div\             | R/W   | Clock Divider Factor   | 0x1  |
	|      | _clk_osc_i2c_div_val |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | reg\                 | R/W   | Clock gate             | 0x0  |
	|      | _div_clk_osc_i2c_dis |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | reg_d\               | R/W   | Select High Wide       | 0x0  |
	|      | iv_clk_osc_i2c_hwide |       | Control (when Divider  |      |
	|      |                      |       | Factor is odd) 0: Low  |      |
	|      |                      |       | level of the clock is  |      |
	|      |                      |       | wider 1: High level of |      |
	|      |                      |       | the clock is wider     |      |
	+------+----------------------+-------+------------------------+------+
	| 23:22| Reserved             |       |                        |      |
	|      |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 29:24| reg_div_cl\          | R/W   | Clock Divider Factor   | 0x1  |
	|      | k_osc_saradc_div_val |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | reg_di\              | R/W   | Clock gate             | 0x0  |
	|      | v_clk_osc_saradc_dis |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | reg_div\_\           | R/W   | Select High Wide       | 0x0  |
	|      | clk_osc_saradc_hwide |       | Control (when Divider  |      |
	|      |                      |       | Factor is odd) 0: Low  |      |
	|      |                      |       | level of the clock is  |      |
	|      |                      |       | wider 1: High level of |      |
	|      |                      |       | the clock is wider     |      |
	+------+----------------------+-------+------------------------+------+

fc_coarse_en
^^^^^^^^^^^^

.. _table_fc_coarse_en:
.. table:: fc_coarse_en, Offset Address: 0x040
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | fc_coarse_en         | R/W   | Enable 32K coarse      | 0x0  |
	|      |                      |       | fine tuning            |      |
	|      |                      |       | 0 = disable, 1 = enable|      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

fc_coarse_cal
^^^^^^^^^^^^^

.. _table_fc_coarse_cal:
.. table:: fc_coarse_cal, Offset Address: 0x044
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | fc_coarse_value      | RO    | 32K coarse fine tuning |      |
	|      |                      |       | counter value          |      |
	|      |                      |       | (unit: 32K clock)      |      |
	|      |                      |       | 25MHz clock counts one |      |
	|      |                      |       | fc_fine period         |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| fc_coarse_time       | RO    | 32K coarse fine tuning |      |
	|      |                      |       | completion times       |      |
	+------+----------------------+-------+------------------------+------+

fc_fine_en
^^^^^^^^^^

.. _table_fc_fine_en:
.. table:: fc_fine_en, Offset Address: 0x048
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | fc_fine_en           | R/W   | Enable 32K fine tuning | 0x0  |
	|      |                      |       | 0 =disable, 1 = enable |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

fc_fine_period
^^^^^^^^^^^^^^

.. _table_fc_fine_period:
.. table:: fc_fine_period, Offset Address: 0x04c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | fc_fine_period       | R/W   | 32K fine-tuning count  |0x0100|
	|      |                      |       | cycle(unit: 32K clock) |      |
	|      |                      |       | count 32K clock cycles |      |
	|      |                      |       | each time a 25MHz      |      |
	|      |                      |       | being used             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

fc_fine_cal
^^^^^^^^^^^

.. _table_fc_fine_cal:
.. table:: fc_fine_cal, Offset Address: 0x050
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 23:0 | fc_fine_value        | RO    | 32K fine counter value |      |
	|      |                      |       | (unit 25MHz clock)     |      |
	|      |                      |       | 25MHz clock counts one |      |
	|      |                      |       | fc_fine period         |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| fc_fine_time         | RO    | 32K fine-tuning        |      |
	|      |                      |       | completion times       |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_pmu2
^^^^^^^^^^^

.. _table_rtcsys_pmu2:
.. table:: rtcsys_pmu2, Offset Address: 0x054
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg\                 | R/W   | PMU wakeup int         | 0x1  |
	|      | _rtc_sys_wkint_db_en |       | debounce enable        |      |
	+------+----------------------+-------+------------------------+------+
	| 4:1  | reg\_\               | R/W   | PMU wakeup int         | 0x2  |
	|      | rtc_sys_wkint_db_cnt |       | debounce cycle (32K)   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:5 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_clkdiv1
^^^^^^^^^^^^^^

.. _table_rtcsys_clkdiv1:
.. table:: rtcsys_clkdiv1, Offset Address: 0x058
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 21:16| reg_div\_\           | R/W   | Clock Divider Factor   | 0x0  |
	|      | clk_osc_irrx_div_val |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | reg\_\               | R/W   | Clock gate             | 0x1  |
	|      | div_clk_osc_irrx_dis |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_mcu51_dbg
^^^^^^^^^^^^^^^^

.. _table_rtcsys_mcu51_dbg:
.. table:: rtcsys_mcu51_dbg, Offset Address: 0x05c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_51_dbg_sel       | R/W   | select mcu51 debug bus | 0x0  |
	|      |                      |       | (check mcu design      |      |
	|      |                      |       | review ppt)            |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_51_dbg_snap_shot | W1P   | snap shot mcu51        |      |
	|      |                      |       | internal register to   |      |
	|      |                      |       | dbg register           |      |
	|      |                      |       | (reg_rtcsys_dbg)       |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | reg_51_dbg_step_en   | R/W   | 0: disable mcu debug   | 0x0  |
	|      |                      |       | function               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: enable mcu debug    |      |
	|      |                      |       | function, and mcu stop |      |
	|      |                      |       | at current PC          |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | reg_51_dbg_step      | W1P   | 1: mcu jump to next PC |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | reg_51_dbg_jump      | W1P   | 1: mcu jump to target  |      |
	|      |                      |       | pc value               |      |
	|      |                      |       | (reg_51_dbg_jump2pc)   |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg_51_dbg_jump2pc   | R/W   | 16 bit mcu target pc   | 0x0  |
	|      |                      |       | value                  |      |
	+------+----------------------+-------+------------------------+------+

sw_reg0
^^^^^^^

.. _table_sw_reg0:
.. table:: sw_reg0, Offset Address: 0x060
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | sw_reg0              | R/W   | reg for SW             | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

sw_reg1_por
^^^^^^^^^^^

.. _table_sw_reg1_por:
.. table:: sw_reg1_por, Offset Address: 0x064
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | sw_reg1_por          | R/W   | reg for SW could only  | 0x0  |
	|      |                      |       | be reset by power      |      |
	|      |                      |       | reset                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

fab_lp_ctrl
^^^^^^^^^^^

.. _table_fab_lp_ctrl:
.. table:: fab_lp_ctrl, Offset Address: 0x068
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | rtcsys_fab_busy_sel  | R/W   | select signal to       | 0xDF |
	|      |                      |       | request sys_ctrl to    |      |
	|      |                      |       | speed up fab clock     |      |
	+------+----------------------+-------+------------------------+------+
	| 9:8  | rtcsys_fab_busy_ctrl | R/W   | rtcsys_fab_busy signal | 0x0  |
	|      |                      |       | is combi or register   |      |
	|      |                      |       | out                    |      |
	+------+----------------------+-------+------------------------+------+
	| 11:10| apdbg_busy_ctrl      | R/W   | apdbg_busy signal is   | 0x0  |
	|      |                      |       | combi or register out  |      |
	+------+----------------------+-------+------------------------+------+
	| 13:12| reg_apb_busy_ctrl    | R/W   | apb bridge_busy signal | 0x3  |
	|      |                      |       | is combi or register   |      |
	|      |                      |       | out                    |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| reg_mcu_busy_ctrl    | R/W   | mcu_busy signal is     | 0x3  |
	|      |                      |       | combi or register out  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_mcu51_ictrl1
^^^^^^^^^^^^^^^^^^^

.. _table_rtcsys_mcu51_ictrl1:
.. table:: rtcsys_mcu51_ictrl1, Offset Address: 0x07c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_51_int1_src_mask | R/W   | select rtcsys_int src  |0xffff|
	|      |                      |       | to mcu int1_n          |      |
	|      |                      |       | 1: mask, 0: un-mask    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0]: vbat_det          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1]: mbox0_int         |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2]: NA                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3]: irrx_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4]: gpio_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5]: uart_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6]: spinor1_int       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7]: timer0_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [8]: timer1_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [9]: irq_ap2rtc[0]     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [10]: irq_ap2rtc[1]    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [11]: i2c_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [12]:                  |      |
	|      |                      |       | rtc_state_change_int   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [13]: hw_thm_shdn      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [14]: saradc           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [15]: wdt_int          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg\_\               | R0    | mcu int1_n status      |      |
	|      | 51_int1_final_status |       |                        |      |
	|      |                      |       | [0]: vbat_det          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1]: mbox0_int         |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2]: NA                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3]: irrx_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4]: gpio_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5]: uart_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6]: spinor1_int       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7]: timer0_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [8]: timer1_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [9]: irq_ap2rtc[0]     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [10]: irq_ap2rtc[1]    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [11]: i2c_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [12]:                  |      |
	|      |                      |       | rtc_state_change_int   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [13]: hw_thm_shdn      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [14]: saradc           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [15]: wdt_int          |      |
	+------+----------------------+-------+------------------------+------+

rtc_ip_pwr_req
^^^^^^^^^^^^^^

.. _table_rtc_ip_pwr_req:
.. table:: rtc_ip_pwr_req, Offset Address: 0x080
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg_sd1_pwr_req      | R/W   | power fence control    | 0x1  |
	|      |                      |       |                        |      |
	|      |                      |       | 1: power on, 0: power  |      |
	|      |                      |       | off                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0]: sd1               |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_sd1_pwr_req_2nd  | R/W   | power fence control    | 0x1  |
	|      |                      |       |                        |      |
	|      |                      |       | 1: power on, 0: power  |      |
	|      |                      |       | off                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0]: sd1               |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg_mcu_pwr_req      | R/W   | power fence control    | 0x1  |
	|      |                      |       |                        |      |
	|      |                      |       | 1: power on, 0: power  |      |
	|      |                      |       | off                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1]: mcu subsys        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg_mcu_pwr_req_2nd  | R/W   | power fence control    | 0x1  |
	|      |                      |       |                        |      |
	|      |                      |       | 1: power on, 0: power  |      |
	|      |                      |       | off                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1]: mcu subsys        |      |
	+------+----------------------+-------+------------------------+------+
	| 15:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg_sd1_pwr_ack      | R0    | power fence power      |      |
	|      |                      |       | status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: power on, 0: power  |      |
	|      |                      |       | off                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0]: sd1               |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | reg_sd1_pwr_ack_2nd  | R0    | power fence power      |      |
	|      |                      |       | status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: power on, 0: power  |      |
	|      |                      |       | off                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0]: sd1               |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | reg_mcu_pwr_ack      | R0    | power fence power      |      |
	|      |                      |       | status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: power on, 0: power  |      |
	|      |                      |       | off                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1]: mcu subsys        |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | reg_mcu_pwr_ack_2nd  | R0    | power fence power      |      |
	|      |                      |       | status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: power on, 0: power  |      |
	|      |                      |       | off                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1]: mcu subsys        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:20| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtc_ip_iso_ctrl
^^^^^^^^^^^^^^^

.. _table_rtc_ip_iso_ctrl:
.. table:: rtc_ip_iso_ctrl, Offset Address: 0x084
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg_sd1_iso_en       | R/W   | sd1 iso enablel        | 0x0  |
	|      |                      |       | 1: iso enable, 0: iso  |      |
	|      |                      |       | disable                |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_mcu_iso_en       | R/W   | mcu iso enablel        | 0x0  |
	|      |                      |       | 1: iso enable, 0: iso  |      |
	|      |                      |       | disable                |      |
	+------+----------------------+-------+------------------------+------+
	| 15:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 17:16| reg_ip_por_en        | R/W   | 1: pwr_island reset    | 0x3  |
	|      |                      |       | assert when power ack  |      |
	|      |                      |       | is 0                   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:18| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_wkup_ctrl1
^^^^^^^^^^^^^^^^^

.. _table_rtcsys_wkup_ctrl1:
.. table:: rtcsys_wkup_ctrl1, Offset Address: 0x094
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | reg_rtcsy\           | RO    | wkint final status     |      |
	|      | s_wkint_final_status |       |                        |      |
	|      |                      |       | [0]: sd1_wakeup_intr   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1]: gpio_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2]: timer0_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3]: timer1_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4]: saradc_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5]: rtcsys_ictrl_int  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6]: NA                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7]: NA                |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_sram_ctrl
^^^^^^^^^^^^^^^^

.. _table_rtcsys_sram_ctrl:
.. table:: rtcsys_sram_ctrl, Offset Address: 0x098
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg_ahb_sram_slp     | R/W   | 1 : ahb sram into      | 0x0  |
	|      |                      |       | sleep mode             |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_ahb_sram_sd      | R/W   | 1 : ahb sram into shut | 0x0  |
	|      |                      |       | down mode              |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg_ahb_sram_ctrl_ov | R/W   | 0 : ahb sram ctrl by   | 0x1  |
	|      |                      |       | PMU FSM and ahb sram   |      |
	|      |                      |       | busy                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: sram ctrol by       |      |
	|      |                      |       | register               |      |
	|      |                      |       | reg_ahb_sr             |      |
	|      |                      |       | am_slp/reg_ahb_sram_sd |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg_sdio_sram_slp    | R/W   | 1 : sdio sram into     | 0x0  |
	|      |                      |       | sleep mode             |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_sdio_sram_sd     | R/W   | 1 : sdio sram into     | 0x0  |
	|      |                      |       | shut down mode         |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | r\                   | R/W   | 0 : sram's sd pin =    | 0x1  |
	|      | eg_sdio_sram_ctrl_ov |       | 1'b0                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: sram ctrol by       |      |
	|      |                      |       | register               |      |
	|      |                      |       | reg_sdio_sram_sd       |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | reg_mcu_sram_slp     | R/W   | 1 : mcu iram sram into | 0x0  |
	|      |                      |       | sleep mode             |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | reg_mcu_sram_sd      | R/W   | 1 : mcu iram sram into | 0x0  |
	|      |                      |       | shut down mode         |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg_mcu_sram_ctrl_ov | R/W   | 0 : mcu iram sram ctrl | 0x1  |
	|      |                      |       | by PMU FSM             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: sram ctrol by       |      |
	|      |                      |       | register               |      |
	|      |                      |       | reg_ahb_sr             |      |
	|      |                      |       | am_slp/reg_ahb_sram_sd |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | reg_rtc_sram_slp     | R/W   | 1 : mcu iram sram into | 0x0  |
	|      |                      |       | sleep mode             |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | reg_rtc_sram_sd      | R/W   | 1 : mcu iram sram into | 0x0  |
	|      |                      |       | shut down mode         |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | reg_rtc_sram_ctrl_ov | R/W   | 0 : mcu iram sram ctrl | 0x1  |
	|      |                      |       | by PMU FSM             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: sram ctrol by       |      |
	|      |                      |       | register               |      |
	|      |                      |       | reg_ahb_sr             |      |
	|      |                      |       | am_slp/reg_ahb_sram_sd |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Reserved             |       |                        |      |
	| 7:12 |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | r\                   | R/W   | 1: force mcu_iram cs = | 0x1  |
	|      | eg_mcu_sram_force_ce |       | 1                      |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Reserved             |       |                        |      |
	| 1:29 |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_io_ctrl
^^^^^^^^^^^^^^

.. _table_rtcsys_io_ctrl:
.. table:: rtcsys_io_ctrl, Offset Address: 0x09c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg_i2c_mux_opt0     | R/W   | 0: pwr_gpio6/8 control | 0x0  |
	|      |                      |       | by dw_gpio             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: pwr_gpio6 is        |      |
	|      |                      |       | PWR_IIC_SDA            |      |
	|      |                      |       | pwr_gpio8 is           |      |
	|      |                      |       | PWR_IIC_SCL            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_wdt_ctrl
^^^^^^^^^^^^^^^

.. _table_rtcsys_wdt_ctrl:
.. table:: rtcsys_wdt_ctrl, Offset Address: 0x0a0
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | r\                   | R/W   | 0: disable rtc wdt     | 0x0  |
	|      | eg_rtc_hw_wdg_rst_en |       | trigger warm reset or  |      |
	|      |                      |       | pwrcyc reset           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: enable rtc wdt      |      |
	|      |                      |       | trigger warm reset or  |      |
	|      |                      |       | pwrcyc reset           |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg\_\               | R/W   | no load                | 0x1  |
	|      | rtc_wdt_ctrl_mask_en |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_irrx_clk_ctrl
^^^^^^^^^^^^^^^^^^^^

.. _table_rtcsys_irrx_clk_ctrl:
.. table:: rtcsys_irrx_clk_ctrl, Offset Address: 0x0a4
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg\_\               | R/W   | force on clk ctrl of   | 0x1  |
	|      | irrx_clk_sw_force_on |       | irrx                   |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_irrx_xtal_req_en | R/W   | enable irrx clk ctrl   | 0x0  |
	|      |                      |       | requet XTAL            |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg_irrx_osc_req_en  | R/W   | enable irrx clk ctrl   | 0x0  |
	|      |                      |       | requet OSC             |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg_irrx_ldo_req_en  | R/W   | enable irrx clk ctrl   | 0x0  |
	|      |                      |       | requet LDO             |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | reg\_\               | R/W   | irrx xtal filter cycle | 0x40 |
	|      | irrx_xtal_filter_cyc |       | (default 2ms)          |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_irrx_clk_ctrl_st | RO    | irrx clock ctrol state |      |
	| 9:16 |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Reserved             |       |                        |      |
	| 1:20 |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_rtc_wkup_ctrl
^^^^^^^^^^^^^^^^^^^^

.. _table_rtcsys_rtc_wkup_ctrl:
.. table:: rtcsys_rtc_wkup_ctrl, Offset Address: 0x0a8
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | reg_rtc_wkint_mask   | R/W   | wakeup source mask int | 0xff |
	|      |                      |       | to RTC_CORE            |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0]: irrrx_intr        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1]: gpio_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2]: timer0_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3]: timer1_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4]: saradc_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5]: rtcsys_ictrl_int  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6]: wdt_int           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7]: irrx_wakeup       |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 23:16| reg_rtc_puint_mask   | R/W   | power-up source mask   | 0xff |
	|      |                      |       | int to RTC_CORE        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0]: irrrx_intr        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1]: gpio_int          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2]: timer0_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3]: timer1_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4]: saradc_int        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5]: rtcsys_ictrl_int  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6]: wdt_int           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7]: irrx_wakeup       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

rtcsys_por_rst_ctrl
^^^^^^^^^^^^^^^^^^^

.. _table_rtcsys_por_rst_ctrl:
.. table:: rtcsys_por_rst_ctrl, Offset Address: 0x0ac
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg_rtcsys_reset_en  | R/W   | 0: not allow rtcsys    | 0x0  |
	|      |                      |       | reset by pwr cyc/ wdt  |      |
	|      |                      |       | warm reset             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : allow rtcsys reset |      |
	|      |                      |       | by pwr cyc/ wdt warm   |      |
	|      |                      |       | reset                  |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg\                 | R/W   | select rtcsys rstn src | 0x0  |
	|      | _rtcsys_rstn_src_sel |       | 0: rtc_core fsm (reset |      |
	|      |                      |       | with die domain)       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: por_pwr_rstn        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

