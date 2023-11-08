
CLKENREG0: offset 0x0000
""""""""""""""""""""""""

.. table:: Clock enable register 0

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31      RW          0x1         Clock Enable for clk_axi_eth0 (1: Enable; 0: Gate)
    30      RW          0x1         Clock Enable for clk_tx_eth0 (1: Enable; 0: Gate)
    29      RW          0x1         Clock Enable for clk_apb_rtc (1: Enable; 0: Gate)
    28      RW          0x1         Clock Enable for clk_apb_pwm (1: Enable; 0: Gate)
    27      RW          0x1         Clock Enable for clk_apb_wdt (1: Enable; 0: Gate)
    26      RW          0x1         Clock Enable for clk_apb_i2c (1: Enable; 0: Gate)
    25      RW          0x1         Clock Enable for clk_apb_spi (1: Enable; 0: Gate)
    24      RW          0x1         Clock Enable for clk_gpio_db (1: Enable; 0: Gate)
    23      RW          0x1         Clock Enable for clk_apb_gpio_intr (1: Enable; 0: Gate)
    22      RW          0x1         Clock Enable for clk_apb_gpio (1: Enable; 0: Gate)
    21      RW          0x1         Clock Enable for clk_apb_efuse (1: Enable; 0: Gate)
    20      RW          0x1         Clock Enable for clk_efuse (1: Enable; 0: Gate)
    19      RW          0x1         Clock Enable for clk_timer_8 (1: Enable; 0: Gate)
    18      RW          0x1         Clock Enable for clk_timer_7 (1: Enable; 0: Gate)
    17      RW          0x1         Clock Enable for clk_timer_6 (1: Enable; 0: Gate)
    16      RW          0x1         Clock Enable for clk_timer_5 (1: Enable; 0: Gate)
    15      RW          0x1         Clock Enable for clk_timer_4 (1: Enable; 0: Gate)
    14      RW          0x1         Clock Enable for clk_timer_3 (1: Enable; 0: Gate)
    13      RW          0x1         Clock Enable for clk_timer_2 (1: Enable; 0: Gate)
    12      RW          0x1         Clock Enable for clk_timer_1 (1: Enable; 0: Gate)
    11      RW          0x1         Clock Enable for clk_apb_timer (1: Enable; 0: Gate)
    10      RW          0x1         Clock Enable for clk_axi_sram (1: Enable; 0: Gate)
    9       RW          0x1         Clock Enable for clk_ahb_sf (1: Enable; 0: Gate)
    8       RW          0x1         Clock Enable for clk_ahb_rom (1: Enable; 0: Gate)
    7       RW          0x1         Clock Enable for clk_ahb_lpc (1: Enable; 0: Gate)
    6       RW          0x1         Clock Enable for clk_axi_dbg_i2c (1: Enable; 0: Gate)
    5       RW          0x1         Clock Enable for clk_apb_uart (1: Enable; 0: Gate)
    4       RW          0x1         Clock Enable for clk_uart_500m (1: Enable; 0: Gate)
    3       RW          0x1         Clock Enable for clk_sysdma_axi (1: Enable; 0: Gate)
    2       RW          0x1         Clock Enable for clk_slc (1: Enable; 0: Gate)
    1       RW          0x1         Clock Enable for clk_scp_timer (1: Enable; 0: Gate)
    0       RW          0x1         Clock Enable for clk_rp_cpu_normal (1: Enable; 0: Gate)
    =====   =========   =======     ===========


CLKENREG1: offset 0x0004
""""""""""""""""""""""""

.. table:: Clock enable register 1

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          NA          Reserved
    15      RW          0x1         Clock Enable for clk_ddr23 (1: Enable; 0: Gate)
    14      RW          0x1         Clock Enable for clk_ddr01 (1: Enable; 0: Gate)
    13      RW          0x1         Clock Enable for clk_axi_ddr (1: Enable; 0: Gate)
    12      RW          0x1         Clock Enable for clk_top_axi_hsperi (1: Enable; 0: Gate)
    11      RW          0x1         Clock Enable for clk_top_axi0 (1: Enable; 0: Gate)
    10      RW          0x1         Clock Enable for clk_hsdma (1: Enable; 0: Gate)
    9       RW          0x1         Clock Enable for clk_axi_pcie1 (1: Enable; 0: Gate)
    8       RW          0x1         Clock Enable for clk_axi_pcie0 (1: Enable; 0: Gate)
    7       RW          0x1         Clock Enable for clk_100k_sd (1: Enable; 0: Gate)
    6       RW          0x1         Clock Enable for clk_sd (1: Enable; 0: Gate)
    5       RW          0x1         Clock Enable for clk_axi_sd (1: Enable; 0: Gate)
    4       RW          0x1         Clock Enable for clk_100k_emmc (1: Enable; 0: Gate)
    3       RW          0x1         Clock Enable for clk_emmc (1: Enable; 0: Gate)
    2       RW          0x1         Clock Enable for clk_axi_emmc (1: Enable; 0: Gate)
    1       RW          0x1         Clock Enable for clk_ref_eth0 (1: Enable; 0: Gate)
    0       RW          0x1         Clock Enable for clk_ptp_ref_i_eth0 (1: Enable; 0: Gate)
    =====   =========   =======     ===========


