.. _table_tempsensor_interrupt_describe:
.. table:: Tempsensor Interrupt Signal Description
	:widths: 2 4 4

	+------+---------------------+--------------------------+
	| Bit  | Signal              | Description              |
	+======+=====================+==========================+
	| [0]  | Irq_Temp0_measure   | Tempsens0 measurement    |
	|      |                     | completed.               |
	+------+---------------------+--------------------------+
	| [1]  | Irq_Temp1_measure   | Tempsens1 measurement    |
	|      |                     | completed.               |
	+------+---------------------+--------------------------+
	| [2]  | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [3]  | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [4]  | Irq_Te\             | Tempsens0                |
	|      | mp0_over_high_level | The temperature is       |
	|      |                     | greater than or equal to |
	|      |                     | the high temperature     |
	|      |                     | critical value.          |
	+------+---------------------+--------------------------+
	| [5]  | Irq_Te\             | Tempsens1                |
	|      | mp1_over_high_level | The temperature is       |
	|      |                     | greater than or equal to |
	|      |                     | the high temperature     |
	|      |                     | critical value.          |
	+------+---------------------+--------------------------+
	| [6]  | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [7]  | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [8]  | Irq_Te\             | Tempsens0                |
	|      | mp0_under_low_level | The temperature is less  |
	|      |                     | than or equal to the low |
	|      |                     | temperature critical     |
	|      |                     | value.                   |
	+------+---------------------+--------------------------+
	| [9]  | Irq_Te\             | Tempsens1                |
	|      | mp1_under_low_level | The temperature is less  |
	|      |                     | than or equal to the low |
	|      |                     | temperature critical     |
	|      |                     | value.                   |
	+------+---------------------+--------------------------+
	| [10] | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [11] | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [12] | Irq_T\              | The number of times the  |
	|      | emp0_over_high_cont | Tempsens0 temperature is |
	|      |                     | greater than or equal to |
	|      |                     | the high temperature     |
	|      |                     | critical value has       |
	|      |                     | reached the value of     |
	|      |                     | reg_tempsen_ovhl_cnt_to\ |
	|      |                     | _irq.                    |
	+------+---------------------+--------------------------+
	| [13] | Irq_T\              | The number of times the  |
	|      | emp1_over_high_cont | Tempsens1 temperature is |
	|      |                     | greater than or equal to |
	|      |                     | the high temperature     |
	|      |                     | critical value has       |
	|      |                     | reached the value of     |
	|      |                     | reg_tempsen_ovhl_cnt_to\ |
	|      |                     | _irq.                    |
	+------+---------------------+--------------------------+
	| [14] | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [15] | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [16] | Irq_T\              | The number of times the  |
	|      | emp0_under_low_cont | temperature of Tempsens0 |
	|      |                     | is less than or equal to |
	|      |                     | the low temperature      |
	|      |                     | critical value has       |
	|      |                     | reached the value of     |
	|      |                     | reg_tempsen_udll_cnt_to\ |
	|      |                     | _irq.                    |
	+------+---------------------+--------------------------+
	| [17] | Irq_T\              | The number of times the  |
	|      | emp1_under_low_cont | temperature of Tempsens1 |
	|      |                     | is less than or equal to |
	|      |                     | the low temperature      |
	|      |                     | critical value has       |
	|      |                     | reached the value of     |
	|      |                     | reg_tempsen_udll_cnt_to\ |
	|      |                     | _irq.                    |
	+------+---------------------+--------------------------+
	| [18] | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [19] | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [20] | Irq_Temp0_overheat  | The temperature of       |
	|      |                     | Tempsens0 is greater than|
	|      |                     | or equal to the          |
	|      |                     | overheating critical     |
	|      |                     | value.                   |
	+------+---------------------+--------------------------+
	| [21] | Irq_Temp1_overheat  | The temperature of       |
	|      |                     | Tempsens1 is greater than|
	|      |                     | or equal to the          |
	|      |                     | overheating critical     |
	|      |                     | value.                   |
	+------+---------------------+--------------------------+
	| [22] | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
	| [23] | reserved            | Reserved                 |
	+------+---------------------+--------------------------+
