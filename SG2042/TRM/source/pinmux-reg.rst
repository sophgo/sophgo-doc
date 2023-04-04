

REG00: offset 0x0000
""""""""""""""""""""

.. table:: LPC_LCLK and LPC_LFRAME

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for LPC_LFRAME. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for LPC_LFRAME. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for LPC_LFRAME
    21:20   RW          0x0         Pin Mux Selector for LPC_LFRAME
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for LPC_LFRAME. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for LPC_LFRAME.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for LPC_LCLK. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for LPC_LCLK. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for LPC_LCLK
    5:4     RW          0x0         Pin Mux Selector for LPC_LCLK
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for LPC_LCLK. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for LPC_LCLK.
    ======  ====        =======     ========


REG01: offset 0x0004
""""""""""""""""""""

.. table:: LPC_LAD0 and LPC_LAD1

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for LPC_LAD1. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for LPC_LAD1. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for LPC_LAD1
    21:20   RW          0x0         Pin Mux Selector for LPC_LAD1
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for LPC_LAD1. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for LPC_LAD1.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for LPC_LAD0. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for LPC_LAD0. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for LPC_LAD0
    5:4     RW          0x0         Pin Mux Selector for LPC_LAD0
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for LPC_LAD0. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for LPC_LAD0.
    ======  ====        =======     ========


REG02: offset 0x0008
""""""""""""""""""""

.. table:: LPC_LAD2 and LPC_LAD3

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for LPC_LAD3. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for LPC_LAD3. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for LPC_LAD3
    21:20   RW          0x0         Pin Mux Selector for LPC_LAD3
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for LPC_LAD3. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for LPC_LAD3.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for LPC_LAD2. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for LPC_LAD2. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for LPC_LAD2
    5:4     RW          0x0         Pin Mux Selector for LPC_LAD2
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for LPC_LAD2. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for LPC_LAD2.
    ======  ====        =======     ========


REG03: offset 0x000c
""""""""""""""""""""

.. table:: LPC_LDRQ0 and LPC_LDRQ1

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for LPC_LDRQ1. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for LPC_LDRQ1. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for LPC_LDRQ1
    21:20   RW          0x0         Pin Mux Selector for LPC_LDRQ1
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for LPC_LDRQ1. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for LPC_LDRQ1.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for LPC_LDRQ0. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for LPC_LDRQ0. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for LPC_LDRQ0
    5:4     RW          0x0         Pin Mux Selector for LPC_LDRQ0
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for LPC_LDRQ0. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for LPC_LDRQ0.
    ======  ====        =======     ========


REG04: offset 0x0010
""""""""""""""""""""

.. table:: LPC_SERIRQ and LPC_CLKRUN

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for LPC_CLKRUN. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for LPC_CLKRUN. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for LPC_CLKRUN
    21:20   RW          0x0         Pin Mux Selector for LPC_CLKRUN
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for LPC_CLKRUN. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for LPC_CLKRUN.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for LPC_SERIRQ. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for LPC_SERIRQ. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for LPC_SERIRQ
    5:4     RW          0x0         Pin Mux Selector for LPC_SERIRQ
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for LPC_SERIRQ. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for LPC_SERIRQ.
    ======  ====        =======     ========


REG05: offset 0x0014
""""""""""""""""""""

.. table:: LPC_LPME and LPC_LPCPD

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for LPC_LPCPD. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for LPC_LPCPD. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for LPC_LPCPD
    21:20   RW          0x0         Pin Mux Selector for LPC_LPCPD
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for LPC_LPCPD. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for LPC_LPCPD.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for LPC_LPME. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for LPC_LPME. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for LPC_LPME
    5:4     RW          0x0         Pin Mux Selector for LPC_LPME
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for LPC_LPME. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for LPC_LPME.
    ======  ====        =======     ========


REG06: offset 0x0018
""""""""""""""""""""

.. table:: LPC_LSMI and PCIE0_L0_RESET_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for PCIE0_L0_RESET_X. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for PCIE0_L0_RESET_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for PCIE0_L0_RESET_X
    21:20   RW          0x0         Pin Mux Selector for PCIE0_L0_RESET_X
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for PCIE0_L0_RESET_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for PCIE0_L0_RESET_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for LPC_LSMI. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for LPC_LSMI. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for LPC_LSMI
    5:4     RW          0x0         Pin Mux Selector for LPC_LSMI
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for LPC_LSMI. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for LPC_LSMI.
    ======  ====        =======     ========


REG07: offset 0x001c
""""""""""""""""""""

.. table:: PCIE0_L1_RESET_X and PCIE0_L0_WAKEUP_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for PCIE0_L0_WAKEUP_X. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for PCIE0_L0_WAKEUP_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for PCIE0_L0_WAKEUP_X
    21:20   RW          0x0         Pin Mux Selector for PCIE0_L0_WAKEUP_X
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for PCIE0_L0_WAKEUP_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for PCIE0_L0_WAKEUP_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for PCIE0_L1_RESET_X. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for PCIE0_L1_RESET_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for PCIE0_L1_RESET_X
    5:4     RW          0x0         Pin Mux Selector for PCIE0_L1_RESET_X
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for PCIE0_L1_RESET_X. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for PCIE0_L1_RESET_X.
    ======  ====        =======     ========


REG08: offset 0x0020
""""""""""""""""""""

.. table:: PCIE0_L1_WAKEUP_X and PCIE0_L0_CLKREQ_IN_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for PCIE0_L0_CLKREQ_IN_X. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for PCIE0_L0_CLKREQ_IN_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for PCIE0_L0_CLKREQ_IN_X
    21:20   RW          0x0         Pin Mux Selector for PCIE0_L0_CLKREQ_IN_X
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for PCIE0_L0_CLKREQ_IN_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for PCIE0_L0_CLKREQ_IN_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for PCIE0_L1_WAKEUP_X. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for PCIE0_L1_WAKEUP_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for PCIE0_L1_WAKEUP_X
    5:4     RW          0x0         Pin Mux Selector for PCIE0_L1_WAKEUP_X
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for PCIE0_L1_WAKEUP_X. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for PCIE0_L1_WAKEUP_X.
    ======  ====        =======     ========


REG09: offset 0x0024
""""""""""""""""""""

.. table:: PCIE0_L1_CLKREQ_IN_X and PCIE1_L0_RESET_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for PCIE1_L0_RESET_X. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for PCIE1_L0_RESET_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for PCIE1_L0_RESET_X
    21:20   RW          0x0         Pin Mux Selector for PCIE1_L0_RESET_X
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for PCIE1_L0_RESET_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for PCIE1_L0_RESET_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for PCIE0_L1_CLKREQ_IN_X. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for PCIE0_L1_CLKREQ_IN_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for PCIE0_L1_CLKREQ_IN_X
    5:4     RW          0x0         Pin Mux Selector for PCIE0_L1_CLKREQ_IN_X
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for PCIE0_L1_CLKREQ_IN_X. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for PCIE0_L1_CLKREQ_IN_X.
    ======  ====        =======     ========


