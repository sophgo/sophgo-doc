DMAC_IDREG
~~~~~~~~~~

.. _table_dmac_idreg:
.. table:: DMAC_IDREG, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 63:0 | DMAC_IDREG           | RO    | DMAC ID Number         |      |
	+------+----------------------+-------+------------------------+------+

DMAC_COMPVERREG
~~~~~~~~~~~~~~~

.. _table_dmac_cmppverreg:
.. table:: DMAC_COMPVERREG, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | DMAC_COMPVER         | RO    | DMAC Component Version |      |
	|      |                      |       | Number.                |      |
	+------+----------------------+-------+------------------------+------+

DMAC_CFGREG
~~~~~~~~~~~

.. _table_dmac_cfgreg:
.. table:: DMAC_CFGREG, Offset Address: 0x010
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | DMAC_EN              | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | enable the             |      |
	|      |                      |       | DW_axi_dmac.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DW_axi_dmac       |      |
	|      |                      |       |   disabled             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DW_axi_dmac       |      |
	|      |                      |       |   enabled              |      |
	|      |                      |       |                        |      |
	|      |                      |       | NOTE: If this bit      |      |
	|      |                      |       | DMAC_EN bit is cleared |      |
	|      |                      |       | while any channel      |      |
	|      |                      |       | is still active, then  |      |
	|      |                      |       | this bit still returns |      |
	|      |                      |       | 1 to indicate that     |      |
	|      |                      |       | there                  |      |
	|      |                      |       | are channels still     |      |
	|      |                      |       | active until           |      |
	|      |                      |       | DW_axi_dmac hardware   |      |
	|      |                      |       | has                    |      |
	|      |                      |       | terminated all         |      |
	|      |                      |       | activity on all        |      |
	|      |                      |       | channels, at which     |      |
	|      |                      |       | point this bit         |      |
	|      |                      |       | returns zero (0).      |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | INT_EN               | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | globally enable the    |      |
	|      |                      |       | interrupt generation.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DW_axi_dmac       |      |
	|      |                      |       |   Interrupts are       |      |
	|      |                      |       |   disabled             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DW_axi_dmac       |      |
	|      |                      |       |   Interrupt logic is   |      |
	|      |                      |       |   enabled.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DMAC_CHENREG
~~~~~~~~~~~~

