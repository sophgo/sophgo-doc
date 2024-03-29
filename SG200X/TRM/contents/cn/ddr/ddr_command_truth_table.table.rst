.. _table_ddr2_command_truth_table:
.. table:: DDR2 Command Truth Table
	:widths: 3 1 1 1 1 1 1 1 1 1 1

	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Function                 | CKE   | CKE   | CS#  | RAS# | CAS# | WE#  | BA0   | A11   | A10 | A0 |
	|                          | Pre   | Cur   |      |      |      |      | -     | -     | /   | -  |
	|                          |       |       |      |      |      |      | BA2   | A15   | AP  | A9 |
	+==========================+=======+=======+======+======+======+======+=======+=======+=====+====+
	| Mode Register Set        | H     | H     | L    | L    | L    | L    | BA    | OP    |     |    |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Refresh                  | H     | H     | L    | L    | L    | H    | V     | V     | V   | V  |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Self Refresh Entry       | H     | L     | L    | L    | L    | H    | V     | V     | V   | V  |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Self Refresh Exit        | L     | H     | H    | X    | X    | X    | X     | X     | X   | X  |
	|                          |       |       +------+------+------+------+-------+-------+-----+----+
	|                          |       |       | L    | H    | H    | H    | V     | V     | V   | V  |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Single Bank Precharge    | H     | H     | L    | L    | H    | L    | BA    | V     | L   | V  |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Precharge all Banks      | H     | H     | L    | L    | H    | L    | V     | V     | H   | V  |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Bank Activate            | H     | H     | L    | L    | H    | H    | BA    | RA    |     |    |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Write                    | H     | H     | L    | H    | L    | L    | BA    | RFU   | L   | CA |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Write with Auto Precharge| H     | H     | L    | H    | L    | L    | BA    | RFU   | H   | CA |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Read                     | H     | H     | L    | H    | L    | H    | BA    | RFU   | L   | CA |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Read with Auto Precharge | H     | H     | L    | H    | L    | H    | BA    | RFU   | H   | CA |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Read with Auto Precharge | H     | H     | L    | H    | L    | H    | BA    | RFU   | H   | CA |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| No Operation             | H     | H     | L    | H    | H    | H    | V     | V     | V   | V  |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Device Deselected        | H     | H     | H    | X    | X    | X    | X     | X     | X   | X  |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Power Down Entry         | H     | L     | L    | H    | H    | H    | V     | V     | V   | V  |
	|                          |       |       +------+------+------+------+-------+-------+-----+----+
	|                          |       |       | H    | X    | X    | X    | X     | X     | X   | X  |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| Power Down Exit          | L     | H     | L    | H    | H    | H    | V     | V     | V   | V  |
	|                          |       |       +------+------+------+------+-------+-------+-----+----+
	|                          |       |       | H    | X    | X    | X    | X     | X     | X   | X  |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-----+----+
	| H: High level; L: Low level; V: Valid; X: N/A. RFU: Reserved for Future Usage.                  |
	+-------------------------------------------------------------------------------------------------+