REG0a: offset 0x0028
""""""""""""""""""""

.. table:: PCIE1_L1_RESET_X and PCIE1_L0_WAKEUP_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for PCIE1_L0_WAKEUP_X. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for PCIE1_L0_WAKEUP_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for PCIE1_L0_WAKEUP_X
    21:20   RW          0x0         Pin Mux Selector for PCIE1_L0_WAKEUP_X
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for PCIE1_L0_WAKEUP_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for PCIE1_L0_WAKEUP_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for PCIE1_L1_RESET_X. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for PCIE1_L1_RESET_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for PCIE1_L1_RESET_X
    5:4     RW          0x0         Pin Mux Selector for PCIE1_L1_RESET_X
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for PCIE1_L1_RESET_X. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for PCIE1_L1_RESET_X.
    ======  ====        =======     ========


REG0b: offset 0x002c
""""""""""""""""""""

.. table:: PCIE1_L1_WAKEUP_X and PCIE1_L0_CLKREQ_IN_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for PCIE1_L0_CLKREQ_IN_X. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for PCIE1_L0_CLKREQ_IN_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for PCIE1_L0_CLKREQ_IN_X
    21:20   RW          0x0         Pin Mux Selector for PCIE1_L0_CLKREQ_IN_X
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for PCIE1_L0_CLKREQ_IN_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for PCIE1_L0_CLKREQ_IN_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for PCIE1_L1_WAKEUP_X. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for PCIE1_L1_WAKEUP_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for PCIE1_L1_WAKEUP_X
    5:4     RW          0x0         Pin Mux Selector for PCIE1_L1_WAKEUP_X
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for PCIE1_L1_WAKEUP_X. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for PCIE1_L1_WAKEUP_X.
    ======  ====        =======     ========


REG0c: offset 0x0030
""""""""""""""""""""

.. table:: PCIE1_L1_CLKREQ_IN_X and SPIF0_CLK_SEL1

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPIF0_CLK_SEL1. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPIF0_CLK_SEL1. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPIF0_CLK_SEL1
    21:20   RW          0x0         Pin Mux Selector for SPIF0_CLK_SEL1
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPIF0_CLK_SEL1. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPIF0_CLK_SEL1.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for PCIE1_L1_CLKREQ_IN_X. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for PCIE1_L1_CLKREQ_IN_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for PCIE1_L1_CLKREQ_IN_X
    5:4     RW          0x0         Pin Mux Selector for PCIE1_L1_CLKREQ_IN_X
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for PCIE1_L1_CLKREQ_IN_X. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for PCIE1_L1_CLKREQ_IN_X.
    ======  ====        =======     ========


REG0d: offset 0x0034
""""""""""""""""""""

.. table:: SPIF0_CLK_SEL0 and SPIF0_WP_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPIF0_WP_X. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPIF0_WP_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPIF0_WP_X
    21:20   RW          0x0         Pin Mux Selector for SPIF0_WP_X
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPIF0_WP_X. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPIF0_WP_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPIF0_CLK_SEL0. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPIF0_CLK_SEL0. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPIF0_CLK_SEL0
    5:4     RW          0x0         Pin Mux Selector for SPIF0_CLK_SEL0
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPIF0_CLK_SEL0. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPIF0_CLK_SEL0.
    ======  ====        =======     ========


REG0e: offset 0x0038
""""""""""""""""""""

.. table:: SPIF0_HOLD_X and SPIF0_SDI

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPIF0_SDI. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPIF0_SDI. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPIF0_SDI
    21:20   RW          0x0         Pin Mux Selector for SPIF0_SDI
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPIF0_SDI. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPIF0_SDI.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPIF0_HOLD_X. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPIF0_HOLD_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPIF0_HOLD_X
    5:4     RW          0x0         Pin Mux Selector for SPIF0_HOLD_X
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPIF0_HOLD_X. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPIF0_HOLD_X.
    ======  ====        =======     ========


REG0f: offset 0x003c
""""""""""""""""""""

.. table:: SPIF0_CS_X and SPIF0_SCK

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPIF0_SCK. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPIF0_SCK. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPIF0_SCK
    21:20   RW          0x0         Pin Mux Selector for SPIF0_SCK
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPIF0_SCK. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPIF0_SCK.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPIF0_CS_X. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPIF0_CS_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPIF0_CS_X
    5:4     RW          0x0         Pin Mux Selector for SPIF0_CS_X
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPIF0_CS_X. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPIF0_CS_X.
    ======  ====        =======     ========


REG10: offset 0x0040
""""""""""""""""""""

.. table:: SPIF0_SDO and SPIF1_CLK_SEL1

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPIF1_CLK_SEL1. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPIF1_CLK_SEL1. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPIF1_CLK_SEL1
    21:20   RW          0x0         Pin Mux Selector for SPIF1_CLK_SEL1
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPIF1_CLK_SEL1. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPIF1_CLK_SEL1.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPIF0_SDO. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPIF0_SDO. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPIF0_SDO
    5:4     RW          0x0         Pin Mux Selector for SPIF0_SDO
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPIF0_SDO. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPIF0_SDO.
    ======  ====        =======     ========


REG11: offset 0x0044
""""""""""""""""""""

.. table:: SPIF1_CLK_SEL0 and SPIF1_WP_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPIF1_WP_X. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPIF1_WP_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPIF1_WP_X
    21:20   RW          0x0         Pin Mux Selector for SPIF1_WP_X
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPIF1_WP_X. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPIF1_WP_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPIF1_CLK_SEL0. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPIF1_CLK_SEL0. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPIF1_CLK_SEL0
    5:4     RW          0x0         Pin Mux Selector for SPIF1_CLK_SEL0
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPIF1_CLK_SEL0. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPIF1_CLK_SEL0.
    ======  ====        =======     ========


REG12: offset 0x0048
""""""""""""""""""""

.. table:: SPIF1_HOLD_X and SPIF1_SDI

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPIF1_SDI. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPIF1_SDI. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPIF1_SDI
    21:20   RW          0x0         Pin Mux Selector for SPIF1_SDI
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPIF1_SDI. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPIF1_SDI.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPIF1_HOLD_X. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPIF1_HOLD_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPIF1_HOLD_X
    5:4     RW          0x0         Pin Mux Selector for SPIF1_HOLD_X
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPIF1_HOLD_X. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPIF1_HOLD_X.
    ======  ====        =======     ========


REG13: offset 0x004c
""""""""""""""""""""

