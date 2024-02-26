.. _table_aiao_registers_overview:
.. table:: AIAO Registers Overview (Base Address: 0x0410_8000)
	:widths: 3 1 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| i2s_tdm_sclk_in_sel  | 0x000   | Select the Source of the Mode      |
	|                      |         | TX/RX Module SCLK Source           |
	+----------------------+---------+------------------------------------+
	| i2s_tdm_fs_in_sel    | 0x004   | Select the Synchronous signal      |
	|                      |         | Source of the Mode TX/RX Module    |
	+----------------------+---------+------------------------------------+
	| i2s_tdm_sdi_in_sel   | 0x008   | Select the RX module SDI signal    |
	|                      |         | source		              |
	+----------------------+---------+------------------------------------+
	| i2s_tdm_sdo_out_sel  | 0x00c   | Select the subsystem SDO           |
	|                      |         | output source	              |
	+----------------------+---------+------------------------------------+
	| i2s_bclk_oen_sel     | 0x030   | BCLK IO output control             |
	+----------------------+---------+------------------------------------+
	| audio_pdm_ctrl       | 0x040   | Enable PDM mode                    |
	+----------------------+---------+------------------------------------+
	| i2s_sys_int_en       | 0x060   | Enable the I2S subsystem           |
	|                      |         | interrupt signal	              |
	+----------------------+---------+------------------------------------+
	| i2s_sys_ints         | 0x064   | I2S subsystem interrupt            |
	|                      |         | signal status                      |
	+----------------------+---------+------------------------------------+