.. _table_dmac_chenreg:
.. table:: DMAC_CHENREG, Offset Address: 0x018
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CH1_EN               | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | enable the DW_axi_dmac |      |
	|      |                      |       | Channel-1.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DW_axi_dmac       |      |
	|      |                      |       |   Channel-1 is disabled|      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DW_axi_dmac       |      |
	|      |                      |       |   Channel-1 is enabled |      |
	|      |                      |       |                        |      |
	|      |                      |       | The bit                |      |
	|      |                      |       | 'DMAC_ChEnReg.CH1_EN'  |      |
	|      |                      |       | is automatically       |      |
	|      |                      |       | cleared                |      |
	|      |                      |       | by hardware to disable |      |
	|      |                      |       | the channel after the  |      |
	|      |                      |       | last AMBA              |      |
	|      |                      |       | transfer of the DMA    |      |
	|      |                      |       | transfer to the        |      |
	|      |                      |       | destination has        |      |
	|      |                      |       | completed. Software    |      |
	|      |                      |       | can therefore poll     |      |
	|      |                      |       | this bit to determine  |      |
	|      |                      |       | when this channel is   |      |
	|      |                      |       | free for a new DMA     |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | CH2_EN               | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | enable the DW_axi_dmac |      |
	|      |                      |       | Channel-2.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DW_axi_dmac       |      |
	|      |                      |       |   Channel-2 is disabled|      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DW_axi_dmac       |      |
	|      |                      |       |   Channel-2 is enabled |      |
	|      |                      |       |                        |      |
	|      |                      |       | The bit                |      |
	|      |                      |       | 'DMAC_ChEnReg.CH2_EN'  |      |
	|      |                      |       | is automatically       |      |
	|      |                      |       | cleared                |      |
	|      |                      |       | by hardware to disable |      |
	|      |                      |       | the channel after the  |      |
	|      |                      |       | last AMBA              |      |
	|      |                      |       | transfer of the DMA    |      |
	|      |                      |       | transfer to the        |      |
	|      |                      |       | destination has        |      |
	|      |                      |       | completed. Software    |      |
	|      |                      |       | can therefore poll     |      |
	|      |                      |       | this bit to determine  |      |
	|      |                      |       | when this channel is   |      |
	|      |                      |       | free for a new DMA     |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | CH3_EN               | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | enable the DW_axi_dmac |      |
	|      |                      |       | Channel-3.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DW_axi_dmac       |      |
	|      |                      |       |   Channel-3 is disabled|      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DW_axi_dmac       |      |
	|      |                      |       |   Channel-3 is enabled |      |
	|      |                      |       |                        |      |
	|      |                      |       | The bit                |      |
	|      |                      |       | 'DMAC_ChEnReg.CH3_EN'  |      |
	|      |                      |       | is automatically       |      |
	|      |                      |       | cleared                |      |
	|      |                      |       | by hardware to disable |      |
	|      |                      |       | the channel after the  |      |
	|      |                      |       | last AMBA              |      |
	|      |                      |       | transfer of the DMA    |      |
	|      |                      |       | transfer to the        |      |
	|      |                      |       | destination has        |      |
	|      |                      |       | completed. Software    |      |
	|      |                      |       | can therefore poll     |      |
	|      |                      |       | this bit to determine  |      |
	|      |                      |       | when this channel is   |      |
	|      |                      |       | free for a new DMA     |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | CH4_EN               | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | enable the DW_axi_dmac |      |
	|      |                      |       | Channel-4.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DW_axi_dmac       |      |
	|      |                      |       |   Channel-4 is disabled|      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DW_axi_dmac       |      |
	|      |                      |       |   Channel-4 is enabled |      |
	|      |                      |       |                        |      |
	|      |                      |       | The bit                |      |
	|      |                      |       | 'DMAC_ChEnReg.CH4_EN'  |      |
	|      |                      |       | is automatically       |      |
	|      |                      |       | cleared                |      |
	|      |                      |       | by hardware to disable |      |
	|      |                      |       | the channel after the  |      |
	|      |                      |       | last AMBA              |      |
	|      |                      |       | transfer of the DMA    |      |
	|      |                      |       | transfer to the        |      |
	|      |                      |       | destination has        |      |
	|      |                      |       | completed. Software    |      |
	|      |                      |       | can therefore poll     |      |
	|      |                      |       | this bit to determine  |      |
	|      |                      |       | when this channel is   |      |
	|      |                      |       | free for a new DMA     |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | CH5_EN               | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | enable the DW_axi_dmac |      |
	|      |                      |       | Channel-5.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DW_axi_dmac       |      |
	|      |                      |       |   Channel-5 is disabled|      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DW_axi_dmac       |      |
	|      |                      |       |   Channel-5 is enabled |      |
	|      |                      |       |                        |      |
	|      |                      |       | The bit                |      |
	|      |                      |       | 'DMAC_ChEnReg.CH5_EN'  |      |
	|      |                      |       | is automatically       |      |
	|      |                      |       | cleared                |      |
	|      |                      |       | by hardware to disable |      |
	|      |                      |       | the channel after the  |      |
	|      |                      |       | last AMBA              |      |
	|      |                      |       | transfer of the DMA    |      |
	|      |                      |       | transfer to the        |      |
	|      |                      |       | destination has        |      |
	|      |                      |       | completed. Software    |      |
	|      |                      |       | can therefore poll     |      |
	|      |                      |       | this bit to determine  |      |
	|      |                      |       | when this channel is   |      |
	|      |                      |       | free for a new DMA     |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | CH6_EN               | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | enable the DW_axi_dmac |      |
	|      |                      |       | Channel-6.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DW_axi_dmac       |      |
	|      |                      |       |   Channel-6 is disabled|      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DW_axi_dmac       |      |
	|      |                      |       |   Channel-6 is enabled |      |
	|      |                      |       |                        |      |
	|      |                      |       | The bit                |      |
	|      |                      |       | 'DMAC_ChEnReg.CH6_EN'  |      |
	|      |                      |       | is automatically       |      |
	|      |                      |       | cleared                |      |
	|      |                      |       | by hardware to disable |      |
	|      |                      |       | the channel after the  |      |
	|      |                      |       | last AMBA              |      |
	|      |                      |       | transfer of the DMA    |      |
	|      |                      |       | transfer to the        |      |
	|      |                      |       | destination has        |      |
	|      |                      |       | completed. Software    |      |
	|      |                      |       | can therefore poll     |      |
	|      |                      |       | this bit to determine  |      |
	|      |                      |       | when this channel is   |      |
	|      |                      |       | free for a new DMA     |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | CH7_EN               | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | enable the DW_axi_dmac |      |
	|      |                      |       | Channel-7.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DW_axi_dmac       |      |
	|      |                      |       |   Channel-7 is disabled|      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DW_axi_dmac       |      |
	|      |                      |       |   Channel-7 is enabled |      |
	|      |                      |       |                        |      |
	|      |                      |       | The bit                |      |
	|      |                      |       | 'DMAC_ChEnReg.CH7_EN'  |      |
	|      |                      |       | is automatically       |      |
	|      |                      |       | cleared                |      |
	|      |                      |       | by hardware to disable |      |
	|      |                      |       | the channel after the  |      |
	|      |                      |       | last AMBA              |      |
	|      |                      |       | transfer of the DMA    |      |
	|      |                      |       | transfer to the        |      |
	|      |                      |       | destination has        |      |
	|      |                      |       | completed. Software    |      |
	|      |                      |       | can therefore poll     |      |
	|      |                      |       | this bit to determine  |      |
	|      |                      |       | when this channel is   |      |
	|      |                      |       | free for a new DMA     |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | CH8_EN               | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | enable the DW_axi_dmac |      |
	|      |                      |       | Channel-8.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DW_axi_dmac       |      |
	|      |                      |       |   Channel-8 is disabled|      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DW_axi_dmac       |      |
	|      |                      |       |   Channel-8 is enabled |      |
	|      |                      |       |                        |      |
	|      |                      |       | The bit                |      |
	|      |                      |       | 'DMAC_ChEnReg.CH8_EN'  |      |
	|      |                      |       | is automatically       |      |
	|      |                      |       | cleared                |      |
	|      |                      |       | by hardware to disable |      |
	|      |                      |       | the channel after the  |      |
	|      |                      |       | last AMBA              |      |
	|      |                      |       | transfer of the DMA    |      |
	|      |                      |       | transfer to the        |      |
	|      |                      |       | destination has        |      |
	|      |                      |       | completed. Software    |      |
	|      |                      |       | can therefore poll     |      |
	|      |                      |       | this bit to determine  |      |
	|      |                      |       | when this channel is   |      |
	|      |                      |       | free for a new DMA     |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | CH1_EN_WE            | WO    | DW_axi_dmac Channel-1  | 0x0  |
	|      |                      |       | Enable Write Enable    |      |
	|      |                      |       | bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Read back value of     |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always '0'.            |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | CH2_EN_WE            | WO    | DW_axi_dmac Channel-2  | 0x0  |
	|      |                      |       | Enable Write Enable    |      |
	|      |                      |       | bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Read back value of     |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always '0'.            |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | CH3_EN_WE            | WO    | DW_axi_dmac Channel-3  | 0x0  |
	|      |                      |       | Enable Write Enable    |      |
	|      |                      |       | bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Read back value of     |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always '0'.            |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | CH4_EN_WE            | WO    | DW_axi_dmac Channel-4  | 0x0  |
	|      |                      |       | Enable Write Enable    |      |
	|      |                      |       | bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Read back value of     |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always '0'.            |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | CH5_EN_WE            | WO    | DW_axi_dmac Channel-5  | 0x0  |
	|      |                      |       | Enable Write Enable    |      |
	|      |                      |       | bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Read back value of     |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always '0'.            |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | CH6_EN_WE            | WO    | DW_axi_dmac Channel-6  | 0x0  |
	|      |                      |       | Enable Write Enable    |      |
	|      |                      |       | bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Read back value of     |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always '0'.            |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | CH7_EN_WE            | WO    | DW_axi_dmac Channel-7  | 0x0  |
	|      |                      |       | Enable Write Enable    |      |
	|      |                      |       | bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Read back value of     |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always '0'.            |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | CH8_EN_WE            | WO    | DW_axi_dmac Channel-8  | 0x0  |
	|      |                      |       | Enable Write Enable    |      |
	|      |                      |       | bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Read back value of     |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always '0'.            |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | CH1_SUSP             | R/W   | Channel-1 Suspend      | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel suspend. If    |      |
	|      |                      |       | this                   |      |
	|      |                      |       | bit is set to 1,       |      |
	|      |                      |       | DW_axi_dmac suspends   |      |
	|      |                      |       | all DMA data           |      |
	|      |                      |       | transfers from the     |      |
	|      |                      |       | source gracefully      |      |
	|      |                      |       | until this bit is      |      |
	|      |                      |       | cleared.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | There is no guarantee  |      |
	|      |                      |       | that the current dma   |      |
	|      |                      |       | transaction will       |      |
	|      |                      |       | complete. This bit can |      |
	|      |                      |       | also be used in        |      |
	|      |                      |       | conjunction with       |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H1_Status.CH_SUSPENDED |      |
	|      |                      |       | to cleanly disable the |      |
	|      |                      |       | channel without losing |      |
	|      |                      |       | any data. In this      |      |
	|      |                      |       | case, software first   |      |
	|      |                      |       | sets CH1_SUSP bit to 1 |      |
	|      |                      |       | and polls              |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H1_Status.CH_SUSPENDED |      |
	|      |                      |       | till it is set to 1.   |      |
	|      |                      |       | Software can           |      |
	|      |                      |       | then clear CH1_EN bit  |      |
	|      |                      |       | to 0 to disable the    |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel        |      |
	|      |                      |       |   Suspend Request.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Suspend.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software can clear     |      |
	|      |                      |       | CH1_SUSP bit to 0,     |      |
	|      |                      |       | after DW_axi_dmac      |      |
	|      |                      |       | sets                   |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H1_Status.CH_SUSPENDED |      |
	|      |                      |       | bit to 1, to exit the  |      |
	|      |                      |       | channel suspend mode.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: CH_SUSP is       |      |
	|      |                      |       | cleared when channel   |      |
	|      |                      |       | is disabled.           |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | CH2_SUSP             | R/W   | Channel-2 Suspend      | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel suspend. If    |      |
	|      |                      |       | this                   |      |
	|      |                      |       | bit is set to 1,       |      |
	|      |                      |       | DW_axi_dmac suspends   |      |
	|      |                      |       | all DMA data           |      |
	|      |                      |       | transfers from the     |      |
	|      |                      |       | source gracefully      |      |
	|      |                      |       | until this bit is      |      |
	|      |                      |       | cleared.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | There is no guarantee  |      |
	|      |                      |       | that the current dma   |      |
	|      |                      |       | transaction will       |      |
	|      |                      |       | complete. This bit can |      |
	|      |                      |       | also be used in        |      |
	|      |                      |       | conjunction with       |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H2_Status.CH_SUSPENDED |      |
	|      |                      |       | to cleanly disable the |      |
	|      |                      |       | channel without losing |      |
	|      |                      |       | any data. In this      |      |
	|      |                      |       | case, software first   |      |
	|      |                      |       | sets CH2_SUSP bit to 1 |      |
	|      |                      |       | and polls              |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H2_Status.CH_SUSPENDED |      |
	|      |                      |       | till it is set to 1.   |      |
	|      |                      |       | Software can           |      |
	|      |                      |       | then clear CH2_EN bit  |      |
	|      |                      |       | to 0 to disable the    |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel        |      |
	|      |                      |       |   Suspend Request.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Suspend.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software can clear     |      |
	|      |                      |       | CH2_SUSP bit to 0,     |      |
	|      |                      |       | after DW_axi_dmac      |      |
	|      |                      |       | sets                   |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H2_Status.CH_SUSPENDED |      |
	|      |                      |       | bit to 1, to exit the  |      |
	|      |                      |       | channel suspend mode.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: CH_SUSP is       |      |
	|      |                      |       | cleared when channel   |      |
	|      |                      |       | is disabled.           |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | CH3_SUSP             | R/W   | Channel-3 Suspend      | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel suspend. If    |      |
	|      |                      |       | this                   |      |
	|      |                      |       | bit is set to 1,       |      |
	|      |                      |       | DW_axi_dmac suspends   |      |
	|      |                      |       | all DMA data           |      |
	|      |                      |       | transfers from the     |      |
	|      |                      |       | source gracefully      |      |
	|      |                      |       | until this bit is      |      |
	|      |                      |       | cleared.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | There is no guarantee  |      |
	|      |                      |       | that the current dma   |      |
	|      |                      |       | transaction will       |      |
	|      |                      |       | complete. This bit can |      |
	|      |                      |       | also be used in        |      |
	|      |                      |       | conjunction with       |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H3_Status.CH_SUSPENDED |      |
	|      |                      |       | to cleanly disable the |      |
	|      |                      |       | channel without losing |      |
	|      |                      |       | any data. In this      |      |
	|      |                      |       | case, software first   |      |
	|      |                      |       | sets CH3_SUSP bit to 1 |      |
	|      |                      |       | and polls              |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H3_Status.CH_SUSPENDED |      |
	|      |                      |       | till it is set to 1.   |      |
	|      |                      |       | Software can           |      |
	|      |                      |       | then clear CH3_EN bit  |      |
	|      |                      |       | to 0 to disable the    |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel        |      |
	|      |                      |       |   Suspend Request.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Suspend.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software can clear     |      |
	|      |                      |       | CH3_SUSP bit to 0,     |      |
	|      |                      |       | after DW_axi_dmac      |      |
	|      |                      |       | sets                   |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H3_Status.CH_SUSPENDED |      |
	|      |                      |       | bit to 1, to exit the  |      |
	|      |                      |       | channel suspend mode.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: CH_SUSP is       |      |
	|      |                      |       | cleared when channel   |      |
	|      |                      |       | is disabled.           |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | CH4_SUSP             | R/W   | Channel-4 Suspend      | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel suspend. If    |      |
	|      |                      |       | this                   |      |
	|      |                      |       | bit is set to 1,       |      |
	|      |                      |       | DW_axi_dmac suspends   |      |
	|      |                      |       | all DMA data           |      |
	|      |                      |       | transfers from the     |      |
	|      |                      |       | source gracefully      |      |
	|      |                      |       | until this bit is      |      |
	|      |                      |       | cleared.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | There is no guarantee  |      |
	|      |                      |       | that the current dma   |      |
	|      |                      |       | transaction will       |      |
	|      |                      |       | complete. This bit can |      |
	|      |                      |       | also be used in        |      |
	|      |                      |       | conjunction with       |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H4_Status.CH_SUSPENDED |      |
	|      |                      |       | to cleanly disable the |      |
	|      |                      |       | channel without losing |      |
	|      |                      |       | any data. In this      |      |
	|      |                      |       | case, software first   |      |
	|      |                      |       | sets CH4_SUSP bit to 1 |      |
	|      |                      |       | and polls              |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H4_Status.CH_SUSPENDED |      |
	|      |                      |       | till it is set to 1.   |      |
	|      |                      |       | Software can           |      |
	|      |                      |       | then clear CH4_EN bit  |      |
	|      |                      |       | to 0 to disable the    |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel        |      |
	|      |                      |       |   Suspend Request.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Suspend.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software can clear     |      |
	|      |                      |       | CH4_SUSP bit to 0,     |      |
	|      |                      |       | after DW_axi_dmac      |      |
	|      |                      |       | sets                   |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H4_Status.CH_SUSPENDED |      |
	|      |                      |       | bit to 1, to exit the  |      |
	|      |                      |       | channel suspend mode.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: CH_SUSP is       |      |
	|      |                      |       | cleared when channel   |      |
	|      |                      |       | is disabled.           |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | CH5_SUSP             | R/W   | Channel-5 Suspend      | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel suspend. If    |      |
	|      |                      |       | this                   |      |
	|      |                      |       | bit is set to 1,       |      |
	|      |                      |       | DW_axi_dmac suspends   |      |
	|      |                      |       | all DMA data           |      |
	|      |                      |       | transfers from the     |      |
	|      |                      |       | source gracefully      |      |
	|      |                      |       | until this bit is      |      |
	|      |                      |       | cleared.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | There is no guarantee  |      |
	|      |                      |       | that the current dma   |      |
	|      |                      |       | transaction will       |      |
	|      |                      |       | complete. This bit can |      |
	|      |                      |       | also be used in        |      |
	|      |                      |       | conjunction with       |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H5_Status.CH_SUSPENDED |      |
	|      |                      |       | to cleanly disable the |      |
	|      |                      |       | channel without losing |      |
	|      |                      |       | any data. In this      |      |
	|      |                      |       | case, software first   |      |
	|      |                      |       | sets CH5_SUSP bit to 1 |      |
	|      |                      |       | and polls              |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H5_Status.CH_SUSPENDED |      |
	|      |                      |       | till it is set to 1.   |      |
	|      |                      |       | Software can           |      |
	|      |                      |       | then clear CH5_EN bit  |      |
	|      |                      |       | to 0 to disable the    |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel        |      |
	|      |                      |       |   Suspend Request.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Suspend.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software can clear     |      |
	|      |                      |       | CH5_SUSP bit to 0,     |      |
	|      |                      |       | after DW_axi_dmac      |      |
	|      |                      |       | sets                   |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H5_Status.CH_SUSPENDED |      |
	|      |                      |       | bit to 1, to exit the  |      |
	|      |                      |       | channel suspend mode.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: CH_SUSP is       |      |
	|      |                      |       | cleared when channel   |      |
	|      |                      |       | is disabled.           |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | CH6_SUSP             | R/W   | Channel-6 Suspend      | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel suspend. If    |      |
	|      |                      |       | this                   |      |
	|      |                      |       | bit is set to 1,       |      |
	|      |                      |       | DW_axi_dmac suspends   |      |
	|      |                      |       | all DMA data           |      |
	|      |                      |       | transfers from the     |      |
	|      |                      |       | source gracefully      |      |
	|      |                      |       | until this bit is      |      |
	|      |                      |       | cleared.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | There is no guarantee  |      |
	|      |                      |       | that the current dma   |      |
	|      |                      |       | transaction will       |      |
	|      |                      |       | complete. This bit can |      |
	|      |                      |       | also be used in        |      |
	|      |                      |       | conjunction with       |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H6_Status.CH_SUSPENDED |      |
	|      |                      |       | to cleanly disable the |      |
	|      |                      |       | channel without losing |      |
	|      |                      |       | any data. In this      |      |
	|      |                      |       | case, software first   |      |
	|      |                      |       | sets CH6_SUSP bit to 1 |      |
	|      |                      |       | and polls              |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H6_Status.CH_SUSPENDED |      |
	|      |                      |       | till it is set to 1.   |      |
	|      |                      |       | Software can           |      |
	|      |                      |       | then clear CH6_EN bit  |      |
	|      |                      |       | to 0 to disable the    |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel        |      |
	|      |                      |       |   Suspend Request.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Suspend.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software can clear     |      |
	|      |                      |       | CH6_SUSP bit to 0,     |      |
	|      |                      |       | after DW_axi_dmac      |      |
	|      |                      |       | sets                   |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H6_Status.CH_SUSPENDED |      |
	|      |                      |       | bit to 1, to exit the  |      |
	|      |                      |       | channel suspend mode.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: CH_SUSP is       |      |
	|      |                      |       | cleared when channel   |      |
	|      |                      |       | is disabled.           |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | CH7_SUSP             | R/W   | Channel-7 Suspend      | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel suspend. If    |      |
	|      |                      |       | this                   |      |
	|      |                      |       | bit is set to 1,       |      |
	|      |                      |       | DW_axi_dmac suspends   |      |
	|      |                      |       | all DMA data           |      |
	|      |                      |       | transfers from the     |      |
	|      |                      |       | source gracefully      |      |
	|      |                      |       | until this bit is      |      |
	|      |                      |       | cleared.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | There is no guarantee  |      |
	|      |                      |       | that the current dma   |      |
	|      |                      |       | transaction will       |      |
	|      |                      |       | complete. This bit can |      |
	|      |                      |       | also be used in        |      |
	|      |                      |       | conjunction with       |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H7_Status.CH_SUSPENDED |      |
	|      |                      |       | to cleanly disable the |      |
	|      |                      |       | channel without losing |      |
	|      |                      |       | any data. In this      |      |
	|      |                      |       | case, software first   |      |
	|      |                      |       | sets CH7_SUSP bit to 1 |      |
	|      |                      |       | and polls              |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H7_Status.CH_SUSPENDED |      |
	|      |                      |       | till it is set to 1.   |      |
	|      |                      |       | Software can           |      |
	|      |                      |       | then clear CH7_EN bit  |      |
	|      |                      |       | to 0 to disable the    |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel        |      |
	|      |                      |       |   Suspend Request.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Suspend.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software can clear     |      |
	|      |                      |       | CH7_SUSP bit to 0,     |      |
	|      |                      |       | after DW_axi_dmac      |      |
	|      |                      |       | sets                   |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H7_Status.CH_SUSPENDED |      |
	|      |                      |       | bit to 1, to exit the  |      |
	|      |                      |       | channel suspend mode.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: CH_SUSP is       |      |
	|      |                      |       | cleared when channel   |      |
	|      |                      |       | is disabled.           |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | CH8_SUSP             | R/W   | Channel-8 Suspend      | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel suspend. If    |      |
	|      |                      |       | this                   |      |
	|      |                      |       | bit is set to 1,       |      |
	|      |                      |       | DW_axi_dmac suspends   |      |
	|      |                      |       | all DMA data           |      |
	|      |                      |       | transfers from the     |      |
	|      |                      |       | source gracefully      |      |
	|      |                      |       | until this bit is      |      |
	|      |                      |       | cleared.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | There is no guarantee  |      |
	|      |                      |       | that the current dma   |      |
	|      |                      |       | transaction will       |      |
	|      |                      |       | complete. This bit can |      |
	|      |                      |       | also be used in        |      |
	|      |                      |       | conjunction with       |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H8_Status.CH_SUSPENDED |      |
	|      |                      |       | to cleanly disable the |      |
	|      |                      |       | channel without losing |      |
	|      |                      |       | any data. In this      |      |
	|      |                      |       | case, software first   |      |
	|      |                      |       | sets CH8_SUSP bit to 1 |      |
	|      |                      |       | and polls              |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H8_Status.CH_SUSPENDED |      |
	|      |                      |       | till it is set to 1.   |      |
	|      |                      |       | Software can           |      |
	|      |                      |       | then clear CH8_EN bit  |      |
	|      |                      |       | to 0 to disable the    |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel        |      |
	|      |                      |       |   Suspend Request.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Suspend.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software can clear     |      |
	|      |                      |       | CH8_SUSP bit to 0,     |      |
	|      |                      |       | after DW_axi_dmac      |      |
	|      |                      |       | sets                   |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | H8_Status.CH_SUSPENDED |      |
	|      |                      |       | bit to 1, to exit the  |      |
	|      |                      |       | channel suspend mode.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: CH_SUSP is       |      |
	|      |                      |       | cleared when channel   |      |
	|      |                      |       | is disabled.           |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | CH1_SUSP_WE          | WO    | This bit is used as a  | 0x0  |
	|      |                      |       | write enable to the    |      |
	|      |                      |       | Channel-1 Suspend      |      |
	|      |                      |       | bit. The read back     |      |
	|      |                      |       | value of this register |      |
	|      |                      |       | bit is always 0.       |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | CH2_SUSP_WE          | WO    | This bit is used as a  | 0x0  |
	|      |                      |       | write enable to the    |      |
	|      |                      |       | Channel-2 Suspend      |      |
	|      |                      |       | bit. The read back     |      |
	|      |                      |       | value of this register |      |
	|      |                      |       | bit is always 0.       |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | CH3_SUSP_WE          | WO    | This bit is used as a  | 0x0  |
	|      |                      |       | write enable to the    |      |
	|      |                      |       | Channel-3 Suspend      |      |
	|      |                      |       | bit. The read back     |      |
	|      |                      |       | value of this register |      |
	|      |                      |       | bit is always 0.       |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | CH4_SUSP_WE          | WO    | This bit is used as a  | 0x0  |
	|      |                      |       | write enable to the    |      |
	|      |                      |       | Channel-4 Suspend      |      |
	|      |                      |       | bit. The read back     |      |
	|      |                      |       | value of this register |      |
	|      |                      |       | bit is always 0.       |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | CH5_SUSP_WE          | WO    | This bit is used as a  | 0x0  |
	|      |                      |       | write enable to the    |      |
	|      |                      |       | Channel-5 Suspend      |      |
	|      |                      |       | bit. The read back     |      |
	|      |                      |       | value of this register |      |
	|      |                      |       | bit is always 0.       |      |
	+------+----------------------+-------+------------------------+------+
	| 29   | CH6_SUSP_WE          | WO    | This bit is used as a  | 0x0  |
	|      |                      |       | write enable to the    |      |
	|      |                      |       | Channel-6 Suspend      |      |
	|      |                      |       | bit. The read back     |      |
	|      |                      |       | value of this register |      |
	|      |                      |       | bit is always 0.       |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | CH7_SUSP_WE          | WO    | This bit is used as a  | 0x0  |
	|      |                      |       | write enable to the    |      |
	|      |                      |       | Channel-7 Suspend      |      |
	|      |                      |       | bit. The read back     |      |
	|      |                      |       | value of this register |      |
	|      |                      |       | bit is always 0.       |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | CH8_SUSP_WE          | WO    | This bit is used as a  | 0x0  |
	|      |                      |       | write enable to the    |      |
	|      |                      |       | Channel-8 Suspend      |      |
	|      |                      |       | bit. The read back     |      |
	|      |                      |       | value of this register |      |
	|      |                      |       | bit is always 0.       |      |
	+------+----------------------+-------+------------------------+------+
	| 32   | CH1_ABORT            | R/W   | Channel-1 Abort        | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel abort. If this |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | is set to 1,           |      |
	|      |                      |       | DW_axi_dmac disables   |      |
	|      |                      |       | the channel            |      |
	|      |                      |       | immediately.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Aborting the channel   |      |
	|      |                      |       | might result in AXI    |      |
	|      |                      |       | Protocol violation as  |      |
	|      |                      |       | DW_axi_dmac does not   |      |
	|      |                      |       | make sure that all AXI |      |
	|      |                      |       | transfers              |      |
	|      |                      |       | initiated on the       |      |
	|      |                      |       | master interface are   |      |
	|      |                      |       | completed.Aborting the |      |
	|      |                      |       | channel is not         |      |
	|      |                      |       | recommended and should |      |
	|      |                      |       | be used only in        |      |
	|      |                      |       | situations where a     |      |
	|      |                      |       | particular channel     |      |
	|      |                      |       | hangs due to no        |      |
	|      |                      |       | response from the      |      |
	|      |                      |       | corresponding AXI      |      |
	|      |                      |       | slave interface and    |      |
	|      |                      |       | software wants to      |      |
	|      |                      |       | disable the channel    |      |
	|      |                      |       | without resetting the  |      |
	|      |                      |       | entire DW_axi_dmac. It |      |
	|      |                      |       | is recommended to try  |      |
	|      |                      |       | channel                |      |
	|      |                      |       | disabling first and    |      |
	|      |                      |       | then only opt for      |      |
	|      |                      |       | channel aborting.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel Abort  |      |
	|      |                      |       |   Request.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Abort.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | DW_axi_dmac clears     |      |
	|      |                      |       | this bit to 0 once the |      |
	|      |                      |       | channel is             |      |
	|      |                      |       | aborted (when it sets  |      |
	|      |                      |       | CH1_Status.CH_ABORTED  |      |
	|      |                      |       | bit to 1).             |      |
	+------+----------------------+-------+------------------------+------+
	| 33   | CH2_ABORT            | R/W   | Channel-2 Abort        | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel abort. If this |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | is set to 1,           |      |
	|      |                      |       | DW_axi_dmac disables   |      |
	|      |                      |       | the channel            |      |
	|      |                      |       | immediately.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Aborting the channel   |      |
	|      |                      |       | might result in AXI    |      |
	|      |                      |       | Protocol violation as  |      |
	|      |                      |       | DW_axi_dmac does not   |      |
	|      |                      |       | make sure that all AXI |      |
	|      |                      |       | transfers              |      |
	|      |                      |       | initiated on the       |      |
	|      |                      |       | master interface are   |      |
	|      |                      |       | completed.Aborting the |      |
	|      |                      |       | channel is not         |      |
	|      |                      |       | recommended and should |      |
	|      |                      |       | be used only in        |      |
	|      |                      |       | situations where a     |      |
	|      |                      |       | particular channel     |      |
	|      |                      |       | hangs due to no        |      |
	|      |                      |       | response from the      |      |
	|      |                      |       | corresponding AXI      |      |
	|      |                      |       | slave interface and    |      |
	|      |                      |       | software wants to      |      |
	|      |                      |       | disable the channel    |      |
	|      |                      |       | without resetting the  |      |
	|      |                      |       | entire DW_axi_dmac. It |      |
	|      |                      |       | is recommended to try  |      |
	|      |                      |       | channel                |      |
	|      |                      |       | disabling first and    |      |
	|      |                      |       | then only opt for      |      |
	|      |                      |       | channel aborting.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel Abort  |      |
	|      |                      |       |   Request.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Abort.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | DW_axi_dmac clears     |      |
	|      |                      |       | this bit to 0 once the |      |
	|      |                      |       | channel is             |      |
	|      |                      |       | aborted (when it sets  |      |
	|      |                      |       | CH2_Status.CH_ABORTED  |      |
	|      |                      |       | bit to 1).             |      |
	+------+----------------------+-------+------------------------+------+
	| 34   | CH3_ABORT            | R/W   | Channel-3 Abort        | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel abort. If this |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | is set to 1,           |      |
	|      |                      |       | DW_axi_dmac disables   |      |
	|      |                      |       | the channel            |      |
	|      |                      |       | immediately.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Aborting the channel   |      |
	|      |                      |       | might result in AXI    |      |
	|      |                      |       | Protocol violation as  |      |
	|      |                      |       | DW_axi_dmac does not   |      |
	|      |                      |       | make sure that all AXI |      |
	|      |                      |       | transfers              |      |
	|      |                      |       | initiated on the       |      |
	|      |                      |       | master interface are   |      |
	|      |                      |       | completed.Aborting the |      |
	|      |                      |       | channel is not         |      |
	|      |                      |       | recommended and should |      |
	|      |                      |       | be used only in        |      |
	|      |                      |       | situations where a     |      |
	|      |                      |       | particular channel     |      |
	|      |                      |       | hangs due to no        |      |
	|      |                      |       | response from the      |      |
	|      |                      |       | corresponding AXI      |      |
	|      |                      |       | slave interface and    |      |
	|      |                      |       | software wants to      |      |
	|      |                      |       | disable the channel    |      |
	|      |                      |       | without resetting the  |      |
	|      |                      |       | entire DW_axi_dmac. It |      |
	|      |                      |       | is recommended to try  |      |
	|      |                      |       | channel                |      |
	|      |                      |       | disabling first and    |      |
	|      |                      |       | then only opt for      |      |
	|      |                      |       | channel aborting.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel Abort  |      |
	|      |                      |       |   Request.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Abort.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | DW_axi_dmac clears     |      |
	|      |                      |       | this bit to 0 once the |      |
	|      |                      |       | channel is             |      |
	|      |                      |       | aborted (when it sets  |      |
	|      |                      |       | CH3_Status.CH_ABORTED  |      |
	|      |                      |       | bit to 1).             |      |
	+------+----------------------+-------+------------------------+------+
	| 35   | CH4_ABORT            | R/W   | Channel-4 Abort        | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel abort. If this |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | is set to 1,           |      |
	|      |                      |       | DW_axi_dmac disables   |      |
	|      |                      |       | the channel            |      |
	|      |                      |       | immediately.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Aborting the channel   |      |
	|      |                      |       | might result in AXI    |      |
	|      |                      |       | Protocol violation as  |      |
	|      |                      |       | DW_axi_dmac does not   |      |
	|      |                      |       | make sure that all AXI |      |
	|      |                      |       | transfers              |      |
	|      |                      |       | initiated on the       |      |
	|      |                      |       | master interface are   |      |
	|      |                      |       | completed.Aborting the |      |
	|      |                      |       | channel is not         |      |
	|      |                      |       | recommended and should |      |
	|      |                      |       | be used only in        |      |
	|      |                      |       | situations where a     |      |
	|      |                      |       | particular channel     |      |
	|      |                      |       | hangs due to no        |      |
	|      |                      |       | response from the      |      |
	|      |                      |       | corresponding AXI      |      |
	|      |                      |       | slave interface and    |      |
	|      |                      |       | software wants to      |      |
	|      |                      |       | disable the channel    |      |
	|      |                      |       | without resetting the  |      |
	|      |                      |       | entire DW_axi_dmac. It |      |
	|      |                      |       | is recommended to try  |      |
	|      |                      |       | channel                |      |
	|      |                      |       | disabling first and    |      |
	|      |                      |       | then only opt for      |      |
	|      |                      |       | channel aborting.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel Abort  |      |
	|      |                      |       |   Request.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Abort.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | DW_axi_dmac clears     |      |
	|      |                      |       | this bit to 0 once the |      |
	|      |                      |       | channel is             |      |
	|      |                      |       | aborted (when it sets  |      |
	|      |                      |       | CH4_Status.CH_ABORTED  |      |
	|      |                      |       | bit to 1).             |      |
	+------+----------------------+-------+------------------------+------+
	| 36   | CH5_ABORT            | R/W   | Channel-5 Abort        | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel abort. If this |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | is set to 1,           |      |
	|      |                      |       | DW_axi_dmac disables   |      |
	|      |                      |       | the channel            |      |
	|      |                      |       | immediately.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Aborting the channel   |      |
	|      |                      |       | might result in AXI    |      |
	|      |                      |       | Protocol violation as  |      |
	|      |                      |       | DW_axi_dmac does not   |      |
	|      |                      |       | make sure that all AXI |      |
	|      |                      |       | transfers              |      |
	|      |                      |       | initiated on the       |      |
	|      |                      |       | master interface are   |      |
	|      |                      |       | completed.Aborting the |      |
	|      |                      |       | channel is not         |      |
	|      |                      |       | recommended and should |      |
	|      |                      |       | be used only in        |      |
	|      |                      |       | situations where a     |      |
	|      |                      |       | particular channel     |      |
	|      |                      |       | hangs due to no        |      |
	|      |                      |       | response from the      |      |
	|      |                      |       | corresponding AXI      |      |
	|      |                      |       | slave interface and    |      |
	|      |                      |       | software wants to      |      |
	|      |                      |       | disable the channel    |      |
	|      |                      |       | without resetting the  |      |
	|      |                      |       | entire DW_axi_dmac. It |      |
	|      |                      |       | is recommended to try  |      |
	|      |                      |       | channel                |      |
	|      |                      |       | disabling first and    |      |
	|      |                      |       | then only opt for      |      |
	|      |                      |       | channel aborting.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel Abort  |      |
	|      |                      |       |   Request.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Abort.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | DW_axi_dmac clears     |      |
	|      |                      |       | this bit to 0 once the |      |
	|      |                      |       | channel is             |      |
	|      |                      |       | aborted (when it sets  |      |
	|      |                      |       | CH5_Status.CH_ABORTED  |      |
	|      |                      |       | bit to 1).             |      |
	+------+----------------------+-------+------------------------+------+
	| 37   | CH6_ABORT            | R/W   | Channel-6 Abort        | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel abort. If this |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | is set to 1,           |      |
	|      |                      |       | DW_axi_dmac disables   |      |
	|      |                      |       | the channel            |      |
	|      |                      |       | immediately.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Aborting the channel   |      |
	|      |                      |       | might result in AXI    |      |
	|      |                      |       | Protocol violation as  |      |
	|      |                      |       | DW_axi_dmac does not   |      |
	|      |                      |       | make sure that all AXI |      |
	|      |                      |       | transfers              |      |
	|      |                      |       | initiated on the       |      |
	|      |                      |       | master interface are   |      |
	|      |                      |       | completed.Aborting the |      |
	|      |                      |       | channel is not         |      |
	|      |                      |       | recommended and should |      |
	|      |                      |       | be used only in        |      |
	|      |                      |       | situations where a     |      |
	|      |                      |       | particular channel     |      |
	|      |                      |       | hangs due to no        |      |
	|      |                      |       | response from the      |      |
	|      |                      |       | corresponding AXI      |      |
	|      |                      |       | slave interface and    |      |
	|      |                      |       | software wants to      |      |
	|      |                      |       | disable the channel    |      |
	|      |                      |       | without resetting the  |      |
	|      |                      |       | entire DW_axi_dmac. It |      |
	|      |                      |       | is recommended to try  |      |
	|      |                      |       | channel                |      |
	|      |                      |       | disabling first and    |      |
	|      |                      |       | then only opt for      |      |
	|      |                      |       | channel aborting.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel Abort  |      |
	|      |                      |       |   Request.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Abort.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | DW_axi_dmac clears     |      |
	|      |                      |       | this bit to 0 once the |      |
	|      |                      |       | channel is             |      |
	|      |                      |       | aborted (when it sets  |      |
	|      |                      |       | CH6_Status.CH_ABORTED  |      |
	|      |                      |       | bit to 1).             |      |
	+------+----------------------+-------+------------------------+------+
	| 38   | CH7_ABORT            | R/W   | Channel-7 Abort        | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel abort. If this |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | is set to 1,           |      |
	|      |                      |       | DW_axi_dmac disables   |      |
	|      |                      |       | the channel            |      |
	|      |                      |       | immediately.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Aborting the channel   |      |
	|      |                      |       | might result in AXI    |      |
	|      |                      |       | Protocol violation as  |      |
	|      |                      |       | DW_axi_dmac does not   |      |
	|      |                      |       | make sure that all AXI |      |
	|      |                      |       | transfers              |      |
	|      |                      |       | initiated on the       |      |
	|      |                      |       | master interface are   |      |
	|      |                      |       | completed.Aborting the |      |
	|      |                      |       | channel is not         |      |
	|      |                      |       | recommended and should |      |
	|      |                      |       | be used only in        |      |
	|      |                      |       | situations where a     |      |
	|      |                      |       | particular channel     |      |
	|      |                      |       | hangs due to no        |      |
	|      |                      |       | response from the      |      |
	|      |                      |       | corresponding AXI      |      |
	|      |                      |       | slave interface and    |      |
	|      |                      |       | software wants to      |      |
	|      |                      |       | disable the channel    |      |
	|      |                      |       | without resetting the  |      |
	|      |                      |       | entire DW_axi_dmac. It |      |
	|      |                      |       | is recommended to try  |      |
	|      |                      |       | channel                |      |
	|      |                      |       | disabling first and    |      |
	|      |                      |       | then only opt for      |      |
	|      |                      |       | channel aborting.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel Abort  |      |
	|      |                      |       |   Request.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Abort.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | DW_axi_dmac clears     |      |
	|      |                      |       | this bit to 0 once the |      |
	|      |                      |       | channel is             |      |
	|      |                      |       | aborted (when it sets  |      |
	|      |                      |       | CH7_Status.CH_ABORTED  |      |
	|      |                      |       | bit to 1).             |      |
	+------+----------------------+-------+------------------------+------+
	| 39   | CH8_ABORT            | R/W   | Channel-8 Abort        | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Software sets this bit |      |
	|      |                      |       | to 1 to request        |      |
	|      |                      |       | channel abort. If this |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | is set to 1,           |      |
	|      |                      |       | DW_axi_dmac disables   |      |
	|      |                      |       | the channel            |      |
	|      |                      |       | immediately.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Aborting the channel   |      |
	|      |                      |       | might result in AXI    |      |
	|      |                      |       | Protocol violation as  |      |
	|      |                      |       | DW_axi_dmac does not   |      |
	|      |                      |       | make sure that all AXI |      |
	|      |                      |       | transfers              |      |
	|      |                      |       | initiated on the       |      |
	|      |                      |       | master interface are   |      |
	|      |                      |       | completed.Aborting the |      |
	|      |                      |       | channel is not         |      |
	|      |                      |       | recommended and should |      |
	|      |                      |       | be used only in        |      |
	|      |                      |       | situations where a     |      |
	|      |                      |       | particular channel     |      |
	|      |                      |       | hangs due to no        |      |
	|      |                      |       | response from the      |      |
	|      |                      |       | corresponding AXI      |      |
	|      |                      |       | slave interface and    |      |
	|      |                      |       | software wants to      |      |
	|      |                      |       | disable the channel    |      |
	|      |                      |       | without resetting the  |      |
	|      |                      |       | entire DW_axi_dmac. It |      |
	|      |                      |       | is recommended to try  |      |
	|      |                      |       | channel                |      |
	|      |                      |       | disabling first and    |      |
	|      |                      |       | then only opt for      |      |
	|      |                      |       | channel aborting.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Channel Abort  |      |
	|      |                      |       |   Request.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Request for       |      |
	|      |                      |       |   Channel Abort.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | DW_axi_dmac clears     |      |
	|      |                      |       | this bit to 0 once the |      |
	|      |                      |       | channel is             |      |
	|      |                      |       | aborted (when it sets  |      |
	|      |                      |       | CH8_Status.CH_ABORTED  |      |
	|      |                      |       | bit to 1).             |      |
	+------+----------------------+-------+------------------------+------+
	| 40   | CH1_ABORT_WE         | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | write enable the       |      |
	|      |                      |       | Channel-1 Abort bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | The read back value of |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always 0.              |      |
	+------+----------------------+-------+------------------------+------+
	| 41   | CH2_ABORT_WE         | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | write enable the       |      |
	|      |                      |       | Channel-2 Abort bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | The read back value of |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always 0.              |      |
	+------+----------------------+-------+------------------------+------+
	| 42   | CH3_ABORT_WE         | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | write enable the       |      |
	|      |                      |       | Channel-3 Abort bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | The read back value of |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always 0.              |      |
	+------+----------------------+-------+------------------------+------+
	| 43   | CH4_ABORT_WE         | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | write enable the       |      |
	|      |                      |       | Channel-4 Abort bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | The read back value of |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always 0.              |      |
	+------+----------------------+-------+------------------------+------+
	| 44   | CH5_ABORT_WE         | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | write enable the       |      |
	|      |                      |       | Channel-5 Abort bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | The read back value of |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always 0.              |      |
	+------+----------------------+-------+------------------------+------+
	| 45   | CH6_ABORT_WE         | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | write enable the       |      |
	|      |                      |       | Channel-6 Abort bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | The read back value of |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always 0.              |      |
	+------+----------------------+-------+------------------------+------+
	| 46   | CH7_ABORT_WE         | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | write enable the       |      |
	|      |                      |       | Channel-7 Abort bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | The read back value of |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always 0.              |      |
	+------+----------------------+-------+------------------------+------+
	| 47   | CH8_ABORT_WE         | R/W   | This bit is used to    | 0x0  |
	|      |                      |       | write enable the       |      |
	|      |                      |       | Channel-8 Abort bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | The read back value of |      |
	|      |                      |       | this register bit is   |      |
	|      |                      |       | always 0.              |      |
	+------+----------------------+-------+------------------------+------+
	| 63:48| RSVD_DMAC_CHENREG    | RO    | DMAC_CHENREG Reserved  |      |
	|      |                      |       | bits                   |      |
	+------+----------------------+-------+------------------------+------+

