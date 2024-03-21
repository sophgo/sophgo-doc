ADC
^^^

.. only:: sg2002

	.. _table_inf_signal_pin_fmux_adc_sg2002:
	.. table:: ADC
		:widths: 2 1 1 1 3

		+---------+---------+---------+--------+-----------------------+
		| Signal  |Direction| PinName |Function| Function select       |
		| Name    |         |         |Number  | register              |
		+=========+=========+=========+========+=======================+
		| (ADC1)  | I       | ADC1    | 0      | FMUX\                 |
		|         |         |         |        | _GPIO_REG_IOCTRL_ADC1 |
		|         |         |         |        | 0x0300_10F8           |
		+---------+---------+---------+--------+-----------------------+

.. only:: sg2000

	.. _table_inf_signal_pin_fmux_adc_sg2000:
	.. table:: ADC
		:widths: 2 1 1 1 3

		+---------+---------+---------+--------+-----------------------+
		| Signal  |Direction| PinName |Function| Function select       |
		| Name    |         |         |Number  | register              |
		+=========+=========+=========+========+=======================+
		| (ADC1)  | I       | ADC1    | 0      | FMUX\                 |
		|         |         |         |        | _GPIO_REG_IOCTRL_ADC1 |
		|         |         |         |        | 0x0300_10F8           |
		+---------+---------+---------+--------+-----------------------+
		| (ADC2)  | I       | ADC2    | 0      | FMUX\                 |
		|         |         |         |        | _GPIO_REG_IOCTRL_ADC1 |
		|         |         |         |        | 0x0300_10F8           |
		+---------+---------+---------+--------+-----------------------+
		| (ADC3)  | I       | ADC3    | 0      | FMUX\                 |
		|         |         |         |        | _GPIO_REG_IOCTRL_ADC1 |
		|         |         |         |        | 0x0300_10F8           |
		+---------+---------+---------+--------+-----------------------+
	
No-die domain ADC
^^^^^^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_nodia_domain_adc:
.. table:: No-die domain ADC
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| PWR\    | I       | PW      | 0      | FMUX_GPIO             |
	| _GPIO[2\|         | R_GPIO2 |        | _REG_IOCTRL_PWR_GPIO2 |
	| ](PWRSA |         |         |        | 0x0300_10AC           |
	| R.VIN1) |         |         |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I       | PW      | 0      | FMUX_GPIO             |
	| _GPIO[1\|         | R_GPIO1 |        | _REG_IOCTRL_PWR_GPIO1 |
	| ](PWRSA |         |         |        | 0x0300_10A8           |
	| R1.VIN2)|         |         |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I       | PWR_V   | 0      | FMUX_GPIO_RE          |
	| _VBAT_DE|         | BAT_DET |        | G_IOCTRL_PWR_VBAT_DET |
	| T(PWRSA |         |         |        | 0x0300_107C           |
	| R.VIN3) |         |         |        |                       |
	+---------+---------+---------+--------+-----------------------+


Audio
^^^^^

.. only:: sg2002

	.. _table_inf_signal_pin_fmux_audio_sg2002:
	.. table:: Audio
		:widths: 2 1 1 1 3

		+---------+---------+---------+--------+-----------------------+
		| Signal  |Direction| PinName |Function| Function select       |
		| Name    |         |         |Number  | register              |
		+=========+=========+=========+========+=======================+
		| (PAD\   | I       | PA      | 0      | FMUX_GPIO_REG_IO      |
		| _AUD_AI |         | D_AUD_A |        | CTRL_PAD_AUD_AINL_MIC |
		| NL_MIC) |         | INL_MIC |        | 0x0300_11BC           |
		+---------+---------+---------+--------+-----------------------+
		| (\      | O       | PAD_AU  | 0      | FMUX_GPIO_REG_IO      |
		| PAD_AUD\|         | D_AOUTR |        | CTRL_PAD_AUD_AOUTR    |
		| _AOUTR) |         |         |        | 0x0300_11C8           |
		+---------+---------+---------+--------+-----------------------+

.. only:: sg2000

	.. _table_inf_signal_pin_fmux_audio_sg2000:
	.. table:: Audio
		:widths: 2 1 1 1 3

		+---------+---------+---------+--------+-----------------------+
		| Signal  |Direction| PinName |Function| Function select       |
		| Name    |         |         |Number  | register              |
		+=========+=========+=========+========+=======================+
		| (PAD\   | I       | PA      | 0      | FMUX_GPIO_REG_IO      |
		| _AUD_AI |         | D_AUD_A |        | CTRL_PAD_AUD_AINL_MIC |
		| NL_MIC) |         | INL_MIC |        | 0x0300_11BC           |
		+---------+---------+---------+--------+-----------------------+
		| (PAD\   | I       | PA      | 0      | FMUX_GPIO_REG_IO      |
		| _AUD_AI |         | D_AUD_A |        | CTRL_PAD_AUD_AINR_MIC |
		| NR_MIC) |         | INR_MIC |        | 0x0300_11BC           |
		+---------+---------+---------+--------+-----------------------+
		| (\      | O       | PAD_AU  | 0      | FMUX_GPIO_REG_IO      |
		| PAD_AUD\|         | D_AOUTL |        | CTRL_PAD_AUD_AOUTL    |
		| _AOUTL) |         |         |        | 0x0300_11C8           |
		+---------+---------+---------+--------+-----------------------+
		| (\      | O       | PAD_AU  | 0      | FMUX_GPIO_REG_IO      |
		| PAD_AUD\|         | D_AOUTR |        | CTRL_PAD_AUD_AOUTR    |
		| _AOUTR) |         |         |        | 0x0300_11C8           |
		+---------+---------+---------+--------+-----------------------+


Ethernet
^^^^^^^^

.. _table_inf_signal_pin_fmux_ethernet:
.. table:: Ethernet
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| (PAD_E\ | I/O     | PAD     | 0      | FMUX_GPIO_R           |
	| TH_RXM) |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXM |
	|         |         | M\_\__E |        | 0x0300_1130           |
	|         |         | PHY_TXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_E\ | I/O     | PAD     | 0      | FMUX_GPIO_R           |
	| TH_RXP) |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXP |
	|         |         | P\_\__E |        | 0x0300_112C           |
	|         |         | PHY_TXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_E\ | I/O     | PAD     | 0      | FMUX_GPIO_R           |
	| TH_TXM) |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXM |
	|         |         | M\_\__E |        | 0x0300_1128           |
	|         |         | PHY_RXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_E\ | I/O     | PAD     | 0      | FMUX_GPIO_R           |
	| TH_TXP) |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXP |
	|         |         | P\_\__E |        | 0x0300_1124           |
	|         |         | PHY_RXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| EPHY\   | O       | SD0_CLK | 6      | FMUX_GP               |
	| _LNK_LED|         |         |        | IO_REG_IOCTRL_SD0_CLK |
	|         |         |         |        | 0x0300_101C           |
	+---------+---------+---------+--------+-----------------------+
	| EPHY\   | O       | PWR     | 6      | FMUX_GPIO_R           |
	| _LNK_LED|         | _WAKEUP0|        | EG_IOCTRL_PWR_WAKEUP0 |
	|         |         |         |        | 0x0300_1090           |
	+---------+---------+---------+--------+-----------------------+
	| EPHY\   | O       | SD1_CMD | 5      | FMUX_GP               |
	| _LNK_LED|         |         |        | IO_REG_IOCTRL_SD1_CMD |
	|         |         |         |        | 0x0300_10E0           |
	+---------+---------+---------+--------+-----------------------+
	| EPHY\   | O       | PW      | 3      | FMUX_GPIO             |
	| _LNK_LED|         | R_GPIO1 |        | _REG_IOCTRL_PWR_GPIO1 |
	|         |         |         |        | 0x0300_10A8           |
	+---------+---------+---------+--------+-----------------------+
	| EPHY\   | O       | SD0_CMD | 6      | FMUX_GP               |
	| _SPD_LED|         |         |        | IO_REG_IOCTRL_SD0_CMD |
	|         |         |         |        | 0x0300_1020           |
	+---------+---------+---------+--------+-----------------------+
	| EPHY\   | O       | PWR     | 6      | FMUX_GPIO_R           |
	| _SPD_LED|         | _BUTTON1|        | EG_IOCTRL_PWR_BUTTON1 |
	|         |         |         |        | 0x0300_1098           |
	+---------+---------+---------+--------+-----------------------+
	| EPHY\   | O       | SD1_CLK | 5      | FMUX_GP               |
	| _SPD_LED|         |         |        | IO_REG_IOCTRL_SD1_CLK |
	|         |         |         |        | 0x0300_10E4           |
	+---------+---------+---------+--------+-----------------------+
	| EPHY\   | O       | PW      | 3      | FMUX_GPIO             |
	| _SPD_LED|         | R_GPIO2 |        | _REG_IOCTRL_PWR_GPIO2 |
	|         |         |         |        | 0x0300_10AC           |
	+---------+---------+---------+--------+-----------------------+

DSI/LVDS
^^^^^^^^

.. _table_inf_signal_pin_fmux_dsi_lvds:
.. table:: DSI/LVDS
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| (\      | I/O     | PAD_MI  | 0      | FMUX_GPIO_REG_IO      |
	| PAD_MIP\|         | PI_TXM0 |        | CTRL_PAD_MIPI_TXM0    |
	| I_TXM0) |         |         |        | 0x0300_11B4           |
	+---------+---------+---------+--------+-----------------------+
	| (\      | I/O     | PAD_MI  | 0      | FMUX_GPIO_REG_IO      |
	| PAD_MIP\|         | PI_TXP0 |        | CTRL_PAD_MIPI_TXP0    |
	| I_TXP0) |         |         |        | 0x0300_11B8           |
	+---------+---------+---------+--------+-----------------------+
	| (\      | I/O     | PAD_MI  | 3      | FMUX_GPIO_REG_IO      |
	| PAD_MIP\|         | PI_TXM1 |        | CTRL_PAD_MIPI_TXM1    |
	| I_TXM1) |         |         |        | 0x0300_11AC           |
	+---------+---------+---------+--------+-----------------------+
	| (\      | I/O     | PAD_MI  | 3      | FMUX_GPIO_REG_IO      |
	| PAD_MIP\|         | PI_TXP1 |        | CTRL_PAD_MIPI_TXP1    |
	| I_TXP1) |         |         |        | 0x0300_11B0           |
	+---------+---------+---------+--------+-----------------------+
	| (\      | I/O     | PAD_MI  | 3      | FMUX_GPIO_REG_IO      |
	| PAD_MIP\|         | PI_TXM2 |        | CTRL_PAD_MIPI_TXM2    |
	| I_TXM2) |         |         |        | 0x0300_11A4           |
	+---------+---------+---------+--------+-----------------------+
	| (\      | I/O     | PAD_MI  | 3      | FMUX_GPIO_REG_IO      |
	| PAD_MIP\|         | PI_TXP2 |        | CTRL_PAD_MIPI_TXP2    |
	| I_TXP2) |         |         |        | 0x0300_11A8           |
	+---------+---------+---------+--------+-----------------------+

CSI/sLVDS/HiSPI
^^^^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_csi:
.. table:: CSI/sLVDS/HiSPI
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| (PAD_MI\| I/O     | PAD_M   | 0      | FMUX_GPIO_RE          |
	| PIRX0N) |         | IPIRX0N |        | G_IOCTRL_PAD_MIPIRX0N |
	|         |         |         |        | 0x0300_118C           |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_MI\| I/O     | PAD_M   | 0      | FMUX_GPIO_RE          |
	| PIRX0P) |         | IPIRX0P |        | G_IOCTRL_PAD_MIPIRX0P |
	|         |         |         |        | 0x0300_1190           |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_MI\| I/O     | PAD_M   | 0      | FMUX_GPIO_RE          |
	| PIRX1N) |         | IPIRX1N |        | G_IOCTRL_PAD_MIPIRX1N |
	|         |         |         |        | 0x0300_1184           |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_MI\| I/O     | PAD_M   | 0      | FMUX_GPIO_RE          |
	| PIRX1P) |         | IPIRX1P |        | G_IOCTRL_PAD_MIPIRX1P |
	|         |         |         |        | 0x0300_1188           |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_MI\| I/O     | PAD_M   | 0      | FMUX_GPIO_RE          |
	| PIRX2N) |         | IPIRX2N |        | G_IOCTRL_PAD_MIPIRX2N |
	|         |         |         |        | 0x0300_117C           |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_MI\| I/O     | PAD_M   | 0      | FMUX_GPIO_RE          |
	| PIRX2P) |         | IPIRX2P |        | G_IOCTRL_PAD_MIPIRX2P |
	|         |         |         |        | 0x0300_1180           |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_MI\| I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIRX3N) |         | IPIRX3N |        | G_IOCTRL_PAD_MIPIRX3N |
	|         |         |         |        | 0x0300_1174           |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_MI\| I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIRX3P) |         | IPIRX3P |        | G_IOCTRL_PAD_MIPIRX3P |
	|         |         |         |        | 0x0300_1178           |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_MI\| I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIRX4N) |         | IPIRX4N |        | G_IOCTRL_PAD_MIPIRX4N |
	|         |         |         |        | 0x0300_116C           |
	+---------+---------+---------+--------+-----------------------+
	| (PAD_MI\| I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIRX4P) |         | IPIRX4P |        | G_IOCTRL_PAD_MIPIRX4P |
	|         |         |         |        | 0x0300_1170           |
	+---------+---------+---------+--------+-----------------------+

