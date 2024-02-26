.. _table_BassAddress:
.. table:: BassAddress: 0x030A0000
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| tempsen_version      | 0x000   | ip version number                  |
	+----------------------+---------+------------------------------------+
	| tempsen_ctrl         | 0x004   | control register                   |
	+----------------------+---------+------------------------------------+
	| tempsen_status       | 0x008   | staus register                     |
	+----------------------+---------+------------------------------------+
	| tempsen_set          | 0x00c   | temperature sensor macro setting   |
	+----------------------+---------+------------------------------------+
	| tempsen_intr_en      | 0x010   | interrupt enable                   |
	+----------------------+---------+------------------------------------+
	| tempsen_intr_clr     | 0x014   | interrupt clear                    |
	+----------------------+---------+------------------------------------+
	| tempsen_intr_sta     | 0x018   | interupt status                    |
	+----------------------+---------+------------------------------------+
	| tempsen_intr_raw     | 0x01c   | interrupt raw status               |
	+----------------------+---------+------------------------------------+
	| tempsen_ch0_result   | 0x020   | temperature sensor channel 0       |
	|                      |         | result                             |
	+----------------------+---------+------------------------------------+
	| tempsen_ch1_result   | 0x024   | temperature sensor channel 1       |
	|                      |         | result                             |
	+----------------------+---------+------------------------------------+
	| tempsen_ch0_temp_th  | 0x040   | temperature sensor channel 0       |
	|                      |         | threshold                          |
	+----------------------+---------+------------------------------------+
	| tempsen_ch1_temp_th  | 0x044   | temperature sensor channel 1       |
	|                      |         | threshold                          |
	+----------------------+---------+------------------------------------+
	| Overheat_th          | 0x060   | overheat threshold register        |
	+----------------------+---------+------------------------------------+
	| tempsen_auto_period  | 0x064   | auto sample setting register       |
	+----------------------+---------+------------------------------------+
	| t\                   | 0x068   | overheat control register          |
	| empsen_overheat_ctrl |         |                                    |
	+----------------------+---------+------------------------------------+
	| tempse\              | 0x06c   | overheat status register           |
	| n_overheat_countdown |         |                                    |
	+----------------------+---------+------------------------------------+
	| tem\                 | 0x070   | counter of channel 0 over/under    |
	| psen_ch0_temp_th_cnt |         | threshold event                    |
	+----------------------+---------+------------------------------------+
	| tem\                 | 0x074   | counter of channel 1 over/under    |
	| psen_ch1_temp_th_cnt |         | threshold event                    |
	+----------------------+---------+------------------------------------+
