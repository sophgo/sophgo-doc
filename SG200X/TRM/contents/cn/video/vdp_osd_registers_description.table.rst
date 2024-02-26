VGOP_REG_0
''''''''''

.. _table_vdp_vgop_reg_0:
.. table:: VGOP_REG_0, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_ow0_format       | R/W   | OW0 Format             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0000: ARGB8888      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0100: ARGB4444      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0101: ARGB1555      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1000:               |      |
	|      |                      |       | 256LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1010:               |      |
	|      |                      |       | 16-LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1100: Font-base     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_1
''''''''''

.. _table_vdp_vgop_reg_1:
.. table:: VGOP_REG_1, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow0_h_start      | R/W   | OW0 H start pixel,     | 0x0  |
	|      |                      |       | unit: 1pixel           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow0_h_end        | R/W   | OW0 H end pixel, unit: | 0x0  |
	|      |                      |       | 1pixel                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_2
''''''''''

.. _table_vdp_vgop_reg_2:
.. table:: VGOP_REG_2, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow0_v_start      | R/W   | OW0 V start pixel,     | 0x0  |
	|      |                      |       | unit: 1line            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow0_v_end        | R/W   | OW0 V end pixel, unit: | 0x0  |
	|      |                      |       | 1line                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_3
''''''''''

.. _table_vdp_vgop_reg_3:
.. table:: VGOP_REG_3, Offset Address: 0x00c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | re\                  | R/W   | OW0 DRAM Start         | 0x0  |
	|      | g_ow0_dram_str_adr_l |       | address[31:0]          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_4
''''''''''

.. _table_vdp_vgop_reg_4:
.. table:: VGOP_REG_4, Offset Address: 0x010
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | re\                  | R/W   | OW0 DRAM Start         | 0x0  |
	|      | g_ow0_dram_str_adr_h |       | address[39:32]         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_5
''''''''''

.. _table_vdp_vgop_reg_5:
.. table:: VGOP_REG_5, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 15:4 | reg_ow0_dram_strip   | R/W   | OW0 DRAM Strip         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 22:16| reg_ow0_crop_pixels  | R/W   | OW0 crop pixels (per   | 0x0  |
	|      |                      |       | line)                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format ARGB8888, crop  |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~3                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format                 |      |
	|      |                      |       | ARGB4444/ARGB1555,     |      |
	|      |                      |       | crop pixels valid      |      |
	|      |                      |       | value: 0~7             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 256LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~15                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 16-LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~31                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format Font-base, crop |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~127                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:23| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_6
''''''''''

.. _table_vdp_vgop_reg_6:
.. table:: VGOP_REG_6, Offset Address: 0x018
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 13:4 | reg_ow0_dram_hsize   | R/W   | OW0 DRAM Hsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | \*\* while             |      |
	|      |                      |       | reg_odec_en=1,         |      |
	|      |                      |       | odec_stream_size =     |      |
	|      |                      |       | {reg_ow_dram_vs        |      |
	|      |                      |       | ize,reg_ow_dram_hsize} |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow0_dram_vsize   | R/W   | OW0 DRAM Vsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_10
'''''''''''

.. _table_vdp_vgop_reg_10:
.. table:: VGOP_REG_10, Offset Address: 0x020
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_ow1_format       | R/W   | OW1 Format             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0000: ARGB8888      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0100: ARGB4444      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0101: ARGB1555      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1000:               |      |
	|      |                      |       | 256LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1010:               |      |
	|      |                      |       | 16-LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1100: Font-base     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_11
'''''''''''

.. _table_vdp_vgop_reg_11:
.. table:: VGOP_REG_11, Offset Address: 0x024
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow1_h_start      | R/W   | OW1 H start pixel,     | 0x0  |
	|      |                      |       | unit: 1pixel           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow1_h_end        | R/W   | OW1 H end pixel, unit: | 0x0  |
	|      |                      |       | 1pixel                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_12
'''''''''''

.. _table_vdp_vgop_reg_12:
.. table:: VGOP_REG_12, Offset Address: 0x028
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow1_v_start      | R/W   | OW1 V start pixel,     | 0x0  |
	|      |                      |       | unit: 1line            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow1_v_end        | R/W   | OW1 V end pixel, unit: | 0x0  |
	|      |                      |       | 1line                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_13
'''''''''''

.. _table_vdp_VGOP_REG_13:
.. table:: VGOP_REG_13, Offset Address: 0x02c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | re\                  | R/W   | OW1 DRAM Start         | 0x0  |
	|      | g_ow1_dram_str_adr_l |       | address[31:0]          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_14
'''''''''''

.. _table_vdp_vgop_reg_14:
.. table:: VGOP_REG_14, Offset Address: 0x030
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | re\                  | R/W   | OW1 DRAM Start         | 0x0  |
	|      | g_ow1_dram_str_adr_h |       | address[39:32]         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_15
