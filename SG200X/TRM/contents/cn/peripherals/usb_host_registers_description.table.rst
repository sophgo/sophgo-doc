HCFG
````

Host Configuration Register

.. _table_usb_hcfg_contd_0:
.. table:: HCFG, Offset Address: 0x400
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 1:0  | FS\       | R/W | FS/LS PHY Clock Select              | 0x0  |
	|      | LSPclkSel |     | (FSLSPclkSel)                       |      |
	|      |           |     |                                     |      |
	|      |           |     | When the core is in FS Host mode:   |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b00: PHY clock is running at    |      |
	|      |           |     |   30/60 MHz                         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b01: PHY clock is running at 48 |      |
	|      |           |     |   MHz                               |      |
	|      |           |     |                                     |      |
	|      |           |     | - Others: Reserved                  |      |
	|      |           |     |                                     |      |
	|      |           |     | When the core is in LS Host mode:   |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b00: PHY clock is running at    |      |
	|      |           |     |   30/60 MHz. When the UTMI+/ULPI    |      |
	|      |           |     |   PHY Low Power mode is not         |      |
	|      |           |     |   selected, use 30/60 MHz.          |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b01: PHY clock is running at 48 |      |
	|      |           |     |   MHz. When the UTMI+ PHY Low       |      |
	|      |           |     |   Power mode is selected, use 48MHz |      |
	|      |           |     |   If the PHY supplies a 48 MHz      |      |
	|      |           |     |   clock during LS mode.             |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b10: PHY clock is running at 6  |      |
	|      |           |     |   MHz. In USB 1.1 FS mode, use 6    |      |
	|      |           |     |   MHz when the UTMI+ PHY Low Power  |      |
	|      |           |     |   mode is selected and the          |      |
	|      |           |     |   PHY supplies a 6 MHz clock during |      |
	|      |           |     |   LS mode. If you select a 6 MHz    |      |
	|      |           |     |   clock during LS mode, you must do |      |
	|      |           |     |   a soft reset.                     |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b11: Reserved                   |      |
	|      |           |     |                                     |      |
	|      |           |     | Notes:                              |      |
	|      |           |     |                                     |      |
	|      |           |     | - When Core in FS mode, the         |      |
	|      |           |     |   internal and external clocks have |      |
	|      |           |     |   the same frequency.               |      |
	|      |           |     |                                     |      |
	|      |           |     | - When Core in LS mode,             |      |
	|      |           |     |                                     |      |
	|      |           |     |   - If FSLSPclkSel = 2'b00: Internal|      |
	|      |           |     |     and external clocks have the    |      |
	|      |           |     |     same frequency                  |      |
	|      |           |     |                                     |      |
	|      |           |     |   - If FSLSPclkSel = 2'b10: Internal|      |
	|      |           |     |     clock is divided by eight       |      |
	|      |           |     |     version of external 48 MHz clock|      |
	|      |           |     |     (utmifs_clk).                   |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_hcfg_contd_1:
