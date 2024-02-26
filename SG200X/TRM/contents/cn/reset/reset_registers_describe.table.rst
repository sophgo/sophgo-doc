SOFT_RSTN_0
^^^^^^^^^^^

.. _table_soft_rstn_0:
.. table:: SOFT_RSTN_0, Offset Address: 0x000
	:widths: 1 2 1 4 1
	
	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 1:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg_soft_reset_x_ddr | R/W   | DDR system software    | 0x1  |
	|      |                      |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg                  | R/W   | H264 IP software reset | 0x1  |
	|      | _soft_reset_x_h264c  |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg                  | R/W   | JPEG IP software reset | 0x1  |
	|      | _soft_reset_x_jpeg   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | reg                  | R/W   | H265 IP software reset | 0x1  |
	|      | _soft_reset_x_h265c  |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | reg                  | R/W   | VIP system software    | 0x1  |
	|      | _soft_reset_x_vipsys |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | reg                  | R/W   | TPU_DMA IP software    | 0x1  |
	|      | _soft_reset_x_tdma   |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg_soft_reset_x_tpu | R/W   | TPU IP software reset  | 0x1  |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | reg                  | R/W   | TPU system software    | 0x1  |
	|      | _soft_reset_x_tpusys |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | reg_soft_reset_x_usb | R/W   | USB IP software reset  | 0x1  |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | reg                  | R/W   | ETH0 IP software reset | 0x1  |
	|      | _soft_reset_x_eth0   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | reg                  | R/W   | ETH1 IP software reset | 0x1  |
	|      | _soft_reset_x_eth1   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | reg                  | R/W   | NAND IP software reset | 0x1  |
	|      | _soft_reset_x_nand   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | reg                  | R/W   | EMMC IP software reset | 0x1  |
	|      | _soft_reset_x_emmc   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg_soft_reset_x_sd0 | R/W   | SD0 IP software reset  | 0x1  |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | reg                  | R/W   | SDMA IP software reset | 0x1  |
	|      | _soft_reset_x_sdma   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | reg                  | R/W   | I2S0 IP software reset | 0x1  |
	|      | _soft_reset_x_i2s0   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | reg                  | R/W   | I2S1 IP software reset | 0x1  |
	|      | _soft_reset_x_i2s1   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | reg                  | R/W   | I2S2 IP software reset | 0x1  |
	|      | _soft_reset_x_i2s2   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | reg                  | R/W   | I2S3 IP software reset | 0x1  |
	|      | _soft_reset_x_i2s3   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | reg                  | R/W   | UART0 IP software      | 0x1  |
	|      | _soft_reset_x_uart0  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | reg                  | R/W   | UART1 IP software      | 0x1  |
	|      | _soft_reset_x_uart1  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | reg                  | R/W   | UART2 IP software      | 0x1  |
	|      | _soft_reset_x_uart2  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | reg                  | R/W   | UART3 IP software      | 0x1  |
	|      | _soft_reset_x_uart3  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | reg                  | R/W   | I2C0 IP software reset | 0x1  |
	|      | _soft_reset_x_i2c0   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | reg                  | R/W   | I2C1 IP software reset | 0x1  |
	|      | _soft_reset_x_i2c1   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 29   | reg                  | R/W   | I2C2 IP software reset | 0x1  |
	|      | _soft_reset_x_i2c2   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | reg                  | R/W   | I2C3 IP software reset | 0x1  |
	|      | _soft_reset_x_i2c3   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | reg                  | R/W   | I2C4 IP software reset | 0x1  |
	|      | _soft_reset_x_i2c4   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+

SOFT_RSTN_1
^^^^^^^^^^^