Aux clockout
^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_aux_clockout:
.. table:: Aux clockout
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| AUX0    | O       | AUX0    | 0      | FMUX                  |
	|         |         |         |        | _GPIO_REG_IOCTRL_AUX0 |
	|         |         |         |        | 0x0300_1078           |
	+---------+---------+---------+--------+-----------------------+
	| AUX0    | O       | SD0_D1  | 2      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D1 |
	|         |         |         |        | 0x0300_1028           |
	+---------+---------+---------+--------+-----------------------+
	| AUX0    | O       | U       | 5      | FMUX_GPI              |
	|         |         | ART0_RX |        | O_REG_IOCTRL_UART0_RX |
	|         |         |         |        | 0x0300_1044           |
	+---------+---------+---------+--------+-----------------------+
	| AUX0    | O       | JTAG    | 5      | FMUX_GPIO_RE          |
	|         |         | _CPU_TMS|        | G_IOCTRL_JTAG_CPU_TMS |
	|         |         |         |        | 0x0300_1064           |
	+---------+---------+---------+--------+-----------------------+
	| AUX1    | O       | SD0_D2  | 2      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D2 |
	|         |         |         |        | 0x0300_102C           |
	+---------+---------+---------+--------+-----------------------+
	| AUX1    | O       | U       | 5      | FMUX_GPI              |
	|         |         | ART0_TX |        | O_REG_IOCTRL_UART0_TX |
	|         |         |         |        | 0x0300_1040           |
	+---------+---------+---------+--------+-----------------------+
	| AUX1    | O       | JTAG    | 5      | FMUX_GPIO_RE          |
	|         |         | _CPU_TCK|        | G_IOCTRL_JTAG_CPU_TCK |
	|         |         |         |        | 0x0300_1068           |
	+---------+---------+---------+--------+-----------------------+


Camera Interface
^^^^^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_camdra:
.. table:: Camera Interface
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| CAM_HS0 | O       | SD1_CLK | 4      | FMUX_GP               |
	|         |         |         |        | IO_REG_IOCTRL_SD1_CLK |
	|         |         |         |        | 0x0300_10E4           |
	+---------+---------+---------+--------+-----------------------+
	| CAM_HS0 | O       | PAD_MI  | 6      | FMUX_GPIO_REG         |
	|         |         | PI_TXP0 |        | _IOCTRL_PAD_MIPI_TXP0 |
	|         |         |         |        | 0x0300_11B8           |
	+---------+---------+---------+--------+-----------------------+
	| CAM_HS0 | O       | PAD     | 5      | FMUX_GPIO_R           |
	|         |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXP |
	|         |         | P\_\__E |        | 0x0300_112C           |
	|         |         | PHY_TXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD_MI  | 4      | FMUX_GPIO_REG         |
	| M_MCLK0 |         | PI_TXP0 |        | _IOCTRL_PAD_MIPI_TXP0 |
	|         |         |         |        | 0x0300_11B8           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | SD0_D3  | 1      | FMUX_G                |
	| M_MCLK0 |         |         |        | PIO_REG_IOCTRL_SD0_D3 |
	|         |         |         |        | 0x0300_1030           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | U       | 1      | FMUX_GPI              |
	| M_MCLK0 |         | ART0_RX |        | O_REG_IOCTRL_UART0_RX |
	|         |         |         |        | 0x0300_1044           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | JTAG    | 1      | FMUX_GPIO_RE          |
	| M_MCLK0 |         | _CPU_TMS|        | G_IOCTRL_JTAG_CPU_TMS |
	|         |         |         |        | 0x0300_1064           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | SD1_D3  | 4      | FMUX_G                |
	| M_MCLK0 |         |         |        | PIO_REG_IOCTRL_SD1_D3 |
	|         |         |         |        | 0x0300_10D0           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | SD1_D2  | 4      | FMUX_G                |
	| M_MCLK0 |         |         |        | PIO_REG_IOCTRL_SD1_D2 |
	|         |         |         |        | 0x0300_10D4           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | USB_V   | 4      | FMUX_GPIO_RE          |
	| M_MCLK0 |         | BUS_DET |        | G_IOCTRL_USB_VBUS_DET |
	|         |         |         |        | 0x0300_1108           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD_M   | 4      | FMUX_GPIO_RE          |
	| M_MCLK0 |         | IPIRX3N |        | G_IOCTRL_PAD_MIPIRX3N |
	|         |         |         |        | 0x0300_1174           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD_M   | 4      | FMUX_GPIO_RE          |
	| M_MCLK0 |         | IPIRX0P |        | G_IOCTRL_PAD_MIPIRX0P |
	|         |         |         |        | 0x0300_1190           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | MUX     | 2      | FMUX_GPIO_R           |
	| M_MCLK0 |         | _SPI1_CS|        | EG_IOCTRL_MUX_SPI1_CS |
	|         |         |         |        | 0x0300_111C           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD     | 2      | FMUX_GPIO_R           |
	| M_MCLK0 |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXM |
	|         |         | M\_\__E |        | 0x0300_1130           |
	|         |         | PHY_TXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD     | 5      | FMUX_GPIO_R           |
	| M_MCLK0 |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXP |
	|         |         | P\_\__E |        | 0x0300_1124           |
	|         |         | PHY_RXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD_M   | 5      | FMUX_GPIO_RE          |
	| M_MCLK0 |         | IPIRX4N |        | G_IOCTRL_PAD_MIPIRX4N |
	|         |         |         |        | 0x0300_116C           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | GPIO_RT | 5      | FMUX_GPI              |
	| M_MCLK0 |         | X\_\__E |        | O_REG_IOCTRL_GPIO_RTX |
	|         |         | PHY_RTX |        | 0x0300_11CC           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | SD1_D1  | 4      | FMUX_G                |
	| M_MCLK1 |         |         |        | PIO_REG_IOCTRL_SD1_D1 |
	|         |         |         |        | 0x0300_10D8           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | SD1_D0  | 4      | FMUX_G                |
	| M_MCLK1 |         |         |        | PIO_REG_IOCTRL_SD1_D0 |
	|         |         |         |        | 0x0300_10DC           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD_MI  | 4      | FMUX_GPIO_REG         |
	| M_MCLK1 |         | PI_TXM0 |        | _IOCTRL_PAD_MIPI_TXM0 |
	|         |         |         |        | 0x0300_11B4           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | MUX_S   | 2      | FMUX_GPIO_RE          |
	| M_MCLK1 |         | PI1_SCK |        | G_IOCTRL_MUX_SPI1_SCK |
	|         |         |         |        | 0x0300_1120           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD     | 2      | FMUX_GPIO_R           |
	| M_MCLK1 |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXP |
	|         |         | P\_\__E |        | 0x0300_112C           |
	|         |         | PHY_TXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | USB_V   | 5      | FMUX_GPIO_RE          |
	| M_MCLK1 |         | BUS_DET |        | G_IOCTRL_USB_VBUS_DET |
	|         |         |         |        | 0x0300_1108           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD     | 5      | FMUX_GPIO_R           |
	| M_MCLK1 |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXM |
	|         |         | M\_\__E |        | 0x0300_1128           |
	|         |         | PHY_RXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD_M   | 5      | FMUX_GPIO_RE          |
	| M_MCLK1 |         | IPIRX4P |        | G_IOCTRL_PAD_MIPIRX4P |
	|         |         |         |        | 0x0300_1170           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | PAD_M   | 5      | FMUX_GPIO_RE          |
	| M_MCLK1 |         | IPIRX0N |        | G_IOCTRL_PAD_MIPIRX0N |
	|         |         |         |        | 0x0300_118C           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | SD0_D0  | 1      | FMUX_G                |
	| M_MCLK1 |         |         |        | PIO_REG_IOCTRL_SD0_D0 |
	|         |         |         |        | 0x0300_1024           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | U       | 1      | FMUX_GPI              |
	| M_MCLK1 |         | ART0_TX |        | O_REG_IOCTRL_UART0_TX |
	|         |         |         |        | 0x0300_1040           |
	+---------+---------+---------+--------+-----------------------+
	| CA\     | O       | JTAG    | 1      | FMUX_GPIO_RE          |
	| M_MCLK1 |         | _CPU_TCK|        | G_IOCTRL_JTAG_CPU_TCK |
	|         |         |         |        | 0x0300_1068           |
	+---------+---------+---------+--------+-----------------------+
	| CAM_VS0 | O       | SD1_CMD | 4      | FMUX_GP               |
	|         |         |         |        | IO_REG_IOCTRL_SD1_CMD |
	|         |         |         |        | 0x0300_10E0           |
	+---------+---------+---------+--------+-----------------------+
	| CAM_VS0 | O       | PAD_MI  | 6      | FMUX_GPIO_REG_IO      |
	|         |         | PI_TXM0 |        | CTRL_PAD_MIPI_TXM0    |
	|         |         |         |        | 0x0300_11B4           |
	+---------+---------+---------+--------+-----------------------+
	| CAM_VS0 | O       | PAD     | 5      | FMUX_GPIO_R           |
	|         |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXM |
	|         |         | M\_\__E |        | 0x0300_1130           |
	|         |         | PHY_TXP |        |                       |
	+---------+---------+---------+--------+-----------------------+

Parallel Video Out
^^^^^^^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_parallel_videoout:
.. table:: Parallel Video Out
	:widths: 1 1 2 1 5

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| VO_CLK0 | O       | PAD_MI  | 2      | FMUX_GPIO_REG         |
	|         |         | PI_TXP2 |        | _IOCTRL_PAD_MIPI_TXP2 |
	|         |         |         |        | 0x0300_11A8           |
	|         |         |         |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| VO_D[0] | O       | PAD_MI  | 2      | FMUX_GPIO_REG         |
	|         |         | PI_TXM2 |        | _IOCTRL_PAD_MIPI_TXM2 |
	|         |         |         |        | 0x0300_11A4           |
	+---------+---------+---------+--------+-----------------------+
	| VO_D[1] | O       | PAD_MI  | 2      | FMUX_GPIO_REG         |
	|         |         | PI_TXP1 |        | _IOCTRL_PAD_MIPI_TXP1 |
	|         |         |         |        | 0x0300_11B0           |
	+---------+---------+---------+--------+-----------------------+
	| VO_D[2] | O       | PAD_MI  | 2      | FMUX_GPIO_REG         |
	|         |         | PI_TXM1 |        | _IOCTRL_PAD_MIPI_TXM1 |
	|         |         |         |        | 0x0300_11AC           |
	+---------+---------+---------+--------+-----------------------+
	| VO_D[3] | O       | PAD_MI  | 2      | FMUX_GPIO_REG         |
	|         |         | PI_TXP0 |        | _IOCTRL_PAD_MIPI_TXP0 |
	|         |         |         |        | 0x0300_11B8           |
	+---------+---------+---------+--------+-----------------------+
	| VO_D[4] | O       | PAD_MI  | 2      | FMUX_GPIO_REG         |
	|         |         | PI_TXM0 |        | _IOCTRL_PAD_MIPI_TXM0 |
	|         |         |         |        | 0x0300_11B4           |
	+---------+---------+---------+--------+-----------------------+
	| VO_D[5] | O       | PAD_M   | 2      | FMUX_GPIO_RE          |
	|         |         | IPIRX0P |        | G_IOCTRL_PAD_MIPIRX0P |
	|         |         |         |        | 0x0300_1190           |
	+---------+---------+---------+--------+-----------------------+
	| VO_D[6] | O       | PAD_M   | 2      | FMUX_GPIO_RE          |
	|         |         | IPIRX0N |        | G_IOCTRL_PAD_MIPIRX0N |
	|         |         |         |        | 0x0300_118C           |
	+---------+---------+---------+--------+-----------------------+
	| VO_D[7] | O       | PAD_M   | 2      | FMUX_GPIO_RE          |
	|         |         | IPIRX1P |        | G_IOCTRL_PAD_MIPIRX1P |
	|         |         |         |        | 0x0300_1188           |
	+---------+---------+---------+--------+-----------------------+
	| VO_D[8] | O       | PAD_M   | 2      | FMUX_GPIO_RE          |
	|         |         | IPIRX1N |        | G_IOCTRL_PAD_MIPIRX1N |
	|         |         |         |        | 0x0300_1184           |
	+---------+---------+---------+--------+-----------------------+
	| VO_D[9] | O       | PAD_M   | 2      | FMUX_GPIO_RE          |
	|         |         | IPIRX2P |        | G_IOCTRL_PAD_MIPIRX2P |
	|         |         |         |        | 0x0300_1180           |
	+---------+---------+---------+--------+-----------------------+
	| V       | O       | PAD_M   | 2      | FMUX_GPIO_RE          |
	| O_D[10] |         | IPIRX2N |        | G_IOCTRL_PAD_MIPIRX2N |
	|         |         |         |        | 0x0300_117C           |
	+---------+---------+---------+--------+-----------------------+
	| V       | O       | JTAG    | 7      | FMUX_GPIO_RE          |
	| O_D[28] |         | _CPU_TMS|        | G_IOCTRL_JTAG_CPU_TMS |
	|         |         |         |        | 0x0300_1064           |
	+---------+---------+---------+--------+-----------------------+
	| V       | O       | JTAG    | 7      | FMUX_GPIO_RE          |
	| O_D[29] |         | _CPU_TCK|        | G_IOCTRL_JTAG_CPU_TCK |
	|         |         |         |        | 0x0300_1068           |
	+---------+---------+---------+--------+-----------------------+
	| V       | O       | AUX0    | 5      | FMUX                  |
	| O_D[31] |         |         |        | _GPIO_REG_IOCTRL_AUX0 |
	|         |         |         |        | 0x0300_1078           |
	+---------+---------+---------+--------+-----------------------+
	| V       | O       | SD1_D3  | 0      | FMUX_G                |
	| O_D[32] |         |         |        | PIO_REG_IOCTRL_SD1_D3 |
	|         |         |         |        | 0x0300_10D0           |
	+---------+---------+---------+--------+-----------------------+
	| V       | O       | SD1_D2  | 0      | FMUX_G                |
	| O_D[33] |         |         |        | PIO_REG_IOCTRL_SD1_D2 |
	|         |         |         |        | 0x0300_10D4           |
	+---------+---------+---------+--------+-----------------------+
	| V       | O       | SD1_D1  | 0      | FMUX_G                |
	| O_D[34] |         |         |        | PIO_REG_IOCTRL_SD1_D1 |
	|         |         |         |        | 0x0300_10D8           |
	+---------+---------+---------+--------+-----------------------+
	| V       | O       | SD1_D0  | 0      | FMUX_G                |
	| O_D[35] |         |         |        | PIO_REG_IOCTRL_SD1_D0 |
	|         |         |         |        | 0x0300_10DC           |
	+---------+---------+---------+--------+-----------------------+
	| V       | O       | SD1_CMD | 0      | FMUX_GP               |
	| O_D[36] |         |         |        | IO_REG_IOCTRL_SD1_CMD |
	|         |         |         |        | 0x0300_10E0           |
	+---------+---------+---------+--------+-----------------------+
	| V       | O       | SD1_CLK | 0      | FMUX_GP               |
	| O_D[37] |         |         |        | IO_REG_IOCTRL_SD1_CLK |
	|         |         |         |        | 0x0300_10E4           |
	+---------+---------+---------+--------+-----------------------+