.. table:: HCFG, Offset Address: 0x400 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 2    | FSLSSupp  | R/W | FS- and LS-Only Support (FSLSSupp)  | 0x0  |
	|      |           |     | The application uses this bit to    |      |
	|      |           |     | control the core's enumeration      |      |
	|      |           |     | speed.                              |      |
	|      |           |     |                                     |      |
	|      |           |     | Using this bit, the application can |      |
	|      |           |     | make the core enumerate as a FS     |      |
	|      |           |     | host, even If the connected device  |      |
	|      |           |     | supports HS traffic. Do not make    |      |
	|      |           |     | changes to this field after initial |      |
	|      |           |     | programming.                        |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: HS/FS/LS, based on the      |      |
	|      |           |     |   maximum speed supported by the    |      |
	|      |           |     |   connected device                  |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: FS/LS-only, even If the     |      |
	|      |           |     |   connected device can support HS   |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 6:3  | Reserve\  | RO  | Reserved for future use.            |      |
	|      | d_400_6_3 |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 7    | Ena32KHzS | R/W | Enable 32 KHz Suspend mode          | 0x0  |
	|      |           |     | (Ena32KHzS)                         |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit can be set only if FS PHY  |      |
	|      |           |     | interface is selected. Otherwise,   |      |
	|      |           |     | this                                |      |
	|      |           |     | bit needs to be set to zero. When   |      |
	|      |           |     | FS PHY interface is chosen and this |      |
	|      |           |     | bit                                 |      |
	|      |           |     | is set, the core expects that the   |      |
	|      |           |     | PHY clock is switched from 48 MHz   |      |
	|      |           |     | to                                  |      |
	|      |           |     | 32 KHz during Suspend.              |      |
	+------+-----------+-----+-------------------------------------+------+
	| 15:8 | ResValid  | R/W | Resume Validation Period (ResValid) | 0x2  |
	|      |           |     | This field is effective only when   |      |
	|      |           |     | HCFG.Ena32KHzS is set. It controls  |      |
	|      |           |     | the                                 |      |
	|      |           |     | Resume period when the core resumes |      |
	|      |           |     | from Suspend. The core counts       |      |
	|      |           |     | the ResValid number of clock cycles |      |
	|      |           |     | to detect a valid resume when this  |      |
	|      |           |     | is set.                             |      |
	+------+-----------+-----+-------------------------------------+------+
	| 22:16| Reserved\ | RO  | Reserved for future use.            |      |
	|      | _400_22_16|     |                                     |      |
	+------+-----------+-----+-------------------------------------+------+


To be continued ......

.. _table_usb_hcfg_contd_2:
.. table:: HCFG, Offset Address: 0x400 (continued)
	:widths: 1 2 1 6 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 23   | DescDMA   | R/W | Enable Scatter/gather DMA in Host   | 0x0  |
	|      |           |     | mode (DescDMA)                      |      |
	|      |           |     |                                     |      |
	|      |           |     | When the Scatter/Gather DMA option  |      |
	|      |           |     | is selected during configuration of |      |
	|      |           |     | the RTL, the application can set    |      |
	|      |           |     | this bit during initialization to   |      |
	|      |           |     | enable the                          |      |
	|      |           |     | Scatter/Gather DMA operation.       |      |
	|      |           |     | Note: This bit must be modified     |      |
	|      |           |     | only once after a reset. The        |      |
	|      |           |     | following                           |      |
	|      |           |     | combinations are available for      |      |
	|      |           |     | programming:                        |      |
	|      |           |     |                                     |      |
	|      |           |     | - GAHBCFG.DMAEn=0,HCFG.DescDMA=0 => |      |
	|      |           |     |   Slave mode                        |      |
	|      |           |     |                                     |      |
	|      |           |     | - GAHBCFG.DMAEn=0,HCFG.DescDMA=1 => |      |
	|      |           |     |   Invalid                           |      |
	|      |           |     |                                     |      |
	|      |           |     | - GAHBCFG.DMAEn=1,HCFG.DescDMA=0 => |      |
	|      |           |     |   Buffered DMA mode                 |      |
	|      |           |     |                                     |      |
	|      |           |     | - GAHBCFG.DMAEn=1,HCFG.DescDMA=1 => |      |
	|      |           |     |   Scatter/Gather DMA mode           |      |
	|      |           |     |                                     |      |
	|      |           |     | In non-Scatter/Gather DMA mode,     |      |
	|      |           |     | this bit is reserved.               |      |
	+------+-----------+-----+-------------------------------------+------+
	| 25:24| FrListEn  | R/W | Frame List Entries (FrListEn)       | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | The value in the register specifies |      |
	|      |           |     | the number of entries in the Frame  |      |
	|      |           |     | list. This field is valid only in   |      |
	|      |           |     | Scatter/Gather DMA mode.            |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b00: Reserved                   |      |
	|      |           |     | - 2'b01: 8 Entries                  |      |
	|      |           |     | - 2'b10: 16 Entries                 |      |
	|      |           |     | - 2'b11: 32 Entries                 |      |
	|      |           |     |                                     |      |
	|      |           |     | In non-Scatter/Gather DMA mode,     |      |
	|      |           |     | these bits are reserved.            |      |
	+------+-----------+-----+-------------------------------------+------+
	| 26   | Pe\       | R/W | Enable Periodic Scheduling          | 0x0  |
	|      | rSchedEna |     | (PerSchedEna)                       |      |
	|      |           |     |                                     |      |
	|      |           |     | Applicable in Host Scatter/Gather   |      |
	|      |           |     | DMA mode only. Enables periodic     |      |
	|      |           |     | scheduling within the core.         |      |
	|      |           |     | Initially, the bit is res and the   |      |
	|      |           |     | core does not                       |      |
	|      |           |     | process any periodic channels. As   |      |
	|      |           |     | soon as this bit is set, the core   |      |
	|      |           |     | gets                                |      |
	|      |           |     | ready to start scheduling periodic  |      |
	|      |           |     | channels and sets                   |      |
	|      |           |     | HCFG.PerSchedStat.                  |      |
	|      |           |     |                                     |      |
	|      |           |     | The setting of HCFG.PerSchedStat    |      |
	|      |           |     | indicates the core has enabled      |      |
	|      |           |     | periodic scheduling. Once           |      |
	|      |           |     | HCFG.PerSchedEna is set, the        |      |
	|      |           |     | application is                      |      |
	|      |           |     | not supposed to reset the bit       |      |
	|      |           |     | unless HCFG.PerSchedStat is set. As |      |
	|      |           |     | soon                                |      |
	|      |           |     | as this bit is reset, the core gets |      |
	|      |           |     | ready to stop scheduling periodic   |      |
	|      |           |     | channels and resets                 |      |
	|      |           |     | HCFG.PerSchedStat.                  |      |
	|      |           |     |                                     |      |
	|      |           |     | In non-Scatter/Gather DMA mode,     |      |
	|      |           |     | this bit is reserved.               |      |
	+------+-----------+-----+-------------------------------------+------+
	| 30:27| Reserved\ | RO  | Reserved for future use.            |      |
	|      | _400_30_27|     |                                     |      |
	+------+-----------+-----+-------------------------------------+------+