.. _table_soft_rstn_1:
.. table:: SOFT_RSTN_1, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg                  | R/W   | PWM0 IP software reset | 0x1  |
	|      | _soft_reset_x_pwm0   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg                  | R/W   | PWM1 IP software reset | 0x1  |
	|      | _soft_reset_x_pwm1   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg                  | R/W   | PWM2 IP software reset | 0x1  |
	|      | _soft_reset_x_pwm2   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg                  | R/W   | PWM3 IP software reset | 0x1  |
	|      | _soft_reset_x_pwm3   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg                  | R/W   | SPI0 IP software reset | 0x1  |
	|      | _soft_reset_x_spi0   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | reg                  | R/W   | SPI1 IP software reset | 0x1  |
	|      | _soft_reset_x_spi1   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | reg                  | R/W   | SPI2 IP software reset | 0x1  |
	|      | _soft_reset_x_spi2   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | reg                  | R/W   | SPI3 IP software reset | 0x1  |
	|      | _soft_reset_x_spi3   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | reg                  | R/W   | GPIO0 IP software      | 0x1  |
	|      | _soft_reset_x_gpio0  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | reg                  | R/W   | GPIO1 IP software      | 0x1  |
	|      | _soft_reset_x_gpio1  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | reg                  | R/W   | GPIO2 IP software      | 0x1  |
	|      | _soft_reset_x_gpio2  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | reg                  | R/W   | EFUSE IP software      | 0x1  |
	|      | _soft_reset_x_efuse  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg_soft_reset_x_wdt | R/W   | WDT0 IP software reset | 0x1  |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | reg                  | R/W   | ROM IP software reset  | 0x1  |
	|      | _soft_reset_x_ahb_rom|       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | reg                  | R/W   | SPIC IP software reset | 0x1  |
	|      | _soft_reset_x_spic   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | reg                  | R/W   | TEMPSEN IP software    | 0x1  |
	|      | _soft_reset_x_tempsen|       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | reg                  | R/W   | SARADC IP software     | 0x1  |
	|      | _soft_reset_x_saradc |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Reserved             |       |                        |      |
	| 5:21 |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | reg_soft             | R/W   | USB_PHY IP software    | 0x1  |
	|      | _reset_x_combo_phy0  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Reserved             |       |                        |      |
	| 8:27 |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 29   | reg_soft             | R/W   | NAND IP software reset | 0x1  |
	|      | _reset_x_spi_nand    |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | reg_soft_reset_x_se  | R/W   | SE IP software reset   | 0x1  |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SOFT_RSTN_2
^^^^^^^^^^^

.. _table_soft_rstn_2:
.. table:: SOFT_RSTN_2, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | reg                  | R/W   | UART4 IP software      | 0x1  |
	|      | _soft_reset_x_uart4  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | reg                  | R/W   | GPIO3 IP software      | 0x1  |
	|      | _soft_reset_x_gpio3  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | reg                  | R/W   | SYSTEM software reset  | 0x1  |
	|      | _soft_reset_x_system |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | reg                  | R/W   | TIMER IP software      | 0x1  |
	|      | _soft_reset_x_timer  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | reg                  | R/W   | TIMER0 IP software     | 0x1  |
	|      | _soft_reset_x_timer0 |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | reg                  | R/W   | TIMER1 IP software     | 0x1  |
	|      | _soft_reset_x_timer1 |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg                  | R/W   | TIMER2 IP software     | 0x1  |
	|      | _soft_reset_x_timer2 |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | reg                  | R/W   | TIMER3 IP software     | 0x1  |
	|      | _soft_reset_x_timer3 |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | reg                  | R/W   | TIMER4 IP software     | 0x1  |
	|      | _soft_reset_x_timer4 |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | reg                  | R/W   | TIMER5 IP software     | 0x1  |
	|      | _soft_reset_x_timer5 |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | reg                  | R/W   | TIMER6 IP software     | 0x1  |
	|      | _soft_reset_x_timer6 |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | reg                  | R/W   | TIMER7 IP software     | 0x1  |
	|      | _soft_reset_x_timer7 |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | reg                  | R/W   | WGN0 IP software reset | 0x1  |
	|      | _soft_reset_x_wgn0   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | reg                  | R/W   | WGN1 IP software reset | 0x1  |
	|      | _soft_reset_x_wgn1   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | reg                  | R/W   | WGN2 IP software reset | 0x1  |
	|      | _soft_reset_x_wgn2   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | reg                  | R/W   | KEYSCAN IP software    | 0x1  |
	|      | _soft_reset_x_keyscan|       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | reg                  | R/W   | AUDDAC IP software     | 0x1  |
	|      | _soft_reset_x_auddac |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | reg_soft             | R/W   | AUDDAC APB software    | 0x1  |
	|      | _reset_x_auddac_apb  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 29   | reg                  | R/W   | AUDADC IP software     | 0x1  |
	|      | _soft_reset_x_audadc |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | reg                  | R/W   | VCSYS SYS software     | 0x1  |
	|      | _soft_reset_x_vcsys  |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+