'''''''''''

.. _table_vdp_vgop_reg_15:
.. table:: VGOP_REG_15, Offset Address: 0x034
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 15:4 | reg_ow1_dram_strip   | R/W   | OW1 DRAM Strip         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 22:16| reg_ow1_crop_pixels  | R/W   | OW1 crop pixels (per   | 0x0  |
	|      |                      |       | line)                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format ARGB8888, crop  |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~3                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format                 |      |
	|      |                      |       | ARGB4444/ARGB1555,     |      |
	|      |                      |       | crop pixels valid      |      |
	|      |                      |       | value: 0~7             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 256LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~15                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 16-LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~31                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format Font-base, crop |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~127                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:23| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_16
'''''''''''

.. _table_vdp_vgop_reg_16:
.. table:: VGOP_REG_16, Offset Address: 0x038
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 13:4 | reg_ow1_dram_hsize   | R/W   | OW1 DRAM Hsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | \*\* while             |      |
	|      |                      |       | reg_odec_en=1,         |      |
	|      |                      |       | odec_stream_size =     |      |
	|      |                      |       | {reg_ow_dram_vs        |      |
	|      |                      |       | ize,reg_ow_dram_hsize} |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow1_dram_vsize   | R/W   | OW1 DRAM Vsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_20
'''''''''''

.. _table_vdp_vgop_reg_20:
.. table:: VGOP_REG_20, Offset Address: 0x040
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_ow2_format       | R/W   | OW2 Format             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0000: ARGB8888      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0100: ARGB4444      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0101: ARGB1555      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1000:               |      |
	|      |                      |       | 256LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1010:               |      |
	|      |                      |       | 16-LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1100: Font-base     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_21
'''''''''''

.. _table_vdp_vgop_reg_21:
.. table:: VGOP_REG_21, Offset Address: 0x044
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow2_h_start      | R/W   | OW2 H start pixel,     | 0x0  |
	|      |                      |       | unit: 1pixel           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow2_h_end        | R/W   | OW2 H end pixel, unit: | 0x0  |
	|      |                      |       | 1pixel                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_22
'''''''''''

.. _table_vdp_vgop_reg_22:
.. table:: VGOP_REG_22, Offset Address: 0x048
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow2_v_start      | R/W   | OW2 V start pixel,     | 0x0  |
	|      |                      |       | unit: 1line            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow2_v_end        | R/W   | OW2 V end pixel, unit: | 0x0  |
	|      |                      |       | 1line                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_23
'''''''''''

.. _table_vdp_vgop_reg_23:
.. table:: VGOP_REG_23, Offset Address: 0x04c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | re\                  | R/W   | OW2 DRAM Start         | 0x0  |
	|      | g_ow2_dram_str_adr_l |       | address[31:0]          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_24
'''''''''''

.. _table_vdp_vgop_reg_24:
.. table:: VGOP_REG_24, Offset Address: 0x050
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | re\                  | R/W   | OW2 DRAM Start         | 0x0  |
	|      | g_ow2_dram_str_adr_h |       | address[39:32]         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_25
'''''''''''

.. _table_vdp_vgop_reg_25:
.. table:: VGOP_REG_25, Offset Address: 0x054
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 15:4 | reg_ow2_dram_strip   | R/W   | OW2 DRAM Strip         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 22:16| reg_ow2_crop_pixels  | R/W   | OW2 crop pixels (per   | 0x0  |
	|      |                      |       | line)                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format ARGB8888, crop  |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~3                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format                 |      |
	|      |                      |       | ARGB4444/ARGB1555,     |      |
	|      |                      |       | crop pixels valid      |      |
	|      |                      |       | value: 0~7             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 256LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~15                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 16-LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~31                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format Font-base, crop |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~127                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:23| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_26
'''''''''''

.. _table_vdp_vgop_reg_26:
.. table:: VGOP_REG_26, Offset Address: 0x058
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 13:4 | reg_ow2_dram_hsize   | R/W   | OW2 DRAM Hsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | \*\* while             |      |
	|      |                      |       | reg_odec_en=1,         |      |
	|      |                      |       | odec_stream_size =     |      |
	|      |                      |       | {reg_ow_dram_vs        |      |
	|      |                      |       | ize,reg_ow_dram_hsize} |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow2_dram_vsize   | R/W   | OW2 DRAM Vsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_30
'''''''''''

.. _table_vdp_vgop_reg_30:
.. table:: VGOP_REG_30, Offset Address: 0x060
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_ow3_format       | R/W   | OW3 Format             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0000: ARGB8888      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0100: ARGB4444      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0101: ARGB1555      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1000:               |      |
	|      |                      |       | 256LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1010:               |      |
	|      |                      |       | 16-LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1100: Font-base     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_31
