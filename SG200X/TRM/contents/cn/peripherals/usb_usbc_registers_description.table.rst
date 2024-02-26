GOTGCTL
```````

Control and Status Register

.. _table_usb_gotgctl_contd_0:
.. table:: GOTGCTL, Offset Address: 0x000
	:widths: 1 2 1 6 1

	+------+------------+----+-------------------------------------+------+
	| Bits | Name       | Ac\| Description                         | R\   |
	|      |            | ce\|                                     | eset |
	|      |            | ss\|                                     |      |
	+======+============+====+=====================================+======+
	| 0    | SesReqScs  | RO | Mode: Device only                   |      |
	|      |            |    |                                     |      |
	|      |            |    | Session Request Success (SesReqScs) |      |
	|      |            |    |                                     |      |
	|      |            |    | The core sets this bit when a       |      |
	|      |            |    | session request initiation is       |      |
	|      |            |    | successful.                         |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Session request failure     |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Session request success     |      |
	|      |            |    |                                     |      |
	|      |            |    | Shadow: Yes                         |      |
	|      |            |    |                                     |      |
	|      |            |    | Shadow Ctrl: vs_1t                  |      |
	|      |            |    |                                     |      |
	|      |            |    | Shadow Read Select: shrd_sel        |      |
	|      |            |    |                                     |      |
	|      |            |    | One-Way: Enabled                    |      |
	+------+------------+----+-------------------------------------+------+
	| 1    | SesReq     | R\ | Mode: SRP-capable device            | 0x0  |
	|      |            | /W |                                     |      |
	|      |            |    | Session Request (SesReq)            |      |
	|      |            |    |                                     |      |
	|      |            |    | The application sets this bit to    |      |
	|      |            |    | initiate a session request on the   |      |
	|      |            |    | USB. The application can clear this |      |
	|      |            |    | bit by writing a 0 when the Host    |      |
	|      |            |    | Negotiation                         |      |
	|      |            |    |                                     |      |
	|      |            |    | Success Status Change bit in the    |      |
	|      |            |    | OTG Interrupt register              |      |
	|      |            |    | (GOTGINT.HstNegSucStsChng) is SET.  |      |
	|      |            |    | The core clears this bit when the   |      |
	|      |            |    | HstNegSucStsChng bit is cleared.    |      |
	|      |            |    |                                     |      |
	|      |            |    | If you use the USB 1.1 Full-Speed   |      |
	|      |            |    | Serial Transceiver interface to     |      |
	|      |            |    | initiate the session request, the   |      |
	|      |            |    | application must wait until the     |      |
	|      |            |    | VBUS discharges to 0.2 V, after the |      |
	|      |            |    | B-Session Valid bit in this         |      |
	|      |            |    | register (GOTGCTL.BSesVld) is       |      |
	|      |            |    | cleared. This discharge time varies |      |
	|      |            |    | between                             |      |
	|      |            |    | different PHYs and can be obtained  |      |
	|      |            |    | from the PHY vendor.                |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: No session request          |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Session request             |      |
	|      |            |    |                                     |      |
	|      |            |    | Shadow: Yes                         |      |
	|      |            |    |                                     |      |
	|      |            |    | Shadow Ctrl: vs_1t                  |      |
	|      |            |    |                                     |      |
	|      |            |    | Shadow Read Select: shrd_sel        |      |
	+------+------------+----+-------------------------------------+------+
	| 2    | V\         | R\ | Mode: Host only                     | 0x0  |
	|      | bvalidOvEn | /W |                                     |      |
	|      |            |    | VBUS Valid Override Enable          |      |
	|      |            |    | (VbvalidOvEn)                       |      |
	|      |            |    |                                     |      |
	|      |            |    | This bit is used to enable/disable  |      |
	|      |            |    | the software to override the Bvalid |      |
	|      |            |    | signal using the                    |      |
	|      |            |    | GOTGCTL.VbvalidOvVal.               |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Internally Bvalid received  |      |
	|      |            |    |   from the PHY is overridden with   |      |
	|      |            |    |   GOTGCTL.VbvalidOvVal.             |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Override is disabled and    |      |
	|      |            |    |   bvalid signal from the respective |      |
	|      |            |    |   PHY                               |      |
	|      |            |    |                                     |      |
	|      |            |    | selected is used internally by the  |      |
	|      |            |    | core.                               |      |
	|      |            |    |                                     |      |
	|      |            |    | Shadow: Yes                         |      |
	|      |            |    |                                     |      |
	|      |            |    | Shadow Ctrl: vs_1t                  |      |
	|      |            |    |                                     |      |
	|      |            |    | Shadow Read Select: shrd_sel        |      |
	|      |            |    |                                     |      |
	|      |            |    | One-Way: Enabled                    |      |
	+------+------------+----+-------------------------------------+------+

To be continued ......

.. _table_usb_gotgctl_contd_1:
.. table:: GOTGCTL, Offset Address: 0x000 (continued)
	:widths: 1 2 1 4 1

	+------+------------+----+-------------------------------------+------+
	| Bits | Name       | Ac\| Description                         | R\   |
	|      |            | ce\|                                     | eset |
	|      |            | ss\|                                     |      |
	+------+------------+----+-------------------------------------+------+
	| 3    | Vb\        | R\ | Mode: Host only                     | 0x0  |
	|      | validOvVal | /W |                                     |      |
	|      |            |    | VBUS Valid Override Value           |      |
	|      |            |    | (VbvalidOvVal)                      |      |
	|      |            |    |                                     |      |
	|      |            |    | This bit is used to set Override    |      |
	|      |            |    | value for vbusvalid signal when     |      |
	|      |            |    | GOTGCTL.VbvalidOvEn is set.         |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: vbusvalid value is 1'b0     |      |
	|      |            |    |   when GOTGCTL.VbvalidOvEn =1       |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: vbusvalid value is 1'b1     |      |
	|      |            |    |   when GOTGCTL.VbvalidOvEn =1       |      |
	|      |            |    |                                     |      |
	+------+------------+----+-------------------------------------+------+
	| 4    | AvalidOvEn | R\ | Mode: Host only                     | 0x0  |
	|      |            | /W |                                     |      |
	|      |            |    | A-Peripheral Session Valid Override |      |
	|      |            |    | Enable (AvalidOvEn)                 |      |
	|      |            |    | This bit is used to enable/disable  |      |
	|      |            |    | the software to override the Avalid |      |
	|      |            |    | signal using the                    |      |
	|      |            |    | GOTGCTL.AvalidOvVal.                |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Internally Avalid received  |      |
	|      |            |    |   from the PHY is overridden with   |      |
	|      |            |    |   GOTGCTL.AvalidOvVal.              |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Override is disabled and    |      |
	|      |            |    |   avalid signal from the respective |      |
	|      |            |    |   PHY                               |      |
	|      |            |    |                                     |      |
	|      |            |    | selected is used internally by the  |      |
	|      |            |    | core.                               |      |
	+------+------------+----+-------------------------------------+------+
	| 5    | A\         | R\ | Mode: Host only                     | 0x0  |
	|      | validOvVal | /W |                                     |      |
	|      |            |    | A-Peripheral Session Valid Override |      |
	|      |            |    | Value (AvalidOvVal)                 |      |
	|      |            |    |                                     |      |
	|      |            |    | This bit is used to set Override    |      |
	|      |            |    | value for Avalid signal when        |      |
	|      |            |    | GOTGCTL.AvalidOvEn is set.          |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Avalid value is 1'b0 when   |      |
	|      |            |    |   GOTGCTL.AvalidOvEn =1             |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Avalid value is 1'b1 when   |      |
	|      |            |    |   GOTGCTL.AvalidOvEn =1             |      |
	+------+------------+----+-------------------------------------+------+
	| 6    | BvalidOvEn | R\ | Mode: Device only                   | 0x0  |
	|      |            | /W |                                     |      |
	|      |            |    | B-Peripheral Session Valid Override |      |
	|      |            |    | Enable (BvalidOvEn)                 |      |
	|      |            |    |                                     |      |
	|      |            |    | This bit is used to enable/disable  |      |
	|      |            |    | the software to override the Bvalid |      |
	|      |            |    | signal using the                    |      |
	|      |            |    | GOTGCTL.BvalidOvVal.                |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Internally Bvalid receiv  ed|      |
	|      |            |    |   from the PHY is overridden with   |      |
	|      |            |    |   GOTGCTL.BvalidOvVal.              |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Override is disabled and    |      |
	|      |            |    |   bvalid signal from the respective |      |
	|      |            |    |   PHY                               |      |
	|      |            |    |                                     |      |
	|      |            |    | selected is used internally by the  |      |
	|      |            |    | force                               |      |
	+------+------------+----+-------------------------------------+------+


To be continued ......

.. _table_usb_gotgctl_contd_2:
.. table:: GOTGCTL, Offset Address: 0x000 (continued)
	:widths: 1 2 1 4 1

	+------+------------+----+-------------------------------------+------+
	| Bits | Name       | Ac\| Description                         | R\   |
	|      |            | ce\|                                     | eset |
	|      |            | ss\|                                     |      |
	+------+------------+----+-------------------------------------+------+
	| 7    | B\         | R\ | Mode: Device only                   | 0x0  |
	|      | validOvVal | /W |                                     |      |
	|      |            |    | B-Peripheral Session Valid Override |      |
	|      |            |    | Value (BvalidOvVal)                 |      |
	|      |            |    |                                     |      |
	|      |            |    | This bit is used to set Override    |      |
	|      |            |    | value for Bvalid signal when        |      |
	|      |            |    | GOTGCTL.BvalidOvEn is set.          |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Bvalid value is 1'b0 when   |      |
	|      |            |    |   GOTGCTL.BvalidOvEn =1             |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Bvalid value is 1'b1 when   |      |
	|      |            |    |   GOTGCTL.BvalidOvEn =1             |      |
	+------+------------+----+-------------------------------------+------+
	| 8    | HstNegScs  | RO | Mode: HNP-capable device            |      |
	|      |            |    |                                     |      |
	|      |            |    | Host Negotiation Success            |      |
	|      |            |    | (HstNegScs)                         |      |
	|      |            |    |                                     |      |
	|      |            |    | The core sets this bit when host    |      |
	|      |            |    | negotiation is successful. The core |      |
	|      |            |    | clears this bit when the HNP        |      |
	|      |            |    | Request (HNPReq) bit in this        |      |
	|      |            |    | register is                         |      |
	|      |            |    | set.                                |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Host negotiation failure    |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Host negotiation success    |      |
	+------+------------+----+-------------------------------------+------+
	| 9    | HNPReq     | R\ | Mode: HNP Capable OTG Device        | 0x0  |
	|      |            | /W |                                     |      |
	|      |            |    | HNP Request (HNPReq)                |      |
	|      |            |    |                                     |      |
	|      |            |    | The application sets this bit to    |      |
	|      |            |    | initiate an HNP request to the      |      |
	|      |            |    | connected                           |      |
	|      |            |    | USB host. The application can clear |      |
	|      |            |    | this bit by writing a 0 when the    |      |
	|      |            |    | Host                                |      |
	|      |            |    | Negotiation Success Status Change   |      |
	|      |            |    | bit in the OTG Interrupt register   |      |
	|      |            |    | (GOTGINT.HstNegSucStsChng) is set.  |      |
	|      |            |    | The core clears this bit when the   |      |
	|      |            |    | HstNegSucStsChng bit is cleared.    |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: No HNP request              |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: HNP request                 |      |
	+------+------------+----+-------------------------------------+------+
	| 10   | H\         | R\ | Mode: HNP Capable OTG Host          | 0x0  |
	|      | stSetHNPEn | /W |                                     |      |
	|      |            |    | Host Set HNP Enable (HstSetHNPEn)   |      |
	|      |            |    |                                     |      |
	|      |            |    | The application sets this bit when  |      |
	|      |            |    | it has successfully enabled HNP     |      |
	|      |            |    | (using the SetFeature.SetHNPEnable  |      |
	|      |            |    | command) on the connected           |      |
	|      |            |    | device.                             |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Host Set HNP is not enab led|      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Host Set HNP is enabled     |      |
	+------+------------+----+-------------------------------------+------+


To be continued ......

.. _table_usb_gotgctl_contd_3:
.. table:: GOTGCTL, Offset Address: 0x000 (continued)
	:widths: 1 2 1 4 1

	+------+------------+----+-------------------------------------+------+
	| Bits | Name       | Ac\| Description                         | R\   |
	|      |            | ce\|                                     | eset |
	|      |            | ss\|                                     |      |
	+------+------------+----+-------------------------------------+------+
	| 11   | DevHNPEn   | R\ | Mode: HNP Capable OTG Device        | 0x0  |
	|      |            | /W |                                     |      |
	|      |            |    | Device HNP Enabled (DevHNPEn)       |      |
	|      |            |    |                                     |      |
	|      |            |    | The application sets this bit when  |      |
	|      |            |    | it successfully receives            |      |
	|      |            |    | aSetFeature.SetHNPEnable command    |      |
	|      |            |    | from the connected USB host.        |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: HNP is not enabled in the   |      |
	|      |            |    |   application                       |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: HNP is enabled in the       |      |
	|      |            |    |   application                       |      |
	+------+------------+----+-------------------------------------+------+
	| 12   | EHEn       | R\ | Embedded Host Enable                | 0x0  |
	|      |            | /W |                                     |      |
	|      |            |    | It is used to select between OTG A  |      |
	|      |            |    | Device state Machine andEmbedded    |      |
	|      |            |    | Host state machine.                 |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Embedded Host State Mach ine|      |
	|      |            |    |   is selected                       |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: OTG A Device state machi  ne|      |
	|      |            |    |   is selected                       |      |
	|      |            |    |                                     |      |
	|      |            |    | Note: This field is valid only in   |      |
	|      |            |    | SRP-Capable OTG Mode (OTG_MODE=0,1) |      |
	+------+------------+----+-------------------------------------+------+
	| 14:13| Reserve\   | RO | Reserved for future use.            |      |
	|      | d_00_14_13 |    |                                     |      |
	+------+------------+----+-------------------------------------+------+
	| 15   | Dbnce\     | R\ | Mode: Host and Device               | 0x0  |
	|      | FltrBypass | /W |                                     |      |
	|      |            |    | Debounce Filter Bypass              |      |
	|      |            |    |                                     |      |
	|      |            |    | Bypass Debounce filters for avalid, |      |
	|      |            |    | bvalid, vbusvalid, sessend, and     |      |
	|      |            |    | iddig                               |      |
	|      |            |    |                                     |      |
	|      |            |    | signals when enabled.               |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Disabled                    |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Enabled                     |      |
	+------+------------+----+-------------------------------------+------+
	| 16   | ConIDSts   | RO | Mode: Host and Device               |      |
	|      |            |    |                                     |      |
	|      |            |    | Connector ID Status (ConIDSts)      |      |
	|      |            |    |                                     |      |
	|      |            |    | Indicates the connector ID status   |      |
	|      |            |    | on a connect event.                 |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: The DWC_otg core is in      |      |
	|      |            |    |   A-Device mode                     |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: The DWC_otg core is in      |      |
	|      |            |    |   B-Device mode                     |      |
	+------+------------+----+-------------------------------------+------+
	| 17   | DbncTime   | RO | Mode: Host only                     |      |
	|      |            |    |                                     |      |
	|      |            |    | Long/Short Debounce Time (DbncTime) |      |
	|      |            |    |                                     |      |
	|      |            |    | Indicates the debounce time of a    |      |
	|      |            |    | detected connection.                |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Long debounce time, used    |      |
	|      |            |    |   for physical connections (100 ms +|      |
	|      |            |    |   2.5 us)                           |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: Short debounce time, use  d |      |
	|      |            |    |   for soft connections (2.5 us)     |      |
	+------+------------+----+-------------------------------------+------+


To be continued ......

.. _table_usb_gotgctl_contd_4:
.. table:: GOTGCTL, Offset Address: 0x000 (continued)
	:widths: 1 2 1 4 1

	+------+------------+----+-------------------------------------+------+
	| Bits | Name       | Ac\| Description                         | R\   |
	|      |            | ce\|                                     | eset |
	|      |            | ss\|                                     |      |
	+------+------------+----+-------------------------------------+------+
	| 18   | ASesVld    | RO | Mode: Host only                     |      |
	|      |            |    |                                     |      |
	|      |            |    | A-Session Valid (ASesVld)           |      |
	|      |            |    |                                     |      |
	|      |            |    | Indicates the Host mode transceiver |      |
	|      |            |    | status.                             |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: A-session is not valid      |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: A-session is valid          |      |
	+------+------------+----+-------------------------------------+------+
	| 19   | BSesVld    | RO | Mode: Device only                   |      |
	|      |            |    |                                     |      |
	|      |            |    | B-Session Valid (BSesVld)           |      |
	|      |            |    |                                     |      |
	|      |            |    | Indicates the Device mode           |      |
	|      |            |    | transceiver status.                 |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: B-session is not valid.     |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: B-session is valid.         |      |
	|      |            |    |                                     |      |
	|      |            |    | In OTG mode, you can use this bit   |      |
	|      |            |    | to determine if the device is       |      |
	|      |            |    | connected or disconnected.          |      |
	+------+------------+----+-------------------------------------+------+
	| 20   | OTGVer     | R\ | OTG Version (OTGVer)                | 0x0  |
	|      |            | /W |                                     |      |
	|      |            |    | Indicates the OTG revision.         |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: OTG Version 1.3. In this    |      |
	|      |            |    |   version the core supports Data    |      |
	|      |            |    |   line pulsing and VBus pulsing for |      |
	|      |            |    |   SRP.                              |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b1: OTG Version 2.0. In this    |      |
	|      |            |    |   version the core supports only    |      |
	|      |            |    |   Data line pulsing for SRP.        |      |
	+------+------------+----+-------------------------------------+------+
	| 21   | CurMod\    | RO | Current Mode of Operation (CurMod)  |      |
	|      | _operation |    |                                     |      |
	|      |            |    | Mode: Host and Device               |      |
	|      |            |    |                                     |      |
	|      |            |    | Indicates the current mode.         |      |
	|      |            |    |                                     |      |
	|      |            |    | - 1'b0: Device mode                 |      |
	|      |            |    | - 1'b1: Host mode                   |      |
	+------+------------+----+-------------------------------------+------+
	| 26:22| M\         | RO | Multi Valued ID pin (MultValIdBC)   |      |
	|      | ultValIdBC\|    |                                     |      |
	|      | _operation |    | Mode: Host and Device               |      |
	|      |            |    |                                     |      |
	|      |            |    | Battery Charger ACA inputs in the   |      |
	|      |            |    | following order:                    |      |
	|      |            |    |                                     |      |
	|      |            |    | - Bit 26 - rid_float                |      |
	|      |            |    | - Bit 25 - rid_gnd                  |      |
	|      |            |    | - Bit 24 - rid_a                    |      |
	|      |            |    | - Bit 23 - rid_b                    |      |
	|      |            |    | - Bit 22 - rid_c                    |      |
	+------+------------+----+-------------------------------------+------+
	| 27   | ChirpEn    | RO | Chirp On Enable (ChirpEn)           |      |
	|      |            |    |                                     |      |
	|      |            |    | Mode: Device Only                   |      |
	|      |            |    |                                     |      |
	|      |            |    | This bit when programmed to 1'b1    |      |
	|      |            |    | results in the core asserting       |      |
	|      |            |    | chirp_on                            |      |
	|      |            |    | before sending an actual Chirp "K"  |      |
	|      |            |    | signal on USB. This bit is present  |      |
	|      |            |    | only if OTG_BC_SUPPORT = 1. If      |      |
	|      |            |    | OTG_BC_SUPPORT!=1, this bit is a    |      |
	|      |            |    | reserved bit.                       |      |
	+------+------------+----+-------------------------------------+------+
	| 31:28| Reserve\   | RO | Reserved for future use.            |      |
	|      | d_00_31_28 |    |                                     |      |
	+------+------------+----+-------------------------------------+------+

GOTGINT
```````

Interrupt Register

.. _table_usb_gotgint_contd_0:
.. table:: GOTGINT, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+---------------+-------+--------------------------------+------+
	| Bits | Name          | Access| Description                    | Reset|
	+======+===============+=======+================================+======+
	| 1:0  | Re\           | RO    | Reserved for future use.       |      |
	|      | served_04_1_0 |       |                                |      |
	|      |               |       | Shadow: Yes                    |      |
	|      |               |       |                                |      |
	|      |               |       | Shadow Ctrl: vs_1t             |      |
	|      |               |       |                                |      |
	|      |               |       | Shadow Read Select: shrd_sel   |      |
	+------+---------------+-------+--------------------------------+------+
	| 2    | SesEndDet     | RWC   | Write Behavior: One to clear   |      |
	|      |               |       |                                |      |
	|      |               |       | Mode: Host and Device          |      |
	|      |               |       |                                |      |
	|      |               |       | Session End Detected           |      |
	|      |               |       | (SesEndDet)                    |      |
	|      |               |       |                                |      |
	|      |               |       | The core sets this bit when    |      |
	|      |               |       | the utmiotg_bvalid signal is   |      |
	|      |               |       | deasserted.This bit can be set |      |
	|      |               |       | only by the core and the       |      |
	|      |               |       | application                    |      |
	|      |               |       | should write 1 to clear it.    |      |
	+------+---------------+-------+--------------------------------+------+
	| 7:3  | Re\           | RO    | Reserved for future use.       |      |
	|      | served_04_7_3 |       |                                |      |
	+------+---------------+-------+--------------------------------+------+
	| 8    | Ses\          | RWC   | Write Behavior: One to clear   |      |
	|      | ReqSucStsChng |       |                                |      |
	|      |               |       | Mode: Host and Device          |      |
	|      |               |       |                                |      |
	|      |               |       | Session Request Success Status |      |
	|      |               |       | Change (SesReqSucStsChng)      |      |
	|      |               |       |                                |      |
	|      |               |       | The core sets this bit on the  |      |
	|      |               |       | success or failure of a        |      |
	|      |               |       | session request.               |      |
	|      |               |       |                                |      |
	|      |               |       | The application must read the  |      |
	|      |               |       | Session Request Success bit in |      |
	|      |               |       | the                            |      |
	|      |               |       | OTG Control and Status         |      |
	|      |               |       | register (GOTGCTL.SesReqScs)   |      |
	|      |               |       | to check                       |      |
	|      |               |       | for success or failure.This    |      |
	|      |               |       | bit can be set only by the     |      |
	|      |               |       | core and the                   |      |
	|      |               |       | application should write 1 to  |      |
	|      |               |       | clear it.                      |      |
	+------+---------------+-------+--------------------------------+------+
	| 9    | Hst\          | RWC   | Write Behavior: One to clear   |      |
	|      | NegSucStsChng |       |                                |      |
	|      |               |       | Mode: Host and Device          |      |
	|      |               |       |                                |      |
	|      |               |       | Host Negotiation Success       |      |
	|      |               |       | Status Change                  |      |
	|      |               |       | (HstNegSucStsChng)             |      |
	|      |               |       |                                |      |
	|      |               |       | The core sets this bit on the  |      |
	|      |               |       | success or failure of a USB    |      |
	|      |               |       | host                           |      |
	|      |               |       | negotiation request. The       |      |
	|      |               |       | application must read the Host |      |
	|      |               |       | Negotiation                    |      |
	|      |               |       | Success bit of the OTG Control |      |
	|      |               |       | and Status register            |      |
	|      |               |       | (GOTGCTL.HstNegScs) to check   |      |
	|      |               |       | for success or failure.This    |      |
	|      |               |       | bit can                        |      |
	|      |               |       | be set only by the core and    |      |
	|      |               |       | the application should write 1 |      |
	|      |               |       | to clear it.                   |      |
	+------+---------------+-------+--------------------------------+------+
	| 16:10| Rese\         | RO    | Reserved for future use.       |      |
	|      | rved_04_16_10 |       |                                |      |
	+------+---------------+-------+--------------------------------+------+



