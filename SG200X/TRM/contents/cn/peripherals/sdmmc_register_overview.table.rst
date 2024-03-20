.. _table_sdmmc_register_overview:
.. table::  SDMMC Registers Overview
	:widths: 5 2 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| SDMA_SADDR           | 0x000   | SDMA System Memory Address/        |
	|                      |         | Argument2                          |
	+----------------------+---------+------------------------------------+
	| BLK_SIZE_AND_CNT     | 0x004   | Block Size and Block Count         |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+
	| ARGUMENT             | 0x008   | Argument 1 Register                |
	+----------------------+---------+------------------------------------+
	| XFER_MODE_AND_CMD    | 0x00c   | Transfer Mode and Command Register |
	+----------------------+---------+------------------------------------+
	| RESP31_0             | 0x010   | Response Bit 31-0 Regsiter         |
	+----------------------+---------+------------------------------------+
	| RESP63_32            | 0x014   | Response Bit 63-32 Regsiter        |
	+----------------------+---------+------------------------------------+
	| RESP95_64            | 0x018   | Response Bit 95-64 Regsiter        |
	+----------------------+---------+------------------------------------+
	| RESP127_96           | 0x01c   | Response Bit 127-96 Regsiter       |
	+----------------------+---------+------------------------------------+
	| BUF_DATA             | 0x020   | Buffer Data Port Register          |
	+----------------------+---------+------------------------------------+
	| PRESENT_STS          | 0x024   | Present State Register             |
	+----------------------+---------+------------------------------------+
	| HOST_CTL1_PWR_BG_WUP | 0x028   | Host Control 1 , Power, Block Gap  |
	|                      |         | and Wakeup Register                |
	+----------------------+---------+------------------------------------+
	| CLK_CTL_SWRST        | 0x02c   | Clock and Reset Control Register   |
	+----------------------+---------+------------------------------------+
	| NORM_AND_ERR_INT_STS | 0x030   | Normal and Error Interrupt Status  |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+
	| NOR\                 | 0x034   | Normal and Error Interrupt Status  |
	| M_AND_ERR_INT_STS_EN |         | Enable Register                    |
	+----------------------+---------+------------------------------------+
	| NOR\                 | 0x038   | Normal and Error Interrupt Signal  |
	| M_AND_ERR_INT_SIG_EN |         | Enable Register                    |
	+----------------------+---------+------------------------------------+
	| AUTO_C\              | 0x03c   | Auto CMD Error Status Register and |
	| MD_ERR_AND_HOST_CTL2 |         | Host Control 2 register            |
	+----------------------+---------+------------------------------------+
	| CAPABILITIES1        | 0x040   | Capabilities 1 Register            |
	+----------------------+---------+------------------------------------+
	| CAPABILITIES2        | 0x044   | Capabilities 2 Register            |
	+----------------------+---------+------------------------------------+
	| FORCE_EVENT_ERR      | 0x050   | Force Event Register for Auto CMD  |
	|                      |         | Error Status                       |
	+----------------------+---------+------------------------------------+
	| ADMA_ERR_STS         | 0x054   | ADMA Error Status Register         |
	+----------------------+---------+------------------------------------+
	| ADMA_SADDR_L         | 0x058   | ADMA System Address Register for   |
	|                      |         | low 32-bit                         |
	+----------------------+---------+------------------------------------+
	| ADMA_SADDR_H         | 0x05c   | ADMA System Address Register for   |
	|                      |         | high 32-bit                        |
	+----------------------+---------+------------------------------------+
	| PRESENT_VUL_INIT_DS  | 0x060   | Present Value Register for         |
	|                      |         | Initialization and Default Speed   |
	+----------------------+---------+------------------------------------+
	| PRESENT_VUL_HS_SDR12 | 0x064   | Present Value Register for         |
	|                      |         | High-speed and SDR12               |
	+----------------------+---------+------------------------------------+
	| PRE\                 | 0x068   | Present Value Register for SDR25   |
	| SENT_VUL_SDR25_SDR50 |         | and SDR50                          |
	+----------------------+---------+------------------------------------+
	| PRES\                | 0x06c   | Present Value Register for SDR104  |
	| ENT_VUL_SDR104_DDR50 |         | and DDR50                          |
	+----------------------+---------+------------------------------------+
	| S\                   | 0x0fc   | Slot Interrupt Status and Host     |
	| LOT_INT_AND_HOST_VER |         | Controller Version Register        |
	+----------------------+---------+------------------------------------+
	| EMMC_CTRL            | 0x200   | MSHC Control register              |
	+----------------------+---------+------------------------------------+
	| EMMC_BOOT_CTL        | 0x204   | eMMC Boot Control Register         |
	+----------------------+---------+------------------------------------+
	| CDET_TOUT_CTL        | 0x208   | Card Detect Control Register       |
	+----------------------+---------+------------------------------------+
	| MBIU_CTRL            | 0x20c   | MBIU Control register              |
	+----------------------+---------+------------------------------------+
	| PHY_TX_RX_DLY        | 0x240   | PHY tx and rx delay line register  |
	+----------------------+---------+------------------------------------+
	| PHY_DS_DLY           | 0x244   | PHY DS delay line register         |
	+----------------------+---------+------------------------------------+
	| PHY_DLY_STS          | 0x248   | PHY delay line status register     |
	+----------------------+---------+------------------------------------+
	| PHY_CONFIG           | 0x24c   | PHY Configuration register         |
	+----------------------+---------+------------------------------------+