'''''''''''

.. _table_vdp_vgop_reg_31:
.. table:: VGOP_REG_31, Offset Address: 0x064
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow3_h_start      | R/W   | OW3 H start pixel,     | 0x0  |
	|      |                      |       | unit: 1pixel           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow3_h_end        | R/W   | OW3 H end pixel, unit: | 0x0  |
	|      |                      |       | 1pixel                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_32
'''''''''''

.. _table_vdp_vgop_reg_32:
.. table:: VGOP_REG_32, Offset Address: 0x068
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow3_v_start      | R/W   | OW3 V start pixel,     | 0x0  |
	|      |                      |       | unit: 1line            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow3_v_end        | R/W   | OW3 V end pixel, unit: | 0x0  |
	|      |                      |       | 1line                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_33
'''''''''''

.. _table_vdp_vgop_reg_33:
.. table:: VGOP_REG_33, Offset Address: 0x06c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | re\                  | R/W   | OW3 DRAM Start         | 0x0  |
	|      | g_ow3_dram_str_adr_l |       | address[31:0]          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_34
'''''''''''

.. _table_vdp_vgop_reg_34:
.. table:: VGOP_REG_34, Offset Address: 0x070
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | re\                  | R/W   | OW3 DRAM Start         | 0x0  |
	|      | g_ow3_dram_str_adr_h |       | address[39:32]         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_35
'''''''''''

.. _table_vdp_vgop_reg_35:
.. table:: VGOP_REG_35, Offset Address: 0x074
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 15:4 | reg_ow3_dram_strip   | R/W   | OW3 DRAM Strip         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 22:16| reg_ow3_crop_pixels  | R/W   | OW3 crop pixels (per   | 0x0  |
	|      |                      |       | line)                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format ARGB8888, crop  |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~3                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format                 |      |
	|      |                      |       | ARGB4444/ARGB1555,     |      |
	|      |                      |       | crop pixels valid      |      |
	|      |                      |       | value: 0~7             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 256LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~15                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 16-LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~31                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format Font-base, crop |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~127                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:23| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_36
'''''''''''

.. _table_vdp_vgop_reg_36:
.. table:: VGOP_REG_36, Offset Address: 0x078
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 13:4 | reg_ow3_dram_hsize   | R/W   | OW3 DRAM Hsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | \*\* while             |      |
	|      |                      |       | reg_odec_en=1,         |      |
	|      |                      |       | odec_stream_size =     |      |
	|      |                      |       | {reg_ow_dram_vs        |      |
	|      |                      |       | ize,reg_ow_dram_hsize} |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow3_dram_vsize   | R/W   | OW3 DRAM Vsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_40
'''''''''''

.. _table_vdp_vgop_reg_40:
.. table:: VGOP_REG_40, Offset Address: 0x080
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_ow4_format       | R/W   | OW4 Format             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0000: ARGB8888      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0100: ARGB4444      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0101: ARGB1555      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1000:               |      |
	|      |                      |       | 256LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1010:               |      |
	|      |                      |       | 16-LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1100: Font-base     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_41
'''''''''''

.. _table_vdp_vgop_reg_41:
.. table:: VGOP_REG_41, Offset Address: 0x084
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow4_h_start      | R/W   | OW4 H start pixel,     | 0x0  |
	|      |                      |       | unit: 1pixel           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow4_h_end        | R/W   | OW4 H end pixel, unit: | 0x0  |
	|      |                      |       | 1pixel                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_42
'''''''''''

.. _table_vdp_vgop_reg_42:
.. table:: VGOP_REG_42, Offset Address: 0x088
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow4_v_start      | R/W   | OW4 V start pixel,     | 0x0  |
	|      |                      |       | unit: 1line            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow4_v_end        | R/W   | OW4 V end pixel, unit: | 0x0  |
	|      |                      |       | 1line                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_43
'''''''''''

.. _table_vdp_vgop_reg_43:
.. table:: VGOP_REG_43, Offset Address: 0x08c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | re\                  | R/W   | OW4 DRAM Start         | 0x0  |
	|      | g_ow4_dram_str_adr_l |       | address[31:0]          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_44
'''''''''''

.. _table_vdp_vgop_reg_44:
.. table:: VGOP_REG_44, Offset Address: 0x090
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | re\                  | R/W   | OW4 DRAM Start         | 0x0  |
	|      | g_ow4_dram_str_adr_h |       | address[39:32]         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_45
'''''''''''

.. _table_vdp_vgop_reg_45:
.. table:: VGOP_REG_45, Offset Address: 0x094
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 15:4 | reg_ow4_dram_strip   | R/W   | OW4 DRAM Strip         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 22:16| reg_ow4_crop_pixels  | R/W   | OW4 crop pixels (per   | 0x0  |
	|      |                      |       | line)                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format ARGB8888, crop  |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~3                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format                 |      |
	|      |                      |       | ARGB4444/ARGB1555,     |      |
	|      |                      |       | crop pixels valid      |      |
	|      |                      |       | value: 0~7             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 256LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~15                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 16-LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~31                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format Font-base, crop |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~127                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:23| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_46