To be continued ......

.. _table_usb_hcfg_contd_3:
.. table:: HCFG, Offset Address: 0x400 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 31   | Mo\       | R/W | Mode Change Ready Timer Enable      | 0x0  |
	|      | deChTimEn |     | (ModeChTimEn)                       |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is used to enable/disable  |      |
	|      |           |     | the Host core to wait 200 PHY clock |      |
	|      |           |     | cycles at the end of Resume to      |      |
	|      |           |     | change the opmode signal to the PHY |      |
	|      |           |     | to                                  |      |
	|      |           |     | 00 after Suspend or LPM.            |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: The Host core waits for     |      |
	|      |           |     |   either 200 PHY clock cycles or a  |      |
	|      |           |     |   linestate of SE0 at the end of    |      |
	|      |           |     |   resume to the change the opmode   |      |
	|      |           |     |   from 2'b10 to 2'b00               |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: The Host core waits only    |      |
	|      |           |     |   for a linestate of SE0 at the end |      |
	|      |           |     |   of                                |      |
	|      |           |     |   resume to change the opmode from  |      |
	|      |           |     |   2'b10 to 2'b00.                   |      |
	+------+-----------+-----+-------------------------------------+------+

HFIR
````

Host Frame Interval Register

.. _table_usb_hfir:
.. table:: HFIR, Offset Address: 0x404
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc | Description                         | R    |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 15:0 | FrInt     | R/W | Frame Interval (FrInt)              |0xEA60|
	|      |           |     |                                     |      |
	|      |           |     | The value that the application      |      |
	|      |           |     | programs to this field specifies    |      |
	|      |           |     | the interval                        |      |
	|      |           |     | between two consecutive SOFs (FS)   |      |
	|      |           |     | or micro- SOFs (HS) or Keep-Alive   |      |
	|      |           |     | tokens (HS). This field contains    |      |
	|      |           |     | the number of PHY clocks that       |      |
	|      |           |     | constitute the                      |      |
	|      |           |     | required frame interval. The        |      |
	|      |           |     | default value set in this field for |      |
	|      |           |     | an FS operation                     |      |
	|      |           |     | when the PHY clock frequency is 60  |      |
	|      |           |     | MHz. The application can write a    |      |
	|      |           |     | value to                            |      |
	|      |           |     | this register only after the Port   |      |
	|      |           |     | Enable bit of the Host Port Control |      |
	|      |           |     | and Status                          |      |
	|      |           |     | register (HPRT.PrtEnaPort) has been |      |
	|      |           |     | set. If no value is programmed, the |      |
	|      |           |     | core                                |      |
	|      |           |     | calculates the value based on the   |      |
	|      |           |     | PHY clock specified in the FS/LS    |      |
	|      |           |     | PHY Clock                           |      |
	|      |           |     |                                     |      |
	|      |           |     | Select field of the Host            |      |
	|      |           |     | Configuration register              |      |
	|      |           |     | (HCFG.FSLSPclkSel). Do not          |      |
	|      |           |     | change the value of this field      |      |
	|      |           |     | after the initial configuration.    |      |
	|      |           |     |                                     |      |
	|      |           |     | - 125 us \* (PHY clock frequency    |      |
	|      |           |     |   for HS)                           |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1 ms \* (PHY clock frequency for  |      |
	|      |           |     |   FS/LS)                            |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 16   | HF\       | R/W | Reload Control (HFIRRldCtrl)        | 0x0  |
	|      | IRRldCtrl |     |                                     |      |
	|      |           |     | This bit allows dynamic reloading   |      |
	|      |           |     | of the HFIR register during run     |      |
	|      |           |     | time.                               |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: The HFIR cannot be reloaded |      |
	|      |           |     |   dynamically                       |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: The HFIR can be dynamically |      |
	|      |           |     |   reloaded during runtime.          |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit needs to be programmed     |      |
	|      |           |     | during initial configuration and    |      |
	|      |           |     | its value must                      |      |
	|      |           |     | not be changed during runtime.      |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31:17| Reserved\ | RO  | Reserved for future use.            |      |
	|      | _404_31_17|     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+