SOFT_RSTN_3
^^^^^^^^^^^

.. _table_soft_rstn_3:
.. table:: SOFT_RSTN_3, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg                  | R/W   | ETHPHY IP software     | 0x1  |
	|      | _soft_reset_x_ethphy |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_soft             | R/W   | ETHPHY APB REG         | 0x1  |
	|      | _reset_x_ethphy_apb  |       | software reset (active |      |
	|      |                      |       | low)                   |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg                  | R/W   | AUDSRC IP software     | 0x1  |
	|      | _soft_reset_x_audsrc |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg_soft             | R/W   | VIP CAM0 IP software   | 0x1  |
	|      | _reset_x_vip_cam0    |       | reset (active low)     |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg                  | R/W   | WDT1 IP software reset | 0x1  |
	|      | _soft_reset_x_wdt1   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | reg                  | R/W   | WDT2 IP software reset | 0x1  |
	|      | _soft_reset_x_wdt2   |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SOFT_CPUAC_RSTN
^^^^^^^^^^^^^^^

Write Lock: SOFT_CPUAC_RSTN_wr_lock

.. _table_soft_cpuac_rstn:
.. table:: SOFT_CPUAC_RSTN, Offset Address: 0x020
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg_auto_clear       | R/W   | CPUCORE0               | 0x1  |
	|      | _reset_x_cpucore0    |       | auto_clear_reset       |      |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_auto_clear       | R/W   | CPUCORE1               | 0x1  |
	|      | _reset_x_cpucore1    |       | auto_clear_reset       |      |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg_auto_clear       | R/W   | CPUCORE2               | 0x1  |
	|      | _reset_x_cpucore2    |       | auto_clear_reset       |      |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg_auto_clear       | R/W   | CPUCORE3               | 0x1  |
	|      | _reset_x_cpucore3    |       | auto_clear_reset       |      |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_auto_clear       | R/W   | CPUSYS0                | 0x1  |
	|      | _reset_x_cpusys0     |       | auto_clear_reset       |      |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | reg_auto_clear       | R/W   | CPUSYS1                | 0x1  |
	|      | _reset_x_cpusys1     |       | auto_clear_reset       |      |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | reg_auto_clear       | R/W   | CPUSYS2                | 0x1  |
	|      | _reset_x_cpusys2     |       | auto_clear_reset       |      |
	|      |                      |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 31:7 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SOFT_CPU_RSTN
^^^^^^^^^^^^^

.. _table_soft_cpu_rstn:
.. table:: SOFT_CPU_RSTN, Offset Address: 0x024
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | reg_soft             | R/W   | CPUCORE0 soft reset    | 0x0  |
	|      | _reset_x_cpucore0    |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | reg_soft             | R/W   | CPUCORE1 soft reset    | 0x0  |
	|      | _reset_x_cpucore1    |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | reg_soft             | R/W   | CPUCORE2 soft reset    | 0x0  |
	|      | _reset_x_cpucore2    |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | reg_soft             | R/W   | CPUCORE3 soft reset    | 0x0  |
	|      | _reset_x_cpucore3    |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_soft             | R/W   | CPUSYS0 soft reset     | 0x0  |
	|      | _reset_x_cpusys0     |       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | reg                  | R/W   | CPUSYS1 soft reset     | 0x0  |
	|      | _soft_reset_x_cpusys1|       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | reg                  | R/W   | CPUSYS2 soft reset     | 0x0  |
	|      | _soft_reset_x_cpusys2|       | (active low)           |      |
	+------+----------------------+-------+------------------------+------+
	| 31:7 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