Parallel Video In
^^^^^^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_parallel_videoin:
.. table:: Parallel Video In
	:widths: 1 1 1 1 5

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| VI0_CLK | I       | PAD_M   | 1      | FMUX_GPIO_RE          |
	|         |         | IPIRX4N |        | G_IOCTRL_PAD_MIPIRX4N |
	|         |         |         |        | 0x0300_116C           |
	|         |         |         |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| V       | I       | PAD_M   | 1      | FMUX_GPIO_RE          |
	| I0_D[0] |         | IPIRX4P |        | G_IOCTRL_PAD_MIPIRX4P |
	|         |         |         |        | 0x0300_1170           |
	+---------+---------+---------+--------+-----------------------+
	| V       | I       | PAD_M   | 1      | FMUX_GPIO_RE          |
	| I0_D[1] |         | IPIRX3N |        | G_IOCTRL_PAD_MIPIRX3N |
	|         |         |         |        | 0x0300_1174           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_MI  | 1      | FMUX_GPIO_REG         |
	| 0_D[10] |         | PI_TXP0 |        | _IOCTRL_PAD_MIPI_TXP0 |
	|         |         |         |        | 0x0300_11B8           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_MI  | 1      | FMUX_GPIO_REG         |
	| 0_D[11] |         | PI_TXM1 |        | _IOCTRL_PAD_MIPI_TXM1 |
	|         |         |         |        | 0x0300_11AC           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_MI  | 1      | FMUX_GPIO_REG         |
	| 0_D[12] |         | PI_TXP1 |        | _IOCTRL_PAD_MIPI_TXP1 |
	|         |         |         |        | 0x0300_11B0           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_MI  | 1      | FMUX_GPIO_REG         |
	| 0_D[13] |         | PI_TXM2 |        | _IOCTRL_PAD_MIPI_TXM2 |
	|         |         |         |        | 0x0300_11A4           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_MI  | 1      | FMUX_GPIO_REG         |
	| 0_D[14] |         | PI_TXP2 |        | _IOCTRL_PAD_MIPI_TXP2 |
	|         |         |         |        | 0x0300_11A8           |
	+---------+---------+---------+--------+-----------------------+
	| V       | I       | PAD_M   | 1      | FMUX_GPIO_RE          |
	| I0_D[2] |         | IPIRX3P |        | G_IOCTRL_PAD_MIPIRX3P |
	|         |         |         |        | 0x0300_1178           |
	+---------+---------+---------+--------+-----------------------+
	| V       | I       | PAD_M   | 1      | FMUX_GPIO_RE          |
	| I0_D[3] |         | IPIRX2N |        | G_IOCTRL_PAD_MIPIRX2N |
	|         |         |         |        | 0x0300_117C           |
	+---------+---------+---------+--------+-----------------------+
	| V       | I       | PAD_M   | 1      | FMUX_GPIO_RE          |
	| I0_D[4] |         | IPIRX2P |        | G_IOCTRL_PAD_MIPIRX2P |
	|         |         |         |        | 0x0300_1180           |
	+---------+---------+---------+--------+-----------------------+
	| V       | I       | PAD_M   | 1      | FMUX_GPIO_RE          |
	| I0_D[5] |         | IPIRX1N |        | G_IOCTRL_PAD_MIPIRX1N |
	|         |         |         |        | 0x0300_1184           |
	+---------+---------+---------+--------+-----------------------+
	| V       | I       | PAD_M   | 1      | FMUX_GPIO_RE          |
	| I0_D[6] |         | IPIRX1P |        | G_IOCTRL_PAD_MIPIRX1P |
	|         |         |         |        | 0x0300_1188           |
	+---------+---------+---------+--------+-----------------------+
	| V       | I       | PAD_M   | 1      | FMUX_GPIO_RE          |
	| I0_D[7] |         | IPIRX0N |        | G_IOCTRL_PAD_MIPIRX0N |
	|         |         |         |        | 0x0300_118C           |
	+---------+---------+---------+--------+-----------------------+
	| V       | I       | PAD_M   | 1      | FMUX_GPIO_RE          |
	| I0_D[8] |         | IPIRX0P |        | G_IOCTRL_PAD_MIPIRX0P |
	|         |         |         |        | 0x0300_1190           |
	+---------+---------+---------+--------+-----------------------+
	| V       | I       | PAD_MI  | 1      | FMUX_GPIO_REG         |
	| I0_D[9] |         | PI_TXM0 |        | _IOCTRL_PAD_MIPI_TXM0 |
	|         |         |         |        | 0x0300_11B4           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_M   | 2      | FMUX_GPIO_RE          |
	| 1_D[13] |         | IPIRX4N |        | G_IOCTRL_PAD_MIPIRX4N |
	|         |         |         |        | 0x0300_116C           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_M   | 2      | FMUX_GPIO_RE          |
	| 1_D[14] |         | IPIRX4P |        | G_IOCTRL_PAD_MIPIRX4P |
	|         |         |         |        | 0x0300_1170           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_M   | 2      | FMUX_GPIO_RE          |
	| 1_D[15] |         | IPIRX3N |        | G_IOCTRL_PAD_MIPIRX3N |
	|         |         |         |        | 0x0300_1174           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_M   | 2      | FMUX_GPIO_RE          |
	| 1_D[16] |         | IPIRX3P |        | G_IOCTRL_PAD_MIPIRX3P |
	|         |         |         |        | 0x0300_1178           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_M   | 4      | FMUX_GPIO_RE          |
	| 1_D[17] |         | IPIRX2N |        | G_IOCTRL_PAD_MIPIRX2N |
	|         |         |         |        | 0x0300_117C           |
	+---------+---------+---------+--------+-----------------------+
	| VI      | I       | PAD_M   | 4      | FMUX_GPIO_RE          |
	| 1_D[18] |         | IPIRX2P |        | G_IOCTRL_PAD_MIPIRX2P |
	|         |         |         |        | 0x0300_1180           |
	+---------+---------+---------+--------+-----------------------+

eMMC
^^^^

.. _table_inf_signal_pin_fmux_emmc:
.. table:: eMMC
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| E\      | O       | E       | 0      | FMUX_GPI              |
	| MMC_CLK |         | MMC_CLK |        | O_REG_IOCTRL_EMMC_CLK |
	|         |         |         |        | 0x0300_1050           |
	+---------+---------+---------+--------+-----------------------+
	| E\      | I/O     | E       | 0      | FMUX_GPI              |
	| MMC_CMD |         | MMC_CMD |        | O_REG_IOCTRL_EMMC_CMD |
	|         |         |         |        | 0x0300_105C           |
	+---------+---------+---------+--------+-----------------------+
	| EMMC\   | I/O     | EM      | 0      | FMUX_GPIO             |
	| _DAT[0] |         | MC_DAT0 |        | _REG_IOCTRL_EMMC_DAT0 |
	|         |         |         |        | 0x0300_1054           |
	+---------+---------+---------+--------+-----------------------+
	| EMMC\   | I/O     | EM      | 0      | FMUX_GPIO             |
	| _DAT[1] |         | MC_DAT1 |        | _REG_IOCTRL_EMMC_DAT1 |
	|         |         |         |        | 0x0300_1060           |
	+---------+---------+---------+--------+-----------------------+
	| EMMC\   | I/O     | EM      | 0      | FMUX_GPIO             |
	| _DAT[2] |         | MC_DAT2 |        | _REG_IOCTRL_EMMC_DAT2 |
	|         |         |         |        | 0x0300_104C           |
	+---------+---------+---------+--------+-----------------------+
	| EMMC\   | I/O     | EM      | 0      | FMUX_GPIO             |
	| _DAT[3] |         | MC_DAT3 |        | _REG_IOCTRL_EMMC_DAT3 |
	|         |         |         |        | 0x0300_1058           |
	+---------+---------+---------+--------+-----------------------+


SPI_NAND
^^^^^^^^

.. _table_inf_signal_pin_fmux_spi_nand:
.. table:: SPI_NAND
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| SPIN\   | O       | E       | 2      | FMUX_GPI              |
	| AND_CLK |         | MMC_CLK |        | O_REG_IOCTRL_EMMC_CLK |
	|         |         |         |        | 0x0300_1050           |
	+---------+---------+---------+--------+-----------------------+
	| SPI\    | O       | EM      | 2      | FMUX_GPIO             |
	| NAND_CS |         | MC_DAT1 |        | _REG_IOCTRL_EMMC_DAT1 |
	|         |         |         |        | 0x0300_1060           |
	+---------+---------+---------+--------+-----------------------+
	| SPINA\  | I/O     | EM      | 2      | FMUX_GPIO             |
	| ND_HOLD |         | MC_DAT2 |        | _REG_IOCTRL_EMMC_DAT2 |
	|         |         |         |        | 0x0300_104C           |
	+---------+---------+---------+--------+-----------------------+
	| SPINA\  | I/O     | E       | 2      | FMUX_GPI              |
	| ND_MISO |         | MMC_CMD |        | O_REG_IOCTRL_EMMC_CMD |
	|         |         |         |        | 0x0300_105C           |
	+---------+---------+---------+--------+-----------------------+
	| SPINA\  | I/O     | EM      | 2      | FMUX_GPIO             |
	| ND_MOSI |         | MC_DAT0 |        | _REG_IOCTRL_EMMC_DAT0 |
	|         |         |         |        | 0x0300_1054           |
	+---------+---------+---------+--------+-----------------------+
	| SPI\    | I/O     | EM      | 2      | FMUX_GPIO             |
	| NAND_WP |         | MC_DAT3 |        | _REG_IOCTRL_EMMC_DAT3 |
	|         |         |         |        | 0x0300_1058           |
	+---------+---------+---------+--------+-----------------------+

SPI_NOR
^^^^^^^

.. _table_inf_signal_pin_fmux_spi_nor:
.. table:: SPI_NOR
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| SPIN\   | O       | EM      | 1      | FMUX_GPIO             |
	| OR_CS_X |         | MC_DAT1 |        | _REG_IOCTRL_EMMC_DAT1 |
	|         |         |         |        | 0x0300_1060           |
	+---------+---------+---------+--------+-----------------------+
	| SPINOR\ | I/O     | EM      | 1      | FMUX_GPIO             |
	| _HOLD_X |         | MC_DAT2 |        | _REG_IOCTRL_EMMC_DAT2 |
	|         |         |         |        | 0x0300_104C           |
	+---------+---------+---------+--------+-----------------------+
	| SPIN\   | I/O     | E       | 1      | FMUX_GPI              |
	| OR_MISO |         | MMC_CMD |        | O_REG_IOCTRL_EMMC_CMD |
	|         |         |         |        | 0x0300_105C           |
	+---------+---------+---------+--------+-----------------------+
	| SPIN\   | I/O     | EM      | 1      | FMUX_GPIO             |
	| OR_MOSI |         | MC_DAT0 |        | _REG_IOCTRL_EMMC_DAT0 |
	|         |         |         |        | 0x0300_1054           |
	+---------+---------+---------+--------+-----------------------+
	| SPI\    | O       | E       | 1      | FMUX_GPI              |
	| NOR_SCK |         | MMC_CLK |        | O_REG_IOCTRL_EMMC_CLK |
	|         |         |         |        | 0x0300_1050           |
	+---------+---------+---------+--------+-----------------------+
	| SPIN\   | I/O     | EM      | 1      | FMUX_GPIO             |
	| OR_WP_X |         | MC_DAT3 |        | _REG_IOCTRL_EMMC_DAT3 |
	|         |         |         |        | 0x0300_1058           |
	+---------+---------+---------+--------+-----------------------+

I2C
^^^

.. _table_inf_signal_pin_fmux_i2c:
.. table:: I2C
	:widths: 1 1 1 1 2

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	|IIC1_SCL | I/O     | PAD_M   | 4      | FMUX_GPIO_REG         |
	|         |         | IPIRX4P |        | _IOCTRL_PAD_MIPIRX4P  |
	|         |         |         |        | 0x0300_1170           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SCL | I/O     | PAD_M   | 4      | FMUX_GPIO_REG_IO      |
	|         |         | IPIRX0N |        | CTRL_PAD_MIPIRX0N     |
	|         |         |         |        | 0x0300_118C           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SCL | I/O     | SD0_CMD | 1      | FMUX_GPIO             |
	|         |         |         |        | _REG_IOCTRL_SD0_CMD   |
	|         |         |         |        | 0x0300_1020           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SCL | I/O     | SD0_D2  | 1      | FMUX_GPIO             |
	|         |         |         |        | _REG_IOCTRL_SD0_D2    |
	|         |         |         |        | 0x0300_102C           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SCL | I/O     | PAD_MI  | 4      | FMUX_GPIO_REG         |
	|         |         | PI_TXP2 |        | _IOCTRL_PAD_MIPI_TXP2 |
	|         |         |         |        | 0x0300_11A8           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SCL | I/O     | SD1_D3  | 2      | FMUX_GPIO             |
	|         |         |         |        | _REG_IOCTRL_SD1_D3    |
	|         |         |         |        | 0x0300_10D0           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SCL | I/O     | MUX_SP  | 2      | FMUX_GPIO_REG         |
	|         |         | I1_MOSI |        | _IOCTRL_MUX_SPI1_MOSI |
	|         |         |         |        | 0x0300_1118           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SCL | I/O     | PAD     | 2      | FMUX_GPIO_REG         |
	|         |         | _ETH_TX |        | _IOCTRL_PAD_ETH_TXP   |
	|         |         | P___E   |        | 0x0300_1124           |
	|         |         | PHY_RXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SCL | I/O     | SD1_D2  | 1      | FMUX_GPIO             |
	|         |         |         |        | _REG_IOCTRL_SD1_D2    |
	|         |         |         |        | 0x0300_10D4           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SDA | I/O     | PAD_M   | 4      | FMUX_GPIO_REG         |
	|         |         | IPIRX4N |        | _IOCTRL_PAD_MIPIRX4N  |
	|         |         |         |        | 0x0300_116C           |
	+---------+---------+---------+--------+-----------------------+