HFNUM
`````

Host Frame Number/Frame Time Remaining Register

.. _table_usb_hfnum:
.. table:: HFNUM, Offset Address: 0x408
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 15:0 | FrNum     | RO  | Frame Number (FrNum)                |      |
	|      |           |     |                                     |      |
	|      |           |     | This field increments when a new    |      |
	|      |           |     | SOF is transmitted on the USB, and  |      |
	|      |           |     | is                                  |      |
	|      |           |     | reset to 0 when it reaches          |      |
	|      |           |     | 16'h3FFF.                           |      |
	|      |           |     |                                     |      |
	|      |           |     | This field is writable only if      |      |
	|      |           |     | Remove Optional Features? was not   |      |
	|      |           |     | selected in                         |      |
	|      |           |     | coreConsultant (OTG_RM_OTG_FEATURES |      |
	|      |           |     | = 0). Otherwise, reads return       |      |
	|      |           |     | the frame number value.             |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31:16| FrRem     | RO  | Frame Time Remaining (FrRem)        |      |
	|      |           |     |                                     |      |
	|      |           |     | Indicates the amount of time        |      |
	|      |           |     | remaining in the current microframe |      |
	|      |           |     | (HS) or                             |      |
	|      |           |     | Frame (FS/LS), in terms of PHY      |      |
	|      |           |     | clocks. This field decrements on    |      |
	|      |           |     | each PHY                            |      |
	|      |           |     | clock. When it reaches zero, this   |      |
	|      |           |     | field is reloaded with the value in |      |
	|      |           |     | the Frame                           |      |
	|      |           |     |                                     |      |
	|      |           |     | Interval register and a new SOF is  |      |
	|      |           |     | transmitted on the USB.             |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+

HPTXSTS
```````

