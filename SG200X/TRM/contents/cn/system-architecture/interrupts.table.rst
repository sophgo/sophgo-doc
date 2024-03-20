.. _table_a53_interrupts_map:
.. table:: Interrupt number and Interrupt source mapping for ARM Cortex-A53
	:widths: 1 2 1 2 1 2

	======  ==================  ======  ===================  ======  ============
	INT #   INT Source          INT     INT Source           INT #   INT Source
	======  ==================  ======  ===================  ======  ============
	32      TEMPSENS            70      SPI1                 108     TRNG
	33      RTC Alarm           71      SPI2                 109     ddr_axi_mon
	34      RTC Longpress       72      SPI3                 110     ddr_pi_phy
	35      VBAT DET            73      SPI4                 111     SPI_NOR
	36      JPEG                74      WatchDog0            112     EPHY
	37      H264                75      KEYSCAN              113     IVE
	38      H265                76      GPIO0                114     Reserved
	39      VC SBM              77      GPIO1                115     Reserved
	40      ISP                 78      GPIO2                116     SARADC
	41      SC_TOP              79      GPIO3                117     mbox
	42      CSI_MAC0            80      Wiegand0             151     npmuirq[0]
	43      CSI_MAC1            81      Wiegand1             152     ctiirq[0]
	44      LDC                 82      Wiegand2             159     nexterrirq
	45      System DMA          83      RTC MBOX             116     SARADC
	46      USB                 84      N/A                  \       \
	47      Ethnet0             85      RTC IRRX             \       \
	48      Ethnet0             86      RTC GPIO             \       \
	49      EMMC Wakup          87      RTC UART             \       \
	50      EMMC                88      RTC SPI_NOR          \       \
	51      SD0 Wakup           89      RTC I2C              \       \
	52      SD0                 90      RTC WDG              \       \
	53      SD1 Wakup           91      TPU                  \       \
	54      SD1                 92      TDMA                 \       \
	55      SPI_NAND            93      Reserved             \       \
	56      I2S0                94      Reserved             \       \
	57      I2S1                95      Timer0               \       \
	58      I2S2                96      Timer1               \       \
	59      I2S3                97      Timer2               \       \
	60      UART0               98      Timer3               \       \
	61      UART1               99      Timer4               \       \
	62      UART2               100     Timer5               \       \
	63      UART3               101     Timer6               \       \
	64      UART4               102     Timer7               \       \
	65      I2C0                103     peri_firewall        \       \
	66      I2C1                104     hsperi_firewall      \       \
	67      I2C2                105     ddr_fw               \       \
	68      I2C3                106     rom_firewall         \       \
	69      I2C4                107     SPACC                \       \
	======  ==================  ======  ===================  ======  ============


.. _table_c906-master_interrupts_map:
.. table:: Interrupt number and Interrupt source mapping for Master RISCV C906 @ 1.0Ghz
	:widths: 1 2 1 2 1 2

	======  ==================  ======  ==================  ======  ======
	INT #   INT Source          INT #   INT Source          INT #   INT Source
	======  ==================  ======  ==================  ======  ======
	16      TEMPSENS            52      I2C3                88      hsperi_firewall
	17      RTC Alarm           53      I2C4                89      ddr_fw
	18      RTC Longpress       54      SPI1                90      rom_firewall
	19      VBAT DET            55      SPI2                91      SPACC
	20      JPEG                56      SPI3                92      TRNG
	21      H264                57      SPI4                93      ddr_axi_mon
	22      H265                58      WatchDog1           94      ddr_pi_phy
	23      VC SBM              59      KEYSCAN             95      SPI_NOR
	24      ISP                 60      GPIO0               96      EPHY
	25      SC_TOP              61      GPIO1               97      IVE
	26      CSI_MAC0            62      GPIO2               98      Reserved
	27      CSI_MAC1            63      GPIO3               99      Reserved
	28      LDC                 64      Wiegand0            100     SARADC
	29      System DMA          65      Wiegand1            101     mbox
	30      USB                 66      Wiegand2            \       \
	31      Ethnet0             67      RTC MBOX            \       \
	32      Ethnet0             68      N/A                 \       \
	33      EMMC Wakup          69      RTC IRRX            \       \
	34      EMMC                70      RTC GPIO            \       \
	35      SD0 Wakup           71      RTC UART            \       \
	36      SD0                 72      RTC SPI_NOR         \       \
	37      SD1 Wakup           73      RTC I2C             \       \
	38      SD1                 74      RTC WDG             \       \
	39      SPI_NAND            75      TPU                 \       \
	40      I2S0                76      TDMA                \       \
	41      I2S1                77      Reserved            \       \
	42      I2S2                78      Reserved            \       \
	43      I2S3                79      Timer0              \       \
	44      UART0               80      Timer1              \       \
	45      UART1               81      Timer2              \       \
	46      UART2               82      Timer3              \       \
	47      UART3               83      Timer4              \       \
	48      UART4               84      Timer5              \       \
	49      I2C0                85      Timer6              \       \
	50      I2C1                86      Timer7              \       \
	51      I2C2                87      peri_firewall       \       \
	======  ==================  ======  ==================  ======  ======

.. _table_c906-slave_interrupts_map:
.. table:: Interrupt number and Interrupt source mapping for Slave RISCV C906 @ 700Mhz
	:widths: 1 2 1 2 1 2

	======  ===============  ======  ===============  ======  ======
	INT #   INT Source       INT #   INT Source       INT #   INT Source
	======  ===============  ======  ===============  ======  ======
	16      JPEG             32      I2C0             48      RTC GPIO
	17      H264             33      I2C1             49      RTC UART
	18      H265             34      I2C2             50      RTC I2C
	19      VC SBM           35      I2C3             51      RTC WDG
	20      ISP              36      I2C4             52      TDMA
	21      SC_TOP           37      SPI1             53      Reserved
	22      CSI_MAC0         38      SPI2             54      Reserved
	23      CSI_MAC1         39      WatchDog2        55      Timer4
	24      LDC              40      KEYSCAN          56      Timer5
	25      System DMA       41      GPIO0            57      Timer6
	26      I2S0             42      GPIO1            58      Timer7
	27      I2S1             43      GPIO2            59      SPACC
	28      I2S2             44      GPIO3            60      IVE
	29      I2S3             45      Wiegand0         61      mbox
	30      UART0            46      RTC MBOX         \       \
	31      UART1            47      RTC IRRX         \       \
	======  ===============  ======  ===============  ======  ======