.. table:: SPIF1_CS_X and SPIF1_SCK

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPIF1_SCK. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPIF1_SCK. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPIF1_SCK
    21:20   RW          0x0         Pin Mux Selector for SPIF1_SCK
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPIF1_SCK. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPIF1_SCK.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPIF1_CS_X. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPIF1_CS_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPIF1_CS_X
    5:4     RW          0x0         Pin Mux Selector for SPIF1_CS_X
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPIF1_CS_X. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPIF1_CS_X.
    ======  ====        =======     ========


REG14: offset 0x0050
""""""""""""""""""""

.. table:: SPIF1_SDO and EMMC_WP

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for EMMC_WP. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for EMMC_WP. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for EMMC_WP
    21:20   RW          0x0         Pin Mux Selector for EMMC_WP
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for EMMC_WP. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for EMMC_WP.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPIF1_SDO. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPIF1_SDO. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPIF1_SDO
    5:4     RW          0x0         Pin Mux Selector for SPIF1_SDO
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPIF1_SDO. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPIF1_SDO.
    ======  ====        =======     ========


REG15: offset 0x0054
""""""""""""""""""""

.. table:: EMMC_CD_X and EMMC_RST_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for EMMC_RST_X. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for EMMC_RST_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for EMMC_RST_X
    21:20   RW          0x0         Pin Mux Selector for EMMC_RST_X
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for EMMC_RST_X. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for EMMC_RST_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for EMMC_CD_X. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for EMMC_CD_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for EMMC_CD_X
    5:4     RW          0x0         Pin Mux Selector for EMMC_CD_X
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for EMMC_CD_X. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for EMMC_CD_X.
    ======  ====        =======     ========


REG16: offset 0x0058
""""""""""""""""""""

.. table:: EMMC_PWR_EN and SDIO_CD_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SDIO_CD_X. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for SDIO_CD_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SDIO_CD_X
    21:20   RW          0x0         Pin Mux Selector for SDIO_CD_X
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for SDIO_CD_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for SDIO_CD_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for EMMC_PWR_EN. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for EMMC_PWR_EN. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for EMMC_PWR_EN
    5:4     RW          0x0         Pin Mux Selector for EMMC_PWR_EN
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for EMMC_PWR_EN. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for EMMC_PWR_EN.
    ======  ====        =======     ========


REG17: offset 0x005c
""""""""""""""""""""

.. table:: SDIO_WP and SDIO_RST_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SDIO_RST_X. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SDIO_RST_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SDIO_RST_X
    21:20   RW          0x0         Pin Mux Selector for SDIO_RST_X
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SDIO_RST_X. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SDIO_RST_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SDIO_WP. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for SDIO_WP. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SDIO_WP
    5:4     RW          0x0         Pin Mux Selector for SDIO_WP
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SDIO_WP. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SDIO_WP.
    ======  ====        =======     ========


REG18: offset 0x0060
""""""""""""""""""""

.. table:: SDIO_PWR_EN and RGMII0_TXD0

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for RGMII0_TXD0. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for RGMII0_TXD0. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for RGMII0_TXD0
    21:20   RW          0x0         Pin Mux Selector for RGMII0_TXD0
    19      RW          0x0         Pull Down Enable for RGMII0_TXD0
    18      RW          0x0         Pull Up Enable for RGMII0_TXD0
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SDIO_PWR_EN. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SDIO_PWR_EN. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SDIO_PWR_EN
    5:4     RW          0x0         Pin Mux Selector for SDIO_PWR_EN
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SDIO_PWR_EN. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SDIO_PWR_EN.
    ======  ====        =======     ========


REG19: offset 0x0064
""""""""""""""""""""

.. table:: RGMII0_TXD1 and RGMII0_TXD2

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for RGMII0_TXD2. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for RGMII0_TXD2. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for RGMII0_TXD2
    21:20   RW          0x0         Pin Mux Selector for RGMII0_TXD2
    19      RW          0x0         Pull Down Enable for RGMII0_TXD2
    18      RW          0x0         Pull Up Enable for RGMII0_TXD2
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for RGMII0_TXD1. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for RGMII0_TXD1. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for RGMII0_TXD1
    5:4     RW          0x0         Pin Mux Selector for RGMII0_TXD1
    3       RW          0x0         Pull Down Enable for RGMII0_TXD1
    2       RW          0x0         Pull Up Enable for RGMII0_TXD1
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG1a: offset 0x0068
""""""""""""""""""""

.. table:: RGMII0_TXD3 and RGMII0_TXCTRL

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for RGMII0_TXCTRL. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for RGMII0_TXCTRL. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for RGMII0_TXCTRL
    21:20   RW          0x0         Pin Mux Selector for RGMII0_TXCTRL
    19      RW          0x0         Pull Down Enable for RGMII0_TXCTRL
    18      RW          0x0         Pull Up Enable for RGMII0_TXCTRL
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for RGMII0_TXD3. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for RGMII0_TXD3. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for RGMII0_TXD3
    5:4     RW          0x0         Pin Mux Selector for RGMII0_TXD3
    3       RW          0x0         Pull Down Enable for RGMII0_TXD3
    2       RW          0x0         Pull Up Enable for RGMII0_TXD3
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG1b: offset 0x006c
""""""""""""""""""""

.. table:: RGMII0_RXD0 and RGMII0_RXD1

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for RGMII0_RXD1. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for RGMII0_RXD1. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for RGMII0_RXD1
    21:20   RW          0x0         Pin Mux Selector for RGMII0_RXD1
    19      RW          0x0         Pull Down Enable for RGMII0_RXD1
    18      RW          0x0         Pull Up Enable for RGMII0_RXD1
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for RGMII0_RXD0. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for RGMII0_RXD0. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for RGMII0_RXD0
    5:4     RW          0x0         Pin Mux Selector for RGMII0_RXD0
    3       RW          0x0         Pull Down Enable for RGMII0_RXD0
    2       RW          0x0         Pull Up Enable for RGMII0_RXD0
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG1c: offset 0x0070
""""""""""""""""""""

.. table:: RGMII0_RXD2 and RGMII0_RXD3

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for RGMII0_RXD3. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for RGMII0_RXD3. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for RGMII0_RXD3
    21:20   RW          0x0         Pin Mux Selector for RGMII0_RXD3
    19      RW          0x0         Pull Down Enable for RGMII0_RXD3
    18      RW          0x0         Pull Up Enable for RGMII0_RXD3
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for RGMII0_RXD2. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for RGMII0_RXD2. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for RGMII0_RXD2
    5:4     RW          0x0         Pin Mux Selector for RGMII0_RXD2
    3       RW          0x0         Pull Down Enable for RGMII0_RXD2
    2       RW          0x0         Pull Up Enable for RGMII0_RXD2
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG1d: offset 0x0074
""""""""""""""""""""