Host Periodic Transmit FIFO/Queue Status Register

.. _table_usb_hptxsts:
.. table:: HPTXSTS, Offset Address: 0x410
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 15:0 | PTx\      | RO  | Periodic Transmit Data FIFO Space   |      |
	|      | FSpcAvail |     |                                     |      |
	|      |           |     | Available (PTxFSpcAvail)            |      |
	|      |           |     |                                     |      |
	|      |           |     | Indicates the number of free        |      |
	|      |           |     | locations available to be written   |      |
	|      |           |     | to in the Periodic                  |      |
	|      |           |     |                                     |      |
	|      |           |     | TxFIFO. Values are in terms of      |      |
	|      |           |     | 32-bit words                        |      |
	|      |           |     |                                     |      |
	|      |           |     | - 16'h0: Periodic TxFIFO is full    |      |
	|      |           |     | - 16'h1: 1 word available           |      |
	|      |           |     | - 16'h2: 2 words available          |      |
	|      |           |     | - 16'hn: n words available (n: 0 ~  |      |
	|      |           |     |   32,768)                           |      |
	|      |           |     | - 16'h8000: 32,768 words available  |      |
	|      |           |     | - Others: Reserved                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 23:16| PTx\      | RO  | Periodic Transmit Request Queue     |      |
	|      | QSpcAvail |     |                                     |      |
	|      |           |     | Space Available (PTxQSpcAvail)      |      |
	|      |           |     |                                     |      |
	|      |           |     | Indicates the number of free        |      |
	|      |           |     | locations available to be written   |      |
	|      |           |     | in the Periodic                     |      |
	|      |           |     |                                     |      |
	|      |           |     | Transmit Request Queue. This queue  |      |
	|      |           |     | holds both IN and OUT requests.     |      |
	|      |           |     |                                     |      |
	|      |           |     | - 8'h0: Periodic Transmit Request   |      |
	|      |           |     |   ueue is full                      |      |
	|      |           |     |                                     |      |
	|      |           |     | - 8'h1: 1 location available        |      |
	|      |           |     |                                     |      |
	|      |           |     | - 8'h2: 2 locations available       |      |
	|      |           |     |                                     |      |
	|      |           |     | - n: n locations available (n:      |      |
	|      |           |     |   0~16)                             |      |
	|      |           |     |                                     |      |
	|      |           |     | - Others: Reserved                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31:24| PTxQTop   | RO  | Top of the Periodic Transmit        |      |
	|      |           |     | Request Queue (PTxQTop)             |      |
	|      |           |     |                                     |      |
	|      |           |     | This indicates the entry in the     |      |
	|      |           |     | Periodic Tx Request Queue that is   |      |
	|      |           |     | currently                           |      |
	|      |           |     | being processes by the MAC. This    |      |
	|      |           |     | register is used for debugging.     |      |
	|      |           |     |                                     |      |
	|      |           |     | - Bit [31]: Odd/Even (micro)Frame   |      |
	|      |           |     |                                     |      |
	|      |           |     |   - 1'b0: send in even (micro)Frame |      |
	|      |           |     |                                     |      |
	|      |           |     |   - 1'b1: send in odd (micro)Frame  |      |
	|      |           |     |                                     |      |
	|      |           |     | - Bits [30:27]: Channel/endpoint    |      |
	|      |           |     |   number                            |      |
	|      |           |     |                                     |      |
	|      |           |     | - Bits [26:25]: Type                |      |
	|      |           |     |                                     |      |
	|      |           |     |   - 2'b00: IN/OUT                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   - 2'b01: Zero-length packet       |      |
	|      |           |     |                                     |      |
	|      |           |     |   - 2'b10: CSPLIT                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   - 2'b11: Disable channel command  |      |
	|      |           |     |                                     |      |
	|      |           |     | - Bit [24]: Terminate (last entry   |      |
	|      |           |     |   for the selected channel or       |      |
	|      |           |     |   endpoint)                         |      |
	+------+-----------+-----+-------------------------------------+------+