'''''''''''

.. _table_vdp_vgop_reg_46:
.. table:: VGOP_REG_46, Offset Address: 0x098
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 13:4 | reg_ow4_dram_hsize   | R/W   | OW4 DRAM Hsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | \*\* while             |      |
	|      |                      |       | reg_odec_en=1,         |      |
	|      |                      |       | odec_stream_size =     |      |
	|      |                      |       | {reg_ow_dram_vs        |      |
	|      |                      |       | ize,reg_ow_dram_hsize} |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow4_dram_vsize   | R/W   | OW4 DRAM Vsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_50
'''''''''''

.. _table_vdp_vgop_reg_50:
.. table:: VGOP_REG_50, Offset Address: 0x0a0
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_ow5_format       | R/W   | OW5 Format             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0000: ARGB8888      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0100: ARGB4444      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0101: ARGB1555      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1000:               |      |
	|      |                      |       | 256LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1010:               |      |
	|      |                      |       | 16-LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1100: Font-base     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_51
'''''''''''

.. _table_vdp_vgop_reg_51:
.. table:: VGOP_REG_51, Offset Address: 0x0a4
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow5_h_start      | R/W   | OW5 H start pixel,     | 0x0  |
	|      |                      |       | unit: 1pixel           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow5_h_end        | R/W   | OW5 H end pixel, unit: | 0x0  |
	|      |                      |       | 1pixel                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_52
'''''''''''

.. _table_vdp_vgop_reg_52:
.. table:: VGOP_REG_52, Offset Address: 0x0a8
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow5_v_start      | R/W   | OW5 V start pixel,     | 0x0  |
	|      |                      |       | unit: 1line            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow5_v_end        | R/W   | OW5 V end pixel, unit: | 0x0  |
	|      |                      |       | 1line                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_53
'''''''''''

.. _table_vdp_vgop_reg_53:
.. table:: VGOP_REG_53, Offset Address: 0x0ac
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | re\                  | R/W   | OW5 DRAM Start         | 0x0  |
	|      | g_ow5_dram_str_adr_l |       | address[31:0]          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_54
'''''''''''

.. _table_vdp_vgop_reg_54:
.. table:: VGOP_REG_54, Offset Address: 0x0b0
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | re\                  | R/W   | OW5 DRAM Start         | 0x0  |
	|      | g_ow5_dram_str_adr_h |       | address[39:32]         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_55
'''''''''''

.. _table_vdp_vgop_reg_55:
.. table:: VGOP_REG_55, Offset Address: 0x0b4
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 15:4 | reg_ow5_dram_strip   | R/W   | OW5 DRAM Strip         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 22:16| reg_ow5_crop_pixels  | R/W   | OW5 crop pixels (per   | 0x0  |
	|      |                      |       | line)                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format ARGB8888, crop  |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~3                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format                 |      |
	|      |                      |       | ARGB4444/ARGB1555,     |      |
	|      |                      |       | crop pixels valid      |      |
	|      |                      |       | value: 0~7             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 256LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~15                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 16-LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~31                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format Font-base, crop |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~127                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:23| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_56
'''''''''''

.. _table_vdp_vgop_reg_56:
.. table:: VGOP_REG_56, Offset Address: 0x0b8
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 13:4 | reg_ow5_dram_hsize   | R/W   | OW5 DRAM Hsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | \*\* while             |      |
	|      |                      |       | reg_odec_en=1,         |      |
	|      |                      |       | odec_stream_size =     |      |
	|      |                      |       | {reg_ow_dram_vs        |      |
	|      |                      |       | ize,reg_ow_dram_hsize} |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow5_dram_vsize   | R/W   | OW5 DRAM Vsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_60
'''''''''''

.. _table_vdp_vgop_reg_60:
.. table:: VGOP_REG_60, Offset Address: 0x0c0
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_ow6_format       | R/W   | OW6 Format             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0000: ARGB8888      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0100: ARGB4444      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0101: ARGB1555      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1000:               |      |
	|      |                      |       | 256LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1010:               |      |
	|      |                      |       | 16-LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1100: Font-base     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_61
'''''''''''

.. _table_vdp_vgop_reg_61:
.. table:: VGOP_REG_61, Offset Address: 0x0c4
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow6_h_start      | R/W   | OW6 H start pixel,     | 0x0  |
	|      |                      |       | unit: 1pixel           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow6_h_end        | R/W   | OW6 H end pixel, unit: | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_62