.. table:: RGMII0_RXCTRL and RGMII0_TXC

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for RGMII0_TXC. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for RGMII0_TXC. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for RGMII0_TXC
    21:20   RW          0x0         Pin Mux Selector for RGMII0_TXC
    19      RW          0x0         Pull Down Enable for RGMII0_TXC
    18      RW          0x0         Pull Up Enable for RGMII0_TXC
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for RGMII0_RXCTRL. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for RGMII0_RXCTRL. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for RGMII0_RXCTRL
    5:4     RW          0x0         Pin Mux Selector for RGMII0_RXCTRL
    3       RW          0x0         Pull Down Enable for RGMII0_RXCTRL
    2       RW          0x0         Pull Up Enable for RGMII0_RXCTRL
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG1e: offset 0x0078
""""""""""""""""""""

.. table:: RGMII0_RXC and RGMII0_REFCLKO

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for RGMII0_REFCLKO. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for RGMII0_REFCLKO. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for RGMII0_REFCLKO
    21:20   RW          0x0         Pin Mux Selector for RGMII0_REFCLKO
    19      RW          0x0         Pull Down Enable for RGMII0_REFCLKO
    18      RW          0x0         Pull Up Enable for RGMII0_REFCLKO
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for RGMII0_RXC. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for RGMII0_RXC. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for RGMII0_RXC
    5:4     RW          0x0         Pin Mux Selector for RGMII0_RXC
    3       RW          0x0         Pull Down Enable for RGMII0_RXC
    2       RW          0x0         Pull Up Enable for RGMII0_RXC
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG1f: offset 0x007c
""""""""""""""""""""

.. table:: RGMII0_IRQ and RGMII0_MDC

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for RGMII0_MDC. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for RGMII0_MDC. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for RGMII0_MDC
    21:20   RW          0x0         Pin Mux Selector for RGMII0_MDC
    19      RW          0x0         Pull Down Enable for RGMII0_MDC
    18      RW          0x0         Pull Up Enable for RGMII0_MDC
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for RGMII0_IRQ. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for RGMII0_IRQ. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for RGMII0_IRQ
    5:4     RW          0x0         Pin Mux Selector for RGMII0_IRQ
    3       RW          0x0         Pull Down Enable for RGMII0_IRQ
    2       RW          0x0         Pull Up Enable for RGMII0_IRQ
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG20: offset 0x0080
""""""""""""""""""""

.. table:: RGMII0_MDIO and PWM0

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for PWM0. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for PWM0. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for PWM0
    21:20   RW          0x0         Pin Mux Selector for PWM0
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for PWM0. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for PWM0.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for RGMII0_MDIO. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for RGMII0_MDIO. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for RGMII0_MDIO
    5:4     RW          0x0         Pin Mux Selector for RGMII0_MDIO
    3       RW          0x0         Pull Down Enable for RGMII0_MDIO
    2       RW          0x0         Pull Up Enable for RGMII0_MDIO
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG21: offset 0x0084
""""""""""""""""""""

.. table:: PWM1 and PWM2

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for PWM2. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for PWM2. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for PWM2
    21:20   RW          0x0         Pin Mux Selector for PWM2
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for PWM2. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for PWM2.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for PWM1. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for PWM1. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for PWM1
    5:4     RW          0x0         Pin Mux Selector for PWM1
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for PWM1. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for PWM1.
    ======  ====        =======     ========


REG22: offset 0x0088
""""""""""""""""""""

.. table:: PWM3 and FAN0

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for FAN0. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for FAN0. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for FAN0
    21:20   RW          0x0         Pin Mux Selector for FAN0
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for FAN0. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for FAN0.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for PWM3. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for PWM3. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for PWM3
    5:4     RW          0x0         Pin Mux Selector for PWM3
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for PWM3. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for PWM3.
    ======  ====        =======     ========


REG23: offset 0x008c
""""""""""""""""""""

.. table:: FAN1 and FAN2

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for FAN2. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for FAN2. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for FAN2
    21:20   RW          0x0         Pin Mux Selector for FAN2
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for FAN2. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for FAN2.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for FAN1. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for FAN1. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for FAN1
    5:4     RW          0x0         Pin Mux Selector for FAN1
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for FAN1. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for FAN1.
    ======  ====        =======     ========


REG24: offset 0x0090
""""""""""""""""""""

.. table:: FAN3 and IIC0_SDA

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for IIC0_SDA. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for IIC0_SDA. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for IIC0_SDA
    21:20   RW          0x0         Pin Mux Selector for IIC0_SDA
    19      RW          0x0         Pull Down Enable for IIC0_SDA
    18      RW          0x0         Pull Up Enable for IIC0_SDA
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for FAN3. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for FAN3. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for FAN3
    5:4     RW          0x0         Pin Mux Selector for FAN3
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for FAN3. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for FAN3.
    ======  ====        =======     ========


REG25: offset 0x0094
""""""""""""""""""""

.. table:: IIC0_SCL and IIC1_SDA

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for IIC1_SDA. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for IIC1_SDA. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for IIC1_SDA
    21:20   RW          0x0         Pin Mux Selector for IIC1_SDA
    19      RW          0x0         Pull Down Enable for IIC1_SDA
    18      RW          0x0         Pull Up Enable for IIC1_SDA
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for IIC0_SCL. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for IIC0_SCL. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for IIC0_SCL
    5:4     RW          0x0         Pin Mux Selector for IIC0_SCL
    3       RW          0x0         Pull Down Enable for IIC0_SCL
    2       RW          0x0         Pull Up Enable for IIC0_SCL
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG26: offset 0x0098
""""""""""""""""""""

.. table:: IIC1_SCL and IIC2_SDA

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for IIC2_SDA. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for IIC2_SDA. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for IIC2_SDA
    21:20   RW          0x0         Pin Mux Selector for IIC2_SDA
    19      RW          0x0         Pull Down Enable for IIC2_SDA
    18      RW          0x0         Pull Up Enable for IIC2_SDA
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for IIC1_SCL. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for IIC1_SCL. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for IIC1_SCL
    5:4     RW          0x0         Pin Mux Selector for IIC1_SCL
    3       RW          0x0         Pull Down Enable for IIC1_SCL
    2       RW          0x0         Pull Up Enable for IIC1_SCL
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG27: offset 0x009c
""""""""""""""""""""

.. table:: IIC2_SCL and IIC3_SDA

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for IIC3_SDA. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for IIC3_SDA. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for IIC3_SDA
    21:20   RW          0x0         Pin Mux Selector for IIC3_SDA
    19      RW          0x0         Pull Down Enable for IIC3_SDA
    18      RW          0x0         Pull Up Enable for IIC3_SDA
    17:16   RW          NA          Reserved
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for IIC2_SCL. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for IIC2_SCL. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for IIC2_SCL
    5:4     RW          0x0         Pin Mux Selector for IIC2_SCL
    3       RW          0x0         Pull Down Enable for IIC2_SCL
    2       RW          0x0         Pull Up Enable for IIC2_SCL
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG28: offset 0x00a0
""""""""""""""""""""