To be continued ......


.. _table_inf_signal_pin_fmux_i2c_2:
.. table:: I2C (continued)
	:widths: 1 1 1 1 2

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	|IIC1_SDA | I/O     | PAD_M   | 4      | FMUX_GPIO_REG         |
	|         |         | IPIRX1P |        | _IOCTRL_PAD_MIPIRX1P  |
	|         |         |         |        | 0x0300_1188           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SDA | I/O     | SD0_CLK | 1      | FMUX_GPIO_REG         |
	|         |         |         |        | _IOCTRL_SD0_CLK       |
	|         |         |         |        | 0x0300_101C           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SDA | I/O     | SD0_D1  | 1      | FMUX_GPIO_REG         |
	|         |         |         |        | _IOCTRL_SD0_D1        |
	|         |         |         |        | 0x0300_1028           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SDA | I/O     | PAD_MI  | 4      | FMUX_GPIO_REG         |
	|         |         | PI_TXM2 |        | _IOCTRL_PAD_MIPI_TXM2 |
	|         |         |         |        | 0x0300_11A4           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SDA | I/O     | SD1_D0  | 2      | FMUX_GPIO_REG         |
	|         |         |         |        | _IOCTRL_SD1_D0        |
	|         |         |         |        | 0x0300_10DC           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SDA | I/O     | MUX_SP  | 2      | FMUX_GPIO_REG         |
	|         |         | I1_MISO |        | _IOCTRL_MUX_SPI1_MISO |
	|         |         |         |        | 0x0300_1114           |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SDA | I/O     | PAD     | 2      | FMUX_GPIO_REG         |
	|         |         | _ETH_TX |        | _IOCTRL_PAD_ETH_TXM   |
	|         |         | M\_\__E |        | 0x0300_1128           |
	|         |         | PHY_RXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	|IIC1_SDA | I/O     | SD1_D1  | 1      | FMUX_GPIO_REG         |
	|         |         |         |        | _IOCTRL_SD1_D1        |
	|         |         |         |        | 0x0300_10D8           |
	+---------+---------+---------+--------+-----------------------+
	|IIC2_SCL | I/O     | PAD_MI  | 4      | FMUX_GPIO_REG         |
	|         |         | PI_TXP1 |        | _IOCTRL_PAD_MIPI_TXP1 |
	|         |         |         |        | 0x0300_11B0           |
	+---------+---------+---------+--------+-----------------------+
	|IIC2_SCL | I/O     | PW      | 6      | FMUX_GPIO_REG         |
	|         |         | R_GPIO1 |        | _IOCTRL_PWR_GPIO1     |
	|         |         |         |        | 0x0300_10A8           |
	+---------+---------+---------+--------+-----------------------+
	|IIC2_SDA | I/O     | PAD_MI  | 4      | FMUX_GPIO_REG         |
	|         |         | PI_TXM1 |        | _IOCTRL_PAD_MIPI_TXM1 |
	|         |         |         |        | 0x0300_11AC           |
	+---------+---------+---------+--------+-----------------------+
	|IIC2_SDA | I/O     | PW      | 6      | FMUX_GPIO_REG         |
	|         |         | R_GPIO2 |        | _IOCTRL_PWR_GPIO2     |
	|         |         |         |        | 0x0300_10AC           |
	+---------+---------+---------+--------+-----------------------+
	|IIC3_SCL | I/O     | SD1_CMD | 2      | FMUX_GPIO_REG         |
	|         |         |         |        | _IOCTRL_SD1_CMD       |
	|         |         |         |        | 0x0300_10E0           |
	+---------+---------+---------+--------+-----------------------+
	|IIC3_SDA | I/O     | SD1_CLK | 2      | FMUX_GPIO_REG         |
	|         |         |         |        | _IOCTRL_SD1_CLK       |
	|         |         |         |        | 0x0300_10E4           |
	+---------+---------+---------+--------+-----------------------+
	|IIC4_SCL | I/O     | PWR     | 5      | FMUX_GPIO_REG         |
	|         |         | _WAKEUP0|        | _IOCTRL_PWR_WAKEUP0   |
	|         |         |         |        | 0x0300_1090           |
	+---------+---------+---------+--------+-----------------------+
	|IIC4_SCL | I/O     | PAD_M   | 5      | FMUX_GPIO_REG         |
	|         |         | IPIRX2N |        | _IOCTRL_PAD_MIPIRX2N  |
	|         |         |         |        | 0x0300_117C           |
	+---------+---------+---------+--------+-----------------------+
	|IIC4_SDA | I/O     | PWR     | 5      | FMUX_GPIO_REG         |
	|         |         | _BUTTON1|        | _IOCTRL_PWR_BUTTON1   |
	|         |         |         |        | 0x0300_1098           |
	+---------+---------+---------+--------+-----------------------+
	|IIC4_SDA | I/O     | PAD_M   | 5      | FMUX_GPIO_REG         |
	|         |         | IPIRX2P |        | _IOCTRL_PAD_MIPIRX2P  |
	|         |         |         |        | 0x0300_1180           |
	+---------+---------+---------+--------+-----------------------+

No-die domain I2C
^^^^^^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_nodie_i2c:
.. table:: No-die domain I2C
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| PWR\    | I/O     | PW      | 5      | FMUX_GPIO             |
	| _IIC_SCL|         | R_GPIO1 |        | _REG_IOCTRL_PWR_GPIO1 |
	|         |         |         |        | 0x0300_10A8           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I/O     | PW      | 5      | FMUX_GPIO             |
	| _IIC_SDA|         | R_GPIO2 |        | _REG_IOCTRL_PWR_GPIO2 |
	|         |         |         |        | 0x0300_10AC           |
	+---------+---------+---------+--------+-----------------------+


IIS
^^^

.. _table_inf_signal_pin_fmux_iis:
.. table:: IIS
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| II\     | I/O     | PA      | 4      | FMUX_GPIO_REG_IO      |
	| S1_BCLK |         | D_AUD_A |        | CTRL_PAD_AUD_AINL_MIC |
	|         |         | INL_MIC |        | 0x0300_11BC           |
	+---------+---------+---------+--------+-----------------------+
	| IIS1_DI | I       | PAD_AU  | 4      | FMUX_GPIO_REG_IO      |
	|         |         | D_AOUTR |        | CTRL_PAD_AUD_AOUTR    |
	|         |         |         |        | 0x0300_11C8           |
	+---------+---------+---------+--------+-----------------------+
	| IIS1_DO | O       | PAD_AU  | 6      | FMUX_GPIO_REG         |
	|         |         | D_AOUTR |        | _IOCTRL_PAD_AUD_AOUTR |
	|         |         |         |        | 0x0300_11C8           |
	+---------+---------+---------+--------+-----------------------+
	| II\     | I/O     | AUX0    | 4      | FMUX                  |
	| S1_MCLK |         |         |        | _GPIO_REG_IOCTRL_AUX0 |
	|         |         |         |        | 0x0300_1078           |
	+---------+---------+---------+--------+-----------------------+
	| II\     | I/O     | PA      | 5      | FMUX_GPIO_REG_IO      |
	| S2_BCLK |         | D_AUD_A |        | CTRL_PAD_AUD_AINL_MIC |
	|         |         | INL_MIC |        | 0x0300_11BC           |
	+---------+---------+---------+--------+-----------------------+
	| II\     | I/O     | PAD     | 7      | FMUX_GPIO_R           |
	| S2_BCLK |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXM |
	|         |         | M\_\__E |        | 0x0300_1128           |
	|         |         | PHY_RXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| IIS2_DI | I       | PAD     | 7      | FMUX_GPIO_R           |
	|         |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXM |
	|         |         | M\_\__E |        | 0x0300_1130           |
	|         |         | PHY_TXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| IIS2_DO | O       | PAD_AU  | 5      | FMUX_GPIO_REG         |
	|         |         | D_AOUTR |        | _IOCTRL_PAD_AUD_AOUTR |
	|         |         |         |        | 0x0300_11C8           |
	+---------+---------+---------+--------+-----------------------+
	| IIS2_DO | O       | PAD     | 7      | FMUX_GPIO_R           |
	|         |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXP |
	|         |         | P\_\__E |        | 0x0300_112C           |
	|         |         | PHY_TXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| II\     | I/O     | PAD     | 7      | FMUX_GPIO_R           |
	| S2_LRCK |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXP |
	|         |         | P\_\__E |        | 0x0300_1124           |
	|         |         | PHY_RXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| K\      | I/O     | MUX_SP  | 5      | FMUX_GPIO_REG         |
	| EY_COL0 |         | I1_MOSI |        | _IOCTRL_MUX_SPI1_MOSI |
	|         |         |         |        | 0x0300_1118           |
	+---------+---------+---------+--------+-----------------------+
	| K\      | I/O     | MUX_SP  | 5      | FMUX_GPIO_REG         |
	| EY_COL1 |         | I1_MISO |        | _IOCTRL_MUX_SPI1_MISO |
	|         |         |         |        | 0x0300_1114           |
	+---------+---------+---------+--------+-----------------------+
	| K\      | I/O     | ADC1    | 4      | FMUX                  |
	| EY_COL2 |         |         |        | _GPIO_REG_IOCTRL_ADC1 |
	|         |         |         |        | 0x0300_10F8           |
	+---------+---------+---------+--------+-----------------------+
	| K\      | I/O     | PAD_M   | 6      | FMUX_GPIO_RE          |
	| EY_ROW0 |         | IPIRX4N |        | G_IOCTRL_PAD_MIPIRX4N |
	|         |         |         |        | 0x0300_116C           |
	+---------+---------+---------+--------+-----------------------+
	| K\      | I/O     | PAD_M   | 6      | FMUX_GPIO_RE          |
	| EY_ROW1 |         | IPIRX4P |        | G_IOCTRL_PAD_MIPIRX4P |
	|         |         |         |        | 0x0300_1170           |
	+---------+---------+---------+--------+-----------------------+

To be continued ......

.. _table_inf_signal_pin_fmux_iis_2:
.. table:: IIS (continued)
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| K\      | I/O     | PAD_M   | 6      | FMUX_GPIO_RE          |
	| EY_ROW2 |         | IPIRX1P |        | G_IOCTRL_PAD_MIPIRX1P |
	|         |         |         |        | 0x0300_1188           |
	+---------+---------+---------+--------+-----------------------+
	| K\      | I/O     | MUX_S   | 5      | FMUX_GPIO_RE          |
	| EY_ROW2 |         | PI1_SCK |        | G_IOCTRL_MUX_SPI1_SCK |
	|         |         |         |        | 0x0300_1120           |
	+---------+---------+---------+--------+-----------------------+
	| K\      | I/O     | PAD_M   | 6      | FMUX_GPIO_RE          |
	| EY_ROW3 |         | IPIRX1N |        | G_IOCTRL_PAD_MIPIRX1N |
	|         |         |         |        | 0x0300_1184           |
	+---------+---------+---------+--------+-----------------------+
	| K\      | I/O     | MUX     | 5      | FMUX_GPIO_R           |
	| EY_ROW3 |         | _SPI1_CS|        | EG_IOCTRL_MUX_SPI1_CS |
	|         |         |         |        | 0x0300_111C           |
	+---------+---------+---------+--------+-----------------------+

PWM
^^^

