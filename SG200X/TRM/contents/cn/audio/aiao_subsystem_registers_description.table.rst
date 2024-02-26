i2s_tdm_sclk_in_sel
'''''''''''''''''''

Select sclk source

.. _table_aiao_i2s_tdm_sclk_in_sel:
.. table:: i2s_tdm_sclk_in_sel, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+---------------------------------+------+
	| Bits | Name                 |Access | Description                     |Reset |
	+======+======================+=======+=================================+======+
	| 2:0  | i2s_tdm_0_sclk_in_sel| R/W   | Selects SCLK input source when  | 0x4  |
	|      |                      |       | i2s_tdm_0 operates in slave     |      |
	|      |                      |       | mode                            |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b000 = Reserved               |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b001 = From i2s_tdm_1         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b010 = From i2s_tdm_2         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b011 = From i2s_tdm_3         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b100 = From internal Audio    |      |
	|      |                      |       | Codec ADC BCLK                  |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b101 = From IO I2S1_BCLK      |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b110 = From IO I2S2_BCLK      |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b111 = Reserved               |      |
	+------+----------------------+-------+---------------------------------+------+
	| 3    | Reserved             |       |                                 |      |
	+------+----------------------+-------+---------------------------------+------+
	| 6:4  | i2s_tdm_1_sclk_in_sel| R/W   | Selects SCLK input source when  | 0x5  |
	|      |                      |       | i2s_tdm_1 operates in slave     |      |
	|      |                      |       | mode                            |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b000 = From i2s_tdm_0         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b001 = From audio_pdm module  |      |
	|      |                      |       | SCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b010 = From i2s_tdm_2         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b011 = From i2s_tdm_3         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b100 = From internal Audio    |      |
	|      |                      |       | Codec ADC BCLK                  |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b101 = From IO I2S1_BCLK      |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b110 = From IO I2S2_BCLK      |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b111 = Reserved               |      |
	+------+----------------------+-------+---------------------------------+------+
	| 7    | Reserved             |       |                                 |      |
	+------+----------------------+-------+---------------------------------+------+
	| 10:8 | i2s_tdm_2_sclk_in_sel| R/W   | Selects SCLK input source when  | 0x6  |
	|      |                      |       | i2s_tdm_2 operates in slave     |      |
	|      |                      |       | mode                            |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b000 = From i2s_tdm_0         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b001 = From i2s_tdm_1         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b010 = Reserved               |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b011 = From i2s_tdm_3         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b100 = From internal Audio    |      |
	|      |                      |       | Codec ADC BCLK                  |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b101 = From IO I2S1_BCLK      |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b110 = From IO I2S2_BCLK      |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b111 = Reserved               |      |
	+------+----------------------+-------+---------------------------------+------+
	| 11   | Reserved             |       |                                 |      |
	+------+----------------------+-------+---------------------------------+------+
	| 14:12| i2s_tdm_3_sclk_in_sel| R/W   | Selects SCLK input source when  | 0x7  |
	|      |                      |       | i2s_tdm_3 operates in slave     |      |
	|      |                      |       | mode                            |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b000 = From i2s_tdm_0         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b001 = From i2s_tdm_1         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b010 = From i2s_tdm_2         |      |
	|      |                      |       | BCLK_out                        |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b011 = Reserved               |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b100 = From internal Audio    |      |
	|      |                      |       | Codec ADC BCLK                  |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b101 = From IO I2S1_BCLK      |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b110 = From IO I2S2_BCLK      |      |
	|      |                      |       |                                 |      |
	|      |                      |       | 3'b111 = Reserved               |      |
	+------+----------------------+-------+---------------------------------+------+
	| 31:15| Reserved             |       |                                 |      |
	+------+----------------------+-------+---------------------------------+------+