CLKSELREG0: offset 0x0020
"""""""""""""""""""""""""

.. table:: Clock select register 0

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:4    RW          NA          Reserved
    3       RW          0x1         Clock Select for DDR23's clock core_ddrc_core_clk (aka clk_ddr23)
                                    1: Select in_dpll1_clk as clock source
                                    0: Select in_fpll_clk as clock source
    2       RW          0x1         Clock Select for DDR01's clock core_ddrc_core_clk (aka clk_ddr01)
                                    1: Select in_dpll0_clk as clock source
                                    0: Select in_fpll_clk as clock source
    1       RW          0x1         Clock Select for FABRIC_AXI_DDR's clock aclk (aka clk_axi_ddr)
                                    1: Select in_mpll_clk as clock source
                                    0: Select in_fpll_clk as clock source
    0       RW          0x1         Clock Select for RP's clock top_rp_cpu_clk_normal (aka clk_rp_cpu_normal)
                                    1: Select in_mpll_clk as clock source
                                    0: Select in_fpll_clk as clock source
    =====   =========   =======     ===========


CLKDIVREG0: offset 0x0040
"""""""""""""""""""""""""

.. table:: Clock divider 0 control of RISC-V core

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:5    RW          NA          Reserved
    4       RW          0x0         Clock Enable for this Branch Divider
                                    0: Gate this Branch Divider
                                    1: Enable this Branch Divider
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========

CLKDIVREG1: offset 0x0044
"""""""""""""""""""""""""

.. table:: Clock divider 1 control of RISC-V core

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:5    RW          NA          Reserved
    4       RW          0x0         Clock Enable for this Branch Divider
                                    0: Gate this Branch Divider
                                    1: Enable this Branch Divider
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========

CLKDIVREG2: offset 0x0048
"""""""""""""""""""""""""

.. table:: Clock divider control of SCP timer

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:24   RW          NA          Reserved
    23:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========


CLKDIVREG3: offset 0x004c
"""""""""""""""""""""""""

.. table:: Clock divider control of SLC

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========


CLKDIVREG4: offset 0x0050
"""""""""""""""""""""""""

.. table:: Clock divider control of UART

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:23   RW          NA          Reserved
    22:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========


CLKDIVREG5: offset 0x0054
"""""""""""""""""""""""""

.. table:: Clock divider control of LPC

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========


CLKDIVREG6: offset 0x0058
"""""""""""""""""""""""""

.. table:: Clock divider control of TIMER1

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========


CLKDIVREG7: offset 0x005c
"""""""""""""""""""""""""

.. table:: Clock divider control of TIMER2

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========


CLKDIVREG8: offset 0x0060
"""""""""""""""""""""""""

.. table:: Clock divider control of TIMER3

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========


CLKDIVREG9: offset 0x0064
"""""""""""""""""""""""""

.. table:: Clock divider control of TIMER4

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========


CLKDIVREG10: offset 0x0068
""""""""""""""""""""""""""

.. table:: Clock divider control of TIMER5

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG11: offset 0x006c
""""""""""""""""""""""""""

.. table:: Clock divider control of TIMER6
    
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG12: offset 0x0070
""""""""""""""""""""""""""

.. table:: Clock divider control of TIMER7
   
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========

    
CLKDIVREG13: offset 0x0074
""""""""""""""""""""""""""

.. table:: Clock divider control of TIMER8
   
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========

    
CLKDIVREG14: offset 0x0078
""""""""""""""""""""""""""

.. table:: Clock divider control of eFuse
   
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:23   RW          NA          Reserved
    22:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG15: offset 0x007c