.. _table_inf_signal_pin_fmux_pwm:
.. table:: PWM
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| PWM[0]  | I/O     | PW      | 0      | FMUX_GPIO             |
	|         |         | M0_BUCK |        | _REG_IOCTRL_PWM0_BUCK |
	|         |         |         |        | 0x0300_10EC           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[1]  | I/O     | GPIO_RT | 4      | FMUX_GPI              |
	|         |         | X\_\__E |        | O_REG_IOCTRL_GPIO_RTX |
	|         |         | PHY_RTX |        | 0x0300_11CC           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[2]  | I/O     | GPIO    | 4      | FMUX_GP               |
	|         |         | _ZQ\_\_ |        | IO_REG_IOCTRL_GPIO_ZQ |
	|         |         | _PAD_ZQ |        | 0x0300_11D0           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[4]  | I/O     | U       | 2      | FMUX_GPI              |
	|         |         | ART0_TX |        | O_REG_IOCTRL_UART0_TX |
	|         |         |         |        | 0x0300_1040           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[4]  | I/O     | SD1_D3  | 7      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD1_D3 |
	|         |         |         |        | 0x0300_10D0           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[5]  | I/O     | U       | 2      | FMUX_GPI              |
	|         |         | ART0_RX |        | O_REG_IOCTRL_UART0_RX |
	|         |         |         |        | 0x0300_1044           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[5]  | I/O     | SD1_D2  | 7      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD1_D2 |
	|         |         |         |        | 0x0300_10D4           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[6]  | I/O     | JTAG    | 2      | FMUX_GPIO_RE          |
	|         |         | _CPU_TCK|        | G_IOCTRL_JTAG_CPU_TCK |
	|         |         |         |        | 0x0300_1068           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[6]  | I/O     | SD1_D1  | 7      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD1_D1 |
	|         |         |         |        | 0x0300_10D8           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[7]  | I/O     | JTAG    | 2      | FMUX_GPIO_RE          |
	|         |         | _CPU_TMS|        | G_IOCTRL_JTAG_CPU_TMS |
	|         |         |         |        | 0x0300_1064           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[7]  | I/O     | SD1_D0  | 7      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD1_D0 |
	|         |         |         |        | 0x0300_10DC           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[8]  | I/O     | PW      | 4      | FMUX_GPIO             |
	|         |         | R_GPIO0 |        | _REG_IOCTRL_PWR_GPIO0 |
	|         |         |         |        | 0x0300_10A4           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[8]  | I/O     | MUX_SP  | 4      | FMUX_GPIO_REG_IO      |
	|         |         | I1_MOSI |        | CTRL_MUX_SPI1_MOSI    |
	|         |         |         |        | 0x0300_1118           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[8]  | I/O     | SD1_CMD | 7      | FMUX_GP               |
	|         |         |         |        | IO_REG_IOCTRL_SD1_CMD |
	|         |         |         |        | 0x0300_10E0           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[8]  | I/O     | PAD_MI  | 5      | FMUX_GPIO_REG_IO      |
	|         |         | PI_TXM2 |        | CTRL_PAD_MIPI_TXM2    |
	|         |         |         |        | 0x0300_11A4           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[9]  | I/O     | PW      | 4      | FMUX_GPIO             |
	|         |         | R_GPIO1 |        | _REG_IOCTRL_PWR_GPIO1 |
	|         |         |         |        | 0x0300_10A8           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[9]  | I/O     | MUX_SP  | 4      | FMUX_GPIO_REG_IO      |
	|         |         | I1_MISO |        | CTRL_MUX_SPI1_MISO    |
	|         |         |         |        | 0x0300_1114           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[9]  | I/O     | SD1_CLK | 7      | FMUX_GP               |
	|         |         |         |        | IO_REG_IOCTRL_SD1_CLK |
	|         |         |         |        | 0x0300_10E4           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[9]  | I/O     | PAD_MI  | 5      | FMUX_GPIO_REG_IO      |
	|         |         | PI_TXP2 |        | CTRL_PAD_MIPI_TXP2    |
	|         |         |         |        | 0x0300_11A8           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[10] | I/O     | PW      | 4      | FMUX_GPIO             |
	|         |         | R_GPIO2 |        | _REG_IOCTRL_PWR_GPIO2 |
	|         |         |         |        | 0x0300_10AC           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[10] | I/O     | MUX_S   | 4      | FMUX_GPIO_RE          |
	|         |         | PI1_SCK |        | G_IOCTRL_MUX_SPI1_SCK |
	|         |         |         |        | 0x0300_1120           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[10] | I/O     | SD0_D3  | 5      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D3 |
	|         |         |         |        | 0x0300_1030           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[10] | I/O     | PAD_MI  | 5      | FMUX_GPIO_REG_IO      |
	|         |         | PI_TXM1 |        | CTRL_PAD_MIPI_TXM1    |
	|         |         |         |        | 0x0300_11AC           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[11] | I/O     | MUX     | 4      | FMUX_GPIO_R           |
	|         |         | _SPI1_CS|        | EG_IOCTRL_MUX_SPI1_CS |
	|         |         |         |        | 0x0300_111C           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[11] | I/O     | SD0_D2  | 5      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D2 |
	|         |         |         |        | 0x0300_102C           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[11] | I/O     | PAD_MI  | 5      | FMUX_GPIO_REG_IO      |
	|         |         | PI_TXP1 |        | CTRL_PAD_MIPI_TXP1    |
	|         |         |         |        | 0x0300_11B0           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[12] | I/O     | PAD     | 4      | FMUX_GPIO_R           |
	|         |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXM |
	|         |         | M\_\__E |        | 0x0300_1128           |
	|         |         | PHY_RXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| PWM[12] | I/O     | SD0_D1  | 5      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D1 |
	|         |         |         |        | 0x0300_1028           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[13] | I/O     | PAD     | 4      | FMUX_GPIO_R           |
	|         |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXP |
	|         |         | P\_\__E |        | 0x0300_1124           |
	|         |         | PHY_RXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| PWM[13] | I/O     | SD0_D0  | 5      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D0 |
	|         |         |         |        | 0x0300_1024           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[14] | I/O     | PAD     | 4      | FMUX_GPIO_R           |
	|         |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXM |
	|         |         | M\_\__E |        | 0x0300_1130           |
	|         |         | PHY_TXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| PWM[14] | I/O     | SD0_CMD | 5      | FMUX_GP               |
	|         |         |         |        | IO_REG_IOCTRL_SD0_CMD |
	|         |         |         |        | 0x0300_1020           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[14] | I/O     | PAD_MI  | 5      | FMUX_GPIO_REG_IO      |
	|         |         | PI_TXM0 |        | CTRL_PAD_MIPI_TXM0    |
	|         |         |         |        | 0x0300_11B4           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[15] | I/O     | PAD     | 4      | FMUX_GPIO_R           |
	|         |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXP |
	|         |         | P\_\__E |        | 0x0300_112C           |
	|         |         | PHY_TXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| PWM[15] | I/O     | SD0_CLK | 5      | FMUX_GP               |
	|         |         |         |        | IO_REG_IOCTRL_SD0_CLK |
	|         |         |         |        | 0x0300_101C           |
	+---------+---------+---------+--------+-----------------------+
	| PWM[15] | I/O     | PAD_MI  | 5      | FMUX_GPIO_REG_IO      |
	|         |         | PI_TXP0 |        | CTRL_PAD_MIPI_TXP0    |
	|         |         |         |        | 0x0300_11B8           |
	+---------+---------+---------+--------+-----------------------+

CA53 JTAG(2W) RISCV JTAG(4W) I2C0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_ca53_rv_jtag_i2c0:
.. table:: CA53 JTAG(2W) RISCV JTAG(4W) I2C0
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| C\      | I/O     | JTAG    | 0      | FMUX_GPIO_RE          |
	| R_4WTCK |         | _CPU_TCK|        | G_IOCTRL_JTAG_CPU_TCK |
	|         |         |         |        | 0x0300_1068           |
	|         |         |         |        |                       |
	|         |         |         |        |                       |
	|         |         |         |        |                       |
	|         |         |         |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| C\      | I/O     | JTAG    | 0      | FMUX_GPIO_RE          |
	| R_4WTMS |         | _CPU_TMS|        | G_IOCTRL_JTAG_CPU_TMS |
	|         |         |         |        | 0x0300_1064           |
	+---------+---------+---------+--------+-----------------------+
	| C\      | I/O     | PAD_M   | 0      | FMUX_GPIO_RE          |
	| R_2WTCK |         | IPIRX3P |        | G_IOCTRL_PAD_MIPIRX3P |
	|         |         |         |        | 0x0300_1178           |
	+---------+---------+---------+--------+-----------------------+
	| C\      | I/O     | PAD_MI  | 0      | FMUX_GPIO_REG_IO      |
	| R_2WTCK |         | PI_TXP1 |        | CTRL_PAD_MIPI_TXP1    |
	|         |         |         |        | 0x0300_11B0           |
	+---------+---------+---------+--------+-----------------------+
	| C\      | I/O     | PW      | 7      | FMUX_GPIO             |
	| R_2WTCK |         | R_GPIO2 |        | _REG_IOCTRL_PWR_GPIO2 |
	|         |         |         |        | 0x0300_10AC           |
	+---------+---------+---------+--------+-----------------------+
	| CR_SCL0 | I/O     | PAD_M   | 0      | FMUX_GPIO_RE          |
	|         |         | IPIRX4N |        | G_IOCTRL_PAD_MIPIRX4N |
	|         |         |         |        | 0x0300_116C           |
	+---------+---------+---------+--------+-----------------------+
	| CR_SCL0 | I/O     | PAD_MI  | 0      | FMUX_GPIO_REG_IO      |
	|         |         | PI_TXP2 |        | CTRL_PAD_MIPI_TXP2    |
	|         |         |         |        | 0x0300_11A8           |
	+---------+---------+---------+--------+-----------------------+
	| C\      | I/O     | PAD_M   | 0      | FMUX_GPIO_RE          |
	| R_2WTMS |         | IPIRX3N |        | G_IOCTRL_PAD_MIPIRX3N |
	|         |         |         |        | 0x0300_1174           |
	+---------+---------+---------+--------+-----------------------+
	| C\      | I/O     | PAD_MI  | 0      | FMUX_GPIO_REG_IO      |
	| R_2WTMS |         | PI_TXM1 |        | CTRL_PAD_MIPI_TXM1    |
	|         |         |         |        | 0x0300_11AC           |
	+---------+---------+---------+--------+-----------------------+
	| CR_SDA0 | I/O     | PAD_M   | 0      | FMUX_GPIO_RE          |
	|         |         | IPIRX4P |        | G_IOCTRL_PAD_MIPIRX4P |
	|         |         |         |        | 0x0300_1170           |
	+---------+---------+---------+--------+-----------------------+
	| CR_SDA0 | I/O     | PAD_MI  | 0      | FMUX_GPIO_REG_IO      |
	|         |         | PI_TXM2 |        | CTRL_PAD_MIPI_TXM2    |
	|         |         |         |        | 0x0300_11A4           |
	+---------+---------+---------+--------+-----------------------+
	| CR_SDA0 | I/O     | PW      | 7      | FMUX_GPIO             |
	|         |         | R_GPIO1 |        | _REG_IOCTRL_PWR_GPIO1 |
	|         |         |         |        | 0x0300_10A8           |
	+---------+---------+---------+--------+-----------------------+
	| C\      | I/O     | I       | 0      | FMUX_GPI              |
	| R_4WTDI |         | IC0_SCL |        | O_REG_IOCTRL_IIC0_SCL |
	|         |         |         |        | 0x0300_1070           |
	+---------+---------+---------+--------+-----------------------+
	| C\      | I/O     | I       | 0      | FMUX_GPI              |
	| R_4WTDO |         | IC0_SDA |        | O_REG_IOCTRL_IIC0_SDA |
	|         |         |         |        | 0x0300_1074           |
	+---------+---------+---------+--------+-----------------------+


System
^^^^^^

.. _table_inf_signal_pin_fmux_system:
.. table:: System
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| PWR\    | I       | PWR     | 0      | FMUX_GPIO_R           |
	| _BUTTON1|         | _BUTTON1|        | EG_IOCTRL_PWR_BUTTON1 |
	|         |         |         |        | 0x0300_1098           |
	+---------+---------+---------+--------+-----------------------+
	| P\      | I       | P       | 0      | FMUX_GPI              |
	| WR_RSTN |         | WR_RSTN |        | O_REG_IOCTRL_PWR_RSTN |
	|         |         |         |        | 0x0300_1080           |
	+---------+---------+---------+--------+-----------------------+
	| P\      | O       | P       | 0      | FMUX_GPI              |
	| WR_SEQ1 |         | WR_SEQ1 |        | O_REG_IOCTRL_PWR_SEQ1 |
	|         |         |         |        | 0x0300_1084           |
	+---------+---------+---------+--------+-----------------------+
	| P\      | O       | P       | 0      | FMUX_GPI              |
	| WR_SEQ2 |         | WR_SEQ2 |        | O_REG_IOCTRL_PWR_SEQ2 |
	|         |         |         |        | 0x0300_1088           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I       | PWR     | 0      | FMUX_GPIO_R           |
	| _WAKEUP0|         | _WAKEUP0|        | EG_IOCTRL_PWR_WAKEUP0 |
	|         |         |         |        | 0x0300_1090           |
	+---------+---------+---------+--------+-----------------------+
	| USB_V\  | I       | USB_V   | 0      | FMUX_GPIO_RE          |
	| BUS_DET |         | BUS_DET |        | G_IOCTRL_USB_VBUS_DET |
	|         |         |         |        | 0x0300_1108           |
	+---------+---------+---------+--------+-----------------------+


No-die domain IR
^^^^^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_nodie_ir:
.. table:: No-die domain IR
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| PWR_IR0 | I       | PWR     | 1      | FMUX_GPIO_R           |
	|         |         | _WAKEUP0|        | EG_IOCTRL_PWR_WAKEUP0 |
	|         |         |         |        | 0x0300_1090           |
	+---------+---------+---------+--------+-----------------------+


SPI_NOR1
^^^^^^^^

.. _table_inf_signal_pin_fmux_spi_nor1:
.. table:: SPI_NOR1
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| PW\     | O       | SD1_D3  | 6      | FMUX_G                |
	| R_SPINO\|         |         |        | PIO_REG_IOCTRL_SD1_D3 |
	| R1_CS_X |         |         |        | 0x0300_10D0           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I/O     | SD1_D2  | 6      | FMUX_G                |
	| _SPINOR\|         |         |        | PIO_REG_IOCTRL_SD1_D2 |
	| 1_HOLD_X|         |         |        | 0x0300_10D4           |
	+---------+---------+---------+--------+-----------------------+
	| PW\     | I/O     | SD1_D0  | 6      | FMUX_G                |
	| R_SPINO\|         |         |        | PIO_REG_IOCTRL_SD1_D0 |
	| R1_MISO |         |         |        | 0x0300_10DC           |
	+---------+---------+---------+--------+-----------------------+
	| PW\     | I/O     | SD1_CMD | 6      | FMUX_GP               |
	| R_SPINO\|         |         |        | IO_REG_IOCTRL_SD1_CMD |
	| R1_MOSI |         |         |        | 0x0300_10E0           |
	+---------+---------+---------+--------+-----------------------+
	| P\      | O       | SD1_CLK | 6      | FMUX_GP               |
	| WR_SPIN\|         |         |        | IO_REG_IOCTRL_SD1_CLK |
	| OR1_SCK |         |         |        | 0x0300_10E4           |
	+---------+---------+---------+--------+-----------------------+
	| PW\     | I/O     | SD1_D1  | 6      | FMUX_G                |
	| R_SPINO\|         |         |        | PIO_REG_IOCTRL_SD1_D1 |
	| R1_WP_X |         |         |        | 0x0300_10D8           |
	+---------+---------+---------+--------+-----------------------+


SD1
^^^