HAINT
`````

Host All Channels Interrupt Register

.. _table_usb_haint:
.. table:: HAINT, Offset Address: 0x414
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 15:0 | HAINT     | RO  | Channel Interrupts (HAINT)          |      |
	|      |           |     |                                     |      |
	|      |           |     | One bit per channel: Bit 0 for      |      |
	|      |           |     | Channel 0, bit 15 for Channel 15    |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31:16| Reserved\ | RO  | Reserved for future use             |      |
	|      | _414_31_16|     |                                     |      |
	+------+-----------+-----+-------------------------------------+------+


HAINTMSK
````````

Host All Channels Interrupt Mask Register

.. _table_usb_haintmsk:
.. table:: HAINTMSK, Offset Address: 0x418
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 15:0 | HAINTMsk  | R/W | Channel Interrupt Mask (HAINTMsk)   | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | One bit per channel: Bit 0 for      |      |
	|      |           |     | channel 0, bit 15 for channel 15    |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31:16| Reserved\ | RO  | Reserved for future use             |      |
	|      | _418_31_16|     |                                     |      |
	+------+-----------+-----+-------------------------------------+------+

HFLBAddr
````````

Host Frame List Base Address Register

.. _table_usb_hflbaddr:
.. table:: HFLBAddr, Offset Address: 0x41c
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 31:0 | HFLBAddr  | R/W | The starting address of the Frame   | 0x0  |
	|      |           |     | list. This register is              |      |
	|      |           |     | used only for Isochronous and       |      |
	|      |           |     | Interrupt Channels.                 |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+

HCCHARn
```````

Host Channel-n Characteristics Register

.. _table_usb_hccharn_contd_0:
.. table:: HCCHARn, Offset Address: 0x500
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 10:0 | MPS       | R/W | Maximum Packet Size (MPS)           | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Indicates the maximum packet size   |      |
	|      |           |     | of the associated endpoint.         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 14:11| EPNum     | R/W | Endpoint Number (EPNum)             | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Indicates the endpoint number on    |      |
	|      |           |     | the device serving as the data      |      |
	|      |           |     | source                              |      |
	|      |           |     | or sink.                            |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 15   | EPDir     | R/W | Endpoint Direction (EPDir)          | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Indicates whether the transaction   |      |
	|      |           |     | is IN or OUT.                       |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: OUT                         |      |
	|      |           |     | - 1'b1: IN                          |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 16   | Reserv\   | RO  | Reserved for future use.            |      |
	|      | ed_500_16 |     |                                     |      |
	+------+-----------+-----+-------------------------------------+------+
	| 17   | LSpdDev   | R/W | Low-Speed Device (LSpdDev)          | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | This field is set by the            |      |
	|      |           |     | application to indicate that this   |      |
	|      |           |     | channel is                          |      |
	|      |           |     | communicating to a low-speed        |      |
	|      |           |     | device.                             |      |
	|      |           |     |                                     |      |
	|      |           |     | The application must program this   |      |
	|      |           |     | bit when a low speed device is      |      |
	|      |           |     | connected to the host through an FS |      |
	|      |           |     | HUB. The DWC_otg Host core          |      |
	|      |           |     | uses this field to drive the        |      |
	|      |           |     | XCVR_SELECT signal to 2'b11 while   |      |
	|      |           |     | communicating to the LS Device      |      |
	|      |           |     | through the FS hub.                 |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: In a peer to peer setup, the  |      |
	|      |           |     | DWC_otg Host core ignores this bit  |      |
	|      |           |     | even if it is set by the            |      |
	|      |           |     | application software.               |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_hccharn_contd_1:
.. table:: HCCHARn, Offset Address: 0x500 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 19:18| EPType    | R/W | Endpoint Type (EPType)              | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Indicates the transfer type         |      |
	|      |           |     | selected.                           |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b00: Control                    |      |
	|      |           |     | - 2'b01: Isochronous                |      |
	|      |           |     | - 2'b10: Bulk                       |      |
	|      |           |     | - 2'b11: Interrupt                  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 21:20| EC        | R/W | Multi Count (MC) / Error Count (EC) | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | When the Split Enable bit of the    |      |
	|      |           |     | Host Channel-n Split Control        |      |
	|      |           |     | register                            |      |
	|      |           |     | (HCSPLTn.SpltEna) is reset (1'b0),  |      |
	|      |           |     | this field indicates to the host    |      |
	|      |           |     | the                                 |      |
	|      |           |     | number of transactions that must be |      |
	|      |           |     | executed per microframe for this    |      |
	|      |           |     | periodic endpoint. For non-periodic |      |
	|      |           |     | transfers, this field is used only  |      |
	|      |           |     | in                                  |      |
	|      |           |     | DMA mode, and specifies the number  |      |
	|      |           |     | packets to be fetched for this      |      |
	|      |           |     | channel before the internal DMA     |      |
	|      |           |     | engine changes arbitration.         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b00: Reserved. This field       |      |
	|      |           |     |   yields undefined results.         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b01: 1 transaction              |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b10: 2 transactions to be       |      |
	|      |           |     |   issued for this endpoint per      |      |
	|      |           |     |   microframe                        |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b11: 3 transactions to be       |      |
	|      |           |     |   issued for this endpoint per      |      |
	|      |           |     |   microframe                        |      |
	|      |           |     |                                     |      |
	|      |           |     | When HCSPLTn.SpltEna is set (1'b1), |      |
	|      |           |     | this field indicates the number of  |      |
	|      |           |     | immediate retries to be performed   |      |
	|      |           |     | for a periodic split transaction on |      |
	|      |           |     | transaction errors. This field must |      |
	|      |           |     | be set to at least 2'b01.           |      |
	+------+-----------+-----+-------------------------------------+------+
	| 28:22| DevAddr   | R/W | Device Address (DevAddr)            | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | This field selects the specific     |      |
	|      |           |     | device serving as the data source   |      |
	|      |           |     | or sink.                            |      |
	+------+-----------+-----+-------------------------------------+------+


To be continued ......

.. _table_usb_hccharn_contd_2:
.. table:: HCCHARn, Offset Address: 0x500 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 29   | OddFrm    | R/W | Odd Frame (OddFrm)                  | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | This field is set (reset) by the    |      |
	|      |           |     | application to indicate that the    |      |
	|      |           |     | OTG host                            |      |
	|      |           |     | must perform a transfer in an odd   |      |
	|      |           |     | (micro)frame. This field is         |      |
	|      |           |     | applicable                          |      |
	|      |           |     | for only periodic (isochronous and  |      |
	|      |           |     | interrupt) transactions.            |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Even (micro)frame           |      |
	|      |           |     | - 1'b1: Odd (micro)frame            |      |
	|      |           |     |                                     |      |
	|      |           |     | This field is not applicable for    |      |
	|      |           |     | Scatter/Gather DMA mode and need    |      |
	|      |           |     | not                                 |      |
	|      |           |     | be programmed by the application    |      |
	|      |           |     | and is ignored by the core.         |      |
	+------+-----------+-----+-------------------------------------+------+
	| 30   | ChDis     | RWS | Write Behavior: One to set          |      |
	|      |           |     |                                     |      |
	|      |           |     | Channel Disable (ChDis)             |      |
	|      |           |     |                                     |      |
	|      |           |     | The application sets this bit to    |      |
	|      |           |     | stop transmitting/receiving data on |      |
	|      |           |     | a                                   |      |
	|      |           |     | channel, even before the transfer   |      |
	|      |           |     | for that channel is complete. The   |      |
	|      |           |     | application must wait for the       |      |
	|      |           |     | Channel Disabled interrupt before   |      |
	|      |           |     | treating                            |      |
	|      |           |     | the channel as disabled.            |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31   | ChEna     | RWS | Write Behavior: One to set          |      |
	|      |           |     | Channel Enable (ChEna)              |      |
	|      |           |     | When Scatter/Gather mode is         |      |
	|      |           |     | enabled:                            |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Indicates that the          |      |
	|      |           |     |   descriptor structure is not yet   |      |
	|      |           |     |   ready.                            |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: Indicates that the          |      |
	|      |           |     |   descriptor structure and data     |      |
	|      |           |     |   buffer with data                  |      |
	|      |           |     |   is setup and this channel can     |      |
	|      |           |     |   access the descriptor.            |      |
	|      |           |     |                                     |      |
	|      |           |     | When Scatter/Gather mode is         |      |
	|      |           |     | disabled:                           |      |
	|      |           |     |                                     |      |
	|      |           |     | This field is set by the            |      |
	|      |           |     | application and cleared by the OTG  |      |
	|      |           |     | host.                               |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Channel disabled            |      |
	|      |           |     | - 1'b1: Channel enabled             |      |
	+------+-----------+-----+-------------------------------------+------+

HCDMAn
``````

Host Channel-n DMA Address Register

.. _table_usb_hcdman:
.. table:: HCDMAn, Offset Address: 0x514
	:widths: 1 2 1 4 1

	+------+----------+-------+-------------------------------------+------+
	| Bits | Name     | Access| Description                         | Reset|
	+======+==========+=======+=====================================+======+
	| 31:0 | DMAAddr  | R/W   | DMA Address (DMAAddr)               | 0x0  |
	|      |          |       |                                     |      |
	|      |          |       | This field holds the start address  |      |
	|      |          |       | in the external memory from which   |      |
	|      |          |       | the data                            |      |
	|      |          |       | for the endpoint must be fetched or |      |
	|      |          |       | to which it must be stored. This    |      |
	|      |          |       | register is                         |      |
	|      |          |       | incremented on every AHB            |      |
	|      |          |       | transaction.                        |      |
	|      |          |       |                                     |      |
	|      |          |       | Shadow: Yes                         |      |
	|      |          |       |                                     |      |
	|      |          |       | Shadow Ctrl: vs_1t                  |      |
	|      |          |       |                                     |      |
	|      |          |       | Shadow Read Select: shrd_sel        |      |
	|      |          |       |                                     |      |
	|      |          |       | One-Way: Enabled                    |      |
	+------+----------+-------+-------------------------------------+------+

HCDMABn
```````

Host Channel-n DMA Buffer Address Register

.. _table_usb_hcdmabn:
.. table:: HCDMABn, Offset Address: 0x51c
	:widths: 1 2 1 4 1

	+------+----------+-------+-------------------------------------+------+
	| Bits | Name     | Access| Description                         | Reset|
	+======+==========+=======+=====================================+======+
	| 31:0 | DM\      | R/W   | DMA Address (DMAAddr)               | 0x0  |
	|      | ABufAddr |       |                                     |      |
	|      |          |       | Holds the current buffer address.   |      |
	|      |          |       | This register is updated as and     |      |
	|      |          |       | when the data                       |      |
	|      |          |       | transfer for the corresponding end  |      |
	|      |          |       | point is in progress. This register |      |
	|      |          |       | is present only                     |      |
	|      |          |       | in Scatter/Gather DMA mode.         |      |
	|      |          |       | Otherwise this field is reserved.   |      |
	|      |          |       |                                     |      |
	|      |          |       | Shadow: Yes                         |      |
	|      |          |       |                                     |      |
	|      |          |       | Shadow Ctrl: vs_1t                  |      |
	|      |          |       |                                     |      |
	|      |          |       | Shadow Read Select: shrd_sel        |      |
	|      |          |       |                                     |      |
	|      |          |       | One-Way: Enabled                    |      |
	+------+----------+-------+-------------------------------------+------+