.. table:: IIC3_SCL and UART0_TX

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for UART0_TX. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for UART0_TX. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for UART0_TX
    21:20   RW          0x0         Pin Mux Selector for UART0_TX
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for UART0_TX. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for UART0_TX.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for IIC3_SCL. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for IIC3_SCL. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for IIC3_SCL
    5:4     RW          0x0         Pin Mux Selector for IIC3_SCL
    3       RW          0x0         Pull Down Enable for IIC3_SCL
    2       RW          0x0         Pull Up Enable for IIC3_SCL
    1:0     RW          NA          Reserved
    ======  ====        =======     ========


REG29: offset 0x00a4
""""""""""""""""""""

.. table:: UART0_RX and UART0_RTS

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for UART0_RTS. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for UART0_RTS. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for UART0_RTS
    21:20   RW          0x0         Pin Mux Selector for UART0_RTS
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for UART0_RTS. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for UART0_RTS.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for UART0_RX. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for UART0_RX. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for UART0_RX
    5:4     RW          0x0         Pin Mux Selector for UART0_RX
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for UART0_RX. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for UART0_RX.
    ======  ====        =======     ========


REG2a: offset 0x00a8
""""""""""""""""""""

.. table:: UART0_CTS and UART1_TX

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for UART1_TX. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for UART1_TX. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for UART1_TX
    21:20   RW          0x0         Pin Mux Selector for UART1_TX
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for UART1_TX. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for UART1_TX.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for UART0_CTS. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for UART0_CTS. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for UART0_CTS
    5:4     RW          0x0         Pin Mux Selector for UART0_CTS
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for UART0_CTS. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for UART0_CTS.
    ======  ====        =======     ========


REG2b: offset 0x00ac
""""""""""""""""""""

.. table:: UART1_RX and UART1_RTS

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for UART1_RTS. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for UART1_RTS. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for UART1_RTS
    21:20   RW          0x0         Pin Mux Selector for UART1_RTS
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for UART1_RTS. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for UART1_RTS.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for UART1_RX. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for UART1_RX. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for UART1_RX
    5:4     RW          0x0         Pin Mux Selector for UART1_RX
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for UART1_RX. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for UART1_RX.
    ======  ====        =======     ========


REG2c: offset 0x00b0
""""""""""""""""""""

.. table:: UART1_CTS and UART2_TX

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for UART2_TX. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for UART2_TX. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for UART2_TX
    21:20   RW          0x0         Pin Mux Selector for UART2_TX
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for UART2_TX. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for UART2_TX.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for UART1_CTS. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for UART1_CTS. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for UART1_CTS
    5:4     RW          0x0         Pin Mux Selector for UART1_CTS
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for UART1_CTS. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for UART1_CTS.
    ======  ====        =======     ========


REG2d: offset 0x00b4
""""""""""""""""""""

.. table:: UART2_RX and UART2_RTS

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for UART2_RTS. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for UART2_RTS. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for UART2_RTS
    21:20   RW          0x0         Pin Mux Selector for UART2_RTS
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for UART2_RTS. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for UART2_RTS.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for UART2_RX. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for UART2_RX. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for UART2_RX
    5:4     RW          0x0         Pin Mux Selector for UART2_RX
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for UART2_RX. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for UART2_RX.
    ======  ====        =======     ========


REG2e: offset 0x00b8
""""""""""""""""""""

.. table:: UART2_CTS and UART3_TX

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for UART3_TX. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for UART3_TX. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for UART3_TX
    21:20   RW          0x0         Pin Mux Selector for UART3_TX
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for UART3_TX. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for UART3_TX.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for UART2_CTS. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for UART2_CTS. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for UART2_CTS
    5:4     RW          0x0         Pin Mux Selector for UART2_CTS
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for UART2_CTS. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for UART2_CTS.
    ======  ====        =======     ========


REG2f: offset 0x00bc
""""""""""""""""""""

.. table:: UART3_RX and UART3_RTS

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for UART3_RTS. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for UART3_RTS. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for UART3_RTS
    21:20   RW          0x0         Pin Mux Selector for UART3_RTS
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for UART3_RTS. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for UART3_RTS.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for UART3_RX. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for UART3_RX. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for UART3_RX
    5:4     RW          0x0         Pin Mux Selector for UART3_RX
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for UART3_RX. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for UART3_RX.
    ======  ====        =======     ========


REG30: offset 0x00c0
""""""""""""""""""""

.. table:: UART3_CTS and SPI0_CS0_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPI0_CS0_X. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPI0_CS0_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPI0_CS0_X
    21:20   RW          0x0         Pin Mux Selector for SPI0_CS0_X
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPI0_CS0_X. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPI0_CS0_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for UART3_CTS. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for UART3_CTS. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for UART3_CTS
    5:4     RW          0x0         Pin Mux Selector for UART3_CTS
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for UART3_CTS. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for UART3_CTS.
    ======  ====        =======     ========


REG31: offset 0x00c4
""""""""""""""""""""

.. table:: SPI0_CS1_X and SPI0_SDI

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPI0_SDI. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPI0_SDI. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPI0_SDI
    21:20   RW          0x0         Pin Mux Selector for SPI0_SDI
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPI0_SDI. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPI0_SDI.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPI0_CS1_X. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPI0_CS1_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPI0_CS1_X
    5:4     RW          0x0         Pin Mux Selector for SPI0_CS1_X
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPI0_CS1_X. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPI0_CS1_X.
    ======  ====        =======     ========


REG32: offset 0x00c8
""""""""""""""""""""

.. table:: SPI0_SDO and SPI0_SCK

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPI0_SCK. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPI0_SCK. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPI0_SCK
    21:20   RW          0x0         Pin Mux Selector for SPI0_SCK
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPI0_SCK. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPI0_SCK.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPI0_SDO. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPI0_SDO. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPI0_SDO
    5:4     RW          0x0         Pin Mux Selector for SPI0_SDO
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPI0_SDO. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPI0_SDO.
    ======  ====        =======     ========


REG33: offset 0x00cc
""""""""""""""""""""

.. table:: SPI1_CS0_X and SPI1_CS1_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPI1_CS1_X. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPI1_CS1_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPI1_CS1_X
    21:20   RW          0x0         Pin Mux Selector for SPI1_CS1_X
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPI1_CS1_X. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPI1_CS1_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPI1_CS0_X. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPI1_CS0_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPI1_CS0_X
    5:4     RW          0x0         Pin Mux Selector for SPI1_CS0_X
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPI1_CS0_X. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPI1_CS0_X.
    ======  ====        =======     ========