i2s_tdm_fs_in_sel
'''''''''''''''''

.. _table_aiao_i2s_tdm_fs_in_sel:
.. table:: i2s_tdm_fs_in_sel, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+------------------------+-------+--------------------------------------+------+
	| Bits | Name                   | Access| Description                          | Reset|
	+======+========================+=======+======================================+======+
	| 2:0  | i2s_tdm_0_fs_in_sel    | R/W   | Select LRCK/FS input source for      | 0x4  |
	|      |                        |       | i2s_tdm_0 operation in slave mode    |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b000 = Reserved                    |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b001 = From i2s_tdm_1 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b010 = From i2s_tdm_2 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b011 = From i2s_tdm_3 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b100 = From internal Audio Codec   |      |
	|      |                        |       | ADC LRCK                             |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b101 = From IO I2S1_LRCK           |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b110 = From IO I2S2_LRCK           |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b111 = Reserved                    |      |
	+------+------------------------+-------+--------------------------------------+------+
	| 3    | Reserved               |       |                                      |      |
	+------+------------------------+-------+--------------------------------------+------+
	| 6:4  | i2s_tdm_1_fs_in_sel    | R/W   | Select LRCK/FS input source for      | 0x5  |
	|      |                        |       | i2s_tdm_1 operation in slave mode    |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b000 = From i2s_tdm_0 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b001 = From audio_pdm module       |      |
	|      |                        |       | lrck_out                             |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b010 = From i2s_tdm_2 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b011 = From i2s_tdm_3 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b100 = From internal Audio Codec   |      |
	|      |                        |       | ADC LRCK                             |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b101 = From IO I2S1_LRCK           |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b110 = From IO I2S2_LRCK           |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b111 = Reserved                    |      |
	+------+------------------------+-------+--------------------------------------+------+
	| 7    | Reserved               |       |                                      |      |
	+------+------------------------+-------+--------------------------------------+------+
	| 10:8 | i2s_tdm_2_fs_in_sel    | R/W   | Select LRCK/FS input source for      | 0x6  |
	|      |                        |       | i2s_tdm_2 operation in slave mode    |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b000 = From i2s_tdm_0 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b001 = From i2s_tdm_1 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b010 = Reserved                    |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b011 = From i2s_tdm_3 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b100 = From internal Audio Codec   |      |
	|      |                        |       | ADC LRCK                             |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b101 = From IO I2S1_LRCK           |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b110 = From IO I2S2_LRCK           |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b111 = Reserved                    |      |
	+------+------------------------+-------+--------------------------------------+------+
	| 11   | Reserved               |       |                                      |      |
	+------+------------------------+-------+--------------------------------------+------+
	| 14:12| i2s_tdm_3_fs_in_sel    | R/W   | Select LRCK/FS input source for      | 0x7  |
	|      |                        |       | i2s_tdm_3 operation in slave mode    |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b000 = From i2s_tdm_0 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b001 = From i2s_tdm_1 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b010 = Reserved                    |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b011 = From i2s_tdm_3 lrck_out     |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b100 = From internal Audio Codec   |      |
	|      |                        |       | ADC LRCK                             |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b101 = From IO I2S1_LRCK           |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b110 = From IO I2S2_LRCK           |      |
	|      |                        |       |                                      |      |
	|      |                        |       | 3'b111 = Reserved                    |      |
	+------+------------------------+-------+--------------------------------------+------+
	| 31:15| Reserved               |       |                                      |      |
	+------+------------------------+-------+--------------------------------------+------+



i2s_tdm_sdi_in_sel
''''''''''''''''''

.. _table_aiao_i2s_tdm_sdi_in_sel:
.. table:: i2s_tdm_sdi_in_sel, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 2:0  | i2s_tdm_0_sdi_in_sel | R/W   | Select i2s_tdm_0       | 0x4  |
	|      |                      |       | RX Module SDI Signal   |      |
	|      |                      |       | Source                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b000 = Reserved      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b001 = From i2s_tdm_1|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b010 = From i2s_tdm_2|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b011 = From i2s_tdm_3|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b100 = From Internal |      |
	|      |                      |       | Audio Codec ADC SDO    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b101 = From IO       |      |
	|      |                      |       | I2S1_SDI               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b110 = From IO       |      |
	|      |                      |       | I2S2_SDI               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b111 = Reserved      |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 6:4  | i2s_tdm_1_sdi_in_sel | R/W   | Select i2s_tdm_1       | 0x5  |
	|      |                      |       | RX Module SDI Signal   |      |
	|      |                      |       | Source                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b000 = From i2s_tdm_0|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b001 = From Audio PDM|      |
	|      |                      |       | Module sdo             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b010 = From i2s_tdm_2|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b011 = From i2s_tdm_3|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b100 = From Internal |      |
	|      |                      |       | Audio Codec ADC SDO    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b101 = From IO       |      |
	|      |                      |       | I2S1_SDI               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b110 = From IO       |      |
	|      |                      |       | I2S2_SDI               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b111 = Reserved      |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 10:8 | i2s_tdm_2_sdi_in_sel | R/W   | Select i2s_tdm_2       | 0x6  |
	|      |                      |       | RX Module SDI Signal   |      |
	|      |                      |       | Source                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b000 = From i2s_tdm_0|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b001 = From i2s_tdm_1|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b010 = Reserved      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b011 = From i2s_tdm_3|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b100 = From Internal |      |
	|      |                      |       | Audio Codec ADC SDO    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b101 = From IO       |      |
	|      |                      |       | I2S1_SDI               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b110 = From IO       |      |
	|      |                      |       | I2S2_SDI               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b111 = Reserved      |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 14:12| i2s_tdm_3_sdi_in_sel | R/W   | Select i2s_tdm_3       | 0x7  |
	|      |                      |       | RX Module SDI Signal   |      |
	|      |                      |       | Source                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b000 = From i2s_tdm_0|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b001 = From i2s_tdm_1|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b010 = From i2s_tdm_2|      |
	|      |                      |       | sdo                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b011 = Reserved      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b100 = From Internal |      |
	|      |                      |       | Audio Codec DAC SDO    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b101 = From IO       |      |
	|      |                      |       | I2S1_SDI               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b110 = From IO       |      |
	|      |                      |       | I2S2_SDI               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b111 = Reserved      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:15| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


i2s_tdm_sdo_out_sel
'''''''''''''''''''

.. _table_aiao_i2s_tdm_sdo_out_sel:
.. table:: i2s_tdm_sdo_out_sel, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 2:0  | i2s_tdm_0_sdo_out_sel| R/W   | Only allowed to        | 0x4  |
	|      |                      |       | configure as default   |      |
	|      |                      |       | value 0x4              |      |
	|      |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 6:4  | i2s_tdm_1_sdo_out_sel| R/W   | Select I2S1_SDO Signal | 0x5  |
	|      |                      |       | Source                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b100 = I2S1_SDO from |      |
	|      |                      |       | i2s_tdm_0 TX Module sdo|      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b101 = I2S1_SDO from |      |
	|      |                      |       | i2s_tdm_1 TX Module sdo|      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b110 = I2S1_SDO from |      |
	|      |                      |       | i2s_tdm_2 TX Module sdo|      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b111 = I2S1_SDO from |      |
	|      |                      |       | i2s_tdm_3 TX Module sdo|      |
	|      |                      |       |                        |      |
	|      |                      |       | Other values = Reserved|      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 10:8 | i2s_tdm_2_sdo_out_sel| R/W   | Select I2S2_SDO Signal | 0x6  |
	|      |                      |       | Source                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b100 = I2S2_SDO from |      |
	|      |                      |       | i2s_tdm_0 TX Module sdo|      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b101 = I2S2_SDO from |      |
	|      |                      |       | i2s_tdm_1 TX Module sdo|      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b110 = I2S2_SDO from |      |
	|      |                      |       | i2s_tdm_2 TX Module sdo|      |
	|      |                      |       |                        |      |
	|      |                      |       | 3'b111 = I2S2_SDO from |      |
	|      |                      |       | i2s_tdm_3 TX Module sdo|      |
	|      |                      |       |                        |      |
	|      |                      |       | Other values = Reserved|      |
	+------+----------------------+-------+------------------------+------+
	| 11   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 14:12| i2s_tdm_3_sdo_out_sel| R/W   | Only allowed to        | 0x7  |
	|      |                      |       | configure as default   |      |
	|      |                      |       | value 0x7              |      |
	|      |                      |       | Internal Audio Codec   |      |
	|      |                      |       | DAC SDI fixed from     |      |
	|      |                      |       | i2s_tdm_3 TX Module sdo|      |
	+------+----------------------+-------+------------------------+------+
	| 31:15| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+



i2s_bclk_oen_sel
''''''''''''''''

