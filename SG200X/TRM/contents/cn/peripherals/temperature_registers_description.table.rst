tempsen_version
^^^^^^^^^^^^^^^

.. _table_tempsen_version:
.. table:: tempsen_version, BassAddress: 0x000
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | reg_ip_version       | RO    | verision 1.0           |      |
	+------+----------------------+-------+------------------------+------+

tempsen_ctrl
^^^^^^^^^^^^

.. _table_tempsen_ctrl:
.. table:: tempsen_ctrl, BassAddress: 0x004
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_tempsen_en       | R/W   | when re_tempsen_en is  | 0x0  |
	|      |                      |       | set , tempsen start to |      |
	|      |                      |       | measure the channel    |      |
	|      |                      |       | set in reg_tempsen_sel |      |
	+------+----------------------+-------+------------------------+------+
	| 3:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | reg_tempsen_sel      | R/W   | temperature sense      | 0x0  |
	|      |                      |       | channel selection      |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 23:16| reg_tem\             | R/W   | counting threshold of  | 0x8  |
	|      | psen_ovhl_cnt_to_irq |       | high temperature       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| reg_tem\             | R/W   | counting threshold of  | 0x8  |
	|      | psen_udll_cnt_to_irq |       | low temperature        |      |
	+------+----------------------+-------+------------------------+------+

tempsen_status
^^^^^^^^^^^^^^

.. _table_tempsen_status:
.. table:: tempsen_ctrl, BassAddress: 0x008
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | sta_tempsen_busy     | RO    | busy status rise when  |      |
	|      |                      |       | re_tempsen_en is set   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

tempsen_set
^^^^^^^^^^^

.. _table_tempsen_set:
.. table:: tempsen_set, BassAddress: 0x00c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_tempsen_bgen     | R/W   | sensor macro bandgap   | 0x0  |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_tempsen_chopen   | R/W   | sensor macro chopper   | 0x1  |
	|      |                      |       | function enable        |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg_tempsen_choppol  | R/W   | sensor macro chopper   | 0x1  |
	|      |                      |       | polarity when CHOPEN=0 |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg_tempsen_clkpol   | R/W   | sensor macro clock     | 0x1  |
	|      |                      |       | polarity when          |      |
	|      |                      |       | DA_TEMPSEN_EN=0        |      |
	+------+----------------------+-------+------------------------+------+
	| 5:4  | reg_tempsen_chopsel  | R/W   | sensor macro chop      | 0x2  |
	|      |                      |       | period, 0:128T,        |      |
	|      |                      |       | 1:256T, 2:512T,        |      |
	|      |                      |       | 3:1024T                |      |
	+------+----------------------+-------+------------------------+------+
	| 7:6  | reg_tempsen_accsel   | R/W   | sensor macro           | 0x1  |
	|      |                      |       | accumulate period,     |      |
	|      |                      |       | 0:512T, 1:1024T,       |      |
	|      |                      |       | 2:2048T, 3:4096T       |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | re\                  | R/W   | clock divider for      | 0xB  |
	|      | g_tempsen_cyc_clkdiv |       | sensor macro, freq =   |      |
	|      |                      |       | ip_clk/(1+clk_div) ,   |      |
	|      |                      |       | default is 25M/12      |      |
	|      |                      |       | =2.083M , T = 0.48us   |      |
	+------+----------------------+-------+------------------------+------+
	| 17:16| reg_tempsen_tsel     | R/W   | sensor macro test      | 0x0  |
	|      |                      |       | selection, please keep |      |
	|      |                      |       | 0                      |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | reg\                 | R/W   | sensor macro test      | 0x0  |
	|      | _tempsen_en_bjt_test |       | selection, please keep |      |
	|      |                      |       | 0                      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:19| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

tempsen_intr_en
^^^^^^^^^^^^^^^

.. _table_tempsen_intr_en:
.. table:: tempsen_intr_en, BassAddress: 0x010
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | sta_tempsen_intr_en  | R/W   | interrupt enable       | 0x0  |
	+------+----------------------+-------+------------------------+------+

tempsen_intr_clr
^^^^^^^^^^^^^^^^

.. _table_tempsen_intr_clr:
.. table:: tempsen_intr_clr, BassAddress: 0x014
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | sta_tempsen_intr_clr | RWC   | interrupt clear        |      |
	+------+----------------------+-------+------------------------+------+

tempsen_intr_sta
^^^^^^^^^^^^^^^^

.. _table_tempsen_intr_sta:
.. table:: tempsen_intr_clr, BassAddress: 0x018
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | sta_tempsen_intr_sta | RO    | interrupt masked       |      |
	|      |                      |       | status                 |      |
	+------+----------------------+-------+------------------------+------+