REG34: offset 0x00d0
""""""""""""""""""""

.. table:: SPI1_SDI and SPI1_SDO

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for SPI1_SDO. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for SPI1_SDO. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for SPI1_SDO
    21:20   RW          0x0         Pin Mux Selector for SPI1_SDO
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SPI1_SDO. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for SPI1_SDO.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPI1_SDI. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPI1_SDI. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPI1_SDI
    5:4     RW          0x0         Pin Mux Selector for SPI1_SDI
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPI1_SDI. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPI1_SDI.
    ======  ====        =======     ========


REG35: offset 0x00d4
""""""""""""""""""""

.. table:: SPI1_SCK and JTAG0_TDO

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for JTAG0_TDO. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for JTAG0_TDO. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for JTAG0_TDO
    21:20   RW          0x0         Pin Mux Selector for JTAG0_TDO
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for JTAG0_TDO. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for JTAG0_TDO.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for SPI1_SCK. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for SPI1_SCK. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for SPI1_SCK
    5:4     RW          0x0         Pin Mux Selector for SPI1_SCK
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SPI1_SCK. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for SPI1_SCK.
    ======  ====        =======     ========


REG36: offset 0x00d8
""""""""""""""""""""

.. table:: JTAG0_TCK and JTAG0_TDI

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for JTAG0_TDI. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for JTAG0_TDI. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for JTAG0_TDI
    21:20   RW          0x0         Pin Mux Selector for JTAG0_TDI
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for JTAG0_TDI. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for JTAG0_TDI.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for JTAG0_TCK. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for JTAG0_TCK. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for JTAG0_TCK
    5:4     RW          0x0         Pin Mux Selector for JTAG0_TCK
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for JTAG0_TCK. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for JTAG0_TCK.
    ======  ====        =======     ========


REG37: offset 0x00dc
""""""""""""""""""""

.. table:: JTAG0_TMS and JTAG0_TRST_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for JTAG0_TRST_X. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for JTAG0_TRST_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for JTAG0_TRST_X
    21:20   RW          0x0         Pin Mux Selector for JTAG0_TRST_X
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for JTAG0_TRST_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for JTAG0_TRST_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for JTAG0_TMS. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for JTAG0_TMS. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for JTAG0_TMS
    5:4     RW          0x0         Pin Mux Selector for JTAG0_TMS
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for JTAG0_TMS. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for JTAG0_TMS.
    ======  ====        =======     ========


REG38: offset 0x00e0
""""""""""""""""""""

.. table:: JTAG0_SRST_X and JTAG1_TDO

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for JTAG1_TDO. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for JTAG1_TDO. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for JTAG1_TDO
    21:20   RW          0x0         Pin Mux Selector for JTAG1_TDO
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for JTAG1_TDO. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for JTAG1_TDO.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for JTAG0_SRST_X. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for JTAG0_SRST_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for JTAG0_SRST_X
    5:4     RW          0x0         Pin Mux Selector for JTAG0_SRST_X
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for JTAG0_SRST_X. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for JTAG0_SRST_X.
    ======  ====        =======     ========


REG39: offset 0x00e4
""""""""""""""""""""

.. table:: JTAG1_TCK and JTAG1_TDI

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for JTAG1_TDI. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for JTAG1_TDI. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for JTAG1_TDI
    21:20   RW          0x0         Pin Mux Selector for JTAG1_TDI
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for JTAG1_TDI. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for JTAG1_TDI.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for JTAG1_TCK. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for JTAG1_TCK. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for JTAG1_TCK
    5:4     RW          0x0         Pin Mux Selector for JTAG1_TCK
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for JTAG1_TCK. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for JTAG1_TCK.
    ======  ====        =======     ========


REG3a: offset 0x00e8
""""""""""""""""""""

.. table:: JTAG1_TMS and JTAG1_TRST_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for JTAG1_TRST_X. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for JTAG1_TRST_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for JTAG1_TRST_X
    21:20   RW          0x0         Pin Mux Selector for JTAG1_TRST_X
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for JTAG1_TRST_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for JTAG1_TRST_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for JTAG1_TMS. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for JTAG1_TMS. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for JTAG1_TMS
    5:4     RW          0x0         Pin Mux Selector for JTAG1_TMS
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for JTAG1_TMS. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for JTAG1_TMS.
    ======  ====        =======     ========


REG3b: offset 0x00ec
""""""""""""""""""""

.. table:: JTAG1_SRST_X and JTAG2_TDO

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for JTAG2_TDO. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for JTAG2_TDO. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for JTAG2_TDO
    21:20   RW          0x0         Pin Mux Selector for JTAG2_TDO
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for JTAG2_TDO. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for JTAG2_TDO.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for JTAG1_SRST_X. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for JTAG1_SRST_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for JTAG1_SRST_X
    5:4     RW          0x0         Pin Mux Selector for JTAG1_SRST_X
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for JTAG1_SRST_X. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for JTAG1_SRST_X.
    ======  ====        =======     ========


REG3c: offset 0x00f0
""""""""""""""""""""

.. table:: JTAG2_TCK and JTAG2_TDI

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for JTAG2_TDI. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for JTAG2_TDI. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for JTAG2_TDI
    21:20   RW          0x0         Pin Mux Selector for JTAG2_TDI
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for JTAG2_TDI. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for JTAG2_TDI.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for JTAG2_TCK. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for JTAG2_TCK. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for JTAG2_TCK
    5:4     RW          0x0         Pin Mux Selector for JTAG2_TCK
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for JTAG2_TCK. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for JTAG2_TCK.
    ======  ====        =======     ========


REG3d: offset 0x00f4
""""""""""""""""""""

.. table:: JTAG2_TMS and JTAG2_TRST_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for JTAG2_TRST_X. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for JTAG2_TRST_X. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for JTAG2_TRST_X
    21:20   RW          0x0         Pin Mux Selector for JTAG2_TRST_X
    19:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for JTAG2_TRST_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for JTAG2_TRST_X.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for JTAG2_TMS. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for JTAG2_TMS. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for JTAG2_TMS
    5:4     RW          0x0         Pin Mux Selector for JTAG2_TMS
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for JTAG2_TMS. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for JTAG2_TMS.
    ======  ====        =======     ========


REG3e: offset 0x00f8
""""""""""""""""""""

.. table:: JTAG2_SRST_X and GPIO0

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO0. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO0. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO0
    21:20   RW          0x0         Pin Mux Selector for GPIO0
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO0. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO0.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for JTAG2_SRST_X. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for JTAG2_SRST_X. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for JTAG2_SRST_X
    5:4     RW          0x0         Pin Mux Selector for JTAG2_SRST_X
    3:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for JTAG2_SRST_X. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for JTAG2_SRST_X.
    ======  ====        =======     ========