'''''''''''

.. _table_vdp_vgop_reg_62:
.. table:: VGOP_REG_62, Offset Address: 0x0c8
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow6_v_start      | R/W   | OW6 V start pixel,     | 0x0  |
	|      |                      |       | unit: 1line            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow6_v_end        | R/W   | OW6 V end pixel, unit: | 0x0  |
	|      |                      |       | 1line                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_63
'''''''''''

.. _table_vdp_vgop_reg_63:
.. table:: VGOP_REG_63, Offset Address: 0x0cc
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | re\                  | R/W   | OW6 DRAM Start         | 0x0  |
	|      | g_ow6_dram_str_adr_l |       | address[31:0]          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_64
'''''''''''

.. _table_vdp_vgop_reg_64:
.. table:: VGOP_REG_64, Offset Address: 0x0d0
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | re\                  | R/W   | OW6 DRAM Start         | 0x0  |
	|      | g_ow6_dram_str_adr_h |       | address[39:32]         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_65
'''''''''''

.. _table_vdp_vgop_reg_65:
.. table:: VGOP_REG_65, Offset Address: 0x0d4
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 15:4 | reg_ow6_dram_strip   | R/W   | OW6 DRAM Strip         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 22:16| reg_ow6_crop_pixels  | R/W   | OW6 crop pixels (per   | 0x0  |
	|      |                      |       | line)                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format ARGB8888, crop  |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~3                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format                 |      |
	|      |                      |       | ARGB4444/ARGB1555,     |      |
	|      |                      |       | crop pixels valid      |      |
	|      |                      |       | value: 0~7             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 256LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~15                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 16-LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~31                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format Font-base, crop |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~127                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:23| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_66
'''''''''''

.. _table_vdp_vgop_reg_66:
.. table:: VGOP_REG_66, Offset Address: 0x0d8
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 13:4 | reg_ow6_dram_hsize   | R/W   | OW6 DRAM Hsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | \*\* while             |      |
	|      |                      |       | reg_odec_en=1,         |      |
	|      |                      |       | odec_stream_size =     |      |
	|      |                      |       | {reg_ow_dram_vs        |      |
	|      |                      |       | ize,reg_ow_dram_hsize} |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow6_dram_vsize   | R/W   | OW6 DRAM Vsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_70
'''''''''''

.. _table_vdp_vgop_reg_70:
.. table:: VGOP_REG_70, Offset Address: 0x0e0
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | reg_ow7_format       | R/W   | OW7 Format             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0000: ARGB8888      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0100: ARGB4444      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b0101: ARGB1555      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1000:               |      |
	|      |                      |       | 256LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1010:               |      |
	|      |                      |       | 16-LUT-ARGB4444        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4'b1100: Font-base     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_71
'''''''''''

.. _table_vdp_vgop_reg_71:
.. table:: VGOP_REG_71, Offset Address: 0x0e4
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow7_h_start      | R/W   | OW7 H start pixel,     | 0x0  |
	|      |                      |       | unit: 1pixel           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow7_h_end        | R/W   | OW7 H end pixel, unit: | 0x0  |
	|      |                      |       | 1pixel                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_72
'''''''''''

.. _table_vdp_vgop_reg_72:
.. table:: VGOP_REG_72, Offset Address: 0x0e8
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11:0 | reg_ow7_v_start      | R/W   | OW7 V start pixel,     | 0x0  |
	|      |                      |       | unit: 1line            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow7_v_end        | R/W   | OW7 V end pixel, unit: | 0x0  |
	|      |                      |       | 1line                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_73
'''''''''''

.. _table_vdp_vgop_reg_73:
.. table:: VGOP_REG_73, Offset Address: 0x0ec
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | re\                  | R/W   | OW7 DRAM Start         | 0x0  |
	|      | g_ow7_dram_str_adr_l |       | address[31:0]          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_74
'''''''''''

.. _table_vdp_vgop_reg_74:
.. table:: VGOP_REG_74, Offset Address: 0x0f0
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | re\                  | R/W   | OW7 DRAM Start         | 0x0  |
	|      | g_ow7_dram_str_adr_h |       | address[39:32]         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_75
'''''''''''

.. _table_vdp_vgop_reg_75:
.. table:: VGOP_REG_75, Offset Address: 0x0f4
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 15:4 | reg_ow7_dram_strip   | R/W   | OW7 DRAM Strip         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 22:16| reg_ow7_crop_pixels  | R/W   | OW7 crop pixels (per   | 0x0  |
	|      |                      |       | line)                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format ARGB8888, crop  |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~3                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format                 |      |
	|      |                      |       | ARGB4444/ARGB1555,     |      |
	|      |                      |       | crop pixels valid      |      |
	|      |                      |       | value: 0~7             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 256LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~15                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format 16-LUT, crop    |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~31                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Format Font-base, crop |      |
	|      |                      |       | pixels valid value:    |      |
	|      |                      |       | 0~127                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:23| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_76
'''''''''''