tempsen_intr_raw
^^^^^^^^^^^^^^^^

.. _table_tempsen_intr_raw:
.. table:: tempsen_intr_raw, BassAddress: 0x01c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | sta_tempsen_intr_raw | RO    | interrupt raw status:  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3:0] ch3~ch0          |      |
	|      |                      |       | measurement finish     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7:4] ch3~ch0          |      |
	|      |                      |       | measurement result is  |      |
	|      |                      |       | higher than high       |      |
	|      |                      |       | temperature threshold  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [11:8] ch3~ch0         |      |
	|      |                      |       | measurement result is  |      |
	|      |                      |       | lower than low         |      |
	|      |                      |       | temperature threshold  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [15:12] ch3~ch0's high |      |
	|      |                      |       | temperature event      |      |
	|      |                      |       | count is more than     |      |
	|      |                      |       | threshold              |      |
	|      |                      |       |                        |      |
	|      |                      |       | [19:16] ch3~ch0's low  |      |
	|      |                      |       | temperature event      |      |
	|      |                      |       | count is more than     |      |
	|      |                      |       | threshold              |      |
	|      |                      |       |                        |      |
	|      |                      |       | [23:20] ch3~ch0        |      |
	|      |                      |       | measurement result is  |      |
	|      |                      |       | higher than overheat   |      |
	|      |                      |       | temperature            |      |
	+------+----------------------+-------+------------------------+------+

tempsen_ch0_result
^^^^^^^^^^^^^^^^^^

.. _table_tempsen_ch0_result:
.. table:: tempsen_intr_raw, BassAddress: 0x020
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 12:0 | st\                  | RO    | channel 0 current      |      |
	|      | a_tempsen_ch0_result |       | temperature            |      |
	|      |                      |       | measurement result     |      |
	+------+----------------------+-------+------------------------+------+
	| 15:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28:16| sta_te\              | RO    | channel 0 max          |      |
	|      | mpsen_ch0_max_result |       | temperature            |      |
	|      |                      |       | measurement result     |      |
	+------+----------------------+-------+------------------------+------+
	| 30:29| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | clr_te\              | RWC   | write 1 to clear       |      |
	|      | mpsen_ch0_max_result |       | channel 0 max          |      |
	|      |                      |       | temperature            |      |
	|      |                      |       | measurement result     |      |
	+------+----------------------+-------+------------------------+------+

tempsen_ch1_result
^^^^^^^^^^^^^^^^^^

.. _table_tempsen_ch1_result:
.. table:: tempsen_ch1_result, BassAddress: 0x024
	:widths: 1 3 1 4 1


	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 12:0 | st\                  | RO    | channel 1 current      |      |
	|      | a_tempsen_ch1_result |       | temperature            |      |
	|      |                      |       | measurement result     |      |
	+------+----------------------+-------+------------------------+------+
	| 15:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28:16| sta_te\              | RO    | channel 1 max          |      |
	|      | mpsen_ch1_max_result |       | temperature            |      |
	|      |                      |       | measurement result     |      |
	+------+----------------------+-------+------------------------+------+
	| 30:29| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | clr_te\              | RWC   | write 1 to clear       |      |
	|      | mpsen_ch1_max_result |       | channel 1 max          |      |
	|      |                      |       | temperature            |      |
	|      |                      |       | measurement result     |      |
	+------+----------------------+-------+------------------------+------+

tempsen_ch0_temp_th
^^^^^^^^^^^^^^^^^^^

.. _table_tempsen_ch0_temp_th:
.. table:: tempsen_ch0_temp_th, BassAddress: 0x040
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 12:0 | r\                   | R/W   | channel 0 high         | 0x0  |
	|      | eg_tempsen_ch0_hi_th |       | temperature threshold  |      |
	|      |                      |       | to trigger interrupt   |      |
	+------+----------------------+-------+------------------------+------+
	| 15:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28:16| r\                   | R/W   | channel 0 low          | 0x0  |
	|      | eg_tempsen_ch0_lo_th |       | temperature threshold  |      |
	|      |                      |       | to trigger interrupt   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:29| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

tempsen_ch1_temp_th
^^^^^^^^^^^^^^^^^^^