""""""""""""""""""""""""""

.. table:: Clock divider control of GPIO DB

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG16: offset 0x0080
""""""""""""""""""""""""""

.. table:: Clock divider control of ETH TX
    
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:27   RW          NA          Reserved
    26:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    
    
CLKDIVREG17: offset 0x0084
""""""""""""""""""""""""""

.. table:: Clock divider control of ETH PTP

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:24   RW          NA          Reserved
    23:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG18: offset 0x0088
""""""""""""""""""""""""""

.. table:: Clock divider control of ETH
    
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:24   RW          NA          Reserved
    23:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG19: offset 0x008c
""""""""""""""""""""""""""

.. table:: Clock divider control of eMMC
    
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG20: offset 0x0090
""""""""""""""""""""""""""

.. table:: Clock divider control of eMMC 100k
   
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG21: offset 0x0094
""""""""""""""""""""""""""

.. table:: Clock divider control of SDIO

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG22: offset 0x0098
""""""""""""""""""""""""""

.. table:: Clock divider control of SDIO 100k

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG23: offset 0x009c
""""""""""""""""""""""""""

.. table:: Clock divider control of TOP AXI0

    
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RO          0x0         Select Divide Factor from Register
                                    This bit is reserved for this divider.
    2       RO          0x0         Select High Wide Control from Register
                                    This bit is reserved for this divider.
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RO          0x1         Divider Reset Control
                                    This bit is reserved for this divider.
    =====   =========   =======     ===========
    

CLKDIVREG24: offset 0x00a0
""""""""""""""""""""""""""

.. table:: Clock divider control of TOP AXI0

    
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:4    RW          NA          Reserved
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========

    
CLKDIVREG25: offset 0x00a4
""""""""""""""""""""""""""

.. table:: Clock divider 0 control of AXI DDR

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:5    RW          NA          Reserved
    4       RW          0x0         Clock Enable for this Branch Divider
                                    0: Gate this Branch Divider
                                    1: Enable this Branch Divider
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    
CLKDIVREG26: offset 0x00a8
""""""""""""""""""""""""""

.. table:: Clock divider 1 control of AXI DDR
   
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:5    RW          NA          Reserved
    4       RW          0x0         Clock Enable for this Branch Divider
                                    0: Gate this Branch Divider
                                    1: Enable this Branch Divider
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG27: offset 0x00ac
""""""""""""""""""""""""""

.. table:: Clock divider 0 control of DDR01
   
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:5    RW          NA          Reserved
    4       RW          0x0         Clock Enable for this Branch Divider
                                    0: Gate this Branch Divider
                                    1: Enable this Branch Divider
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    

CLKDIVREG28: offset 0x00b0
""""""""""""""""""""""""""

.. table:: Clock divider 1 control of DDR01

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:5    RW          NA          Reserved
    4       RW          0x0         Clock Enable for this Branch Divider
                                    0: Gate this Branch Divider
                                    1: Enable this Branch Divider
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    
    
CLKDIVREG29: offset 0x00b4
""""""""""""""""""""""""""

.. table:: Clock divider 0 control of DDR23

    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:5    RW          NA          Reserved
    4       RW          0x0         Clock Enable for this Branch Divider
                                    0: Gate this Branch Divider
                                    1: Enable this Branch Divider
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========


CLKDIVREG30: offset 0x00b8
""""""""""""""""""""""""""

.. table:: Clock divider 1 control of DDR23
    
    =====   =========   =======     ===========
    Bits    Attribute   Default     Description
    =====   =========   =======     ===========
    31:21   RW          NA          Reserved
    20:16   RW          0x0         Clock Divider Factor
    15:5    RW          NA          Reserved
    4       RW          0x0         Clock Enable for this Branch Divider
                                    0: Gate this Branch Divider
                                    1: Enable this Branch Divider
    3       RW          0x0         Select Divide Factor from Register
                                    0: Select initial value
                                    1: Select Divide Factor from this register
    2       RW          0x0         Select High Wide Control from Register
                                    0: Select initial value
                                    1: Select High Wide from this register
    1       RW          0x0         High Wide Control (when Divider Factor is odd)
                                    0: Low level of the clock is wider
                                    1: High level of the clock is wider
    0       RW          0x1         Divider Reset Control
                                    0: Assert Reset
                                    1: De-assert Reset
    =====   =========   =======     ===========
    
