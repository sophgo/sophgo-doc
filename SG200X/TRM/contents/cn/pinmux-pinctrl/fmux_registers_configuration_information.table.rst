.. _table_fmux_info:
.. table:: FMUX Registers Configuration Information
	:widths: 1 2 6 1 5

	+---+------+------------------------+----+---------------------------+
	|Pin| Pin  |Function_select_register|fmu\| Description               |
	|Num| Name |                        |x\_ |                           |
	|   |      |                        |defa|                           |
	|   |      |                        |ult |                           |
	+===+======+========================+====+===========================+
	| 6 | SD0\ | FMUX_G\                | 0x0| IO SD0_CLK function       |
	|   | _CLK | PIO_REG_IOCTRL_SD0_CLK |    | select :                  |
	|   |      | 0x0300_101C            |    |                           |
	|   |      |                        |    | - 0 : SDIO0_CLK (default) |
	|   |      |                        |    | - 1 : IIC1_SDA            |
	|   |      |                        |    | - 2 : SPI0_SCK            |
	|   |      |                        |    | - 3 : XGPIOA[7]           |
	|   |      |                        |    | - 5 : PWM[15]             |
	|   |      |                        |    | - 6 : EPHY_LNK_LED        |
	|   |      |                        |    | - 7 : DBG[0]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 7 | SD0\ | FMUX_G\                | 0x0| IO SD0_CMD function       |
	|   | _CMD | PIO_REG_IOCTRL_SD0_CMD |    | select :                  |
	|   |      | 0x0300_1020            |    |                           |
	|   |      |                        |    | - 0 : SDIO0_CMD (default) |
	|   |      |                        |    | - 1 : IIC1_SCL            |
	|   |      |                        |    | - 2 : SPI0_SDO            |
	|   |      |                        |    | - 3 : XGPIOA[8]           |
	|   |      |                        |    | - 5 : PWM[14]             |
	|   |      |                        |    | - 6 : EPHY_SPD_LED        |
	|   |      |                        |    | - 7 : DBG[1]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 8 | SD0\ | FMUX_G\                | 0x0| IO SD0_D0 function select:|
	|   | _D0  | PIO_REG_IOCTRL_SD0_D0  |    |                           |
	|   |      | 0x0300_1024            |    | - 0 : SDIO0_D[0] (default)|
	|   |      |                        |    | - 1 : CAM_MCLK1           |
	|   |      |                        |    | - 2 : SPI0_SDI            |
	|   |      |                        |    | - 3 : XGPIOA[9]           |
	|   |      |                        |    | - 4 : UART3_TX            |
	|   |      |                        |    | - 5 : PWM[13]             |
	|   |      |                        |    | - 6 : WG0_D0              |
	|   |      |                        |    | - 7 : DBG[2]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 10| SD\  | FMUX_G\                | 0x0| IO SD0_D1 function select:|
	|   | 0_D1 | PIO_REG_IOCTRL_SD0_D1  |    |                           |
	|   |      | 0x0300_1028            |    | - 0 : SDIO0_D[1] (default)|
	|   |      |                        |    | - 1 : IIC1_SDA            |
	|   |      |                        |    | - 2 : AUX0                |
	|   |      |                        |    | - 3 : XGPIOA[10]          |
	|   |      |                        |    | - 4 : UART1_TX            |
	|   |      |                        |    | - 5 : PWM[12]             |
	|   |      |                        |    | - 6 : WG0_D1              |
	|   |      |                        |    | - 7 : DBG[3]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 11| SD\  | FMUX_G\                | 0x0| IO SD0_D2 function select:|
	|   | 0_D2 | PIO_REG_IOCTRL_SD0_D2  |    |                           |
	|   |      | 0x0300_102C            |    | - 0 : SDIO0_D[2] (default)|
	|   |      |                        |    | - 1 : IIC1_SCL            |
	|   |      |                        |    | - 2 : AUX1                |
	|   |      |                        |    | - 3 : XGPIOA[11]          |
	|   |      |                        |    | - 4 : UART1_RX            |
	|   |      |                        |    | - 5 : PWM[11]             |
	|   |      |                        |    | - 6 : WG1_D0              |
	|   |      |                        |    | - 7 : DBG[4]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 12| SD\  | FMUX_G\                | 0x0| IO SD0_D3 function select:|
	|   | 0_D3 | PIO_REG_IOCTRL_SD0_D3  |    |                           |
	|   |      | 0x0300_1030            |    | - 0 : SDIO0_D[3] (default)|
	|   |      |                        |    | - 1 : CAM_MCLK0           |
	|   |      |                        |    | - 2 : SPI0_CS_X           |
	|   |      |                        |    | - 3 : XGPIOA[12]          |
	|   |      |                        |    | - 4 : UART3_RX            |
	|   |      |                        |    | - 5 : PWM[10]             |
	|   |      |                        |    | - 6 : WG1_D1              |
	|   |      |                        |    | - 7 : DBG[5]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 14| SD\  |FMUX_GPIO_REG_IOCTRL\   | 0x0| IO SD0_CD function select:|
	|   | 0_CD |_SD0_CD                 |    |                           |
	|   |      |0x0300_1034             |    | - 0 : SDIO0_CD (default)  |
	|   |      |                        |    | - 3 : XGPIOA[13]          |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 15| SD   | FMUX_GPIO              | 0x3| IO SD0_PWR_EN function    |
	|   | 0_PW | _REG_IOCTRL_SD0_PWR_EN |    | select :                  |
	|   | R_EN | 0x0300_1038            |    |                           |
	|   |      |                        |    | - 0 : SDIO0_PWR_EN        |
	|   |      |                        |    | - 3 : XGPIOA[14] (default)|
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 17| SP\  | FMUX_G\                | 0x3| IO SPK_EN function select:|
	|   | K_EN | PIO_REG_IOCTRL_SPK_EN  |    |                           |
	|   |      | 0x0300_103C            |    | - 3 : XGPIOA[15] (default)|
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 18| UART\| FMUX_GP                | 0x0| IO UART0_TX function      |
	|   | 0_TX | IO_REG_IOCTRL_UART0_TX |    | select :                  |
	|   |      | 0x0300_1040            |    |                           |
	|   |      |                        |    | - 0 : UART0_TX (default)  |
	|   |      |                        |    | - 1 : CAM_MCLK1           |
	|   |      |                        |    | - 2 : PWM[4]              |
	|   |      |                        |    | - 3 : XGPIOA[16]          |
	|   |      |                        |    | - 4 : UART1_TX            |
	|   |      |                        |    | - 7 : DBG[6]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 19| UART\| FMUX_GP\               | 0x0| IO UART0_RX function      |
	|   | 0_RX | IO_REG_IOCTRL_UART0_RX |    | select :                  |
	|   |      | 0x0300_1044            |    |                           |
	|   |      |                        |    | - 0 : UART0_RX (default)  |
	|   |      |                        |    | - 1 : CAM_MCLK0           |
	|   |      |                        |    | - 2 : PWM[5]              |
	|   |      |                        |    | - 3 : XGPIOA[17]          |
	|   |      |                        |    | - 4 : UART1_RX            |
	|   |      |                        |    | - 5 : AUX0                |
	|   |      |                        |    | - 7 : DBG[7]              |
	|   |      |                        |    | - Others : Reserved       |	
	+---+------+------------------------+----+---------------------------+
	| 20|EMMC\ |FMUX_GPIO_REG_IOCTRL    | 0x1| IO EMMC_DAT2 function     |
	|   |_DAT2 |_EMMC_DAT2              |    | select :                  |
	|   |      |0x0300_104C             |    |                           |
	|   |      |                        |    | - 0 : EMMC_DAT[2]         |
	|   |      |                        |    | - 1 : SPINOR_HOLD_X\      |
	|   |      |                        |    |   (default)               |
	|   |      |                        |    | - 2 : SPINAND_HOLD        |
	|   |      |                        |    | - 3 : XGPIOA[26]          |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 21| EMMC\| FMUX_GP                | 0x1| IO EMMC_CLK function      |
	|   | _CLK | IO_REG_IOCTRL_EMMC_CLK |    | select :                  |
	|   |      | 0x0300_1050            |    |                           |
	|   |      |                        |    | - 0 : EMMC_CLK            |
	|   |      |                        |    | - 1 : SPINOR_SCK (default)|
	|   |      |                        |    | - 2 : SPINAND_CLK         |
	|   |      |                        |    | - 3 : XGPIOA[22]          |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 22| EMMC | FMUX_GPI               | 0x1| IO EMMC_DAT0 function     |
	|   | _DAT0| O_REG_IOCTRL_EMMC_DAT0 |    | select :                  |
	|   |      | 0x0300_1054            |    |                           |
	|   |      |                        |    | - 0 : EMMC_DAT[0]         |
	|   |      |                        |    | - 1 : SPINOR_MOSI(default)|
	|   |      |                        |    | - 2 : SPINAND_MOSI        |
	|   |      |                        |    | - 3 : XGPIOA[25]          |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 23| EMMC | FMUX_GPI               | 0x1|IO EMMC_DAT3 function      |
	|   | _DAT3| O_REG_IOCTRL_EMMC_DAT3 |    |select :                   |
	|   |      | 0x0300_1058            |    |                           |
	|   |      |                        |    |- 0 : EMMC_DAT[3]          |
	|   |      |                        |    |- 1 : SPINOR_WP_X (default)|
	|   |      |                        |    |- 2 : SPINAND_WP           |
	|   |      |                        |    |- 3 : XGPIOA[27]           |
	|   |      |                        |    |- Others : Reserved        |
	+---+------+------------------------+----+---------------------------+
	| 24| EMMC | FMUX_GP                | 0x1|IO EMMC_CMD function       |
	|   | _CMD | IO_REG_IOCTRL_EMMC_CMD |    |select :                   |
	|   |      | 0x0300_105C            |    |                           |
	|   |      |                        |    |- 0 : EMMC_CMD             |
	|   |      |                        |    |- 1 : SPINOR_MISO (default)|
	|   |      |                        |    |- 2 : SPINAND_MISO         |
	|   |      |                        |    |- 3 : XGPIOA[23]           |
	|   |      |                        |    |- Others : Reserved        |
	+---+------+------------------------+----+---------------------------+
	| 25|EMMC  | FMUX_GPI               | 0x1|IO EMMC_DAT1 function      |
	|   |_DAT1 | O_REG_IOCTRL_EMMC_DAT1 |    |select :                   |
	|   |      | 0x0300_1060            |    |                           |
	|   |      |                        |    |- 0 : EMMC_DAT[1]          |
	|   |      |                        |    |- 1 : SPINOR_CS_X (default)|
	|   |      |                        |    |- 2 : SPINAND_CS           |
	|   |      |                        |    |- 3 : XGPIOA[24]           |
	|   |      |                        |    |- Others : Reserved        |
	+---+------+------------------------+----+---------------------------+
	| 26| JTAG | FMUX_GPIO_R            | 0x0| IO JTAG_CPU_TMS function  |
	|   | _CPU | EG_IOCTRL_JTAG_CPU_TMS |    | select :                  |
	|   | _TMS | 0x0300_1064            |    |                           |
	|   | _TMS |                        |    | - 0 : CR_4WTMS (default)  |
	|   |      |                        |    | - 1 : CAM_MCLK0           |
	|   |      |                        |    | - 2 : PWM[7]              |
	|   |      |                        |    | - 3 : XGPIOA[19]          |
	|   |      |                        |    | - 4 : UART1_RTS           |
	|   |      |                        |    | - 5 : AUX0                |
	|   |      |                        |    | - 6 : UART1_TX            |
	|   |      |                        |    | - 7 : VO_D[28]            |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 27| JTAG | FMUX_GPIO_R            | 0x0| IO JTAG_CPU_TCK function  |
	|   | _CPU | EG_IOCTRL_JTAG_CPU_TCK |    | select :                  |
	|   | _TCK | 0x0300_1068            |    |                           |
	|   | _TCK |                        |    | - 0 : CR_4WTCK (default)  |
	|   |      |                        |    | - 1 : CAM_MCLK1           |
	|   |      |                        |    | - 2 : PWM[6]              |
	|   |      |                        |    | - 3 : XGPIOA[18]          |
	|   |      |                        |    | - 4 : UART1_CTS           |
	|   |      |                        |    | - 5 : AUX1                |
	|   |      |                        |    | - 6 : UART1_RX            |
	|   |      |                        |    | - 7 : VO_D[29]            |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 28| IIC0\| FMUX_GP\               | 0x0| IO IIC0_SCL function      |
	|   | _SCL | IO_REG_IOCTRL_IIC0_SCL |    | select :                  |
	|   |      | 0x0300_1070            |    |                           |
	|   |      |                        |    | - 0 : CR_4WTDI (default)  |
	|   |      |                        |    | - 1 : UART1_TX            |
	|   |      |                        |    | - 2 : UART2_TX            |
	|   |      |                        |    | - 3 : XGPIOA[28]          |
	|   |      |                        |    | - 5 : WG0_D0              |
	|   |      |                        |    | - 7 : DBG[10]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 29| IIC0\| FMUX_GP\               | 0x0| IO IIC0_SDA function      |
	|   | _SDA | IO_REG_IOCTRL_IIC0_SDA |    | select :                  |
	|   |      | 0x0300_1074            |    |                           |
	|   |      |                        |    | - 0 : CR_4WTDO (default)  |
	|   |      |                        |    | - 1 : UART1_RX            |
	|   |      |                        |    | - 2 : UART2_RX            |
	|   |      |                        |    | - 3 : XGPIOA[29]          |
	|   |      |                        |    | - 5 : WG0_D1              |
	|   |      |                        |    | - 6 : WG1_D0              |
	|   |      |                        |    | - 7 : DBG[11]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 30| AUX0 | FMU\                   | 0x3| IO AUX0 function select : |
	|   |      | X_GPIO_REG_IOCTRL_AUX0 |    |                           |
	|   |      | 0x0300_1078            |    | - 0 : AUX0                |
	|   |      |                        |    | - 3 : XGPIOA[30] (default)|
	|   |      |                        |    | - 4 : IIS1_MCLK           |
	|   |      |                        |    | - 5 : VO_D[31]            |
	|   |      |                        |    | - 6 : WG1_D1              |
	|   |      |                        |    | - 7 : DBG[12]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 38|PWR   | FMUX_GPIO_R            | 0x0| IO PWR_VBAT_DET function  |
	|   |_VBAT | EG_IOCTRL_PWR_VBAT_DET |    | select :                  |
	|   |_DET  |                        |    |                           |
	|   |      | 0x0300_107C            |    | - 0 : PWR_VBAT_DET        |
	|   |      |                        |    |   (default)               |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 39|PWR\  | FMUX_GP\               | 0x0| IO PWR_RSTN function      |
	|   |_RSTN | IO_REG_IOCTRL_PWR_RSTN |    | select :                  |
	|   |      |                        |    |                           |
	|   |      | 0x0300_1080            |    | - 0 : PWR_RSTN (default)  |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 40|PWR\  | FMUX_GP\               | 0x0| IO PWR_SEQ1 function      |
	|   |_SEQ1 | IO_REG_IOCTRL_PWR_SEQ1 |    | select :                  |
	|   |      |                        |    |                           |
	|   |      | 0x0300_1084            |    | - 0 : PWR_SEQ1 (default)  |
	|   |      |                        |    | - 3 : PWR_GPIO[3]         |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 41|PWR\  | FMUX_GP\               | 0x0| IO PWR_SEQ2 function      |
	|   |_SEQ2 | IO_REG_IOCTRL_PWR_SEQ2 |    | select :                  |
	|   |      |                        |    |                           |
	|   |      | 0x0300_1088            |    | - 0 : PWR_SEQ2 (default)  |
	|   |      |                        |    | - 3 : PWR_GPIO[4]         |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 43|PWR   |FMUX_GPIO_REG_IOCTRL    | 0x0| IO PWR_WAKEUP0 function   |
	|   |_WAK  |_PWR_WAKEUP0            |    | select :                  |
	|   |EUP0  |0x0300_1090             |    |                           |
	|   |      |                        |    | - 0 : PWR_WAKEUP0(default)|
	|   |      |                        |    | - 1 : PWR_IR0             |
	|   |      |                        |    | - 2 : PWR_UART0_TX        |
	|   |      |                        |    | - 3 : PWR_GPIO[6]         |
	|   |      |                        |    | - 4 : UART1_TX            |
	|   |      |                        |    | - 5 : IIC4_SCL            |
	|   |      |                        |    | - 6 : EPHY_LNK_LED        |
	|   |      |                        |    | - 7 : WG2_D0              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 44| PWR\ |FMUX_GPIO               | 0x0| IO PWR_BUTTON1 function   |
	|   | _BUT |_REG_IOCTRL_PWR_BUTTON1 |    | select :                  |
	|   | TON1 |0x0300_1098             |    |                           |
	|   |      |                        |    | - 0 : PWR_BUTTON1(default)|
	|   |      |                        |    | - 3 : PWR_GPIO[8]         |
	|   |      |                        |    | - 4 : UART1_RX            |
	|   |      |                        |    | - 5 : IIC4_SDA            |
	|   |      |                        |    | - 6 : EPHY_SPD_LED        |
	|   |      |                        |    | - 7 : WG2_D1              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 45| XTAL\| FMUX_GP\               | 0x0| IO XTAL_XIN function      |
	|   | _XIN | IO_REG_IOCTRL_XTAL_XIN |    | select :                  |
	|   |      |                        |    |                           |
	|   |      | 0x0300_10A0            |    | - 0 : PWR_XTAL_CLKIN\     |
	|   |      |                        |    |   (default)               |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 47| PWR\ | FMUX_GPI               | 0x0| IO PWR_GPIO0 function     |
	|   | _\   | O_REG_IOCTRL_PWR_GPIO0 |    | select :                  |
	|   | GPIO0| 0x0300_10A4            |    |                           |
	|   |      |                        |    | - 0 : PWR_GPIO[0](default)|
	|   |      |                        |    | - 1 : UART2_TX            |
	|   |      |                        |    | - 2 : PWR_UART0_RX        |
	|   |      |                        |    | - 4 : PWM[8]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 48| PWR\ | FMUX_GPI               | 0x0| IO PWR_GPIO1 function     |
	|   | _\   | O_REG_IOCTRL_PWR_GPIO1 |    | select :                  |
	|   | GPIO1| 0x0300_10A8            |    |                           |
	|   |      |                        |    | - 0 : PWR_GPIO[1](default)|
	|   |      |                        |    | - 1 : UART2_RX            |
	|   |      |                        |    | - 3 : EPHY_LNK_LED        |
	|   |      |                        |    | - 4 : PWM[9]              |
	|   |      |                        |    | - 5 : PWR_IIC_SCL         |
	|   |      |                        |    | - 6 : IIC2_SCL            |
	|   |      |                        |    | - 7 : CR_SDA0             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 49| PWR\ | FMUX_GPI               | 0x0| IO PWR_GPIO2 function     |
	|   | _\   | O_REG_IOCTRL_PWR_GPIO2 |    | select :                  |
	|   | GPIO2| 0x0300_10AC            |    |                           |
	|   |      |                        |    | - 0 : PWR_GPIO[2](default)|
	|   |      |                        |    | - 2 : PWR_SECTICK         |
	|   |      |                        |    | - 3 : EPHY_SPD_LED        |
	|   |      |                        |    | - 4 : PWM[10]             |
	|   |      |                        |    | - 5 : PWR_IIC_SDA         |
	|   |      |                        |    | - 6 : IIC2_SDA            |
	|   |      |                        |    | - 7 : CR_2WTCK            |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 51| SD1\ |FMUX\                   | 0x6| IO SD1_D3 function select |
	|   | _D3  |_GPIO_REG_IOCTRL_SD1_D3 |    | :                         |
	|   |      |                        |    |                           |
	|   |      |0x0300_10D0             |    | - 0 : PWR_SD1_D3_VO32     |
	|   |      |                        |    | - 1 : SPI2_CS_X           |
	|   |      |                        |    | - 2 : IIC1_SCL            |
	|   |      |                        |    | - 3 : PWR_GPIO[18]        |
	|   |      |                        |    | - 4 : CAM_MCLK0           |
	|   |      |                        |    | - 5 : UART3_CTS           |
	|   |      |                        |    | - 6 : PWR_SPINOR1_CS_X    |
	|   |      |                        |    | - (default)               |
	|   |      |                        |    | - 7 : PWM[4]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 52| SD1\ |FMUX\                   | 0x6| IO SD1_D2 function select |
	|   | _D2  |_GPIO_REG_IOCTRL_SD1_D2 |    | :                         |
	|   |      |                        |    |                           |
	|   |      |0x0300_10D4             |    | - 0 : PWR_SD1_D2_VO33     |
	|   |      |                        |    | - 1 : IIC1_SCL            |
	|   |      |                        |    | - 2 : UART2_TX            |
	|   |      |                        |    | - 3 : PWR_GPIO[19]        |
	|   |      |                        |    | - 4 : CAM_MCLK0           |
	|   |      |                        |    | - 5 : UART3_TX            |
	|   |      |                        |    | - 6 : PWR_SPINOR1_HOLD_X  |
	|   |      |                        |    | - (default)               |
	|   |      |                        |    | - 7 : PWM[5]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 53| SD1\ |FMUX\                   | 0x6| IO SD1_D1 function select |
	|   | _D1  |_GPIO_REG_IOCTRL_SD1_D1 |    | :                         |
	|   |      |                        |    |                           |
	|   |      |0x0300_10D8             |    | - 0 : PWR_SD1_D1_VO34     |
	|   |      |                        |    | - 1 : IIC1_SDA            |
	|   |      |                        |    | - 2 : UART2_RX            |
	|   |      |                        |    | - 3 : PWR_GPIO[20]        |
	|   |      |                        |    | - 4 : CAM_MCLK1           |
	|   |      |                        |    | - 5 : UART3_RX            |
	|   |      |                        |    | - 6 : PWR_SPINOR1_WP_X    |
	|   |      |                        |    | - (default)               |
	|   |      |                        |    | - 7 : PWM[6]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 54| SD1\ |FMUX\                   | 0x6| IO SD1_D0 function select |
	|   | _D0  |_GPIO_REG_IOCTRL_SD1_D0 |    | :                         |
	|   |      |                        |    |                           |
	|   |      |0x0300_10DC             |    | - 0 : PWR_SD1_D0_VO35     |
	|   |      |                        |    | - 1 : SPI2_SDI            |
	|   |      |                        |    | - 2 : IIC1_SDA            |
	|   |      |                        |    | - 3 : PWR_GPIO[21]        |
	|   |      |                        |    | - 4 : CAM_MCLK1           |
	|   |      |                        |    | - 5 : UART3_RTS           |
	|   |      |                        |    | - 6 : PWR_SPINOR1_MISO    |
	|   |      |                        |    | - (default)               |
	|   |      |                        |    | - 7 : PWM[7]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 55| SD1\ | FMUX_G\                | 0x6| IO SD1_CMD function       |
	|   | _CMD | PIO_REG_IOCTRL_SD1_CMD |    | select :                  |
	|   |      |                        |    |                           |
	|   |      | 0x0300_10E0            |    | - 0 : PWR_SD1_CMD_VO36    |
	|   |      |                        |    | - 1 : SPI2_SDO            |
	|   |      |                        |    | - 2 : IIC3_SCL            |
	|   |      |                        |    | - 3 : PWR_GPIO[22]        |
	|   |      |                        |    | - 4 : CAM_VS0             |
	|   |      |                        |    | - 5 : EPHY_LNK_LED        |
	|   |      |                        |    | - 6 : PWR_SPINOR1_MOSI    |
	|   |      |                        |    | - (default)               |
	|   |      |                        |    | - 7 : PWM[8]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 56|SD1\  | FMUX_G\                | 0x6| IO SD1_CLK function       |
	|   |_CLK  | PIO_REG_IOCTRL_SD1_CLK |    | select :                  |
	|   |      |                        |    |                           |
	|   |      | 0x0300_10E4            |    | - 0 : PWR_SD1_CLK_VO37    |
	|   |      |                        |    | - 1 : SPI2_SCK            |
	|   |      |                        |    | - 2 : IIC3_SDA            |
	|   |      |                        |    | - 3 : PWR_GPIO[23]        |
	|   |      |                        |    | - 4 : CAM_HS0             |
	|   |      |                        |    | - 5 : EPHY_SPD_LED        |
	|   |      |                        |    | - 6 : PWR_SPINOR1_SCK     |
	|   |      |                        |    | - (default)               |
	|   |      |                        |    | - 7 : PWM[9]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 58|PWM0  | FMUX_GPI               | 0x3| IO PWM0_BUCK function     |
	|   |_BUCK | O_REG_IOCTRL_PWM0_BUCK |    | select :                  |
	|   |      |                        |    |                           |
	|   |      | 0x0300_10EC            |    | - 0 : PWM[0]              |
	|   |      |                        |    | - 3 : XGPIOB[0] (default) |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 59| ADC1 | FMU\                   | 0x3| IO ADC1 function select : |
	|   |      | X_GPIO_REG_IOCTRL_ADC1 |    |                           |
	|   |      |                        |    | - 3 : XGPIOB[3] (default) |
	|   |      | 0x0300_10F8            |    | - 4 : KEY_COL2            |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 60|USB   | FMUX_GPIO_R            | 0x0| IO USB_VBUS_DET function  |
	|   |_VBUS | EG_IOCTRL_USB_VBUS_DET |    | select :                  |
	|   |_DET  |                        |    |                           |
	|   |      | 0x0300_1108            |    | - 0 : USB_VBUS_DET        |
	|   |      |                        |    | - (default)               |
	|   |      |                        |    | - 3 : XGPIOB[6]           |
	|   |      |                        |    | - 4 : CAM_MCLK0           |
	|   |      |                        |    | - 5 : CAM_MCLK1           |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 62|PAD   |FMUX_GPIO               | 0x3| IO PAD_ETH_TXP function   |
	|   |_ETH  |_REG_IOCTRL_PAD_ETH_TXP |    | select :                  |
	|   |_TXP  |                        |    |                           |
	|   |___   |0x0300_1124             |    | - 1 : UART3_RX            |
	|   |EPHY  |                        |    | - 2 : IIC1_SCL            |
	|   |_RXN  |                        |    | - 3 : XGPIOB[25] (default)|
	|   |      |                        |    | - 4 : PWM[13]             |
	|   |      |                        |    | - 5 : CAM_MCLK0           |
	|   |      |                        |    | - 6 : SPI1_SDO            |
	|   |      |                        |    | - 7 : IIS2_LRCK           |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 63|PAD   |FMUX_GPIO               | 0x3| IO PAD_ETH_TXM function   |
	|   |_ETH  |_REG_IOCTRL_PAD_ETH_TXM |    | select :                  |
	|   |_TXM  |                        |    |                           |
	|   |___   |0x0300_1128             |    | - 1 : UART3_RTS           |
	|   |EPHY  |                        |    | - 2 : IIC1_SDA            |
	|   |_RXP  |                        |    | - 3 : XGPIOB[24] (default)|
	|   |      |                        |    | - 4 : PWM[12]             |
	|   |      |                        |    | - 5 : CAM_MCLK1           |
	|   |      |                        |    | - 6 : SPI1_SDI            |
	|   |      |                        |    | - 7 : IIS2_BCLK           |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 64|PAD   |FMUX_GPIO               | 0x3| IO PAD_ETH_RXP function   |
	|   |_ETH  |_REG_IOCTRL_PAD_ETH_RXP |    | select :                  |
	|   |_RXP  |                        |    |                           |
	|   |___   |0x0300_112C             |    | - 1 : UART3_TX            |
	|   |EPHY  |                        |    | - 2 : CAM_MCLK1           |
	|   |_TXN  |                        |    | - 3 : XGPIOB[27] (default)|
	|   |      |                        |    | - 4 : PWM[15]             |
	|   |      |                        |    | - 5 : CAM_HS0             |
	|   |      |                        |    | - 6 : SPI1_SCK            |
	|   |      |                        |    | - 7 : IIS2_DO             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 65|PAD   | FMUX_GPIO              | 0x3| IO PAD_ETH_RXM function   |
	|   |_ETH  | _REG_IOCTRL_PAD_ETH_RXM|    | select :                  |
	|   |_RXM  |                        |    |                           |
	|   |___   | 0x0300_1130            |    | - 1 : UART3_CTS           |
	|   |EPHY  |                        |    | - 2 : CAM_MCLK0           |
	|   |_TXP  |                        |    | - 3 : XGPIOB[26] (default)|
	|   |      |                        |    | - 4 : PWM[14]             |
	|   |      |                        |    | - 5 : CAM_VS0             |
	|   |      |                        |    | - 6 : SPI1_CS_X           |
	|   |      |                        |    | - 7 : IIS2_DI             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 72|PAD   | FMUX_GPIO_R            | 0x0| IO PAD_MIPIRX4N function  |
	|   |_MIPI | EG_IOCTRL_PAD_MIPIRX4N |    | select :                  |
	|   |RX4N  | 0x0300_116C            |    |                           |
	|   |      |                        |    | - 0 : CR_SCL0 (default)   |
	|   |      |                        |    | - 1 : VI0_CLK             |
	|   |      |                        |    | - 2 : VI1_D[13]           |
	|   |      |                        |    | - 3 : XGPIOC[2]           |
	|   |      |                        |    | - 4 : IIC1_SDA            |
	|   |      |                        |    | - 5 : CAM_MCLK0           |
	|   |      |                        |    | - 6 : KEY_ROW0            |
	|   |      |                        |    | - 7 : MUX_SPI1_SCK        |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 73|PAD   | FMUX_GPIO_R            | 0x0| IO PAD_MIPIRX4P function  |
	|   |_MIPI | EG_IOCTRL_PAD_MIPIRX4P |    | select :                  |
	|   |RX4P  | 0x0300_1170            |    |                           |
	|   |      |                        |    | - 0 : CR_SDA0 (default)   |
	|   |      |                        |    | - 1 : VI0_D[0]            |
	|   |      |                        |    | - 2 : VI1_D[14]           |
	|   |      |                        |    | - 3 : XGPIOC[3]           |
	|   |      |                        |    | - 4 : IIC1_SCL            |
	|   |      |                        |    | - 5 : CAM_MCLK1           |
	|   |      |                        |    | - 6 : KEY_ROW1            |
	|   |      |                        |    | - 7 : MUX_SPI1_CS         |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 74|PAD   | FMUX_GPIO_R            | 0x3| IO PAD_MIPIRX3N function  |
	|   |_MIPI | EG_IOCTRL_PAD_MIPIRX3N |    | select :                  |
	|   |RX3N  | 0x0300_1174            |    |                           |
	|   |      |                        |    | - 0 : CR_2WTMS            |
	|   |      |                        |    | - 1 : VI0_D[1]            |
	|   |      |                        |    | - 2 : VI1_D[15]           |
	|   |      |                        |    | - 3 : XGPIOC[4] (default) |
	|   |      |                        |    | - 4 : CAM_MCLK0           |
	|   |      |                        |    | - 7 : MUX_SPI1_MISO       |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 75|PAD   | FMUX_GPIO_R            | 0x3| IO PAD_MIPIRX3P function  |
	|   |_MIPI | EG_IOCTRL_PAD_MIPIRX3P |    | select :                  |
	|   |RX3P  | 0x0300_1178            |    |                           |
	|   |      |                        |    | - 0 : CR_2WTCK            |
	|   |      |                        |    | - 1 : VI0_D[2]            |
	|   |      |                        |    | - 2 : VI1_D[16]           |
	|   |      |                        |    | - 3 : XGPIOC[5] (default) |
	|   |      |                        |    | - 7 : MUX_SPI1_MOSI       |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 76|PAD   | FMUX_GPIO_R            | 0x3| IO PAD_MIPIRX2N function  |
	|   |_MIPI | EG_IOCTRL_PAD_MIPIRX2N |    | select :                  |
	|   |RX2N  | 0x0300_117C            |    |                           |
	|   |      |                        |    | - 1 : VI0_D[3]            |
	|   |      |                        |    | - 2 : VO_D[10]            |
	|   |      |                        |    | - 3 : XGPIOC[6] (default) |
	|   |      |                        |    | - 4 : VI1_D[17]           |
	|   |      |                        |    | - 5 : IIC4_SCL            |
	|   |      |                        |    | - 7 : DBG[6]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 77|PAD   | FMUX_GPIO_R            | 0x3| IO PAD_MIPIRX2P function  |
	|   |_MIPI | EG_IOCTRL_PAD_MIPIRX2P |    | select :                  |
	|   |RX2P  | 0x0300_1180            |    |                           |
	|   |      |                        |    | - 1 : VI0_D[4]            |
	|   |      |                        |    | - 2 : VO_D[9]             |
	|   |      |                        |    | - 3 : XGPIOC[7] (default) |
	|   |      |                        |    | - 4 : VI1_D[18]           |
	|   |      |                        |    | - 5 : IIC4_SDA            |
	|   |      |                        |    | - 7 : DBG[7]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 78|PAD   | FMUX_GPIO_R            | 0x3| IO PAD_MIPIRX1N function  |
	|   |_MIPI | EG_IOCTRL_PAD_MIPIRX1N |    | select :                  |
	|   |RX1N  | 0x0300_1184            |    |                           |
	|   |      |                        |    | - 1 : VI0_D[5]            |
	|   |      |                        |    | - 2 : VO_D[8]             |
	|   |      |                        |    | - 3 : XGPIOC[8] (default) |
	|   |      |                        |    | - 6 : KEY_ROW3            |
	|   |      |                        |    | - 7 : DBG[8]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 79|PAD   | FMUX_GPIO_R            | 0x3| IO PAD_MIPIRX1P function  |
	|   |_MIPI | EG_IOCTRL_PAD_MIPIRX1P |    | select :                  |
	|   |RX1P  | 0x0300_1188            |    |                           |
	|   |      |                        |    | - 1 : VI0_D[6]            |
	|   |      |                        |    | - 2 : VO_D[7]             |
	|   |      |                        |    | - 3 : XGPIOC[9] (default) |
	|   |      |                        |    | - 4 : IIC1_SDA            |
	|   |      |                        |    | - 6 : KEY_ROW2            |
	|   |      |                        |    | - 7 : DBG[9]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 80|PAD   | FMUX_GPIO_R            | 0x3| IO PAD_MIPIRX0N function  |
	|   |_MIPI | EG_IOCTRL_PAD_MIPIRX0N |    | select :                  |
	|   |RX0N  | 0x0300_118C            |    |                           |
	|   |      |                        |    | - 1 : VI0_D[7]            |
	|   |      |                        |    | - 2 : VO_D[6]             |
	|   |      |                        |    | - 3 : XGPIOC[10] (default)|
	|   |      |                        |    | - 4 : IIC1_SCL            |
	|   |      |                        |    | - 5 : CAM_MCLK1           |
	|   |      |                        |    | - 7 : DBG[10]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 81|PAD   | FMUX_GPIO_R            | 0x3| IO PAD_MIPIRX0P function  |
	|   |_MIPI | EG_IOCTRL_PAD_MIPIRX0P |    | select :                  |
	|   |RX0P  | 0x0300_1190            |    |                           |
	|   |      |                        |    | - 1 : VI0_D[8]            |
	|   |      |                        |    | - 2 : VO_D[5]             |
	|   |      |                        |    | - 3 : XGPIOC[11] (default)|
	|   |      |                        |    | - 4 : CAM_MCLK0           |
	|   |      |                        |    | - 7 : DBG[11]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 83|PAD   | FMUX_GPIO_RE           | 0x3| IO PAD_MIPI_TXM2 function |
	|   |_MIPI | G_IOCTRL_PAD_MIPI_TXM2 |    | select :                  |
	|   |_TXM2 | 0x0300_11A4            |    |                           |
	|   |      |                        |    | - 0 : CR_SDA0             |
	|   |      |                        |    | - 1 : VI0_D[13]           |
	|   |      |                        |    | - 2 : VO_D[0]             |
	|   |      |                        |    | - 3 : XGPIOC[16] (default)|
	|   |      |                        |    | - 4 : IIC1_SDA            |
	|   |      |                        |    | - 5 : PWM[8]              |
	|   |      |                        |    | - 6 : SPI0_SCK            |
	|   |      |                        |    | - 7 : SD1_D2              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 84|PAD   | FMUX_GPIO_RE           | 0x3| IO PAD_MIPI_TXP2 function |
	|   |_MIPI | G_IOCTRL_PAD_MIPI_TXP2 |    | select :                  |
	|   |_TXP2 | 0x0300_11A8            |    |                           |
	|   |      |                        |    | - 0 : CR_SCL0             |
	|   |      |                        |    | - 1 : VI0_D[14]           |
	|   |      |                        |    | - 2 : VO_CLK0             |
	|   |      |                        |    | - 3 : XGPIOC[17] (default)|
	|   |      |                        |    | - 4 : IIC1_SCL            |
	|   |      |                        |    | - 5 : PWM[9]              |
	|   |      |                        |    | - 6 : SPI0_CS_X           |
	|   |      |                        |    | - 7 : SD1_D3              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 85|PAD   | FMUX_GPIO_RE           | 0x3| IO PAD_MIPI_TXM1 function |
	|   |_MIPI | G_IOCTRL_PAD_MIPI_TXM1 |    | select :                  |
	|   |_TXM1 | 0x0300_11AC            |    |                           |
	|   |      |                        |    | - 0 : CR_2WTMS            |
	|   |      |                        |    | - 1 : VI0_D[11]           |
	|   |      |                        |    | - 2 : VO_D[2]             |
	|   |      |                        |    | - 3 : XGPIOC[14] (default)|
	|   |      |                        |    | - 4 : IIC2_SDA            |
	|   |      |                        |    | - 5 : PWM[10]             |
	|   |      |                        |    | - 6 : SPI0_SDO            |
	|   |      |                        |    | - 7 : DBG[14]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 86|PAD   | FMUX_GPIO_RE           | 0x3| IO PAD_MIPI_TXP1 function |
	|   |_MIPI | G_IOCTRL_PAD_MIPI_TXP1 |    | select :                  |
	|   |_TXP1 | 0x0300_11B0            |    |                           |
	|   |      |                        |    | - 0 : CR_2WTCK            |
	|   |      |                        |    | - 1 : VI0_D[12]           |
	|   |      |                        |    | - 2 : VO_D[1]             |
	|   |      |                        |    | - 3 : XGPIOC[15] (default)|
	|   |      |                        |    | - 4 : IIC2_SCL            |
	|   |      |                        |    | - 5 : PWM[11]             |
	|   |      |                        |    | - 6 : SPI0_SDI            |
	|   |      |                        |    | - 7 : DBG[15]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 87|PAD   | FMUX_GPIO_RE           | 0x3| IO PAD_MIPI_TXM0 function |
	|   |_MIPI | G_IOCTRL_PAD_MIPI_TXM0 |    | select :                  |
	|   |_TXM0 | 0x0300_11B4            |    |                           |
	|   |      |                        |    | - 1 : VI0_D[9]            |
	|   |      |                        |    | - 2 : VO_D[4]             |
	|   |      |                        |    | - 3 : XGPIOC[12] (default)|
	|   |      |                        |    | - 4 : CAM_MCLK1           |
	|   |      |                        |    | - 5 : PWM[14]             |
	|   |      |                        |    | - 6 : CAM_VS0             |
	|   |      |                        |    | - 7 : DBG[12]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 88|PAD   | FMUX_GPIO_RE           | 0x3| IO PAD_MIPI_TXP0 function |
	|   |_MIPI | G_IOCTRL_PAD_MIPI_TXP0 |    | select :                  |
	|   |_TXP0 | 0x0300_11B8            |    |                           |
	|   |      |                        |    | - 1 : VI0_D[10]           |
	|   |      |                        |    | - 2 : VO_D[3]             |
	|   |      |                        |    | - 3 : XGPIOC[13] (default)|
	|   |      |                        |    | - 4 : CAM_MCLK0           |
	|   |      |                        |    | - 5 : PWM[15]             |
	|   |      |                        |    | - 6 : CAM_HS0             |
	|   |      |                        |    | - 7 : DBG[13]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 2 |PAD   | FMUX_GPIO_REG_I        | 0x3| IO PAD_AUD_AINL_MIC       |
	|   |_AUD  | OCTRL_PAD_AUD_AINL_MIC |    | function select :         |
	|   |_AINL | 0x0300_11BC            |    |                           |
	|   |_MIC  |                        |    | - 3 : XGPIOC[23] (default)|
	|   |      |                        |    | - 4 : IIS1_BCLK           |
	|   |      |                        |    | - 5 : IIS2_BCLK           |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 4 |PAD   | FMUX_GPIO_RE           | 0x3| IO PAD_AUD_AOUTR function |
	|   |_AUD  | G_IOCTRL_PAD_AUD_AOUTR |    | select :                  |
	|   |_AOUTR| 0x0300_11C8            |    |                           |
	|   |      |                        |    | - 3 : XGPIOC[24] (default)|
	|   |      |                        |    | - 4 : IIS1_DI             |
	|   |      |                        |    | - 5 : IIS2_DO             |
	|   |      |                        |    | - 6 : IIS1_DO             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 67| GPIO | FMUX_GP                | 0x3| IO GPIO_RTX function      |
	|   | _RTX | IO_REG_IOCTRL_GPIO_RTX |    | select :                  |
	|   | ___  | 0x0300_11CC            |    |                           |
	|   | EPHY |                        |    | - 3 : XGPIOB[23] (default)|
	|   | _RTX |                        |    | - 4 : PWM[1]              |
	|   |      |                        |    | - 5 : CAM_MCLK0           |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| 35| GPIO | FMUX_G\                | 0x3| IO GPIO_ZQ function       |
	|   | _ZQ  | PIO_REG_IOCTRL_GPIO_ZQ |    | select :                  |
	|   | ___  | 0x0300_11D0            |    |                           |
	|   | PAD  |                        |    | - 3 : PWR_GPIO[24]\       |
	|   | _ZQ  |                        |    |   (default)               |
	|   |      |                        |    | - 4 : PWM[2]              |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| #\|PKG   | FMUX_GPI               | 0x0| IO PKG_TYPE0 function     |
	| N\|_TYPE0| O_REG_IOCTRL_PKG_TYPE0 |    | select :                  |
	| /\|      | 0x0300_1104            |    |                           |
	| A |      |                        |    | - 0 : PKG_TYPE0 (default) |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| #\|PKG   | FMUX_GPI               | 0x0| IO PKG_TYPE1 function     |
	| N\|_TYPE1| O_REG_IOCTRL_PKG_TYPE1 |    | select :                  |
	| /\|      | 0x0300_110C            |    |                           |
	| A |      |                        |    | - 0 : PKG_TYPE1 (default) |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| #\|PKG   | FMUX_GPI               | 0x0| IO PKG_TYPE2 function     |
	| N\|_TYPE2| O_REG_IOCTRL_PKG_TYPE2 |    | select :                  |
	| /\|      | 0x0300_1110            |    |                           |
	| A |      |                        |    | - 0 : PKG_TYPE2 (default) |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| #\|MUX   | FMUX_GPIO_RE           | 0x3| IO MUX_SPI1_MISO function |
	| N\|_SPI1 | G_IOCTRL_MUX_SPI1_MISO |    | select :                  |
	| /\|_MISO | 0x0300_1114            |    |                           |
	| A |      |                        |    | - 1 : UART3_RTS           |
	|   |      |                        |    | - 2 : IIC1_SDA            |
	|   |      |                        |    | - 3 : XGPIOB[8] (default) |
	|   |      |                        |    | - 4 : PWM[9]              |
	|   |      |                        |    | - 5 : KEY_COL1            |
	|   |      |                        |    | - 6 : SPI1_SDI            |
	|   |      |                        |    | - 7 : DBG[14]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| #\|MUX   | FMUX_GPIO_RE           | 0x3| IO MUX_SPI1_MOSI function |
	| N\|_SPI1 | G_IOCTRL_MUX_SPI1_MOSI |    | select :                  |
	| /\|_MOSI | 0x0300_1118            |    |                           |
	| A |      |                        |    | - 1 : UART3_RX            |
	|   |      |                        |    | - 2 : IIC1_SCL            |
	|   |      |                        |    | - 3 : XGPIOB[7] (default) |
	|   |      |                        |    | - 4 : PWM[8]              |
	|   |      |                        |    | - 5 : KEY_COL0            |
	|   |      |                        |    | - 6 : SPI1_SDO            |
	|   |      |                        |    | - 7 : DBG[13]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| #\|MUX   | FMUX_GPIO              | 0x3| IO MUX_SPI1_CS function   |
	| N\|_SPI1 | _REG_IOCTRL_MUX_SPI1_CS|    | select :                  |
	| /\|_CS   | 0x0300_111C            |    |                           |
	| A |      |                        |    | - 1 : UART3_CTS           |
	|   |      |                        |    | - 2 : CAM_MCLK0           |
	|   |      |                        |    | - 3 : XGPIOB[10] (default)|
	|   |      |                        |    | - 4 : PWM[11]             |
	|   |      |                        |    | - 5 : KEY_ROW3            |
	|   |      |                        |    | - 6 : SPI1_CS_X           |
	|   |      |                        |    | - 7 : DBG[16]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
	| #\|MUX   | FMUX_GPIO_R            | 0x3| IO MUX_SPI1_SCK function  |
	| N\|_SPI1 | EG_IOCTRL_MUX_SPI1_SCK |    | select :                  |
	| /\|_SCK  | 0x0300_1120            |    |                           |
	| A |      |                        |    | - 1 : UART3_TX            |
	|   |      |                        |    | - 2 : CAM_MCLK1           |
	|   |      |                        |    | - 3 : XGPIOB[9] (default) |
	|   |      |                        |    | - 4 : PWM[10]             |
	|   |      |                        |    | - 5 : KEY_ROW2            |
	|   |      |                        |    | - 6 : SPI1_SCK            |
	|   |      |                        |    | - 7 : DBG[15]             |
	|   |      |                        |    | - Others : Reserved       |
	+---+------+------------------------+----+---------------------------+