.. _table_tempsen_ch1_temp_th:
.. table:: tempsen_ch1_temp_th, BassAddress: 0x044
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 12:0 | r\                   | R/W   | channel 1 high         | 0x0  |
	|      | eg_tempsen_ch1_hi_th |       | temperature threshold  |      |
	|      |                      |       | to trigger interrupt   |      |
	+------+----------------------+-------+------------------------+------+
	| 15:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28:16| r\                   | R/W   | channel 1 low          | 0x0  |
	|      | eg_tempsen_ch1_lo_th |       | temperature threshold  |      |
	|      |                      |       | to trigger interrupt   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:29| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

Overheat_th
^^^^^^^^^^^

.. _table_overheat_th:
.. table:: Overheat_th, BassAddress: 0x060
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 12:0 | reg\                 | R/W   | overheat temperature   | 0x0  |
	|      | _tempsen_overheat_th |       | threshold              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


tempsen_auto_period
^^^^^^^^^^^^^^^^^^^

.. _table_tempsen_auto_period:
.. table:: tempsen_auto_period, BassAddress: 0x064
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | re\                  | R/W   | auto measure period.   | 0x0  |
	|      | g_tempsen_auto_cycle |       | T_measure =            |      |
	|      |                      |       | reg_temps\             |      |
	|      |                      |       | en_auto_cycle*T_prediv |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| reg\                 | R/W   | a predivider setting   | 0x18 |
	|      | _tempsen_auto_prediv |       | for auto measure       |      |
	|      |                      |       | period. T_prediv =     |      |
	|      |                      |       | (25M/(                 |      |
	|      |                      |       | reg_t\                 |      |
	|      |                      |       | empsen_auto_prediv+1)) |      |
	+------+----------------------+-------+------------------------+------+

tempsen_overheat_ctrl
^^^^^^^^^^^^^^^^^^^^^

.. _table_tempsen_overheat_ctrl:
.. table:: tempsen_overheat_ctrl, BassAddress: 0x068
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 29:0 | reg_te\              | R/W   | After overheat event   | 0x10 |
	|      | mpsen_overheat_cycle |       | happens, the cycle     | 0000 |
	|      |                      |       | count will be load to  |      |
	|      |                      |       | a counter and trigger  |      |
	|      |                      |       | counting down. when    |      |
	|      |                      |       | counting down to 1, a  |      |
	|      |                      |       | reset signal will be   |      |
	|      |                      |       | issue to power control |      |
	|      |                      |       | unit.                  |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | re\                  | RWC   | write 1 to stop        |      |
	|      | g_overheat_reset_clr |       | overheat reset         |      |
	|      |                      |       | counting.              |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | r\                   | R/W   | enable overheat reset  | 0x0  |
	|      | eg_overheat_reset_en |       | counting down.         |      |
	+------+----------------------+-------+------------------------+------+

tempsen_overheat_countdown
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_tempsen_overheat_countdown:
.. table:: tempsen_overheat_countdown, BassAddress: 0x06c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 29:0 | sta_tempse\          | RO    | overheat reset counter |      |
	|      | n_overheat_countdown |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | sta_overheat_reset   | RO    | overheat reset signal  |      |
	|      |                      |       | status                 |      |
	+------+----------------------+-------+------------------------+------+

tempsen_ch0_temp_th_cnt
^^^^^^^^^^^^^^^^^^^^^^^

.. _table_tempsen_ch0_temp_th_cnt:
.. table:: tempsen_ch0_temp_th_cnt, BassAddress: 0x070
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 7:0  | sta_ch0\             | RO    | channel 0 high         |      |
	|      | _over_hi_temp_th_cnt |       | temperature event      |      |
	|      |                      |       | count status           |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | sta_ch0_under\       | RO    | channel 0 low          |      |
	|      | _lo_temp_th_cnt      |       | temperature event      |      |
	|      |                      |       | count status           |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg\                 | RWC   | write 1 to clear       |      |
	|      | _ch0_temp_th_cnt_clr |       | channel 0 temperature  |      |
	|      |                      |       | event count            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:17| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

tempsen_ch1_temp_th_cnt
^^^^^^^^^^^^^^^^^^^^^^^

.. _table_tempsen_ch1_temp_th_cnt:
.. table:: tempsen_ch1_temp_th_cnt, BassAddress: 0x074
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 7:0  | sta_ch1\             | RO    | channel 1 high         |      |
	|      | _over_hi_temp_th_cnt |       | temperature event      |      |
	|      |                      |       | count status           |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | sta_ch1_under\       | RO    | channel 1 low          |      |
	|      | _lo_temp_th_cnt      |       | temperature event      |      |
	|      |                      |       | count status           |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg\                 | RWC   | write 1 to clear       |      |
	|      | _ch1_temp_th_cnt_clr |       | channel 1 temperature  |      |
	|      |                      |       | event count            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:17| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
