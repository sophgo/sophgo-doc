Power Domain and Power Sequence 
================================
SG2042 implements single-voltage design to minimize the design effort. Different blocks will work at identical voltage (core: 0.8v) to alleviate further implementation.

So there will be no content on power domain partition, power good indication, isolation and level shifter insertion, etc. The following sections focus on power-up sequence.


.. table:: power bump  

    +-------+--------------------+----------+--------------+-------------------------------+
    |       | Power Bump         | Voltage  | Variation    | Comment                       |
    +=======+====================+==========+==============+===============================+
    | Top   | VDDC               | 0.8      | 10%          | Core Power                    |
    +-------+--------------------+----------+--------------+-------------------------------+
    | PLL   | VDDIO_FPLL         | 0.8      | 10%          | PLL Power                     |
    +       +--------------------+          |              |                               |
    |       | VDDIO_MPLL         |          |              |                               |
    +       +--------------------+          |              |                               |
    |       | VDDIO_DPLL0        |          |              |                               |
    +       +--------------------+          |              |                               |
    |       | VDDIO_DPLL1        |          |              |                               |
    +-------+--------------------+----------+--------------+-------------------------------+
    | eFUSE | VDD_EFUSE          | 0.8      | 10%          |                               |
    +-------+--------------------+----------+--------------+-------------------------------+
    | PCIe  | cmn_avdd_clk       | 0.8      | 0.76v~0.88v  | pma power                     |
    |       +--------------------+          |              |                               |
    |       | rx_avdd_clk_ln_0~15|          |              |                               |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | tx_avdd_ln_0~15    | 0.8      | 0.76v~0.88v  | pma power                     |
    |       +--------------------+          |              |                               |
    |       | rx_avdd_ln_0~15    |          |              |                               |
    |       +--------------------+          |              |                               |
    |       | cmn_avdd           |          |              |                               |
    +-------+--------------------+----------+--------------+-------------------------------+
    | DDR   | VDD                | 0.8      | 0.72v~0.88v  | core supply                   |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | VDDPLL             | 0.8      | 0.72v~0.88v  | PLL control supply            |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | VDDQ               | 1.2      | 1.14v~1.26v  | I/O drive supply              |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | VDDQCK             | 1.2      | 1.14v~1.26v  | I/O drive supply              |
    +-------+--------------------+----------+--------------+-------------------------------+
    | DDR4  | VDDQ               | 1.2      | 1.14v~1.26v  | DQ Power supply               |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | VDD                | 1.2      | 1.14v~1.26v  | Power supply                  |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | cmn_avdd_h         | 1.5/1.8  | 1.425v~1.98v | pma power                     |
    |       +--------------------+          |              |                               |
    |       | xcvr_avdd_h_ln_0~15|          |              |                               |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | VQPS               | 1.8      | 5%           | efuse 1.8v for programming    |
    +-------+--------------------+----------+--------------+-------------------------------+
    | IO    | VDDIO_EMMC_18      | 1.8      | 10%          | PHY power for EMMC and SD     |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | VDDIO_SENSOR       | 1.8      | 10%          |                               |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | VPP                | 2.5      | 2.375v~2.75v | DRAM Activating Power supply  |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | VDDIO_EMMC_33      | 3.3      | 10%          | PHY power for EMMC and SD     |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | VDDIO_RGM_33       | 1.8      | 10%          | 1*RGMII 1682 Test data 11mA   |
    +-------+--------------------+----------+--------------+-------------------------------+
    |       | VDDIO_RGM_18       | 1.8      | 10%          | 1*RGMII 1682 Test data 11mA   |
    +-------+--------------------+----------+--------------+-------------------------------+

Power Up Sequence
-----------------

DDR Power-Up Sequence
^^^^^^^^^^^^^^^^^^^^^

The DDR spec requires the core supply should be sequenced on before, or concurrently with the IO supply.

The recommended power up sequence is:

1. Turn on core supply (VDD) and PLL supply (VDDPLL)

2. Assert rst_n and dll_rst_n ports on the PHY

3. Turn on IO supply (VDDQ, VDDQCK, VDDQX) 

The Power Up requirement of particles

1. The power voltage ramp time between 300mV to VDD min must be no greater than  200ms

2. Power on sequence is  VPP → VDD → VDDQ

PCIe Power-Up Sequence
^^^^^^^^^^^^^^^^^^^^^^

PMA power supply has no sequence requirements.(see integration guide 4.3.4.3) 

Based on Vendor's reply: There are no power supply sequence requirements for PHY/Controller, power supplies can be enabled in any order.

eFUSE Power-Up Sequence
^^^^^^^^^^^^^^^^^^^^^^^

The recommended power up sequence of eFUSE is

1. Turn on 0.8v VDD core

2. Turn on 1.8v VQPS

IO Power-Up Sequence
^^^^^^^^^^^^^^^^^^^^

**1.8V tphn12ffcllgv18e**

1. Turn on 1.8v VDDPST I/O power

2. Turn on 0.8v vdd core power

 (Based on app note: power up I/O power and core power simultaneously is also acceptable)

**3.3/1.8 tphn12ffcll_18od33rgmii**

- In 3.3V mode, First power up VDDPST18 through PVDD18RGM; after at least 20us, power up VDDPST33 through PVDD3CDGRGM
- In 1.8V mode, VDDPST33 is 1.8V
- In our chip, only 1.8V mode is used.
- based on zhuoming's feedback: VDDPST18 and VDDPST33 can be power on simultaneous or can connect together in PCB if only used at 1.8V mode.  
- MS1/MS2 should come form always-on core main.But as there are POC control in IO,when VDD not power on, MS1/MS2 will be set to a 1.8V mode. So these is no problem at the case.

**3.3/1.8V tphn12ffcll_18od33sdio**

- 0.8V VDD core -> 3.3/1.8V power up.
- based on zhuoming's feedback: MS signal should come form a always-on core domain. If no such always-on core domain. You can refer to option 3. (which is power up VDD core first)

Whole Chip Power-Up Sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0ms  VDDIO (1.8v VDDPST)  VDDIO_RGM_33, VDDIO_RGM_18 ->

1ms  VDDC (0.8V) →

2ms  VDDIO_EMMC_33 (3.3V) ->

3ms  VDD_PCIE (0.8V PCIe PHY +PCIe Controller), VDD_PMA (1.5v/1.8v); DDR VDD (0.8v), DDR PLL (0.8v VDDPLL) ->

4ms  DDR IO supply (1.2V, VDDQ,VDDQCK, VDDQX) ->

5ms  VQPS (1.8V)->

6ms  Release IO reset signals: SYS_RST_X and PWR_BUTTON