.. _table_vdp_vgop_reg_76:
.. table:: VGOP_REG_76, Offset Address: 0x0f8
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 13:4 | reg_ow7_dram_hsize   | R/W   | OW7 DRAM Hsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | \*\* while             |      |
	|      |                      |       | reg_odec_en=1,         |      |
	|      |                      |       | odec_stream_size =     |      |
	|      |                      |       | {reg_ow_dram_vs        |      |
	|      |                      |       | ize,reg_ow_dram_hsize} |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27:16| reg_ow7_dram_vsize   | R/W   | OW7 DRAM Vsize         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:28| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_80
'''''''''''

osd_common_ctrl

.. _table_vdp_vgop_reg_80:
.. table:: VGOP_REG_80, Offset Address: 0x100
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg_ow0_en           | R/W   | OSD Window0 enable     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_ow1_en           | R/W   | OSD Window1 enable     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg_ow2_en           | R/W   | OSD Window2 enable     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg_ow3_en           | R/W   | OSD Window3 enable     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_ow4_en           | R/W   | OSD Window4 enable     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | reg_ow5_en           | R/W   | OSD Window5 enable     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | reg_ow6_en           | R/W   | OSD Window6 enable     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | reg_ow7_en           | R/W   | OSD Window7 enable     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg_vgop_hscal       | R/W   | VGOP H scale up (x2)   | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | reg_vgop_vscal       | R/W   | VGOP V scale up (x2)   | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | reg_clr_key_en       | R/W   | Color Key enable       | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_vdp_vgop_reg_80_2:
.. table:: VGOP_REG_80, Offset Address: 0x100 (continued)
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:12| reg_vgop_arlen       | R/W   | AXI-R burst length     | 0x0  |
	|      |                      |       | (INCR mode)            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 30:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | reg_vgop_sw_rst      | R/W   | vgop software reset    | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_81
'''''''''''

LUT256 SRAM

.. _table_vdp_vgop_reg_81:
.. table:: VGOP_REG_81, Offset Address: 0x104
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_idx_wdata        | R/W   | Idx sram wdata         | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	+------+----------------------+-------+------------------------+------+
	| 23:16| reg_idx_adr          | R/W   | Idx sram address       | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_82
'''''''''''

LUT256 SRAM

.. _table_vdp_vgop_reg_82:
.. table:: VGOP_REG_82, Offset Address: 0x108
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_idx_rdata        | R     | idx sram rdata         |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg_idx_wr           | R/W   | idx sram write         | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 17   | reg_idx_rd           | R/W   | idx sram read          | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 18   | reg_vgop_db_clr      | R/W   | vgop debug flag clear  | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:19| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_83
'''''''''''

color key content

.. _table_vdp_vgop_reg_83:
.. table:: VGOP_REG_83, Offset Address: 0x10c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 23:0 | reg_clr_key          | R/W   | Color Key (RGB888)     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_84
'''''''''''

constant color

.. _table_vdp_vgop_reg_84:
.. table:: VGOP_REG_84, Offset Address: 0x110
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_const_argb0      | R/W   | Constant0 ARGB4444 for | 0x0  |
	|      |                      |       | Font-base              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg_const_argb1      | R/W   | Constant1 ARGB4444 for | 0x0  |
	|      |                      |       | Font-base              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_85
'''''''''''

debug

.. _table_vdp_vgop_reg_85:
.. table:: VGOP_REG_85, Offset Address: 0x114
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | reg_vgop_debug       | R     | debug                  |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_86
'''''''''''

fb_thr

.. _table_vdp_vgop_reg_86:
.. table:: VGOP_REG_86, Offset Address: 0x120
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 5:0  | reg_fb_clr_hi_thr    | R/W   | font_box brightness    | 0x30 |
	|      |                      |       | strong threshold ,     |      |
	|      |                      |       | unit: 4 levels         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 7:6  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 13:8 | reg_fb_clr_lo_thr    | R/W   | font_box brightness    | 0x20 |
	|      |                      |       | wrak threshold , unit: |      |
	|      |                      |       | 4 levels               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg_fb_init          | R/W   | fb strong status init  | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | reg_fb_font_is_dark  | R/W   | fb inv control         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : font color is dark |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : font color is      |      |
	|      |                      |       | light                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 19:18| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 25:20| reg_fb_diff_fnum     | R/W   | font_box brightness    | 0x1  |
	|      |                      |       | detect interval        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: stop detection      |      |
	|      |                      |       | update                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: always detection    |      |
	|      |                      |       | update                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2~63: detection update |      |
	|      |                      |       | if n-1 continous       |      |
	|      |                      |       | frames detection value |      |
	|      |                      |       | is all difference      |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:26| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_87
'''''''''''

