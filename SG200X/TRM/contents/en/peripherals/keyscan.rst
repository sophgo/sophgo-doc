KeyScan
-------

Overview
~~~~~~~~

Keyscan supports a matrix of up to 8 x 8 = 64 keys. If you don't need so many keys, you can freely decide which rows or columns to mask or retain. Depending on the software needs, snapshot mode and FIFO mode can be selected to obtain key information.

Way of Working
~~~~~~~~~~~~~~

.. _diagram_keyscan_construction:
.. figure:: ../../../../media/image136.png
	:align: center

	Keyscan architecture block diagram

When the state machine (FSM) is in rest mode (no keys are pressed), all rows output 0, and col is in input mode with weak pull-up enabled (the weak pull-up is set in the register corresponding to ioblk, not in keyscan module). When any key is pressed, the col end will see a value other than all 1 after debounce, indicating that a key is pressed. At this time, FSM will start a scan, sequentially making Row [0] -> Row [7] output 0 only one bit at a time (the rest are in the HiZ high-impedance state). Each result will be updated into an array.

FSM will continue to scan in a loop until the col returned by all rows is all 1, indicating that the keys are not pressed, and then it will enter the rest mode again (all rows output 0).

Basic Settings
~~~~~~~~~~~~~~

The reg_row_mask, reg_col_mask and reg_enable in KEYSCAN0 allow you to selectively block certain IOs without outputting or referring to their inputs when the 8x8 matrix is not used. Default is fully off. So it needs to be opened. reg_db_col in KEYSCAN_CONFIG2 determines how long the column input needs to debounce before it can be used.

The reg_slow_div in KEYSCAN_CONFIG1 determines the stay time of each stage of IP's FSM. Remember that this number must be larger than the debounce time, otherwise the interpretation will be confusing if the debounce is not completed after the IO transition.

reg_wait_cntr in KEYSCAN_CONFIG3 can be used to reduce the scanning speed. Because as long as the key is pressed, the keyscan module will continue to scan. This counter can control a fixed waiting time before starting a new round of scanning to reduce the scanning frequency.

Use FIFO mode
~~~~~~~~~~~~~

When using FIFO mode, the 64 key values scanned in by IP will be stored in the array. Every time the status of any key is different from the last scanned content, it will push the key's index and current value (0/1) into the FIFO. So the number in [5:0] specifies which button it is. [6] Indicates whether to press (0) or release (1). When the FIFO is not empty, an IRQ is issued. The advantage of this mode is that it eliminates the need for software to check which bit has changed bit by bit. The disadvantage is that KEY_SCAN_FIFO is a register that will automatically pop when read, so be careful when operating it.

Turn on reg_irq_fifo_not_empty_enable of KEYSCAN_IRQ_ENABLE. After receiving the IRQ, read reg_irq_fifo_not_empty in KEYSCAN_IRQ_FLAG, and then check reg_fifo_not_empty of KEYSCAN_FIFO_STATUS. Then start reading the contents of KEYSCAN_FIFO. Until it is cleared, clear KEY_SCAN_IRQ_CLEAR and end IRQ retine.

Use snapshot array mode
~~~~~~~~~~~~~~~~~~~~~~~

When using the snapshot array, the values of the 64 keys currently scanned in the IP will be stored in an array. If the content of this array is different from the content of KEYSCAN_SNAPSHOT_ARRAY, an IRQ will be sent. The software can trigger KEYSCAN_SNAPSHOT_TRIG, capture the current array content into the snapshot array, and then slowly compare what content has changed from the previous knowledge.

Turn on reg_irq_snapshot_change_enable of KEYSCAN_IRQ_ENABLE. After receiving the IRQ, read trigger KEYSCAN_SNAPSHOT_TRIG, and then interpret the contents of KEYSCAN_SNAPSHOT_ARRAY. Then clear KEY_SCAN_IRQ_CLEAR to end IRQ retine.

KeyScan Register Overview
~~~~~~~~~~~~~~~~~~~~~~~~~

.. This table is very small and no longer included in the file

.. _table_keyscan_register_overviews:
.. table:: Key scan Registers Overview
	:widths: 4 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| KEYSCAN_CONFIG0      | 0x000   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_CONFIG1      | 0x004   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_CONFIG2      | 0x008   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_CONFIG3      | 0x00c   |                                    |
	+----------------------+---------+------------------------------------+
	|KEYSCAN_SNAPSHOT_ARRAY| 0x014   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_SNAPSHOT_TRIG| 0x01c   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_FIFO_STATUS  | 0x020   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_FIFO         | 0x024   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_IRQ_ENABLE   | 0x028   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_IRQ_FLAG     | 0x02c   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_IRQ_CLEAR    | 0x030   |                                    |
	+----------------------+---------+------------------------------------+

KeyScan Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/peripherals/keyscan_registers_description.table.rst