.. _table_inf_signal_pin_fmux_sd1:
.. table:: SD1
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| PWR\    | O       | SD1_CLK | 0      | FMUX_GP               |
	| _SD1_CLK|         |         |        | IO_REG_IOCTRL_SD1_CLK |
	|         |         |         |        | 0x0300_10E4           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I/O     | SD1_CMD | 0      | FMUX_GP               |
	| _SD1_CMD|         |         |        | IO_REG_IOCTRL_SD1_CMD |
	|         |         |         |        | 0x0300_10E0           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I/O     | SD1_D0  | 0      | FMUX_G                |
	| _SD1_D0 |         |         |        | PIO_REG_IOCTRL_SD1_D0 |
	|         |         |         |        | 0x0300_10DC           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I/O     | SD1_D1  | 0      | FMUX_G                |
	| _SD1_D1 |         |         |        | PIO_REG_IOCTRL_SD1_D1 |
	|         |         |         |        | 0x0300_10D8           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I/O     | SD1_D2  | 0      | FMUX_G                |
	| _SD1_D2 |         |         |        | PIO_REG_IOCTRL_SD1_D2 |
	|         |         |         |        | 0x0300_10D4           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I/O     | SD1_D3  | 0      | FMUX_G                |
	| _SD1_D3 |         |         |        | PIO_REG_IOCTRL_SD1_D3 |
	|         |         |         |        | 0x0300_10D0           |
	+---------+---------+---------+--------+-----------------------+


SD0
^^^

.. _table_inf_signal_pin_fmux_sd0:
.. table:: SD0
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| S\      | I       | SD0_CD  | 0      | FMUX_G                |
	| DIO0_CD |         |         |        | PIO_REG_IOCTRL_SD0_CD |
	|         |         |         |        | 0x0300_1034           |
	+---------+---------+---------+--------+-----------------------+
	| SD\     | O       | SD0_CLK | 0      | FMUX_GP               |
	| IO0_CLK |         |         |        | IO_REG_IOCTRL_SD0_CLK |
	|         |         |         |        | 0x0300_101C           |
	+---------+---------+---------+--------+-----------------------+
	| SD\     | I/O     | SD0_CMD | 0      | FMUX_GP               |
	| IO0_CMD |         |         |        | IO_REG_IOCTRL_SD0_CMD |
	|         |         |         |        | 0x0300_1020           |
	+---------+---------+---------+--------+-----------------------+
	| SDI\    | I/O     | SD0_D0  | 0      | FMUX_G                |
	| O0_D[0] |         |         |        | PIO_REG_IOCTRL_SD0_D0 |
	|         |         |         |        | 0x0300_1024           |
	+---------+---------+---------+--------+-----------------------+
	| SDI\    | I/O     | SD0_D1  | 0      | FMUX_G                |
	| O0_D[1] |         |         |        | PIO_REG_IOCTRL_SD0_D1 |
	|         |         |         |        | 0x0300_1028           |
	+---------+---------+---------+--------+-----------------------+
	| SDI\    | I/O     | SD0_D2  | 0      | FMUX_G                |
	| O0_D[2] |         |         |        | PIO_REG_IOCTRL_SD0_D2 |
	|         |         |         |        | 0x0300_102C           |
	+---------+---------+---------+--------+-----------------------+
	| SDI\    | I/O     | SD0_D3  | 0      | FMUX_G                |
	| O0_D[3] |         |         |        | PIO_REG_IOCTRL_SD0_D3 |
	|         |         |         |        | 0x0300_1030           |
	+---------+---------+---------+--------+-----------------------+
	| SDIO0\  | O       | SD0     | 0      | FMUX_GPIO             |
	| _PWR_EN |         | _PWR_EN |        | _REG_IOCTRL_SD0_PWR_EN|
	|         |         |         |        | 0x0300_1038           |
	+---------+---------+---------+--------+-----------------------+

SPI
^^^

.. _table_inf_signal_pin_fmux_spi:
.. table:: SPI
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| SP\     | O       | SD0_D3  | 2      | FMUX_G                |
	| I0_CS_X |         |         |        | PIO_REG_IOCTRL_SD0_D3 |
	|         |         |         |        | 0x0300_1030           |
	+---------+---------+---------+--------+-----------------------+
	| SP\     | O       | PAD_MI  | 6      | FMUX_GPIO_REG_IO      |
	| I0_CS_X |         | PI_TXP2 |        | CTRL_PAD_MIPI_TXP2    |
	|         |         |         |        | 0x0300_11A8           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | O       | SD0_CLK | 2      | FMUX_GPIO             |
	| PI0_SCK |         |         |        | _REG_IOCTRL_SD0_CLK   |
	|         |         |         |        | 0x0300_101C           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | O       | PAD_MI  | 6      | FMUX_GPIO_REG_IO      |
	| PI0_SCK |         | PI_TXM2 |        | CTRL_PAD_MIPI_TXM2    |
	|         |         |         |        | 0x0300_11A4           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | I       | SD0_D0  | 2      | FMUX_GPIO_REG_IO      |
	| PI0_SDI |         |         |        | CTRL_SD0_D0           |
	|         |         |         |        | 0x0300_1024           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | I       | PAD_MI  | 6      | FMUX_GPIO_REG_IO      |
	| PI0_SDI |         | PI_TXP1 |        | CTRL_PAD_MIPI_TXP1    |
	|         |         |         |        | 0x0300_11B0           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | I/O     | SD0_CMD | 2      | FMUX_GP               |
	| PI0_SDO |         |         |        | IO_REG_IOCTRL_SD0_CMD |
	|         |         |         |        | 0x0300_1020           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | I/O     | PAD_MI  | 6      | FMUX_GPIO_REG_IO      |
	| PI0_SDO |         | PI_TXM1 |        | CTRL_PAD_MIPI_TXM1    |
	|         |         |         |        | 0x0300_11AC           |
	+---------+---------+---------+--------+-----------------------+
	| SP\     | O       | MUX     | 6      | FMUX_GPIO_R           |
	| I1_CS_X |         | _SPI1_CS|        | EG_IOCTRL_MUX_SPI1_CS |
	|         |         |         |        | 0x0300_111C           |
	+---------+---------+---------+--------+-----------------------+
	| SP\     | O       | PAD     | 6      | FMUX_GPIO_R           |
	| I1_CS_X |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXM |
	|         |         | M\_\__E |        | 0x0300_1130           |
	|         |         | PHY_TXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| S\      | O       | MUX_S   | 6      | FMUX_GPIO_RE          |
	| PI1_SCK |         | PI1_SCK |        | G_IOCTRL_MUX_SPI1_SCK |
	|         |         |         |        | 0x0300_1120           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | O       | PAD     | 6      | FMUX_GPIO_R           |
	| PI1_SCK |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXP |
	|         |         | P\_\__E |        | 0x0300_112C           |
	|         |         | PHY_TXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| S\      | I       | MUX_SP  | 6      | FMUX_GPIO_REG_IO      |
	| PI1_SDI |         | I1_MISO |        | CTRL_MUX_SPI1_MISO    |
	|         |         |         |        | 0x0300_1114           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | I       | PAD     | 6      | FMUX_GPIO_R           |
	| PI1_SDI |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXM |
	|         |         | M\_\__E |        | 0x0300_1128           |
	|         |         | PHY_RXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| S\      | I/O     | MUX_SP  | 6      | FMUX_GPIO_REG_IO      |
	| PI1_SDO |         | I1_MOSI |        | CTRL_MUX_SPI1_MOSI    |
	|         |         |         |        | 0x0300_1118           |
	+---------+---------+---------+--------+-----------------------+

To be continued ......	
	
.. _table_inf_signal_pin_fmux_spi_2:
.. table:: SPI (continued)
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+	
	| S\      | I/O     | PAD     | 6      | FMUX_GPIO_R           |
	| PI1_SDO |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXP |
	|         |         | P\_\__E |        | 0x0300_1124           |
	|         |         | PHY_RXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| SP\     | O       | SD1_D3  | 1      | FMUX_G                |
	| I2_CS_X |         |         |        | PIO_REG_IOCTRL_SD1_D3 |
	|         |         |         |        | 0x0300_10D0           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | O       | SD1_CLK | 1      | FMUX_GP               |
	| PI2_SCK |         |         |        | IO_REG_IOCTRL_SD1_CLK |
	|         |         |         |        | 0x0300_10E4           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | I       | SD1_D0  | 1      | FMUX_G                |
	| PI2_SDI |         |         |        | PIO_REG_IOCTRL_SD1_D0 |
	|         |         |         |        | 0x0300_10DC           |
	+---------+---------+---------+--------+-----------------------+
	| S\      | I/O     | SD1_CMD | 1      | FMUX_GP               |
	| PI2_SDO |         |         |        | IO_REG_IOCTRL_SD1_CMD |
	|         |         |         |        | 0x0300_10E0           |
	+---------+---------+---------+--------+-----------------------+


UART
^^^^

.. _table_inf_signal_pin_fmux_uart:
.. table:: UART
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| U\      | I       | U       | 0      | FMUX_GPI              |
	| ART0_RX |         | ART0_RX |        | O_REG_IOCTRL_UART0_RX |
	|         |         |         |        | 0x0300_1044           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | U       | 0      | FMUX_GPI              |
	| ART0_TX |         | ART0_TX |        | O_REG_IOCTRL_UART0_TX |
	|         |         |         |        | 0x0300_1040           |
	+---------+---------+---------+--------+-----------------------+
	| UA\     | I       | JTAG    | 4      | FMUX_GPIO_RE          |
	| RT1_CTS |         | _CPU_TCK|        | G_IOCTRL_JTAG_CPU_TCK |
	|         |         |         |        | 0x0300_1068           |
	+---------+---------+---------+--------+-----------------------+
	| UA\     | O       | JTAG    | 4      | FMUX_GPIO_RE          |
	| RT1_RTS |         | _CPU_TMS|        | G_IOCTRL_JTAG_CPU_TMS |
	|         |         |         |        | 0x0300_1064           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | SD0_D2  | 4      | FMUX_G                |
	| ART1_RX |         |         |        | PIO_REG_IOCTRL_SD0_D2 |
	|         |         |         |        | 0x0300_102C           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | U       | 4      | FMUX_GPI              |
	| ART1_RX |         | ART0_RX |        | O_REG_IOCTRL_UART0_RX |
	|         |         |         |        | 0x0300_1044           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | PWR     | 4      | FMUX_GPIO_R           |
	| ART1_RX |         | _BUTTON1|        | EG_IOCTRL_PWR_BUTTON1 |
	|         |         |         |        | 0x0300_1098           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | JTAG    | 6      | FMUX_GPIO_RE          |
	| ART1_RX |         | _CPU_TCK|        | G_IOCTRL_JTAG_CPU_TCK |
	|         |         |         |        | 0x0300_1068           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | I       | 1      | FMUX_GPI              |
	| ART1_RX |         | IC0_SDA |        | O_REG_IOCTRL_IIC0_SDA |
	|         |         |         |        | 0x0300_1074           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | SD0_D1  | 4      | FMUX_G                |
	| ART1_TX |         |         |        | PIO_REG_IOCTRL_SD0_D1 |
	|         |         |         |        | 0x0300_1028           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | U       | 4      | FMUX_GPI              |
	| ART1_TX |         | ART0_TX |        | O_REG_IOCTRL_UART0_TX |
	|         |         |         |        | 0x0300_1040           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | PWR     | 4      | FMUX_GPIO_R           |
	| ART1_TX |         | _WAKEUP0|        | EG_IOCTRL_PWR_WAKEUP0 |
	|         |         |         |        | 0x0300_1090           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | JTAG    | 6      | FMUX_GPIO_RE          |
	| ART1_TX |         | _CPU_TMS|        | G_IOCTRL_JTAG_CPU_TMS |
	|         |         |         |        | 0x0300_1064           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | I       | 1      | FMUX_GPI              |
	| ART1_TX |         | IC0_SCL |        | O_REG_IOCTRL_IIC0_SCL |
	|         |         |         |        | 0x0300_1070           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | I       | 2      | FMUX_GPI              |
	| ART2_RX |         | IC0_SDA |        | O_REG_IOCTRL_IIC0_SDA |
	|         |         |         |        | 0x0300_1074           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | SD1_D1  | 2      | FMUX_G                |
	| ART2_RX |         |         |        | PIO_REG_IOCTRL_SD1_D1 |
	|         |         |         |        | 0x0300_10D8           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | PW      | 1      | FMUX_GPIO             |
	| ART2_RX |         | R_GPIO1 |        | _REG_IOCTRL_PWR_GPIO1 |
	|         |         |         |        | 0x0300_10A8           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | I       | 2      | FMUX_GPI              |
	| ART2_TX |         | IC0_SCL |        | O_REG_IOCTRL_IIC0_SCL |
	|         |         |         |        | 0x0300_1070           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | SD1_D2  | 2      | FMUX_G                |
	| ART2_TX |         |         |        | PIO_REG_IOCTRL_SD1_D2 |
	|         |         |         |        | 0x0300_10D4           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | PW      | 1      | FMUX_GPIO             |
	| ART2_TX |         | R_GPIO0 |        | _REG_IOCTRL_PWR_GPIO0 |
	|         |         |         |        | 0x0300_10A4           |
	+---------+---------+---------+--------+-----------------------+
	| UA\     | I       | MUX     | 1      | FMUX_GPIO_R           |
	| RT3_CTS |         | _SPI1_CS|        | EG_IOCTRL_MUX_SPI1_CS |
	|         |         |         |        | 0x0300_111C           |
	+---------+---------+---------+--------+-----------------------+
	| UA\     | I       | PAD     | 1      | FMUX_GPIO_R           |
	| RT3_CTS |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXM |
	|         |         | M\_\__E |        | 0x0300_1130           |
	|         |         | PHY_TXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| UA\     | I       | SD1_D3  | 5      | FMUX_G                |
	| RT3_CTS |         |         |        | PIO_REG_IOCTRL_SD1_D3 |
	|         |         |         |        | 0x0300_10D0           |
	+---------+---------+---------+--------+-----------------------+
	| UA\     | O       | MUX_SP  | 1      | FMUX_GPIO_REG_IO      |
	| RT3_RTS |         | I1_MISO |        | CTRL_MUX_SPI1_MISO    |
	|         |         |         |        | 0x0300_1114           |
	+---------+---------+---------+--------+-----------------------+
	| UA\     | O       | PAD     | 1      | FMUX_GPIO_R           |
	| RT3_RTS |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXM |
	|         |         | M\_\__E |        | 0x0300_1128           |
	|         |         | PHY_RXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| UA\     | O       | SD1_D0  | 5      | FMUX_G                |
	| RT3_RTS |         |         |        | PIO_REG_IOCTRL_SD1_D0 |
	|         |         |         |        | 0x0300_10DC           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | SD0_D3  | 4      | FMUX_G                |
	| ART3_RX |         |         |        | PIO_REG_IOCTRL_SD0_D3 |
	|         |         |         |        | 0x0300_1030           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | MUX_SP  | 1      | FMUX_GPIO_REG_IO      |
	| ART3_RX |         | I1_MOSI |        | CTRL_MUX_SPI1_MOSI    |
	|         |         |         |        | 0x0300_1118           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | PAD     | 1      | FMUX_GPIO_R           |
	| ART3_RX |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXP |
	|         |         | P\_\__E |        | 0x0300_1124           |
	|         |         | PHY_RXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| U\      | I       | SD1_D1  | 5      | FMUX_G                |
	| ART3_RX |         |         |        | PIO_REG_IOCTRL_SD1_D1 |
	|         |         |         |        | 0x0300_10D8           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | SD0_D0  | 4      | FMUX_G                |
	| ART3_TX |         |         |        | PIO_REG_IOCTRL_SD0_D0 |
	|         |         |         |        | 0x0300_1024           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | MUX_S   | 1      | FMUX_GPIO_RE          |
	| ART3_TX |         | PI1_SCK |        | G_IOCTRL_MUX_SPI1_SCK |
	|         |         |         |        | 0x0300_1120           |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | PAD     | 1      | FMUX_GPIO_R           |
	| ART3_TX |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXP |
	|         |         | P\_\__E |        | 0x0300_112C           |
	|         |         | PHY_TXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| U\      | O       | SD1_D2  | 5      | FMUX_G                |
	| ART3_TX |         |         |        | PIO_REG_IOCTRL_SD1_D2 |
	|         |         |         |        | 0x0300_10D4           |
	+---------+---------+---------+--------+-----------------------+