.. _table_aiao_i2s_bclk_oen_sel:
.. table:: i2s_bclk_oen_sel, Offset Address: 0x030
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | i2s0_bclk_oen_sel    | R/W   | Reserved               | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 1    | i2s1_bclk_oen_sel    | R/W   | Select I2S1_BCLK IO    | 0x0  |
	|      |                      |       | OEN Control Mode       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Controlled by      |      |
	|      |                      |       | i2s_tdm_1 TX Module    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Controlled by      |      |
	|      |                      |       | Register               |      |
	|      |                      |       | i2s1_bclk_oen_ext      |      |
	|      |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | i2s2_bclk_oen_sel    | R/W   | Select I2S2_BCLK IO    | 0x0  |
	|      |                      |       | OEN Control Mode       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Controlled by      |      |
	|      |                      |       | i2s_tdm_2 TX Module    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Controlled by      |      |
	|      |                      |       | Register               |      |
	|      |                      |       | i2s2_bclk_oen_ext      |      |
	|      |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | i2s3_bclk_oen_sel    | R/W   | Only allowed to        | 0x0  |
	|      |                      |       | configure as default   |      |
	|      |                      |       | value 0x0              |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | i2s0_bclk_oen_ext    | R/W   | Reserved               | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 9    | i2s1_bclk_oen_ext    | R/W   | Controlled by          | 0x0  |
	|      |                      |       | Sub-Register to        |      |
	|      |                      |       | Control I2S1_BCLK IO   |      |
	|      |                      |       | OEN                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Disable IO Output  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Enable IO Output   |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | i2s2_bclk_oen_ext    | R/W   | Controlled by          | 0x0  |
	|      |                      |       | Sub-Register to        |      |
	|      |                      |       | Control I2S2_BCLK IO   |      |
	|      |                      |       | OEN                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Disable IO Output  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Enable IO Output   |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | i2s3_bclk_oen_ext    | R/W   | Only allowed to        | 0x0  |
	|      |                      |       | configure as default   |      |
	|      |                      |       | value 0x0              |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | i2s_bclk_oen_no_delay| R/W   | Only allowed to        | 0x0  |
	|      |                      |       | configure as default   |      |
	|      |                      |       | value 0x0              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:17| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