fb0_setting

.. _table_vdp_vgop_reg_87:
.. table:: VGOP_REG_87, Offset Address: 0x124
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 6:0  | reg_fb0_width        | R/W   | font_box_0 width ,     | 0x0f |
	|      |                      |       | unit: 1 pixel, 1~128   |      |
	|      |                      |       | pixels                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | (reg_fb_width+1) \*    |      |
	|      |                      |       | (reg_fb_num+1) must be |      |
	|      |                      |       | equal to attached ow   |      |
	|      |                      |       | width                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12:8 | reg_fb0_pix_thr      | R/W   | font_box_0 strong      | 0x10 |
	|      |                      |       | pixel pixel threshold, |      |
	|      |                      |       | unit: 8 pixels         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 14:13| reg_fb0_sample_rate  | R/W   | font_box_0 sample      | 0x1  |
	|      |                      |       | rqtio                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: per pixel           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: 2 pixels            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2: 4 pixels            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3: 8 pixels            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 20:16| reg_fb0_num          | R/W   | font_box_0 box numbers | 0x1f |
	|      |                      |       | , 1~32 boxes           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 23:21| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 26:24| reg_fb0_attached_idx | R/W   | font_box_0 attached ow | 0x0  |
	|      |                      |       | number                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | reg_fb0_en           | R/W   | font_box_0 enable      | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | (active while attached |      |
	|      |                      |       | ow is alive and set as |      |
	|      |                      |       | font base fromat)      |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:29| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_88
'''''''''''

fb0_init_st

.. _table_vdp_vgop_reg_88:
.. table:: VGOP_REG_88, Offset Address: 0x128
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | reg_fb0_init_st      | R/W   | font_box_0 init strong | 0x0  |
	|      |                      |       | value                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_89
'''''''''''

fb0_st_ro

.. _table_vdp_vgop_reg_89:
.. table:: VGOP_REG_89, Offset Address: 0x12c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | reg_fb0_record       | R     | font_box_0 strong      |      |
	|      |                      |       | value record           |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_90
'''''''''''

fb1_setting

.. _table_vdp_vgop_reg_90:
.. table:: VGOP_REG_90, Offset Address: 0x134
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 6:0  | reg_fb1_width        | R/W   | font_box_1 width ,     | 0x0f |
	|      |                      |       | unit: 1 pixel, 1~128   |      |
	|      |                      |       | pixels                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | (reg_fb_width+1) \*    |      |
	|      |                      |       | (reg_fb_num+1) must be |      |
	|      |                      |       | equal to attached ow   |      |
	|      |                      |       | width                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12:8 | reg_fb1_pix_thr      | R/W   | font_box_1 strong      | 0x10 |
	|      |                      |       | pixel pixel threshold, |      |
	|      |                      |       | unit: 8 pixels         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 14:13| reg_fb1_sample_rate  | R/W   | font_box_1 sample      | 0x1  |
	|      |                      |       | rqtio                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: per pixel           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: 2 pixels            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2: 4 pixels            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3: 8 pixels            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 20:16| reg_fb1_num          | R/W   | font_box_1 box numbers | 0x1f |
	|      |                      |       | , 1~32 boxes           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 23:21| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 26:24| reg_fb1_attached_idx | R/W   | font_box_1 attached ow | 0x7  |
	|      |                      |       | number                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | reg_fb1_en           | R/W   | font_box_1 enable      | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | (active while attached |      |
	|      |                      |       | ow is alive and set as |      |
	|      |                      |       | font base fromat)      |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:29| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_91
'''''''''''

fb1_init_st

.. _table_vdp_vgop_reg_91:
.. table:: VGOP_REG_91, Offset Address: 0x138
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | reg_fb1_init_st      | R/W   | font_box_1 init strong | 0x0  |
	|      |                      |       | value                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_REG_92
'''''''''''

fb1_st_ro

.. _table_vdp_vgop_reg_92:
.. table:: VGOP_REG_92, Offset Address: 0x13c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | reg_fb1_record       | R     | font_box_1 strong      |      |
	|      |                      |       | value record           |      |
	+------+----------------------+-------+------------------------+------+

BW_LIMIT
''''''''

.. _table_vdp_bw_limit:
.. table:: BW_LIMIT, Offset Address: 0x140
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | reg_bwl_win          | R/W   | B.W. limit window      | 0x0  |
	|      |                      |       | period, unit : clk_axi |      |
	|      |                      |       | cycle                  |      |
	+------+----------------------+-------+------------------------+------+
	| 15:10| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 25:16| reg_bwl_vld          | R/W   | B.W. limit valid       | 0x0  |
	|      |                      |       | number in reg_bwl_win, |      |
	|      |                      |       | unit : Byte            |      |
	+------+----------------------+-------+------------------------+------+
	| 30:26| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | reg_bwl_en           | R/W   | B.W. limit enable      | 0x0  |
	+------+----------------------+-------+------------------------+------+

VGOP_DEC_00
'''''''''''