No-die domain UART
^^^^^^^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_nodie_uart:
.. table:: No-die domain UART
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| PWR_U\  | I       | PW      | 2      | FMUX_GPIO             |
	| ART0_RX |         | R_GPIO0 |        | _REG_IOCTRL_PWR_GPIO0 |
	|         |         |         |        | 0x0300_10A4           |
	+---------+---------+---------+--------+-----------------------+
	| PWR_U\  | O       |PWR      | 2      | FMUX_GPIO_R           |
	| ART0_TX |         |_WAKEUP0 |        | EG_IOCTRL_PWR_WAKEUP0 |
	|         |         |         |        | 0x0300_1090           |
	+---------+---------+---------+--------+-----------------------+


Wiegand
^^^^^^^

.. _table_inf_signal_pin_fmux_wiegand:
.. table:: Wiegand
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| WG0_D0  | I/O     | SD0_D0  | 6      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D0 |
	|         |         |         |        | 0x0300_1024           |
	+---------+---------+---------+--------+-----------------------+
	| WG0_D0  | I/O     | I       | 5      | FMUX_GPI              |
	|         |         | IC0_SCL |        | O_REG_IOCTRL_IIC0_SCL |
	|         |         |         |        | 0x0300_1070           |
	+---------+---------+---------+--------+-----------------------+
	| WG0_D1  | I/O     | SD0_D1  | 6      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D1 |
	|         |         |         |        | 0x0300_1028           |
	+---------+---------+---------+--------+-----------------------+
	| WG0_D1  | I/O     | I       | 5      | FMUX_GPI              |
	|         |         | IC0_SDA |        | O_REG_IOCTRL_IIC0_SDA |
	|         |         |         |        | 0x0300_1074           |
	+---------+---------+---------+--------+-----------------------+
	| WG1_D0  | I/O     | SD0_D2  | 6      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D2 |
	|         |         |         |        | 0x0300_102C           |
	+---------+---------+---------+--------+-----------------------+
	| WG1_D0  | I/O     | I       | 6      | FMUX_GPI              |
	|         |         | IC0_SDA |        | O_REG_IOCTRL_IIC0_SDA |
	|         |         |         |        | 0x0300_1074           |
	+---------+---------+---------+--------+-----------------------+
	| WG1_D1  | I/O     | SD0_D3  | 6      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D3 |
	|         |         |         |        | 0x0300_1030           |
	+---------+---------+---------+--------+-----------------------+
	| WG1_D1  | I/O     | AUX0    | 6      | FMUX                  |
	|         |         |         |        | _GPIO_REG_IOCTRL_AUX0 |
	|         |         |         |        | 0x0300_1078           |
	+---------+---------+---------+--------+-----------------------+
	| WG2_D0  | I/O     | PWR     | 7      | FMUX_GPIO_R           |
	|         |         | _WAKEUP0|        | EG_IOCTRL_PWR_WAKEUP0 |
	|         |         |         |        | 0x0300_1090           |
	+---------+---------+---------+--------+-----------------------+
	| WG2_D1  | I/O     | PWR     | 7      | FMUX_GPIO_R           |
	|         |         | _BUTTON1|        | EG_IOCTRL_PWR_BUTTON1 |
	|         |         |         |        | 0x0300_1098           |
	+---------+---------+---------+--------+-----------------------+


GPIO
^^^^

.. _table_inf_signal_pin_fmux_gpio:
.. table:: GPIO
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| XG\     | I/O     | SD0_CLK | 3      | FMUX_GP               |
	| PIOA[7] |         |         |        | IO_REG_IOCTRL_SD0_CLK |
	|         |         |         |        | 0x0300_101C           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | SD0_CMD | 3      | FMUX_GP               |
	| PIOA[8] |         |         |        | IO_REG_IOCTRL_SD0_CMD |
	|         |         |         |        | 0x0300_1020           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | SD0_D0  | 3      | FMUX_G                |
	| PIOA[9] |         |         |        | PIO_REG_IOCTRL_SD0_D0 |
	|         |         |         |        | 0x0300_1024           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | SD0_D1  | 3      | FMUX_G                |
	| IOA[10] |         |         |        | PIO_REG_IOCTRL_SD0_D1 |
	|         |         |         |        | 0x0300_1028           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | SD0_D2  | 3      | FMUX_G                |
	| IOA[11] |         |         |        | PIO_REG_IOCTRL_SD0_D2 |
	|         |         |         |        | 0x0300_102C           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | SD0_D3  | 3      | FMUX_G                |
	| IOA[12] |         |         |        | PIO_REG_IOCTRL_SD0_D3 |
	|         |         |         |        | 0x0300_1030           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | SD0_CD  | 3      | FMUX_G                |
	| IOA[13] |         |         |        | PIO_REG_IOCTRL_SD0_CD |
	|         |         |         |        | 0x0300_1034           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | SD0     | 3      | FMUX_GPIO             |
	| IOA[14] |         | _PWR_EN |        | _REG_IOCTRL_SD0_PWR_EN|
	|         |         |         |        | 0x0300_1038           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | SPK_EN  | 3      | FMUX_G                |
	| IOA[15] |         |         |        | PIO_REG_IOCTRL_SPK_EN |
	|         |         |         |        | 0x0300_103C           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | U       | 3      | FMUX_GPI              |
	| IOA[16] |         | ART0_TX |        | O_REG_IOCTRL_UART0_TX |
	|         |         |         |        | 0x0300_1040           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | U       | 3      | FMUX_GPI              |
	| IOA[17] |         | ART0_RX |        | O_REG_IOCTRL_UART0_RX |
	|         |         |         |        | 0x0300_1044           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | JTAG    | 3      | FMUX_GPIO_RE          |
	| IOA[18] |         | _CPU_TCK|        | G_IOCTRL_JTAG_CPU_TCK |
	|         |         |         |        | 0x0300_1068           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | JTAG    | 3      | FMUX_GPIO_RE          |
	| IOA[19] |         | _CPU_TMS|        | G_IOCTRL_JTAG_CPU_TMS |
	|         |         |         |        | 0x0300_1064           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | E       | 3      | FMUX_GPI              |
	| IOA[22] |         | MMC_CLK |        | O_REG_IOCTRL_EMMC_CLK |
	|         |         |         |        | 0x0300_1050           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | E       | 3      | FMUX_GPI              |
	| IOA[23] |         | MMC_CMD |        | O_REG_IOCTRL_EMMC_CMD |
	|         |         |         |        | 0x0300_105C           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | EM      | 3      | FMUX_GPIO             |
	| IOA[24] |         | MC_DAT1 |        | _REG_IOCTRL_EMMC_DAT1 |
	|         |         |         |        | 0x0300_1060           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | EM      | 3      | FMUX_GPIO             |
	| IOA[25] |         | MC_DAT0 |        | _REG_IOCTRL_EMMC_DAT0 |
	|         |         |         |        | 0x0300_1054           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | EM      | 3      | FMUX_GPIO             |
	| IOA[26] |         | MC_DAT2 |        | _REG_IOCTRL_EMMC_DAT2 |
	|         |         |         |        | 0x0300_104C           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | EM      | 3      | FMUX_GPIO             |
	| IOA[27] |         | MC_DAT3 |        | _REG_IOCTRL_EMMC_DAT3 |
	|         |         |         |        | 0x0300_1058           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | I       | 3      | FMUX_GPI              |
	| IOA[28] |         | IC0_SCL |        | O_REG_IOCTRL_IIC0_SCL |
	|         |         |         |        | 0x0300_1070           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | I       | 3      | FMUX_GPI              |
	| IOA[29] |         | IC0_SDA |        | O_REG_IOCTRL_IIC0_SDA |
	|         |         |         |        | 0x0300_1074           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | AUX0    | 3      | FMUX                  |
	| IOA[30] |         |         |        | _GPIO_REG_IOCTRL_AUX0 |
	|         |         |         |        | 0x0300_1078           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | PW      | 3      | FMUX_GPIO             |
	| PIOB[0] |         | M0_BUCK |        | _REG_IOCTRL_PWM0_BUCK |
	|         |         |         |        | 0x0300_10EC           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | MUX     | 3      | FMUX_GPIO_R           |
	| IOB[10] |         | _SPI1_CS|        | EG_IOCTRL_MUX_SPI1_CS |
	|         |         |         |        | 0x0300_111C           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | GPIO_RT | 3      | FMUX_GPI              |
	| IOB[23] |         | X\_\__E |        | O_REG_IOCTRL_GPIO_RTX |
	|         |         | PHY_RTX |        | 0x0300_11CC           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD     | 3      | FMUX_GPIO_R           |
	| IOB[24] |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXM |
	|         |         | M\_\__E |        | 0x0300_1128           |
	|         |         | PHY_RXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD     | 3      | FMUX_GPIO_R           |
	| IOB[25] |         | _ETH_TX |        | EG_IOCTRL_PAD_ETH_TXP |
	|         |         | P\_\__E |        | 0x0300_1124           |
	|         |         | PHY_RXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD     | 3      | FMUX_GPIO_R           |
	| IOB[26] |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXM |
	|         |         | M\_\__E |        | 0x0300_1130           |
	|         |         | PHY_TXP |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD     | 3      | FMUX_GPIO_R           |
	| IOB[27] |         | _ETH_RX |        | EG_IOCTRL_PAD_ETH_RXP |
	|         |         | P\_\__E |        | 0x0300_112C           |
	|         |         | PHY_TXN |        |                       |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | ADC1    | 3      | FMUX                  |
	| PIOB[3] |         |         |        | _GPIO_REG_IOCTRL_ADC1 |
	|         |         |         |        | 0x0300_10F8           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | USB_V   | 3      | FMUX_GPIO_RE          |
	| PIOB[6] |         | BUS_DET |        | G_IOCTRL_USB_VBUS_DET |
	|         |         |         |        | 0x0300_1108           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | MUX_SP  | 3      | FMUX_GPIO_REG         |
	| PIOB[7] |         | I1_MOSI |        | _IOCTRL_MUX_SPI1_MOSI |
	|         |         |         |        | 0x0300_1118           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | MUX_SP  | 3      | FMUX_GPIO_REG         |
	| PIOB[8] |         | I1_MISO |        | _IOCTRL_MUX_SPI1_MISO |
	|         |         |         |        | 0x0300_1114           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | MUX_S   | 3      | FMUX_GPIO_RE          |
	| PIOB[9] |         | PI1_SCK |        | G_IOCTRL_MUX_SPI1_SCK |
	|         |         |         |        | 0x0300_1120           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIOC[2] |         | IPIRX4N |        | G_IOCTRL_PAD_MIPIRX4N |
	|         |         |         |        | 0x0300_116C           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIOC[3] |         | IPIRX4P |        | G_IOCTRL_PAD_MIPIRX4P |
	|         |         |         |        | 0x0300_1170           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIOC[4] |         | IPIRX3N |        | G_IOCTRL_PAD_MIPIRX3N |
	|         |         |         |        | 0x0300_1174           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIOC[5] |         | IPIRX3P |        | G_IOCTRL_PAD_MIPIRX3P |
	|         |         |         |        | 0x0300_1178           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIOC[6] |         | IPIRX2N |        | G_IOCTRL_PAD_MIPIRX2N |
	|         |         |         |        | 0x0300_117C           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIOC[7] |         | IPIRX2P |        | G_IOCTRL_PAD_MIPIRX2P |
	|         |         |         |        | 0x0300_1180           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIOC[8] |         | IPIRX1N |        | G_IOCTRL_PAD_MIPIRX1N |
	|         |         |         |        | 0x0300_1184           |
	+---------+---------+---------+--------+-----------------------+
	| XG\     | I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| PIOC[9] |         | IPIRX1P |        | G_IOCTRL_PAD_MIPIRX1P |
	|         |         |         |        | 0x0300_1188           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| IOC[10] |         | IPIRX0N |        | G_IOCTRL_PAD_MIPIRX0N |
	|         |         |         |        | 0x0300_118C           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD_M   | 3      | FMUX_GPIO_RE          |
	| IOC[11] |         | IPIRX0P |        | G_IOCTRL_PAD_MIPIRX0P |
	|         |         |         |        | 0x0300_1190           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD_MI  | 3      | FMUX_GPIO_REG_IO      |
	| IOC[12] |         | PI_TXM0 |        | CTRL_PAD_MIPI_TXM0    |
	|         |         |         |        | 0x0300_11B4           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD_MI  | 3      | FMUX_GPIO_REG_IO      |
	| IOC[13] |         | PI_TXP0 |        | CTRL_PAD_MIPI_TXP0    |
	|         |         |         |        | 0x0300_11B8           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD_MI  | 3      | FMUX_GPIO_REG_IO      |
	| IOC[14] |         | PI_TXM1 |        | CTRL_PAD_MIPI_TXM1    |
	|         |         |         |        | 0x0300_11AC           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD_MI  | 3      | FMUX_GPIO_REG_IO      |
	| IOC[15] |         | PI_TXP1 |        | CTRL_PAD_MIPI_TXP1    |
	|         |         |         |        | 0x0300_11B0           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD_MI  | 3      | FMUX_GPIO_REG_IO      |
	| IOC[16] |         | PI_TXM2 |        | CTRL_PAD_MIPI_TXM2    |
	|         |         |         |        | 0x0300_11A4           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD_MI  | 3      | FMUX_GPIO_REG_IO      |
	| IOC[17] |         | PI_TXP2 |        | CTRL_PAD_MIPI_TXP2    |
	|         |         |         |        | 0x0300_11A8           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PA      | 3      | FMUX_GPIO_REG_IO      |
	| IOC[23] |         | D_AUD_A |        | CTRL_PAD_AUD_AINL_MIC |
	|         |         | INL_MIC |        | 0x0300_11BC           |
	+---------+---------+---------+--------+-----------------------+
	| XGP\    | I/O     | PAD_AU  | 3      | FMUX_GPIO_REG_IO      |
	| IOC[24] |         | D_AOUTR |        | CTRL_PAD_AUD_AOUTR    |
	|         |         |         |        | 0x0300_11C8           |
	+---------+---------+---------+--------+-----------------------+