audio_pdm_ctrl
''''''''''''''

.. _table_aiao_audio_pdm_ctrl:
.. table:: audio_pdm_ctrl, Offset Address: 0x040
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | audio_pdm_sel_i2s1   | R/W   | Enable PDM Mode        | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Normal Operation   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = I2S2 IO Operates   |      |
	|      |                      |       | in PDM Mode, using     |      |
	|      |                      |       | i2s_tdm_1 RX Module    |      |
	|      |                      |       |                        |      |
	|      |                      |       | When this is set to 1, |      |
	|      |                      |       | I2S2_BCLK IO OEN is    |      |
	|      |                      |       | controlled by          |      |
	|      |                      |       | Register i2s2_bclk_oen |      |
	|      |                      |       | _ext                   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


i2s_sys_int_en
''''''''''''''

.. _table_aiao_i2s_sys_int_en:
.. table:: i2s_sys_int_en, Offset Address: 0x060
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | i2s0_int_en          | R/W   | Enable I2S0 Interrupt  | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 1    | i2s1_int_en          | R/W   | Enable I2S1 Interrupt  | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 2    | i2s2_int_en          | R/W   | Enable I2S2 Interrupt  | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 3    | i2s3_int_en          | R/W   | Enable I2S3 Interrupt  | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | i2s_subsys_int_en    | R/W   | Enable I2S_SUBSYS      | 0x1  |
	|      |                      |       | Interrupt              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


i2s_sys_ints
''''''''''''

.. _table_aiao_i2s_sys_ints:
.. table:: i2s_sys_ints, Offset Address: 0x064
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | i2s0_int             | RO    | I2S0 Interrupt Status  |      |
	|      |                      |       | When an I2S0 interrupt |      |
	|      |                      |       | occurs, this can be    |      |
	|      |                      |       | further read to check  |      |
	|      |                      |       | I2S0 register I2S_INT  |      |
	|      |                      |       | value to determine the |      |
	|      |                      |       | interrupt status.      |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | i2s1_int             | RO    | I2S1 Interrupt Status  |      |
	|      |                      |       | When an I2S1 interrupt |      |
	|      |                      |       | occurs, this can be    |      |
	|      |                      |       | further read to check  |      |
	|      |                      |       | I2S1 register I2S_INT  |      |
	|      |                      |       | value to determine the |      |
	|      |                      |       | interrupt status.      |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | i2s2_int             | RO    | I2S2 Interrupt Status  |      |
	|      |                      |       | When an I2S2 interrupt |      |
	|      |                      |       | occurs, this can be    |      |
	|      |                      |       | further read to check  |      |
	|      |                      |       | I2S2 register I2S_INT  |      |
	|      |                      |       | value to determine the |      |
	|      |                      |       | interrupt status.      |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | i2s3_int             | RO    | I2S3 Interrupt Status  |      |
	|      |                      |       | When an I2S3 interrupt |      |
	|      |                      |       | occurs, this can be    |      |
	|      |                      |       | further read to check  |      |
	|      |                      |       | I2S3 register I2S_INT  |      |
	|      |                      |       | value to determine the |      |
	|      |                      |       | interrupt status.      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