To be continued ......

.. _table_usb_gotgint_contd_1:
.. table:: GOTGINT, Offset Address: 0x004 (continued)
	:widths: 1 2 1 4 1

	+------+---------------+-------+--------------------------------+------+
	| Bits | Name          | Access| Description                    | Reset|
	+======+===============+=======+================================+======+
	| 17   | HstNegDet     | RWC   | Write Behavior: One to clear   |      |
	|      |               |       |                                |      |
	|      |               |       | Mode: Host and Device          |      |
	|      |               |       |                                |      |
	|      |               |       | Host Negotiation Detected      |      |
	|      |               |       | (HstNegDet)                    |      |
	|      |               |       |                                |      |
	|      |               |       | The core sets this bit when it |      |
	|      |               |       | detects a host negotiation     |      |
	|      |               |       | request on                     |      |
	|      |               |       | the USB.This bit can be set    |      |
	|      |               |       | only by the core and the       |      |
	|      |               |       | application                    |      |
	|      |               |       | should write 1 to clear it.    |      |
	+------+---------------+-------+--------------------------------+------+
	| 18   | ADevTOUTChg   | RWC   | Write Behavior: One to clear   |      |
	|      |               |       |                                |      |
	|      |               |       | Mode: Host and Device          |      |
	|      |               |       |                                |      |
	|      |               |       | A-Device Timeout Change        |      |
	|      |               |       | (ADevTOUTChg)                  |      |
	|      |               |       |                                |      |
	|      |               |       | The core sets this bit to      |      |
	|      |               |       | indicate that the A-device has |      |
	|      |               |       | timed out                      |      |
	|      |               |       | while waiting for the B-device |      |
	|      |               |       | to connect.This bit can be set |      |
	|      |               |       | only by                        |      |
	|      |               |       | the core and the application   |      |
	|      |               |       | should write 1 to clear it.    |      |
	+------+---------------+-------+--------------------------------+------+
	| 19   | DbnceDone     | RWC   | Write Behavior: One to clear   |      |
	|      |               |       |                                |      |
	|      |               |       | Mode: Host only                |      |
	|      |               |       |                                |      |
	|      |               |       | Debounce Done (DbnceDone)      |      |
	|      |               |       | The core sets this bit when    |      |
	|      |               |       | the debounce is completed      |      |
	|      |               |       | after the                      |      |
	|      |               |       | device connect. The            |      |
	|      |               |       | application can start driving  |      |
	|      |               |       | USB reset after                |      |
	|      |               |       | seeing this interrupt. This    |      |
	|      |               |       | bit is only valid when the HNP |      |
	|      |               |       | Capable or                     |      |
	|      |               |       | SRP Capable bit is set in the  |      |
	|      |               |       | Core USB Configuration         |      |
	|      |               |       | register                       |      |
	|      |               |       | (GUSBCFG.HNPCap or             |      |
	|      |               |       | GUSBCFG.SRPCap,                |      |
	|      |               |       | respectively).This bit         |      |
	|      |               |       | can be set only by the core    |      |
	|      |               |       | and the application should     |      |
	|      |               |       | write 1 to                     |      |
	|      |               |       | clear it.                      |      |
	+------+---------------+-------+--------------------------------+------+
	| 20   | MultValIpChng | RWC   | Write Behavior: One to clear   |      |
	|      |               |       |                                |      |
	|      |               |       | This bit when set indicates    |      |
	|      |               |       | that there is a change in the  |      |
	|      |               |       | value of at                    |      |
	|      |               |       | least one ACA pin value.       |      |
	|      |               |       | This bit is present only if    |      |
	|      |               |       | OTG_BC_SUPPORT=1, otherwise it |      |
	|      |               |       | is                             |      |
	|      |               |       | reserved.                      |      |
	+------+---------------+-------+--------------------------------+------+
	| 31:21| Rese\         | RO    | Reserved for future use.       |      |
	|      | rved_04_31_21 |       |                                |      |
	|      |               |       | Shadow: Yes                    |      |
	|      |               |       |                                |      |
	|      |               |       | Shadow Ctrl: vs_1t             |      |
	|      |               |       |                                |      |
	|      |               |       | Shadow Read Select: shrd_sel   |      |
	+------+---------------+-------+--------------------------------+------+

GAHBCFG
```````

AHB Configuration Register

.. _table_usb_gahbcfg_contd_0:
.. table:: GAHBCFG, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Ac\ | Description                         | R\   |
	|      |           | ce\ |                                     | eset |
	|      |           | ss\ |                                     |      |
	+======+===========+=====+=====================================+======+
	| 0    | Gl\       | R/W | Mode: Host and device               | 0x0  |
	|      | blIntrMsk |     |                                     |      |
	|      |           |     | Global Interrupt Mask (GlblIntrMsk) |      |
	|      |           |     |                                     |      |
	|      |           |     | The application uses this bit to    |      |
	|      |           |     | mask or unmask the interrupt line   |      |
	|      |           |     | assertion                           |      |
	|      |           |     | to itself. Irrespective of this     |      |
	|      |           |     | bit's setting, the interrupt status |      |
	|      |           |     | registers are                       |      |
	|      |           |     | updated by the core.                |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Mask the interrupt          |      |
	|      |           |     |   assertion to the application.     |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: Unmask the interrupt        |      |
	|      |           |     |   assertion to the application.     |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 4:1  | HBstLen   | R/W | Mode: Host and device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Burst Length/Type (HBstLen)         |      |
	|      |           |     |                                     |      |
	|      |           |     | This field is used in both External |      |
	|      |           |     | and Internal DMA modes. In External |      |
	|      |           |     | DMA mode, these bits appear on      |      |
	|      |           |     | dma_burst[3:0] ports, which can be  |      |
	|      |           |     | used                                |      |
	|      |           |     | by an external wrapper to interface |      |
	|      |           |     | the External DMA Controller         |      |
	|      |           |     | interface to                        |      |
	|      |           |     | Synopsys DW_ahb_dmac or ARM         |      |
	|      |           |     | PrimeCell.                          |      |
	|      |           |     |                                     |      |
	|      |           |     | External DMA Mode defines the DMA   |      |
	|      |           |     | burst length in terms of 32-bit     |      |
	|      |           |     | words:                              |      |
	|      |           |     |                                     |      |
	|      |           |     | - 4'b0000: 1 word                   |      |
	|      |           |     | - 4'b0001: 4 words                  |      |
	|      |           |     | - 4'b0010: 8 words                  |      |
	|      |           |     | - 4'b0011: 16 words                 |      |
	|      |           |     | - 4'b0100: 32 words                 |      |
	|      |           |     | - 4'b0101: 64 words                 |      |
	|      |           |     | - 4'b0110: 128 words                |      |
	|      |           |     | - 4'b0111: 256 words                |      |
	|      |           |     | - Others: Reserved                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Internal DMA Mode-AHB Master burst  |      |
	|      |           |     | type:                               |      |
	|      |           |     |                                     |      |
	|      |           |     | - 4'b0000 Single                    |      |
	|      |           |     | - 4'b0001 INCR 4'b0011              |      |
	|      |           |     | - INCR4 4'b0101                     |      |
	|      |           |     | - INCR8 4'b0111                     |      |
	|      |           |     | - INCR16                            |      |
	|      |           |     | - Others: Reserved                  |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_gahbcfg_contd_1:
.. table:: GAHBCFG, Offset Address: 0x008 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Ac\ | Description                         | R\   |
	|      |           | ce\ |                                     | eset |
	|      |           | ss\ |                                     |      |
	+======+===========+=====+=====================================+======+
	| 5    | DMAEn     | R/W | Mode: Host and device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | DMA Enable (DMAEn)                  |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Core operates in Slave mode |      |
	|      |           |     | - 1'b1: Core operates in a DMA mode |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is always 0 when           |      |
	|      |           |     | Slave-Only mode has been selected.  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 6    | Rese\     | RO  | Reserved for future use.            |      |
	|      | rved_08_6 |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 7    | NP\       | R/W | Mode: Host and device               | 0x0  |
	|      | TxFEmpLvl |     |                                     |      |
	|      |           |     | Non-Periodic TxFIFO Empty Level     |      |
	|      |           |     | (NPTxFEmpLvl)                       |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is used only in Slave      |      |
	|      |           |     | mode. In host mode and with Shared  |      |
	|      |           |     | FIFO                                |      |
	|      |           |     | with device mode, this bit          |      |
	|      |           |     | indicates when the Non-Periodic     |      |
	|      |           |     | TxFIFO Empty                        |      |
	|      |           |     | Interrupt bit in the Core Interrupt |      |
	|      |           |     | register (GINTSTS.NPTxFEmp) is      |      |
	|      |           |     | triggered.                          |      |
	|      |           |     |                                     |      |
	|      |           |     | With dedicated FIFO in device mode, |      |
	|      |           |     | this bit indicates when IN endpoint |      |
	|      |           |     | Transmit FIFO empty interrupt       |      |
	|      |           |     | (DIEPINTn.TxFEmp) is triggered.     |      |
	|      |           |     | Host mode and with Shared FIFO with |      |
	|      |           |     | device mode:                        |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: GINTSTS.NPTxFEmp interrupt  |      |
	|      |           |     |   indicates that the Non- Periodic  |      |
	|      |           |     |   TxFIFO is half empty              |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: GINTSTS.NPTxFEmp interrupt  |      |
	|      |           |     |   indicates that the Non- Periodic  |      |
	|      |           |     |   TxFIFO is completely empty        |      |
	|      |           |     |   Dedicated FIFO in device mode:    |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: DIEPINTn.TxFEmp interrupt   |      |
	|      |           |     |   indicates that the IN Endpoint    |      |
	|      |           |     |   TxFIFO is half empty              |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: DIEPINTn.TxFEmp interrupt   |      |
	|      |           |     |   indicates that the IN Endpoint    |      |
	|      |           |     |   TxFIFO is completely empty        |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_gahbcfg_contd_2:
.. table:: GAHBCFG, Offset Address: 0x008 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Ac\ | Description                         | R\   |
	|      |           | ce\ |                                     | eset |
	|      |           | ss\ |                                     |      |
	+======+===========+=====+=====================================+======+
	| 8    | P\        | R/W | Mode: Host only                     | 0x0  |
	|      | TxFEmpLvl |     |                                     |      |
	|      |           |     | Periodic TxFIFO Empty Level         |      |
	|      |           |     |                                     |      |
	|      |           |     | (PTxFEmpLvl)                        |      |
	|      |           |     | Indicates when the Periodic TxFIFO  |      |
	|      |           |     | Empty Interrupt bit in the Core     |      |
	|      |           |     | Interrupt register                  |      |
	|      |           |     | (GINTSTS.PTxFEmp) is triggered.     |      |
	|      |           |     | This bit is used only in            |      |
	|      |           |     | Slave mode.                         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: GINTSTS.PTxFEmp interrupt   |      |
	|      |           |     |   indicates that the Periodic       |      |
	|      |           |     |   TxFIFO is half empty              |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: GINTSTS.PTxFEmp interrupt   |      |
	|      |           |     |   indicates that the Periodic       |      |
	|      |           |     |   TxFIFO is completely empty        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 20:9 | Reserve\  | RO  | Reserved for future use.            |      |
	|      | d_08_20_9 |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 21   | R\        | R/W | Mode: Host and Device               | 0x0  |
	|      | emMemSupp |     |                                     |      |
	|      |           |     | Remote Memory Support (RemMemSupp)  |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is programmed to enable    |      |
	|      |           |     | the functionality to wait for the   |      |
	|      |           |     | system                              |      |
	|      |           |     | DMA Done Signal for the DMA Write   |      |
	|      |           |     | Transfers.                          |      |
	|      |           |     |                                     |      |
	|      |           |     | - GAHBCFG.RemMemSupp=1              |      |
	|      |           |     |                                     |      |
	|      |           |     |   The int_dma_req output signal is  |      |
	|      |           |     |   asserted when HSOTG DMA starts    |      |
	|      |           |     |   write transfer to the external    |      |
	|      |           |     |   memory. When the core is done with|      |
	|      |           |     |   the                               |      |
	|      |           |     |   Transfers it asserts int_dma_done |      |
	|      |           |     |   signal to flag the completion of  |      |
	|      |           |     |   DMA                               |      |
	|      |           |     |   writes from HSOTG. The core then  |      |
	|      |           |     |   waits for sys_dma_done signal from|      |
	|      |           |     |   the system to proceed further and |      |
	|      |           |     |   complete the Data Transfer        |      |
	|      |           |     |   corresponding to a particular     |      |
	|      |           |     |   Channel/Endpoint.                 |      |
	|      |           |     |                                     |      |
	|      |           |     | - GAHBCFG.RemMemSupp=0              |      |
	|      |           |     |                                     |      |
	|      |           |     |   The int_dma_req and int_dma_done  |      |
	|      |           |     |   signals are not asserted and the  |      |
	|      |           |     |   core proceeds with the assertion  |      |
	|      |           |     |   of                                |      |
	|      |           |     |   the XferComp interrupt as soon as |      |
	|      |           |     |   the DMA write transfer is done at |      |
	|      |           |     |   the HSOTG Core Boundary and it    |      |
	|      |           |     |   doesn't wait for the sys_dma_done |      |
	|      |           |     |   signal to complete the DATA       |      |
	|      |           |     |   transfers.                        |      |
	+------+-----------+-----+-------------------------------------+------+



To be continued ......

.. _table_usb_gahbcfg_contd_3:
.. table:: GAHBCFG, Offset Address: 0x008 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Ac\ | Description                         | R\   |
	|      |           | ce\ |                                     | eset |
	|      |           | ss\ |                                     |      |
	+======+===========+=====+=====================================+======+
	| 22   | NotiA\    | R/W | Mode: Host and Device               | 0x0  |
	|      | llDmaWrit |     |                                     |      |
	|      |           |     | Notify all DMA Write Transactions   |      |
	|      |           |     | (NotiAllDmaWrit)                    |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is programmed to enable    |      |
	|      |           |     | the System DMA Done functionality   |      |
	|      |           |     | for all                             |      |
	|      |           |     | the DMA write Transactions          |      |
	|      |           |     | corresponding to the                |      |
	|      |           |     | Channel/Endpoint. This              |      |
	|      |           |     | bit is valid only when              |      |
	|      |           |     | GAHBCFG.RemMemSupp is set to 1.     |      |
	|      |           |     |                                     |      |
	|      |           |     | - GAHBCFG.NotiAllDmaWrit = 1        |      |
	|      |           |     |                                     |      |
	|      |           |     |   DWC_otg core asserts int_dma_req  |      |
	|      |           |     |   for all the DMA write transactions|      |
	|      |           |     |   on the AHB interface along with   |      |
	|      |           |     |   int_dma_done, chep_last_transact  |      |
	|      |           |     |   and                               |      |
	|      |           |     |   chep_number signal informations.  |      |
	|      |           |     |   The core waits for sys_dma_done   |      |
	|      |           |     |   signal for all the DMA write      |      |
	|      |           |     |   transactions in order to complete |      |
	|      |           |     |   the                               |      |
	|      |           |     |   transfer of a particular          |      |
	|      |           |     |   Channel/Endpoint.                 |      |
	|      |           |     |                                     |      |
	|      |           |     | - GAHBCFG.NotiAllDmaWrit = 0        |      |
	|      |           |     |                                     |      |
	|      |           |     |   DWC_otg core asserts int_dma_req  |      |
	|      |           |     |   signal only for the last          |      |
	|      |           |     |   transaction                       |      |
	|      |           |     |   of DMA write transfer             |      |
	|      |           |     |   corresponding                     |      |
	|      |           |     |   to a particular Channel/Endpoint. |      |
	|      |           |     |   Similarly, the core waits for     |      |
	|      |           |     |   sys_dma_done signal only for that |      |
	|      |           |     |   transaction of DMA write to       |      |
	|      |           |     |   complete the transfer of a        |      |
	|      |           |     |   particular                        |      |
	|      |           |     |   Channel/Endpoint.                 |      |
	+------+-----------+-----+-------------------------------------+------+
	| 23   | AHBSingle | R/W | Mode: Host and Device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | AHBSingleSupport (AHBSingle)        |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit when programmed supports   |      |
	|      |           |     | Single transfers for the remaining  |      |
	|      |           |     | data                                |      |
	|      |           |     | in a transfer when the DWC_otg core |      |
	|      |           |     | is operating in DMA mode.           |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: This is the default mode  . |      |
	|      |           |     |   When this bit is set to 1'b0, the |      |
	|      |           |     |   remaining                         |      |
	|      |           |     |   data in the transfer is sent      |      |
	|      |           |     |   using                             |      |
	|      |           |     |   INCR burst size.                  |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: When set to 1'b1, the       |      |
	|      |           |     |   remaining data in a transfer is   |      |
	|      |           |     |   sent using Single burst size.     |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: If this feature is enabled,   |      |
	|      |           |     | the AHB RETRY and SPLIT transfers   |      |
	|      |           |     | still                               |      |
	|      |           |     | have INCR burst type. Enable this   |      |
	|      |           |     | feature when the AHB Slave          |      |
	|      |           |     | connected                           |      |
	|      |           |     | to the DWC_otg core does not        |      |
	|      |           |     | support INCR burst (and when Split, |      |
	|      |           |     | and                                 |      |
	|      |           |     | Retry transactions are not being    |      |
	|      |           |     | used in the bus.)                   |      |
	+------+-----------+-----+-------------------------------------+------+


To be continued ......

.. _table_usb_gahbcfg_contd_4:
.. table:: GAHBCFG, Offset Address: 0x008 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Ac\ | Description                         | R\   |
	|      |           | ce\ |                                     | eset |
	|      |           | ss\ |                                     |      |
	+======+===========+=====+=====================================+======+
	| 24   | InvDescE\ | R/W | Mode: Host and Device               | 0x0  |
	|      | ndianness |     |                                     |      |
	|      |           |     | Inverse Descriptor Endianness       |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Descriptor endianness is    |      |
	|      |           |     |   similar to the AHB Master         |      |
	|      |           |     |   endianness                        |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1:                             |      |
	|      |           |     |                                     |      |
	|      |           |     |   - If the AHB Master endianness is |      |
	|      |           |     |     Big Endian, the Descriptor      |      |
	|      |           |     |     Endianness is Little Endian.    |      |
	|      |           |     |                                     |      |
	|      |           |     |   - If the AHB Master endianness is |      |
	|      |           |     |     Little Endian, the Descriptor   |      |
	|      |           |     |     Endianness is Big Endian.       |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31:25| Reserved\ | RO  | Reserved for future use.            |      |
	|      | _08_31_25 |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+

GUSBCFG
```````
USB Configuration Register

.. _table_usb_gusbcfg_contd_0:
.. table:: GUSBCFG, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 2:0  | TOutCal  | R/W | Mode: Host and Device                | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | HS/FS Timeout Calibration (TOutCal)  |      |
	|      |          |     | The number of PHY clocks that the    |      |
	|      |          |     | application programs in this field   |      |
	|      |          |     | is added to the                      |      |
	|      |          |     | high-speed/full-speed interpacket    |      |
	|      |          |     | timeout duration in                  |      |
	|      |          |     | the core to account for any          |      |
	|      |          |     | additional delays introduced by the  |      |
	|      |          |     | PHY.                                 |      |
	|      |          |     |                                      |      |
	|      |          |     | This can be required, because the    |      |
	|      |          |     | delay introduced by the PHY in       |      |
	|      |          |     | generating the linestate condition   |      |
	|      |          |     | can vary from one PHY to another.    |      |
	|      |          |     | The USB standard timeout value for   |      |
	|      |          |     | high-speed operation is 736 to       |      |
	|      |          |     | 816 (inclusive) bit times. The USB   |      |
	|      |          |     | standard timeout value for fullspeed |      |
	|      |          |     | operation is 16 to 18 (inclusive)    |      |
	|      |          |     | bit times. The application           |      |
	|      |          |     | must program this field based on the |      |
	|      |          |     | speed of enumeration. The            |      |
	|      |          |     | number of bit times added per PHY    |      |
	|      |          |     | clock are:                           |      |
	|      |          |     |                                      |      |
	|      |          |     | High-speed operation:                |      |
	|      |          |     |                                      |      |
	|      |          |     | - One 30-MHz PHY clock = 16 bit times|      |
	|      |          |     | - One 60-MHz PHY clock = 8 bit times |      |
	|      |          |     |                                      |      |
	|      |          |     | Full-speed operation:                |      |
	|      |          |     |                                      |      |
	|      |          |     | - One 30-MHz PHY clock = 0.4 bit     |      |
	|      |          |     |   times                              |      |
	|      |          |     | - One 60-MHz PHY clock = 0.2 bit     |      |
	|      |          |     |   times                              |      |
	|      |          |     | - One 48-MHz PHY clock = 0.25 bit    |      |
	|      |          |     |   times                              |      |
	|      |          |     |                                      |      |
	|      |          |     | Using the HS as an example, if you   |      |
	|      |          |     | set ToutCal to '001' you add one     |      |
	|      |          |     | 30MHz PHY clock or 16 bit times. If  |      |
	|      |          |     | you set ToutCal to '010' you add     |      |
	|      |          |     | two 30MHz PHY clocks or 32 bit       |      |
	|      |          |     | times, and so on. The 3 bits allow   |      |
	|      |          |     | you to add up to 7 PHY clocks, and   |      |
	|      |          |     | the number of bit times depend       |      |
	|      |          |     | on the speed, and the PHY clock you  |      |
	|      |          |     | are using.                           |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	|      |          |     |                                      |      |
	|      |          |     | One-Way: Enabled                     |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_gusbcfg_contd_1:
.. table:: GUSBCFG, Offset Address: 0x00c (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 3    | PHYIf    | RO  | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | PHY Interface (PHYIf)                |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | configure the core to support a      |      |
	|      |          |     | UTMI+ PHY with an 8- or 16-bit       |      |
	|      |          |     | interface. When a ULPI PHY is        |      |
	|      |          |     | chosen, this must be set to 8-bit    |      |
	|      |          |     | mode.                                |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: 8 bits                       |      |
	|      |          |     | - 1'b1: 16 bits                      |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is writable only If UTMI+   |      |
	|      |          |     | and ULPI were selected.              |      |
	|      |          |     |                                      |      |
	|      |          |     | Otherwise, this bit returns the      |      |
	|      |          |     | value for the power-on interface     |      |
	|      |          |     | selected during configuration.       |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	+------+----------+-----+--------------------------------------+------+
	| 4    | ULPI_U\  | R/W | Mode: Host and Device                | 0x0  |
	|      | TMI_Sel  |     |                                      |      |
	|      |          |     | ULPI or UTMI+ Select (ULPI_UTMI_Sel) |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | select either a UTMI+ interface or   |      |
	|      |          |     | ULPI Interface.                      |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: UTMI+ Interface              |      |
	|      |          |     | - 1'b1: ULPI Interface               |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is writable only If UTMI+   |      |
	|      |          |     | and ULPI was specified for High-     |      |
	|      |          |     | Speed PHY Interface(s).              |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	|      |          |     |                                      |      |
	|      |          |     | One-Way: Enabled                     |      |
	+------+----------+-----+--------------------------------------+------+
	| 5    | FSIntf   | R/W | Mode: Host and Device                | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | Full-Speed Serial Interface Select   |      |
	|      |          |     | (FSIntf)                             |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | select either a unidirectional or    |      |
	|      |          |     | bidirectional USB 1.1 full-speed     |      |
	|      |          |     | serial transceiver interface.        |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: 6-pin unidirectional         |      |
	|      |          |     |   full-speed serial interface        |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: 3-pin bidirectional          |      |
	|      |          |     |   full-speed serial interface        |      |
	|      |          |     |                                      |      |
	|      |          |     | If a USB 1.1 Full-Speed Serial       |      |
	|      |          |     | Transceiver interface was not        |      |
	|      |          |     | selected, this bit is always 0, with |      |
	|      |          |     | Read Only access.                    |      |
	|      |          |     |                                      |      |
	|      |          |     | If a USB 1.1 FS interface was        |      |
	|      |          |     | selected, then the application can   |      |
	|      |          |     | set                                  |      |
	|      |          |     | this bit to select between the 3-    |      |
	|      |          |     | and 6-pin interfaces, and access is  |      |
	|      |          |     | Read and Write.                      |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_gusbcfg_contd_2:
.. table:: GUSBCFG, Offset Address: 0x00c (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 6    | PHYSel   | R/W | Mode: Host and Device                | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | USB 2.0 High-Speed PHY or USB 1.1    |      |
	|      |          |     | Full-Speed Serial Transceiver        |      |
	|      |          |     | Select (PHYSel)                      |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | select either a high-speed UTMI+ or  |      |
	|      |          |     | ULPI PHY, or a full-speed            |      |
	|      |          |     | transceiver.                         |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: USB 2.0 high-speed UTMI+   or|      |
	|      |          |     |   ULPI PHY                           |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: USB 1.1 full-speed seria  l  |      |
	|      |          |     |   transceiver                        |      |
	|      |          |     |                                      |      |
	|      |          |     | If a USB 1.1 Full-Speed Serial       |      |
	|      |          |     | Transceiver interface was not        |      |
	|      |          |     | selected, this bit is always 0, with |      |
	|      |          |     | Read Only access.                    |      |
	|      |          |     |                                      |      |
	|      |          |     | If a high-speed PHY interface was    |      |
	|      |          |     | not selected, this bit is always 1,  |      |
	|      |          |     | with Read Only access.               |      |
	|      |          |     |                                      |      |
	|      |          |     | If both interface types were         |      |
	|      |          |     | selected (parameters have non-zero   |      |
	|      |          |     | values), the application uses this   |      |
	|      |          |     | bit to select which interface is     |      |
	|      |          |     | active, and access is Read and       |      |
	|      |          |     | Write.                               |      |
	+------+----------+-----+--------------------------------------+------+
	| 7    | DDRSel   | R/W | Mode: Host and Device                | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | ULPI DDR Select (DDRSel)             |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | select a Single Data Rate (SDR) or   |      |
	|      |          |     | Double Data Rate (DDR) or ULPI       |      |
	|      |          |     | interface.                           |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Single Data Rate ULPI        |      |
	|      |          |     |   Interface, with 8-bit-wide data bus|      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: Double Data Rate ULPI        |      |
	|      |          |     |   Interface, with 4-bit-wide data bus|      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is valid only when          |      |
	|      |          |     | OTG_HSPHY_INTERFACE = 2 or 3.        |      |
	+------+----------+-----+--------------------------------------+------+
	| 8    | SRPCap   | R/W | Mode: Host and Device                | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | SRP-Capable (SRPCap)                 |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | control the DWC_otg core SRP         |      |
	|      |          |     | capabilities. If the core operates   |      |
	|      |          |     | as a non-SRP-capable B-device, it    |      |
	|      |          |     | cannot request the connected         |      |
	|      |          |     | A-device (host) to activate VBUS and |      |
	|      |          |     | start a session.                     |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: SRP capability is not        |      |
	|      |          |     |   enabled.                           |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: SRP capability is enabled.   |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is writable only if an SRP  |      |
	|      |          |     | mode was specified for Mode of       |      |
	|      |          |     | Operation in coreConsultant          |      |
	|      |          |     | (parameter OTG_MODE). Otherwise,     |      |
	|      |          |     | reads return 0.                      |      |
	|      |          |     |                                      |      |
	|      |          |     | If SRP functionality is disabled by  |      |
	|      |          |     | the software, the OTG signals on     |      |
	|      |          |     | the PHY domain must be tied to the   |      |
	|      |          |     | appropriate values.                  |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_gusbcfg_contd_3:
.. table:: GUSBCFG, Offset Address: 0x00c (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 9    | HNPCap   | R/W | Mode: Host and Device                | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | HNP-Capable (HNPCap)                 |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | control the DWC_otg core's HNP       |      |
	|      |          |     | capabilities.                        |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: HNP capability is not        |      |
	|      |          |     |   enabled.                           |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: HNP capability is enabled.   |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is writable only if an HNP  |      |
	|      |          |     | mode was specified for Mode of       |      |
	|      |          |     | Operation in coreConsultant          |      |
	|      |          |     | (parameter OTG_MODE). Otherwise,     |      |
	|      |          |     | reads return 0.                      |      |
	|      |          |     |                                      |      |
	|      |          |     | If HNP functionality is disabled by  |      |
	|      |          |     | the software, the OTG signals on     |      |
	|      |          |     | the PHY domain must be tied to the   |      |
	|      |          |     | appropriate values.                  |      |
	+------+----------+-----+--------------------------------------+------+
	| 13:10| U\       | R/W | Mode: Device only                    | 0x5  |
	|      | SBTrdTim |     |                                      |      |
	|      |          |     | USB Turnaround Time (USBTrdTim)      |      |
	|      |          |     |                                      |      |
	|      |          |     | Sets the turnaround time in PHY      |      |
	|      |          |     | clocks. Specifies the response time  |      |
	|      |          |     | for a MAC request to the Packet FIFO |      |
	|      |          |     | Controller (PFC) to fetch data       |      |
	|      |          |     | from the DFIFO (SPRAM). This must be |      |
	|      |          |     | programmed to                        |      |
	|      |          |     |                                      |      |
	|      |          |     | - 4'h5: When the MAC interface is    |      |
	|      |          |     |   16-bit UTMI+.                      |      |
	|      |          |     |                                      |      |
	|      |          |     | - 4'h9: When the MAC interface is    |      |
	|      |          |     |   8-bit UTMI+.                       |      |
	|      |          |     |                                      |      |
	|      |          |     | Note: The values above are           |      |
	|      |          |     | calculated for the minimum AHB       |      |
	|      |          |     | frequency of 30 MHz. USB turnaround  |      |
	|      |          |     | time is critical for certification   |      |
	|      |          |     | where long cables and 5-Hubs are     |      |
	|      |          |     | used, so If you need the AHB to      |      |
	|      |          |     | run at less than 30 MHz, and If USB  |      |
	|      |          |     | turnaround time is not critical,     |      |
	|      |          |     | these bits can be programmed to a    |      |
	|      |          |     | larger value.                        |      |
	+------+----------+-----+--------------------------------------+------+
	| 14   | Reserv\  | RO  | Reserved for future use.             |      |
	|      | ed_0C_14 |     |                                      |      |
	+------+----------+-----+--------------------------------------+------+


To be continued ......

.. _table_usb_gusbcfg_contd_4:
.. table:: GUSBCFG, Offset Address: 0x00c (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 15   | PhyLP\   | R/W | Mode: Host and Device                | 0x0  |
	|      | wrClkSel |     |                                      |      |
	|      |          |     | PHY Low-Power Clock Select           |      |
	|      |          |     | (PhyLPwrClkSel)                      |      |
	|      |          |     |                                      |      |
	|      |          |     | Selects either 480-MHz or 48-MHz     |      |
	|      |          |     | (low-power) PHY mode. In FS          |      |
	|      |          |     | and LS modes, the PHY can usually    |      |
	|      |          |     | operate on a 48-MHz clock to         |      |
	|      |          |     | save power.                          |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: 480-MHz Internal PLL clock   |      |
	|      |          |     | - 1'b1: 48-MHz External Clock        |      |
	|      |          |     |                                      |      |
	|      |          |     | In 480 MHz mode, the UTMI interface  |      |
	|      |          |     | operates at either 60 or 30-         |      |
	|      |          |     | MHz, depending upon whether 8- or    |      |
	|      |          |     | 16-bit data width is selected. In    |      |
	|      |          |     | 48-MHz mode, the UTMI interface      |      |
	|      |          |     | operates at 48 MHz in FS mode        |      |
	|      |          |     | and at either 48 or 6 MHz in LS mode |      |
	|      |          |     | (depending on the PHY                |      |
	|      |          |     | vendor). This bit drives the         |      |
	|      |          |     | utmi_fsls_low_power core output      |      |
	|      |          |     | signal,                              |      |
	|      |          |     | and is valid only For UTMI+ PHYs.    |      |
	+------+----------+-----+--------------------------------------+------+
	| 16   | O\       | R/W | Mode: Host and Device                | 0x0  |
	|      | tgI2CSel |     |                                      |      |
	|      |          |     | UTMIFS or I2C Interface Select       |      |
	|      |          |     | (OtgI2CSel)                          |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | select the I2C interface.            |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: UTMI USB 1.1 Full-Speed      |      |
	|      |          |     |   interface for OTG signals          |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: I2C interface for OTG        |      |
	|      |          |     |   signals                            |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is writable only if I2C and |      |
	|      |          |     | UTMIFS were specified for Enable     |      |
	|      |          |     | I2C Interface? in coreConsultant     |      |
	|      |          |     | (parameter OTG_I2C_INTERFACE         |      |
	|      |          |     | = 2). Otherwise, reads return 0.     |      |
	+------+----------+-----+--------------------------------------+------+
	| 17   | ULPIFsLs | R/W | Mode: Host and Device                | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | ULPI FS/LS Select (ULPIFsLs)         |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | select the FS/LS serial interface    |      |
	|      |          |     | for                                  |      |
	|      |          |     | the ULPI PHY. This bit is valid only |      |
	|      |          |     | when the FS serial transceiver is    |      |
	|      |          |     | selected on the ULPI PHY.            |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: ULPI interface               |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b1: ULPI FS/LS serial interface  |      |
	|      |          |     |                                      |      |
	|      |          |     | (Valid only when RTL parameters      |      |
	|      |          |     | OTG_HSPHY_INTERFACE = 2 or           |      |
	|      |          |     | 3 and OTG_FSPHY_INTERFACE = 1, 2, or |      |
	|      |          |     | 3)                                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Before setting this bit, the         |      |
	|      |          |     | application needs to ensure that     |      |
	|      |          |     | GUSBCFG.ULPI_UTMI_SEL = 1'b1.        |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_gusbcfg_contd_5:
.. table:: GUSBCFG, Offset Address: 0x00c (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 18   | ULP      | R/W | Mode: Host and Device                | 0x0  |
	|      | IAutoRes |     |                                      |      |
	|      |          |     | ULPI Auto Resume (ULPIAutoRes)       |      |
	|      |          |     | This bit sets the AutoResume bit in  |      |
	|      |          |     | the Interface Control register on    |      |
	|      |          |     | the ULPI PHY.                        |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: PHY does not use AutoResume  |      |
	|      |          |     |   feature.                           |      |
	|      |          |     | - 1'b1: PHY uses AutoResume feature. |      |
	|      |          |     |                                      |      |
	|      |          |     | (Valid only when RTL parameter       |      |
	|      |          |     | OTG_HSPHY_INTERFACE = 2 or 3)        |      |
	+------+----------+-----+--------------------------------------+------+
	| 19   | ULP\     | R/W | Mode: Host and Device                | 0x0  |
	|      | IClkSusM |     |                                      |      |
	|      |          |     | ULPI Clock SuspendM (ULPIClkSusM)    |      |
	|      |          |     | This bit sets the ClockSuspendM bit  |      |
	|      |          |     | in the Interface Control register    |      |
	|      |          |     | on the ULPI PHY. This bit applies    |      |
	|      |          |     | only in serial or carkit modes.      |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: PHY powers down internal     |      |
	|      |          |     |   clock during suspend.              |      |
	|      |          |     | - 1'b1: PHY does not power down      |      |
	|      |          |     |   internal clock.                    |      |
	|      |          |     |                                      |      |
	|      |          |     | (Valid only when RTL parameter       |      |
	|      |          |     | OTG_HSPHY_INTERFACE = 2 or 3)        |      |
	+------+----------+-----+--------------------------------------+------+
	| 20   | ULPIEx\  | R/W | Mode: Host only                      | 0x0  |
	|      | tVbusDrv |     |                                      |      |
	|      |          |     | ULPI External VBUS Drive             |      |
	|      |          |     | (ULPIExtVbusDrv)                     |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit selects between internal or |      |
	|      |          |     | external supply to drive 5V on       |      |
	|      |          |     | VBUS, in ULPI PHY.                   |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: PHY drives VBUS using        |      |
	|      |          |     |   internal charge pump (Default).    |      |
	|      |          |     | - 1'b1: PHY drives VBUS using        |      |
	|      |          |     |   external supply.                   |      |
	|      |          |     |                                      |      |
	|      |          |     | (Valid only when RTL parameter       |      |
	|      |          |     | OTG_HSPHY_INTERFACE = 2 or 3)        |      |
	+------+----------+-----+--------------------------------------+------+


To be continued ......

.. _table_usb_gusbcfg_contd_6:
.. table:: GUSBCFG, Offset Address: 0x00c (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 21   | ULPI\    | R/W | Mode: Host only                      | 0x0  |
	|      | ExtVbusI\|     |                                      |      |
	|      | ndicator |     | ULPI External VBUS Indicator         |      |
	|      |          |     | (ULPIExtVbusIndicator)               |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit indicates to the ULPI PHY   |      |
	|      |          |     | to use an external VBUS              |      |
	|      |          |     | overcurrent indicator.               |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: PHY uses internal VBUS valid |      |
	|      |          |     |   comparator.                        |      |
	|      |          |     | - 1'b1: PHY uses external VBUS valid |      |
	|      |          |     |   comparator.                        |      |
	|      |          |     |                                      |      |
	|      |          |     | (Valid only when RTL parameter       |      |
	|      |          |     | OTG_HSPHY_INTERFACE = 2 or 3)        |      |
	+------+----------+-----+--------------------------------------+------+
	| 22   | TermSe\  | R/W | Mode: Device only                    | 0x0  |
	|      | lDLPulse |     |                                      |      |
	|      |          |     | TermSel DLine Pulsing Selection      |      |
	|      |          |     | (TermSelDLPulse)                     |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit selects utmi_termselect to  |      |
	|      |          |     | drive data line pulse during SRP.    |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Data line pulsing using      |      |
	|      |          |     |   utmi_txvalid (Default).            |      |
	|      |          |     | - 1'b1: Data line pulsing using      |      |
	|      |          |     |   utmi_termsel.                      |      |
	+------+----------+-----+--------------------------------------+------+
	| 23   | Co\      | R/W | Mode: Host only                      | 0x0  |
	|      | mplement |     |                                      |      |
	|      |          |     | Indicator Complement                 |      |
	|      |          |     |                                      |      |
	|      |          |     | Controls the PHY to invert the       |      |
	|      |          |     | ExternalVbusIndicator input signal,  |      |
	|      |          |     | generating the Complement Output.    |      |
	|      |          |     | For more information, refer to       |      |
	|      |          |     | the ULPI Specification.              |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: PHY does not invert          |      |
	|      |          |     |   ExternalVbusIndicator signal       |      |
	|      |          |     | - 1'b1: PHY does invert              |      |
	|      |          |     |   ExternalVbusIndicator signal       |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is reserved and read-only   |      |
	|      |          |     | when OTG_HSPHY_INTERFACE             |      |
	|      |          |     | is set to 0 or 1.                    |      |
	+------+----------+-----+--------------------------------------+------+
	| 24   | I\       | R/W | Mode: Host only                      | 0x0  |
	|      | ndicator |     |                                      |      |
	|      |          |     | Indicator Pass Through               |      |
	|      |          |     |                                      |      |
	|      |          |     | Controls whether the Complement      |      |
	|      |          |     |                                      |      |
	|      |          |     | Output is qualified with the         |      |
	|      |          |     | Internal Vbus Valid comparator       |      |
	|      |          |     | before being used in the Vbus State  |      |
	|      |          |     | in the RX CMD. For more information, |      |
	|      |          |     | refer to the ULPI                    |      |
	|      |          |     | Specification.                       |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Complement Output signal is  |      |
	|      |          |     |   qualified with the Internal        |      |
	|      |          |     |   VbusValid comparator.              |      |
	|      |          |     | - 1'b1: Complement Output signal is  |      |
	|      |          |     |   not qualified with the Internal    |      |
	|      |          |     |   VbusValid comparator.              |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is reserved and read-only   |      |
	|      |          |     | when OTG_HSPHY_INTERFACE             |      |
	|      |          |     | is set to 0 or 1.                    |      |
	+------+----------+-----+--------------------------------------+------+



To be continued ......

.. _table_usb_gusbcfg_contd_7:
.. table:: GUSBCFG, Offset Address: 0x00c (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 25   | ULPI     | R/W | Mode: Host only                      | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | ULPI Interface Protect Disable       |      |
	|      |          |     | Controls circuitry built into the    |      |
	|      |          |     | PHY For protecting the ULPI          |      |
	|      |          |     | interface                            |      |
	|      |          |     | when the link tri-states STP and     |      |
	|      |          |     | data. Any pull-ups or pull-downs     |      |
	|      |          |     | employed by this feature can be      |      |
	|      |          |     | disabled. For more information,      |      |
	|      |          |     | refer to the ULPI Specification.     |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Enables the interface        |      |
	|      |          |     |   protect circuit                    |      |
	|      |          |     | - 1'b1: Disables the interface       |      |
	|      |          |     |   protect circuit                    |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is reserved and read-only   |      |
	|      |          |     | when OTG_HSPHY_INTERFACE             |      |
	|      |          |     | is set to 0 or 1.                    |      |
	+------+----------+-----+--------------------------------------+------+
	| 26   | I\       | RO  | Mode: Host and Device                |      |
	|      | C_USBCap |     |                                      |      |
	|      |          |     | IC_USB-Capable (IC_USBCap)           |      |
	|      |          |     |                                      |      |
	|      |          |     | The application uses this bit to     |      |
	|      |          |     | control the DWC_otg core's IC_USB    |      |
	|      |          |     | capabilities.                        |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: IC_USB PHY Interface is not  |      |
	|      |          |     |   selected.                          |      |
	|      |          |     | - 1'b1: IC_USB PHY Interface is      |      |
	|      |          |     |   selected.                          |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is writable only if         |      |
	|      |          |     | OTG_ENABLE_IC_USB=1 and              |      |
	|      |          |     | OTG_FSPHY_INTERFACE!=0.              |      |
	|      |          |     |                                      |      |
	|      |          |     | The reset value depends on the       |      |
	|      |          |     | configuration parameter              |      |
	|      |          |     | OTG_SELECT_IC_USB when               |      |
	|      |          |     | OTG_ENABLE_IC_USB = 1. In all        |      |
	|      |          |     | other cases, this bit is set to 1'b0 |      |
	|      |          |     | and the bit is read only.            |      |
	+------+----------+-----+--------------------------------------+------+
	| 27   | IC_US\   | R/W | Mode: Device only                    | 0x0  |
	|      | BTrafCtl |     |                                      |      |
	|      |          |     | IC_USB TrafficPullRemove Control     |      |
	|      |          |     | (IC_USBTrafCtl)                      |      |
	|      |          |     |                                      |      |
	|      |          |     | When this bit is set,                |      |
	|      |          |     | pullup/pulldown resistors are        |      |
	|      |          |     | detached from the                    |      |
	|      |          |     | USB during traffic signaling, per    |      |
	|      |          |     | section 6.3.4 of the IC_USB          |      |
	|      |          |     | specification. This bit is valid     |      |
	|      |          |     | only when configuration parameter    |      |
	|      |          |     | OTG_ENABLE_IC_USB = 1 and register   |      |
	|      |          |     | field                                |      |
	|      |          |     | USBCFG.IC_USBCap is set to 1.        |      |
	+------+----------+-----+--------------------------------------+------+
	| 28   | Tx\      | R/W | Mode: Device only                    | 0x0  |
	|      | EndDelay |     |                                      |      |
	|      |          |     | Tx End Delay (TxEndDelay)            |      |
	|      |          |     |                                      |      |
	|      |          |     | Writing 1'b1 to this bit enables the |      |
	|      |          |     | core to follow the TxEndDelay        |      |
	|      |          |     | timings as per UTMI+ specification   |      |
	|      |          |     | 1.05 section 4.1.5 for opmode        |      |
	|      |          |     | signal during remote wakeup.         |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Normal Mode.                 |      |
	|      |          |     | - 1'b1: Tx End delay.                |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_gusbcfg_contd_8:
.. table:: GUSBCFG, Offset Address: 0x00c (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 29   | Forc\    | R/W | Mode: Host and device                | 0x0  |
	|      | eHstMode |     |                                      |      |
	|      |          |     | Force Host Mode (ForceHstMode)       |      |
	|      |          |     |                                      |      |
	|      |          |     | Writing a 1 to this bit forces the   |      |
	|      |          |     | core to host mode irrespective of    |      |
	|      |          |     | utmiotg_iddig input pin.             |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Normal Mode.                 |      |
	|      |          |     | - 1'b1: Force Host Mode.             |      |
	|      |          |     |                                      |      |
	|      |          |     | After setting the force bit, the     |      |
	|      |          |     | application must wait at least 25 ms |      |
	|      |          |     | before the change to take effect.    |      |
	|      |          |     |                                      |      |
	|      |          |     | When the simulation is in scale      |      |
	|      |          |     | down mode, waiting for 500 us is     |      |
	|      |          |     | sufficient. This bit is valid only   |      |
	|      |          |     | when OTG_MODE = 0, 1 or 2. In all    |      |
	|      |          |     | other cases, this bit reads 0.       |      |
	+------+----------+-----+--------------------------------------+------+
	| 30   | Forc\    | R/W | Mode: Host and device                | 0x0  |
	|      | eDevMode |     |                                      |      |
	|      |          |     | Force Device Mode (ForceDevMode)     |      |
	|      |          |     | Writing a 1 to this bit forces the   |      |
	|      |          |     | core to device mode irrespective of  |      |
	|      |          |     | utmiotg_iddig input pin.             |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Normal Mode.                 |      |
	|      |          |     | - 1'b1: Force Device Mode.           |      |
	|      |          |     |                                      |      |
	|      |          |     | After setting the force bit, the     |      |
	|      |          |     | application must wait at least 25 ms |      |
	|      |          |     | before the change to take effect.    |      |
	|      |          |     | When the simulation is in scale      |      |
	|      |          |     | down mode, waiting for 500 us is     |      |
	|      |          |     | sufficient. This bit is valid only   |      |
	|      |          |     | when OTG_MODE = 0, 1 or 2. In all    |      |
	|      |          |     | other cases, this bit reads 0.       |      |
	+------+----------+-----+--------------------------------------+------+
	| 31   | Corr\    | R/W | Mode: Host and device                | 0x0  |
	|      | uptTxPkt |     |                                      |      |
	|      |          |     | Corrupt Tx packet (CorruptTxPkt)     |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is for debug purposes only. |      |
	|      |          |     |                                      |      |
	|      |          |     | Never set this bit to 1.The          |      |
	|      |          |     | application should always write 1'b0 |      |
	|      |          |     | to this bit.                         |      |
	+------+----------+-----+--------------------------------------+------+

GRSTCTL
```````

Reset Register

.. _table_usb_grstctl_contd_0:
.. table:: GRSTCTL, Offset Address: 0x010
	:widths: 1 2 1 6 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 0    | CSftRst  | RO  | Write Behavior: One to set           |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | Core Soft Reset (CSftRst)            |      |
	|      |          |     |                                      |      |
	|      |          |     | Resets the hclk and phy_clock        |      |
	|      |          |     | domains as follows:                  |      |
	|      |          |     |                                      |      |
	|      |          |     | - Clears the interrupts and all the  |      |
	|      |          |     |   CSR registers except the following |      |
	|      |          |     |   register bits:                     |      |
	|      |          |     |                                      |      |
	|      |          |     |   - PCGCCTL.RstPdwnModule            |      |
	|      |          |     |   - PCGCCTL.GateHclk                 |      |
	|      |          |     |   - PCGCCTL.PwrClmp                  |      |
	|      |          |     |   - PCGCCTL.StopPPhyLPwrClkSelclk    |      |
	|      |          |     |   - GUSBCFG.PhyLPwrClkSel            |      |
	|      |          |     |   - GUSBCFG.DDRSel                   |      |
	|      |          |     |   - GUSBCFG.PHYSel                   |      |
	|      |          |     |   - GUSBCFG.FSIntf                   |      |
	|      |          |     |   - GUSBCFG.ULPI_UTMI_Sel            |      |
	|      |          |     |   - GUSBCFG.PHYIf                    |      |
	|      |          |     |   - GUSBCFG.TxEndDelay               |      |
	|      |          |     |   - GUSBCFG.TermSelDLPulse           |      |
	|      |          |     |   - GUSBCFG.ULPIClkSusM              |      |
	|      |          |     |   - GUSBCFG.ULPIAutoRes              |      |
	|      |          |     |   - GUSBCFG.ULPIFsLs                 |      |
	|      |          |     |   - GGPIO                            |      |
	|      |          |     |   - GPWRDN                           |      |
	|      |          |     |   - GADPCTL                          |      |
	|      |          |     |   - HCFG.FSLSPclkSel                 |      |
	|      |          |     |   - DCFG.DevSpd                      |      |
	|      |          |     |   - DCTL.SftDiscon                   |      |
	|      |          |     |                                      |      |
	|      |          |     | - All module state machines (except  |      |
	|      |          |     |   the AHB Slave Unit) are reset to   |      |
	|      |          |     |   the                                |      |
	|      |          |     |   IDLE state, and all the transmit   |      |
	|      |          |     |   FIFOs and the receive FIFO are     |      |
	|      |          |     |   flushed.                           |      |
	|      |          |     |                                      |      |
	|      |          |     | - Any transactions on the AHB Master |      |
	|      |          |     |   are terminated as soon as possible,|      |
	|      |          |     |   after gracefully completing the    |      |
	|      |          |     |   last                               |      |
	|      |          |     |   data phase of an AHB transfer. Any |      |
	|      |          |     |   transactions on the USB are        |      |
	|      |          |     |   terminated immediately.            |      |
	|      |          |     |                                      |      |
	|      |          |     | - When Hibernation or ADP feature is |      |
	|      |          |     |   enabled, the PMU module is not     |      |
	|      |          |     |   reset by the Core Soft Reset.      |      |
	|      |          |     |                                      |      |
	|      |          |     | The application can write to this    |      |
	|      |          |     | bit any time it wants to reset the   |      |
	|      |          |     | core. This is a                      |      |
	|      |          |     | self-clearing bit and the core       |      |
	|      |          |     | clears this bit after all the        |      |
	|      |          |     | necessary logic is reset             |      |
	|      |          |     | in the core, which can take several  |      |
	|      |          |     | clocks, depending on the current     |      |
	|      |          |     | state of                             |      |
	|      |          |     | the core. After this bit is cleared, |      |
	|      |          |     | the application must wait at least 3 |      |
	|      |          |     | PHY                                  |      |
	|      |          |     | clocks before doing any access to    |      |
	|      |          |     | the PHY domain (synchronization      |      |
	|      |          |     | delay).                              |      |
	|      |          |     |                                      |      |
	|      |          |     | The application must also must check |      |
	|      |          |     | that bit 31 of this register is 1    |      |
	|      |          |     | (AHB                                 |      |
	|      |          |     | Master is IDLE) before starting any  |      |
	|      |          |     | operation.                           |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_grstctl_contd_1:
.. table:: GRSTCTL, Offset Address: 0x010 (continued)
	:widths: 1 2 1 5 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	|      |          |     | Typically, software reset is used    |      |
	|      |          |     | during software development and also |      |
	|      |          |     | when                                 |      |
	|      |          |     | you dynamically change the PHY       |      |
	|      |          |     | selection bits in the USB            |      |
	|      |          |     | configuration                        |      |
	|      |          |     | registers listed above. When you     |      |
	|      |          |     | change the PHY, the corresponding    |      |
	|      |          |     | clock for                            |      |
	|      |          |     | the PHY is selected and used in the  |      |
	|      |          |     | PHY domain. After a new clock is     |      |
	|      |          |     | selected, the PHY domain has to be   |      |
	|      |          |     | reset for proper operation.          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	|      |          |     |                                      |      |
	|      |          |     | One-Way: Enabled                     |      |
	+------+----------+-----+--------------------------------------+------+
	| 1    | PIU\     | RO  | Write Behavior: One to set           |      |
	|      | FSSftRst |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | PIU FS Dedicated Controller Soft     |      |
	|      |          |     | Reset (PIUFSSftRst)                  |      |
	|      |          |     |                                      |      |
	|      |          |     | Resets the PIU FS Dedicated          |      |
	|      |          |     | Controller                           |      |
	|      |          |     |                                      |      |
	|      |          |     | All module state machines in FS      |      |
	|      |          |     | Dedicated Controller of PIU are      |      |
	|      |          |     | reset to the                         |      |
	|      |          |     | IDLE state. Used to reset the FS     |      |
	|      |          |     | Dedicated controller in PIU in case  |      |
	|      |          |     | of any                               |      |
	|      |          |     | PHY Errors like Loss of activity or  |      |
	|      |          |     | Babble Error resulting in the PHY    |      |
	|      |          |     | remaining                            |      |
	|      |          |     | in RX state for more than one frame  |      |
	|      |          |     | boundary.                            |      |
	|      |          |     |                                      |      |
	|      |          |     | This is a self clearing bit and core |      |
	|      |          |     | clears this bit after all the        |      |
	|      |          |     | necessary logic is                   |      |
	|      |          |     | reset in the core.                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	+------+----------+-----+--------------------------------------+------+
	| 2    | Fr\      | RO  | Write Behavior: One to set           |      |
	|      | mCntrRst |     |                                      |      |
	|      |          |     | Mode: Host only                      |      |
	|      |          |     |                                      |      |
	|      |          |     | Host Frame Counter Reset             |      |
	|      |          |     | (FrmCntrRst)                         |      |
	|      |          |     |                                      |      |
	|      |          |     | The application writes this bit to   |      |
	|      |          |     | reset the (micro)frame number        |      |
	|      |          |     | counter inside                       |      |
	|      |          |     | the core. When the (micro)frame      |      |
	|      |          |     | counter is reset, the subsequent SOF |      |
	|      |          |     | sent                                 |      |
	|      |          |     | out by the core has a (micro)frame   |      |
	|      |          |     | number of 0.                         |      |
	|      |          |     |                                      |      |
	|      |          |     | If the application writes 1 to the   |      |
	|      |          |     | bit, it may not be able to read back |      |
	|      |          |     | the value as                         |      |
	|      |          |     | it gets cleared by the core in a few |      |
	|      |          |     | clock cycles.                        |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	|      |          |     |                                      |      |
	|      |          |     | One-Way: Enabled                     |      |
	+------+----------+-----+--------------------------------------+------+
	| 3    | IN\      | RWS | Mode: Device only                    |      |
	|      | TknQFlsh |     |                                      |      |
	|      |          |     | IN Token Sequence Learning Queue     |      |
	|      |          |     |                                      |      |
	|      |          |     | Flush (INTknQFlsh)                   |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is valid only if            |      |
	|      |          |     | OTG_EN_DED_TX_FIFO = 0.              |      |
	|      |          |     |                                      |      |
	|      |          |     | The application writes this bit to   |      |
	|      |          |     | flush the IN Token Sequence Learning |      |
	|      |          |     | Queue.                               |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_grstctl_contd_2:
.. table:: GRSTCTL, Offset Address: 0x010 (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 4    | RxFFlsh  | RO  | Write Behavior: One to set           |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | RxFIFO Flush (RxFFlsh)               |      |
	|      |          |     |                                      |      |
	|      |          |     | The application can flush the entire |      |
	|      |          |     | RxFIFO using this bit, but must      |      |
	|      |          |     | first ensure                         |      |
	|      |          |     | that the core is not in the middle   |      |
	|      |          |     | of a transaction. The application    |      |
	|      |          |     | must only                            |      |
	|      |          |     | write to this bit after checking     |      |
	|      |          |     | that the core is neither reading     |      |
	|      |          |     | from the RxFIFO                      |      |
	|      |          |     | nor writing to the RxFIFO.           |      |
	|      |          |     | The application must wait until the  |      |
	|      |          |     | bit is cleared before performing any |      |
	|      |          |     | other                                |      |
	|      |          |     | operations. This bit requires 8      |      |
	|      |          |     | clocks (slowest of PHY or AHB clock) |      |
	|      |          |     | to clear.                            |      |
	+------+----------+-----+--------------------------------------+------+
	| 5    | TxFFlsh  | RWS | Write Behavior: One to set           |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | TxFIFO Flush (TxFFlsh)               |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit selectively flushes a       |      |
	|      |          |     | single or all transmit FIFOs, but    |      |
	|      |          |     | cannot do so if                      |      |
	|      |          |     | the core is in the midst of a        |      |
	|      |          |     | transaction.                         |      |
	|      |          |     |                                      |      |
	|      |          |     | The application must write this bit  |      |
	|      |          |     | only after checking that the core is |      |
	|      |          |     | neither                              |      |
	|      |          |     | writing to the TxFIFO nor reading    |      |
	|      |          |     | from the TxFIFO.                     |      |
	|      |          |     |                                      |      |
	|      |          |     | Verify using these registers:        |      |
	|      |          |     |                                      |      |
	|      |          |     | - Read - NAK Effective Interrupt     |      |
	|      |          |     |   ensures the core is not reading    |      |
	|      |          |     |   from the FIFO                      |      |
	|      |          |     |                                      |      |
	|      |          |     | - Write - GRSTCTL.AHBIdle ensures    |      |
	|      |          |     |   the core is not writing anything   |      |
	|      |          |     |   to the FIFO                        |      |
	|      |          |     |                                      |      |
	|      |          |     | Flushing is normally recommended     |      |
	|      |          |     | when FIFOs are reconfigured or when  |      |
	|      |          |     | switching between Shared FIFO and    |      |
	|      |          |     | Dedicated Transmit FIFO operation.   |      |
	|      |          |     | FIFO flushing is also recommended    |      |
	|      |          |     | during device endpoint disable. The  |      |
	|      |          |     | application must wait until the core |      |
	|      |          |     | clears this bit before performing    |      |
	|      |          |     | any                                  |      |
	|      |          |     | operations. This bit takes eight     |      |
	|      |          |     | clocks to clear, using the slower    |      |
	|      |          |     | clock of                             |      |
	|      |          |     | phy_clk or hclk.                     |      |
	+------+----------+-----+--------------------------------------+------+

To be continued ......

.. _table_usb_grstctl_contd_3:
.. table:: GRSTCTL, Offset Address: 0x010 (continued)
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 10:6 | TxFNum   | R/W | Mode: Host and Device                | 0x0  |
	|      |          |     |                                      |      |
	|      |          |     | TxFIFO Number (TxFNum)               |      |
	|      |          |     |                                      |      |
	|      |          |     | This is the FIFO number that must be |      |
	|      |          |     | flushed using the TxFIFO Flush bit.  |      |
	|      |          |     | This                                 |      |
	|      |          |     | field must not be changed until the  |      |
	|      |          |     | core clears the TxFIFO Flush bit.    |      |
	|      |          |     |                                      |      |
	|      |          |     | - 5'h0:                              |      |
	|      |          |     |                                      |      |
	|      |          |     |   - Non-periodic TxFIFO flush in     |      |
	|      |          |     |     Host mode                        |      |
	|      |          |     |   - Non-periodic TxFIFO flush in     |      |
	|      |          |     |     device mode when in shared FIFO  |      |
	|      |          |     |     operation                        |      |
	|      |          |     |   - Tx FIFO 0 flush in device mode   |      |
	|      |          |     |     when in dedicated FIFO mode      |      |
	|      |          |     |                                      |      |
	|      |          |     | - 5'h1:                              |      |
	|      |          |     |                                      |      |
	|      |          |     |   - Periodic TxFIFO flush in Host    |      |
	|      |          |     |     mode                             |      |
	|      |          |     |   - Periodic TxFIFO 1 flush in Device|      |
	|      |          |     |     mode when in shared FIFO         |      |
	|      |          |     |     operation                        |      |
	|      |          |     |   - TXFIFO 1 flush in device mode    |      |
	|      |          |     |     when in dedicated FIFO mode      |      |
	|      |          |     |                                      |      |
	|      |          |     | - 5'h2:                              |      |
	|      |          |     |                                      |      |
	|      |          |     |   - Periodic TxFIFO 2 flush in       |      |
	|      |          |     |     Device mode when in shared FIFO  |      |
	|      |          |     |     operation                        |      |
	|      |          |     |   - TXFIFO 2 flush in device mode    |      |
	|      |          |     |     when in dedicated FIFO mode      |      |
	|      |          |     |                                      |      |
	|      |          |     |  ...                                 |      |
	|      |          |     |                                      |      |
	|      |          |     | - 5'hF:                              |      |
	|      |          |     |                                      |      |
	|      |          |     |   - Periodic TxFIFO 15 flush in      |      |
	|      |          |     |     Device mode when in shared FIFO  |      |
	|      |          |     |     operation                        |      |
	|      |          |     |   - TXFIFO 15 flush in device mode   |      |
	|      |          |     |     when in dedicated FIFO mode      |      |
	|      |          |     |                                      |      |
	|      |          |     | - 5'h10:                             |      |
	|      |          |     |                                      |      |
	|      |          |     |   - Flush all the transmit FIFOs in  |      |
	|      |          |     |     device or host mode.             |      |
	+------+----------+-----+--------------------------------------+------+
	| 29:11| R\       | RO  | Reserved for future use.             |      |
	|      | eserved\ |     |                                      |      |
	|      | _10_29_11|     |                                      |      |
	+------+----------+-----+--------------------------------------+------+
	| 30   | DMAReq   | RO  | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | DMA Request Signal (DMAReq)          |      |
	|      |          |     |                                      |      |
	|      |          |     | Indicates that the DMA request is in |      |
	|      |          |     | progress. Used for debug.            |      |
	+------+----------+-----+--------------------------------------+------+
	| 31   | AHBIdle  | RO  | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | AHB Master Idle (AHBIdle)            |      |
	|      |          |     |                                      |      |
	|      |          |     | Indicates that the AHB Master State  |      |
	|      |          |     | Machine is in the IDLE condition.    |      |
	+------+----------+-----+--------------------------------------+------+

GINTSTS
```````

Interrupt Status Register

.. _table_usb_gintsts:
.. table:: GINTSTS, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------+-----+--------------------------------------+------+
	| Bits | Name     | Acc\| Description                          | R\   |
	|      |          | ess |                                      | eset |
	+======+==========+=====+======================================+======+
	| 0    | CurMod   | RO  | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | Current Mode of Operation (CurMod)   |      |
	|      |          |     |                                      |      |
	|      |          |     | Indicates the current mode.          |      |
	|      |          |     |                                      |      |
	|      |          |     | - 1'b0: Device mode                  |      |
	|      |          |     | - 1'b1: Host mode                    |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	|      |          |     |                                      |      |
	|      |          |     | One-Way: Enabled                     |      |
	+------+----------+-----+--------------------------------------+------+
	| 1    | ModeMis  | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode Mismatch Interrupt (ModeMis)    |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit when the      |      |
	|      |          |     | application is trying to access:     |      |
	|      |          |     |                                      |      |
	|      |          |     | - A Host mode register, when the     |      |
	|      |          |     |   core is operating in Device mode   |      |
	|      |          |     |                                      |      |
	|      |          |     | - A Device mode register, when the   |      |
	|      |          |     |   core is operating in Host mode     |      |
	|      |          |     |                                      |      |
	|      |          |     | The register access is completed on  |      |
	|      |          |     | the AHB with an OKAY response,       |      |
	|      |          |     | but is ignored by the core           |      |
	|      |          |     | internally and does not affect the   |      |
	|      |          |     | operation                            |      |
	|      |          |     | of the core.                         |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit can be set only by the core |      |
	|      |          |     | and the application should write 1   |      |
	|      |          |     | to clear it.                         |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	+------+----------+-----+--------------------------------------+------+
	| 2    | OTGInt   | RO  | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | OTG Interrupt (OTGInt)               |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit to indicate   |      |
	|      |          |     | an OTG protocol event. The           |      |
	|      |          |     | application must read the OTG        |      |
	|      |          |     | Interrupt Status (GOTGINT) register  |      |
	|      |          |     | to                                   |      |
	|      |          |     | determine the exact event that       |      |
	|      |          |     | caused this interrupt. The           |      |
	|      |          |     | application                          |      |
	|      |          |     | must clear the appropriate status    |      |
	|      |          |     | bit in the GOTGINT register to clear |      |
	|      |          |     | this bit.                            |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow: Yes                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Ctrl: vs_1t                   |      |
	|      |          |     |                                      |      |
	|      |          |     | Shadow Read Select: shrd_sel         |      |
	|      |          |     |                                      |      |
	|      |          |     | One-Way: Enabled                     |      |
	+------+----------+-----+--------------------------------------+------+
	| 3    | Sof      | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | Start of (micro)Frame (Sof)          |      |
	|      |          |     |                                      |      |
	|      |          |     | In Host mode, the core sets this bit |      |
	|      |          |     | to indicate that an SOF (FS),        |      |
	|      |          |     | micro-SOF (HS), or Keep-Alive (LS)   |      |
	|      |          |     | is transmitted on the USB. The       |      |
	|      |          |     | application must write a 1 to this   |      |
	|      |          |     | bit to clear the interrupt.          |      |
	|      |          |     |                                      |      |
	|      |          |     | In Device mode, in the core sets     |      |
	|      |          |     | this bit to indicate that an SOF     |      |
	|      |          |     | token                                |      |
	|      |          |     | has been received on the USB. The    |      |
	|      |          |     | application can read the Device      |      |
	|      |          |     | Status register to get the current   |      |
	|      |          |     | (micro)Frame number. This interrupt  |      |
	|      |          |     | is seen only when the core is        |      |
	|      |          |     | operating at either HS or FS.This    |      |
	|      |          |     | bit can                              |      |
	|      |          |     | be set only by the core and the      |      |
	|      |          |     | application must write 1 to clear    |      |
	|      |          |     | it.                                  |      |
	|      |          |     |                                      |      |
	|      |          |     | Note: The register may return 1'b1   |      |
	|      |          |     | if read immediately after power on   |      |
	|      |          |     | reset. If the register bit reads     |      |
	|      |          |     | 1'b1 immediately after power on      |      |
	|      |          |     | reset, it                            |      |
	|      |          |     | does not indicate that an SOF has    |      |
	|      |          |     | been sent (in host mode), or SOF     |      |
	|      |          |     | has been received (in device mode).  |      |
	|      |          |     | The read value of this interrupt is  |      |
	|      |          |     | valid only after a valid connection  |      |
	|      |          |     | between host and device is           |      |
	|      |          |     | established. If the bit is set after |      |
	|      |          |     | power on reset, the application can  |      |
	|      |          |     | clear the bit.                       |      |
	+------+----------+-----+--------------------------------------+------+
	| 4    | RxFLvl   | RO  | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | RxFIFO Non-Empty (RxFLvl)            |      |
	|      |          |     |                                      |      |
	|      |          |     | Indicates that there is at least one |      |
	|      |          |     | packet pending to be read from the   |      |
	|      |          |     | RxFIFO.                              |      |
	+------+----------+-----+--------------------------------------+------+
	| 5    | NPTxFEmp | RO  | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | Non-periodic TxFIFO Empty (NPTxFEmp) |      |
	|      |          |     |                                      |      |
	|      |          |     | This interrupt is asserted when the  |      |
	|      |          |     | Non-periodic TxFIFO is either half   |      |
	|      |          |     | or completely empty, and there is    |      |
	|      |          |     | space for at least one entry to be   |      |
	|      |          |     | written to the Non-periodic Transmit |      |
	|      |          |     | Request Queue. The half or           |      |
	|      |          |     | completely empty status is           |      |
	|      |          |     | determined by the Non-periodic       |      |
	|      |          |     | TxFIFO                               |      |
	|      |          |     | Empty Level bit in the Core AHB      |      |
	|      |          |     | Configuration register               |      |
	|      |          |     | (GAHBCFG.NPTxFEmpLvl).               |      |
	|      |          |     |                                      |      |
	|      |          |     | In host mode, the application can    |      |
	|      |          |     | use GINTSTS.NPTxFEmp with the        |      |
	|      |          |     | OTG_EN_DED_TX_FIFO parameter set to  |      |
	|      |          |     | either 1 or 0.                       |      |
	|      |          |     |                                      |      |
	|      |          |     | In device mode, the application uses |      |
	|      |          |     | GINTSTS.NPTxFEmp when                |      |
	|      |          |     | OTG_EN_DED_TX_FIFO=0. When           |      |
	|      |          |     | OTG_EN_DED_TX_FIFO=1, the            |      |
	|      |          |     | application uses DIEPINTn.TxFEmp.    |      |
	+------+----------+-----+--------------------------------------+------+
	| 6    | G\       | RO  | Mode: Device only                    |      |
	|      | INNakEff |     |                                      |      |
	|      |          |     | Global IN Non-periodic NAK Effective |      |
	|      |          |     | (GINNakEff)                          |      |
	|      |          |     |                                      |      |
	|      |          |     | Indicates that the Set Global        |      |
	|      |          |     | Non-periodic IN NAK bit in the       |      |
	|      |          |     | Device                               |      |
	|      |          |     | Control register (DCTL.SGNPInNak)    |      |
	|      |          |     | set by the application has taken     |      |
	|      |          |     | effect in the core. That is, the     |      |
	|      |          |     | core has sampled the Global IN NAK   |      |
	|      |          |     | bit                                  |      |
	|      |          |     | set by the application. This bit can |      |
	|      |          |     | be cleared by clearing the Clear     |      |
	|      |          |     | Global Non-periodic IN NAK bit in    |      |
	|      |          |     | the Device Control register          |      |
	|      |          |     | (DCTL.CGNPInNak). This interrupt     |      |
	|      |          |     | does not necessarily mean that a     |      |
	|      |          |     | NAK handshake is sent out on the     |      |
	|      |          |     | USB. The STALL bit takes             |      |
	|      |          |     | precedence over the NAK bit.         |      |
	+------+----------+-----+--------------------------------------+------+
	| 7    | GO\      | RO  | Mode: Device only                    |      |
	|      | UTNakEff |     |                                      |      |
	|      |          |     | Global OUT NAK Effective             |      |
	|      |          |     | (GOUTNakEff)                         |      |
	|      |          |     |                                      |      |
	|      |          |     | Indicates that the Set Global OUT    |      |
	|      |          |     | NAK bit in the Device Control        |      |
	|      |          |     | register (DCTL.SGOUTNak) set by the  |      |
	|      |          |     | application has taken effect in      |      |
	|      |          |     | the core. This bit can be cleared by |      |
	|      |          |     | writing the Clear Global OUT NAK     |      |
	|      |          |     | bit in the Device Control register   |      |
	|      |          |     | (DCTL.CGOUTNak).                     |      |
	+------+----------+-----+--------------------------------------+------+
	| 8    | UL\      | RWC | Write Behavior: One to clear         |      |
	|      | PICKINT  |     |                                      |      |
	|      | _I2CCKINT|     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | ULPI Carkit Interrupt (ULPICKINT)    |      |
	|      |          |     | The core sets this interrupt when a  |      |
	|      |          |     | ULPI Carkit interrupt is received.   |      |
	|      |          |     | The core's PHY sets ULPI Carkit      |      |
	|      |          |     | interrupt in UART or Audio mode.     |      |
	|      |          |     | This field is used only if the       |      |
	|      |          |     | Carkit interface was enabled in      |      |
	|      |          |     | coreConsultant (parameter            |      |
	|      |          |     | OTG_ULPI_CARKIT = 1). Otherwise,     |      |
	|      |          |     | reads return 0.                      |      |
	|      |          |     |                                      |      |
	|      |          |     | I2C Carkit Interrupt (I2CCKINT)      |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this interrupt when a  |      |
	|      |          |     | Carkit interrupt is received. The    |      |
	|      |          |     | core's PHY sets the I2C Carkit       |      |
	|      |          |     | interrupt in Audio mode.             |      |
	|      |          |     | This field is used only if the I2C   |      |
	|      |          |     | interface was enabled in             |      |
	|      |          |     | coreConsultant (parameter            |      |
	|      |          |     | OTG_I2C_INTERFACE = 1). Otherwise,   |      |
	|      |          |     | reads return 0.                      |      |
	+------+----------+-----+--------------------------------------+------+
	| 9    | I2CINT   | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | I2C Interrupt (I2CINT)               |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this interrupt when    |      |
	|      |          |     | I2C access is completed on the I2C   |      |
	|      |          |     | interface.                           |      |
	|      |          |     |                                      |      |
	|      |          |     | This field is used only if the I2C   |      |
	|      |          |     | interface was enabled in             |      |
	|      |          |     | coreConsultant (parameter            |      |
	|      |          |     | OTG_I2C_INTERFACE = 1). Otherwise,   |      |
	|      |          |     | reads return 0.                      |      |
	+------+----------+-----+--------------------------------------+------+
	| 10   | ErlySusp | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | Early Suspend (ErlySusp)             |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit to indicate   |      |
	|      |          |     | that an Idle state has been detected |      |
	|      |          |     | on the USB For 3 ms.                 |      |
	+------+----------+-----+--------------------------------------+------+
	| 11   | USBSusp  | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | USB Suspend (USBSusp)                |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit to indicate   |      |
	|      |          |     | that a suspend was detected on the   |      |
	|      |          |     | USB. The core enters the Suspend     |      |
	|      |          |     | state when there is no activity on   |      |
	|      |          |     | the linestate signal for an extended |      |
	|      |          |     | period of time.                      |      |
	+------+----------+-----+--------------------------------------+------+
	| 12   | USBRst   | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | USB Reset (USBRst)                   |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit to indicate   |      |
	|      |          |     | that a reset is detected on the USB. |      |
	+------+----------+-----+--------------------------------------+------+
	| 13   | EnumDone | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | Enumeration Done (EnumDone)          |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit to indicate   |      |
	|      |          |     | that speed enumeration is complete.  |      |
	|      |          |     |                                      |      |
	|      |          |     | The application must read the Device |      |
	|      |          |     | Status (DSTS) register to obtain     |      |
	|      |          |     | the enumerated speed.                |      |
	+------+----------+-----+--------------------------------------+------+
	| 14   | IS\      | RWC | Write Behavior: One to clear         |      |
	|      | OOutDrop |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | Isochronous OUT Packet Dropped       |      |
	|      |          |     | Interrupt (ISOOutDrop)               |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit when it fails |      |
	|      |          |     | to write an isochronous OUT packet   |      |
	|      |          |     | into the RxFIFO because the RxFIFO   |      |
	|      |          |     | does not have enough space to        |      |
	|      |          |     | accommodate a maximum packet size    |      |
	|      |          |     | packet for the isochronous           |      |
	|      |          |     | OUT endpoint.                        |      |
	+------+----------+-----+--------------------------------------+------+
	| 15   | EOPF     | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | End of Periodic Frame Interrupt      |      |
	|      |          |     | (EOPF)                               |      |
	|      |          |     |                                      |      |
	|      |          |     | Indicates that the period specified  |      |
	|      |          |     | in the Periodic Frame Interval field |      |
	|      |          |     | of the Device Configuration register |      |
	|      |          |     | (DCFG.PerFrInt) has been             |      |
	|      |          |     | reached in the current microframe.   |      |
	+------+----------+-----+--------------------------------------+------+
	| 16   | Rst\     | RWC | Mode: Host and Device                |      |
	|      | rDoneInt |     |                                      |      |
	|      |          |     | Restore Done Interrupt (RstrDoneInt) |      |
	|      |          |     | The core sets this bit to indicate   |      |
	|      |          |     | that the Restore command after       |      |
	|      |          |     | Hibernation was completed by the     |      |
	|      |          |     | core.                                |      |
	|      |          |     |                                      |      |
	|      |          |     | The core continues from Suspend      |      |
	|      |          |     | state into the mode dictated by the  |      |
	|      |          |     | PCGCCTL.RestoreMode field.           |      |
	|      |          |     |                                      |      |
	|      |          |     | This bit is valid only when          |      |
	|      |          |     | Hibernation feature is enabled       |      |
	|      |          |     | (OTG_EN_PWRPOPT=2).                  |      |
	+------+----------+-----+--------------------------------------+------+
	| 17   | EPMis    | RO  | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | Endpoint Mismatch Interrupt (EPMis)  |      |
	|      |          |     | Note: This interrupt is valid only   |      |
	|      |          |     | in shared FIFO operation.            |      |
	|      |          |     |                                      |      |
	|      |          |     | Indicates that an IN token has been  |      |
	|      |          |     | received for a non-periodic          |      |
	|      |          |     | endpoint, but the data for another   |      |
	|      |          |     | endpoint is present in the top of    |      |
	|      |          |     | the                                  |      |
	|      |          |     | Non-periodic Transmit FIFO and the   |      |
	|      |          |     | IN endpoint mismatch count           |      |
	|      |          |     | programmed by the application has    |      |
	|      |          |     | expired.                             |      |
	+------+----------+-----+--------------------------------------+------+
	| 18   | IEPInt   | RO  | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | IN Endpoints Interrupt (IEPInt)      |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit to indicate   |      |
	|      |          |     | that an interrupt is pending on one  |      |
	|      |          |     | of                                   |      |
	|      |          |     | the IN endpoints of the core (in     |      |
	|      |          |     | Device mode). The application must   |      |
	|      |          |     | read the Device All Endpoints        |      |
	|      |          |     | Interrupt (DAINT) register to        |      |
	|      |          |     | determine                            |      |
	|      |          |     | the exact number of the IN endpoint  |      |
	|      |          |     | on Device IN Endpoint-n Interrupt    |      |
	|      |          |     | (DIEPINTn) register to determine the |      |
	|      |          |     | exact cause of the interrupt. The    |      |
	|      |          |     | application must clear the           |      |
	|      |          |     | appropriate status bit in the        |      |
	|      |          |     | corresponding                        |      |
	|      |          |     | DIEPINTn register to clear this bit. |      |
	+------+----------+-----+--------------------------------------+------+
	| 19   | OEPInt   | RO  | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | OUT Endpoints Interrupt (OEPInt)     |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit to indicate   |      |
	|      |          |     | that an interrupt is pending on one  |      |
	|      |          |     | of                                   |      |
	|      |          |     | the OUT endpoints of the core (in    |      |
	|      |          |     | Device mode). The application must   |      |
	|      |          |     | read the Device All Endpoints        |      |
	|      |          |     | Interrupt (DAINT) register to        |      |
	|      |          |     | determine                            |      |
	|      |          |     | the exact number of the OUT endpoint |      |
	|      |          |     | on which the interrupt               |      |
	|      |          |     | occurred, and Then read the          |      |
	|      |          |     | corresponding Device OUT Endpoint-n  |      |
	|      |          |     | Interrupt (DOEPINTn) register to     |      |
	|      |          |     | determine the exact cause of the     |      |
	|      |          |     | interrupt. The application must      |      |
	|      |          |     | clear the appropriate status bit in  |      |
	|      |          |     | the                                  |      |
	|      |          |     | corresponding DOEPINTn register to   |      |
	|      |          |     | clear this bit.                      |      |
	+------+----------+-----+--------------------------------------+------+
	| 20   | inc\     | RWC | Write Behavior: One to clear         |      |
	|      | ompISOIN |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | Incomplete Isochronous IN Transfer   |      |
	|      |          |     | (incompISOIN)                        |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this interrupt to      |      |
	|      |          |     | indicate that there is at least one  |      |
	|      |          |     | isochronous IN endpoint on which the |      |
	|      |          |     | transfer is not completed in the     |      |
	|      |          |     | current microframe. This interrupt   |      |
	|      |          |     | is asserted along with the End of    |      |
	|      |          |     | Periodic Frame Interrupt (EOPF) bit  |      |
	|      |          |     | in this register.                    |      |
	|      |          |     |                                      |      |
	|      |          |     | Note: This interrupt is not asserted |      |
	|      |          |     | in Scatter/Gather DMA mode.          |      |
	+------+----------+-----+--------------------------------------+------+
	| 21   | incom\   | RWC | Write Behavior: One to clear         |      |
	|      | plP_inco\|     |                                      |      |
	|      | mpISOOUT |     | Incomplete Periodic Transfer         |      |
	|      |          |     | (incomplP)                           |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Host only                      |      |
	|      |          |     |                                      |      |
	|      |          |     | In Host mode, the core sets this     |      |
	|      |          |     | interrupt bit when there are         |      |
	|      |          |     | incomplete periodic transactions     |      |
	|      |          |     | still pending which are scheduled    |      |
	|      |          |     | for                                  |      |
	|      |          |     | the current microframe.              |      |
	|      |          |     | Incomplete Isochronous OUT Transfer  |      |
	|      |          |     | (incompISOOUT)                       |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | In Device mode, the core sets this   |      |
	|      |          |     | interrupt to indicate that there is  |      |
	|      |          |     | at                                   |      |
	|      |          |     | least one isochronous OUT endpoint   |      |
	|      |          |     | on which the transfer is not         |      |
	|      |          |     | completed in the current microframe. |      |
	|      |          |     | This interrupt is asserted along     |      |
	|      |          |     | with the End of Periodic Frame       |      |
	|      |          |     | Interrupt (EOPF) bit in this         |      |
	|      |          |     | register.                            |      |
	+------+----------+-----+--------------------------------------+------+
	| 22   | FetSusp  | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | Data Fetch Suspended (FetSusp)       |      |
	|      |          |     |                                      |      |
	|      |          |     | This interrupt is valid only in DMA  |      |
	|      |          |     | mode. This interrupt indicates that  |      |
	|      |          |     | the core has stopped fetching data   |      |
	|      |          |     | For IN endpoints due to the          |      |
	|      |          |     | unavailability of TxFIFO space or    |      |
	|      |          |     | Request Queue space. This            |      |
	|      |          |     | interrupt is used by the application |      |
	|      |          |     | For an endpoint mismatch             |      |
	|      |          |     | algorithm.                           |      |
	|      |          |     |                                      |      |
	|      |          |     | For example, after detecting an      |      |
	|      |          |     | endpoint mismatch, the application:  |      |
	|      |          |     |                                      |      |
	|      |          |     | - Sets a Global non-periodic IN NAK  |      |
	|      |          |     |   handshake                          |      |
	|      |          |     |                                      |      |
	|      |          |     | - Disables In endpoints              |      |
	|      |          |     |                                      |      |
	|      |          |     | - Flushes the FIFO                   |      |
	|      |          |     |                                      |      |
	|      |          |     | - Determines the token sequence from |      |
	|      |          |     |   the IN Token Sequence              |      |
	|      |          |     |                                      |      |
	|      |          |     | Learning Queue                       |      |
	|      |          |     |                                      |      |
	|      |          |     | - Re-enables the endpoints           |      |
	|      |          |     |                                      |      |
	|      |          |     | - Clears the Global non-periodic IN  |      |
	|      |          |     |   NAK handshake                      |      |
	|      |          |     |                                      |      |
	|      |          |     | If the Global non-periodic IN NAK is |      |
	|      |          |     | cleared, the core has not yet        |      |
	|      |          |     | fetched data for the IN endpoint,    |      |
	|      |          |     | and the IN token is received. The    |      |
	|      |          |     | core generates an 'IN token received |      |
	|      |          |     | when FIFO empty' interrupt.          |      |
	|      |          |     |                                      |      |
	|      |          |     | DWC_otg then sends the host a NAK    |      |
	|      |          |     | response. To avoid this scenario,    |      |
	|      |          |     | the application can check the        |      |
	|      |          |     | GINTSTS.FetSusp interrupt, which     |      |
	|      |          |     | ensures that the FIFO is full before |      |
	|      |          |     | clearing a Global NAK handshake.     |      |
	|      |          |     |                                      |      |
	|      |          |     | Alternatively, the application can   |      |
	|      |          |     | mask the “IN token received when     |      |
	|      |          |     | FIFO empty” interrupt when clearing  |      |
	|      |          |     | a Global IN NAK handshake.           |      |
	+------+----------+-----+--------------------------------------+------+
	| 23   | ResetDet | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Device only                    |      |
	|      |          |     |                                      |      |
	|      |          |     | Reset detected Interrupt (ResetDet)  |      |
	|      |          |     | In Device mode, this interrupt is    |      |
	|      |          |     | asserted when a reset is detected on |      |
	|      |          |     | the USB in partial power-down mode   |      |
	|      |          |     | when the device is in Suspend.       |      |
	|      |          |     |                                      |      |
	|      |          |     | In Host mode, this interrupt is not  |      |
	|      |          |     | asserted.                            |      |
	+------+----------+-----+--------------------------------------+------+
	| 24   | PrtInt   | RO  | Mode: Host only                      |      |
	|      |          |     |                                      |      |
	|      |          |     | Host Port Interrupt (PrtInt)         |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit to indicate a |      |
	|      |          |     | change in port status of one of the  |      |
	|      |          |     | DWC_otg core ports in Host mode. The |      |
	|      |          |     | application must read the            |      |
	|      |          |     | Host Port Control and Status (HPRT)  |      |
	|      |          |     | register to determine the exact      |      |
	|      |          |     | event that caused this interrupt.    |      |
	|      |          |     |                                      |      |
	|      |          |     | The application must clear the       |      |
	|      |          |     | appropriate status bit in the Host   |      |
	|      |          |     | Port Control and Status register to  |      |
	|      |          |     | clear this bit.                      |      |
	+------+----------+-----+--------------------------------------+------+
	| 25   | HChInt   | RO  | Mode: Host only                      |      |
	|      |          |     |                                      |      |
	|      |          |     | Host Channels Interrupt (HChInt)     |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit to indicate   |      |
	|      |          |     | that an interrupt is pending on one  |      |
	|      |          |     | of                                   |      |
	|      |          |     | the channels of the core (in Host    |      |
	|      |          |     | mode). The application must read the |      |
	|      |          |     | Host All Channels Interrupt (HAINT)  |      |
	|      |          |     | register to determine the exact      |      |
	|      |          |     | number of the channel on which the   |      |
	|      |          |     | interrupt occurred and then read     |      |
	|      |          |     | the corresponding Host Channel-n     |      |
	|      |          |     | Interrupt (HCINTn) register to       |      |
	|      |          |     | determine the exact cause of the     |      |
	|      |          |     | interrupt. The application must      |      |
	|      |          |     | clear                                |      |
	|      |          |     | the appropriate status bit in the    |      |
	|      |          |     | HCINTn register to clear this bit.   |      |
	+------+----------+-----+--------------------------------------+------+
	| 26   | PTxFEmp  | RO  | Mode: Host only                      |      |
	|      |          |     |                                      |      |
	|      |          |     | Periodic TxFIFO Empty (PTxFEmp)      |      |
	|      |          |     |                                      |      |
	|      |          |     | This interrupt is asserted when the  |      |
	|      |          |     | Periodic Transmit FIFO is either     |      |
	|      |          |     | half or completely empty and there   |      |
	|      |          |     | is space for at least one entry to   |      |
	|      |          |     | be                                   |      |
	|      |          |     | written in the Periodic Request      |      |
	|      |          |     | Queue. The half or completely empty  |      |
	|      |          |     | status is determined by the Periodic |      |
	|      |          |     | TxFIFO Empty Level bit in the        |      |
	|      |          |     | Core AHB Configuration register      |      |
	|      |          |     | (GAHBCFG.PTxFEmpLvl).                |      |
	+------+----------+-----+--------------------------------------+------+
	| 27   | LPM_Int  | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | LPM Transaction Received Interrupt   |      |
	|      |          |     | (LPM_Int)                            |      |
	|      |          |     |                                      |      |
	|      |          |     | - Device Mode - This interrupt is    |      |
	|      |          |     |   asserted when the device receives  |      |
	|      |          |     |   an LPM transaction and responds    |      |
	|      |          |     |   with a non-ERRORed response.       |      |
	|      |          |     |                                      |      |
	|      |          |     | - Host Mode - This interrupt is      |      |
	|      |          |     |   asserted when the device responds  |      |
	|      |          |     |   to an LPM transaction with a       |      |
	|      |          |     |   non-ERRORed response or when the   |      |
	|      |          |     |   host core has completed LPM        |      |
	|      |          |     |   transactions for the programmed    |      |
	|      |          |     |   number of times (GLPMCFG.RetryCnt).|      |
	+------+----------+-----+--------------------------------------+------+
	| 28   | ConI\    | RWC | Write Behavior: One to clear         |      |
	|      | DStsChng |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | Connector ID Status Change           |      |
	|      |          |     | (ConIDStsChng)                       |      |
	|      |          |     |                                      |      |
	|      |          |     | The core sets this bit when there is |      |
	|      |          |     | a change in connector ID status.     |      |
	+------+----------+-----+--------------------------------------+------+
	| 29   | Di\      | RWC | Write Behavior: One to clear         |      |
	|      | sconnInt |     |                                      |      |
	|      |          |     | Mode: Host only                      |      |
	|      |          |     |                                      |      |
	|      |          |     | Disconnect Detected Interrupt        |      |
	|      |          |     | (DisconnInt)                         |      |
	|      |          |     |                                      |      |
	|      |          |     | Asserted when a device disconnect is |      |
	|      |          |     | detected.                            |      |
	+------+----------+-----+--------------------------------------+------+
	| 30   | Se\      | RWC | Write Behavior: One to clear         |      |
	|      | ssReqInt |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | Session Request/New Session Detected |      |
	|      |          |     | Interrupt (SessReqInt)               |      |
	|      |          |     |                                      |      |
	|      |          |     | In Host mode, this interrupt is      |      |
	|      |          |     | asserted when a session request is   |      |
	|      |          |     | detected from the device.            |      |
	|      |          |     |                                      |      |
	|      |          |     | In Device mode, this interrupt is    |      |
	|      |          |     | asserted when the utmisrp_bvalid     |      |
	|      |          |     | signal goes high.                    |      |
	+------+----------+-----+--------------------------------------+------+
	| 31   | WkUpInt  | RWC | Write Behavior: One to clear         |      |
	|      |          |     |                                      |      |
	|      |          |     | Mode: Host and Device                |      |
	|      |          |     |                                      |      |
	|      |          |     | Resume/Remote Wakeup Detected        |      |
	|      |          |     |                                      |      |
	|      |          |     | Interrupt (WkUpInt)                  |      |
	|      |          |     |                                      |      |
	|      |          |     | Wakeup Interrupt during Suspend(L2)  |      |
	|      |          |     | or LPM(L1) state.                    |      |
	|      |          |     |                                      |      |
	|      |          |     | - During Suspend (L2):               |      |
	|      |          |     |                                      |      |
	|      |          |     |   - Device Mode - This interrupt is  |      |
	|      |          |     |     asserted only when Host          |      |
	|      |          |     |     Initiated Resume is detected     |      |
	|      |          |     |     on USB.                          |      |
	|      |          |     |                                      |      |
	|      |          |     |   - Host Mode - This interrupt is    |      |
	|      |          |     |     asserted only when Device        |      |
	|      |          |     |     Initiated Remote Wakeup is       |      |
	|      |          |     |     detected on USB.                 |      |
	|      |          |     |                                      |      |
	|      |          |     | - During LPM (L1):                   |      |
	|      |          |     |                                      |      |
	|      |          |     |   - Device Mode - This interrupt is  |      |
	|      |          |     |     asserted for either Host         |      |
	|      |          |     |     Initiated Resume or Device       |      |
	|      |          |     |     Initiated Remote Wakeup on USB.  |      |
	|      |          |     |                                      |      |
	|      |          |     |   - Host Mode - This interrupt is    |      |
	|      |          |     |     asserted for either Host         |      |
	|      |          |     |     Initiated Resume or Device       |      |
	|      |          |     |     Initiated Remote Wakeup on USB.  |      |
	+------+----------+-----+--------------------------------------+------+

GINTMSK
```````

Interrupt Mask Register

.. _table_usb_gintmsk:
.. table:: GINTMSK, Offset Address: 0x018
	:widths: 1 2 1 4 1

	+------+------------+-----+------------------------------------+------+
	| Bits | Name       | Acc\| Description                        | R\   |
	|      |            | ess |                                    | eset |
	+======+============+=====+====================================+======+
	| 0    | Res\       | RO  | Reserved for future use.           |      |
	|      | erved_18_0 |     |                                    |      |
	|      |            |     | Shadow: Yes                        |      |
	|      |            |     |                                    |      |
	|      |            |     | Shadow Ctrl: vs_1t                 |      |
	|      |            |     |                                    |      |
	|      |            |     | Shadow Read Select: shrd_sel       |      |
	|      |            |     |                                    |      |
	|      |            |     | One-Way: Enabled                   |      |
	+------+------------+-----+------------------------------------+------+
	| 1    | ModeMisMsk | R/W | Mode: Host and Device              | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | Mode Mismatch Interrupt Mask       |      |
	|      |            |     | (ModeMisMsk)                       |      |
	|      |            |     |                                    |      |
	|      |            |     | Shadow: Yes                        |      |
	|      |            |     |                                    |      |
	|      |            |     | Shadow Ctrl: vs_1t                 |      |
	|      |            |     |                                    |      |
	|      |            |     | Shadow Read Select: shrd_sel       |      |
	+------+------------+-----+------------------------------------+------+
	| 2    | OTGIntMsk  | R/W | Mode: Host and Device              | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | OTG Interrupt Mask (OTGIntMsk)     |      |
	|      |            |     |                                    |      |
	|      |            |     | Shadow: Yes                        |      |
	|      |            |     |                                    |      |
	|      |            |     | Shadow Ctrl: vs_1t                 |      |
	|      |            |     |                                    |      |
	|      |            |     | Shadow Read Select: shrd_sel       |      |
	|      |            |     |                                    |      |
	|      |            |     | One-Way: Enabled                   |      |
	+------+------------+-----+------------------------------------+------+
	| 3    | SofMsk     | R/W | Mode: Host and Device              | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | Start of (micro)Frame Mask         |      |
	|      |            |     |                                    |      |
	|      |            |     | (SofMsk)                           |      |
	+------+------------+-----+------------------------------------+------+
	| 4    | RxFLvlMsk  | R/W | Mode: Host and Device              | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | Receive FIFO Non-Empty Mask        |      |
	|      |            |     | (RxFLvlMsk)                        |      |
	+------+------------+-----+------------------------------------+------+
	| 5    | N\         | R/W | Mode: Host and Device              | 0x0  |
	|      | PTxFEmpMsk |     |                                    |      |
	|      |            |     | Non-periodic TxFIFO Empty Mask     |      |
	|      |            |     | (NPTxFEmpMsk)                      |      |
	+------+------------+-----+------------------------------------+------+
	| 6    | GI\        | R/W | Mode: Device only                  | 0x0  |
	|      | NNakEffMsk |     |                                    |      |
	|      |            |     | Global Non-periodic IN NAK         |      |
	|      |            |     | Effective Mask (GINNakEffMsk)      |      |
	+------+------------+-----+------------------------------------+------+
	| 7    | GOU\       | R/W | Mode: Device only                  | 0x0  |
	|      | TNakEffMsk |     |                                    |      |
	|      |            |     | Global OUT NAK Effective Mask      |      |
	|      |            |     | (GOUTNakEffMsk)                    |      |
	+------+------------+-----+------------------------------------+------+
	| 8    | ULPI\      | R/W | ULPI Carkit Interrupt Mask         | 0x0  |
	|      | CKINTMsk_I\|     | (ULPICKINTMsk)                     |      |
	|      | 2CCKINTMsk |     |                                    |      |
	|      |            |     | Mode: Host and Device              |      |
	|      |            |     |                                    |      |
	|      |            |     | I2C Carkit Interrupt Mask          |      |
	|      |            |     | (I2CCKINTMsk)                      |      |
	|      |            |     |                                    |      |
	|      |            |     | Mode: Host and Device              |      |
	+------+------------+-----+------------------------------------+------+
	| 9    | I2CIntMsk  | R/W | Mode: Host and Device              | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | I2C Interrupt Mask (I2CIntMsk)     |      |
	+------+------------+-----+------------------------------------+------+
	| 10   | E\         | R/W | Mode: Device only                  | 0x0  |
	|      | rlySuspMsk |     |                                    |      |
	|      |            |     | Early Suspend Mask (ErlySuspMsk)   |      |
	+------+------------+-----+------------------------------------+------+
	| 11   | USBSuspMsk | R/W | Mode: Device only                  | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | USB Suspend Mask (USBSuspMsk)      |      |
	+------+------------+-----+------------------------------------+------+
	| 12   | USBRstMsk  | R/W | Mode: Device only                  | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | USB Reset Mask (USBRstMsk)         |      |
	+------+------------+-----+------------------------------------+------+
	| 13   | E\         | R/W | Mode: Device only                  | 0x0  |
	|      | numDoneMsk |     |                                    |      |
	|      |            |     | Enumeration Done Mask              |      |
	|      |            |     | (EnumDoneMsk)                      |      |
	+------+------------+-----+------------------------------------+------+
	| 14   | ISO\       | R/W | Mode: Device only Isochronous OUT  | 0x0  |
	|      | OutDropMsk |     | Packet Dropped Interrupt           |      |
	|      |            |     |                                    |      |
	|      |            |     | Mask (ISOOutDropMsk)               |      |
	+------+------------+-----+------------------------------------+------+
	| 15   | EOPFMsk    | R/W | Mode: Device only                  | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | End of Periodic Frame Interrupt    |      |
	|      |            |     | Mask (EOPFMsk)                     |      |
	+------+------------+-----+------------------------------------+------+
	| 16   | Rstr\      | R/W | Mode: Host and Device              | 0x0  |
	|      | DoneIntMsk |     |                                    |      |
	|      |            |     | Restore Done Interrupt Mask        |      |
	|      |            |     | (RstrDoneIntMsk)                   |      |
	|      |            |     |                                    |      |
	|      |            |     | This field is valid only when      |      |
	|      |            |     | Hibernation feature is enabled     |      |
	|      |            |     | (OTG_EN_PWROPT=2).                 |      |
	+------+------------+-----+------------------------------------+------+
	| 17   | EPMisMsk   | R/W | Mode: Device only                  | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | Endpoint Mismatch Interrupt Mask   |      |
	|      |            |     | (EPMisMsk)                         |      |
	+------+------------+-----+------------------------------------+------+
	| 18   | IEPIntMsk  | R/W | Mode: Device only                  | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | IN Endpoints Interrupt Mask        |      |
	|      |            |     | (IEPIntMsk)                        |      |
	+------+------------+-----+------------------------------------+------+
	| 19   | OEPIntMsk  | R/W | Mode: Device only                  | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | OUT Endpoints Interrupt Mask       |      |
	|      |            |     |                                    |      |
	|      |            |     | (OEPIntMsk)                        |      |
	+------+------------+-----+------------------------------------+------+
	| 20   | inco\      | R/W | Mode: Device only                  | 0x0  |
	|      | mpISOINMsk |     |                                    |      |
	|      |            |     | Incomplete Isochronous IN Transfer |      |
	|      |            |     | Mask (incompISOINMsk)              |      |
	|      |            |     |                                    |      |
	|      |            |     | This bit is enabled only when      |      |
	|      |            |     | device periodic endpoints are      |      |
	|      |            |     | enabled                            |      |
	|      |            |     | in Dedicated TxFIFO mode.          |      |
	+------+------------+-----+------------------------------------+------+
	| 21   | incompl\   | R/W | Incomplete Periodic Transfer Mask  | 0x0  |
	|      | PMsk_incom\|     | (incomplPMsk)                      |      |
	|      | pISOOUTMsk |     |                                    |      |
	|      |            |     | Mode: Host only                    |      |
	|      |            |     |                                    |      |
	|      |            |     | Incomplete Isochronous OUT         |      |
	|      |            |     | Transfer Mask (incompISOOUTMsk)    |      |
	|      |            |     |                                    |      |
	|      |            |     | Mode: Device only                  |      |
	+------+------------+-----+------------------------------------+------+
	| 22   | FetSuspMsk | R/W | Mode: Device only                  | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | Data Fetch Suspended Mask          |      |
	|      |            |     | (FetSuspMsk)                       |      |
	+------+------------+-----+------------------------------------+------+
	| 23   | R\         | R/W | Mode: Device only                  | 0x0  |
	|      | esetDetMsk |     |                                    |      |
	|      |            |     | Reset detected Interrupt Mask      |      |
	|      |            |     | (ResetDetMsk)                      |      |
	+------+------------+-----+------------------------------------+------+
	| 24   | PrtIntMsk  | R/W | Mode: Host only                    | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | Host Port Interrupt Mask           |      |
	|      |            |     | (PrtIntMsk)                        |      |
	+------+------------+-----+------------------------------------+------+
	| 25   | HChIntMsk  | R/W | Mode: Host only                    | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | Host Channels Interrupt Mask       |      |
	|      |            |     | (HChIntMsk)                        |      |
	+------+------------+-----+------------------------------------+------+
	| 26   | PTxFEmpMsk | R/W | Mode: Host only                    | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | Periodic TxFIFO Empty Mask         |      |
	|      |            |     | (PTxFEmpMsk)                       |      |
	+------+------------+-----+------------------------------------+------+
	| 27   | LPM_IntMsk | R/W | Mode: Host and Device              | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | LPM Transaction received interrupt |      |
	|      |            |     | Mask (LPM_IntMsk)                  |      |
	+------+------------+-----+------------------------------------+------+
	| 28   | ConID\     | R/W | Mode: Host and Device              | 0x0  |
	|      | StsChngMsk |     |                                    |      |
	|      |            |     | Connector ID Status Change Mask    |      |
	|      |            |     | (ConIDStsChngMsk)                  |      |
	+------+------------+-----+------------------------------------+------+
	| 29   | Dis\       | R/W | Mode: Host and Device              | 0x0  |
	|      | connIntMsk |     |                                    |      |
	|      |            |     | Disconnect Detected Interrupt Mask |      |
	|      |            |     | (DisconnIntMsk)                    |      |
	+------+------------+-----+------------------------------------+------+
	| 30   | Ses\       | R/W | Mode: Host and Device              | 0x0  |
	|      | sReqIntMsk |     |                                    |      |
	|      |            |     | Session Request/New Session        |      |
	|      |            |     | Detected Interrupt Mask            |      |
	|      |            |     | (SessReqIntMsk)                    |      |
	+------+------------+-----+------------------------------------+------+
	| 31   | WkUpIntMsk | R/W | Mode: Host and Device              | 0x0  |
	|      |            |     |                                    |      |
	|      |            |     | Resume/Remote Wakeup Detected      |      |
	|      |            |     | Interrupt Mask (WkUpIntMsk)        |      |
	|      |            |     |                                    |      |
	|      |            |     | The WakeUp bit is used for LPM     |      |
	|      |            |     | state wake up in a way similar to  |      |
	|      |            |     | that of wake up in suspend state.  |      |
	+------+------------+-----+------------------------------------+------+

GUID
````

User ID Register

.. _table_usb_guid:
.. table:: GUID, Offset Address: 0x03c
	:widths: 1 2 1 4 1

	+------+-----------+-------+------------------------------------+------+
	| Bits | Name      | Access     | Description                   | Reset|
	+======+===========+=======+====================================+======+
	| 31:0 | UserID    | R/W   | User ID (UserID)                   | 0x0  |
	|      |           |       |                                    |      |
	|      |           |       | Application-programmable ID field. |      |
	|      |           |       |                                    |      |
	|      |           |       | Reset: Configurable                |      |
	+------+-----------+-------+------------------------------------+------+

GLPMCFG
```````

Core LPM Configuration Register

.. _table_usb_glpmcfg_contd_0:
.. table:: GLPMCFG, Offset Address: 0x054
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 0    | LPMCap    | R/W | Mode: Host and Device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | LPM-Capable (LPMCap)                |      |
	|      |           |     |                                     |      |
	|      |           |     | The application uses this bit to    |      |
	|      |           |     | control the DWC_otg core LPM        |      |
	|      |           |     | capabilities.                       |      |
	|      |           |     |                                     |      |
	|      |           |     | If the core operates as a           |      |
	|      |           |     | non-LPM-capable host, it cannot     |      |
	|      |           |     | request the connected               |      |
	|      |           |     | device or hub to activate LPM mode. |      |
	|      |           |     |                                     |      |
	|      |           |     | If the core operates as a           |      |
	|      |           |     | non-LPM-capable device, it cannot   |      |
	|      |           |     | respond to any LPM                  |      |
	|      |           |     | transactions.                       |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1b0: LPM capability is not        |      |
	|      |           |     |   enabled                           |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1b1: LPM capability is enabled    |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is writable only if an LPM |      |
	|      |           |     | mode was specified for Mode of      |      |
	|      |           |     | Operation in                        |      |
	|      |           |     | coreConsultant (parameter           |      |
	|      |           |     | OTG_ENABLE_LPM). Otherwise, reads   |      |
	|      |           |     | return 0.                           |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 1    | AppL1Res  | R/W | Mode: Device only                   | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | LPM response programmed by          |      |
	|      |           |     | application (AppL1Res)              |      |
	|      |           |     |                                     |      |
	|      |           |     | Handshake response to LPM token     |      |
	|      |           |     | pre-programmed by device            |      |
	|      |           |     | application                         |      |
	|      |           |     | software. The response depends on   |      |
	|      |           |     | GLPMCFG.LPMCap. If GLPMCFG.LPMCap   |      |
	|      |           |     | is 1’b0, then the core always       |      |
	|      |           |     | responds with NYET response. If     |      |
	|      |           |     | GLPMCFG.LPMCap is 1'b1, the core    |      |
	|      |           |     | response is as follows.             |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1: ACK                            |      |
	|      |           |     |   Even though ACK is pre-programmed,|      |
	|      |           |     |   the core Device responds with ACK |      |
	|      |           |     |   only on successful LPM            |      |
	|      |           |     |   transaction.                      |      |
	|      |           |     |   The LPM transaction is successful |      |
	|      |           |     |   if:                               |      |
	|      |           |     |                                     |      |
	|      |           |     |   - No PID/CRC5 Errors in either EXT|      |
	|      |           |     |     token or LPM token (else ERROR) |      |
	|      |           |     |                                     |      |
	|      |           |     |   - Valid bLinkState = 0001B (L1)   |      |
	|      |           |     |     received in LPM transaction     |      |
	|      |           |     |     (else STALL)                    |      |
	|      |           |     |                                     |      |
	|      |           |     |   - No data pending in transmit     |      |
	|      |           |     |     queue (else NYET).              |      |
	|      |           |     |                                     |      |
	|      |           |     | - 0: NYET                           |      |
	|      |           |     |                                     |      |
	|      |           |     |   The pre-programmed software bit is|      |
	|      |           |     |   over-ridden for response to LPM   |      |
	|      |           |     |   token when:                       |      |
	|      |           |     |                                     |      |
	|      |           |     |   - The received bLinkState is not  |      |
	|      |           |     |     L1 (STALL response), or         |      |
	|      |           |     |                                     |      |
	|      |           |     |   - An error is detected in either  |      |
	|      |           |     |     of the LPM token packets because|      |
	|      |           |     |     of corruption (ERROR response). |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_glpmcfg_contd_1:
.. table:: GLPMCFG, Offset Address: 0x054 (continued)
	:widths: 1 2 1 6 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 5:2  | HIRD      | R/W | Mode: Host and Device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | - EnBESL = 1'b0                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   Host-Initiated Resume Duration    |      |
	|      |           |     |   (HIRD)                            |      |
	|      |           |     |                                     |      |
	|      |           |     |   Host Mode: The value of HIRD to   |      |
	|      |           |     |   be sent in an LPM transaction.    |      |
	|      |           |     |   This value is also used to        |      |
	|      |           |     |   initiate resume for a duration    |      |
	|      |           |     |   TL1HubDrvResume1 for host         |      |
	|      |           |     |   initiated resume.                 |      |
	|      |           |     |                                     |      |
	|      |           |     |   Device Mode (Read-Only): This     |      |
	|      |           |     |   field                             |      |
	|      |           |     |   is updated with the Received LPM  |      |
	|      |           |     |   Token HIRD bmAttribute when an    |      |
	|      |           |     |   ACK, NYET, or STALL response is   |      |
	|      |           |     |   sent to an LPM transaction.       |      |
	|      |           |     |                                     |      |
	|      |           |     |   Sl. No HIRD[3:0] THIRD (us)       |      |
	|      |           |     |                                     |      |
	|      |           |     |   1 4'b0000 50                      |      |
	|      |           |     |                                     |      |
	|      |           |     |   2 4'b0001 125                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   3 4'b0010 200                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   4 4'b0011 275                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   5 4'b0100 350                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   6 4'b0101 425                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   7 4'b0110 500                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   8 4'b0111 575                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   9 4'b1000 650                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   10 4'b1001 725                    |      |
	|      |           |     |                                     |      |
	|      |           |     |   11 4'b1010 800                    |      |
	|      |           |     |                                     |      |
	|      |           |     |   12 4'b1011 875                    |      |
	|      |           |     |                                     |      |
	|      |           |     |   13 4'b1100 950                    |      |
	|      |           |     |                                     |      |
	|      |           |     |   14 4'b1101 1025                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   15 4'b1110 1100                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   16 4'b1111 1175                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   Reset: 4'b0000                    |      |
	|      |           |     |                                     |      |
	|      |           |     | - EnBESL = 1'b1                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   Best Effort Service Latency       |      |
	|      |           |     |   (BESL)                            |      |
	|      |           |     |                                     |      |
	|      |           |     |   Host Mode: The value of BESL to be|      |
	|      |           |     |   sent in an LPM transaction. This  |      |
	|      |           |     |   value is                          |      |
	|      |           |     |   also used to initiate resume for a|      |
	|      |           |     |   duration TL1HubDrvResume1 for host|      |
	|      |           |     |   initiated                         |      |
	|      |           |     |   resume.                           |      |
	|      |           |     |                                     |      |
	|      |           |     |   Device Mode (Read-Only): This     |      |
	|      |           |     |   field                             |      |
	|      |           |     |   is updated with the Received LPM  |      |
	|      |           |     |   Token BESL bmAttribute when an    |      |
	|      |           |     |   ACK, NYET,                        |      |
	|      |           |     |   or STALL response is sent to      |      |
	|      |           |     |   an LPM transaction.               |      |
	|      |           |     |                                     |      |
	|      |           |     |   Sl. No BESL[3:0] TBESL (us)       |      |
	|      |           |     |                                     |      |
	|      |           |     |   1 4'b0000 125                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   2 4'b0001 150                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   3 4'b0010 200                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   4 4'b0011 300                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   5 4'b0100 400                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   6 4'b0101 500                     |      |
	|      |           |     |                                     |      |
	|      |           |     |   7 4'b0110 1000                    |      |
	|      |           |     |                                     |      |
	|      |           |     |   8 4'b0111 2000                    |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_glpmcfg_contd_2:
.. table:: GLPMCFG, Offset Address: 0x054 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	|      |           |     |   9 4'b1000 3000                    |      |
	|      |           |     |                                     |      |
	|      |           |     |   10 4'b1001 4000                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   11 4'b1010 5000                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   12 4'b1011 6000                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   13 4'b1100 7000                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   14 4'b1101 8000                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   15 4'b1110 9000                   |      |
	|      |           |     |                                     |      |
	|      |           |     |   16 4'b1111 10000                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 6    | bR\       | R/W | Mode: Host and Device               | 0x0  |
	|      | emoteWake |     |                                     |      |
	|      |           |     | RemoteWakeEnable (bRemoteWake)      |      |
	|      |           |     |                                     |      |
	|      |           |     | Host Mode: The value of remote wake |      |
	|      |           |     | up to be sent in the wIndex field   |      |
	|      |           |     | of LPM                              |      |
	|      |           |     | transaction.                        |      |
	|      |           |     |                                     |      |
	|      |           |     | Device Mode (Read-Only): This field |      |
	|      |           |     | is updated with the Received LPM    |      |
	|      |           |     | Token                               |      |
	|      |           |     | bRemoteWake bmAttribute when an     |      |
	|      |           |     | ACK, NYET, or STALL response is     |      |
	|      |           |     | sent to an                          |      |
	|      |           |     | LPM transaction.                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 7    | EnblSlpM  | R/W | Mode: Host and Device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Enable utmi_sleep_n (EnblSlpM)      |      |
	|      |           |     |                                     |      |
	|      |           |     | ULPI Interface: The application     |      |
	|      |           |     | uses this bit to control the        |      |
	|      |           |     | utmi_sleep_n                        |      |
	|      |           |     | assertion to the PHY when in L1     |      |
	|      |           |     | state. For the host, this bit is    |      |
	|      |           |     | valid only in “local                |      |
	|      |           |     | device” mode.                       |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1b0: utmi_sleep_n assertion from  |      |
	|      |           |     |   the core is not transferred to the|      |
	|      |           |     |   external PHY.                     |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1b1: utmi_sleep_n assertion from  |      |
	|      |           |     |   the core is transferred to the    |      |
	|      |           |     |   external PHY.                     |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: When a ULPI interface is      |      |
	|      |           |     | configured, enabling this bit       |      |
	|      |           |     | results in a write to Bit           |      |
	|      |           |     | 7 of the ULPI Function Control      |      |
	|      |           |     | register. The Synopsys ULPI PHY     |      |
	|      |           |     | supports writing                    |      |
	|      |           |     | to this bit, and in the L1 state    |      |
	|      |           |     | asserts SleepM when                 |      |
	|      |           |     | utmi_l1_suspend_n cannot be         |      |
	|      |           |     | asserted.                           |      |
	|      |           |     |                                     |      |
	|      |           |     | Other Interfaces: The application   |      |
	|      |           |     | uses this bit to control            |      |
	|      |           |     | utmi_sleep_n assertion              |      |
	|      |           |     | to the PHY in the L1 state. For the |      |
	|      |           |     | host, this bit is valid only in     |      |
	|      |           |     | Local Device mode.                  |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: utmi_sleep_n assertion from |      |
	|      |           |     |   the core is not transferred to the|      |
	|      |           |     |   external PHY.                     |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: utmi_sleep_n assertion from |      |
	|      |           |     |   the core is transferred to the    |      |
	|      |           |     |   external PHY                      |      |
	|      |           |     |   when utmi_l1_suspend_n cannot be  |      |
	|      |           |     |   asserted.                         |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_glpmcfg_contd_3:
.. table:: GLPMCFG, Offset Address: 0x054 (continued)
	:widths: 1 2 1 6 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 12:8 | H\        | R/W | Mode: Host and Device               | 0x0  |
	|      | IRD_Thres |     |                                     |      |
	|      |           |     | BESL or HIRD Threshold (HIRD_Thres) |      |
	|      |           |     |                                     |      |
	|      |           |     | Device Mode:                        |      |
	|      |           |     |                                     |      |
	|      |           |     | - EnBESL = 1'b0: The core puts the  |      |
	|      |           |     |   PHY into deep low power mode in   |      |
	|      |           |     |   L1 (by                            |      |
	|      |           |     |   core asserting L1SuspendM) when   |      |
	|      |           |     |   HIRD value is greater than or     |      |
	|      |           |     |   equal to the                      |      |
	|      |           |     |   value defined in this field       |      |
	|      |           |     |   HIRD_Thres[3:0] and HIRD_Thres[4] |      |
	|      |           |     |   is set to 1'b1.                   |      |
	|      |           |     |                                     |      |
	|      |           |     | - EnBESL = 1'b1: The core puts the  |      |
	|      |           |     |   PHY into deep low power mode in   |      |
	|      |           |     |   L1 (by                            |      |
	|      |           |     |   core asserting L1SuspendM) when   |      |
	|      |           |     |   BESL value is greater than or     |      |
	|      |           |     |   equal to the                      |      |
	|      |           |     |   value defined in this field       |      |
	|      |           |     |   BESL_Thres[3:0] and BESL_Thres[4] |      |
	|      |           |     |   is set to 1'b1.                   |      |
	|      |           |     |                                     |      |
	|      |           |     | - DCTL.DeepSleepBESLReject = 1'b1:  |      |
	|      |           |     |   In device initiated resume, the   |      |
	|      |           |     |   core                              |      |
	|      |           |     |   expects the Host to resume service|      |
	|      |           |     |   to the device within the BESL     |      |
	|      |           |     |   value corresponding to L1 exit    |      |
	|      |           |     |   time specified in                 |      |
	|      |           |     |   HIRD_Thresh[3:0]. The Device      |      |
	|      |           |     |   sends a NYET response when the    |      |
	|      |           |     |   received HIRD in LPM token is     |      |
	|      |           |     |   greater than                      |      |
	|      |           |     |   HIRD threshold.                   |      |
	|      |           |     |                                     |      |
	|      |           |     | - Note: To differentiate between    |      |
	|      |           |     |   Deep Sleep and Shallow sleep HIRD |      |
	|      |           |     |   greater                           |      |
	|      |           |     |   than or equal to HIRD threshold   |      |
	|      |           |     |   comparison is done. For           |      |
	|      |           |     |   differentiating                   |      |
	|      |           |     |   between NYET or ACK response for  |      |
	|      |           |     |   LPM token HIRD greater than HIRD  |      |
	|      |           |     |   Threshold comparison is used.     |      |
	|      |           |     |                                     |      |
	|      |           |     | Host Mode: The core puts the PHY    |      |
	|      |           |     | into deep low power mode in L1 (by  |      |
	|      |           |     | core                                |      |
	|      |           |     | asserting L1SuspendM) when          |      |
	|      |           |     | HIRD_Thres[4] is set to 1b1.        |      |
	|      |           |     | HIRD_Thres[3:0]                     |      |
	|      |           |     | specifies the time for which resume |      |
	|      |           |     | signaling is to be reflected by     |      |
	|      |           |     | host                                |      |
	|      |           |     | (TL1HubDrvResume2) on the USB bus   |      |
	|      |           |     | when it detects device initiated    |      |
	|      |           |     | resume.                             |      |
	|      |           |     |                                     |      |
	|      |           |     | HIRD_Thres must not be programmed   |      |
	|      |           |     | with a value greater than 4'b1100   |      |
	|      |           |     | in Host                             |      |
	|      |           |     | mode, because this exceeds maximum  |      |
	|      |           |     | TL1HubDrvResume2.                   |      |
	|      |           |     |                                     |      |
	|      |           |     | Sl. No ----Thres[3:0] --- -Host     |      |
	|      |           |     | Mode Resume Signaling Time (us)     |      |
	|      |           |     | --- - --- - --- - --- - --------- - |      |
	|      |           |     | --- - EnBESL = 1'b0 - -EnBESL =     |      |
	|      |           |     | 1'b1                                |      |
	|      |           |     |                                     |      |
	|      |           |     | 1 4'b0000 60 75                     |      |
	|      |           |     |                                     |      |
	|      |           |     | 2 4'b0001 135 100                   |      |
	|      |           |     |                                     |      |
	|      |           |     | 3 4'b0010 -210 150                  |      |
	|      |           |     |                                     |      |
	|      |           |     | 4 4'b0011 285 250                   |      |
	|      |           |     |                                     |      |
	|      |           |     | 5 4'b0100 360 350                   |      |
	|      |           |     |                                     |      |
	|      |           |     | 6 4'b0101 435 450                   |      |
	|      |           |     |                                     |      |
	|      |           |     | 7 4'b0110 510 950                   |      |
	|      |           |     |                                     |      |
	|      |           |     | 8 4'b0111 585 Invalid               |      |
	|      |           |     |                                     |      |
	|      |           |     | 9 4'b1000 660 Invalid               |      |
	|      |           |     |                                     |      |
	|      |           |     | 10 4'b1001 735 Invalid              |      |
	|      |           |     |                                     |      |
	|      |           |     | 11 4'b1010 810 Invalid              |      |
	|      |           |     |                                     |      |
	|      |           |     | 12 4'b1011 885 Invalid              |      |
	|      |           |     |                                     |      |
	|      |           |     | 13 4'b1100 960 Invalid              |      |
	|      |           |     |                                     |      |
	|      |           |     | 14 4'b1101 Invalid Invalid          |      |
	|      |           |     |                                     |      |
	|      |           |     | 15 4'b1110 Invalid Invalid          |      |
	|      |           |     |                                     |      |
	|      |           |     | 16 4'b1111 Invalid Invalid          |      |
	+------+-----------+-----+-------------------------------------+------+


To be continued ......

.. _table_usb_glpmcfg_contd_4:
.. table:: GLPMCFG, Offset Address: 0x054 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	|      |           |     | The following truth table explains  |      |
	|      |           |     | the difference in behavior between  |      |
	|      |           |     | the UTMI                            |      |
	|      |           |     | and ULPI interface in different     |      |
	|      |           |     | modes of operation:                 |      |
	|      |           |     |                                     |      |
	|      |           |     | Bit 7 --Bit 6 --sleep_n             |      |
	|      |           |     | ---l1_suspend_n --suspend_n ---Mode |      |
	|      |           |     | of Operation                        |      |
	|      |           |     |                                     |      |
	|      |           |     | 0 --- -----1- --- ----1--- ---      |      |
	|      |           |     | --1--- --- ------- --- --1--- ---   |      |
	|      |           |     | ------- --Normal Operation          |      |
	|      |           |     |                                     |      |
	|      |           |     | 0 --- -----0- --- ----1--- ---      |      |
	|      |           |     | --1--- --- ------- --- --0--- ---   |      |
	|      |           |     | ------- --L2 Suspend                |      |
	|      |           |     |                                     |      |
	|      |           |     | 1 --- -----0- --- ----1--- ---      |      |
	|      |           |     | --0--- --- ------- --- --1--- ---   |      |
	|      |           |     | ------- --L1 Deep Sleep             |      |
	|      |           |     |                                     |      |
	|      |           |     | 1 --- -----1- --- ----0--- ---      |      |
	|      |           |     | --1--- --- ------- --- --1--- ---   |      |
	|      |           |     | ------- --L1 Shallow Sleep          |      |
	+------+-----------+-----+-------------------------------------+------+
	| 14:13| CoreL1Res | RO  | Mode: Host and Device               |      |
	|      |           |     |                                     |      |
	|      |           |     | LPM Response (CoreL1Res)            |      |
	|      |           |     |                                     |      |
	|      |           |     | Device Mode: The response of the    |      |
	|      |           |     | core to LPM transaction received is |      |
	|      |           |     | reflected                           |      |
	|      |           |     | in these two bits.                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Host Mode: Handshake response       |      |
	|      |           |     | received from local device for LPM  |      |
	|      |           |     | transaction                         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 11 - ACK                          |      |
	|      |           |     | - 10 - NYET                         |      |
	|      |           |     | - 01 - STALL                        |      |
	|      |           |     | - 00 - ERROR (No handshake response)|      |
	+------+-----------+-----+-------------------------------------+------+
	| 15   | SlpSts    | RO  | Mode: Device only                   |      |
	|      |           |     |                                     |      |
	|      |           |     | Port Sleep Status (SlpSts)          |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is set as long as a Sleep  |      |
	|      |           |     | condition is present on the USB     |      |
	|      |           |     | bus. The core                       |      |
	|      |           |     | enters the Sleep state when an ACK  |      |
	|      |           |     | response is sent to an LPM          |      |
	|      |           |     | transaction and                     |      |
	|      |           |     | the TL1TokenRetry timer has         |      |
	|      |           |     | expired. To stop the PHY clock, the |      |
	|      |           |     | application must                    |      |
	|      |           |     | set the Port Clock Stop bit, which  |      |
	|      |           |     | asserts the PHY Suspend input       |      |
	|      |           |     | signal.                             |      |
	|      |           |     |                                     |      |
	|      |           |     | The application must rely on SlpSts |      |
	|      |           |     | and not ACK in CoreL1Res to confirm |      |
	|      |           |     | transition into sleep.              |      |
	|      |           |     |                                     |      |
	|      |           |     | The core comes out of sleep:        |      |
	|      |           |     |                                     |      |
	|      |           |     | - When there is any activity on the |      |
	|      |           |     |   USB linestate                     |      |
	|      |           |     |                                     |      |
	|      |           |     | - When the application writes to    |      |
	|      |           |     |   the Remote Wakeup Signaling bit   |      |
	|      |           |     |   in the Device                     |      |
	|      |           |     |                                     |      |
	|      |           |     | Control register (DCTL.RmtWkUpSig)  |      |
	|      |           |     | or when the application resets or   |      |
	|      |           |     | softdisconnects                     |      |
	|      |           |     | the device.                         |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_glpmcfg_contd_5:
.. table:: GLPMCFG, Offset Address: 0x054 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	|      |           |     | Host Mode: The host transitions to  |      |
	|      |           |     | Sleep (L1) state as a side-effect   |      |
	|      |           |     | of a                                |      |
	|      |           |     | successful LPM transaction by the   |      |
	|      |           |     | core to the local port with ACK     |      |
	|      |           |     | response from                       |      |
	|      |           |     | the device. The read value of this  |      |
	|      |           |     | bit reflects the current Sleep      |      |
	|      |           |     | status of the port.                 |      |
	|      |           |     |                                     |      |
	|      |           |     | The core clears this bit after:     |      |
	|      |           |     |                                     |      |
	|      |           |     | - The core detects a remote L1      |      |
	|      |           |     |   Wakeup signal,                    |      |
	|      |           |     |                                     |      |
	|      |           |     | - The application sets the Port     |      |
	|      |           |     |   Reset bit or the Port L1Resume bit|      |
	|      |           |     |   in the HPRT                       |      |
	|      |           |     |   register, or                      |      |
	|      |           |     |                                     |      |
	|      |           |     | - The application sets the          |      |
	|      |           |     |   L1Resume/ Remote Wakeup Detected  |      |
	|      |           |     |   Interrupt bit or                  |      |
	|      |           |     |   Disconnect Detected Interrupt bit |      |
	|      |           |     |   in the Core Interrupt register    |      |
	|      |           |     |   (GINTSTS.L1WkUpInt or             |      |
	|      |           |     |   GINTSTS.DisconnInt, respectively).|      |
	|      |           |     |                                     |      |
	|      |           |     | Values:                             |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1b0: Core not in L1               |      |
	|      |           |     | - 1b1: Core in L1                   |      |
	+------+-----------+-----+-------------------------------------+------+
	| 16   | L\        | RO  | Mode: Host and device               |      |
	|      | 1ResumeOK |     |                                     |      |
	|      |           |     | Sleep State Resume OK (L1ResumeOK)  |      |
	|      |           |     |                                     |      |
	|      |           |     | Indicates that the application or   |      |
	|      |           |     | host can start resume from Sleep    |      |
	|      |           |     | state. This bit is                  |      |
	|      |           |     | valid in LPM sleep (L1) state. It   |      |
	|      |           |     | is set in sleep mode after a delay  |      |
	|      |           |     | of 50 us                            |      |
	|      |           |     | (TL1Residency).                     |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is reset when SlpSts is 0. |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1b1: The application or core can  |      |
	|      |           |     |   start Resume from Sleep state     |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1b0: The application or core      |      |
	|      |           |     |   cannot start Resume from Sleep    |      |
	|      |           |     |   state                             |      |
	+------+-----------+-----+-------------------------------------+------+
	| 20:17| LPM_C\    | R/W | Mode: Host only                     | 0x0  |
	|      | hnl_Indx  |     |                                     |      |
	|      |           |     | LPM Channel Index (LPM_Chnl_Indx)   |      |
	|      |           |     |                                     |      |
	|      |           |     | The channel number on which the LPM |      |
	|      |           |     | transaction has to be applied while |      |
	|      |           |     | sending an LPM transaction to the   |      |
	|      |           |     | local device. Based on the LPM      |      |
	|      |           |     | channel index,                      |      |
	|      |           |     | the core automatically inserts the  |      |
	|      |           |     | device address and end point number |      |
	|      |           |     | programmed in the corresponding     |      |
	|      |           |     | channel into the LPM transaction.   |      |
	+------+-----------+-----+-------------------------------------+------+
	| 23:21| LPM_R\    | R/W | Mode: Host only                     | 0x0  |
	|      | etry_Cnt  |     |                                     |      |
	|      |           |     | LPM Retry Count (LPM_Retry_Cnt)     |      |
	|      |           |     |                                     |      |
	|      |           |     | When the device gives an ERROR      |      |
	|      |           |     | response, this is the number of     |      |
	|      |           |     | additional LPM                      |      |
	|      |           |     | retries that the host performs      |      |
	|      |           |     | until a valid device response       |      |
	|      |           |     | (STALL, NYET, or ACK)               |      |
	|      |           |     | is received.                        |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_glpmcfg_contd_6:
.. table:: GLPMCFG, Offset Address: 0x054 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 24   | SndLPM    | RWS | Write Behavior: One to set          |      |
	|      |           |     |                                     |      |
	|      |           |     | Mode: Host only                     |      |
	|      |           |     |                                     |      |
	|      |           |     | Send LPM Transaction (SndLPM)       |      |
	|      |           |     |                                     |      |
	|      |           |     | When the application software sets  |      |
	|      |           |     | this bit, an LPM transaction        |      |
	|      |           |     | containing two                      |      |
	|      |           |     | tokens, EXT and LPM is sent. The    |      |
	|      |           |     | hardware clears this bit once a     |      |
	|      |           |     | valid response                      |      |
	|      |           |     | (STALL, NYET, or ACK) is received   |      |
	|      |           |     | from the Device or the core has     |      |
	|      |           |     | finished                            |      |
	|      |           |     | transmitting the programmed number  |      |
	|      |           |     | of LPM retries.                     |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: This bit must be set only     |      |
	|      |           |     | when the host is connected to a     |      |
	|      |           |     | local port.                         |      |
	+------+-----------+-----+-------------------------------------+------+
	| 27:25| LPM_Ret\  | RO  | Mode: Host only                     |      |
	|      | ryCnt_Sts |     |                                     |      |
	|      |           |     | LPM Retry Count Status              |      |
	|      |           |     | (LPM_RetryCnt_Sts)                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Number of LPM Host Retries still    |      |
	|      |           |     | remaining to be transmitted for the |      |
	|      |           |     | current LPM                         |      |
	|      |           |     | sequence.                           |      |
	+------+-----------+-----+-------------------------------------+------+
	| 28   | EnBESL    | R/W | Mode: Host and device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Enable Best Effort Service Latency  |      |
	|      |           |     | (BESL)                              |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit enables the BESL feature   |      |
	|      |           |     | as defined in the LPM errata:       |      |
	|      |           |     |                                     |      |
	|      |           |     | - 11'b0: The core works as descri   |      |
	|      |           |     |   bed in the following document:    |      |
	|      |           |     |   USB 2.0 Link Power Management     |      |
	|      |           |     |   Addendum Engineering Change Notice|      |
	|      |           |     |   to                                |      |
	|      |           |     |   the USB 2.0 specification,        |      |
	|      |           |     |   July 16, 2007                     |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: The core works as per the   |      |
	|      |           |     |   LPM Errata                        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 29   | R\        | R/W | Mode: Device only                   | 0x0  |
	|      | strSlpSts |     |                                     |      |
	|      |           |     | Restore SlpSts (RstrSlpSts)         |      |
	|      |           |     |                                     |      |
	|      |           |     | When the application power-gates    |      |
	|      |           |     | the core (partial power-down or     |      |
	|      |           |     | hibernation),                       |      |
	|      |           |     | the application needs to program    |      |
	|      |           |     | this bit to restore the LPM status  |      |
	|      |           |     | in the core.                        |      |
	|      |           |     |                                     |      |
	|      |           |     | Based on the BESL value received    |      |
	|      |           |     | from the Host, the application      |      |
	|      |           |     | needs to                            |      |
	|      |           |     | program this bit during restore     |      |
	|      |           |     | process. The application should     |      |
	|      |           |     | program this bit                    |      |
	|      |           |     | depending on whether it decided to  |      |
	|      |           |     | put the core in Shallow Sleep       |      |
	|      |           |     | (Clock Gating                       |      |
	|      |           |     | Only) or Deep Sleep (Power Gating)  |      |
	|      |           |     | mode:                               |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: The application puts the    |      |
	|      |           |     |   core in Shallow Sleep mode based  |      |
	|      |           |     |   on the BESL                       |      |
	|      |           |     |   value from the Host.              |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: The application puts the    |      |
	|      |           |     |   core in Deep Sleep mode based on  |      |
	|      |           |     |   the BESL                          |      |
	|      |           |     |   value from the Host.              |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_glpmcfg_contd_7:
.. table:: GLPMCFG, Offset Address: 0x054 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 30   | HSICCon   | R/W | Mode: Host and device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | HSIC-Connect (HSICCon)              |      |
	|      |           |     |                                     |      |
	|      |           |     | The application must use this bit   |      |
	|      |           |     | The application must use this bit   |      |
	|      |           |     | to initiate the HSIC Attach         |      |
	|      |           |     | sequence.                           |      |
	|      |           |     |                                     |      |
	|      |           |     | Host Mode: Once this bit is set,    |      |
	|      |           |     | the Host Core configures to drive   |      |
	|      |           |     | HSIC Idle state                     |      |
	|      |           |     | (STROBE=1&DATA=0) on the bus. It    |      |
	|      |           |     | then waits for device to initiate   |      |
	|      |           |     | the HSIC                            |      |
	|      |           |     | Connect sequence.                   |      |
	|      |           |     |                                     |      |
	|      |           |     | Device Mode: Once this bit is set,  |      |
	|      |           |     | the Device Core waits for HSIC Idle |      |
	|      |           |     | linestate                           |      |
	|      |           |     | on the bus. After receiving the     |      |
	|      |           |     | Idle linestate it then initiates    |      |
	|      |           |     | the HSIC Connect.                   |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only if           |      |
	|      |           |     | OTG_ENABLE_HSIC = 1, if_sel_hsic =  |      |
	|      |           |     | 1, and InvSelHSIC                   |      |
	|      |           |     | = 0. Otherwise, it is read-only.    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31   | I\        | R/W | Mode: Host and device               | 0x0  |
	|      | nvSelHsic |     |                                     |      |
	|      |           |     | HSIC-Invert Select HSIC             |      |
	|      |           |     | (InvSelHsic)                        |      |
	|      |           |     |                                     |      |
	|      |           |     | The application uses this bit to    |      |
	|      |           |     | control the DWC_otg core HSIC       |      |
	|      |           |     | enable/disable.                     |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit overrides and functionally |      |
	|      |           |     | inverts the if_sel_hsic input port  |      |
	|      |           |     | signal.                             |      |
	|      |           |     |                                     |      |
	|      |           |     | If the core is non-HSIC-capable, it |      |
	|      |           |     | can connect to only PHYs that are   |      |
	|      |           |     | not HSIC                            |      |
	|      |           |     | capable.                            |      |
	|      |           |     |                                     |      |
	|      |           |     | If the core is HSIC-capable, it can |      |
	|      |           |     | connect only to PHYs that are HSIC  |      |
	|      |           |     | capable.                            |      |
	|      |           |     |                                     |      |
	|      |           |     | - If if_sel_hsic input signal is 1: |      |
	|      |           |     |                                     |      |
	|      |           |     |   - InvSelHsic = 1b1: HSIC          |      |
	|      |           |     |     capability is not enabled       |      |
	|      |           |     |                                     |      |
	|      |           |     |   - InvSelHsic = 1b0: HSIC          |      |
	|      |           |     |     capability is enabled           |      |
	|      |           |     |                                     |      |
	|      |           |     | - If if_sel_hsic input signal is 0: |      |
	|      |           |     |                                     |      |
	|      |           |     |   - InvSelHsic = 1b1: HSIC          |      |
	|      |           |     |     capability is enabled           |      |
	|      |           |     |                                     |      |
	|      |           |     |   - InvSelHsic = 1b0: HSIC          |      |
	|      |           |     |     capability is not enabled       |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is writable only if HSIC   |      |
	|      |           |     | mode is specified for Mode of       |      |
	|      |           |     | Operation in                        |      |
	|      |           |     | coreConsultant (parameter           |      |
	|      |           |     | OTG_ENABLE_HSIC). This bit is valid |      |
	|      |           |     | only if                             |      |
	|      |           |     | OTG_ENABLE_HSIC is enabled.         |      |
	|      |           |     | Otherwise, reads return 0.          |      |
	+------+-----------+-----+-------------------------------------+------+

GPWRDN
``````

Power Down Register

.. _table_usb_gpwrdn_contd_0:
.. table:: GPWRDN, Offset Address: 0x058
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 0    | PMUIntSel | R/W | Mode: Host and Device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | PMU Interrupt Select (PMUIntSel)    |      |
	|      |           |     | When the hibernation functionality  |      |
	|      |           |     | is selected (OTG_EN_PWROPT =        |      |
	|      |           |     | 2), a write to this bit with 1'b1   |      |
	|      |           |     | enables the PMU to generate         |      |
	|      |           |     | interrupts                          |      |
	|      |           |     | to the application. During this     |      |
	|      |           |     | state, all interrupts from the      |      |
	|      |           |     | DWC_otg_core module are blocked to  |      |
	|      |           |     | the application.                    |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: This bit must be set to 1'b1  |      |
	|      |           |     | before the core is put into         |      |
	|      |           |     | hibernation                         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Internal DWC_otg_core       |      |
	|      |           |     |   interrupt is selected             |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: External DWC_otg_pmu        |      |
	|      |           |     |   interrupt is selected             |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: This bit must not be written  |      |
	|      |           |     | to during normal mode of operation. |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	|      |           |     |                                     |      |
	|      |           |     | One-Way: Enabled                    |      |
	+------+-----------+-----+-------------------------------------+------+
	| 1    | PMUActv   | R/W | Mode: Host and Device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | PMU Active (PMUActv)                |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit enables or disables the    |      |
	|      |           |     | PMU logic.                          |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Disable PMU module          |      |
	|      |           |     | - 1'b1: Enable PMU module           |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: This bit must not be written  |      |
	|      |           |     | to during normal mode of operation. |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow: Yes                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Ctrl: vs_1t                  |      |
	|      |           |     |                                     |      |
	|      |           |     | Shadow Read Select: shrd_sel        |      |
	+------+-----------+-----+-------------------------------------+------+
	| 2    | Restore   | R/W | Mode: Host and Device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Restore                             |      |
	|      |           |     |                                     |      |
	|      |           |     | The application must program this   |      |
	|      |           |     | bit to enable or disable restore    |      |
	|      |           |     | mode from the PMU module.           |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: DWC_otg in normal mode of   |      |
	|      |           |     |   operation                         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: DWC_otg in restore mode     |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: This bit must not be written  |      |
	|      |           |     | to during normal mode of operation. |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | OTG_EN_PWROPT = 2.                  |      |
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

.. _table_usb_gpwrdn_contd_1:
.. table:: GPWRDN, Offset Address: 0x058 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 3    | PwrDnClmp | R/W | Mode: Host and Device               | 0x0  |
	|      |           |     |                                     |      |
	|      |           |     | Power Down Clamp (PwrDnClmp)        |      |
	|      |           |     |                                     |      |
	|      |           |     | The application must program this   |      |
	|      |           |     | bit to enable or disable the clamps |      |
	|      |           |     | to all the outputs of the DWC_otg   |      |
	|      |           |     | core module to prevent the          |      |
	|      |           |     | corruption of other active logic.   |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Disable PMU power clamp     |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: Enable PMU power clamp      |      |
	+------+-----------+-----+-------------------------------------+------+
	| 4    | P\        | R/W | Mode: Host and Device               | 0x1  |
	|      | wrDnRst_n |     |                                     |      |
	|      |           |     | Power Down ResetN (PwrDnRst_n)      |      |
	|      |           |     |                                     |      |
	|      |           |     | The application must program this   |      |
	|      |           |     | bit to reset the DWC_otg core       |      |
	|      |           |     | during the Hibernation exit process |      |
	|      |           |     | or during ADP when powering up      |      |
	|      |           |     | the core (if the DWC_otg core was   |      |
	|      |           |     | powered off during ADP process).    |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: DWC_otg is in normal        |      |
	|      |           |     |   operation                         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Reset DWC_otg               |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: This bit must not be written  |      |
	|      |           |     | to during normal mode of operation  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 5    | P\        | R/W | Mode: Host and Device               | 0x0  |
	|      | wrDnSwtch |     |                                     |      |
	|      |           |     | Power Down Switch (PwrDnSwtch)      |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit indicates to the DWC_otg   |      |
	|      |           |     | core whether the VDD switch is in   |      |
	|      |           |     | ON or OFF state.                    |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: DWC_otg is in ON state      |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: DWC_otg is in OFF state     |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: This bit must not be written  |      |
	|      |           |     | to during normal mode of operation. |      |
	+------+-----------+-----+-------------------------------------+------+
	| 6    | Di\       | R/W | Mode: Host and Device               | 0x0  |
	|      | sableVBUS |     |                                     |      |
	|      |           |     | DisableVBUS                         |      |
	|      |           |     |                                     |      |
	|      |           |     | Host Mode:                          |      |
	|      |           |     |                                     |      |
	|      |           |     | The application must program this   |      |
	|      |           |     | bit if HPRT0.PrtPwr was             |      |
	|      |           |     | programmed to 0 before switching    |      |
	|      |           |     | off the Core. This indicates to the |      |
	|      |           |     | PMU whether session was ended       |      |
	|      |           |     | before entering Hibernation.        |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: HPRT0.PrtPwr was not        |      |
	|      |           |     |   programed to 0.                   |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: HPRT0.PrtPwr was programmed |      |
	|      |           |     |   to 0.                             |      |
	|      |           |     |                                     |      |
	|      |           |     | Device Mode:                        |      |
	|      |           |     |                                     |      |
	|      |           |     | The application must program this   |      |
	|      |           |     | bit to inform the PMU whether the   |      |
	|      |           |     | bvalid valid signal is high         |      |
	|      |           |     | (session valid) or low (session     |      |
	|      |           |     | end)                                |      |
	|      |           |     | whenever the core is switched off.  |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: bvalid signal is High       |      |
	|      |           |     |   (Session Valid)                   |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: bvalid signal is Low        |      |
	|      |           |     |   (Session End)                     |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | GPWRDN.PMUActv is 1.                |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_gpwrdn_contd_2:
.. table:: GPWRDN, Offset Address: 0x058 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 7    | LnStsChng | RWC | Write Behavior: One to clear        |      |
	|      |           |     |                                     |      |
	|      |           |     | Mode: Host and Device               |      |
	|      |           |     |                                     |      |
	|      |           |     | Line State Change (LnStsChng)       |      |
	|      |           |     | This interrupt is asserted when     |      |
	|      |           |     | there is a linestate change         |      |
	|      |           |     | detected by                         |      |
	|      |           |     | the PMU. The application must read  |      |
	|      |           |     | GPWRDN.Linestate to determine       |      |
	|      |           |     | the current linestate on USB.       |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: No LineState change on USB  |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: LineState change on USB     |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | GPWRDN.PMUActv is 1 and             |      |
	|      |           |     | OTG_EN_PWROPT = 2.                  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 8    | LineStage\| R/W | Mode: Host and Device               | 0x0  |
	|      | ChangeMsk |     |                                     |      |
	|      |           |     | Mask For LineStateChange interrupt  |      |
	|      |           |     | (LineStageChangeMsk)                |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | OTG_EN_PWROPT = 2.                  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 9    | Rese\     | RWC | Write Behavior: One to clear        |      |
	|      | tDetected |     |                                     |      |
	|      |           |     | Mode: Device only                   |      |
	|      |           |     |                                     |      |
	|      |           |     | ResetDetected                       |      |
	|      |           |     |                                     |      |
	|      |           |     | This field indicates that Reset has |      |
	|      |           |     | been detected by the PMU module.    |      |
	|      |           |     |                                     |      |
	|      |           |     | This field generates an interrupt.  |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Reset Not Detected          |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: Reset Detected              |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | OTG_EN_PWROPT = 2.                  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 10   | Mask_Re\  | R/W | Mode: Device only                   | 0x0  |
	|      | setDetMsk |     |                                     |      |
	|      |           |     | Mask For ResetDetected interrupt    |      |
	|      |           |     | (ResetDetMsk)                       |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | OTG_EN_PWROPT = 2.                  |      |
	+------+-----------+-----+-------------------------------------+------+

To be continued ......

.. _table_usb_gpwrdn_contd_3:
.. table:: GPWRDN, Offset Address: 0x058 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 11   | Disconn\  | RWC | Write Behavior: One to clear        |      |
	|      | ectDetect |     |                                     |      |
	|      |           |     | Mode: Host only                     |      |
	|      |           |     |                                     |      |
	|      |           |     | DisconnectDetect                    |      |
	|      |           |     |                                     |      |
	|      |           |     | This field indicates that           |      |
	|      |           |     | Disconnect has been detected by the |      |
	|      |           |     | PMU.                                |      |
	|      |           |     |                                     |      |
	|      |           |     | This field generates an interrupt.  |      |
	|      |           |     | After detecting disconnect during   |      |
	|      |           |     | hibernation the application must    |      |
	|      |           |     | not restore the core, but instead   |      |
	|      |           |     | start                               |      |
	|      |           |     | the initialization process.         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Disconnect not detected     |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: Disconnect detected         |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | OTG_EN_PWROPT = 2.                  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 12   | D\        | R/W | Mode: Host only                     | 0x0  |
	|      | isconnect |     |                                     |      |
	|      | DetectMsk |     | Mask For DisconnectDetect Interrupt |      |
	|      |           |     | (DisconnectDetectMsk)               |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | OTG_EN_PWROPT = 2.                  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 13   | C\        | RO  | Mode: Host and Device               |      |
	|      | onnectDet |     |                                     |      |
	|      |           |     | Write Behavior: One to clear        |      |
	|      |           |     |                                     |      |
	|      |           |     | ConnectDet                          |      |
	|      |           |     |                                     |      |
	|      |           |     | This field indicates that a new     |      |
	|      |           |     | connect has been detected           |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: Connect not detected        |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: Connect detected            |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | OTG_EN_PWROPT = 2.                  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 14   | C\        | R/W | Mode: Host and Device               | 0x0  |
	|      | onnDetMsk |     |                                     |      |
	|      |           |     | ConnDetMsk                          |      |
	|      |           |     |                                     |      |
	|      |           |     | Mask for ConnectDet interrupt       |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | OTG_EN_PWROPT = 2.                  |      |
	+------+-----------+-----+-------------------------------------+------+
	| 15   | SRPDetect | RWC | Mode: Host only                     |      |
	|      |           |     |                                     |      |
	|      |           |     | SRPDetect                           |      |
	|      |           |     |                                     |      |
	|      |           |     | This field indicates that SRP has   |      |
	|      |           |     | been detected by the PMU. This      |      |
	|      |           |     | field                               |      |
	|      |           |     | generates an interrupt. After       |      |
	|      |           |     | detecting SRP during hibernation    |      |
	|      |           |     | the                                 |      |
	|      |           |     | application must not restore the    |      |
	|      |           |     | core. The application must get into |      |
	|      |           |     | the initialization process.         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: SRP not detected            |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: SRP detected                |      |
	+------+-----------+-----+-------------------------------------+------+


To be continued ......

.. _table_usb_gpwrdn_contd_4:
.. table:: GPWRDN, Offset Address: 0x058 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 16   | SRP\      | R/W | Mode: Host only                     | 0x0  |
	|      | DetectMsk |     |                                     |      |
	|      |           |     | Mask For SRPDetect Interrupt        |      |
	|      |           |     | (SRPDetectMsk)                      |      |
	+------+-----------+-----+-------------------------------------+------+
	| 17   | S\        | RWC | Write Behavior: One to clear        |      |
	|      | tsChngInt |     |                                     |      |
	|      |           |     | Status Change Interrupt             |      |
	|      |           |     | (StsChngInt)                        |      |
	|      |           |     |                                     |      |
	|      |           |     | This field indicates a status       |      |
	|      |           |     | change in either the IDDIG or       |      |
	|      |           |     | BSessVld                            |      |
	|      |           |     | signal.                             |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: No Status change            |      |
	|      |           |     | - 1'b1: status change detected      |      |
	|      |           |     |                                     |      |
	|      |           |     | After receiving this interrupt the  |      |
	|      |           |     | application must read the GPWRDN    |      |
	|      |           |     | register and interpret the change   |      |
	|      |           |     | in IDDIG or BSesVld with respect to |      |
	|      |           |     | the previous value stored by the    |      |
	|      |           |     | application.                        |      |
	|      |           |     |                                     |      |
	|      |           |     | Note: When Battery Charger is       |      |
	|      |           |     | Enabled and the ULPI interface is   |      |
	|      |           |     | used, if StsChngInt is received and |      |
	|      |           |     | the application reads GPWRDN        |      |
	|      |           |     | register and determines that it is  |      |
	|      |           |     | due to a change in the value of     |      |
	|      |           |     | IDDIG, then StsChngInt may be       |      |
	|      |           |     | generated once again within the     |      |
	|      |           |     | next                                |      |
	|      |           |     | few clock cycles.                   |      |
	|      |           |     |                                     |      |
	|      |           |     | This occurs because of an ambiguity |      |
	|      |           |     | in the implementation of Battery    |      |
	|      |           |     | Charger Support over the ULPI       |      |
	|      |           |     | interface. After receiving the      |      |
	|      |           |     | StsChngInt for the second time the  |      |
	|      |           |     | application can once again read     |      |
	|      |           |     | the GPWRDN register. However, this  |      |
	|      |           |     | time the value IDDIG (or            |      |
	|      |           |     | BSesVld) will not have changed. The |      |
	|      |           |     | application then processes the      |      |
	|      |           |     | second interrupt but no further     |      |
	|      |           |     | action will be required as a        |      |
	|      |           |     | result.                             |      |
	+------+-----------+-----+-------------------------------------+------+
	| 18   | StsC\     | R/W | Mode: Host and Device               | 0x0  |
	|      | hngIntMsk |     |                                     |      |
	|      |           |     | Mask For StsChng Interrupt          |      |
	|      |           |     | (StsChngIntMsk)                     |      |
	+------+-----------+-----+-------------------------------------+------+


To be continued ......

.. _table_usb_gpwrdn_contd_5:
.. table:: GPWRDN, Offset Address: 0x058 (continued)
	:widths: 1 2 1 4 1

	+------+-----------+-----+-------------------------------------+------+
	| Bits | Name      | Acc\| Description                         | R\   |
	|      |           | ess |                                     | eset |
	+======+===========+=====+=====================================+======+
	| 20:19| LineState | RO  | Mode: Host and Device               |      |
	|      |           |     |                                     |      |
	|      |           |     | LineState                           |      |
	|      |           |     |                                     |      |
	|      |           |     | This field indicates the current    |      |
	|      |           |     | linestate on USB as seen by the PMU |      |
	|      |           |     | module.                             |      |
	|      |           |     |                                     |      |
	|      |           |     | - 2'b00: DM = 0, DP = 0             |      |
	|      |           |     | - 2'b01: DM = 0, DP = 1             |      |
	|      |           |     | - 2'b10: DM = 1, DP = 0             |      |
	|      |           |     | - 2'b11: Not-defined                |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | GPWRDN.PMUActv is 1.                |      |
	+------+-----------+-----+-------------------------------------+------+
	| 21   | IDDIG     | RO  | Mode: Host and Device               |      |
	|      |           |     |                                     |      |
	|      |           |     | IDDIG                               |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit indicates the status of    |      |
	|      |           |     | the IDDIG signal. The application   |      |
	|      |           |     | must                                |      |
	|      |           |     | read this bit after receiving       |      |
	|      |           |     | GPWRDN.StsChngInt and decode based  |      |
	|      |           |     | on the previous value stored by the |      |
	|      |           |     | application.                        |      |
	|      |           |     |                                     |      |
	|      |           |     | Indicates the current mode.         |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b1: Device mode                 |      |
	|      |           |     | - 1'b0: Host mode                   |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | GPWRDN.PMUActv is 1.                |      |
	+------+-----------+-----+-------------------------------------+------+
	| 22   | BSessVld  | RO  | Mode: Device only                   |      |
	|      |           |     |                                     |      |
	|      |           |     | B Session Valid (BSessVld)          |      |
	|      |           |     |                                     |      |
	|      |           |     | This field reflects the B session   |      |
	|      |           |     | valid status signal from the PHY.   |      |
	|      |           |     |                                     |      |
	|      |           |     | - 1'b0: B-Valid is 0                |      |
	|      |           |     | - 1'b1: B-Valid is 1                |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is valid only when         |      |
	|      |           |     | GPWRDN.PMUActv is 1.                |      |
	+------+-----------+-----+-------------------------------------+------+
	| 23   | ADPInt    | RWC | Write Behavior: One to clear        |      |
	|      |           |     |                                     |      |
	|      |           |     | Mode: Host and Device               |      |
	|      |           |     |                                     |      |
	|      |           |     | ADP Interrupt (ADPInt)              |      |
	|      |           |     |                                     |      |
	|      |           |     | This bit is set whenever there is a |      |
	|      |           |     | ADP event                           |      |
	+------+-----------+-----+-------------------------------------+------+
	| 28:24| Mu\       | RO  | Mode: Host and Device               |      |
	|      | ltValIdBC |     |                                     |      |
	|      |           |     | MultValIdBC (MultValIdBC)           |      |
	|      |           |     |                                     |      |
	|      |           |     | Battery Charger ACA inputs in the   |      |
	|      |           |     | following order:                    |      |
	|      |           |     |                                     |      |
	|      |           |     | - Bit 28 - rid_float                |      |
	|      |           |     | - Bit 27 - rid_gnd                  |      |
	|      |           |     | - Bit 26 - rid_a                    |      |
	|      |           |     | - Bit 25 - rid_b                    |      |
	|      |           |     | - Bit 24 - rid_c                    |      |
	|      |           |     |                                     |      |
	|      |           |     | These bits are present only if      |      |
	|      |           |     | BC_SUPPORT = 1. Otherwise, these    |      |
	|      |           |     | bits are reserved and will read     |      |
	|      |           |     | 5'h0.                               |      |
	|      |           |     |                                     |      |
	|      |           |     | Reset: As per ACA input             |      |
	+------+-----------+-----+-------------------------------------+------+
	| 31:29| Reserved\ | RO  | Reserved for future use.            |      |
	|      | _58_31_29 |     |                                     |      |
	+------+-----------+-----+-------------------------------------+------+
