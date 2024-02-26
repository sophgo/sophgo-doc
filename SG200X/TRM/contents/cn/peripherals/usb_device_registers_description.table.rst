DCFG
````

Device Configuration Register

.. _table_usb_dcfg_contd_0:
.. table:: DCFG, Offset Address: 0x800
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 1:0  | DevSpd   | R/W | Device Speed (DevSpd)                | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | Indicates the speed at which the     |      |
	|      |          |     | application requires the core to     |      |
	|      |          |     | enumerate,                           |      |
	|      |          |     | or the maximum speed the application |      |
	|      |          |     | can support. However, the actual bus |      |
	|      |          |     | speed is determined only after the   |      |
	|      |          |     | chirp sequence is completed, and is  |      |
	|      |          |     | based on the speed of the USB host   |      |
	|      |          |     | to which the core is connected.      |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b00: High speed (USB 2.0 PHY     |      |
	|      |          |     |   clock is 30 MHz or 60 MHz)         |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b01: Full speed (USB 2.0 PHY     |      |
	|      |          |     |   clock is 30 MHz or 60 MHz)         |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b10: Low speed (USB 1.1          |      |
	|      |          |     |   transceiver clock is 6 MHz). If    |      |
	|      |          |     |   you select                         |      |
	|      |          |     |   6MHz LS mode, you must do a soft   |      |
	|      |          |     |   reset.                             |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b11: Full speed (USB 1.1         |      |
	|      |          |     |   transceiver clock is 48 MHz)       |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	|      |          |     |                                      |      |
	|      |          |     | One-Way: Enabled                     |      |
	+------+----------+-----+--------------------------------------+------+
	| 2    | NZSt\    | R/W | Non-Zero-Length Status OUT Handshake | 0x0  |
	|      | sOUTHShk |     | (NZStsOUTHShk)                       |      |
	|      |          |     |                                      |      |
	|      |          |     | The application can use this field   |      |
	|      |          |     | to select the handshake the core     |      |
	|      |          |     | sends on                             |      |
	|      |          |     | receiving a non zero-length data     |      |
	|      |          |     | packet during the OUT transaction of |      |
	|      |          |     | a                                    |      |
	|      |          |     | control transfer's Status stage.     |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: Send a STALL handshake ona   |      |
	|      |          |     |   non zero-length status OUT         |      |
	|      |          |     |   transaction and do not send the    |      |
	|      |          |     |   received OUT packet to the         |      |
	|      |          |     |   application.                       |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Send the received OUT packet |      |
	|      |          |     |   to the application (zero-length or |      |
	|      |          |     |   non zero-length) and send a        |      |
	|      |          |     |   handshake based on the NAK and     |      |
	|      |          |     |   STALL bits for the endpoint in the |      |
	|      |          |     |   Device Endpoint Control register.  |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_dcfg_contd_1:
.. table:: DCFG, Offset Address: 0x800 (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 3    | Ena3\    | R/W | Enable 32 KHz Suspend mode           | 0x0  |
	|      | 2KHzSusp |     | (Ena32KHzSusp)                       |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit can be set only if FS PHY   |      |
	|      |          |     | interface is selected. Otherwise,    |      |
	|      |          |     | this bit                             |      |
	|      |          |     | needs to be set to zero. If FS PHY   |      |
	|      |          |     | interface is chosen and this bit is  |      |
	|      |          |     | set, the                             |      |
	|      |          |     | PHY clock during Suspend must be     |      |
	|      |          |     | switched from 48 MHz to 32 KHz.      |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	|      |          |     |                                      |      |
	|      |          |     | One-Way: Enabled                     |      |
	+------+----------+-----+--------------------------------------+------+
	| 10:4 | DevAddr  | R/W | Device Address (DevAddr)             | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | The application must program this    |      |
	|      |          |     | field after every SetAddress control |      |
	|      |          |     | command.                             |      |
	+------+----------+-----+--------------------------------------+------+
	| 12:11| PerFrInt | R/W | Periodic Frame Interval (PerFrInt)   | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | Indicates the time within a          |      |
	|      |          |     | (micro)frame at which the            |      |
	|      |          |     | application must be                  |      |
	|      |          |     | notified using the End Of Periodic   |      |
	|      |          |     | Frame Interrupt. This can be used to |      |
	|      |          |     | determine if all the isochronous     |      |
	|      |          |     | traffic for that (micro)frame is     |      |
	|      |          |     | complete.                            |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b00: 80% of the (micro)frame     |      |
	|      |          |     |   interval                           |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b01: 85%                         |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b10: 90%                         |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b11: 95%                         |      |
	+------+----------+-----+--------------------------------------+------+
	| 13   | EnD\     | R/W | Enable Device OUT NAK (EnDevOutNak)  | 0x0  |
	|      | evOutNak |     |                                      |      |
	|      |          |     | This bit enables setting NAK for     |      |
	|      |          |     | Bulk OUT endpoints after the         |      |
	|      |          |     | transfer is                          |      |
	|      |          |     | completed for Device mode Descriptor |      |
	|      |          |     | DMA mode.                            |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: The core does not set NAK    |      |
	|      |          |     |   after Bulk OUT transfer complete   |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: The core sets NAK after Bulk |      |
	|      |          |     |   OUT transfer complete              |      |
	|      |          |     |                                      |      |
	|      |          |     | This is a one time programmable bit  |      |
	|      |          |     | after reset like any other DCFG      |      |
	|      |          |     | register bits.                       |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is valid only when          |      |
	|      |          |     | OTG_EN_DESC_DMA == 1'b1.             |      |
	+------+----------+-----+--------------------------------------+------+
	| 14   | XCVRDLY  | R/W | Enables or disables delay between    | 0x0  |
	|      |          |     | xcvr_sel and txvalid during device   |      |
	|      |          |     | chirp                                |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: Enable delay between         |      |
	|      |          |     |   xcvr_sel and txvalid during Device |      |
	|      |          |     |   chirp                              |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: No delay between xcvr_sel    |      |
	|      |          |     |   and txvalid during Device chirp    |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_dcfg_contd_2:
.. table:: DCFG, Offset Address: 0x800 (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 15   | Errat\   | R/W | Mode: Device                         | 0x0  |
	|      |          |     |                                      |      |
	|      | icIntMsk |     | Erratic Error Interrupt Mask         |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: Mask early suspend interrupt |      |
	|      |          |     |   on erratic error                   |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Early suspend interrupt is   |      |
	|      |          |     |   generated on erratic error         |      |
	+------+----------+-----+--------------------------------------+------+
	| 17:16| Re\      | RO  | Reserved for future use.             |      |
	|      | served_8 |     |                                      |      |
	|      | 00_17_16 |     |                                      |      |
	+------+----------+-----+--------------------------------------+------+
	| 22:18| EPMisCnt | R/W | IN Endpoint Mismatch Count           | 0x8  |
	|      |          |     | (EPMisCnt)                           |      |
	|      |          |     |                                      |      |
	|      |          |     | This field is valid only in shared   |      |
	|      |          |     | FIFO operation.                      |      |
	|      |          |     |                                      |      |
	|      |          |     | The application programs this field  |      |
	|      |          |     | with a count that determines when    |      |
	|      |          |     | the                                  |      |
	|      |          |     | core generates an Endpoint Mismatch  |      |
	|      |          |     | interrupt (GINTSTS.EPMis). The core  |      |
	|      |          |     | loads this value into an internal    |      |
	|      |          |     | counter and decrements it. The       |      |
	|      |          |     | counter is                           |      |
	|      |          |     | reloaded whenever there is a match   |      |
	|      |          |     | or when the counter expires. The     |      |
	|      |          |     | width                                |      |
	|      |          |     | of this counter depends on the depth |      |
	|      |          |     | of the Token Queue.                  |      |
	+------+----------+-----+--------------------------------------+------+
	| 23   | DescDMA  | R/W | Enable Scatter/Gather DMA in Device  | 0x0  |
	|      |          |     | mode (DescDMA).                      |      |
	|      |          |     |                                      |      |
	|      |          |     | When the Scatter/Gather DMA option   |      |
	|      |          |     | is selected during configuration of  |      |
	|      |          |     | the                                  |      |
	|      |          |     | RTL, the application can set this    |      |
	|      |          |     | bit during initialization to enable  |      |
	|      |          |     | the                                  |      |
	|      |          |     | Scatter/Gather DMA operation.        |      |
	|      |          |     | Note: This bit must be modified only |      |
	|      |          |     | once after a reset.                  |      |
	|      |          |     |                                      |      |
	|      |          |     | The following combinations are       |      |
	|      |          |     | available for programming:           |      |
	|      |          |     |                                      |      |
	|      |          |     | - GAHBCFG.DMAEn=0,DCFG.DescDMA=0 =>  |      |
	|      |          |     |   Slave mode                         |      |
	|      |          |     |                                      |      |
	|      |          |     | - GAHBCFG.DMAEn=0,DCFG.DescDMA=1 =>  |      |
	|      |          |     |   Invalid                            |      |
	|      |          |     |                                      |      |
	|      |          |     | - GAHBCFG.DMAEn=1,DCFG.DescDMA=0 =>  |      |
	|      |          |     |   Buffer DMA mode                    |      |
	|      |          |     |                                      |      |
	|      |          |     | - GAHBCFG.DMAEn=1,DCFG.DescDMA=1 =>  |      |
	|      |          |     |   Scatter/Gather DMA mode            |      |
	+------+----------+-----+--------------------------------------+------+


To be continued ......

.. _table_usb_dcfg_contd_3:
.. table:: DCFG, Offset Address: 0x800 (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 25:24| Per\     | R/W | Periodic Scheduling Interval         | 0x0  |
	|      | SchIntvl |     | (PerSchIntvl)                        |      |
	|      |          |     |                                      |      |
	|      |          |     | PerSchIntvl must be programmed only  |      |
	|      |          |     | for Scatter/Gather DMA mode.         |      |
	|      |          |     |                                      |      |
	|      |          |     | This field specifies the amount of   |      |
	|      |          |     | time the Internal DMA engine must    |      |
	|      |          |     | allocate For fetching periodic IN    |      |
	|      |          |     | endpoint data. Based on the number   |      |
	|      |          |     | of                                   |      |
	|      |          |     | periodic endpoints, this value must  |      |
	|      |          |     | be specified as 25,50 or 75% of      |      |
	|      |          |     | (micro)frame.                        |      |
	|      |          |     |                                      |      |
	|      |          |     | When any periodic endpoints are      |      |
	|      |          |     | active, the internal DMA engine      |      |
	|      |          |     | allocates                            |      |
	|      |          |     | the specified amount of time in      |      |
	|      |          |     | fetching periodic IN endpoint data.  |      |
	|      |          |     | When no periodic endpoints are       |      |
	|      |          |     | active, the internal DMA engine      |      |
	|      |          |     | services                             |      |
	|      |          |     | non-periodic endpoints, ignoring     |      |
	|      |          |     | this field.                          |      |
	|      |          |     |                                      |      |
	|      |          |     | After the specified time within a    |      |
	|      |          |     | (micro)frame, the DMA switches to    |      |
	|      |          |     | fetching                             |      |
	|      |          |     | for non-periodic endpoints.          |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b00: 25% of (micro)frame.        |      |
	|      |          |     | - 2'b01: 50% of (micro)frame.        |      |
	|      |          |     | - 2'b10: 75% of (micro)frame.        |      |
	|      |          |     | - 2'b11: Reserved.                   |      |
	+------+----------+-----+--------------------------------------+------+
	| 31:26| ResValid | R/W | Resume Validation Period (ResValid)  | 0x2  |
	|      |          |     | This field is effective only when    |      |
	|      |          |     | DCFG.Ena32KHzSusp is set. It         |      |
	|      |          |     | controls the                         |      |
	|      |          |     | resume period when the core resumes  |      |
	|      |          |     | from suspend. The core counts for    |      |
	|      |          |     | “ResValid” number of clock cycles to |      |
	|      |          |     | detect a valid resume when this bit  |      |
	|      |          |     | is set.                              |      |
	+------+----------+-----+--------------------------------------+------+

DCTL
````

Device Control Register

.. _table_usb_dctl_contd_0:
.. table:: DCTL, Offset Address: 0x804
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 0    | Rm\      | R/W | Remote Wakeup Signaling (RmtWkUpSig) | 0x0  |
	|      | tWkUpSig |     |                                      |      |
	|      |          |     | When the application sets this bit,  |      |
	|      |          |     | the core initiates remote            |      |
	|      |          |     | signaling to wake the USB host. The  |      |
	|      |          |     | application must set this            |      |
	|      |          |     | bit to instruct the core to exit the |      |
	|      |          |     | Suspend state. As specified in       |      |
	|      |          |     | the USB 2.0 specification, the       |      |
	|      |          |     | application must clear this bit 1-   |      |
	|      |          |     | 15 ms after setting it.If LPM is     |      |
	|      |          |     | enabled and the core is in the L1    |      |
	|      |          |     | (Sleep) state, when the application  |      |
	|      |          |     | sets this bit, the core              |      |
	|      |          |     | initiates L1 remote signaling to     |      |
	|      |          |     | wake up the USB host. The            |      |
	|      |          |     | application must set this bit to     |      |
	|      |          |     | instruct the core to exit the Sleep  |      |
	|      |          |     | state. As specified in the LPM       |      |
	|      |          |     | specification, the hardware          |      |
	|      |          |     | automatically clears this bit 50 us  |      |
	|      |          |     | (TL1DevDrvResume) after being        |      |
	|      |          |     | set by the application. The          |      |
	|      |          |     | application must not set this bit    |      |
	|      |          |     | when GLPMCFG bRemoteWake from the    |      |
	|      |          |     | previous LPM                         |      |
	|      |          |     | transaction is zero.                 |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	|      |          |     |                                      |      |
	|      |          |     | One-Way: Enabled                     |      |
	+------+----------+-----+--------------------------------------+------+
	| 1    | S\       | R/W | Soft Disconnect (SftDiscon)          | 0x1  |
	|      | ftDiscon |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | signal the DWC_otg core to do        |      |
	|      |          |     | a soft disconnect. As long as this   |      |
	|      |          |     | bit is set, the host does not        |      |
	|      |          |     | see that the device is connected,    |      |
	|      |          |     | and the device does not              |      |
	|      |          |     | receive signals on the USB. The core |      |
	|      |          |     | stays in the disconnected            |      |
	|      |          |     | state until the application clears   |      |
	|      |          |     | this bit.                            |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Normal operation. When this  |      |
	|      |          |     |   bit is cleared after a soft        |      |
	|      |          |     |   disconnect, the core drives the    |      |
	|      |          |     |   phy_opmode_o signal on             |      |
	|      |          |     |   the UTMI+ to 2'b00, which generates|      |
	|      |          |     |   a device connect                   |      |
	|      |          |     |   event to the USB host. When the    |      |
	|      |          |     |   device is reconnected, the         |      |
	|      |          |     |   USB host restarts device           |      |
	|      |          |     |   enumeration.                       |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: The core drives the          |      |
	|      |          |     |   phy_opmode_o signal on the         |      |
	|      |          |     |   UTMI+ to 2'b01, which generates a  |      |
	|      |          |     |   device disconnect event            |      |
	|      |          |     |   to the USB host.                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Note: This bit can be also used for  |      |
	|      |          |     | ULPI/FS Serial interfaces.           |      |
	|      |          |     |                                      |      |
	|      |          |     | Note: This bit is not impacted by a  |      |
	|      |          |     | soft reset.                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	+------+----------+-----+--------------------------------------+------+


To be continued ......

.. _table_usb_dctl_contd_1:
.. table:: DCTL, Offset Address: 0x804 (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 2    | GNP\     | RO  | Global Non-periodic IN NAK Status    |      |
	|      | INNakSts |     | (GNPINNakSts)                        |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: A handshake is sent out      |      |
	|      |          |     |   based on the data availability     |      |
	|      |          |     |   in the transmit FIFO.              |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: A NAK handshake is sent out  |      |
	|      |          |     |   on all non-periodic IN             |      |
	|      |          |     |   endpoints, irrespective of the data|      |
	|      |          |     |   availability in the transmit FIFO. |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	|      |          |     |                                      |      |
	|      |          |     | One-Way: Enabled                     |      |
	+------+----------+-----+--------------------------------------+------+
	| 3    | GO\      | RO  | Global OUT NAK Status (GOUTNakSts)   |      |
	|      | UTNakSts |     |                                      |      |
	|      |          |     | - 1'b0: A handshake is sent based on |      |
	|      |          |     |   the FIFO Status and                |      |
	|      |          |     |   the NAK and STALL bit settings.    |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: No data is written to the    |      |
	|      |          |     |   RxFIFO, irrespective of space      |      |
	|      |          |     |   availability. Sends a NAK handshake|      |
	|      |          |     |   on all packets, except             |      |
	|      |          |     |   on SETUP transactions. All         |      |
	|      |          |     |   isochronous OUT packets are        |      |
	|      |          |     |   dropped.                           |      |
	+------+----------+-----+--------------------------------------+------+
	| 6:4  | TstCtl   | R/W | Test Control (TstCtl)                | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | - 3'b000: Test mode disabled         |      |
	|      |          |     | - 3'b001: Test_J mode                |      |
	|      |          |     | - 3'b010: Test_K mode                |      |
	|      |          |     | - 3'b011: Test_SE0_NAK mode          |      |
	|      |          |     | - 3'b100: Test_Packet mode           |      |
	|      |          |     | - 3'b101: Test_Force_Enable          |      |
	|      |          |     | - Others: Reserved                   |      |
	+------+----------+-----+--------------------------------------+------+
	| 7    | S\       | RWC | Set Global Non-periodic IN NAK       |      |
	|      | GNPInNak |     | (SGNPInNak)                          |      |
	|      |          |     |                                      |      |
	|      |          |     | A write to this field sets the       |      |
	|      |          |     | Global Non-periodic IN NAK.The       |      |
	|      |          |     | application uses this bit to send a  |      |
	|      |          |     | NAK handshake on all nonperiodic     |      |
	|      |          |     | IN endpoints. The core can also set  |      |
	|      |          |     | this bit when a                      |      |
	|      |          |     | timeout condition is detected on a   |      |
	|      |          |     | non-periodic endpoint in             |      |
	|      |          |     | shared FIFO operation.               |      |
	|      |          |     |                                      |      |
	|      |          |     | The application must set this bit    |      |
	|      |          |     | only after making sure that the      |      |
	|      |          |     | Global IN NAK Effective bit in the   |      |
	|      |          |     | Core Interrupt Register              |      |
	|      |          |     | (GINTSTS.GINNakEff) is cleared.      |      |
	+------+----------+-----+--------------------------------------+------+
	| 8    | C\       | RWC | Clear Global Non-periodic IN NAK     |      |
	|      | GNPInNak |     | (CGNPInNak)                          |      |
	|      |          |     |                                      |      |
	|      |          |     | A write to this field clears the     |      |
	|      |          |     | Global Non-periodic IN NAK.          |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_dctl_contd_2:
.. table:: DCTL, Offset Address: 0x804 (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 9    | SGOUTNak | RWC | Set Global OUT NAK (SGOUTNak)        |      |
	|      |          |     |                                      |      |
	|      |          |     | A write to this field sets the       |      |
	|      |          |     | Global OUT NAK.                      |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | send a NAK handshake on all          |      |
	|      |          |     | OUT endpoints. The application must  |      |
	|      |          |     | set the this bit only after          |      |
	|      |          |     | making sure that the Global OUT NAK  |      |
	|      |          |     | Effective bit in the Core            |      |
	|      |          |     | Interrupt Register                   |      |
	|      |          |     | (GINTSTS.GOUTNakEff) is cleared.     |      |
	+------+----------+-----+--------------------------------------+------+
	| 10   | CGOUTNak | RWC | Clear Global OUT NAK (CGOUTNak)      |      |
	|      |          |     | A write to this field clears the     |      |
	|      |          |     | Global OUT NAK.                      |      |
	+------+----------+-----+--------------------------------------+------+
	| 11   | PWRO\    | R/W | Power-On Programming Done            | 0x0  |
	|      | nPrgDone |     | (PWROnPrgDone)                       |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | indicate that register               |      |
	|      |          |     | programming is complete after a      |      |
	|      |          |     | wake-up from Power Down mode.        |      |
	+------+----------+-----+--------------------------------------+------+
	| 12   | Reserve\ | RO  | Reserved for future use.             |      |
	|      | d_804_12 |     |                                      |      |
	+------+----------+-----+--------------------------------------+------+
	| 14:13| GMC      | R/W | Global Multi Count (GMC)             | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | GMC must be programmed only once     |      |
	|      |          |     | after initialization.                |      |
	|      |          |     |                                      |      |
	|      |          |     | Applicable only for Scatter/Gather   |      |
	|      |          |     | DMA mode. This indicates             |      |
	|      |          |     | the number of packets to be serviced |      |
	|      |          |     | for that end point before            |      |
	|      |          |     | moving to the next end point. It is  |      |
	|      |          |     | only for non-periodic end            |      |
	|      |          |     | points.                              |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b00: Invalid.                    |      |
	|      |          |     | - 2'b01: 1 packet.                   |      |
	|      |          |     | - 2'b10: 2 packets.                  |      |
	|      |          |     | - 2'b11: 3 packets.                  |      |
	|      |          |     |                                      |      |
	|      |          |     | The value of this field              |      |
	|      |          |     | automatically changes to 2'h1 when   |      |
	|      |          |     | DCFG.DescDMA is set to 1. When       |      |
	|      |          |     | Scatter/Gather DMA mode              |      |
	|      |          |     | is disabled, this field is reserved  |      |
	|      |          |     | and reads 2'b00.                     |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_dctl_contd_4:
.. table:: DCTL, Offset Address: 0x804 (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 15   | Ig\      | R/W | Ignore frame number for isochronous  | 0x0  |
	|      | nrFrmNum |     | endpoints (IgnrFrmNum)               |      |
	|      |          |     |                                      |      |
	|      |          |     | Slave Mode (GAHBCFG.DMAEn=0):        |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is not valid in Slave mode  |      |
	|      |          |     | and should not be                    |      |
	|      |          |     | programmed to 1.Non-Scatter/Gather   |      |
	|      |          |     | DMA mode                             |      |
	|      |          |     | (GAHBCFG.DMAEn=1,DCFG.DescDMA=0):    |      |
	|      |          |     | This bit is not used when Threshold  |      |
	|      |          |     | mode is enabled and                  |      |
	|      |          |     | should not be programmed to 1.       |      |
	|      |          |     | In non-Scatter/Gather DMA mode, the  |      |
	|      |          |     | application receives                 |      |
	|      |          |     | transfer complete interrupt after    |      |
	|      |          |     | transfers for multiple               |      |
	|      |          |     | (micro)frames are completed.         |      |
	|      |          |     |                                      |      |
	|      |          |     | - When Scatter/Gather DMA mode is    |      |
	|      |          |     |   disabled, this field is            |      |
	|      |          |     |   used by the application to enable  |      |
	|      |          |     |   periodic transfer interrupt.       |      |
	|      |          |     |                                      |      |
	|      |          |     | The application can program periodic |      |
	|      |          |     | endpoint transfers for               |      |
	|      |          |     | multiple (micro)frames.              |      |
	|      |          |     |                                      |      |
	|      |          |     | - 0: Periodic transfer interrupt     |      |
	|      |          |     |   feature is disabled; the           |      |
	|      |          |     |   application must program transfers |      |
	|      |          |     |   for periodic                       |      |
	|      |          |     |   endpoints every (micro)frame       |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1: Packets are not flushed when an |      |
	|      |          |     |   ISOC IN token is                   |      |
	|      |          |     |   received for an elapsed frame. The |      |
	|      |          |     |   core ignores the                   |      |
	|      |          |     |   frame number, sending packets as   |      |
	|      |          |     |   soon as the packets                |      |
	|      |          |     |   are ready, and the corresponding   |      |
	|      |          |     |   token is received. This            |      |
	|      |          |     |   field is also used by the          |      |
	|      |          |     |   application to enable periodic     |      |
	|      |          |     |   transfer interrupts.               |      |
	|      |          |     |                                      |      |
	|      |          |     | Scatter/Gather DMA Mode              |      |
	|      |          |     |                                      |      |
	|      |          |     | (GAHBCFG.DMAEn=1,DCFG.DescDMA=1):    |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is not applicable to        |      |
	|      |          |     | high-speed, high-bandwidth           |      |
	|      |          |     | transfers and should not be          |      |
	|      |          |     | programmed to 1.                     |      |
	|      |          |     |                                      |      |
	|      |          |     | In addition, this bit is not used    |      |
	|      |          |     | when Threshold mode is               |      |
	|      |          |     | enabled and should not be programmed |      |
	|      |          |     | to 1.                                |      |
	|      |          |     |                                      |      |
	|      |          |     | - 0: The core transmits the packets  |      |
	|      |          |     |   only in the frame number           |      |
	|      |          |     |   in which they are intended to be   |      |
	|      |          |     |   transmitted.                       |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1: Packets are not flushed when an |      |
	|      |          |     |   ISOC IN token is                   |      |
	|      |          |     |   received for an elapsed frame. The |      |
	|      |          |     |   core ignores the frame             |      |
	|      |          |     |   number, sending packets as soon as |      |
	|      |          |     |   the packets are ready,             |      |
	|      |          |     |   and the corresponding token is     |      |
	|      |          |     |   received. When this bit is         |      |
	|      |          |     |   set, there must be only one packet |      |
	|      |          |     |   per descriptor.                    |      |
	+------+----------+-----+--------------------------------------+------+
	| 16   | N\       | R/W | NAK on Babble Error (NakOnBble)      | 0x0  |
	|      | akOnBble |     |                                      |      |
	|      |          |     | Set NAK automatically on babble      |      |
	|      |          |     | (NakOnBble). The core sets           |      |
	|      |          |     | NAK automatically for the endpoint   |      |
	|      |          |     | on which babble is received.         |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_dctl_contd_3:
.. table:: DCTL, Offset Address: 0x804 (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 17   | EnC\     | R/W | Enable Continue on BNA (EnContOnBNA) | 0x0  |
	|      | ontOnBNA |     |                                      |      |
	|      |          |     | This bit enables the DWC_otg core to |      |
	|      |          |     | continue on BNA for Bulk             |      |
	|      |          |     | OUT and INTR OUT endpoints. With     |      |
	|      |          |     | this feature enabled,                |      |
	|      |          |     | when a Bulk OUT or INTR OUT endpoint |      |
	|      |          |     | receives a BNA                       |      |
	|      |          |     | interrupt the core starts processing |      |
	|      |          |     | the descriptor that caused           |      |
	|      |          |     | the BNA interrupt after the endpoint |      |
	|      |          |     | re-enables the endpoint.             |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: After receiving BNA          |      |
	|      |          |     |   interrupt, the core disables the   |      |
	|      |          |     |   endpoint. When the endpoint is     |      |
	|      |          |     |   re-enabled by the                  |      |
	|      |          |     |   application, the core starts       |      |
	|      |          |     |   processing from the DOEPDMA        |      |
	|      |          |     |   descriptor.                        |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: After receiving BNA          |      |
	|      |          |     |   interrupt, the core disables the   |      |
	|      |          |     |   endpoint. When the endpoint is     |      |
	|      |          |     |   re-enabled by the                  |      |
	|      |          |     |   application, the core starts       |      |
	|      |          |     |   processing from the descriptor     |      |
	|      |          |     |   that received the BNA interrupt.   |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is valid only when          |      |
	|      |          |     | OTG_EN_DESC_DMA == 1'b1. It is       |      |
	|      |          |     | a one-time programmable after reset  |      |
	|      |          |     | bit like any other DCTL              |      |
	|      |          |     | register bits.                       |      |
	+------+----------+-----+--------------------------------------+------+
	| 18   | Dee\     | R/W | Deep Sleep BESL Reject               | 0x0  |
	|      | pSleepBE\|     |                                      |      |
	|      | SLReject |     | Core rejects LPM request with HIRD   |      |
	|      |          |     | value greater than HIRD              |      |
	|      |          |     | threshold programmed. NYET response  |      |
	|      |          |     | is sent for LPM tokens               |      |
	|      |          |     | with HIRD value greater than HIRD    |      |
	|      |          |     | threshold. By default, the           |      |
	|      |          |     | Deep Sleep BESL Reject feature is    |      |
	|      |          |     | disabled.                            |      |
	+------+----------+-----+--------------------------------------+------+
	| 31:19| Re\      | RO  | Reserved for future use.             |      |
	|      | served_8 |     |                                      |      |
	|      | 04_31_19 |     |                                      |      |
	+------+----------+-----+--------------------------------------+------+

DSTS
````

Device Status Register

.. _table_usb_dsts_contd_0:
.. table:: DSTS, Offset Address: 0x808
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 0    | SuspSts  | RO  | Suspend Status (SuspSts)             |      |
	|      |          |     |                                      |      |
	|      |          |     | In Device mode, this bit is set as   |      |
	|      |          |     | long as a Suspend condition is       |      |
	|      |          |     | detected on                          |      |
	|      |          |     | the USB. The core enters the Suspend |      |
	|      |          |     | state when there is no activity on   |      |
	|      |          |     | the                                  |      |
	|      |          |     | phy_line_state_i signal for an       |      |
	|      |          |     | extended period of time.             |      |
	|      |          |     |                                      |      |
	|      |          |     | The core comes out of the suspend    |      |
	|      |          |     | under the following conditions:      |      |
	|      |          |     |                                      |      |
	|      |          |     | - If there is any activity on the    |      |
	|      |          |     |   phy_line_state_i signal            |      |
	|      |          |     |                                      |      |
	|      |          |     | - If the application writes to the   |      |
	|      |          |     |   Remote Wakeup Signaling bit in the |      |
	|      |          |     |   Device                             |      |
	|      |          |     |   Control register (DCTL.RmtWkUpSig).|      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	+------+----------+-----+--------------------------------------+------+
	| 2:1  | EnumSpd  | RO  | Enumerated Speed (EnumSpd)           |      |
	|      |          |     |                                      |      |
	|      |          |     | Indicates the speed at which the     |      |
	|      |          |     | DWC_otg core has come up after speed |      |
	|      |          |     | detection through a chirp sequence.  |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b00: High speed (PHY clock is    |      |
	|      |          |     |   running at 30 or 60 MHz)           |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b01: Full speed (PHY clock is    |      |
	|      |          |     |   running at 30 or 60 MHz)           |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b10: Low speed (PHY clock is     |      |
	|      |          |     |   running at 6 MHz)                  |      |
	|      |          |     |                                      |      |
	|      |          |     | - 2'b11: Full speed (PHY clock is    |      |
	|      |          |     |   running at 48 MHz)                 |      |
	|      |          |     |                                      |      |
	|      |          |     | Low speed is not supported for       |      |
	|      |          |     | devices using a UTMI+ PHY.           |      |
	+------+----------+-----+--------------------------------------+------+
	| 3    | E\       | RO  | Erratic Error (ErrticErr)            |      |
	|      | rrticErr |     |                                      |      |
	|      |          |     | The core sets this bit to report any |      |
	|      |          |     | erratic errors                       |      |
	|      |          |     | (phy_rxvalid_i/phy_rxvldh_i          |      |
	|      |          |     | or phy_rxactive_i is asserted For at |      |
	|      |          |     | least 2 ms, due to PHY error) seen   |      |
	|      |          |     | on                                   |      |
	|      |          |     | the UTMI+. Due to erratic errors,    |      |
	|      |          |     | the DWC_otg core goes into Suspend   |      |
	|      |          |     | state                                |      |
	|      |          |     | and an interrupt is generated to the |      |
	|      |          |     | application with Early Suspend bit   |      |
	|      |          |     | of the                               |      |
	|      |          |     | Core Interrupt register              |      |
	|      |          |     | (GINTSTS.ErlySusp). If the early     |      |
	|      |          |     | suspend is asserted                  |      |
	|      |          |     | because of an erratic error, the     |      |
	|      |          |     | application can only perform a soft  |      |
	|      |          |     | disconnect recover.                  |      |
	+------+----------+-----+--------------------------------------+------+
	| 7:4  | Reserved\| RO  | Reserved for future use.             |      |
	|      | _808_7_4 |     |                                      |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_dsts_contd_1:
.. table:: DSTS, Offset Address: 0x808 (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 21:8 | SOFFN    | RO  | Frame or Microframe Number of the    |      |
	|      |          |     | Received SOF (SOFFN)                 |      |
	|      |          |     |                                      |      |
	|      |          |     | When the core is operating at high   |      |
	|      |          |     | speed, this field contains a         |      |
	|      |          |     | microframe                           |      |
	|      |          |     | number. When the core is operating   |      |
	|      |          |     | at full or low speed, this field     |      |
	|      |          |     | contains a                           |      |
	|      |          |     | Frame number.                        |      |
	|      |          |     |                                      |      |
	|      |          |     | Note: This register may return a non |      |
	|      |          |     | zero value if read immediately after |      |
	|      |          |     | power on reset. In case the register |      |
	|      |          |     | bit reads non zero immediately after |      |
	|      |          |     | power on reset it does not indicate  |      |
	|      |          |     | that SOF has been received from the  |      |
	|      |          |     | host. The read value of this         |      |
	|      |          |     | interrupt is valid only after a      |      |
	|      |          |     | valid connection                     |      |
	|      |          |     | between host and device is           |      |
	|      |          |     | established.                         |      |
	+------+----------+-----+--------------------------------------+------+
	| 23:22| DevLnSts | RO  | Device Line Status (DevLnSts)        |      |
	|      |          |     |                                      |      |
	|      |          |     | Indicates the current logic level    |      |
	|      |          |     | USB data lines                       |      |
	|      |          |     |                                      |      |
	|      |          |     | - Bit [23]: Logic level of D+        |      |
	|      |          |     | - Bit [22]: Logic level of D-        |      |
	+------+----------+-----+--------------------------------------+------+
	| 31:24| Re\      | RO  | Reserved for future use.             |      |
	|      | served_8\|     |                                      |      |
	|      | 08_31_24 |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	+------+----------+-----+--------------------------------------+------+

DIEPMSK
```````

Device IN Endpoint Common Interrupt Mask Register

.. _table_usb_diepmsk:
.. table:: DIEPMSK, Offset Address: 0x810
	:widths: 1 2 1 4 1

	+------+---------------+-----+---------------------------------+------+
	| Bits | Name          | Acc\| Description                     | R\   |
	|      |               | ess |                                 | eset |
	+======+===============+=====+=================================+======+
	| 0    | D\            | R/W | Transfer Completed Interrupt    | 0x0  |
	|      | iXferComplMsk |     | Mask (XferComplMsk)             |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow: Yes                     |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow Ctrl: vs_1t              |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow Read Select: shrd_sel    |      |
	|      |               |     |                                 |      |
	|      |               |     | One-Way: Enabled                |      |
	+------+---------------+-----+---------------------------------+------+
	| 1    | DiEPDisbldMsk | R/W | Endpoint Disabled Interrupt     | 0x0  |
	|      |               |     | Mask (EPDisbldMsk)              |      |
	+------+---------------+-----+---------------------------------+------+
	| 2    | DiAHBErrMsk   | R/W | AHB Error Mask (AHBErrMsk)      | 0x0  |
	+------+---------------+-----+---------------------------------+------+
	| 3    | TimeOUTMsk    | R/W | Timeout Condition Mask          | 0x0  |
	|      |               |     | (TimeOUTMsk) (Non-isochronous   |      |
	|      |               |     | endpoints)                      |      |
	+------+---------------+-----+---------------------------------+------+
	| 4    | I\            | R/W | IN Token Received When TxFIFO   | 0x0  |
	|      | NTknTXFEmpMsk |     | Empty Mask (INTknTXFEmpMsk)     |      |
	+------+---------------+-----+---------------------------------+------+
	| 5    | INTknEPMisMsk | R/W | IN Token received with EP       | 0x0  |
	|      |               |     | Mismatch Mask (INTknEPMisMsk)   |      |
	+------+---------------+-----+---------------------------------+------+
	| 6    | INEPNakEffMsk | R/W | IN Endpoint NAK Effective Mask  | 0x0  |
	|      |               |     | (INEPNakEffMsk)                 |      |
	+------+---------------+-----+---------------------------------+------+
	| 7    | R\            | RO  | Reserved for future use.        |      |
	|      | eserved_810_7 |     |                                 |      |
	+------+---------------+-----+---------------------------------+------+
	| 8    | T\            | R/W | Fifo Underrun Mask              | 0x0  |
	|      | xfifoUndrnMsk |     | (TxfifoUndrnMsk)                |      |
	+------+---------------+-----+---------------------------------+------+
	| 9    | BNAInIntrMsk  | R/W | BNA Interrupt Mask              | 0x0  |
	|      |               |     | (BNAInIntrMsk)                  |      |
	|      |               |     |                                 |      |
	|      |               |     | This bit is valid only when     |      |
	|      |               |     | Device Descriptor DMA is        |      |
	|      |               |     | enabled.                        |      |
	+------+---------------+-----+---------------------------------+------+
	| 12:10| Reser\        | RO  | Reserved for future use.        |      |
	|      | ved_810_12_10 |     |                                 |      |
	+------+---------------+-----+---------------------------------+------+
	| 13   | DiNAKMsk      | R/W | NAK interrupt Mask (NAKMsk)     | 0x0  |
	|      |               |     |                                 |      |
	|      |               |     | Shadow: Yes                     |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow Ctrl: vs_1t              |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow Read Select: shrd_sel    |      |
	+------+---------------+-----+---------------------------------+------+
	| 31:14| Reser\        | RO  | Reserved for future use.        |      |
	|      | ved_810_31_14 |     |                                 |      |
	+------+---------------+-----+---------------------------------+------+

DOEPMSK
```````

Device OUT Endpoint Common Interrupt Mask Register

.. _table_usb_doepmsk:
.. table:: DOEPMSK, Offset Address: 0x814
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 0    | Xfe\      | R/W | Transfer Completed Interrupt Mask   | 0x0  |
	|      | rComplMsk |     | (XferComplMsk)                      |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 1    | EP\       | R/W | Endpoint Disabled Interrupt Mask    | 0x0  |
	|      | DisbldMsk |     | (EPDisbldMsk)                       |      |
	+------+-----------+-----+-------------------------------------+------+
	| 2    | AHBErrMsk | R/W | AHB Error (AHBErrMsk)               | 0x0  |
	+------+-----------+-----+-------------------------------------+------+
	| 3    | SetUPMsk  | R/W | SETUP Phase Done Mask (SetUPMsk)    | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Applies to control endpoints only.  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 4    | OUTTk\    | R/W | OUT Token Received when Endpoint    | 0x0  |
	|      | nEPdisMsk |     | Disabled Mask                       |      |
	|      |           |     | (OUTTknEPdisMsk)                    |      |
	|      |           |     |                                     |      |
	|      |           |     | Applies to control OUT endpoints    |      |
	|      |           |     | only.                               |      |
	+------+-----------+-----+-------------------------------------+------+
	| 5    | StsPh\    | R/W | Status Phase Received Mask          | 0x0  |
	|      | seRcvdMsk |     | (StsPhseRcvdMsk)                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 6    | Back2Bac\ | R/W | Back-to-Back SETUP Packets Received | 0x0  |
	|      | kSETupMsk |     | Mask (Back2BackSETupMsk)            |      |
	|      |           |     |                                     |      |
	|      |           |     | Applies to control OUT endpoints    |      |
	|      |           |     | only.                               |      |
	+------+-----------+-----+-------------------------------------+------+
	| 7    | Reser\    | RO  | Reserved for future use.            |      |
	|      | ved_814_7 |     |                                     |      |
	+------+-----------+-----+-------------------------------------+------+
	| 8    | Out\      | R/W | OUT Packet Error Mask               | 0x0  |
	|      | PktErrMsk |     | (OutPktErrMsk)                      |      |
	+------+-----------+-----+-------------------------------------+------+
	| 9    | BnaO\     | R/W | BNA interrupt Mask (BnaOutIntrMsk)  | 0x0  |
	|      | utIntrMsk |     |                                     |      |
	+------+-----------+-----+-------------------------------------+------+
	| 11:10| Reserved\ | RO  | Reserved for future use.            |      |
	|      | _814_11_10|     |                                     |      |
	+------+-----------+-----+-------------------------------------+------+
	| 12   | B\        | R/W | Babble Error interrupt Mask         | 0x0  |
	|      | bleErrMsk |     | (BbleErrMsk)                        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 13   | NAKMsk    | R/W | NAK interrupt Mask (NAKMsk)         | 0x0  |
	+------+-----------+-----+-------------------------------------+------+
	| 14   | NYETMsk   | R/W | NYET interrupt Mask (NYETMsk)       | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31:15| Reserved\ | RO  | Reserved for future use.            |      |
	|      | _814_31_15|     |                                     |      |
	+------+-----------+-----+-------------------------------------+------+

DAINT
`````

Device All Endpoints Interrupt Register

.. _table_usb_daint:
.. table:: DAINT, Offset Address: 0x818
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 15:0 | InEpInt   | RO  | OUT Endpoint Interrupt Bits         |      |
	|      |           |     | (OutEPInt)                          |      |
	|      |           |     |                                     |      |
	|      |           |     | One bit per OUT endpoint:           |      |
	|      |           |     |                                     |      |
	|      |           |     | Bit 16 for OUT endpoint 0, bit 31   |      |
	|      |           |     | for OUT endpoint 15                 |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31:16| OutEPInt  | RO  | OUT Endpoint Interrupt Bits         |      |
	|      |           |     | (OutEPInt)                          |      |
	|      |           |     |                                     |      |
	|      |           |     | One bit per OUT endpoint:           |      |
	|      |           |     |                                     |      |
	|      |           |     | Bit 16 for OUT endpoint 0, bit 31   |      |
	|      |           |     | for OUT endpoint 15                 |      |
	+------+-----------+-----+-------------------------------------+------+

DAINTMSK
````````

Device Endpoints Interrupt Mask Register

.. _table_usb_daintmsk:
.. table:: DAINTMSK, Offset Address: 0x81c
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 15:0 | InEpMsk   | R/W | IN EP Interrupt Mask Bits (InEpMsk) | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | One bit per IN Endpoint:            |      |
	|      |           |     |                                     |      |
	|      |           |     | Bit 0 for IN EP 0, bit 15 for IN EP |      |
	|      |           |     | 15                                  |      |
	|      |           |     |                                     |      |
	|      |           |     | The value of this field depends on  |      |
	|      |           |     | the number of IN endpoints that are |      |
	|      |           |     | configured.                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31:16| OutEpMsk  | R/W | OUT EP Interrupt Mask Bits          | 0x0  |
	|      |           |     | (OutEpMsk)                          |      |
	|      |           |     |                                     |      |
	|      |           |     | One per OUT endpoint:               |      |
	|      |           |     |                                     |      |
	|      |           |     | Bit 16 for OUT EP 0, bit 31 for OUT |      |
	|      |           |     | EP 15                               |      |
	|      |           |     |                                     |      |
	|      |           |     | The value of this field depends on  |      |
	|      |           |     | the number of OUT endpoints that    |      |
	|      |           |     | are configured.                     |      |
	+------+-----------+-----+-------------------------------------+------+

DIEPEMPMSK
``````````

Device IN Endpoint FIFO Empty Interrupt Mask Register

.. _table_usb_diepempmsk:
.. table:: DIEPEMPMSK, Offset Address: 0x834
	:widths: 1 2 1 4 1

	+------+---------------+-----+---------------------------------+------+
	| Bits | Name          | Acc\| Description                     | R\   |
	|      |               | ess |                                 | eset |
	+======+===============+=====+=================================+======+
	| 15:0 | InEpTxfEmpMsk | R/W | IN EP Tx FIFO Empty Interrupt   | 0x0  |
	|      |               |     | Mask Bits (InEpTxfEmpMsk)       |      |
	|      |               |     |                                 |      |
	|      |               |     | These bits acts as mask bits    |      |
	|      |               |     | for DIEPINTn.                   |      |
	|      |               |     |                                 |      |
	|      |               |     | TxFEmp interrupt One bit per IN |      |
	|      |               |     | Endpoint:                       |      |
	|      |               |     |                                 |      |
	|      |               |     | - Bit 0 for IN endpoint 0       |      |
	|      |               |     | - ...                           |      |
	|      |               |     | - Bit 15 for endpoint 15        |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow: Yes                     |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow Ctrl: vs_1t              |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow Read Select: shrd_sel    |      |
	|      |               |     |                                 |      |
	|      |               |     | One-Way: Enabled                |      |
	+------+---------------+-----+---------------------------------+------+
	| 31:16| Reser\        | RO  | Reserved for future use.        |      |
	|      | ved_834_31_16 |     |                                 |      |
	+------+---------------+-----+---------------------------------+------+

DEACHINT
````````

Device Each Endpoint Interrupt Register

.. _table_usb_deachint:
.. table:: DEACHINT, Offset Address: 0x838
	:widths: 1 2 1 4 1

	+------+---------------+-----+---------------------------------+------+
	| Bits | Name          | Acc\| Description                     | R\   |
	|      |               | ess |                                 | eset |
	+======+===============+=====+=================================+======+
	| 15:0 | EchInEpInt    | RO  | IN Endpoint Interrupt Bits      |      |
	|      |               |     | (EchInEpInt)                    |      |
	|      |               |     |                                 |      |
	|      |               |     | One bit per IN Endpoint:        |      |
	|      |               |     |                                 |      |
	|      |               |     | - Bit 0 for IN endpoint 0       |      |
	|      |               |     | - ...                           |      |
	|      |               |     | - Bit 15 for endpoint 15        |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow: Yes                     |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow Ctrl: vs_1t              |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow Read Select: shrd_sel    |      |
	|      |               |     |                                 |      |
	|      |               |     | One-Way: Enabled                |      |
	+------+---------------+-----+---------------------------------+------+
	| 31:16| EchOutEPInt   | RO  | OUT Endpoint Interrupt Bits     |      |
	|      |               |     | (EchOutEPInt)                   |      |
	|      |               |     |                                 |      |
	|      |               |     | One bit per OUT endpoint:       |      |
	|      |               |     |                                 |      |
	|      |               |     | - Bit 16 for OUT endpoint 0     |      |
	|      |               |     | - ...                           |      |
	|      |               |     | - Bit 31 for OUT endpoint 15    |      |
	+------+---------------+-----+---------------------------------+------+

DEACHINTMSK
```````````

Device Each Endpoint Interrupt Register Mask

.. _table_usb_deachintmsk:
.. table:: DEACHINTMSK, Offset Address: 0x83c
	:widths: 1 2 1 4 1

	+------+---------------+-----+---------------------------------+------+
	| Bits | Name          | Acc\| Description                     | R\   |
	|      |               | ess |                                 | eset |
	+======+===============+=====+=================================+======+
	| 15:0 | EchInEpMsk    | R/W | IN EP Interrupt Mask Bits       | 0x0  |
	|      |               |     |                                 |      |
	|      |               |     | (EchInEpMsk)                    |      |
	|      |               |     |                                 |      |
	|      |               |     | One bit per IN Endpoint:        |      |
	|      |               |     |                                 |      |
	|      |               |     | - Bit 0 for IN endpoint 0       |      |
	|      |               |     | - ...                           |      |
	|      |               |     | - Bit 15 for endpoint 15        |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow: Yes                     |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow Ctrl: vs_1t              |      |
	|      |               |     |                                 |      |
	|      |               |     | Shadow Read Select: shrd_sel    |      |
	|      |               |     |                                 |      |
	|      |               |     | One-Way: Enabled                |      |
	+------+---------------+-----+---------------------------------+------+
	| 31:16| EchOutEpMsk   | R/W | OUT EP Interrupt Mask Bits      | 0x0  |
	|      |               |     |                                 |      |
	|      |               |     | (EchOutEpMsk)                   |      |
	|      |               |     |                                 |      |
	|      |               |     | One per OUT Endpoint:           |      |
	|      |               |     |                                 |      |
	|      |               |     | - Bit 16 for IN endpoint 0      |      |
	|      |               |     | - ...                           |      |
	|      |               |     | - Bit 31 for endpoint 15        |      |
	+------+---------------+-----+---------------------------------+------+