.. _table_ddr3_command_truth_table:
.. table:: DDR3 Command Truth Table
	:widths: 3 1 1 1 1 1 1 1 1 1 1 1

	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Function                 | CKE   | CKE   | CS#  | RAS# | CAS# | WE#  | BA0   | A13   | A12   | A10 | A0    |
	|                          | Pre   | Cur   |      |      |      |      | -     | -     | /     | /   | -     |
	|                          |       |       |      |      |      |      | BA2   | A15   | BC#   | AP  | A9,11 |
	+==========================+=======+=======+======+======+======+======+=======+=======+=======+=====+=======+
	| Mode Register Set        | H     | H     | L    | L    | L    | L    | BA    | OP                          |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Refresh                  | H     | H     | L    | L    | L    | H    | V     | V     | V     | V   | V     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Self Refresh Entry       | H     | L     | L    | L    | L    | H    | V     | V     | V     | V   | V     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Self Refresh Exit        | L     | H     | H    | X    | X    | X    | X     | X     | X     | X   | X     |
	|                          |       |       +------+------+------+------+-------+-------+-------+-----+-------+
	|                          |       |       | L    | H    | H    | H    | V     | V     | V     | V   | V     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Single Bank Precharge    | H     | H     | L    | L    | H    | L    | BA    | V     | V     | L   | V     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Precharge all Banks      | H     | H     | L    | L    | H    | L    | V     | V     | V     | H   | V     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Bank Activate            | H     | H     | L    | L    | H    | H    | BA    | RA                          |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Write (Fixed BL8 or BC4) | H     | H     | L    | H    | L    | L    | BA    | RFU   | V     | L   | CA    |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Write (BC4, on the Fly)  | H     | H     | L    | H    | L    | L    | BA    | RFU   | L     | L   | CA    |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Write (BL8, on the Fly)  | H     | H     | L    | H    | L    | L    | BA    | RFU   | H     | L   | CA    |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Write with Auto Precharge| H     | H     | L    | H    | L    | L    | BA    | RFU   | V     | H   | CA    |
	| (Fixed BL8 or BC4)       |       |       |      |      |      |      |       |       |       |     |       |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Write with Auto Precharge| H     | H     | L    | H    | L    | L    | BA    | RFU   | L     | H   | CA    |
	| (BC4, on the Fly)        |       |       |      |      |      |      |       |       |       |     |       |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Write with Auto Precharge| H     | H     | L    | H    | L    | L    | BA    | RFU   | H     | H   | CA    |
	| (BL8, on the Fly)        |       |       |      |      |      |      |       |       |       |     |       |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Read (Fixed BL8 or BC4)  | H     | H     | L    | H    | L    | H    | BA    | RFU   | V     | L   | CA    |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Read (BC4, on the Fly)   | H     | H     | L    | H    | L    | H    | BA    | RFU   | L     | L   | CA    |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Read (BL8, on the Fly)   | H     | H     | L    | H    | L    | H    | BA    | RFU   | H     | L   | CA    |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Read with Auto Precharge | H     | H     | L    | H    | L    | H    | BA    | RFU   | V     | H   | CA    |
	| (Fixed BL8 or BC4)       |       |       |      |      |      |      |       |       |       |     |       |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Read with Auto Precharge | H     | H     | L    | H    | L    | H    | BA    | RFU   | L     | H   | CA    |
	| (BC4, on the Fly)        |       |       |      |      |      |      |       |       |       |     |       |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Read with Auto Precharge | H     | H     | L    | H    | L    | H    | BA    | RFU   | H     | H   | CA    |
	| (BL8, on the Fly)        |       |       |      |      |      |      |       |       |       |     |       |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| No Operation             | H     | H     | L    | H    | H    | H    | V     | V     | V     | V   | V     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Device Deselected        | H     | H     | H    | X    | X    | X    | X     | X     | X     | X   | X     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Power Down Entry         | H     | L     | L    | H    | H    | H    | V     | V     | V     | V   | V     |
	|                          |       |       +------+------+------+------+-------+-------+-------+-----+-------+
	|                          |       |       | H    | X    | X    | X    | X     | X     | X     | X   | X     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| Power Down Exit          | L     | H     | L    | H    | H    | H    | V     | V     | V     | V   | V     |
	|                          |       |       +------+------+------+------+-------+-------+-------+-----+-------+
	|                          |       |       | H    | X    | X    | X    | X     | X     | X     | X   | X     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| ZQ Calibration Long      | H     | H     | L    | H    | H    | L    | X     | X     | X     | H   | X     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| ZQ Calibration Short     | H     | H     | L    | H    | H    | L    | X     | X     | X     | L   | X     |
	+--------------------------+-------+-------+------+------+------+------+-------+-------+-------+-----+-------+
	| H: High level; L: Low level; V: Valid; X: N/A. RFU: Reserved for Future Usage.                             |
	+------------------------------------------------------------------------------------------------------------+
