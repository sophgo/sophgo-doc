.. _table_pins_description:
.. table:: Pin information table
	:widths: 1 3 2 2 4 3

	======  ================  =================  =======  ==================  ====
	PinNum  Pin Name          IO Type            IOGroup  PowerDomain         Note
	======  ================  =================  =======  ==================  ====
	6       SD0_CLK           18OD33 IO          G10      VDDIO_SD0_EMMC      \
	7       SD0_CMD           18OD33 IO          G10      VDDIO_SD0_EMMC      \
	8       SD0_D0            18OD33 IO          G10      VDDIO_SD0_EMMC      \
	10      SD0_D1            18OD33 IO          G10      VDDIO_SD0_EMMC      \
	11      SD0_D2            18OD33 IO          G10      VDDIO_SD0_EMMC      \
	12      SD0_D3            18OD33 IO          G10      VDDIO_SD0_EMMC      \
	14      SD0_CD            18OD33 IO          G7       VDDIO_SD0_EMMC      \
	15      SD0_PWR_EN        18OD33 IO          G7       VDDIO_SD0_EMMC      \
	17      SPK_EN            18OD33 IO          G7       VDDIO_SD0_EMMC      \
	18      UART0_TX          18OD33 IO          G7       VDDIO_SD0_EMMC      \
	19      UART0_RX          18OD33 IO          G7       VDDIO_SD0_EMMC      \
	20      EMMC_DAT2         18OD33 IO          G7       VDDIO_SD0_EMMC      \
	21      EMMC_CLK          18OD33 IO          G7       VDDIO_SD0_EMMC      \
	22      EMMC_DAT0         18OD33 IO          G7       VDDIO_SD0_EMMC      \
	23      EMMC_DAT3         18OD33 IO          G7       VDDIO_SD0_EMMC      \
	24      EMMC_CMD          18OD33 IO          G7       VDDIO_SD0_EMMC      \
	25      EMMC_DAT1         18OD33 IO          G7       VDDIO_SD0_EMMC      \
	26      JTAG_CPU_TMS      18OD33 IO          G7       VDDIO_SD0_EMMC      \
	27      JTAG_CPU_TCK      18OD33 IO          G7       VDDIO_SD0_EMMC      \
	28      IIC0_SCL          18OD33 IO          G7       VDDIO_SD0_EMMC      \
	29      IIC0_SDA          18OD33 IO          G7       VDDIO_SD0_EMMC      \
	30      AUX0              18OD33 IO          G7       VDDIO_SD0_EMMC      \
	38      PWR_VBAT_DET      1.8V GPIO          GRTC     VDDIO_RTC           \
	39      PWR_RSTN          1.8V GPIO          GRTC     VDDIO_RTC           \
	40      PWR_SEQ1          1.8V GPIO          GRTC     VDDIO_RTC           \
	41      PWR_SEQ2          1.8V GPIO          GRTC     VDDIO_RTC           \
	43      PWR_WAKEUP0       1.8V GPIO          GRTC     VDDIO_RTC           \
	44      PWR_BUTTON1       1.8V GPIO          GRTC     VDDIO_RTC           \
	45      XTAL_XIN          Xtal               GRTC     VDDIO_RTC           \
	47      PWR_GPIO0         1.8V GPIO          GRTC     VDDIO_RTC           \
	48      PWR_GPIO1         1.8V GPIO          GRTC     VDDIO_RTC           \
	49      PWR_GPIO2         1.8V GPIO          GRTC     VDDIO_RTC           \
	51      SD1_D3            18OD33 IO          GRTC     VDDIO_SD1           SD1_D3 or VO[32] Check 0x0502_70E4
	52      SD1_D2            18OD33 IO          GRTC     VDDIO_SD1           SD1_D2 or VO[33] Check 0x0502_70E4
	53      SD1_D1            18OD33 IO          GRTC     VDDIO_SD1           SD1_D1 or VO[34] Check 0x0502_70E4
	54      SD1_D0            18OD33 IO          GRTC     VDDIO_SD1           SD1_D0 or VO[35] Check 0x0502_70E4
	55      SD1_CMD           18OD33 IO          GRTC     VDDIO_SD1           SD1_CMD or VO[36] Check 0x0502_70E4
	56      SD1_CLK           18OD33 IO          GRTC     VDDIO_SD1           SD1_CLK or VO[37] Check 0x0502_70E4
	58      PWM0_BUCK         1.8V GPIO          G1       VDD18A_USB          \
	                                                      _PLL_ETH
	59      ADC1              1.8V GPIO          G1       VDD18A_USB          \
	                                                      _PLL_ETH
	60      USB_VBUS_DET      1.8V GPIO          G1       VDD18A_USB          \
	                                                      _PLL_ETH
	62      PAD_ETH_TXP       ETH GPIO (1.8V)    \        VDD18A_USB          \
	        ___EPHY_RXN                                   _PLL_ETH
	63      PAD_ETH_TXM       ETH GPIO (1.8V)    \        VDD18A_USB          \
	        ___EPHY_RXP                                   _PLL_ETH
	64      PAD_ETH_RXP       ETH GPIO (1.8V)    \        VDD18A_USB          \
	        ___EPHY_TXN                                   _PLL_ETH
	65      PAD_ETH_RXM       ETH GPIO (1.8V)    \        VDD18A_USB          \
	        ___EPHY_TXP                                   _PLL_ETH
	72      PAD_MIPIRX4N      1.8V GPIO          G12      VDD18A_MIPI         \
	73      PAD_MIPIRX4P      1.8V GPIO          G12      VDD18A_MIPI         \
	74      PAD_MIPIRX3N      1.8V GPIO          G12      VDD18A_MIPI         \
	75      PAD_MIPIRX3P      1.8V GPIO          G12      VDD18A_MIPI         \
	76      PAD_MIPIRX2N      1.8V GPIO          G12      VDD18A_MIPI         \
	77      PAD_MIPIRX2P      1.8V GPIO          G12      VDD18A_MIPI         \
	78      PAD_MIPIRX1N      1.8V GPIO          G12      VDD18A_MIPI         \
	79      PAD_MIPIRX1P      1.8V GPIO          G12      VDD18A_MIPI         \
	80      PAD_MIPIRX0N      1.8V GPIO          G12      VDD18A_MIPI         \
	81      PAD_MIPIRX0P      1.8V GPIO          G12      VDD18A_MIPI         \
	83      PAD_MIPI_TXM2     1.8V GPIO          G12      VDD18A_MIPI         \
	84      PAD_MIPI_TXP2     1.8V GPIO          G12      VDD18A_MIPI         \
	85      PAD_MIPI_TXM1     1.8V GPIO          G12      VDD18A_MIPI         \
	86      PAD_MIPI_TXP1     1.8V GPIO          G12      VDD18A_MIPI         \
	87      PAD_MIPI_TXM0     1.8V GPIO          G12      VDD18A_MIPI         \
	88      PAD_MIPI_TXP0     1.8V GPIO          G12      VDD18A_MIPI         \
	2       PAD_AUD_AINL      AUDIO GPIO (1.8V)  \        VDD18A_MIPI         \
	        _MIC
	4       PAD_AUD_AOUTR     AUDIO GPIO (1.8V)  \        VDD18A_MIPI         \
	67      GPIO_RTX          1.8V GPIO          G12      VDD18A_USB          \
	        ___EPHY_RTX                                   _PLL_ETH
	35      GPIO_ZQ           1.8V GPIO          GRTC     VDDIO_RTC           \
	        ___PAD_ZQ
	#N/A    PKG_TYPE0         1.8V GPIO          G1       VDD18A_USB          no pin out
	                                                      _PLL_ETH
	#N/A    PKG_TYPE1         1.8V GPIO          G1       VDD18A_USB          no pin out
	                                                      _PLL_ETH
	#N/A    PKG_TYPE2         1.8V GPIO          G1       VDD18A_USB          no pin out
	                                                      _PLL_ETH
	#N/A    MUX_SPI1_MISO     NA                 NA       NA                  Result is feed to PAD_MIPIRX3N func7
	#N/A    MUX_SPI1_MOSI     NA                 NA       NA                  Result is feed to PAD_MIPIRX3P func7
	#N/A    MUX_SPI1_CS       NA                 NA       NA                  Result is feed to PAD_MIPIRX4P func7
	#N/A    MUX_SPI1_SCK      NA                 NA       NA                  Result is feed to PAD_MIPIRX4N func7
	======  ================  =================  =======  ==================  ====