DMAC_INTSTATUSREG
~~~~~~~~~~~~~~~~~

.. _table_dmac_intstatusreg:
.. table:: DMAC_INTSTATUSREG, Offset Address: 0x030
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CH1_IntStat          | RO    | Channel 1 Interrupt    |      |
	|      |                      |       | Status Bit.            |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | CH2_IntStat          | RO    | Channel 2 Interrupt    |      |
	|      |                      |       | Status Bit.            |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | CH3_IntStat          | RO    | Channel 3 Interrupt    |      |
	|      |                      |       | Status Bit.            |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | CH4_IntStat          | RO    | Channel 4 Interrupt    |      |
	|      |                      |       | Status Bit.            |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | CH5_IntStat          | RO    | Channel 5 Interrupt    |      |
	|      |                      |       | Status Bit.            |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | CH6_IntStat          | RO    | Channel 6 Interrupt    |      |
	|      |                      |       | Status Bit.            |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | CH7_IntStat          | RO    | Channel 7 Interrupt    |      |
	|      |                      |       | Status Bit.            |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | CH8_IntStat          | RO    | Channel 8 Interrupt    |      |
	|      |                      |       | Status Bit.            |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | CommonReg_IntStat    | RO    | Common Register        |      |
	|      |                      |       | Interrupt Status Bit.  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:17| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DMAC_COMMONREG_INTCLEARREG
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _table_dmac_commonreg_intclearreg:
.. table:: DMAC_COMMONREG_INTCLEARREG, Offset Address: 0x038
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | Clear_SLVIF_Commo    | WO    | Slave Interface Common | 0x0  |
	|      | nReg_DEC_ERR_IntStat |       | Register Decode Error  |      |
	|      |                      |       | Interrupt              |      |
	|      |                      |       | clear Bit.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit             |      |
	|      |                      |       | (SLVIF_Com\            |      |
	|      |                      |       | monReg_DEC_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C\                |      |
	|      |                      |       | ommonReg_IntStatusReg. |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | Clear_SLVIF_CommonR  | WO    | Slave Interface Common | 0x0  |
	|      | eg_WR2RO_ERR_IntStat |       | Register Write to Read |      |
	|      |                      |       | only Error             |      |
	|      |                      |       | Interrupt clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status                 |      |
	|      |                      |       | bit(SLVIF_Commo\       |      |
	|      |                      |       | nReg_WR2RO_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C\                |      |
	|      |                      |       | ommonReg_IntStatusReg. |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Clear_SLVIF_CommonR  | WO    | Slave Interface Common | 0x0  |
	|      | eg_RD2WO_ERR_IntStat |       | Register Read to Write |      |
	|      |                      |       | only Error             |      |
	|      |                      |       | Interrupt clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status                 |      |
	|      |                      |       | bit(SLVIF_Commo\       |      |
	|      |                      |       | nReg_RD2WO_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C\                |      |
	|      |                      |       | ommonReg_IntStatusReg. |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Cl                   | WO    | Slave Interface Common | 0x0  |
	|      | ear_SLVIF_CommonReg\_|       | Register Write On Hold |      |
	|      | WrOnHold_ERR_IntStat |       | Error                  |      |
	|      |                      |       | Interrupt clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status                 |      |
	|      |                      |       | bit(SLVIF_CommonRe\    |      |
	|      |                      |       | g_WrOnHold_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C\                |      |
	|      |                      |       | ommonReg_IntStatusReg. |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | Clear_SLVIF_Undefine | WO    | Slave Interface        | 0x0  |
	|      | dReg_DEC_ERR_IntStat |       | Undefined register     |      |
	|      |                      |       | Decode Error Interrupt |      |
	|      |                      |       | clear Bit.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status                 |      |
	|      |                      |       | bit(SLVIF_Undefi\      |      |
	|      |                      |       | nedReg_DEC_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C\                |      |
	|      |                      |       | ommonReg_IntStatusReg. |      |
	+------+----------------------+-------+------------------------+------+
	| 31:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DMAC_COMMONREG_INTSTATUS_ENABLEREG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _table_dmac_commonreg_intstatus_enablereg:
.. table:: DMAC_COMMONREG_INTSTATUS_ENABLEREG, Offset Address: 0x040
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | Enable_SLVIF_Commo   | R/W   | Slave Interface Common | 0x0  |
	|      | nReg_DEC_ERR_IntStat |       | Register Decode Error  |      |
	|      |                      |       | Interrupt              |      |
	|      |                      |       | Status Enable Bit.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the             |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt status bit   |      |
	|      |                      |       | (SLVIF_Com             |      |
	|      |                      |       | monReg_DEC_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C                 |      |
	|      |                      |       | ommonReg_IntStatusReg. |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | Enable_SLVIF_CommonR | R/W   | Slave Interface Common | 0x0  |
	|      | eg_WR2RO_ERR_IntStat |       | Register Write to Read |      |
	|      |                      |       | only Error             |      |
	|      |                      |       | Interrupt Status       |      |
	|      |                      |       | Enable Bit.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the             |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt status bit   |      |
	|      |                      |       | (SLVIF_Commo           |      |
	|      |                      |       | nReg_WR2RO_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C                 |      |
	|      |                      |       | ommonReg_IntStatusReg. |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Enable_SLVIF_CommonR | R/W   | Slave Interface Common | 0x0  |
	|      | eg_RD2WO_ERR_IntStat |       | Register Read to Write |      |
	|      |                      |       | only Error             |      |
	|      |                      |       | Interrupt Status       |      |
	|      |                      |       | Enable Bit.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the             |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt status bit   |      |
	|      |                      |       | (SLVIF_Commo           |      |
	|      |                      |       | nReg_RD2WO_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C                 |      |
	|      |                      |       | ommonReg_IntStatusReg. |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Ena                  | R/W   | Slave Interface Common | 0x0  |
	|      | ble_SLVIF_CommonReg\_|       | Register Write On Hold |      |
	|      | WrOnHold_ERR_IntStat |       | Error                  |      |
	|      |                      |       | Interrupt Status       |      |
	|      |                      |       | Enable Bit.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the             |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt status bit   |      |
	|      |                      |       | (SLVIF_CommonRe        |      |
	|      |                      |       | g_WrOnHold_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C                 |      |
	|      |                      |       | ommonReg_IntStatusReg. |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | E                    | R/W   | Slave Interface        | 0x0  |
	|      | nable_SLVIF_Undefine |       | Undefined register     |      |
	|      | dReg_DEC_ERR_IntStat |       | Decode Error Interrupt |      |
	|      |                      |       | Status enable Bit.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the             |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt status bit   |      |
	|      |                      |       | (SLVIF_Undefi          |      |
	|      |                      |       | nedReg_DEC_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C                 |      |
	|      |                      |       | ommonReg_IntStatusReg. |      |
	+------+----------------------+-------+------------------------+------+
	| 31:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DMAC_COMMONREG_INTSIGNAL_ENABLEREG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _table_dmac_commonreg_intsignal_enablereg:
.. table:: DMAC_COMMONREG_INTSIGNAL_ENABLEREG, Offset Address: 0x048
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | Enable_SLVIF_CommonR | R/W   | Slave Interface Common | 0x0  |
	|      | eg_DEC_ERR_IntSignal |       | Register Decode Error  |      |
	|      |                      |       | Interrupt              |      |
	|      |                      |       | Signal Enable Bit.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the propagation |      |
	|      |                      |       | of corresponding       |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | status bit             |      |
	|      |                      |       | (SLVIF_Com             |      |
	|      |                      |       | monReg_DEC_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C                 |      |
	|      |                      |       | ommonReg_IntStatusReg) |      |
	|      |                      |       | to generate a port     |      |
	|      |                      |       | level interrupt.       |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | En                   | R/W   | Slave Interface Common | 0x0  |
	|      | able_SLVIF_CommonReg |       | Register Write to Read |      |
	|      | _WR2RO_ERR_IntSignal |       | only Error             |      |
	|      |                      |       | Interrupt Signal       |      |
	|      |                      |       | Enable Bit.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the propagation |      |
	|      |                      |       | of corresponding       |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | status bit             |      |
	|      |                      |       | (SLVIF_Commo           |      |
	|      |                      |       | nReg_WR2RO_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C                 |      |
	|      |                      |       | ommonReg_IntStatusReg) |      |
	|      |                      |       | to generate a port     |      |
	|      |                      |       | level interrupt.       |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | En                   | R/W   | Slave Interface Common | 0x0  |
	|      | able_SLVIF_CommonReg |       | Register Read to Write |      |
	|      | _RD2WO_ERR_IntSignal |       | only Error             |      |
	|      |                      |       | Interrupt Signal       |      |
	|      |                      |       | Enable Bit.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the propagation |      |
	|      |                      |       | of corresponding       |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | status bit             |      |
	|      |                      |       | (SLVIF_Commo           |      |
	|      |                      |       | nReg_RD2WO_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C                 |      |
	|      |                      |       | ommonReg_IntStatusReg) |      |
	|      |                      |       | to generate a port     |      |
	|      |                      |       | level interrupt.       |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Enabl                | R/W   | Slave Interface Common | 0x0  |
	|      | e_SLVIF_CommonReg_Wr |       | Register Write On Hold |      |
	|      | OnHold_ERR_IntSignal |       | Error                  |      |
	|      |                      |       | Interrupt Signal       |      |
	|      |                      |       | Enable Bit.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the propagation |      |
	|      |                      |       | of corresponding       |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | status                 |      |
	|      |                      |       | bit(SLVIF_CommonRe     |      |
	|      |                      |       | g_WrOnHold_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C                 |      |
	|      |                      |       | ommonReg_IntStatusReg) |      |
	|      |                      |       | to generate a port     |      |
	|      |                      |       | level interrupt.       |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | Ena                  | R/W   | Slave Interface        | 0x0  |
	|      | ble_SLVIF_UndefinedR |       | Undefined register     |      |
	|      | eg_DEC_ERR_IntSignal |       | Decode Error Interrupt |      |
	|      |                      |       | Signal Enable Bit.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the propagation |      |
	|      |                      |       | of corresponding       |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | status                 |      |
	|      |                      |       | bit(SLVIF_Undefi       |      |
	|      |                      |       | nedReg_DEC_ERR_IntStat |      |
	|      |                      |       | in                     |      |
	|      |                      |       | DMAC_C                 |      |
	|      |                      |       | ommonReg_IntStatusReg) |      |
	|      |                      |       | to generate a port     |      |
	|      |                      |       | level interrupt.       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


DMAC_COMMONREG_INTSTATUSREG
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _table_dmac_commonreg_intstatusreg:
.. table:: DMAC_COMMONREG_INTSTATUSREG, Offset Address: 0x050
	:widths: 1 3 1 6 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SLVIF_Commo          | RO    | Slave Interface Common |      |
	|      | nReg_DEC_ERR_IntStat |       | Register Decode Error  |      |
	|      |                      |       | Interrupt Status Bit.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Decode Error generated |      |
	|      |                      |       | by DW_axi_dmac during  |      |
	|      |                      |       | register               |      |
	|      |                      |       | access. This error     |      |
	|      |                      |       | occurs if the register |      |
	|      |                      |       | access is to an        |      |
	|      |                      |       | invalid address in the |      |
	|      |                      |       | common register space  |      |
	|      |                      |       | (0x000 to              |      |
	|      |                      |       | 0x0FF) resulting in    |      |
	|      |                      |       | error response by      |      |
	|      |                      |       | DW_axi_dmac slave      |      |
	|      |                      |       | interface.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Decode     |      |
	|      |                      |       |   Errors.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Decode Error         |      |
	|      |                      |       |   detected.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | The Error Interrupt    |      |
	|      |                      |       | status is generated if |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | Status Enable bit in   |      |
	|      |                      |       | DMAC_Comm              |      |
	|      |                      |       | onReg_IntStatus_Enable |      |
	|      |                      |       | register bit is set to |      |
	|      |                      |       | 1. This bit is cleared |      |
	|      |                      |       | to 0 on writing 1 to   |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | clear bit in           |      |
	|      |                      |       | DMAC                   |      |
	|      |                      |       | _COMMONREG_INTCLEARREG |      |
	|      |                      |       | on enabling the        |      |
	|      |                      |       | channel (required when |      |
	|      |                      |       | the interrupt is not   |      |
	|      |                      |       | enabled).              |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | SLVIF_CommonR        | RO    | Slave Interface Common |      |
	|      | eg_WR2RO_ERR_IntStat |       | Register Write to Read |      |
	|      |                      |       | Only Error             |      |
	|      |                      |       | Interrupt Status bit.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | This error occurs if   |      |
	|      |                      |       | write operation is     |      |
	|      |                      |       | performed to a Read    |      |
	|      |                      |       | Only register in the   |      |
	|      |                      |       | common register space  |      |
	|      |                      |       | (0x000 to 0x0FF).      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Write to   |      |
	|      |                      |       |   Read Only Errors.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Write to Read Only   |      |
	|      |                      |       |   Error detected.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | Error Interrupt status |      |
	|      |                      |       | is generated if the    |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | Status Enable bit in   |      |
	|      |                      |       | DMAC_Comm              |      |
	|      |                      |       | onReg_IntStatus_Enable |      |
	|      |                      |       | register bit is set to |      |
	|      |                      |       | 1. This bit is cleared |      |
	|      |                      |       | to 0 on writing 1 to   |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | clear bit in           |      |
	|      |                      |       | DMAC                   |      |
	|      |                      |       | _COMMONREG_INTCLEARREG |      |
	|      |                      |       | on enabling the        |      |
	|      |                      |       | channel (required when |      |
	|      |                      |       | the interrupt is not   |      |
	|      |                      |       | enabled).              |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_dmac_commonreg_intstatusreg_2:
.. table:: DMAC_COMMONREG_INTSTATUSREG, Offset Address: 0x050 (continued)
	:widths: 1 3 1 6 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 2    | SLVIF_CommonR        | RO    | Slave Interface Common |      |
	|      | eg_RD2WO_ERR_IntStat |       | Register Read to Write |      |
	|      |                      |       | only Error             |      |
	|      |                      |       | Interrupt Status bit.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | This error occurs if   |      |
	|      |                      |       | Read operation is      |      |
	|      |                      |       | performed to a Write   |      |
	|      |                      |       | Only register in the   |      |
	|      |                      |       | common register space  |      |
	|      |                      |       | (0x000 to 0x0FF).      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Read to    |      |
	|      |                      |       |   Write Only Errors.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Read to Write Only   |      |
	|      |                      |       |   Error detected.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | Error Interrupt status |      |
	|      |                      |       | is generated if the    |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | Status Enable bit in   |      |
	|      |                      |       | DMAC_Comm              |      |
	|      |                      |       | onReg_IntStatus_Enable |      |
	|      |                      |       | register bit is set to |      |
	|      |                      |       | 1. This bit is cleared |      |
	|      |                      |       | to 0 on writing 1 to   |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | clear bit in           |      |
	|      |                      |       | DMAC                   |      |
	|      |                      |       | _COMMONREG_INTCLEARREG |      |
	|      |                      |       | on enabling the        |      |
	|      |                      |       | channel (required when |      |
	|      |                      |       | the interrupt is not   |      |
	|      |                      |       | enabled).              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Values:                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x1                  |      |
	|      |                      |       |   (Active_CommonReg\   |      |
	|      |                      |       |   _RD2WO_ERR):         |      |
	|      |                      |       |   Slave                |      |
	|      |                      |       |   Interface Read to    |      |
	|      |                      |       |   Write Only Error     |      |
	|      |                      |       |   detected             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x0                  |      |
	|      |                      |       |   (Inactive_CommonReg\ |      |
	|      |                      |       |   _RD2WO_ERR):         |      |
	|      |                      |       |   No Slave             |      |
	|      |                      |       |   Interface Read to    |      |
	|      |                      |       |   Write Only Errors    |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | SLVIF_CommonReg\_    | RO    | Slave Interface Common |      |
	|      | WrOnHold_ERR_IntStat |       | Register Write On Hold |      |
	|      |                      |       | Error                  |      |
	|      |                      |       | Interrupt Status Bit.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | This error occurs if   |      |
	|      |                      |       | an illegal write       |      |
	|      |                      |       | operation is performed |      |
	|      |                      |       | on                     |      |
	|      |                      |       | a common register;     |      |
	|      |                      |       | this happens if a      |      |
	|      |                      |       | write operation is     |      |
	|      |                      |       | performed on a common  |      |
	|      |                      |       | register except        |      |
	|      |                      |       | DMAC_RESETREG with     |      |
	|      |                      |       | DMAC_RST field set to  |      |
	|      |                      |       | 1 when                 |      |
	|      |                      |       | DW_axi_dmac is in Hold |      |
	|      |                      |       | mode.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Common     |      |
	|      |                      |       |   Register Write On    |      |
	|      |                      |       |   Hold Errors.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Common Register Write|      |
	|      |                      |       |   On Hold Error        |      |
	|      |                      |       |   detected.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Error Interrupt Status |      |
	|      |                      |       | is generated if the    |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | Status Enable bit in   |      |
	|      |                      |       | DMAC_Comm              |      |
	|      |                      |       | onReg_IntStatus_Enable |      |
	|      |                      |       | register bit is set to |      |
	|      |                      |       | 1. This bit is cleared |      |
	|      |                      |       | to 0 on writing 1 to   |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | clear bit in           |      |
	|      |                      |       | DMAC                   |      |
	|      |                      |       | _COMMONREG_INTCLEARREG |      |
	|      |                      |       | on enabling the        |      |
	|      |                      |       | channel (required when |      |
	|      |                      |       | the interrupt is not   |      |
	|      |                      |       | enabled).              |      |
	+------+----------------------+-------+------------------------+------+
	
To be continued ......

.. _table_dmac_commonreg_intstatusreg_3:
.. table:: DMAC_COMMONREG_INTSTATUSREG, Offset Address: 0x050 (continued)
	:widths: 1 3 1 6 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | SLVIF_Undefine       | RO    | Slave Interface        |      |
	|      | dReg_DEC_ERR_IntStat |       | Undefined register     |      |
	|      |                      |       | Decode Error Interrupt |      |
	|      |                      |       | Signal Enable Bit.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Decode Error generated |      |
	|      |                      |       | by DW_axi_dmac during  |      |
	|      |                      |       | register               |      |
	|      |                      |       | access. This error     |      |
	|      |                      |       | occurs if the register |      |
	|      |                      |       | access is to           |      |
	|      |                      |       | undefined address      |      |
	|      |                      |       | range (>0x8FF if 8     |      |
	|      |                      |       | channels are           |      |
	|      |                      |       | configured, >0x4FF if  |      |
	|      |                      |       | 4 channels are         |      |
	|      |                      |       | configured etc.)       |      |
	|      |                      |       | resulting in error     |      |
	|      |                      |       | response by            |      |
	|      |                      |       | DW_axi_dmac slave      |      |
	|      |                      |       | interface.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Decode     |      |
	|      |                      |       |   Errors.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Decode Error         |      |
	|      |                      |       |   detected. Error      |      |
	|      |                      |       |   Interrupt Status     |      |
	|      |                      |       |   is generated if the  |      |
	|      |                      |       |   corresponding        |      |
	|      |                      |       |   Status Enable bit in |      |
	|      |                      |       |   DMAC_Comm\           |      |
	|      |                      |       |   onReg_IntStatus\     |      |
	|      |                      |       |   _Enable register     |      |
	|      |                      |       |   bit is set to 1.     |      |
	|      |                      |       |   This bit is cleared  |      |
	|      |                      |       |   to 0 on writing 1 to |      |
	|      |                      |       |   the corresponding    |      |
	|      |                      |       |   channel interrupt    |      |
	|      |                      |       |   clear bit in         |      |
	|      |                      |       |   DMAC\                |      |
	|      |                      |       |   _COMMONREG\          |      |
	|      |                      |       |   _INTCLEARREG         |      |
	|      |                      |       |   on enabling the      |      |
	|      |                      |       |   channel (required    |      |
	|      |                      |       |   when the interrupt   |      |
	|      |                      |       |   is not enabled).     |      |
	+------+----------------------+-------+------------------------+------+
	| 31:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DMAC_RESETREG
~~~~~~~~~~~~~

.. _table_dmac_resetreg:
.. table:: DMAC_RESETREG, Offset Address: 0x058
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | DMAC_RST             | R/W   | DMAC Reset Request bit | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Software writes 1 to   |      |
	|      |                      |       | this bit to reset the  |      |
	|      |                      |       | DW_axi_dmac and        |      |
	|      |                      |       | polls this bit to see  |      |
	|      |                      |       | it as 0. DW_axi_dmac   |      |
	|      |                      |       | resets all the         |      |
	|      |                      |       | modules except the     |      |
	|      |                      |       | slave bus interface    |      |
	|      |                      |       | module and clears      |      |
	|      |                      |       | this bit to 0.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | NOTE: Software is not  |      |
	|      |                      |       | allowed to write 0 to  |      |
	|      |                      |       | this bit.              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CHx_SAR
~~~~~~~

.. _table_chx_sar:
.. table:: CHx_SAR, Offset Address: 0x100
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 63:0 | SAR                  | R/W   | Current Source Address | 0x0  |
	|      |                      |       | of DMA transfer.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | Updated after each     |      |
	|      |                      |       | source transfer. The   |      |
	|      |                      |       | SINC fields in the     |      |
	|      |                      |       | CHx_CTL register       |      |
	|      |                      |       | determines whether the |      |
	|      |                      |       | address                |      |
	|      |                      |       | increments or is left  |      |
	|      |                      |       | unchanged on every     |      |
	|      |                      |       | source transfer        |      |
	|      |                      |       | throughout the block   |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+

CHx_DAR
~~~~~~~

.. _table_chx_dar:
.. table:: CHx_DAR, Offset Address: 0x108
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 63:0 | DAR                  | R/W   | Current Destination    | 0x0  |
	|      |                      |       | Address of DMA         |      |
	|      |                      |       | transfer.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Updated after each     |      |
	|      |                      |       | destination transfer.  |      |
	|      |                      |       | The DINC fields in     |      |
	|      |                      |       | the CHx_CTL register   |      |
	|      |                      |       | determines whether the |      |
	|      |                      |       | address                |      |
	|      |                      |       | increments or is left  |      |
	|      |                      |       | unchanged on every     |      |
	|      |                      |       | destination transfer   |      |
	|      |                      |       | throughout the block   |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+

CHx_BLOCK_TS
~~~~~~~~~~~~

.. _table_chx_block_ts:
.. table:: CHx_BLOCK_TS, Offset Address: 0x110
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 21:0 | BLOCK_TS             | R/W   | Block Transfer Size.   | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | The number programmed  |      |
	|      |                      |       | into BLOCK_TS field    |      |
	|      |                      |       | indicates the          |      |
	|      |                      |       | total number of data   |      |
	|      |                      |       | of width               |      |
	|      |                      |       | CHx_CTL.SRC_TR_WIDTH   |      |
	|      |                      |       | to                     |      |
	|      |                      |       | be transferred in a    |      |
	|      |                      |       | DMA block transfer.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Block Transfer Size =  |      |
	|      |                      |       | BLOCK_TS+1             |      |
	|      |                      |       |                        |      |
	|      |                      |       | When the transfer      |      |
	|      |                      |       | starts, the read-back  |      |
	|      |                      |       | value is the total     |      |
	|      |                      |       | number of data items   |      |
	|      |                      |       | already read from the  |      |
	|      |                      |       | source                 |      |
	|      |                      |       | peripheral, regardless |      |
	|      |                      |       | of who is the flow     |      |
	|      |                      |       | controller. When the   |      |
	|      |                      |       | source or destination  |      |
	|      |                      |       | peripheral is assigned |      |
	|      |                      |       | as the flow            |      |
	|      |                      |       | controller, the value  |      |
	|      |                      |       | before the transfer    |      |
	|      |                      |       | starts saturates at    |      |
	|      |                      |       | DMAX_CHx_MAX_BLK_SIZE, |      |
	|      |                      |       | but the actual block   |      |
	|      |                      |       | size can               |      |
	|      |                      |       | be greater.            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:22| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CHx_CTL
~~~~~~~

.. _table_chx_ctl:
.. table:: CHx_CTL, Offset Address: 0x118
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SMS                  | R/W   | Source Master Select.  | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Identifies the Master  |      |
	|      |                      |       | Interface layer from   |      |
	|      |                      |       | which the source       |      |
	|      |                      |       | device (peripheral or  |      |
	|      |                      |       | memory) is accessed.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: AXI master 1      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: AXI Master 2      |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | DMS                  | R/W   | Destination Master     | 0x0  |
	|      |                      |       | Select.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | Identifies the Master  |      |
	|      |                      |       | Interface layer from   |      |
	|      |                      |       | which the              |      |
	|      |                      |       | destination device     |      |
	|      |                      |       | (peripheral or memory) |      |
	|      |                      |       | is accessed.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: AXI master 1      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: AXI Master 2      |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | SINC                 | R/W   | Source Address         | 0x0  |
	|      |                      |       | Increment.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Indicates whether to   |      |
	|      |                      |       | increment the source   |      |
	|      |                      |       | address on every       |      |
	|      |                      |       | source transfer. If    |      |
	|      |                      |       | the device is fetching |      |
	|      |                      |       | data from a source     |      |
	|      |                      |       | peripheral FIFO with a |      |
	|      |                      |       | fixed address, then    |      |
	|      |                      |       | set this field to 'No  |      |
	|      |                      |       | change'.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Increment         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: No Change         |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | DINC                 | R/W   | Destination Address    | 0x0  |
	|      |                      |       | Increment.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Indicates whether to   |      |
	|      |                      |       | increment the          |      |
	|      |                      |       | destination address on |      |
	|      |                      |       | every destination      |      |
	|      |                      |       | transfer. If the       |      |
	|      |                      |       | device is writing data |      |
	|      |                      |       | from a                 |      |
	|      |                      |       | source peripheral FIFO |      |
	|      |                      |       | with a fixed address,  |      |
	|      |                      |       | then set this          |      |
	|      |                      |       | field to 'No change'.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Increment         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: No Change         |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 10:8 | SRC_TR_WIDTH         | R/W   | Source Transfer Width. | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Mapped to AXI bus      |      |
	|      |                      |       | arsize, this value     |      |
	|      |                      |       | must be less than or   |      |
	|      |                      |       | equal to               |      |
	|      |                      |       | DMAX_M_DATA_WIDTH.     |      |
	+------+----------------------+-------+------------------------+------+
	| 13:11| DST_TR_WIDTH         | R/W   | Destination Transfer   | 0x0  |
	|      |                      |       | Width.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Mapped to AXI bus      |      |
	|      |                      |       | awsize, this value     |      |
	|      |                      |       | must be less than or   |      |
	|      |                      |       | equal to               |      |
	|      |                      |       | DMAX_M_DATA_WIDTH.     |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_ctl_2:
.. table:: CHx_CTL, Offset Address: 0x118 (continued)
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 17:14| SRC_MSIZE            | R/W   | Source Burst           | 0x0  |
	|      |                      |       | Transaction Length.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Number of data items,  |      |
	|      |                      |       | each of width          |      |
	|      |                      |       |                        |      |
	|      |                      |       | CHx_CTL.SRC_TR_WIDTH,  |      |
	|      |                      |       | to be read from the    |      |
	|      |                      |       | source                 |      |
	|      |                      |       | every time a source    |      |
	|      |                      |       | burst transaction      |      |
	|      |                      |       | request is made from   |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | hardware or software   |      |
	|      |                      |       | handshaking            |      |
	|      |                      |       | interface. The maximum |      |
	|      |                      |       | value of DST_MSIZE is  |      |
	|      |                      |       | limited by             |      |
	|      |                      |       | D\                     |      |
	|      |                      |       | MAX_CHx_MAX_MULT_SIZE. |      |
	+------+----------------------+-------+------------------------+------+
	| 21:18| DST_MSIZE            | R/W   | Destination Burst      | 0x0  |
	|      |                      |       | Transaction Length.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Number of data items,  |      |
	|      |                      |       | each of width          |      |
	|      |                      |       | CHx_CTL.DST_TR_WIDTH,  |      |
	|      |                      |       | to be written to the   |      |
	|      |                      |       | destination            |      |
	|      |                      |       | every time a           |      |
	|      |                      |       | destination burst      |      |
	|      |                      |       | transaction request is |      |
	|      |                      |       | made                   |      |
	|      |                      |       | from the corresponding |      |
	|      |                      |       | hardware or software   |      |
	|      |                      |       | handshaking            |      |
	|      |                      |       | interface.Note: This   |      |
	|      |                      |       | Value is not related   |      |
	|      |                      |       | to the AXI awlen       |      |
	|      |                      |       | signal.                |      |
	+------+----------------------+-------+------------------------+------+
	| 25:22| AR_CACHE             | R/W   | AXI 'ar_cache' signal  | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 29:26| AW_CACHE             | R/W   | AXI 'aw_cache' signal  | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 30   | No                   | R/W   | Non Posted Last Write  | 0x0  |
	|      | nPosted_LastWrite_En |       | Enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit decides       |      |
	|      |                      |       | whether posted writes  |      |
	|      |                      |       | can be used            |      |
	|      |                      |       | throughout the block   |      |
	|      |                      |       | transfer.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Posted writes may |      |
	|      |                      |       |   be used throughout   |      |
	|      |                      |       |   the block            |      |
	|      |                      |       |   transfer.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Posted writes may |      |
	|      |                      |       |   be used till the end |      |
	|      |                      |       |   of the block (inside |      |
	|      |                      |       |   a block) and the     |      |
	|      |                      |       |   last write in the    |      |
	|      |                      |       |   block must be        |      |
	|      |                      |       |   non-posted. This is  |      |
	|      |                      |       |   to synchronize block |      |
	|      |                      |       |   completion           |      |
	|      |                      |       |   interrupt generation |      |
	|      |                      |       |   to the last write    |      |
	|      |                      |       |   data reaching the end|      |
	|      |                      |       |   memory/peripheral.   |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 34:32| AR_PROT              | R/W   | AXI 'ar_prot' signal   | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 37:35| AW_PROT              | R/W   | AXI 'aw_prot' signal   | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 38   | ARLEN_EN             | R/W   | Source Burst Length    | 0x0  |
	|      |                      |       | Enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | If this bit is set to  |      |
	|      |                      |       | 1, DW_axi_dmac uses    |      |
	|      |                      |       | the value of           |      |
	|      |                      |       | CHx_CTL.ARLEN as AXI   |      |
	|      |                      |       | Burst length for       |      |
	|      |                      |       | source data            |      |
	|      |                      |       | transfer till the      |      |
	|      |                      |       | extent possible;       |      |
	|      |                      |       | remaining transfers    |      |
	|      |                      |       | use                    |      |
	|      |                      |       | maximum possible burst |      |
	|      |                      |       | length.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | If this bit is set to  |      |
	|      |                      |       | 0, DW_axi_dmac uses    |      |
	|      |                      |       | any possible value     |      |
	|      |                      |       | that is less than or   |      |
	|      |                      |       | equal to               |      |
	|      |                      |       | DMAX_CHx\              |      |
	|      |                      |       | _MAX_AMBA_BURST_LENGTH |      |
	|      |                      |       | as AXI Burst           |      |
	|      |                      |       | length for source data |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+
	
To be continued ......

.. _table_chx_ctl_3:
.. table:: CHx_CTL, Offset Address: 0x118 (continued)
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+	
	| 46:39| ARLEN                | R/W   | Source Burst Length    | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | AXI Burst length used  |      |
	|      |                      |       | for source data        |      |
	|      |                      |       | transfer. The          |      |
	|      |                      |       | specified              |      |
	|      |                      |       | burst length is used   |      |
	|      |                      |       | for source data        |      |
	|      |                      |       | transfer till the      |      |
	|      |                      |       | extent                 |      |
	|      |                      |       | possible; remaining    |      |
	|      |                      |       | transfers use maximum  |      |
	|      |                      |       | possible value         |      |
	|      |                      |       | that is less than or   |      |
	|      |                      |       | equal to               |      |
	|      |                      |       | DMAX_CHx\_             |      |
	|      |                      |       | MAX_AMBA_BURST_LENGTH. |      |
	|      |                      |       |                        |      |
	|      |                      |       | The maximum value of   |      |
	|      |                      |       | ARLEN is limited by    |      |
	|      |                      |       | DMAX_CHx\              |      |
	|      |                      |       | _MAX_AMBA_BURST_LENGTH |      |
	+------+----------------------+-------+------------------------+------+
	| 47   | AWLEN_EN             | R/W   | Destination Burst      | 0x0  |
	|      |                      |       | Length Enable          |      |
	|      |                      |       |                        |      |
	|      |                      |       | If this bit is set to  |      |
	|      |                      |       | 1, DW_axi_dmac uses    |      |
	|      |                      |       | the value of           |      |
	|      |                      |       | CHx_CTL.AWLEN as AXI   |      |
	|      |                      |       | Burst length for       |      |
	|      |                      |       | destination data       |      |
	|      |                      |       | transfer till the      |      |
	|      |                      |       | extent possible;       |      |
	|      |                      |       | remaining transfers    |      |
	|      |                      |       | use                    |      |
	|      |                      |       | maximum possible burst |      |
	|      |                      |       | length.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | If this bit is set to  |      |
	|      |                      |       | 0, DW_axi_dmac uses    |      |
	|      |                      |       | any possible value     |      |
	|      |                      |       | which is less than or  |      |
	|      |                      |       | equal to               |      |
	|      |                      |       | DMAX_CHx\              |      |
	|      |                      |       | _MAX_AMBA_BURST_LENGTH |      |
	|      |                      |       | as AXI Burst           |      |
	|      |                      |       | length for destination |      |
	|      |                      |       | data transfer.         |      |
	+------+----------------------+-------+------------------------+------+
	| 55:48| AWLEN                | RO    | Destination Burst      |      |
	|      |                      |       | Length                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | AXI Burst length used  |      |
	|      |                      |       | for destination data   |      |
	|      |                      |       | transfer. The          |      |
	|      |                      |       | specified burst length |      |
	|      |                      |       | is used for            |      |
	|      |                      |       | destination data       |      |
	|      |                      |       | transfer till          |      |
	|      |                      |       | the extent possible;   |      |
	|      |                      |       | remaining transfers    |      |
	|      |                      |       | use maximum            |      |
	|      |                      |       | possible value that is |      |
	|      |                      |       | less than or equal to  |      |
	|      |                      |       | DMAX_CHx\_\            |      |
	|      |                      |       | MAX_AMBA_BURST_LENGTH. |      |
	|      |                      |       |                        |      |
	|      |                      |       | The maximum value of   |      |
	|      |                      |       | AWLEN is limited by    |      |
	|      |                      |       | DMAX_CHx\_\            |      |
	|      |                      |       | MAX_AMBA_BURST_LENGTH. |      |
	+------+----------------------+-------+------------------------+------+
	| 56   | SRC_STAT_EN          | R/W   | Source Status Enable   | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Enable the logic to    |      |
	|      |                      |       | fetch status from      |      |
	|      |                      |       | source peripheral of   |      |
	|      |                      |       | channel x pointed to   |      |
	|      |                      |       | by the content of      |      |
	|      |                      |       | CHx_SSTATAR            |      |
	|      |                      |       | register and stores it |      |
	|      |                      |       | in CHx_SSTAT register. |      |
	|      |                      |       | This value is          |      |
	|      |                      |       | written back to the    |      |
	|      |                      |       | CHx_SSTAT location of  |      |
	|      |                      |       | linked list at end     |      |
	|      |                      |       | of each block transfer |      |
	|      |                      |       | if DMAX_CHx_LLI_WB_EN  |      |
	|      |                      |       | is set to 1            |      |
	|      |                      |       | and if linked list     |      |
	|      |                      |       | based multi-block      |      |
	|      |                      |       | transfer is used by    |      |
	|      |                      |       | either                 |      |
	|      |                      |       | source or destination  |      |
	|      |                      |       | peripheral.            |      |
	+------+----------------------+-------+------------------------+------+
	
To be continued ......

.. _table_chx_ctl_4:
.. table:: CHx_CTL, Offset Address: 0x118 (continued)
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 57   | DST_STAT_EN          | R/W   | Destination Status     | 0x0  |
	|      |                      |       | Enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Enable the logic to    |      |
	|      |                      |       | fetch status from      |      |
	|      |                      |       | destination peripheral |      |
	|      |                      |       | of                     |      |
	|      |                      |       | channel x pointed to   |      |
	|      |                      |       | by the content of      |      |
	|      |                      |       | CHx_DSTATAR            |      |
	|      |                      |       | register and stores it |      |
	|      |                      |       | in CHx_DSTAT register. |      |
	|      |                      |       | This value is          |      |
	|      |                      |       | written back to the    |      |
	|      |                      |       | CHx_DSTAT location of  |      |
	|      |                      |       | linked list at end     |      |
	|      |                      |       | of each block transfer |      |
	|      |                      |       | if DMAX_CHx_LLI_WB_EN  |      |
	|      |                      |       | is set to 1            |      |
	|      |                      |       | and if linked list     |      |
	|      |                      |       | based multi-block      |      |
	|      |                      |       | transfer is used by    |      |
	|      |                      |       | either                 |      |
	|      |                      |       | source or destination  |      |
	|      |                      |       | peripheral.            |      |
	+------+----------------------+-------+------------------------+------+
	| 58   | IOC_BlkTfr           | R/W   | Interrupt On           | 0x0  |
	|      |                      |       | completion of Block    |      |
	|      |                      |       | Transfer               |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | control the block      |      |
	|      |                      |       | transfer completion    |      |
	|      |                      |       | interrupt generation   |      |
	|      |                      |       | on a block by block    |      |
	|      |                      |       | basis for shadow       |      |
	|      |                      |       | register or linked     |      |
	|      |                      |       | list based multi-block |      |
	|      |                      |       | transfers. Writing 1   |      |
	|      |                      |       | to                     |      |
	|      |                      |       | this register field    |      |
	|      |                      |       | enables                |      |
	|      |                      |       | CHx_IntStatusReg.      |      |
	|      |                      |       | BLOCK_TFR_DONE_IntStat |      |
	|      |                      |       | field if this          |      |
	|      |                      |       | interrupt generation   |      |
	|      |                      |       | is enabled in          |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | Hx_IntStatus_EnableReg |      |
	|      |                      |       | register and the       |      |
	|      |                      |       | external interrupt     |      |
	|      |                      |       | output is is asserted  |      |
	|      |                      |       | if this                |      |
	|      |                      |       | interrupt generation   |      |
	|      |                      |       | is enabled in          |      |
	|      |                      |       | C\                     |      |
	|      |                      |       | Hx_IntSignal_EnableReg |      |
	|      |                      |       | register.              |      |
	+------+----------------------+-------+------------------------+------+
	| 61:59| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 62   | S\                   | R/W   | Last Shadow            | 0x0  |
	|      | HADOWREG_OR_LLI_LAST |       | Register/Linked List   |      |
	|      |                      |       | Item.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Indicates whether      |      |
	|      |                      |       | shadow register        |      |
	|      |                      |       | content or the linked  |      |
	|      |                      |       | list                   |      |
	|      |                      |       | item fetched from the  |      |
	|      |                      |       | memory is the last one |      |
	|      |                      |       | or not.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Not last Shadow   |      |
	|      |                      |       |   Register/LLI         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Last Shadow       |      |
	|      |                      |       |   Register/LLI         |      |
	+------+----------------------+-------+------------------------+------+
	| 63   | SH\                  | R/W   | Shadow Register        | 0x0  |
	|      | ADOWREG_OR_LLI_VALID |       | content/Linked List    |      |
	|      |                      |       | Item valid.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Indicates whether the  |      |
	|      |                      |       | content of shadow      |      |
	|      |                      |       | register or the        |      |
	|      |                      |       | linked list item       |      |
	|      |                      |       | fetched from the       |      |
	|      |                      |       | memory is valid.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Shadow Register   |      |
	|      |                      |       |   content/LLI is       |      |
	|      |                      |       |   invalid.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Last Shadow       |      |
	|      |                      |       |   Register/LLI is      |      |
	|      |                      |       |   valid.               |      |
	+------+----------------------+-------+------------------------+------+

CHx_CFG
~~~~~~~

.. _table_chx_cfg:
.. table:: CHx_CFG, Offset Address: 0x120
	:widths: 1 3 1 6 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 1:0  | SRC_MULTBLK_TYPE     | RO    | Source Multi Block     |      |
	|      |                      |       | Transfer Type.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | These bits define the  |      |
	|      |                      |       | type of multi-block    |      |
	|      |                      |       | transfer used for      |      |
	|      |                      |       | source peripheral.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 00: Contiguous       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 01: Reload           |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 10: Shadow Register  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 11: Linked List      |      |
	|      |                      |       |                        |      |
	|      |                      |       | If the type selected   |      |
	|      |                      |       | is Contiguous, the     |      |
	|      |                      |       | CHx_SAR register is    |      |
	|      |                      |       | loaded with the value  |      |
	|      |                      |       | of the end source      |      |
	|      |                      |       | address of previous    |      |
	|      |                      |       | block + 1 at the end   |      |
	|      |                      |       | of every block for     |      |
	|      |                      |       | multi-block transfers. |      |
	|      |                      |       | A new block transfer is|      |
	|      |                      |       | then initiated.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | If the type selected   |      |
	|      |                      |       | is Reload, the CHx_SAR |      |
	|      |                      |       | register is            |      |
	|      |                      |       | reloaded from the      |      |
	|      |                      |       | initial value of SAR   |      |
	|      |                      |       | at the end of every    |      |
	|      |                      |       | block for multi-block  |      |
	|      |                      |       | transfers. A new block |      |
	|      |                      |       | transfer is then       |      |
	|      |                      |       | initiated.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | If the type selected   |      |
	|      |                      |       | is Shadow Register,    |      |
	|      |                      |       | the CHx_SAR            |      |
	|      |                      |       | register is loaded     |      |
	|      |                      |       | from the content of    |      |
	|      |                      |       | its shadow register if |      |
	|      |                      |       | CHx_CTL.               |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is set to 1 at the |      |
	|      |                      |       | end of every block for |      |
	|      |                      |       | multi-block transfers. |      |
	|      |                      |       | A new block            |      |
	|      |                      |       | transfer is then       |      |
	|      |                      |       | initiated.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | If the type selected   |      |
	|      |                      |       | is Linked List, the    |      |
	|      |                      |       | CHx_SAR register is    |      |
	|      |                      |       | loaded from the Linked |      |
	|      |                      |       | List if                |      |
	|      |                      |       | CTL.                   |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is set to 1 at the |      |
	|      |                      |       | end of                 |      |
	|      |                      |       | every block for        |      |
	|      |                      |       | multi-block transfers. |      |
	|      |                      |       | A new block transfer   |      |
	|      |                      |       | is                     |      |
	|      |                      |       | then initiated.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | CHx_CTL and            |      |
	|      |                      |       | CHx_BLOCK_TS registers |      |
	|      |                      |       | are loaded from        |      |
	|      |                      |       | their initial values   |      |
	|      |                      |       | or from the contents   |      |
	|      |                      |       | of their shadow        |      |
	|      |                      |       | registers (if          |      |
	|      |                      |       | CHx_CTL.               |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is set to          |      |
	|      |                      |       | 1) or from the linked  |      |
	|      |                      |       | list (if               |      |
	|      |                      |       | CTL.                   |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is set to 1) at    |      |
	|      |                      |       | the end of every block |      |
	|      |                      |       | for multi-block        |      |
	|      |                      |       | transfers based on the |      |
	|      |                      |       | multi-block transfer   |      |
	|      |                      |       | type programmed        |      |
	|      |                      |       | for source and         |      |
	|      |                      |       | destination            |      |
	|      |                      |       | peripherals.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Contiguous transfer on |      |
	|      |                      |       | both source and        |      |
	|      |                      |       | destination            |      |
	|      |                      |       | peripheral is not a    |      |
	|      |                      |       | valid multi-block      |      |
	|      |                      |       | transfer               |      |
	|      |                      |       | configuration.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | This field does not    |      |
	|      |                      |       | exist if the           |      |
	|      |                      |       | configuration          |      |
	|      |                      |       | parameter              |      |
	|      |                      |       | DMAX_CHx_MULTI_BLK_EN  |      |
	|      |                      |       | is not selected; in    |      |
	|      |                      |       | that case,             |      |
	|      |                      |       | the read-back value is |      |
	|      |                      |       | always 0.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Values:                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x0 (CONTINGUOUS):   |      |
	|      |                      |       |   Contiguous Multiblock|      |
	|      |                      |       |   Type used            |      |
	|      |                      |       |   for Source Transfer  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x1 (RELOAD): Reload |      |
	|      |                      |       |   Multiblock Type used |      |
	|      |                      |       |   for Source Transfer  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x2                  |      |
	|      |                      |       |   (SHADOW_REGISTER):   |      |
	|      |                      |       |   Shadow Register based|      |
	|      |                      |       |   Multiblock Type used |      |
	|      |                      |       |   for Source Transfer  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x3 (LINKED_LIST):   |      |
	|      |                      |       |   Linked List based    |      |
	|      |                      |       |   Multiblock Type      |      |
	|      |                      |       |   used for Source      |      |
	|      |                      |       |   Transfer             |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_cfg_2:
.. table:: CHx_CFG, Offset Address: 0x120 (continued)
	:widths: 1 3 1 6 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:2  | DST_MULTBLK_TYPE     | R/W   | Destination Multi      | 0x0  |
	|      |                      |       | Block Transfer Type.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | These bits define the  |      |
	|      |                      |       | type of multi-block    |      |
	|      |                      |       | transfer used for      |      |
	|      |                      |       | destination peripheral.|      |
	|      |                      |       |                        |      |
	|      |                      |       | - 00: Contiguous       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 01: Reload           |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 10: Shadow Register  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 11: Linked List      |      |
	|      |                      |       |                        |      |
	|      |                      |       | If the type selected   |      |
	|      |                      |       | is Contiguous, the     |      |
	|      |                      |       | CHx_DAR register is    |      |
	|      |                      |       | loaded with the value  |      |
	|      |                      |       | of the end source      |      |
	|      |                      |       | address of previous    |      |
	|      |                      |       | block + 1 at the end   |      |
	|      |                      |       | of every block for     |      |
	|      |                      |       | multi-block transfers. |      |
	|      |                      |       | A new block transfer is|      |
	|      |                      |       | then initiated.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | If the type selected   |      |
	|      |                      |       | is Reload, the CHx_DAR |      |
	|      |                      |       | register is            |      |
	|      |                      |       | reloaded from the      |      |
	|      |                      |       | initial value of DAR   |      |
	|      |                      |       | at the end of every    |      |
	|      |                      |       | block for multi-block  |      |
	|      |                      |       | transfers. A new block |      |
	|      |                      |       | transfer is then       |      |
	|      |                      |       | initiated.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | If the type selected   |      |
	|      |                      |       | is Shadow Register,    |      |
	|      |                      |       | the CHx_DAR            |      |
	|      |                      |       | register is loaded     |      |
	|      |                      |       | from the content of    |      |
	|      |                      |       | its shadow register if |      |
	|      |                      |       | CHx_CTL.               |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is set to 1 at the |      |
	|      |                      |       | end of every block for |      |
	|      |                      |       | multi-block transfers. |      |
	|      |                      |       | A new block            |      |
	|      |                      |       | transfer is then       |      |
	|      |                      |       | initiated.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | If the type selected   |      |
	|      |                      |       | is Linked List, the    |      |
	|      |                      |       | CHx_DAR register is    |      |
	|      |                      |       | loaded from the Linked |      |
	|      |                      |       | List if                |      |
	|      |                      |       | CTL.                   |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is set to 1 at the |      |
	|      |                      |       | end of                 |      |
	|      |                      |       | every block for        |      |
	|      |                      |       | multi-block transfers. |      |
	|      |                      |       | A new block transfer   |      |
	|      |                      |       | is then initiated.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | CHx_CTL and            |      |
	|      |                      |       | CHx_BLOCK_TS registers |      |
	|      |                      |       | are loaded from        |      |
	|      |                      |       | their initial values   |      |
	|      |                      |       | or from the contents   |      |
	|      |                      |       | of their shadow        |      |
	|      |                      |       | registers (if          |      |
	|      |                      |       | CHx_CTL.               |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is set to          |      |
	|      |                      |       | 1) or from the linked  |      |
	|      |                      |       | list (if               |      |
	|      |                      |       | CTL.                   |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is set to 1) at    |      |
	|      |                      |       | the end of every block |      |
	|      |                      |       | for multi-block        |      |
	|      |                      |       | transfers based on the |      |
	|      |                      |       | multi-block transfer   |      |
	|      |                      |       | type programmed        |      |
	|      |                      |       | for source and         |      |
	|      |                      |       | destination            |      |
	|      |                      |       | peripherals.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Contiguous transfer on |      |
	|      |                      |       | both source and        |      |
	|      |                      |       | destination            |      |
	|      |                      |       | peripheral is not a    |      |
	|      |                      |       | valid multi-block      |      |
	|      |                      |       | transfer               |      |
	|      |                      |       | configuration.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | This field does not    |      |
	|      |                      |       | exist if the           |      |
	|      |                      |       | configuration          |      |
	|      |                      |       | parameter              |      |
	|      |                      |       | DMAX_CHx_MULTI_BLK_EN  |      |
	|      |                      |       | is not selected; in    |      |
	|      |                      |       | that case,             |      |
	|      |                      |       | the read-back value is |      |
	|      |                      |       | always 0.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Values:                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x0 (CONTINGUOUS):   |      |
	|      |                      |       |   Contiguous Multiblock|      |
	|      |                      |       |   Type used            |      |
	|      |                      |       |   for Destination      |      |
	|      |                      |       |   Transfer             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x1 (RELOAD): Reload |      |
	|      |                      |       |   Multiblock Type used |      |
	|      |                      |       |   for                  |      |
	|      |                      |       |   Destination Transfer |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x2                  |      |
	|      |                      |       |   (SHADOW_REGISTER):   |      |
	|      |                      |       |   Shadow Register based|      |
	|      |                      |       |   Multiblock Type used |      |
	|      |                      |       |   for Destination      |      |
	|      |                      |       |   Transfer             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x3 (LINKED_LIST):   |      |
	|      |                      |       |   Linked List based    |      |
	|      |                      |       |   Multiblock Type      |      |
	|      |                      |       |   used for Destination |      |
	|      |                      |       |   Transfer             |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_cfg_3:
.. table:: CHx_CFG, Offset Address: 0x120 (continued)
	:widths: 1 2 1 6 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 34:32| TT_FC                | R/W   | Transfer Type and Flow | 0x0  |
	|      |                      |       | Control.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | The following transfer |      |
	|      |                      |       | types are supported.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Memory to Memory       |      |
	|      |                      |       |                        |      |
	|      |                      |       | Memory to Peripheral   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Peripheral to Memory   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Peripheral to          |      |
	|      |                      |       | Peripheral             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Flow Control can be    |      |
	|      |                      |       | assigned to the        |      |
	|      |                      |       | DW_axi_dmac, the       |      |
	|      |                      |       | source peripheral, or  |      |
	|      |                      |       | hte destination        |      |
	|      |                      |       | peripheral.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | Values:                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x0                  |      |
	|      |                      |       |   (MEM_TO_MEM_DMAC):   |      |
	|      |                      |       |   Transfer Type is     |      |
	|      |                      |       |   memory               |      |
	|      |                      |       |   to memory and Flow   |      |
	|      |                      |       |   Controller is        |      |
	|      |                      |       |   DW_axi_dmac          |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x1                  |      |
	|      |                      |       |   (MEM_TO_PER_DMAC):   |      |
	|      |                      |       |   Transfer Type is     |      |
	|      |                      |       |   memory to            |      |
	|      |                      |       |   peripheral and Flow  |      |
	|      |                      |       |   Controller is        |      |
	|      |                      |       |   DW_axi_dmac          |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x2                  |      |
	|      |                      |       |   (PER_TO_MEM_DMAC):   |      |
	|      |                      |       |   Transfer Type is     |      |
	|      |                      |       |   peripheral           |      |
	|      |                      |       |   to memory and Flow   |      |
	|      |                      |       |   Controller is        |      |
	|      |                      |       |   DW_axi_dmac          |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x3                  |      |
	|      |                      |       |   (PER_TO_PER_DMAC):   |      |
	|      |                      |       |   Transfer Type is     |      |
	|      |                      |       |   peripheral           |      |
	|      |                      |       |   to peripheral and    |      |
	|      |                      |       |   Flow Controller is   |      |
	|      |                      |       |   DW_axi_dmac          |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x4                  |      |
	|      |                      |       |   (PER_TO_MEM_SRC):    |      |
	|      |                      |       |   Transfer Type is     |      |
	|      |                      |       |   peripheral to        |      |
	|      |                      |       |   Memory and Flow      |      |
	|      |                      |       |   Controller is Source |      |
	|      |                      |       |   peripheral           |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x5                  |      |
	|      |                      |       |   (PER_TO_PER_SRC):    |      |
	|      |                      |       |   Transfer Type is     |      |
	|      |                      |       |   peripheral to        |      |
	|      |                      |       |   peripheral and Flow  |      |
	|      |                      |       |   Controller is Source |      |
	|      |                      |       |   peripheral           |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x6                  |      |
	|      |                      |       |   (MEM_TO_PER_DST):    |      |
	|      |                      |       |   Transfer Type is     |      |
	|      |                      |       |   memory to            |      |
	|      |                      |       |   peripheral and Flow  |      |
	|      |                      |       |   Controller is        |      |
	|      |                      |       |   Destination          |      |
	|      |                      |       |   peripheral           |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x7                  |      |
	|      |                      |       |   (PER_TO_PER_DST):    |      |
	|      |                      |       |   Transfer Type is     |      |
	|      |                      |       |   peripheral to        |      |
	|      |                      |       |   peripheral and Flow  |      |
	|      |                      |       |   Controller is        |      |
	|      |                      |       |   Destination          |      |
	|      |                      |       |   peripheral           |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_cfg_4:
.. table:: CHx_CFG, Offset Address: 0x120 (continued)
	:widths: 1 2 1 6 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 35   | HS_SEL_SRC           | R/W   | Source Software or     | 0x0  |
	|      |                      |       | Hardware Handshaking   |      |
	|      |                      |       | Select.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register selects  |      |
	|      |                      |       | which of the           |      |
	|      |                      |       | handshaking interfaces |      |
	|      |                      |       | (hardware or software) |      |
	|      |                      |       | is active for source   |      |
	|      |                      |       | requests on this       |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Hardware          |      |
	|      |                      |       |   handshaking          |      |
	|      |                      |       |   interface.           |      |
	|      |                      |       |   Software-initiated   |      |
	|      |                      |       |   transaction requests |      |
	|      |                      |       |   are ignored.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Software          |      |
	|      |                      |       |   handshaking          |      |
	|      |                      |       |   interface.           |      |
	|      |                      |       |   Hardware-initiated   |      |
	|      |                      |       |   transaction requests |      |
	|      |                      |       |   are ignored.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | If the source          |      |
	|      |                      |       | peripheral is memory,  |      |
	|      |                      |       | then this bit is       |      |
	|      |                      |       | ignored.               |      |
	+------+----------------------+-------+------------------------+------+
	| 36   | HS_SEL_DST           | R/W   | Destination Software   | 0x0  |
	|      |                      |       | or Hardware            |      |
	|      |                      |       | Handshaking Select.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register selects  |      |
	|      |                      |       | which of the           |      |
	|      |                      |       | handshaking interfaces |      |
	|      |                      |       | (hardware or software) |      |
	|      |                      |       | is active for          |      |
	|      |                      |       | destination requests   |      |
	|      |                      |       | on this channel.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Hardware          |      |
	|      |                      |       |   handshaking          |      |
	|      |                      |       |   interface.           |      |
	|      |                      |       |   Software-initiated   |      |
	|      |                      |       |   transaction requests |      |
	|      |                      |       |   are ignored.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Software          |      |
	|      |                      |       |   handshaking          |      |
	|      |                      |       |   interface.           |      |
	|      |                      |       |   Hardware-initiated   |      |
	|      |                      |       |   transaction requests |      |
	|      |                      |       |   are ignored.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | If the destination     |      |
	|      |                      |       | peripheral is memory,  |      |
	|      |                      |       | then this bit is       |      |
	|      |                      |       | ignored.               |      |
	+------+----------------------+-------+------------------------+------+
	| 37   | SRC_HWHS_POL         | RO    | Source Hardware        |      |
	|      |                      |       | Handshaking Interface  |      |
	|      |                      |       | Polarity.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: ACTIVE HIGH       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: ACTIVE LOW        |      |
	+------+----------------------+-------+------------------------+------+
	| 38   | DST_HWHS_POL         | RO    | Destination Hardware   |      |
	|      |                      |       | Handshaking Interface  |      |
	|      |                      |       | Polarity.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: ACTIVE HIGH       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: ACTIVE LOW        |      |
	+------+----------------------+-------+------------------------+------+
	| 39   | SRC_PER              | R/W   | Assigns a hardware     | 0x0  |
	|      |                      |       | handshaking interface  |      |
	|      |                      |       | (0 -                   |      |
	|      |                      |       | DMAX_NUM_HS_IF-1) to   |      |
	|      |                      |       | the source of Channelx |      |
	|      |                      |       | if the                 |      |
	|      |                      |       | CHx_CFG.HS_SEL_SRC     |      |
	|      |                      |       | field is 0; otherwise, |      |
	|      |                      |       | this field is          |      |
	|      |                      |       | ignored. The channel   |      |
	|      |                      |       | can then communicate   |      |
	|      |                      |       | with the source        |      |
	|      |                      |       | peripheral connected   |      |
	|      |                      |       | to that interface      |      |
	|      |                      |       | through the assigned   |      |
	|      |                      |       | hardware handshaking   |      |
	|      |                      |       | interface.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Reset Value = 1        |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: For correct      |      |
	|      |                      |       | DW_axi_dmac operation, |      |
	|      |                      |       | only one               |      |
	|      |                      |       | peripheral (source or  |      |
	|      |                      |       | destination) should be |      |
	|      |                      |       | assigned to the        |      |
	|      |                      |       | same handshaking       |      |
	|      |                      |       | interface.             |      |
	+------+----------------------+-------+------------------------+------+
	| 43:40| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 44   | DST_PER              | R/W   | Assigns a hardware     | 0x0  |
	|      |                      |       | handshaking interface  |      |
	|      |                      |       | (0 -                   |      |
	|      |                      |       | DMAX_NUM_HS_IF-1) to   |      |
	|      |                      |       | the destination of     |      |
	|      |                      |       | Channelx if the        |      |
	|      |                      |       | CHx_CFG.HS_SEL_DST     |      |
	|      |                      |       | field is 0; otherwise, |      |
	|      |                      |       | this field is          |      |
	|      |                      |       | ignored. The channel   |      |
	|      |                      |       | can then communicate   |      |
	|      |                      |       | with the               |      |
	|      |                      |       | destination peripheral |      |
	|      |                      |       | connected to that      |      |
	|      |                      |       | interface through the  |      |
	|      |                      |       | assigned hardware      |      |
	|      |                      |       | handshaking interface. |      |
	|      |                      |       |                        |      |
	|      |                      |       | Reset Value = 1        |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: For correct      |      |
	|      |                      |       | DW_axi_dmac operation, |      |
	|      |                      |       | only one               |      |
	|      |                      |       | peripheral (source or  |      |
	|      |                      |       | destination) should be |      |
	|      |                      |       | assigned to the        |      |
	|      |                      |       | same handshaking       |      |
	|      |                      |       | interface.             |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_cfg_5:
.. table:: CHx_CFG, Offset Address: 0x120 (continued)
	:widths: 1 2 1 6 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 48:45| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 51:49| CH_PRIOR             | R/W   | Channel Priority       | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | A priority of 7 is the |      |
	|      |                      |       | highest priority, and  |      |
	|      |                      |       | 0 is the lowest. This  |      |
	|      |                      |       | field must be          |      |
	|      |                      |       | programmed within the  |      |
	|      |                      |       | following range:       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: DMAX_NUM_CHANNELS-1 |      |
	|      |                      |       |                        |      |
	|      |                      |       | A programmed value     |      |
	|      |                      |       | outside this range     |      |
	|      |                      |       | will cause erroneous   |      |
	|      |                      |       | behavior.              |      |
	+------+----------------------+-------+------------------------+------+
	| 52   | LOCK_CH              | R/W   | Channel Lock bit       | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | When the channel is    |      |
	|      |                      |       | granted control of the |      |
	|      |                      |       | master bus             |      |
	|      |                      |       | interface and if the   |      |
	|      |                      |       | CHx_CFG.LOCK_CH bit is |      |
	|      |                      |       | asserted,              |      |
	|      |                      |       | then no other channels |      |
	|      |                      |       | are granted control of |      |
	|      |                      |       | the master bus         |      |
	|      |                      |       | interface for the      |      |
	|      |                      |       | duration specified in  |      |
	|      |                      |       |                        |      |
	|      |                      |       | CHx_CFG.LOCK_CH_L.     |      |
	|      |                      |       | Indicates to the       |      |
	|      |                      |       | master bus             |      |
	|      |                      |       | interface arbiter that |      |
	|      |                      |       | this channel wants     |      |
	|      |                      |       | exclusive access to    |      |
	|      |                      |       | the master bus         |      |
	|      |                      |       | interface for the      |      |
	|      |                      |       | duration specified in  |      |
	|      |                      |       | CHx_CFG.LOCK_CH_L.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | This field does not    |      |
	|      |                      |       | exist if the           |      |
	|      |                      |       | configuration          |      |
	|      |                      |       | parameter              |      |
	|      |                      |       | DMAX_CHx_LOCK_EN is    |      |
	|      |                      |       | set to False; in this  |      |
	|      |                      |       | case, the              |      |
	|      |                      |       | read-back value is     |      |
	|      |                      |       | always 0.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Locking the channel    |      |
	|      |                      |       | locks AXI Read         |      |
	|      |                      |       | Address, Write Address |      |
	|      |                      |       | and Write Data         |      |
	|      |                      |       | channels on the        |      |
	|      |                      |       | corresponding master   |      |
	|      |                      |       | interface.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note: Channel locking  |      |
	|      |                      |       | feature is supported   |      |
	|      |                      |       | only for memoryto-     |      |
	|      |                      |       | memory transfer at     |      |
	|      |                      |       | Block Transfer and DMA |      |
	|      |                      |       | Transfer               |      |
	|      |                      |       | levels. Hardware does  |      |
	|      |                      |       | not check for the      |      |
	|      |                      |       | validity of channel    |      |
	|      |                      |       | locking setting, hence |      |
	|      |                      |       | the software must take |      |
	|      |                      |       | care of                |      |
	|      |                      |       | enabling the channel   |      |
	|      |                      |       | locking only for       |      |
	|      |                      |       | memory-to-memory       |      |
	|      |                      |       | transfers at Block     |      |
	|      |                      |       | Transfer or DMA        |      |
	|      |                      |       | Transfer levels.       |      |
	|      |                      |       | Illegal                |      |
	|      |                      |       | programming of channel |      |
	|      |                      |       | locking might result   |      |
	|      |                      |       | in unpredictable       |      |
	|      |                      |       | behavior.              |      |
	+------+----------------------+-------+------------------------+------+
	| 54:53| LOCK_CH_L            | R/W   | Channel Lock Level     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | This bit indicates the |      |
	|      |                      |       | duration over which    |      |
	|      |                      |       | CHx_CFG.LOCK_CH bit    |      |
	|      |                      |       | applies.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 00: Over complete    |      |
	|      |                      |       |   DMA transfer         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 01: Over DMA block   |      |
	|      |                      |       |   transfer             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1x: Reserved         |      |
	|      |                      |       |                        |      |
	|      |                      |       | This field does not    |      |
	|      |                      |       | exist if the           |      |
	|      |                      |       | configuration          |      |
	|      |                      |       | parameter              |      |
	|      |                      |       | DMAX_CHx_LOCK_EN is    |      |
	|      |                      |       | set to False; in that  |      |
	|      |                      |       | case, the              |      |
	|      |                      |       | read-back value is     |      |
	|      |                      |       | always 0.              |      |
	+------+----------------------+-------+------------------------+------+
	| 58:55| SRC_OSR_LMT          | R/W   | Source Outstanding     | 0x0  |
	|      |                      |       | Request Limit          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Maximum outstanding    |      |
	|      |                      |       | request supported is   |      |
	|      |                      |       | 16.                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Source Outstanding     |      |
	|      |                      |       | Request Limit =        |      |
	|      |                      |       | SRC_OSR_LMT + 1        |      |
	+------+----------------------+-------+------------------------+------+
	| 62:59| DST_OSR_LMT          | R/W   | Destination            | 0x0  |
	|      |                      |       | Outstanding Request    |      |
	|      |                      |       | Limit                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Maximum outstanding    |      |
	|      |                      |       | request supported is   |      |
	|      |                      |       | 16.                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Source Outstanding     |      |
	|      |                      |       | Request Limit =        |      |
	|      |                      |       | DST_OSR_LMT + 1        |      |
	+------+----------------------+-------+------------------------+------+
	| 63   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CHx_LLP
~~~~~~~

.. _table_chx_llp:
.. table:: CHx_LLP, Offset Address: 0x128
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | LMS                  | R/W   | LLI master Select      | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | This bit identifies    |      |
	|      |                      |       | the AXI                |      |
	|      |                      |       | layer/interface where  |      |
	|      |                      |       | the memory             |      |
	|      |                      |       | device that stores the |      |
	|      |                      |       | next linked list item  |      |
	|      |                      |       | resides.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: AXI Master 1      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: AXI Master 2      |      |
	|      |                      |       |                        |      |
	|      |                      |       | This field does not    |      |
	|      |                      |       | exist if the           |      |
	|      |                      |       | configuration          |      |
	|      |                      |       | parameter              |      |
	|      |                      |       | DMAX_CHx_LMS is not    |      |
	|      |                      |       | set to NO_HARDCODE.    |      |
	+------+----------------------+-------+------------------------+------+
	| 5:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 63:6 | LOC                  | R/W   | Starting Address       | 0x0  |
	|      |                      |       | Memory of LLI block    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Starting Address In    |      |
	|      |                      |       | Memory of next LLI if  |      |
	|      |                      |       | block chaining is      |      |
	|      |                      |       | enabled. The six LSBs  |      |
	|      |                      |       | of the starting        |      |
	|      |                      |       | address are not stored |      |
	|      |                      |       | because the address is |      |
	|      |                      |       | assumed to be aligned  |      |
	|      |                      |       | to a 64-byte           |      |
	|      |                      |       | boundary.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | LLI access always uses |      |
	|      |                      |       | the burst size         |      |
	|      |                      |       | (arsize/awsize) that   |      |
	|      |                      |       | is                     |      |
	|      |                      |       | same as the data bus   |      |
	|      |                      |       | width and cannot be    |      |
	|      |                      |       | changed or             |      |
	|      |                      |       | programmed to anything |      |
	|      |                      |       | other than this. Burst |      |
	|      |                      |       | length                 |      |
	|      |                      |       | (awlen/arlen) is       |      |
	|      |                      |       | chosen based on the    |      |
	|      |                      |       | data bus width so that |      |
	|      |                      |       | the access does not    |      |
	|      |                      |       | cross one complete LLI |      |
	|      |                      |       | structure of 64        |      |
	|      |                      |       | bytes. DW_axi_dmac     |      |
	|      |                      |       | will fetch the entire  |      |
	|      |                      |       | LLI (40 bytes) in      |      |
	|      |                      |       | one AXI burst if the   |      |
	|      |                      |       | burst length is not    |      |
	|      |                      |       | limited by other       |      |
	|      |                      |       | settings.              |      |
	+------+----------------------+-------+------------------------+------+

CHx_STATUSREG
~~~~~~~~~~~~~

.. _table_chx_statusreg:
.. table:: CHx_STATUSREG, Offset Address: 0x130
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 21:0 | CMPLTD_BLK_TFR_SIZE  | RO    | Completed Block        |      |
	|      |                      |       | Transfer Size.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit indicates the |      |
	|      |                      |       | total number of data   |      |
	|      |                      |       | of width               |      |
	|      |                      |       | CHx_CTL.SRC_TR_WIDTH   |      |
	|      |                      |       | transferred for the    |      |
	|      |                      |       | previous               |      |
	|      |                      |       | block transfer.        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:22| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 46:32| DATA_LEFT_IN_FIFO    | RO    | Data Left in FIFO.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit indicates the |      |
	|      |                      |       | total number of data   |      |
	|      |                      |       | left in                |      |
	|      |                      |       | DW_axi_dmac channel    |      |
	|      |                      |       | FIFO after completing  |      |
	|      |                      |       | the current            |      |
	|      |                      |       | block transfer.        |      |
	+------+----------------------+-------+------------------------+------+
	| 63:47| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CHx_SWHSSRCREG
~~~~~~~~~~~~~~

.. _table_chx_swhssrcreg:
.. table:: CHx_SWHSSRCREG, Offset Address: 0x138
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SWHS_REQ_SRC         | R/W   | Software Handshake     | 0x0  |
	|      |                      |       | Request for Channel    |      |
	|      |                      |       | Source.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | request dma source     |      |
	|      |                      |       | data transfer if       |      |
	|      |                      |       | software handshaking   |      |
	|      |                      |       | method is selected for |      |
	|      |                      |       | the source of          |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is ignored if |      |
	|      |                      |       | software handshaking   |      |
	|      |                      |       | is not enabled for     |      |
	|      |                      |       | the source of the      |      |
	|      |                      |       | Channelx. The          |      |
	|      |                      |       | functionality of this  |      |
	|      |                      |       | field                  |      |
	|      |                      |       | depends on whether the |      |
	|      |                      |       | peripheral is the flow |      |
	|      |                      |       | controller or          |      |
	|      |                      |       | not.                   |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | SWHS_REQ_SRC_WE      | WO    | Write Enable bit for   | 0x0  |
	|      |                      |       | Software Handshake     |      |
	|      |                      |       | Request for            |      |
	|      |                      |       | Channel Source.        |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | SWHS_SGLREQ_SRC      | R/W   | Software Handshake     | 0x0  |
	|      |                      |       | Single Request for     |      |
	|      |                      |       | Channel Source.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | request SINGLE (AXI    |      |
	|      |                      |       | burst length = 1)      |      |
	|      |                      |       | dma source data        |      |
	|      |                      |       | transfer if software   |      |
	|      |                      |       | handshaking method is  |      |
	|      |                      |       | selected for the       |      |
	|      |                      |       | source of the          |      |
	|      |                      |       | corresponding channel. |      |
	|      |                      |       | This                   |      |
	|      |                      |       | bit is ignored if      |      |
	|      |                      |       | software handshaking   |      |
	|      |                      |       | is not enabled for the |      |
	|      |                      |       | source of the          |      |
	|      |                      |       | Channelx. The          |      |
	|      |                      |       | functionality of this  |      |
	|      |                      |       | field                  |      |
	|      |                      |       | depends on whether the |      |
	|      |                      |       | peripheral is the flow |      |
	|      |                      |       | controller.            |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | SWHS_SGLREQ_SRC_WE   | WO    | Write Enable bit for   | 0x0  |
	|      |                      |       | Software Handshake     |      |
	|      |                      |       | Single Request for     |      |
	|      |                      |       | Channel Source.        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | SWHS_LST_SRC         | R/W   | Software Handshake     | 0x0  |
	|      |                      |       | Last Request for       |      |
	|      |                      |       | Channel Source.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | request LAST dma       |      |
	|      |                      |       | source data transfer   |      |
	|      |                      |       | if                     |      |
	|      |                      |       | software handshaking   |      |
	|      |                      |       | method is selected for |      |
	|      |                      |       | the source of          |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is ignored if |      |
	|      |                      |       | software handshaking   |      |
	|      |                      |       | is not enabled for     |      |
	|      |                      |       | the source of the      |      |
	|      |                      |       | Channelx or if the     |      |
	|      |                      |       | source of Channelx is  |      |
	|      |                      |       | not the flow           |      |
	|      |                      |       | controller.            |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | SWHS_LST_SRC_WE      | WO    | Write Enable bit for   | 0x0  |
	|      |                      |       | Software Handshake     |      |
	|      |                      |       | Last Request for       |      |
	|      |                      |       | Channel Source.        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CHx_SWHSDSTREG
~~~~~~~~~~~~~~

.. _table_chx_swhsdstreg:
.. table:: CHx_SWHSDSTREG, Offset Address: 0x140
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SWHS_REQ_DST         | R/W   | Software Handshake     | 0x0  |
	|      |                      |       | Request for Channel    |      |
	|      |                      |       | Destination.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | request dma            |      |
	|      |                      |       | destination data       |      |
	|      |                      |       | transfer if            |      |
	|      |                      |       | software handshaking   |      |
	|      |                      |       | method is selected for |      |
	|      |                      |       | the destination        |      |
	|      |                      |       | of the corresponding   |      |
	|      |                      |       | channel.               |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | SWHS_REQ_DST_WE      | WO    | Write Enable bit for   | 0x0  |
	|      |                      |       | Software Handshake     |      |
	|      |                      |       | Request for            |      |
	|      |                      |       | Channel Destination.   |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | SWHS_SGLREQ_DST      | R/W   | Software Handshake     | 0x0  |
	|      |                      |       | Single Request for     |      |
	|      |                      |       | Channel                |      |
	|      |                      |       | Destination.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | request SINGLE (AXI    |      |
	|      |                      |       | burst length = 1)      |      |
	|      |                      |       | dma destination data   |      |
	|      |                      |       | transfer if software   |      |
	|      |                      |       | handshaking            |      |
	|      |                      |       | method is selected for |      |
	|      |                      |       | the destination of the |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | channel.               |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | SWHS_SGLREQ_DST_WE   | WO    | Write Enable bit for   | 0x0  |
	|      |                      |       | Software Handshake     |      |
	|      |                      |       | Single Request for     |      |
	|      |                      |       | Channel Destination.   |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | SWHS_LST_DST         | R/W   | Software Handshake     | 0x0  |
	|      |                      |       | Last Request for       |      |
	|      |                      |       | Channel Destination.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | request LAST dma       |      |
	|      |                      |       | destination data       |      |
	|      |                      |       | transfer if software   |      |
	|      |                      |       | handshaking method is  |      |
	|      |                      |       | selected for the       |      |
	|      |                      |       | destination of the     |      |
	|      |                      |       | corresponding channel. |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | SWHS_LST_DST_WE      | WO    | Write Enable bit for   | 0x0  |
	|      |                      |       | Software Handshake     |      |
	|      |                      |       | Last Request for       |      |
	|      |                      |       |                        |      |
	|      |                      |       | Channel Destination.   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CHx_BLK_TFR_RESUMEREQREG
~~~~~~~~~~~~~~~~~~~~~~~~

.. _table_chx_blk_tfr_resumereqreg:
.. table:: CHx_BLK_TFR_RESUMEREQREG, Offset Address: 0x148
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | BLK_TFR_RESUMEREQ    | WO    | Block Transfer Resume  | 0x0  |
	|      |                      |       | Request during         |      |
	|      |                      |       | Linked-List or         |      |
	|      |                      |       |                        |      |
	|      |                      |       | Shadow-Register-based  |      |
	|      |                      |       | multi-block transfer.  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CHx_AXI_IDREG
~~~~~~~~~~~~~

.. _table_chx_axi_idreg:
.. table:: CHx_AXI_IDREG, Offset Address: 0x150
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 14:0 | AXI_READ_ID_SUFFIX   | R/W   | AXI Read ID Suffix     | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | These bits form part   |      |
	|      |                      |       | of the ARID output of  |      |
	|      |                      |       | AXI3/AXI4 master       |      |
	|      |                      |       | interface.             |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | AXI_WRITE_ID_SUFFIX  | R/W   | AXI Write ID Suffix.   | 0x0  |
	| 0:16 |                      |       |                        |      |
	|      |                      |       | These bits form part   |      |
	|      |                      |       | of the AWID output of  |      |
	|      |                      |       | AXI3/AXI4 master       |      |
	|      |                      |       | interface.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CHx_AXI_QOSREG
~~~~~~~~~~~~~~

.. _table_chx_axi_qosreg:
.. table:: CHx_AXI_QOSREG, Offset Address: 0x158
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | AXI_AWQOS            | R/W   | AXI AWQOS.             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | These bits form the    |      |
	|      |                      |       | awqos output of AXI4   |      |
	|      |                      |       | master interface.      |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | AXI_ARQOS            | R/W   | AXI ARQOS.             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | These bits form the    |      |
	|      |                      |       | arqos output of AXI4   |      |
	|      |                      |       | master interface.      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CHx_SSTAT
~~~~~~~~~

.. _table_chx_sstat:
.. table:: CHx_SSTAT, Offset Address: 0x160
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | SSTAT                | RO    | Source Status          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Source status          |      |
	|      |                      |       | information retrieved  |      |
	|      |                      |       | by hardware from the   |      |
	|      |                      |       | address pointed to by  |      |
	|      |                      |       | the contents of the    |      |
	|      |                      |       | CHx_SSTATAR            |      |
	|      |                      |       | register.              |      |
	+------+----------------------+-------+------------------------+------+

CHx_DSTAT
~~~~~~~~~

.. _table_chx_dstat:
.. table:: CHx_DSTAT, Offset Address: 0x168
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | DSTAT                | RO    | Destination Status     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Destination status     |      |
	|      |                      |       | information retrieved  |      |
	|      |                      |       | by hardware from       |      |
	|      |                      |       | the address pointed to |      |
	|      |                      |       | by the contents of the |      |
	|      |                      |       | CHx_DSTATAR            |      |
	|      |                      |       | register.              |      |
	+------+----------------------+-------+------------------------+------+

CHx_SSTATAR
~~~~~~~~~~~

.. _table_chx_sstatar:
.. table:: CHx_SSTATAR, Offset Address: 0x170
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 63:0 | SSTATAR              | R/W   | Source Status Fetch    | 0x0  |
	|      |                      |       | Address                |      |
	|      |                      |       |                        |      |
	|      |                      |       | Pointer from where     |      |
	|      |                      |       | hardware can fetch the |      |
	|      |                      |       | source status          |      |
	|      |                      |       | information, which is  |      |
	|      |                      |       | registered in the      |      |
	|      |                      |       | CHx_SSTAT register     |      |
	|      |                      |       | and written out to the |      |
	|      |                      |       | CHx_SSTAT register     |      |
	|      |                      |       | location of the LLI    |      |
	|      |                      |       | before the start of    |      |
	|      |                      |       | the next block if      |      |
	|      |                      |       | DMAX_CHx_LLI_WB_EN     |      |
	|      |                      |       | = 1 and linked list    |      |
	|      |                      |       | based multi-block      |      |
	|      |                      |       | transfer is enabled    |      |
	|      |                      |       | for                    |      |
	|      |                      |       | either source or       |      |
	|      |                      |       | destination peripheral |      |
	|      |                      |       | of the channel.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | Source peripheral      |      |
	|      |                      |       | should update the      |      |
	|      |                      |       | source status          |      |
	|      |                      |       | information, if any,   |      |
	|      |                      |       | at the location        |      |
	|      |                      |       | pointed to by          |      |
	|      |                      |       | CHx_SSTATAR to utilize |      |
	|      |                      |       | this feature.          |      |
	+------+----------------------+-------+------------------------+------+

CHx_DSTATAR
~~~~~~~~~~~

.. _table_chx_dstatar:
.. table:: CHx_DSTATAR, Offset Address: 0x178
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 63:0 | DSTATAR              | R/W   | Destination Status     | 0x0  |
	|      |                      |       | Fetch Address          |      |
	|      |                      |       |                        |      |
	|      |                      |       | Pointer from where     |      |
	|      |                      |       | hardware can fetch the |      |
	|      |                      |       | Destination            |      |
	|      |                      |       | status information,    |      |
	|      |                      |       | which is registered in |      |
	|      |                      |       | the CHx_DSTAT          |      |
	|      |                      |       | register and written   |      |
	|      |                      |       | out to the CHx_DSTAT   |      |
	|      |                      |       | register location      |      |
	|      |                      |       | of the LLI before the  |      |
	|      |                      |       | start of the next      |      |
	|      |                      |       | block if               |      |
	|      |                      |       | DMAX_CHx_LLI_WB_EN = 1 |      |
	|      |                      |       | and linked list based  |      |
	|      |                      |       | multiblock             |      |
	|      |                      |       | transfer is enabled    |      |
	|      |                      |       | for either source or   |      |
	|      |                      |       | destination            |      |
	|      |                      |       | peripheral of the      |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Destination peripheral |      |
	|      |                      |       | should update the      |      |
	|      |                      |       | destination status     |      |
	|      |                      |       | information, if any,   |      |
	|      |                      |       | at the location        |      |
	|      |                      |       | pointed to by          |      |
	|      |                      |       | CHx_DSTATAR to utilize |      |
	|      |                      |       | this feature.          |      |
	+------+----------------------+-------+------------------------+------+

CHx_INTSTATUS_ENABLEREG
~~~~~~~~~~~~~~~~~~~~~~~

.. _table_chx_intstatus_enablereg:
.. table:: CHx_INTSTATUS_ENABLEREG, Offset Address: 0x180
	:widths: 1 5 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | Enable_BL\           | R/W   | Block Transfer Done    | 0x0  |
	|      | OCK_TFR_DONE_IntStat |       | Interrupt Status       |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Block  |      |
	|      |                      |       |   Transfer Done        |      |
	|      |                      |       |   Interrupt            |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Block  |      |
	|      |                      |       |   Transfer Done        |      |
	|      |                      |       |   Interrupt            |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | Enable\              | R/W   | DMA Transfer Done      | 0x0  |
	|      | _DMA_TFR_DONE_IntStat|       | Interrupt Status       |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of DMA    |      |
	|      |                      |       |   Transfer Done        |      |
	|      |                      |       |   Interrupt            |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of DMA    |      |
	|      |                      |       |   Transfer Done        |      |
	|      |                      |       |   Interrupt            |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Enable_S\            | R/W   | Source Transaction     | 0x0  |
	|      | RC_TRANSCOMP_IntStat |       | Completed Status       |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Source |      |
	|      |                      |       |   Transaction          |      |
	|      |                      |       |   Complete Interrupt in|      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Source |      |
	|      |                      |       |   Transaction Complete |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | Enable_D\            | R/W   | Destination            | 0x0  |
	|      | ST_TRANSCOMP_IntStat |       | Transaction Completed  |      |
	|      |                      |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of        |      |
	|      |                      |       |   Destination          |      |
	|      |                      |       |   Transaction          |      |
	|      |                      |       |   complete Interrupt in|      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of        |      |
	|      |                      |       |   Destination          |      |
	|      |                      |       |   Transaction          |      |
	|      |                      |       |   complete Interrupt in|      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_enablereg_2:
.. table:: CHx_INTSTATUS_ENABLEREG, Offset Address: 0x180 (continued)
	:widths: 1 5 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 5    | Enable\              | R/W   | Source Decode Error    | 0x0  |
	|      | _SRC_DEC_ERR_IntStat |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Source |      |
	|      |                      |       |   Decode Error         |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Source |      |
	|      |                      |       |   Decode Error         |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | Enable\              | R/W   | Destination Decode     | 0x0  |
	|      | _DST_DEC_ERR_IntStat |       | Error Status Enable.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of        |      |
	|      |                      |       |   Destination Decode   |      |
	|      |                      |       |   Error                |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of        |      |
	|      |                      |       |   Destination Decode   |      |
	|      |                      |       |   Error                |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Enable\              | R/W   | Source Slave Error     | 0x0  |
	|      | _SRC_SLV_ERR_IntStat |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Source |      |
	|      |                      |       |   Slave Error Interrupt|      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Source |      |
	|      |                      |       |   Slave Error Interrupt|      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | Enable\              | R/W   | Destination Slave      | 0x0  |
	|      | _DST_SLV_ERR_IntStat |       | Error Status Enable.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of        |      |
	|      |                      |       |   Destination Slave    |      |
	|      |                      |       |   Error                |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of        |      |
	|      |                      |       |   Destination Slave    |      |
	|      |                      |       |   Error                |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_enablereg_3:
.. table:: CHx_INTSTATUS_ENABLEREG, Offset Address: 0x180 (continued)
	:widths: 1 5 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9    | Enable_LL\           | R/W   | LLI Read Decode Error  | 0x0  |
	|      | I_RD_DEC_ERR_IntStat |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of LLI    |      |
	|      |                      |       |   Read  Decode Error   |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of LLI    |      |
	|      |                      |       |   Read Decode Error    |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | Enable_LL\           | R/W   | LLI WRITE Decode Error | 0x0  |
	|      | I_WR_DEC_ERR_IntStat |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of LLI    |      |
	|      |                      |       |   WRITE Decode Error   |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of LLI    |      |
	|      |                      |       |   WRITE Decode Error   |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | Enable_LL\           | R/W   | LLI Read Slave Error   | 0x0  |
	|      | I_RD_SLV_ERR_IntStat |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of LLI    |      |
	|      |                      |       |   Read Slave Error     |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of LLI    |      |
	|      |                      |       |   Read Slave Error     |      |
	|      |                      |       |   Interrupt            |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | Enable_LL\           | R/W   | LLI WRITE Slave Error  | 0x0  |
	|      | I_WR_SLV_ERR_IntStat |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of LLI    |      |
	|      |                      |       |   WRITE Slave Error    |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of LLI    |      |
	|      |                      |       |   WRITE Slave Error    |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_enablereg_4:
.. table:: CHx_INTSTATUS_ENABLEREG, Offset Address: 0x180 (continued)
	:widths: 1 5 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 13   | Ena\                 | R/W   | Shadow register or LLI | 0x0  |
	|      | ble_SHADOWREG_OR_LLI\|       | Invalid Error Status   |      |
	|      | _INVALID_ERR         |       | Enable.                |      |
	|      | _IntStat             |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Shadow |      |
	|      |                      |       |   Register or LLI      |      |
	|      |                      |       |   Invalid Error        |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Shadow |      |
	|      |                      |       |   Register or LLI      |      |
	|      |                      |       |   Invalid Error        |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | Enable_SLVIF_MULT\   | R/W   | Slave Interface Multi  | 0x0  |
	|      | IBLKTYPE_ERR_IntStat |       | Block type Error       |      |
	|      |                      |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Multi Block|      |
	|      |                      |       |   type Error Interrupt |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Multi Block|      |
	|      |                      |       |   type Error Interrupt |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | Enable_S\            | R/W   | Slave Interface Decode | 0x0  |
	|      | LVIF_DEC_ERR_IntStat |       | Error Status Enable.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Decode     |      |
	|      |                      |       |   Error Interrupt in   |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Decode     |      |
	|      |                      |       |   Error Interrupt in   |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | Enable_SLV\          | R/W   | Slave Interface Write  | 0x0  |
	|      | IF_WR2RO_ERR_IntStat |       | to Read Only Error     |      |
	|      |                      |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Write to   |      |
	|      |                      |       |   Read                 |      |
	|      |                      |       |   only Error Interrupt |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Write to   |      |
	|      |                      |       |   Read                 |      |
	|      |                      |       |   Only Error Interrupt |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_enablereg_5:
.. table:: CHx_INTSTATUS_ENABLEREG, Offset Address: 0x180 (continued)
	:widths: 1 5 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 18   | Enable_SLVI\         | R/W   | Slave Interface Read   | 0x0  |
	|      | F_RD2RWO_ERR_IntStat |       | to write Only Error    |      |
	|      |                      |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Read to    |      |
	|      |                      |       |   Write                |      |
	|      |                      |       |   only Error Interrupt |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Read to    |      |
	|      |                      |       |   Write                |      |
	|      |                      |       |   Only Error Interrupt |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | Enable_SLVIF\        | R/W   | Slave Interface Write  | 0x0  |
	|      | _WRONCHEN_ERR_IntStat|       | On Channel Enabled     |      |
	|      |                      |       | Error Status           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Write On   |      |
	|      |                      |       |   Channel enabled Error|      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Write On   |      |
	|      |                      |       |   Channel enabled Error|      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | Enabl\               | R/W   | Shadow Register Write  | 0x0  |
	|      | e_SLVIF_SHADOWREG_WR\|       | On Valid Error Status  |      |
	|      | ON_VALID             |       | Enable.                |      |
	|      | _ERR_IntStat         |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Shadow |      |
	|      |                      |       |   Register Write On    |      |
	|      |                      |       |   Valid Error Interrupt|      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Shadow |      |
	|      |                      |       |   register Write On    |      |
	|      |                      |       |   Valid Error Interrupt|      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | Enable_SLVIF\        | R/W   | Slave Interface Write  | 0x0  |
	|      | _WRONHOLD_ERR_IntStat|       | On Hold Error Status   |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Write On   |      |
	|      |                      |       |   Hold Error Interrupt |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Slave  |      |
	|      |                      |       |   Interface Write On   |      |
	|      |                      |       |   Hold                 |      |
	|      |                      |       |   Error Interrupt in   |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	
To be continued ......

.. _table_chx_intstatus_enablereg_6:
.. table:: CHx_INTSTATUS_ENABLEREG, Offset Address: 0x180 (continued)
	:widths: 1 5 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 26:22| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | Enable_CH\           | R/W   | Channel Lock Cleared   | 0x0  |
	|      | _LOCK_CLEARED_IntStat|       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Channel|      |
	|      |                      |       |   LOCK CLEARED         |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Channel|      |
	|      |                      |       |   LOCK CLEARED         |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | Enable_CH_S\         | R/W   | Channel Source         | 0x0  |
	|      | RC_SUSPENDED_IntStat |       | Suspended Status       |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Channel|      |
	|      |                      |       |   Source Suspended     |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Channel|      |
	|      |                      |       |   Source Suspended     |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 29   | Enable\              | R/W   | Channel Suspended      | 0x0  |
	|      | _CH_SUSPENDED_IntStat|       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Channel|      |
	|      |                      |       |   Suspended            |      |
	|      |                      |       |   Interrupt in         |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Channel|      |
	|      |                      |       |   Suspended Interrupt  |      |
	|      |                      |       |   in CHx_INTSTATUSREG  |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | Enable\              | R/W   | Channel Disabled       | 0x0  |
	|      | _CH_DISABLED_IntStat |       | Status Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Channel|      |
	|      |                      |       |   Disabled Interrupt in|      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Channel|      |
	|      |                      |       |   Disabled Interrupt in|      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | Enabl\               | R/W   | Channel Aborted Status | 0x0  |
	|      | e_CH_ABORTED_IntStat |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   generation of Channel|      |
	|      |                      |       |   Aborted Interrupt in |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   generation of Channel|      |
	|      |                      |       |   Aborted Interrupt in |      |
	|      |                      |       |   CHx_INTSTATUSREG     |      |
	+------+----------------------+-------+------------------------+------+


CHx_INTSTATUS
~~~~~~~~~~~~~

.. _table_chx_intstatus:
.. table:: CHx_INTSTATUS, Offset Address: 0x188
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | BL\                  | RO    | Block Transfer Done.   |      |
	|      | OCK_TFR_DONE_IntStat |       |                        |      |
	|      |                      |       | This indicates to the  |      |
	|      |                      |       | software that the      |      |
	|      |                      |       | DW_axi_dmac has        |      |
	|      |                      |       | completed the          |      |
	|      |                      |       | requested block        |      |
	|      |                      |       | transfer.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | The DW_axi_dmac sets   |      |
	|      |                      |       | this bit to 1 when the |      |
	|      |                      |       | transfer is            |      |
	|      |                      |       | successfully           |      |
	|      |                      |       | completed.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Block Transfer    |      |
	|      |                      |       |   not completed.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Block Transfer    |      |
	|      |                      |       |   completed.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is cleared to |      |
	|      |                      |       | 0 on writing 1 to the  |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | clear bit in           |      |
	|      |                      |       | CHx_IntClearReg        |      |
	|      |                      |       | register.              |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | DMA_TFR_DONE_IntStat | RO    | DMA Transfer Done.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | This indicates to the  |      |
	|      |                      |       | software that the      |      |
	|      |                      |       | DW_axi_dmac has        |      |
	|      |                      |       | completed the          |      |
	|      |                      |       | requested DMA          |      |
	|      |                      |       | transfer.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | The DW_axi_dmac sets   |      |
	|      |                      |       | this bit to 1 along    |      |
	|      |                      |       | with setting           |      |
	|      |                      |       | CHx_IN\                |      |
	|      |                      |       | TSTATUS.BLOCK_TFR_DONE |      |
	|      |                      |       | bit to 1 when the last |      |
	|      |                      |       | block transfer is      |      |
	|      |                      |       | completed.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: DMA Transfer not  |      |
	|      |                      |       |   completed.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: DMA Transfer      |      |
	|      |                      |       |   Completed            |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is cleared to |      |
	|      |                      |       | 0 on writing 1         |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | S\                   | RO    | Source Transaction     |      |
	|      | RC_TRANSCOMP_IntStat |       | Completed.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is cleared to |      |
	|      |                      |       | 0 on writing 1 to the  |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | clear bit in           |      |
	|      |                      |       | CHx_IntClearReg        |      |
	|      |                      |       | register or on         |      |
	|      |                      |       | enabling the channel   |      |
	|      |                      |       | (needed when interrupt |      |
	|      |                      |       | is not enabled.        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | D\                   | RO    | Destination            |      |
	|      | ST_TRANSCOMP_IntStat |       | Transaction Completed. |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is cleared to |      |
	|      |                      |       | 0 on writing 1 to the  |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | channel interrupt      |      |
	|      |                      |       | clear bit in           |      |
	|      |                      |       | CHx_IntClearReg        |      |
	|      |                      |       | register or on         |      |
	|      |                      |       | enabling the channel   |      |
	|      |                      |       | (needed when interrupt |      |
	|      |                      |       | is not enabled.        |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_2:
.. table:: CHx_INTSTATUS, Offset Address: 0x188 (continued)
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 5    | SRC_DEC_ERR_IntStat  | RO    | Source Decode Error.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Decode Error detected  |      |
	|      |                      |       | by Master Interface    |      |
	|      |                      |       | during source          |      |
	|      |                      |       | data transfer. This    |      |
	|      |                      |       | error occurs if the    |      |
	|      |                      |       | access is to invalid   |      |
	|      |                      |       | address and a Decode   |      |
	|      |                      |       | Error is returned from |      |
	|      |                      |       | interconnect/slave.    |      |
	|      |                      |       | This error condition   |      |
	|      |                      |       | causes the             |      |
	|      |                      |       | DW_axi_dmac to disable |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel                |      |
	|      |                      |       | gracefully; the        |      |
	|      |                      |       | DMAC_ChEnReg.CH_EN bit |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | to the channel which   |      |
	|      |                      |       | received the error is  |      |
	|      |                      |       | set to 0.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Source Decode  |      |
	|      |                      |       |   Errors.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Source Decode     |      |
	|      |                      |       |   Error detected.      |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | DST_DEC_ERR_IntStat  | RO    | Destination Decode     |      |
	|      |                      |       | Error.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Decode Error detected  |      |
	|      |                      |       | by Master Interface    |      |
	|      |                      |       | during                 |      |
	|      |                      |       | destination data       |      |
	|      |                      |       | transfer. This error   |      |
	|      |                      |       | occurs if the access   |      |
	|      |                      |       | is to                  |      |
	|      |                      |       | invalid address and a  |      |
	|      |                      |       | Decode Error is        |      |
	|      |                      |       | returned from          |      |
	|      |                      |       | interconnect/slave.    |      |
	|      |                      |       | This error condition   |      |
	|      |                      |       | causes the             |      |
	|      |                      |       | DW_axi_dmac to disable |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel                |      |
	|      |                      |       | gracefully; the        |      |
	|      |                      |       | DMAC_ChEnReg.CH_EN bit |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | to the channel which   |      |
	|      |                      |       | received the error is  |      |
	|      |                      |       | set to 0.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No destination    |      |
	|      |                      |       |   Decode Errors.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Destination       |      |
	|      |                      |       |   Decode Error Detected|      |
	+------+----------------------+-------+------------------------+------+
	| 7    | SRC_SLV_ERR_IntStat  | RO    | Source Slave Error.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Slave Error detected   |      |
	|      |                      |       | by Master Interface    |      |
	|      |                      |       | during source data     |      |
	|      |                      |       | transfer. This error   |      |
	|      |                      |       | occurs if the slave    |      |
	|      |                      |       | interface from which   |      |
	|      |                      |       | the data is read       |      |
	|      |                      |       | issues a Slave Error.  |      |
	|      |                      |       | This error condition   |      |
	|      |                      |       | causes the DW_axi_dmac |      |
	|      |                      |       | to disable the         |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | channel gracefully;    |      |
	|      |                      |       | the DMAC_ChEnReg.CH_EN |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | corresponding to the   |      |
	|      |                      |       | channel which received |      |
	|      |                      |       | the error is set       |      |
	|      |                      |       | to 0.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Source Slave   |      |
	|      |                      |       |   Errors               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Source Slave      |      |
	|      |                      |       |   Error Detected       |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_3:
.. table:: CHx_INTSTATUS, Offset Address: 0x188 (continued)
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 8    | DST_SLV_ERR_IntStat  | RO    | Destination Slave      |      |
	|      |                      |       | Error.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Slave Error detected   |      |
	|      |                      |       | by Master Interface    |      |
	|      |                      |       | during destination     |      |
	|      |                      |       | data transfer. This    |      |
	|      |                      |       | error occurs if the    |      |
	|      |                      |       | slave interface to     |      |
	|      |                      |       | which                  |      |
	|      |                      |       | the data is written    |      |
	|      |                      |       | issues a Slave Error.  |      |
	|      |                      |       | This error condition   |      |
	|      |                      |       | causes the DW_axi_dmac |      |
	|      |                      |       | to disable the         |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | channel gracefully;    |      |
	|      |                      |       | the DMAC_ChEnReg.CH_EN |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | corresponding to the   |      |
	|      |                      |       | channel which received |      |
	|      |                      |       | the error is set       |      |
	|      |                      |       | to 0.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Destination    |      |
	|      |                      |       |   Slave Errors         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Destination Slave |      |
	|      |                      |       |   Errors Detected      |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | LL\                  | RO    | LLI Read Decode Error. |      |
	|      | I_RD_DEC_ERR_IntStat |       |                        |      |
	|      |                      |       | Decode Error detected  |      |
	|      |                      |       | by Master Interface    |      |
	|      |                      |       | during LLI read        |      |
	|      |                      |       | operation. This error  |      |
	|      |                      |       | occurs if the access   |      |
	|      |                      |       | is to invalid          |      |
	|      |                      |       | address and a Decode   |      |
	|      |                      |       | Error is returned from |      |
	|      |                      |       | interconnect/slave.    |      |
	|      |                      |       | This error condition   |      |
	|      |                      |       | causes the             |      |
	|      |                      |       | DW_axi_dmac to disable |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel                |      |
	|      |                      |       | gracefully; the        |      |
	|      |                      |       | DMAC_ChEnReg.CH_EN1    |      |
	|      |                      |       | bit which received     |      |
	|      |                      |       | the error is set to 0. |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: NO LLI Read       |      |
	|      |                      |       |   Decode Errors.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: LLI Read Decode   |      |
	|      |                      |       |   Error detected       |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | LL\                  | RO    | LLI WRITE Decode       |      |
	|      | I_WR_DEC_ERR_IntStat |       | Error.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Decode Error detected  |      |
	|      |                      |       | by Master Interface    |      |
	|      |                      |       | during LLI writeback   |      |
	|      |                      |       | operation. This error  |      |
	|      |                      |       | occurs if the access   |      |
	|      |                      |       | is to invalid          |      |
	|      |                      |       | address and a Decode   |      |
	|      |                      |       | Error is returned from |      |
	|      |                      |       | interconnect/slave.    |      |
	|      |                      |       | This error condition   |      |
	|      |                      |       | causes the             |      |
	|      |                      |       | DW_axi_dmac to disable |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel                |      |
	|      |                      |       | gracefully; the        |      |
	|      |                      |       | DMAC_ChEnReg.CH_EN1    |      |
	|      |                      |       | bit which received     |      |
	|      |                      |       | the error is set to 0. |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: NO LLI Write      |      |
	|      |                      |       |   Decode Errors.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: LLI write Decode  |      |
	|      |                      |       |   Error detected.      |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_4:
.. table:: CHx_INTSTATUS, Offset Address: 0x188 (continued)
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11   | LL\                  | RO    | LLI Read Slave Error.  |      |
	|      | I_RD_SLV_ERR_IntStat |       |                        |      |
	|      |                      |       | Slave Error detected   |      |
	|      |                      |       | by Master Interface    |      |
	|      |                      |       | during LLI read        |      |
	|      |                      |       | operation. This error  |      |
	|      |                      |       | occurs if the slave    |      |
	|      |                      |       | interface on which     |      |
	|      |                      |       | LLI resides issues a   |      |
	|      |                      |       | Slave Error. This      |      |
	|      |                      |       | error condition causes |      |
	|      |                      |       | the DW_axi_dmac to     |      |
	|      |                      |       | disable the            |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | gracefully; the        |      |
	|      |                      |       | DMAC_ChEnReg.CH_EN1    |      |
	|      |                      |       | bit which received     |      |
	|      |                      |       | the error is set to 0. |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No LLI Read Slave |      |
	|      |                      |       |   Errors.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: LLI read Slave    |      |
	|      |                      |       |   Error detected.      |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | LL\                  | RO    | LLI WRITE Slave Error. |      |
	|      | I_WR_SLV_ERR_IntStat |       |                        |      |
	|      |                      |       | Slave Error detected   |      |
	|      |                      |       | by Master Interface    |      |
	|      |                      |       | during LLI writeback   |      |
	|      |                      |       | operation. This error  |      |
	|      |                      |       | occurs if the slave    |      |
	|      |                      |       | interface on           |      |
	|      |                      |       | which LLI resides      |      |
	|      |                      |       | issues a Slave Error.  |      |
	|      |                      |       | This error condition   |      |
	|      |                      |       | causes the DW_axi_dmac |      |
	|      |                      |       | to disable the         |      |
	|      |                      |       | corresponding          |      |
	|      |                      |       | channel gracefully;    |      |
	|      |                      |       | the                    |      |
	|      |                      |       | DMAC_ChEnReg.CH_EN1    |      |
	|      |                      |       | bit which              |      |
	|      |                      |       | received the error is  |      |
	|      |                      |       | set to 0.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No LLI write      |      |
	|      |                      |       |   Slave Errors.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: LLI Write SLAVE   |      |
	|      |                      |       |   Error detected.      |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_5:
.. table:: CHx_INTSTATUS, Offset Address: 0x188 (continued)
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 13   | SHADOWREG_OR_LLI     | RO    | Shadow register or LLI |      |
	|      | _INVALID_ERR_IntStat |       | Invalid Error.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | This error occurs if   |      |
	|      |                      |       | CHx_CTL.               |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit                    |      |
	|      |                      |       | is seen to be 0 during |      |
	|      |                      |       | DW_axi_dmac Shadow     |      |
	|      |                      |       | Register / LLI         |      |
	|      |                      |       | fetch phase. This      |      |
	|      |                      |       | error condition causes |      |
	|      |                      |       | the DW_axi_dmac        |      |
	|      |                      |       | to halt the            |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | gracefully; Error      |      |
	|      |                      |       | Interrupt              |      |
	|      |                      |       | is generated if the    |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | error interrupt        |      |
	|      |                      |       | mask bit is set to 0   |      |
	|      |                      |       | and the channel waits  |      |
	|      |                      |       | till software writes   |      |
	|      |                      |       | (any value) to         |      |
	|      |                      |       | CH\                    |      |
	|      |                      |       | x_BLK_TFR_ResumeReqReg |      |
	|      |                      |       | to indicate            |      |
	|      |                      |       | valid Shadow Register  |      |
	|      |                      |       | availability.          |      |
	|      |                      |       |                        |      |
	|      |                      |       | In the case of LLI     |      |
	|      |                      |       | pre-fetching,          |      |
	|      |                      |       | Shadow\                |      |
	|      |                      |       | Reg_Or_LLI_Invalid_ERR |      |
	|      |                      |       | Interrupt is not       |      |
	|      |                      |       | generated              |      |
	|      |                      |       | even if                |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is seen to be 0    |      |
	|      |                      |       | for the                |      |
	|      |                      |       | pre-fetched LLI. In    |      |
	|      |                      |       | this case, DW_axi_dmac |      |
	|      |                      |       | re-attempts the        |      |
	|      |                      |       | LLI fetch operation    |      |
	|      |                      |       | after completing the   |      |
	|      |                      |       | current block transfer |      |
	|      |                      |       | and generates          |      |
	|      |                      |       | Shadow                 |      |
	|      |                      |       | Reg_Or_LLI_Invalid_ERR |      |
	|      |                      |       | Interrupt              |      |
	|      |                      |       | only if                |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is still seen to   |      |
	|      |                      |       | be 0.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Shadow         |      |
	|      |                      |       |   Register / LLI       |      |
	|      |                      |       |   Invalid errors.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Shadow Register / |      |
	|      |                      |       |   LLI Invalid error    |      |
	|      |                      |       |   detected.            |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | SLVIF_MULT           | RO    | Slave Interface Multi  |      |
	|      | IBLKTYPE_ERR_IntStat |       | Block type Error.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | This error occurs if   |      |
	|      |                      |       | multi-block transfer   |      |
	|      |                      |       | type programmed in     |      |
	|      |                      |       | CHx_CFG register       |      |
	|      |                      |       | (SRC_MLTBLK_TYPE and   |      |
	|      |                      |       | DST_MLTBLK_TYPE) is    |      |
	|      |                      |       | invalid. This error    |      |
	|      |                      |       | condition causes       |      |
	|      |                      |       | the DW_axi_dmac to     |      |
	|      |                      |       | halt the corresponding |      |
	|      |                      |       | channel                |      |
	|      |                      |       | gracefully; Error      |      |
	|      |                      |       | Interrupt is generated |      |
	|      |                      |       | if the corresponding   |      |
	|      |                      |       | channel error          |      |
	|      |                      |       | interrupt mask bit is  |      |
	|      |                      |       | set to 0 and the       |      |
	|      |                      |       | channel                |      |
	|      |                      |       | waits till software    |      |
	|      |                      |       | writes (any value) to  |      |
	|      |                      |       |                        |      |
	|      |                      |       | CH\                    |      |
	|      |                      |       | x_BLK_TFR_ResumeReqReg |      |
	|      |                      |       | to indicate valid      |      |
	|      |                      |       | multiblock             |      |
	|      |                      |       | transfer type          |      |
	|      |                      |       | availability.          |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Multi-block    |      |
	|      |                      |       |   transfer type Errors.|      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Multi-block       |      |
	|      |                      |       |   transfer type Error  |      |
	|      |                      |       |   detected.            |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_6:
.. table:: CHx_INTSTATUS, Offset Address: 0x188 (continued)
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | S\                   | RO    | Slave Interface Decode |      |
	|      | LVIF_DEC_ERR_IntStat |       | Error.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Decode Error generated |      |
	|      |                      |       | by DW_axi_dmac during  |      |
	|      |                      |       | register               |      |
	|      |                      |       | access. This error     |      |
	|      |                      |       | occurs if the register |      |
	|      |                      |       | access is to invalid   |      |
	|      |                      |       | address in Channelx    |      |
	|      |                      |       | register space         |      |
	|      |                      |       | resulting in error     |      |
	|      |                      |       | response by            |      |
	|      |                      |       | DW_axi_dmac slave      |      |
	|      |                      |       | interface.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Decode     |      |
	|      |                      |       |   errors.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Decode Error         |      |
	|      |                      |       |   detected.            |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | SLV\                 | RO    | Slave Interface Write  |      |
	|      | IF_WR2RO_ERR_IntStat |       | to Read Only Error.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | This error occurs if   |      |
	|      |                      |       | write operation is     |      |
	|      |                      |       | performed to a Read    |      |
	|      |                      |       | Only register.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Write to   |      |
	|      |                      |       |   Read Only Errors.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Write to Read Only   |      |
	|      |                      |       |   Error detected.      |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | SLVI\                | RO    | Slave Interface Read   |      |
	|      | F_RD2RWO_ERR_IntStat |       | to write Only Error.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This error occurs if   |      |
	|      |                      |       | read operation is      |      |
	|      |                      |       | performed to a Write   |      |
	|      |                      |       | Only register.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Read to    |      |
	|      |                      |       |   Write Only Errors.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Read to Write Only   |      |
	|      |                      |       |   Error detected.      |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | SLVIF\_\             | RO    | Slave Interface Write  |      |
	|      | WRONCHEN_ERR_IntStat |       | On Channel Enabled     |      |
	|      |                      |       | Error.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | This error occurs if   |      |
	|      |                      |       | an illegal write       |      |
	|      |                      |       | operation is performed |      |
	|      |                      |       | on                     |      |
	|      |                      |       | a register; this       |      |
	|      |                      |       | happens if a write     |      |
	|      |                      |       | operation is performed |      |
	|      |                      |       | on a                   |      |
	|      |                      |       | register when the      |      |
	|      |                      |       | channel is enabled and |      |
	|      |                      |       | if it is not allowed   |      |
	|      |                      |       | for the corresponding  |      |
	|      |                      |       | register as per the    |      |
	|      |                      |       | DW_axi_dmac            |      |
	|      |                      |       | specification.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Write On   |      |
	|      |                      |       |   Channel Enabled      |      |
	|      |                      |       |   Errors.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Write On Channel     |      |
	|      |                      |       |   Enabled Error        |      |
	|      |                      |       |   detected.            |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_7:
.. table:: CHx_INTSTATUS, Offset Address: 0x188 (continued)
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 20   | SLVIF_SHADOWREG_WR   | RO    | Shadow Register Write  |      |
	|      | ON_VALID_ERR_IntStat |       | On Valid Error.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | This error occurs if   |      |
	|      |                      |       | shadow register based  |      |
	|      |                      |       | multi-block            |      |
	|      |                      |       | transfer is enabled    |      |
	|      |                      |       | and software tries to  |      |
	|      |                      |       | write to the shadow    |      |
	|      |                      |       | register when          |      |
	|      |                      |       | CHx_CTL.               |      |
	|      |                      |       | ShadowReg_Or_LLI_Valid |      |
	|      |                      |       | bit is 1.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Shadow     |      |
	|      |                      |       |   Register Write On    |      |
	|      |                      |       |   Valid Errors.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Shadow Register Write|      |
	|      |                      |       |   On Valid Error       |      |
	|      |                      |       |   detected.            |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | SLVIF\_\             | RO    | Slave Interface Write  |      |
	|      | WRONHOLD_ERR_IntStat |       | On Hold Error.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | This error occurs if   |      |
	|      |                      |       | an illegal write       |      |
	|      |                      |       | operation is performed |      |
	|      |                      |       | on                     |      |
	|      |                      |       | a register; this       |      |
	|      |                      |       | happens if a write     |      |
	|      |                      |       | operation is performed |      |
	|      |                      |       | on a                   |      |
	|      |                      |       | channel register when  |      |
	|      |                      |       | DW_axi_dmac is in Hold |      |
	|      |                      |       | mode.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: No Slave          |      |
	|      |                      |       |   Interface Write On   |      |
	|      |                      |       |   Hold Errors.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Slave Interface   |      |
	|      |                      |       |   Write On Hold Error  |      |
	|      |                      |       |   detected.            |      |
	+------+----------------------+-------+------------------------+------+	
	| 26:22| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | CH\_\                | RO    | Channel Lock Cleared.  |      |
	|      | LOCK_CLEARED_IntStat |       |                        |      |
	|      |                      |       | This indicates to the  |      |
	|      |                      |       | software that the      |      |
	|      |                      |       | locking of the         |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | in DW_axi_dmac is      |      |
	|      |                      |       | cleared.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Channel locking   |      |
	|      |                      |       |   is not cleared.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Channel locking   |      |
	|      |                      |       |   is cleared.          |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | CH_S\                | RO    | Channel Source         |      |
	|      | RC_SUSPENDED_IntStat |       | Suspended.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | This indicates to the  |      |
	|      |                      |       | software that the      |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | source data transfer   |      |
	|      |                      |       | in DW_axi_dmac is      |      |
	|      |                      |       | suspended.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Channel source is |      |
	|      |                      |       |   not suspended        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Channel Source is |      |
	|      |                      |       |   suspended.           |      |
	+------+----------------------+-------+------------------------+------+
	| 29   | CH_SUSPENDED_IntStat | RO    | Channel Suspended.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | This indicates to the  |      |
	|      |                      |       | software that the      |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | in DW_axi_dmac is      |      |
	|      |                      |       | suspended.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Channel is not    |      |
	|      |                      |       |   suspended.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Channel is        |      |
	|      |                      |       |   suspended.           |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intstatus_8:
.. table:: CHx_INTSTATUS, Offset Address: 0x188 (continued)
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 30   | CH_DISABLED_IntStat  | RO    | Channel Disabled.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | This indicates to the  |      |
	|      |                      |       | software that the      |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | in DW_axi_dmac is      |      |
	|      |                      |       | disabled.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Channel is not    |      |
	|      |                      |       |   disabled.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Channel is        |      |
	|      |                      |       |   disabled. Error      |      |
	|      |                      |       |   Interrupt is         |      |
	|      |                      |       |   generated if         |      |
	|      |                      |       |   the corresponding    |      |
	|      |                      |       |   bit in               |      |
	|      |                      |       |   C\                   |      |
	|      |                      |       |   Hx_INTSTATUS_ENABLE\ |      |
	|      |                      |       |   Reg is enabled.      |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | CH_ABORTED_IntStat   | RO    | Channel Aborted.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | This indicates to the  |      |
	|      |                      |       | software that the      |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | in DW_axi_dmac is      |      |
	|      |                      |       | aborted.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Channel is not    |      |
	|      |                      |       |   aborted              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Channel is        |      |
	|      |                      |       |   aborted              |      |
	+------+----------------------+-------+------------------------+------+

CHx_INTSIGNAL_ENABLEREG
~~~~~~~~~~~~~~~~~~~~~~~

.. _table_chx_intsignal_enablereg:
.. table:: CHx_INTSIGNAL_ENABLEREG, Offset Address: 0x190
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | Enable_BLOC          | R/W   | Block Transfer Done    | 0x0  |
	|      | K_TFR_DONE_IntSignal |       | Interrupt Signal       |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Block |      |
	|      |                      |       |   Transfer Done        |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Block |      |
	|      |                      |       |   Transfer Done        |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | Enable_DM            | R/W   | DMA Transfer Done      | 0x0  |
	|      | A_TFR_DONE_IntSignal |       | Interrupt Signal       |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of DMA   |      |
	|      |                      |       |   Transfer Done        |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of DMA   |      |
	|      |                      |       |   Transfer Done        |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Enable_SRC           | R/W   | Source Transaction     | 0x0  |
	|      | _TRANSCOMP_IntSignal |       | Completed Signal       |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Source|      |
	|      |                      |       |   Transaction          |      |
	|      |                      |       |   Complete Interrupt to|      |
	|      |                      |       |   generate a port level|      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Source|      |
	|      |                      |       |   Transaction          |      |
	|      |                      |       |   Complete Interrupt to|      |
	|      |                      |       |   generate a port level|      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | Enable_DST           | R/W   | Destination            | 0x0  |
	|      | _TRANSCOMP_IntSignal |       | Transaction Completed  |      |
	|      |                      |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Destination          |      |
	|      |                      |       |   Transaction          |      |
	|      |                      |       |   complete Interrupt to|      |
	|      |                      |       |   generate a port level|      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Destination          |      |
	|      |                      |       |   Transaction          |      |
	|      |                      |       |   complete Interrupt to|      |
	|      |                      |       |   generate a port level|      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | Enable_S             | R/W   | Source Decode Error    | 0x0  |
	|      | RC_DEC_ERR_IntSignal |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Source|      |
	|      |                      |       |   Decode Error         |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Source|      |
	|      |                      |       |   Decode Error         |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intsignal_enablereg_2:
.. table:: CHx_INTSIGNAL_ENABLEREG, Offset Address: 0x190 (continued)
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 6    | Enable_D             | R/W   | Destination Decode     | 0x0  |
	|      | ST_DEC_ERR_IntSignal |       | Error Signal Enable.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Destination Decode   |      |
	|      |                      |       |   Error                |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Destination Decode   |      |
	|      |                      |       |   Error                |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Enable_S             | R/W   | Source Slave Error     | 0x0  |
	|      | RC_SLV_ERR_IntSignal |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Source|      |
	|      |                      |       |   Slave Error Interrupt|      |
	|      |                      |       |   to generate a port   |      |
	|      |                      |       |   level interrupt      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Source|      |
	|      |                      |       |   Slave Error Interrupt|      |
	|      |                      |       |   to generate a port   |      |
	|      |                      |       |   level interrupt      |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | Enable_D             | R/W   | Destination Slave      | 0x0  |
	|      | ST_SLV_ERR_IntSignal |       | Error Signal Enable.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Destination Slave    |      |
	|      |                      |       |   Error                |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Destination Slave    |      |
	|      |                      |       |   Error                |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | Enable_LLI\_         | R/W   | LLI Read Decode Error  | 0x0  |
	|      | RD_DEC_ERR_IntSignal |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of LLI   |      |
	|      |                      |       |   Read Decode Error    |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of LLI   |      |
	|      |                      |       |   Read Decode Error    |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | Enable_LLI\_         | R/W   | LLI WRITE Decode Error | 0x0  |
	|      | WR_DEC_ERR_IntSignal |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of LLI   |      |
	|      |                      |       |   WRITE Decode Error   |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of LLI   |      |
	|      |                      |       |   WRITE Decode Error   |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | Enable_LLI\_         | R/W   | LLI Read Slave Error   | 0x0  |
	|      | RD_SLV_ERR_IntSignal |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of LLI   |      |
	|      |                      |       |   Read Slave Error     |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of LLI   |      |
	|      |                      |       |   Read Slave Error     |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	
To be continued ......

.. _table_chx_intsignal_enablereg_3:
.. table:: CHx_INTSIGNAL_ENABLEREG, Offset Address: 0x190 (continued)
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 12   | Enable_LLI\_         | R/W   | LLI WRITE Slave Error  | 0x0  |
	|      | WR_SLV_ERR_IntSignal |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of LLI   |      |
	|      |                      |       |   WRITE Slave Error    |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of LLI   |      |
	|      |                      |       |   WRITE Slave Error    |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | Enabl                | R/W   | Shadow register or LLI | 0x0  |
	|      | e_SHADOWREG_OR_LLI_I |       | Invalid Error Signal   |      |
	|      | NVALID_ERR_IntSignal |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Shadow|      |
	|      |                      |       |   Register or LLI      |      |
	|      |                      |       |   Invalid Error        |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Shadow|      |
	|      |                      |       |   Register or LLI      |      |
	|      |                      |       |   Invalid Error        |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | Enable_SLVIF_MULTIB  | R/W   | Slave Interface Multi  | 0x0  |
	|      | LKTYPE_ERR_IntSignal |       | Block type Error       |      |
	|      |                      |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Multi Block|      |
	|      |                      |       |   type Error Interrupt |      |
	|      |                      |       |   to generate a port   |      |
	|      |                      |       |   level interrupt      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Multi Block|      |
	|      |                      |       |   type Error Interrupt |      |
	|      |                      |       |   to generate a port   |      |
	|      |                      |       |   level interrupt      |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | Enable_SLV           | R/W   | Slave Interface Decode | 0x0  |
	|      | IF_DEC_ERR_IntSignal |       | Error Signal Enable.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Decode     |      |
	|      |                      |       |   Error Interrupt to   |      |
	|      |                      |       |   generate a port level|      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Decode     |      |
	|      |                      |       |   Error Interrupt to   |      |
	|      |                      |       |   generate a port level|      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | Enable_SLVIF         | R/W   | Slave Interface Write  | 0x0  |
	|      | _WR2RO_ERR_IntSignal |       | to Read Only Error     |      |
	|      |                      |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Write to   |      |
	|      |                      |       |   Read only Error      |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Write to   |      |
	|      |                      |       |   Read Only Error      |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	
To be continued ......

.. _table_chx_intsignal_enablereg_4:
.. table:: CHx_INTSIGNAL_ENABLEREG, Offset Address: 0x190 (continued)
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 18   | Enable_SLVIF\_       | R/W   | Slave Interface Read   | 0x0  |
	|      | RD2RWO_ERR_IntSignal |       | to write Only Error    |      |
	|      |                      |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Read to    |      |
	|      |                      |       |   Write only Error     |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Read to    |      |
	|      |                      |       |   Write Only Error     |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | Enable_SLVIF_WR      | R/W   | Slave Interface Write  | 0x0  |
	|      | ONCHEN_ERR_IntSignal |       | On Channel Enabled     |      |
	|      |                      |       | Error Signal           |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Write On   |      |
	|      |                      |       |   Channel enabled Error|      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Write On   |      |
	|      |                      |       |   Channel enabled Error|      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | Enable\_             | R/W   | Shadow Register Write  | 0x0  |
	|      | SLVIF_SHADOWREG_WRON |       | On Valid Error Signal  |      |
	|      | _VALID_ERR_IntSignal |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Shadow|      |
	|      |                      |       |   Register Write On    |      |
	|      |                      |       |   Valid Error Interrupt|      |
	|      |                      |       |   to generate a port   |      |
	|      |                      |       |   level interrupt      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Shadow|      |
	|      |                      |       |   register Write On    |      |
	|      |                      |       |   Valid Error Interrupt|      |
	|      |                      |       |   to generate a port   |      |
	|      |                      |       |   level interrupt      |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | Enable_SLVIF_WR      | R/W   | Slave Interface Write  | 0x0  |
	|      | ONHOLD_ERR_IntSignal |       | On Hold Error Signal   |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Write On   |      |
	|      |                      |       |   Hold Error Interrupt |      |
	|      |                      |       |   to generate a port   |      |
	|      |                      |       |   level interrupt      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of Slave |      |
	|      |                      |       |   Interface Write On   |      |
	|      |                      |       |   Hold Error Interrupt |      |
	|      |                      |       |   to generate a port   |      |
	|      |                      |       |   level interrupt      |      |
	+------+----------------------+-------+------------------------+------+
	| 26:22| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intsignal_enablereg_5:
.. table:: CHx_INTSIGNAL_ENABLEREG, Offset Address: 0x190 (continued)
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 27   | Enable_CH_LO         | R/W   | Channel Lock Cleared   | 0x0  |
	|      | CK_CLEARED_IntSignal |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Channel Lock Cleared |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Channel Lock Cleared |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | Enable_CH_SRC        | R/W   | Channel Source         | 0x0  |
	|      | _SUSPENDED_IntSignal |       | Suspended Signal       |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Channel Source       |      |
	|      |                      |       |   Suspended Interrupt  |      |
	|      |                      |       |   to generate a port   |      |
	|      |                      |       |   level interrupt      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Channel Source       |      |
	|      |                      |       |   Suspended Interrupt  |      |
	|      |                      |       |   to generate a port   |      |
	|      |                      |       |   level interrupt      |      |
	+------+----------------------+-------+------------------------+------+
	| 29   | Enable_CH            | R/W   | Channel Suspended      | 0x0  |
	|      | _SUSPENDED_IntSignal |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Channel Suspended    |      |
	|      |                      |       |   Interrupt to         |      |
	|      |                      |       |   generate a port      |      |
	|      |                      |       |   level interrupt      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Channel Suspended    |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | Enable_C             | R/W   | Channel Disabled       | 0x0  |
	|      | H_DISABLED_IntSignal |       | Signal Enable.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Channel Disabled     |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Channel Disabled     |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | Enable\_             | R/W   | Channel Aborted Signal | 0x0  |
	|      | CH_ABORTED_IntSignal |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Disable the       |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Channel Aborted      |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Enable the        |      |
	|      |                      |       |   propagation of       |      |
	|      |                      |       |   Channel Aborted      |      |
	|      |                      |       |   Interrupt to generate|      |
	|      |                      |       |   a port level         |      |
	|      |                      |       |   interrupt            |      |
	+------+----------------------+-------+------------------------+------+

CHx_INTCLEARREG
~~~~~~~~~~~~~~~

.. _table_chx_intclearreg:
.. table:: CHx_INTCLEARREG, Offset Address: 0x198
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | Clear_BL             | WO    | Block Transfer Done    | 0x0  |
	|      | OCK_TFR_DONE_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CH1_INTSTATUSREG       |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | Clear\_              | WO    | DMA Transfer Done      | 0x0  |
	|      | DMA_TFR_DONE_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Clear_S              | WO    | Source Transaction     | 0x0  |
	|      | RC_TRANSCOMP_IntStat |       | Completed Interrupt    |      |
	|      |                      |       | Clear Bit.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | Clear_D              | WO    | Destination            | 0x0  |
	|      | ST_TRANSCOMP_IntStat |       | Transaction Completed  |      |
	|      |                      |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | Clear                | WO    | Source Decode Error    | 0x0  |
	|      | _SRC_DEC_ERR_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | Clear                | WO    | Destination Decode     | 0x0  |
	|      | _DST_DEC_ERR_IntStat |       | Error Interrupt Clear  |      |
	|      |                      |       | Bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Clear                | WO    | Source Slave Error     | 0x0  |
	|      | _SRC_SLV_ERR_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | Clear                | WO    | Destination Slave      | 0x0  |
	|      | _DST_SLV_ERR_IntStat |       | Error Interrupt Clear  |      |
	|      |                      |       | Bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | Clear_LL             | WO    | LLI Read Decode Error  | 0x0  |
	|      | I_RD_DEC_ERR_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | Clear_LL             | WO    | LLI WRITE Decode Error | 0x0  |
	|      | I_WR_DEC_ERR_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intclearreg_2:
.. table:: CHx_INTCLEARREG, Offset Address: 0x198 (continued)
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 11   | Clear_LL             | WO    | LLI Read Slave Error   | 0x0  |
	|      | I_RD_SLV_ERR_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | Clear_LL             | WO    | LLI WRITE Slave Error  | 0x0  |
	|      | I_WR_SLV_ERR_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | Cl                   | WO    | Shadow register or LLI | 0x0  |
	|      | ear_SHADOWREG_OR_LLI |       | Invalid Error          |      |
	|      | _INVALID_ERR_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | Clear_SLVIF_MULT     | WO    | Slave Interface Multi  | 0x0  |
	|      | IBLKTYPE_ERR_IntStat |       | Block type Error       |      |
	|      |                      |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | Clear_S              | WO    | Slave Interface Decode | 0x0  |
	|      | LVIF_DEC_ERR_IntStat |       | Error Interrupt Clear  |      |
	|      |                      |       | Bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | Clear_SLV            | WO    | Slave Interface Write  | 0x0  |
	|      | IF_WR2RO_ERR_IntStat |       | to Read Only Error     |      |
	|      |                      |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | Clear_SLVI           | WO    | Slave Interface Read   | 0x0  |
	|      | F_RD2RWO_ERR_IntStat |       | to write Only Error    |      |
	|      |                      |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | Clear_SLVIF\_        | WO    | Slave Interface Write  | 0x0  |
	|      | WRONCHEN_ERR_IntStat |       | On Channel Enabled     |      |
	|      |                      |       | Error Interrupt        |      |
	|      |                      |       |                        |      |
	|      |                      |       | Clear Bit.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | Clea                 | WO    | Shadow Register Write  | 0x0  |
	|      | r_SLVIF_SHADOWREG_WR |       | On Valid Error         |      |
	|      | ON_VALID_ERR_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_chx_intclearreg_3:
.. table:: CHx_INTCLEARREG, Offset Address: 0x198 (continued)
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 21   | Clear_SLVIF\_        | WO    | Slave Interface Write  | 0x0  |
	|      | WRONHOLD_ERR_IntStat |       | On Hold Error          |      |
	|      |                      |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 26:22| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | Clear_CH\_           | WO    | Channel Lock Cleared   | 0x0  |
	|      | LOCK_CLEARED_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | Clear_CH_S           | WO    | Channel Source         | 0x0  |
	|      | RC_SUSPENDED_IntStat |       | Suspended Interrupt    |      |
	|      |                      |       | Clear Bit.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 29   | Clear\_              | WO    | Channel Suspended      | 0x0  |
	|      | CH_SUSPENDED_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | Clear                | WO    | Channel Disabled       | 0x0  |
	|      | _CH_DISABLED_IntStat |       | Interrupt Clear Bit.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | clear the              |      |
	|      |                      |       | corresponding channel  |      |
	|      |                      |       | interrupt              |      |
	|      |                      |       | status bit in          |      |
	|      |                      |       | CHx_INTSTATUSREG.      |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