REG3f: offset 0x00fc
""""""""""""""""""""

.. table:: GPIO1 and GPIO2

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO2. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO2. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO2
    21:20   RW          0x0         Pin Mux Selector for GPIO2
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO2. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO2.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO1. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO1. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO1
    5:4     RW          0x0         Pin Mux Selector for GPIO1
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO1. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO1.
    ======  ====        =======     ========


REG40: offset 0x0100
""""""""""""""""""""

.. table:: GPIO3 and GPIO4

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO4. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO4. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO4
    21:20   RW          0x0         Pin Mux Selector for GPIO4
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO4. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO4.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO3. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO3. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO3
    5:4     RW          0x0         Pin Mux Selector for GPIO3
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO3. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO3.
    ======  ====        =======     ========


REG41: offset 0x0104
""""""""""""""""""""

.. table:: GPIO5 and GPIO6

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO6. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO6. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO6
    21:20   RW          0x0         Pin Mux Selector for GPIO6
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO6. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO6.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO5. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO5. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO5
    5:4     RW          0x0         Pin Mux Selector for GPIO5
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO5. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO5.
    ======  ====        =======     ========


REG42: offset 0x0108
""""""""""""""""""""

.. table:: GPIO7 and GPIO8

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO8. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO8. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO8
    21:20   RW          0x0         Pin Mux Selector for GPIO8
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO8. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO8.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO7. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO7. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO7
    5:4     RW          0x0         Pin Mux Selector for GPIO7
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO7. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO7.
    ======  ====        =======     ========


REG43: offset 0x010c
""""""""""""""""""""

.. table:: GPIO9 and GPIO10

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO10. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO10. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO10
    21:20   RW          0x0         Pin Mux Selector for GPIO10
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO10. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO10.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO9. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO9. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO9
    5:4     RW          0x0         Pin Mux Selector for GPIO9
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO9. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO9.
    ======  ====        =======     ========


REG44: offset 0x0110
""""""""""""""""""""

.. table:: GPIO11 and GPIO12

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO12. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO12. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO12
    21:20   RW          0x0         Pin Mux Selector for GPIO12
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO12. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO12.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO11. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO11. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO11
    5:4     RW          0x0         Pin Mux Selector for GPIO11
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO11. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO11.
    ======  ====        =======     ========


REG45: offset 0x0114
""""""""""""""""""""

.. table:: GPIO13 and GPIO14

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO14. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO14. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO14
    21:20   RW          0x0         Pin Mux Selector for GPIO14
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO14. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO14.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO13. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO13. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO13
    5:4     RW          0x0         Pin Mux Selector for GPIO13
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO13. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO13.
    ======  ====        =======     ========


REG46: offset 0x0118
""""""""""""""""""""

.. table:: GPIO15 and GPIO16

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO16. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO16. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO16
    21:20   RW          0x0         Pin Mux Selector for GPIO16
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO16. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO16.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO15. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO15. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO15
    5:4     RW          0x0         Pin Mux Selector for GPIO15
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO15. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO15.
    ======  ====        =======     ========


REG47: offset 0x011c
""""""""""""""""""""

.. table:: GPIO17 and GPIO18

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO18. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for GPIO18. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO18
    21:20   RW          0x0         Pin Mux Selector for GPIO18
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO18. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO18.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO17. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for GPIO17. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO17
    5:4     RW          0x0         Pin Mux Selector for GPIO17
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO17. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO17.
    ======  ====        =======     ========


REG48: offset 0x0120
""""""""""""""""""""

.. table:: GPIO19 and GPIO20

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO20. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for GPIO20. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO20
    21:20   RW          0x0         Pin Mux Selector for GPIO20
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO20. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO20.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO19. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for GPIO19. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO19
    5:4     RW          0x0         Pin Mux Selector for GPIO19
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO19. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO19.
    ======  ====        =======     ========


REG49: offset 0x0124
""""""""""""""""""""

.. table:: GPIO21 and GPIO22

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO22. '1' enables PAD output mode under IP's drive
    26      RW          0x0         Schmitt trigger enable for GPIO22. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO22
    21:20   RW          0x0         Pin Mux Selector for GPIO22
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO22. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO22.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO21. '1' enables PAD output mode under IP's drive
    10      RW          0x0         Schmitt trigger enable for GPIO21. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO21
    5:4     RW          0x0         Pin Mux Selector for GPIO21
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO21. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO21.
    ======  ====        =======     ========


REG4a: offset 0x0128
""""""""""""""""""""

.. table:: GPIO23 and GPIO24

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO24. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO24. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO24
    21:20   RW          0x0         Pin Mux Selector for GPIO24
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO24. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO24.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO23. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO23. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO23
    5:4     RW          0x0         Pin Mux Selector for GPIO23
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO23. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO23.
    ======  ====        =======     ========


REG4b: offset 0x012c
""""""""""""""""""""

.. table:: GPIO25 and GPIO26

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO26. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO26. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO26
    21:20   RW          0x0         Pin Mux Selector for GPIO26
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO26. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO26.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO25. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO25. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO25
    5:4     RW          0x0         Pin Mux Selector for GPIO25
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO25. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO25.
    ======  ====        =======     ========


REG4c: offset 0x0130
""""""""""""""""""""

.. table:: GPIO27 and GPIO28

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO28. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO28. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO28
    21:20   RW          0x0         Pin Mux Selector for GPIO28
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO28. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for GPIO28.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO27. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO27. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO27
    5:4     RW          0x0         Pin Mux Selector for GPIO27
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO27. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for GPIO27.
    ======  ====        =======     ========


REG4d: offset 0x0134
""""""""""""""""""""

.. table:: GPIO29 and GPIO30

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:28   RO          NA          Reserved
    27      RW          0x1         PAD OEX enable for GPIO30. '1' enables PAD output mode under IP's drive
    26      RW          0x1         Schmitt trigger enable for GPIO30. '1' enables Schmitt trigger input function
    25:22   RW          0x8         Driving Selector for GPIO30
    21:20   RW          0x0         Pin Mux Selector for GPIO30
    19:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for GPIO30. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for GPIO30.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO29. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO29. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO29
    5:4     RW          0x0         Pin Mux Selector for GPIO29
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO29. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for GPIO29.
    ======  ====        =======     ========


REG4e: offset 0x0138
""""""""""""""""""""

.. table:: GPIO31 and MODE_SEL0

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x1         Schmitt trigger enable for MODE_SEL0. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for MODE_SEL0. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for MODE_SEL0.
    15:12   RO          NA          Reserved
    11      RW          0x1         PAD OEX enable for GPIO31. '1' enables PAD output mode under IP's drive
    10      RW          0x1         Schmitt trigger enable for GPIO31. '1' enables Schmitt trigger input function
    9:6     RW          0x8         Driving Selector for GPIO31
    5:4     RW          0x0         Pin Mux Selector for GPIO31
    3:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for GPIO31. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for GPIO31.
    ======  ====        =======     ========


