KEYSCAN_CONFIG0
^^^^^^^^^^^^^^^

.. _table_keyscan_config0:
.. table:: KEYSCAN_CONFIG0, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 7:0  | reg_row_mask         | R/W   | ROW[7:0] Mask          | 0xff |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | reg_col_mask         | R/W   | COL[7:0] Mask          | 0xff |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg_enable           | R/W   | keyscan enable         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = disable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = enable             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:17| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

KEYSCAN_CONFIG0
^^^^^^^^^^^^^^^

.. _table_keyscan_config1:
.. table:: KEYSCAN_CONFIG1, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | reg_slow_div         | R/W   | slow divider (MUST BE  | 0xff |
	|      |                      |       | BIGGER THAN            |      |
	|      |                      |       | reg_db_col)            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Each step is IP clock  |      |
	|      |                      |       | frequency divide by    |      |
	|      |                      |       | reg_slow_div           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Scan frequency = IP    |      |
	|      |                      |       | clock freq / (         |      |
	|      |                      |       | (reg_slow_div+1) \*    |      |
	|      |                      |       | (9+reg_wait_count+1))  |      |
	|      |                      |       |                        |      |
	|      |                      |       | IDLE -> ROW0 -> ROW1   |      |
	|      |                      |       | ->                     |      |
	|      |                      |       | ROW2->ROW3             |      |
	|      |                      |       | ->ROW4->ROW5->ROW6->RO |      |
	|      |                      |       | W7->UPDATE->WAIT->IDLE |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

KEYSCAN_CONFIG2
^^^^^^^^^^^^^^^

.. _table_keyscan_config2:
.. table:: KEYSCAN_CONFIG2, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 15:0 | reg_db_col           | R/W   | column input debounce  | 0x64 |
	|      |                      |       | counter (IP clock      |      |
	|      |                      |       | cycle)                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

KEYSCAN_CONFIG3
^^^^^^^^^^^^^^^

.. _table_keyscan_config3:
.. table:: KEYSCAN_CONFIG3, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 7:0  | reg_wait_cntr        | R/W   | wait interval between  | 0x10 |
	|      |                      |       | each scan (unit is     |      |
	|      |                      |       | reg_slow_div count)    |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

KEYSCAN_SNAPSHOT_ARRAY
^^^^^^^^^^^^^^^^^^^^^^

.. _table_keyscan_snapshot_array:
.. table:: KEYSCAN_SNAPSHOT_ARRAY, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 63:0 | re\                  | RO    | CPU snapshot array     |      |
	|      | g_cpu_snapshot_array |       | result (0 = press, 1 = |      |
	|      |                      |       | not press)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] = Row 0 , Col 0    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] = Row 0 , Col 1    |      |
	|      |                      |       |                        |      |
	|      |                      |       | ...                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7] = Row 0, Col 7     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [8] = Row 1, Col 0     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [63] = Row 7, Col 7    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [N] = Row Y, Col X (N  |      |
	|      |                      |       | = Y*8 + X)             |      |
	+------+----------------------+-------+------------------------+------+

KEYSCAN_SNAPSHOT_TRIG
^^^^^^^^^^^^^^^^^^^^^

.. _table_keyscan_snapshot_trig:
.. table:: KEYSCAN_SNAPSHOT_TRIG, Offset Address: 0x01c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg\                 | W1T   | Write 1 to Trigger     |      |
	|      | _cpu_snapshot_toggle |       | snapshot array to      |      |
	|      |                      |       | update                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | When current result is |      |
	|      |                      |       | different from         |      |
	|      |                      |       | snapshot result, irq   |      |
	|      |                      |       | happen                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | To solve the IRQ,      |      |
	|      |                      |       | write 1 to trigger the |      |
	|      |                      |       | snapshot array to copy |      |
	|      |                      |       | from current array and |      |
	|      |                      |       | start checking which   |      |
	|      |                      |       | bit is different from  |      |
	|      |                      |       | previous state         |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

KEYSCAN_FIFO_STATUS
^^^^^^^^^^^^^^^^^^^

.. _table_keyscan_fifo_status:
.. table:: KEYSCAN_FIFO_STATUS, Offset Address: 0x020
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 3:0  | reg_fifo_count       | RO    | FIFO content count     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Empty              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = one content in     |      |
	|      |                      |       | FIFO                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | N = N content in FIFO  |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_fifo_not_empty   | RO    | FIFO not empty flag    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Empty              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Not empty          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:5 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

KEYSCAN_FIFO
^^^^^^^^^^^^

.. _table_keyscan_fifo:
.. table:: KEYSCAN_FIFO, Offset Address: 0x024
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 6:0  | reg_fifo_rdata       | ROC   | read data from FIFO    |      |
	|      |                      |       | (Auto POP) - check     |      |
	|      |                      |       | FIFO empty-ness before |      |
	|      |                      |       | read                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6] 0 = press, 1 =     |      |
	|      |                      |       | not-press              |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5:0] = index          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Row = INT(index/8)     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Col = mod(index,8)     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 63 = Row 7 , Column 7  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 13 = Row 1 , Clumne 5  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:7 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

KEYSCAN_IRQ_ENABLE
^^^^^^^^^^^^^^^^^^

.. _table_keyscan_irq_enable:
.. table:: KEYSCAN_IRQ_ENABLE, Offset Address: 0x028
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_irq_f\           | R/W   | FIFO mode IRQ Enable   | 0x0  |
	|      | ifo_not_empty_enable |       |                        |      |
	|      |                      |       | 0 = Disable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Enable             |      |
	+------+----------------------+-------+------------------------+------+
	| 3:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_irq_sn\          | R/W   | Snapshot mode IRQ      | 0x0  |
	|      | apshot_change_enable |       | Enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Disable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Enable             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:5 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

KEYSCAN_IRQ_FLAG
^^^^^^^^^^^^^^^^

.. _table_keyscan_irq_flag:
.. table:: KEYSCAN_IRQ_FLAG, Offset Address: 0x02c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | re\                  | RO    | FIFO not empty IRQ     |      |
	|      | g_irq_fifo_not_empty |       | flag                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Empty              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Not empty          |      |
	+------+----------------------+-------+------------------------+------+
	| 3:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg\                 | RO    | Snapshot change IRQ    |      |
	|      | _irq_snapshot_change |       | flag                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = No change          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Change             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:5 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

KEYSCAN_IRQ_CLEAR
^^^^^^^^^^^^^^^^^

.. _table_keyscan_irq_clear:
.. table:: KEYSCAN_IRQ_CLEAR, Offset Address: 0x030
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_irq_fifo\        | W1T   | FIFO not empty IRQ     |      |
	|      | _not_empty_clear_w1t |       | Clear (Write 1 clear)  |      |
	+------+----------------------+-------+------------------------+------+
	| 3:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_irq_snaps\       | W1T   | Snapshot Change IRQ    |      |
	|      | hot_change_clear_w1t |       | Clear (Write 1 clear)  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:5 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