vgop_dec_ctrl

.. _table_vdp_vgop_dec_00:
.. table:: VGOP_DEC_00, Offset Address: 0x150
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg_odec_en          | R/W   | vgop decoder enable    | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0: bypass              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: decoder mode        |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_odec_int_en      | R/W   | vgop_decoder INT       | 0x0  |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg_odec_int_clr     | R/W   | vgop_decoder INT clear | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg_odec_wdt_en      | R/W   | vgop wdt enable        | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | reg_odec_dbg_ridx    | R/W   | vgop_decoder debug idx | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg_odec_done        | R     | vgop_decoder done      |      |
	+------+----------------------+-------+------------------------+------+
	| 11:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 14:12| r\                   | R/W   | vgop decoder attached  | 0x0  |
	|      | eg_odec_attached_idx |       | ow number              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 18:16| r\                   | R/W   | wdt precision          | 0x0  |
	|      | eg_odec_wdt_fdiv_bit |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 23:19| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| reg_odec_int_vec     | R     | vgop_decoder INT       |      |
	|      |                      |       | vector                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: odec done           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2: Watch Dog time out  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4: detect reduntant    |      |
	|      |                      |       | data input             |      |
	+------+----------------------+-------+------------------------+------+

VGOP_DEC_01
'''''''''''

vgop_dec_debug

.. _table_vdp_vgop_dec_01:
.. table:: VGOP_DEC_01, Offset Address: 0x154
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | reg_odec_dbg_rdata   | R     | vgop decoder debug     |      |
	|      |                      |       | rdata                  |      |
	+------+----------------------+-------+------------------------+------+

VGOP_LUT16_0
''''''''''''

vgop_lut16_0_1

.. _table_vdp_vgop_lut16_0:
.. table:: VGOP_LUT16_0, Offset Address: 0x160
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_lut16_cnt0       | R/W   | LUT 16 content 0       | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg_lut16_cnt1       | R/W   | LUT 16 content 1       | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_LUT16_1
''''''''''''

vgop_lut16_2_3

.. _table_vdp_vgop_lut16_1:
.. table:: VGOP_LUT16_1, Offset Address: 0x164
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_lut16_cnt2       | R/W   | LUT 16 content 2       | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg_lut16_cnt3       | R/W   | LUT 16 content         | 0x0  |
	|      |                      |       | 3(ARGB4444)            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_LUT16_2
''''''''''''

vgop_lut16_4_5

.. _table_vdp_vgop_lut16_2:
.. table:: VGOP_LUT16_2, Offset Address: 0x168
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_lut16_cnt4       | R/W   | LUT 16 content 4       | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg_lut16_cnt5       | R/W   | LUT 16 content 5       | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_LUT16_3
''''''''''''

vgop_lut16_6_7

.. _table_vdp_vgop_lut16_3:
.. table:: VGOP_LUT16_3, Offset Address: 0x16c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_lut16_cnt6       | R/W   | LUT 16 content 6       | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg_lut16_cnt7       | R/W   | LUT 16 content 7       | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_LUT16_4
''''''''''''

vgop_lut16_8_9

.. _table_vdp_vgop_lut16_4:
.. table:: VGOP_LUT16_4, Offset Address: 0x170
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_lut16_cnt8       | R/W   | LUT 16 content 8       | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg_lut16_cnt9       | R/W   | LUT 16 content 9       | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_LUT16_5
''''''''''''

vgop_lut16_10_11

.. _table_vdp_vgop_lut16_5:
.. table:: VGOP_LUT16_5, Offset Address: 0x174
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_lut16_cnt10      | R/W   | LUT 16 content 10      | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg_lut16_cnt11      | R/W   | LUT 16 content 11      | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_LUT16_6
''''''''''''

vgop_lut16_12_13

.. _table_vdp_vgop_lut16_6:
.. table:: VGOP_LUT16_6, Offset Address: 0x178
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_lut16_cnt12      | R/W   | LUT 16 content 12      | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg_lut16_cnt13      | R/W   | LUT 16 content 13      | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+

VGOP_LUT16_7
''''''''''''

vgop_lut16_14_15

.. _table_vdp_vgop_lut16_7:
.. table:: VGOP_LUT16_7, Offset Address: 0x17c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | reg_lut16_cnt14      | R/W   | LUT 16 content 14      | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| reg_lut16_cnt15      | R/W   | LUT 16 content 15      | 0x0  |
	|      |                      |       | (ARGB4444)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow: Yes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Ctrl:           |      |
	|      |                      |       | shdw_update            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow Read Select:    |      |
	|      |                      |       | shdw_read_sel          |      |
	+------+----------------------+-------+------------------------+------+