REG4f: offset 0x013c
""""""""""""""""""""

.. table:: MODE_SEL1 and MODE_SEL2

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x1         Schmitt trigger enable for MODE_SEL2. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for MODE_SEL2. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for MODE_SEL2.
    15:11   RO          NA          Reserved
    10      RW          0x1         Schmitt trigger enable for MODE_SEL1. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for MODE_SEL1. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for MODE_SEL1.
    ======  ====        =======     ========


REG50: offset 0x0140
""""""""""""""""""""

.. table:: BOOT_SEL0 and BOOT_SEL1

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x1         Schmitt trigger enable for BOOT_SEL1. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for BOOT_SEL1. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for BOOT_SEL1.
    15:11   RO          NA          Reserved
    10      RW          0x1         Schmitt trigger enable for BOOT_SEL0. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for BOOT_SEL0. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for BOOT_SEL0.
    ======  ====        =======     ========


REG51: offset 0x0144
""""""""""""""""""""

.. table:: BOOT_SEL2 and BOOT_SEL3

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x1         Schmitt trigger enable for BOOT_SEL3. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for BOOT_SEL3. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for BOOT_SEL3.
    15:11   RO          NA          Reserved
    10      RW          0x1         Schmitt trigger enable for BOOT_SEL2. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for BOOT_SEL2. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for BOOT_SEL2.
    ======  ====        =======     ========


REG52: offset 0x0148
""""""""""""""""""""

.. table:: BOOT_SEL4 and BOOT_SEL5

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x1         Schmitt trigger enable for BOOT_SEL5. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for BOOT_SEL5. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for BOOT_SEL5.
    15:11   RO          NA          Reserved
    10      RW          0x1         Schmitt trigger enable for BOOT_SEL4. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for BOOT_SEL4. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for BOOT_SEL4.
    ======  ====        =======     ========


REG53: offset 0x014c
""""""""""""""""""""

.. table:: BOOT_SEL6 and BOOT_SEL7

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x1         Schmitt trigger enable for BOOT_SEL7. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for BOOT_SEL7. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for BOOT_SEL7.
    15:11   RO          NA          Reserved
    10      RW          0x1         Schmitt trigger enable for BOOT_SEL6. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for BOOT_SEL6. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for BOOT_SEL6.
    ======  ====        =======     ========


REG54: offset 0x0150
""""""""""""""""""""

.. table:: MULTI_SCKT and SCKT_ID0

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x1         Schmitt trigger enable for SCKT_ID0. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for SCKT_ID0. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for SCKT_ID0.
    15:11   RO          NA          Reserved
    10      RW          0x1         Schmitt trigger enable for MULTI_SCKT. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for MULTI_SCKT. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for MULTI_SCKT.
    ======  ====        =======     ========


REG55: offset 0x0154
""""""""""""""""""""

.. table:: SCKT_ID1 and PLL_CLK_IN_MAIN

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x0         Schmitt trigger enable for PLL_CLK_IN_MAIN. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for PLL_CLK_IN_MAIN. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for PLL_CLK_IN_MAIN.
    15:11   RO          NA          Reserved
    10      RW          0x1         Schmitt trigger enable for SCKT_ID1. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for SCKT_ID1. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for SCKT_ID1.
    ======  ====        =======     ========


REG56: offset 0x0158
""""""""""""""""""""

.. table:: PLL_CLK_IN_DDR_L and PLL_CLK_IN_DDR_R

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x0         Schmitt trigger enable for PLL_CLK_IN_DDR_R. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for PLL_CLK_IN_DDR_R. (0:pull down; 1:pull up)
    16      RW          0x0         Pull Enable for PLL_CLK_IN_DDR_R.
    15:11   RO          NA          Reserved
    10      RW          0x0         Schmitt trigger enable for PLL_CLK_IN_DDR_L. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for PLL_CLK_IN_DDR_L. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for PLL_CLK_IN_DDR_L.
    ======  ====        =======     ========


REG57: offset 0x015c
""""""""""""""""""""

.. table:: XTAL_32K and SYS_RST_X

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x1         Schmitt trigger enable for SYS_RST_X. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x1         Pull Selector for SYS_RST_X. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for SYS_RST_X.
    15:11   RO          NA          Reserved
    10      RW          0x0         Schmitt trigger enable for XTAL_32K. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for XTAL_32K. (0:pull down; 1:pull up)
    0       RW          0x0         Pull Enable for XTAL_32K.
    ======  ====        =======     ========


REG58: offset 0x0160
""""""""""""""""""""

.. table:: PWR_BUTTON and TEST_EN

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RO          0x1         Schmitt trigger enable for TEST_EN. '1' enables Schmitt trigger input function
    25:18   RO          NA          Reserved
    17      RO          0x0         Pull Selector for TEST_EN. (0:pull down; 1:pull up)
    16      RO          0x1         Pull Enable for TEST_EN.
    15:11   RO          NA          Reserved
    10      RW          0x1         Schmitt trigger enable for PWR_BUTTON. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x1         Pull Selector for PWR_BUTTON. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for PWR_BUTTON.
    ======  ====        =======     ========


REG59: offset 0x0164
""""""""""""""""""""

.. table:: TEST_MODE_MBIST and TEST_MODE_SCAN

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x1         Schmitt trigger enable for TEST_MODE_SCAN. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for TEST_MODE_SCAN. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for TEST_MODE_SCAN.
    15:11   RO          NA          Reserved
    10      RW          0x1         Schmitt trigger enable for TEST_MODE_MBIST. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for TEST_MODE_MBIST. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for TEST_MODE_MBIST.
    ======  ====        =======     ========


REG5a: offset 0x0168
""""""""""""""""""""

.. table:: TEST_MODE_BSD and BISR_BYP

    ======  ====        =======     ========
    Fields  Type        Default     Function
    ======  ====        =======     ========
    31:27   RO          NA          Reserved
    26      RW          0x1         Schmitt trigger enable for BISR_BYP. '1' enables Schmitt trigger input function
    25:18   RW          NA          Reserved
    17      RW          0x0         Pull Selector for BISR_BYP. (0:pull down; 1:pull up)
    16      RW          0x1         Pull Enable for BISR_BYP.
    15:11   RO          NA          Reserved
    10      RW          0x1         Schmitt trigger enable for TEST_MODE_BSD. '1' enables Schmitt trigger input function
    9:2     RW          NA          Reserved
    1       RW          0x0         Pull Selector for TEST_MODE_BSD. (0:pull down; 1:pull up)
    0       RW          0x1         Pull Enable for TEST_MODE_BSD.
    ======  ====        =======     ========