No die domain GPIO
^^^^^^^^^^^^^^^^^^

.. _table_inf_signal_pin_fmux_nodie_domain_gpio:
.. table:: No die domain GPIO
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| PWR\    | I/O     | PW      | 0      | FMUX_GPIO             |
	| _GPIO[0]|         | R_GPIO0 |        | _REG_IOCTRL_PWR_GPIO0 |
	|         |         |         |        | 0x0300_10A4           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I/O     | P       | 3      | FMUX_GPI              |
	| _GPIO[3]|         | WR_SEQ1 |        | O_REG_IOCTRL_PWR_SEQ1 |
	|         |         |         |        | 0x0300_1084           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I/O     | P       | 3      | FMUX_GPI              |
	| _GPIO[4]|         | WR_SEQ2 |        | O_REG_IOCTRL_PWR_SEQ2 |
	|         |         |         |        | 0x0300_1088           |
	+---------+---------+---------+--------+-----------------------+
	| PWR_G\  | I/O     | PWR     | 3      | FMUX_GPIO_R           |
	| PIO[6]  |         | _WAKEUP0|        | EG_IOCTRL_PWR_WAKEUP0 |
	|         |         |         |        | 0x0300_1090           |
	+---------+---------+---------+--------+-----------------------+
	| PWR\    | I/O     | PWR     | 3      | FMUX_GPIO_R           |
	| _GPIO[8]|         | _BUTTON1|        | EG_IOCTRL_PWR_BUTTON1 |
	|         |         |         |        | 0x0300_1098           |
	+---------+---------+---------+--------+-----------------------+
	| PWR_G\  | I/O     | SD1_D3  | 3      | FMUX_G                |
	| PIO[18] |         |         |        | PIO_REG_IOCTRL_SD1_D3 |
	|         |         |         |        | 0x0300_10D0           |
	+---------+---------+---------+--------+-----------------------+
	| PWR_G\  | I/O     | SD1_D2  | 3      | FMUX_G                |
	| PIO[19] |         |         |        | PIO_REG_IOCTRL_SD1_D2 |
	|         |         |         |        | 0x0300_10D4           |
	+---------+---------+---------+--------+-----------------------+
	| PWR_G\  | I/O     | SD1_D1  | 3      | FMUX_G                |
	| PIO[20] |         |         |        | PIO_REG_IOCTRL_SD1_D1 |
	|         |         |         |        | 0x0300_10D8           |
	+---------+---------+---------+--------+-----------------------+
	| PWR_G\  | I/O     | SD1_D0  | 3      | FMUX_G                |
	| PIO[21] |         |         |        | PIO_REG_IOCTRL_SD1_D0 |
	|         |         |         |        | 0x0300_10DC           |
	+---------+---------+---------+--------+-----------------------+
	| PWR_G\  | I/O     | SD1_CMD | 3      | FMUX_GP               |
	| PIO[22] |         |         |        | IO_REG_IOCTRL_SD1_CMD |
	|         |         |         |        | 0x0300_10E0           |
	+---------+---------+---------+--------+-----------------------+
	| PWR_G\  | I/O     | SD1_CLK | 3      | FMUX_GP               |
	| PIO[23] |         |         |        | IO_REG_IOCTRL_SD1_CLK |
	|         |         |         |        | 0x0300_10E4           |
	+---------+---------+---------+--------+-----------------------+
	| PWR_G\  | I/O     | GPIO    | 3      | FMUX_GP               |
	| PIO[24] |         | _ZQ\_\_ |        | IO_REG_IOCTRL_GPIO_ZQ |
	|         |         | _PAD_ZQ |        | 0x0300_11D0           |
	+---------+---------+---------+--------+-----------------------+

Debug
^^^^^

.. _table_inf_signal_pin_fmux_debug:
.. table:: Debug
	:widths: 1 1 1 1 4

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| DBG[0]  | O       | SD0_CLK | 7      | FMUX_GP               |
	|         |         |         |        | IO_REG_IOCTRL_SD0_CLK |
	|         |         |         |        | 0x0300_101C           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[1]  | O       | SD0_CMD | 7      | FMUX_GP               |
	|         |         |         |        | IO_REG_IOCTRL_SD0_CMD |
	|         |         |         |        | 0x0300_1020           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[10] | O       | I       | 7      | FMUX_GPI              |
	|         |         | IC0_SCL |        | O_REG_IOCTRL_IIC0_SCL |
	|         |         |         |        | 0x0300_1070           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[10] | O       | PAD_M   | 7      | FMUX_GPIO_RE          |
	|         |         | IPIRX0N |        | G_IOCTRL_PAD_MIPIRX0N |
	|         |         |         |        | 0x0300_118C           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[11] | O       | I       | 7      | FMUX_GPI              |
	|         |         | IC0_SDA |        | O_REG_IOCTRL_IIC0_SDA |
	|         |         |         |        | 0x0300_1074           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[11] | O       | PAD_M   | 7      | FMUX_GPIO_RE          |
	|         |         | IPIRX0P |        | G_IOCTRL_PAD_MIPIRX0P |
	|         |         |         |        | 0x0300_1190           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[12] | O       | AUX0    | 7      | FMUX                  |
	|         |         |         |        | _GPIO_REG_IOCTRL_AUX0 |
	|         |         |         |        | 0x0300_1078           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[12] | O       | PAD_MI  | 7      | FMUX_GPIO_REG         |
	|         |         | PI_TXM0 |        | _IOCTRL_PAD_MIPI_TXM0 |
	|         |         |         |        | 0x0300_11B4           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[13] | O       | MUX_SP  | 7      | FMUX_GPIO_REG         |
	|         |         | I1_MOSI |        | _IOCTRL_MUX_SPI1_MOSI |
	|         |         |         |        | 0x0300_1118           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[13] | O       | PAD_MI  | 7      | FMUX_GPIO_REG         |
	|         |         | PI_TXP0 |        | _IOCTRL_PAD_MIPI_TXP0 |
	|         |         |         |        | 0x0300_11B8           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[14] | O       | MUX_SP  | 7      | FMUX_GPIO_REG         |
	|         |         | I1_MISO |        | _IOCTRL_MUX_SPI1_MISO |
	|         |         |         |        | 0x0300_1114           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[14] | O       | PAD_MI  | 7      | FMUX_GPIO_REG         |
	|         |         | PI_TXM1 |        | _IOCTRL_PAD_MIPI_TXM1 |
	|         |         |         |        | 0x0300_11AC           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[15] | O       | MUX_S   | 7      | FMUX_GPIO_RE          |
	|         |         | PI1_SCK |        | G_IOCTRL_MUX_SPI1_SCK |
	|         |         |         |        | 0x0300_1120           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[15] | O       | PAD_MI  | 7      | FMUX_GPIO_REG         |
	|         |         | PI_TXP1 |        | _IOCTRL_PAD_MIPI_TXP1 |
	|         |         |         |        | 0x0300_11B0           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[16] | O       | MUX     | 7      | FMUX_GPIO_R           |
	|         |         | _SPI1_CS|        | EG_IOCTRL_MUX_SPI1_CS |
	|         |         |         |        | 0x0300_111C           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[2]  | O       | SD0_D0  | 7      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D0 |
	|         |         |         |        | 0x0300_1024           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[3]  | O       | SD0_D1  | 7      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D1 |
	|         |         |         |        | 0x0300_1028           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[4]  | O       | SD0_D2  | 7      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D2 |
	|         |         |         |        | 0x0300_102C           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[5]  | O       | SD0_D3  | 7      | FMUX_G                |
	|         |         |         |        | PIO_REG_IOCTRL_SD0_D3 |
	|         |         |         |        | 0x0300_1030           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[6]  | O       | U       | 7      | FMUX_GPI              |
	|         |         | ART0_TX |        | O_REG_IOCTRL_UART0_TX |
	|         |         |         |        | 0x0300_1040           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[6]  | O       | PAD_M   | 7      | FMUX_GPIO_RE          |
	|         |         | IPIRX2N |        | G_IOCTRL_PAD_MIPIRX2N |
	|         |         |         |        | 0x0300_117C           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[7]  | O       | U       | 7      | FMUX_GPI              |
	|         |         | ART0_RX |        | O_REG_IOCTRL_UART0_RX |
	|         |         |         |        | 0x0300_1044           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[7]  | O       | PAD_M   | 7      | FMUX_GPIO_RE          |
	|         |         | IPIRX2P |        | G_IOCTRL_PAD_MIPIRX2P |
	|         |         |         |        | 0x0300_1180           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[8]  | O       | PAD_M   | 7      | FMUX_GPIO_RE          |
	|         |         | IPIRX1N |        | G_IOCTRL_PAD_MIPIRX1N |
	|         |         |         |        | 0x0300_1184           |
	+---------+---------+---------+--------+-----------------------+
	| DBG[9]  | O       | PAD_M   | 7      | FMUX_GPIO_RE          |
	|         |         | IPIRX1P |        | G_IOCTRL_PAD_MIPIRX1P |
	|         |         |         |        | 0x0300_1188           |
	+---------+---------+---------+--------+-----------------------+


Others
^^^^^^

.. _table_inf_signal_pin_fmux_others:
.. table:: Others
	:widths: 2 1 1 1 3

	+---------+---------+---------+--------+-----------------------+
	| Signal  |Direction| PinName |Function| Function select       |
	| Name    |         |         |Number  | register              |
	+=========+=========+=========+========+=======================+
	| MUX\    | I/O     | PAD_M   | 7      | FMUX_GPIO_RE          |
	| _SPI1_CS|         | IPIRX4P |        | G_IOCTRL_PAD_MIPIRX4P |
	|         |         |         |        | 0x0300_1170           |
	+---------+---------+---------+--------+-----------------------+
	| MUX_SP\ | I/O     | PAD_M   | 7      | FMUX_GPIO_RE          |
	| I1_MISO |         | IPIRX3N |        | G_IOCTRL_PAD_MIPIRX3N |
	|         |         |         |        | 0x0300_1174           |
	+---------+---------+---------+--------+-----------------------+
	| MUX_SP\ | I/O     | PAD_M   | 7      | FMUX_GPIO_RE          |
	| I1_MOSI |         | IPIRX3P |        | G_IOCTRL_PAD_MIPIRX3P |
	|         |         |         |        | 0x0300_1178           |
	+---------+---------+---------+--------+-----------------------+
	| MUX_S\  | I/O     | PAD_M   | 7      | FMUX_GPIO_RE          |
	| PI1_SCK |         | IPIRX4N |        | G_IOCTRL_PAD_MIPIRX4N |
	|         |         |         |        | 0x0300_116C           |
	+---------+---------+---------+--------+-----------------------+
	| PK\     | I       | PK      | 0      | FMUX_GPIO             |
	| G_TYPE0 |         | G_TYPE0 |        | _REG_IOCTRL_PKG_TYPE0 |
	|         |         |         |        | 0x0300_1104           |
	+---------+---------+---------+--------+-----------------------+
	| PK\     | I       | PK      | 0      | FMUX_GPIO             |
	| G_TYPE1 |         | G_TYPE1 |        | _REG_IOCTRL_PKG_TYPE1 |
	|         |         |         |        | 0x0300_110C           |
	+---------+---------+---------+--------+-----------------------+
	| PK\     | I       | PK      | 0      | FMUX_GPIO             |
	| G_TYPE2 |         | G_TYPE2 |        | _REG_IOCTRL_PKG_TYPE2 |
	|         |         |         |        | 0x0300_1110           |
	+---------+---------+---------+--------+-----------------------+
