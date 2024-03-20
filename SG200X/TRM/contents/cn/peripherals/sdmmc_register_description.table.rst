SDMA_SADDR
^^^^^^^^^^

SDMA System Memory Address/ Argument2

.. _table_sdma_saddr:
.. table:: SDMA_SADDR, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | SDMA_SA              | R/W   | Physical system memory | 0x0  |
	|      |                      |       | address used for DMA   |      |
	|      |                      |       | transfer and the       |      |
	|      |                      |       | second argument for    |      |
	|      |                      |       | Auto CMD23             |      |
	+------+----------------------+-------+------------------------+------+


BLK_SIZE_AND_CNT
^^^^^^^^^^^^^^^^

Block Size and Block Count Register

.. _table_blk_size_and_cnt:
.. table:: BLK_SIZE_AND_CNT, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 11:0 | XFER_BLK_SIZE        | R/W   | Block Size of data     | 0x0  |
	|      |                      |       | transfer.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x1 : 1 byte         |      |
	|      |                      |       | - 0x2 : 2 bytes        |      |
	|      |                      |       | - \.\.\.\.\.\.         |      |
	|      |                      |       | - 0x200 : 512 bytes    |      |
	|      |                      |       | - \.\.\.\.\.\.         |      |
	|      |                      |       | - 0x800 : 2048 bytes   |      |
	+------+----------------------+-------+------------------------+------+
	| 14:12| SDMA_BUF_BDARY       | R/W   | Host SDMA buffer       | 0x0  |
	|      |                      |       | Boundary               |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0x0 ( 4K bytes)      |      |
	|      |                      |       | - 0x1 (8K bytes)       |      |
	|      |                      |       | - 0x2 (16K bytes)      |      |
	|      |                      |       | - 0x3 (32K bytes)      |      |
	|      |                      |       | - 0x4 (64K bytes)      |      |
	|      |                      |       | - 0x5 (128K bytes)     |      |
	|      |                      |       | - 0x6 (256K bytes)     |      |
	|      |                      |       | - 0x7 (512K bytes)     |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| BLK_CNT              | R/W   | Blocks Count for       | 0x0  |
	|      |                      |       | Current Transfer       |      |
	+------+----------------------+-------+------------------------+------+


ARGUMENT
^^^^^^^^

Argument 1 Register

.. _table_argument:
.. table:: ARGUMENT, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | ARGUMENT             | R/W   | Command Argument 1     | 0x0  |
	+------+----------------------+-------+------------------------+------+

XFER_MODE_AND_CMD
^^^^^^^^^^^^^^^^^

Transfer Mode and Command Register

.. _table_xfer_mode_and_cmd:
.. table:: XFER_MODE_AND_CMD, Offset Address: 0x00c
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | DMA_ENABLE           | R/W   | DMA enable             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : DMA Data Transfer  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : No data transfer   |      |
	|      |                      |       | or Non DMA data        |      |
	|      |                      |       | transfer               |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | BLK_CNT_ENABLE       | R/W   | Block Count Enable.    | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable the block count |      |
	|      |                      |       | regiser, which is only |      |
	|      |                      |       | relevant for multiple  |      |
	|      |                      |       | block transfers.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 3:2  | AUTO_CMD_ENABLE      | R/W   | Auto CMD enable.       | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | This field determines  |      |
	|      |                      |       | use of auto command    |      |
	|      |                      |       | funcitons              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : Auto command     |      |
	|      |                      |       | Disabled               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : Auto CMD12       |      |
	|      |                      |       | Enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : Auto CMD23       |      |
	|      |                      |       | Enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x3 : Reserved         |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | DAT_XFER_DIR         | R/W   | Data Transfer          | 0x0  |
	|      |                      |       | Direction Select       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Read ( card to     |      |
	|      |                      |       | host)                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Write ( host to    |      |
	|      |                      |       | card )                 |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | MULTI_BLK_SEL        | R/W   | Multi/single Block     | 0x0  |
	|      |                      |       | Select                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Multiple block     |      |
	|      |                      |       | transfer               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Single block       |      |
	|      |                      |       | transfer               |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | RESP_TYPE            | R/W   | Response Type R1/R5    | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : R1 (Memory)      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : R5 (SDIO)        |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | RESP_ERR_CHK_ENABLE  | R/W   | Response Error Check   | 0x0  |
	|      |                      |       | Enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | RESP_INT_DISABLE     | R/W   | Response Interrupt     | 0x0  |
	|      |                      |       | Disable                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Disable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Enable             |      |
	+------+----------------------+-------+------------------------+------+
	| 15:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 17:16| RESP_TYPE_SEL        | R/W   | Response Type Select   | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : No Response      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : Response Length  |      |
	|      |                      |       | 136                    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : Response Length  |      |
	|      |                      |       | 48                     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x3 : Response Length  |      |
	|      |                      |       | 48 with busy           |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | SUB_CMD_FLAG         | R/W   | Sub Command Flag       | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Sub Command        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Main Command       |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | CMD_CRC_CHK_ENABLE   | R/W   | Command CRC check      | 0x0  |
	|      |                      |       | enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_xfer_mode_and_cmd_2:
.. table:: XFER_MODE_AND_CMD, Offset Address: 0x00c (continued)
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 20   | CMD_IDX_CHK_ENABLE   | R/W   | Command Index Check    | 0x0  |
	|      |                      |       | Enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | DATA_PRESENT_SEL     | R/W   | Data Present Select.   | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | It is set to 0 for     |      |
	|      |                      |       | following :            |      |
	|      |                      |       |                        |      |
	|      |                      |       | (1) Commands using     |      |
	|      |                      |       | only CMD line (ex.     |      |
	|      |                      |       | CMD52)                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | (2) Commands with no   |      |
	|      |                      |       | data transfer but      |      |
	|      |                      |       | using busy signal on   |      |
	|      |                      |       | DAT0 ( ex. R1b)        |      |
	|      |                      |       |                        |      |
	|      |                      |       | (3) Resume command     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Data Present       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : No Data Present    |      |
	+------+----------------------+-------+------------------------+------+
	| 23:22| CMD_TYPE             | R/W   | Command Type           | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : Normal           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : Suspend ( CMD52  |      |
	|      |                      |       | for writing "Bus       |      |
	|      |                      |       | Suspend" in CCCR)      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : CMD52 for        |      |
	|      |                      |       | writing "Function      |      |
	|      |                      |       | Select" in CCCR)       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x3 : Abort ( CMD12,   |      |
	|      |                      |       | CMD52 for writing "I/O |      |
	|      |                      |       | Abort" in CCCR)        |      |
	+------+----------------------+-------+------------------------+------+
	| 29:24| CMD_IDX              | R/W   | Command Index          | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:30| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RESP31_0
^^^^^^^^

Response Bit 31-0 Regsiter

.. _table_resp31_0:
.. table:: RESP31_0, Offset Address: 0x010
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | RESP31_0             | RO    | Command Response for   |      |
	|      |                      |       | RSP[39:8]              |      |
	+------+----------------------+-------+------------------------+------+

RESP63_32
^^^^^^^^^

Response Bit 63-32 Regsiter

.. _table_resp63_32:
.. table:: RESP63_32, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | RESP63_32            | RO    | Command Response for   |      |
	|      |                      |       | RSP[71:40]             |      |
	+------+----------------------+-------+------------------------+------+

RESP95_64
^^^^^^^^^

Response Bit 95-64 Regsiter

.. _table_resp95_64:
.. table:: RESP95_64, Offset Address: 0x018
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | RESP95_64            | RO    | Command Response for   |      |
	|      |                      |       | RSP[103:72]            |      |
	+------+----------------------+-------+------------------------+------+

RESP127_96
^^^^^^^^^^

Response Bit 127-96 Regsiter

.. _table_resp127_96:
.. table:: RESP127_96, Offset Address: 0x01c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | RESP127_96           | RO    | Command Response for   |      |
	|      |                      |       | RSP[135:104]           |      |
	+------+----------------------+-------+------------------------+------+

BUF_DATA
^^^^^^^^

Buffer Data Port Register

.. _table_buf_data:
.. table:: BUF_DATA, Offset Address: 0x020
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | BUF_DATA             | R/W   | Buffer Data            | 0x0  |
	+------+----------------------+-------+------------------------+------+

PRESENT_STS
^^^^^^^^^^^

Present State Register

.. _table_present_sts:
.. table:: PRESENT_STS, Offset Address: 0x024
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | CMD_INHIBIT          | RO    | Command Inhibit (CMD)  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Cannot issue       |      |
	|      |                      |       | command                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Can issue command  |      |
	|      |                      |       | using only CMD line    |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | CMD_INHIBIT_DAT      | RO    | Command Inhibit (DAT)  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Cannot issue       |      |
	|      |                      |       | command wihich used    |      |
	|      |                      |       | the DAT line           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Can issue command  |      |
	|      |                      |       | using only DAT line    |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | DAT_LINE_ACTIVE      | RO    | DAT Line Active        |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit indicates     |      |
	|      |                      |       | whether one of the DAT |      |
	|      |                      |       | line on SD Bus is in   |      |
	|      |                      |       | use.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : DAT Line Active    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : DAT Line Inactive  |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | RE_TUNE_REQ          | RO    | Re-Tuning Request      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Sampling clock     |      |
	|      |                      |       | need re-tuning         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Fixed or well      |      |
	|      |                      |       | tuned sampling clock   |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | WR_XFER_ACTIVE       | RO    | Write Transfer Active  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Transferring data  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : No valid data      |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | RD_XFER_ACTIVE       | RO    | Read Transfer Active   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Transferring data  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : No valid data      |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | BUF_WR_ENABLE        | RO    | Buffer Write Enable    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | BUF_RD_ENABLE        | RO    | Buffer Read Enable     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | CARD_INSERTED        | RO    | Card Inserted          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Card Inserted      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Reset or           |      |
	|      |                      |       | Debouncing or No card  |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | CARD_STABLE          | RO    | Card State Stable      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : No Card or         |      |
	|      |                      |       | Inserted               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Reset or           |      |
	|      |                      |       | Debouncing             |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | CARD_CD_STS          | RO    | Card Detect Pin Level  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Card Present (     |      |
	|      |                      |       | SD_CD = 0)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : No Card Present    |      |
	|      |                      |       | (SD_CD = 1)            |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | CARD_WP_STS          | RO    | Write Protect Switch   |      |
	|      |                      |       | Pin Level              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Write enabled (    |      |
	|      |                      |       | SD_WP =0)              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Write protected    |      |
	|      |                      |       | (SD_WP = 1)            |      |
	+------+----------------------+-------+------------------------+------+
	| 23:20| DAT_3_0_STS          | RO    | DAT[3:0] Line Signal   |      |
	|      |                      |       | Level                  |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | CMD_LINE_STS         | RO    | CMD Line Signal Level  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:25| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

HOST_CTL1_PWR_BG_WUP
^^^^^^^^^^^^^^^^^^^^

Host Control 1 Register

.. _table_host_ctl1_pwr_bg_wup:
.. table:: HOST_CTL1_PWR_BG_WUP, Offset Address: 0x028
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | LEC_CTL              | R/W   | LED Control            | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | caution the user not   |      |
	|      |                      |       | to remove the card     |      |
	|      |                      |       | while the SD card is   |      |
	|      |                      |       | being accessed.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : LED on             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : LED off            |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | DAT_XFER_WIDTH       | R/W   | Data Transfer Width.   | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : 4-bit mode         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : 1-bit mode         |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | HS_ENABLE            | R/W   | High Speed Enable      | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : High Speed Enable  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Normal Speed       |      |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 4:3  | DMA_SEL              | R/W   | DMA Select.            | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : SDMA mode        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : Reserved         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : ADMA2            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x3 : ADMA2 or ADMA3   |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | EXT_DAT_WIDTH        | R/W   | Extended Data Transfer | 0x0  |
	|      |                      |       | Width                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : 8-bit mode         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Selected by        |      |
	|      |                      |       | DAT_XFER_WIDTH         |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | CRAD_DET_TEST        | R/W   | Card Detect Test Level | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Card Inserted      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : No card            |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | CARD_DET_SEL         | R/W   | Card Detect Signal     | 0x0  |
	|      |                      |       | Selection              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : CARD_DET_TEST is   |      |
	|      |                      |       | selected ( for test    |      |
	|      |                      |       | purpose)               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : SD_CD Is selected  |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | SD_BUS_PWR           | R/W   | SD Bus Power.          | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Power on           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Power off          |      |
	+------+----------------------+-------+------------------------+------+
	| 11:9 | SD_BUS_VOL_SEL       | R/W   | SD Bus Voltage Select  | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 111b : 3.3V            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 110b : 3.0V            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 101b : 1.8V            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 100b - 000b : Reserved |      |
	+------+----------------------+-------+------------------------+------+
	| 15:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | STOP_BG_REQ          | R/W   | Stop At Block Gap      | 0x0  |
	|      |                      |       | Request.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | stop executing read    |      |
	|      |                      |       | and write transaction  |      |
	|      |                      |       | at the next block gap  |      |
	|      |                      |       | for non-DMA, SDMA and  |      |
	|      |                      |       | ADMA transfers.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Stop               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Transfer           |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_host_ctl1_pwr_bg_wup_2:
.. table:: HOST_CTL1_PWR_BG_WUP, Offset Address: 0x028 (continued)
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 17   | CONTINUE_REQ         | R/W   | Continue Request.      | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | restart a transaction, |      |
	|      |                      |       | which was stoped using |      |
	|      |                      |       | the STOP_BG_REQ.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Restart            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Not affect         |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | READ_WAIT            | R/W   | Read Wait Control      | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable Read Wait   |      |
	|      |                      |       | Control                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable Read Wait  |      |
	|      |                      |       | Control                |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | INT_BG               | R/W   | Interrupt At Block Gap | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disabel            |      |
	+------+----------------------+-------+------------------------+------+
	| 23:20| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | WAKEUP_ON_CARD_INT   | R/W   | Wakeup Event Enable On | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Card Interrupt.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | W\                   | R/W   | Wakeup Event Enable On | 0x0  |
	|      | AKEUP_ON_CARD_INSERT |       | Card Insertion.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | WAKEUP_ON_CARD_REMV  | R/W   | Wakeup Event Enable On | 0x0  |
	|      |                      |       | Card Removal.          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:27| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CLK_CTL_SWRST
^^^^^^^^^^^^^

Clock and Timeout Control Register

.. _table_clk_ctl_swrst:
.. table:: CLK_CTL_SWRST, Offset Address: 0x02c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | INT_CLK_EN           | R/W   | Internal Clock Enable  | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Oscillate          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Stop               |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | INT_CLK_STABLE       | RO    | Internal Clock Stable. |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Ready              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Not Ready          |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | SD_CLK_EN            | R/W   | SD Clock Enable for    | 0x0  |
	|      |                      |       | Card                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | PLL_EN               | R/W   | PLL Enable             | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 5:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 7:6  | UP_FREQ_SEL          | R/W   | Upper Bits of SDCLK    | 0x0  |
	|      |                      |       | Frequency Select       |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | FREQ_SEL             | R/W   | SDCLK Frequency Select | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 19:16| TOUT_CNT             | R/W   | Data Timeout Counter   | 0x0  |
	|      |                      |       | Value                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : TMCLK x 2^13     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : TMCLK x 2^14     |      |
	|      |                      |       |                        |      |
	|      |                      |       | \.\.\.\.\.\.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0xe : TMCLK x 2^ 27    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0xf : Reserved         |      |
	+------+----------------------+-------+------------------------+------+
	| 23:20| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | SW_RST_ALL           | R/W   | Software Reset For All | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 25   | SW_RST_CMD           | R/W   | Software Reset For CMD | 0x0  |
	|      |                      |       | Line                   |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | SW_RST_DAT           | R/W   | Software Reset For     | 0x0  |
	|      |                      |       | DATA Line              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:27| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

NORM_AND_ERR_INT_STS
^^^^^^^^^^^^^^^^^^^^

Normal and Error Interrupt Status Register

.. _table_norm_and_err_int_sts:
.. table:: NORM_AND_ERR_INT_STS, Offset Address: 0x030
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | CMD_CMPL             | RWC   | Command Complete       |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | XFER_CMPL            | RWC   | Transfer Complete      |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | BG_EVENT             | RWC   | Block Gap Event        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | DMA_INT              | RWC   | DMA Interrupt          |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | BUF_WRDY             | RWC   | Buffer Write Ready     |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | BUF_RRDY             | RWC   | Buffer Read Ready      |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | CARD_INSERT_INT      | RWC   | Card Insertion         |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | CARD_REMOV_INT       | RWC   | Card Removal           |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | CARD_INT             | RO    | Card Interrupt         |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | INT_A                | RO    | INT_A.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | This status is set if  |      |
	|      |                      |       | INT_A is enabled and   |      |
	|      |                      |       | INT_A pin is in low    |      |
	|      |                      |       | level                  |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | INT_B                | RO    | INT_B.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | This status is set if  |      |
	|      |                      |       | INT_B is enabled and   |      |
	|      |                      |       | INT_B pin is in low    |      |
	|      |                      |       | level                  |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | INT_C                | RO    | INT_C.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | This status is set if  |      |
	|      |                      |       | INT_C is enabled and   |      |
	|      |                      |       | INT_C pin is in low    |      |
	|      |                      |       | level                  |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | RE_TUNE_EVENT        | RO    | Re-Tuning Event        |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | CQE_EVENT            | RO    | Command Queuing Event  |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | ERR_INT              | RO    | Error Interrupt        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | CMD_TOUT_ERR         | RWC   | Command Timeout Error  |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | CMD_CRC_ERR          | RWC   | Command CRC Error      |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | CMD_ENDBIT_ERR       | RWC   | Command End Bit Error  |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | CMD_IDX_ERR          | RWC   | Command Index Error    |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | DAT_TOUT_ERR         | RWC   | Data Timeout Error     |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | DAT_CRC_ERR          | RWC   | Data CRC Error         |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | DAT_ENDBIT_ERR       | RWC   | Data End Bit Error     |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | CURR_LIMIT_ERR       | RWC   | Current Limit Error    |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | AUTO_CMD_ERR         | RWC   | Auto Command Error     |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | ADMA_ERR             | RWC   | ADMA Error             |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | TUNE_ERR             | RWC   | Tuning Error           |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | BOOT_ACK_ERR         | RWC   |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:29| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

NORM_AND_ERR_INT_STS_EN
^^^^^^^^^^^^^^^^^^^^^^^

Normal and Error Interrupt Status Enable Register

.. _table_norm_and_err_int_sts_en:
.. table:: NORM_AND_ERR_INT_STS_EN, Offset Address: 0x034
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | CMD_CMPL_EN          | R/W   | Command Complete       | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | XFER_CMPL_EN         | R/W   | Transfer Complete      | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | BG_EVENT_EN          | R/W   | Block Gap Event Status | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | DMA_INT_EN           | R/W   | DMA Interrupt Status   | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | BUF_WRDY_EN          | R/W   | Buffer Write Ready     | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | BUF_RRDY_EN          | R/W   | Buffer Read Ready      | 0x0  |
	|      |                      |       | Status Enabel          |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | CARD_INSERT_INT_EN   | R/W   | Card Insertion Status  | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | CARD_REMOV_INT_EN    | R/W   | Card Removal Status    | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | CARD_INT_EN          | R/W   | Card Interrupt Status  | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | INT_A_EN             | R/W   | INT_A Status Enable.   | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 10   | INT_B_EN             | R/W   | INT_B Status Enable.   | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 11   | INT_C_EN             | R/W   | INT_C Status Enable.   | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 12   | RE_TUNE_EVENT_EN     | R/W   | Re-Tuning Event Status | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | CQE_EVENT_EN         | R/W   | Command Queuing Event  | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | ERR_INT_EN           | R/W   | Error Interrupt Status | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | CMD_TOUT_ERR_EN      | R/W   | Command Timeout Error  | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | CMD_CRC_ERR_EN       | R/W   | Command CRC Error      | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | CMD_ENDBIT_ERR_EN    | R/W   | Command End Bit Error  | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | CMD_IDX_ERR_EN       | R/W   | Command Index Error    | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | DAT_TOUT_ERR_EN      | R/W   | Data Timeout Error     | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | DAT_CRC_ERR_EN       | R/W   | Data CRC Error Status  | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | DAT_ENDBIT_ERR_EN    | R/W   | Data End Bit Error     | 0x0  |
	|      |                      |       | Statue Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | CURR_LIMIT_ERR_EN    | R/W   | Current Limit Error    | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | AUTO_CMD_ERR_EN      | R/W   | Auto Command Error     | 0x0  |
	|      |                      |       | Status Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | ADMA_ERR_EN          | R/W   | ADMA Error Status      | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | TUNE_ERR_EN          | R/W   | Tuning Error Status    | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | BOOT_ACK_ERR_EN      | R/W   | Boot Ack Error Status  | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:29| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

NORM_AND_ERR_INT_SIG_EN
^^^^^^^^^^^^^^^^^^^^^^^

Normal and Error Interrupt Signal Enable Register

.. _table_norm_and_err_int_sig_en:
.. table:: NORM_AND_ERR_INT_SIG_EN, Offset Address: 0x038
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | CMD_CMPL_SIG_EN      | R/W   | Command Complete       | 0x0  |
	|      |                      |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | XFER_CMPL_SIG_EN     | R/W   | Transfer Complete      | 0x0  |
	|      |                      |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | BG_EVENT_SIG_EN      | R/W   | Block Gap Event Signal | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | DMA_INT_SIG_EN       | R/W   | DMA Interrupt Signal   | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | BUF_WRDY_SIG_EN      | R/W   | Buffer Write Ready     | 0x0  |
	|      |                      |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | BUF_RRDY_SIG_EN      | R/W   | Buffer Read Ready      | 0x0  |
	|      |                      |       | Signal Enabel          |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | CA\                  | R/W   | Card Insertion Signal  | 0x0  |
	|      | RD_INSERT_INT_SIG_EN |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | C\                   | R/W   | Card Removal Signal    | 0x0  |
	|      | ARD_REMOV_INT_SIG_EN |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | CARD_INT_SIG_EN      | R/W   | Card Interrupt Signal  | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | INT_A_SIG_EN         | R/W   | INT_A Signal Enable.   | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 10   | INT_B_SIG_EN         | R/W   | INT_B Signal Enable.   | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 11   | INT_C_SIG_EN         | R/W   | INT_C Signal Enable.   | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 12   | RE_TUNE_EVENT_SIG_EN | R/W   | Re-Tuning EventSignal  | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | CQE_EVENT_SIG_EN     | R/W   | CQE EventSignal Enable | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 15   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | CMD_TOUT_ERR_SIG_EN  | R/W   | Command Timeout Error  | 0x0  |
	|      |                      |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | CMD_CRC_ERR_SIG_EN   | R/W   | Command CRC Error      | 0x0  |
	|      |                      |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | C\                   | R/W   | Command End Bit Error  | 0x0  |
	|      | MD_ENDBIT_ERR_SIG_EN |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | CMD_IDX_ERR_SIG_EN   | R/W   | Command Index Error    | 0x0  |
	|      |                      |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | DAT_TOUT_ERR_SIG_EN  | R/W   | Data Timeout Error     | 0x0  |
	|      |                      |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | DAT_CRC_ERR_SIG_EN   | R/W   | Data CRC Error Signal  | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | D\                   | R/W   | Data End Bit Error     | 0x0  |
	|      | AT_ENDBIT_ERR_SIG_EN |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | C\                   | R/W   | Current Limit Error    | 0x0  |
	|      | URR_LIMIT_ERR_SIG_EN |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | AUTO_CMD_ERR_SIG_EN  | R/W   | Auto Command Error     | 0x0  |
	|      |                      |       | Signal Enable          |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | ADMA_ERR_SIG_EN      | R/W   | ADMA Error Signal      | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | TUNE_ERR_SIG_EN      | R/W   | Tuning Error Signal    | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | BOOT_ACK_ERR_SIG_EN  | R/W   | Boot Ack Error Signal  | 0x0  |
	|      |                      |       | Enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:29| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

AUTO_CMD_ERR_AND_HOST_CTL2
^^^^^^^^^^^^^^^^^^^^^^^^^^

Auto CMD Error Status Register and Host Control 2 register

.. _table_auto_cmd_err_and_host_ctl2:
.. table:: AUTO_CMD_ERR_AND_HOST_CTL2, Offset Address: 0x03c
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | AUTO_CMD12_NO_EXE    | RO    | Auto CMD12 Not         |      |
	|      |                      |       | Executed               |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | AUTO_CMD_TOUT_ERR    | RO    | Auto CMD Timeout Error |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | AUTO_CMD_CRC_ERR     | RO    | Auto CMD CRC Error     |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | AUTO_CMD_ENDBIT_ERR  | RO    | Auto CMD End Bit Error |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | AUTO_CMD_IDX_ERR     | RO    | Auto CMD Index Error   |      |
	+------+----------------------+-------+------------------------+------+
	| 6:5  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | CM\                  | RO    | Command Not Issued By  |      |
	|      | D_NOT_ISSUE_BY_CMD12 |       | Auto CMD12 Error       |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 18:16| UHS_MODE_SEL         | R/W   | USH Speed Mode Select  | 0x0  |
	|      |                      |       | ( for SD)              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : SDR12            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : SDR25            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : SDR50            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x3 : SDR104           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x4 : DDR50            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x5 : Reserved         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x6 : Reserved         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x7 : Reserved         |      |
	|      |                      |       |                        |      |
	|      |                      |       | eMMC Speed Mode Select |      |
	|      |                      |       | ( for eMMC)            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : Default speed    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : High speed       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : Reserved         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x3 : HS200            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x4 : DDR52            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x5 : Reserved         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x6 : Reserved         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x7 : Reserved         |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | EN_18_SIG            | R/W   | 1.8V Signaling Enable  | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 21:20| DRV_SEL              | R/W   | Driver Strength Select | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : Driver Type B    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : Driver Type A    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : Driver Type C    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x3 : Driver Type D    |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | EXECUTE_TUNE         | R/W   | Execute Tuning         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Execute Tuning     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Not Tuned or       |      |
	|      |                      |       | Tuning Completed       |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | SAMPLE_CLK_SEL       | R/W   | Sampling Clock Select  | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Tuned clock is     |      |
	|      |                      |       | used to sample data    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Fixed clock is     |      |
	|      |                      |       | used to sample data    |      |
	+------+----------------------+-------+------------------------+------+
	| 29:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 30   | ASYNC_INT_EN         | R/W   | Asynchronous Interrupt | 0x0  |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | PRESET_VAL_ENABLE    | R/W   | Preset Value Enable    | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Automatic          |      |
	|      |                      |       | Selection by Preset    |      |
	|      |                      |       | Value are Enabled      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : SDLCK and Driver   |      |
	|      |                      |       | Strength are           |      |
	|      |                      |       | controlled by Host     |      |
	|      |                      |       | Driver                 |      |
	+------+----------------------+-------+------------------------+------+


CAPABILITIES1
^^^^^^^^^^^^^

Capabilities 1 Register

.. _table_capabilities1:
.. table:: CAPABILITIES1, Offset Address: 0x040
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 5:0  | TOUT_CLK_FREQ        | RO    | Timeout Clock          |      |
	|      |                      |       | Frequency              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Not 0 : 1KHz~ 63KHz or |      |
	|      |                      |       | 1Mhz~ 63Mhz            |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | TOUT_CLK_UNIT        | RO    | Timeout Clock Unit     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : 1MHz               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : 1KHz               |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | BASE_CLK_FREQ        | RO    | Base Clock Frequency   |      |
	|      |                      |       | for SD clock           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : Get information  |      |
	|      |                      |       | through another method |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : 1MHz             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : 2MHz             |      |
	|      |                      |       |                        |      |
	|      |                      |       | \.\.\.\.\.\.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0xFF : 255Mhz          |      |
	+------+----------------------+-------+------------------------+------+
	| 17:16| MAX_BLK_LEN          | RO    | Max Block Length       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : 512 (byte)       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : 1024             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : 2048             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x3 : Reserverd        |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | EMBEDDED_8BIT        | RO    | 8-bit Support for      |      |
	|      |                      |       | Embedded Device        |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | ADMA2_SUPPORT        | RO    | ADMA2 Support          |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | HS_SUPPORT           | RO    | High Speed Support     |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | SDMA_SUPPORT         | RO    | SDMA Support           |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | SUSP_RES_SUPPORT     | RO    | Suspend/Resume Support |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | V33_SUPPORT          | RO    | 3.3V Support           |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | V30_SUPPORT          | RO    | 3.0V Support           |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | V18_SUPPORT          | RO    | 1.8V Support           |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | BUS64_SUPPORT        | RO    | 64-bit System Bus      |      |
	|      |                      |       | Support                |      |
	+------+----------------------+-------+------------------------+------+
	| 29   | ASYNC_INT_SUPPORT    | RO    | Asynchronous Interrupt |      |
	|      |                      |       | Support                |      |
	+------+----------------------+-------+------------------------+------+
	| 31:30| SLOT_TYPE            | RO    | Slot Type              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : Removable Card   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : Embedded Slot    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : Shared Bus Slot  |      |
	+------+----------------------+-------+------------------------+------+

CAPABILITIES2
^^^^^^^^^^^^^

Capabilities 2 Register

.. _table_capabilities2:
.. table:: CAPABILITIES2, Offset Address: 0x044
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | SDR50_SUPPORT        | RO    | SDR50 Support          |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | SDR104_SUPPORT       | RO    | SDR104 Support         |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | DDR50_SUPPORT        | RO    | DDR50 Support          |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | DRV_A_SUPPORT        | RO    | Driver Type A Support  |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | DRV_C_SUPPORT        | RO    | Driver Type C Support  |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | DRV_D_SUPPORT        | RO    | Driver Type D Support  |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 11:8 | RETUNE_TIMER         | RO    | Timer Count for        |      |
	|      |                      |       | Re-Tuning              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : Disable          |      |
	|      |                      |       |                        |      |
	|      |                      |       | n : 2^(n-1) seconds    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0xB : 1024 seconds     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0xC ~ 0xE : Reserved   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0xF : Get Information  |      |
	|      |                      |       | from other source      |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | TUNE_SDR50           | RO    | Use Tuning for SDR50   |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| RETUNE_MODE          | RO    | Re-Tuning Modes        |      |
	+------+----------------------+-------+------------------------+------+
	| 23:16| CLK_MULTIPLIER       | RO    | Clock Multiplier       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

FORCE_EVENT_ERR
^^^^^^^^^^^^^^^

Force Event Register for Auto CMD Error Status

.. _table_force_event_err:
.. table:: CAPABILITIES2, Offset Address: 0x050
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | FORC\                | R/W   | Force Event for Auto   | 0x0  |
	|      | E_AUTO_CMD12_NOT_EXE |       | CMD12 Not Executed     |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | FOR\                 | R/W   | Force Event for Auto   | 0x0  |
	|      | CE_AUTO_CMD_TOUT_ERR |       | CMD Timeout Error      |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | FO\                  | R/W   | Force Event for Auto   | 0x0  |
	|      | RCE_AUTO_CMD_CRC_ERR |       | CMD CRC Error          |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | FOR\                 | R/W   | Force Event for Auto   | 0x0  |
	|      | CE_AUTO_CMD_EBIT_ERR |       | CMD End Bit Error      |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | FO\                  | R/W   | Force Event for Auto   | 0x0  |
	|      | RCE_AUTO_CMD_IDX_ERR |       | CMD Index Error        |      |
	+------+----------------------+-------+------------------------+------+
	| 6:5  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | FORC\                | R/W   | Force Event for        | 0x0  |
	|      | E_AUTO_CMD_NOT_ISSUE |       | Command Not Issued By  |      |
	|      |                      |       | Auto CMD12 Error       |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | FORCE_CMD_TOUT_ERR   | R/W   | Force Event for Auto   | 0x0  |
	|      |                      |       | CMD12 Not Executed     |      |
	+------+----------------------+-------+------------------------+------+
	| 17   | FORCE_CMD_CRC_ERR    | R/W   | Force Event for CMD    | 0x0  |
	|      |                      |       | Timeout Error          |      |
	+------+----------------------+-------+------------------------+------+
	| 18   | FORCE_CMD_EBIT_ERR   | R/W   | Force Event for CMD    | 0x0  |
	|      |                      |       | End Bit Error          |      |
	+------+----------------------+-------+------------------------+------+
	| 19   | FORCE_CMD_IDX_ERR    | R/W   | Force Event for CMD    | 0x0  |
	|      |                      |       | Index Error            |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | FORCE_DAT_TOUT_ERR   | R/W   | Force Event for DATA   | 0x0  |
	|      |                      |       | Timeout Error          |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | FORCE_DAT_CRC_ERR    | R/W   | Force Event for DATA   | 0x0  |
	|      |                      |       | End Bit Error          |      |
	+------+----------------------+-------+------------------------+------+
	| 22   | FORCE_DAT_EBIT_ERR   | R/W   | Force Event for DATA   | 0x0  |
	|      |                      |       | Index Error            |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | FORCE_CURR_LIMIT_ERR | R/W   | Force Event for        | 0x0  |
	|      |                      |       | current limit error    |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | FORCE_AUTO_CMD_ERR   | R/W   | Force Event for Auto   | 0x0  |
	|      |                      |       | CMD Error              |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | FORCE_ADMA_ERR       | R/W   | Force Event for ADMA   | 0x0  |
	|      |                      |       | Error                  |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | FORCE_TUNING_ERR     | R/W   | Force Event for Tuning | 0x0  |
	|      |                      |       | Error                  |      |
	+------+----------------------+-------+------------------------+------+
	| 27   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 28   | FORCE_BOOT_ACK_ERR   | R/W   | Force Event for        | 0x0  |
	|      |                      |       | Response Error         |      |
	+------+----------------------+-------+------------------------+------+
	| 31:29| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

ADMA_ERR_STS
^^^^^^^^^^^^

ADMA Error Status Register

.. _table_adma_err_sts:
.. table:: ADMA_ERR_STS, Offset Address: 0x054
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 1:0  | ADMA_ERR_STS         | RO    | ADMA Error Status      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x0 : ST_STOP ( Stop   |      |
	|      |                      |       | DMA)                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x1 : ST_FDS ( Fetch   |      |
	|      |                      |       | Descriptor)            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x2 : Never set this   |      |
	|      |                      |       | state                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0x3 : ST_TFR (         |      |
	|      |                      |       | transfer data)         |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | ADMA_LEN_MISMATCH    | RO    | ADMA Length Mismatch   |      |
	|      |                      |       | Error                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:3 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

ADMA_SADDR_L
^^^^^^^^^^^^

ADMA System Address Register for low 32-bit

.. _table_adma_saddr_l:
.. table:: ADMA_SADDR_L, Offset Address: 0x058
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | ADMA_SA_L            | R/W   | ADMA System Address    | 0x0  |
	|      |                      |       | for low 32-bit         |      |
	+------+----------------------+-------+------------------------+------+

ADMA_SADDR_H
^^^^^^^^^^^^

ADMA System Address Register for high 32-bit

.. _table_adma_saddr_h:
.. table:: ADMA_SADDR_H, Offset Address: 0x05c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | ADMA_SA_H            | R/W   | ADMA System Address    | 0x0  |
	|      |                      |       | for high 32-bit        |      |
	+------+----------------------+-------+------------------------+------+

PRESENT_VUL_INIT_DS
^^^^^^^^^^^^^^^^^^^

Present Value Register for Initialization and Default Speed

.. _table_present_vul_init_ds:
.. table:: PRESENT_VUL_INIT_DS, Offset Address: 0x060
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | PRESENT_VUL_INIT_DS  | RO    | Present Value Register |      |
	|      |                      |       | for Initialization and |      |
	|      |                      |       | Default Speed          |      |
	+------+----------------------+-------+------------------------+------+

PRESENT_VUL_HS_SDR12
^^^^^^^^^^^^^^^^^^^^

Present Value Register for High-speed and SDR12

.. _table_present_vul_hs_sdr12:
.. table:: PRESENT_VUL_HS_SDR12, Offset Address: 0x064
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | PRESENT_VUL_HS_SDR12 | RO    | Present Value Register |      |
	|      |                      |       | for High-speed and     |      |
	|      |                      |       | SDR12                  |      |
	+------+----------------------+-------+------------------------+------+

PRESENT_VUL_SDR25_SDR50
^^^^^^^^^^^^^^^^^^^^^^^

Present Value Register for SDR25 and SDR50

.. _table_present_vul_sdr25_sdr50:
.. table:: PRESENT_VUL_SDR25_SDR50, Offset Address: 0x068
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | PRE\                 | RO    | Present Value Register |      |
	|      | SENT_VUL_SDR25_SDR50 |       | for SDR25 and SDR50    |      |
	+------+----------------------+-------+------------------------+------+

PRESENT_VUL_SDR104_DDR50
^^^^^^^^^^^^^^^^^^^^^^^^

Present Value Register for SDR104 and DDR50

.. _table_present_vul_sdr104_ddr50:
.. table:: PRESENT_VUL_SDR104_DDR50, Offset Address: 0x06c
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | PRES\                | RO    | Present Value Register |      |
	|      | ENT_VUL_SDR104_DDR50 |       | for SDR104 and DDR50   |      |
	+------+----------------------+-------+------------------------+------+

SLOT_INT_AND_HOST_VER
^^^^^^^^^^^^^^^^^^^^^

Slot Interrupt Status and Host Controller Version Register

.. _table_slot_int_and_host_ver:
.. table:: SLOT_INT_AND_HOST_VER, Offset Address: 0x0fc
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 7:0  | INT_SLOT             | RO    | Interrupt Signal for   |      |
	|      |                      |       | Each Slot              |      |
	+------+----------------------+-------+------------------------+------+
	| 15:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 23:16| SPEC_VER             | RO    | Specification Version  |      |
	|      |                      |       | Number                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 00h : SD Host 1.00     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 01h : SD Host 2.00     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 02h : SD Host 3.00     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 03h : SD Host 4.00     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 04h : SD Host 4.10     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 05h : SD Host 4.20     |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| VENDOR_VER           | RO    | Verdor Version Number  |      |
	+------+----------------------+-------+------------------------+------+

EMMC_CTRL
^^^^^^^^^

MSHC Control register

.. _table_emmc_ctrl:
.. table:: EMMC_CTRL, Offset Address: 0x200
	:widths: 1 3 1 4 1


	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | EMMC_FUNC_EN         | R/W   | eMMC Card present      | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 1    | LATANCY_1T           | R/W   | Latancy 1t for cmd in  | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 2    | CLK_FREE_EN          | R/W   | Internal clock gating  | 0x0  |
	|      |                      |       | disable control        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | DISABLE_DATA_CRC_CHK | R/W   | Disable Data CRC Check | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | EMMC_RSTN            | R/W   | EMMC Device Reset      | 0x1  |
	|      |                      |       | Signal control         |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | EMMC_RSTN_OEN        | R/W   | Output Enable control  | 0x1  |
	|      |                      |       | for EMMC Device Reset  |      |
	|      |                      |       | Signal PAD             |      |
	+------+----------------------+-------+------------------------+------+
	| 11:10| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | CQE_ALGO_SEL         | R/W   | Scheduler algorithm    | 0x0  |
	|      |                      |       | selected for execution |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : First come First   |      |
	|      |                      |       | serve ( FCFS_ONLY)     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Priority based     |      |
	|      |                      |       | reordering with FCFS   |      |
	|      |                      |       | (                      |      |
	|      |                      |       | PRI_REORDER_PLUS_FCFS) |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | CQE_PREFETCH_DISABLE | R/W   | Enable or Disable      | 0x0  |
	|      |                      |       | CQE's PREFETCH Feature |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Disable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Enable             |      |
	+------+----------------------+-------+------------------------+------+
	| 15:14| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | timer_clk_sel        | R/W   | timer clock source     | 0x0  |
	|      |                      |       | selection              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : 32K                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : 100K               |      |
	+------+----------------------+-------+------------------------+------+
	| 31:17| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


EMMC_BOOT_CTL
^^^^^^^^^^^^^

eMMC Boot Control Register

.. _table_emmc_boot_ctl:
.. table:: EMMC_BOOT_CTL, Offset Address: 0x204
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | BOOT_MODE_ENABLE     | R/W   | Mandatory Boot Enable  | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 1    | BOOT_ACK_ENABLE      | R/W   | Boot Ack Enable        | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 3:2  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | BOOT_TOUT_CNT        | R/W   | Boot Ack Timeout       | 0x0  |
	|      |                      |       | Counter Value          |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | VALIDATE_BOOT        | W     | Validate Mandatory     |      |
	|      |                      |       | Boot Enable Bit        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CDET_TOUT_CTL
^^^^^^^^^^^^^

Card Detect Control Register

.. _table_cdet_tout_ctl:
.. table:: CDET_TOUT_CTL, Offset Address: 0x208
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 15:0 | CDET_DEBUUNCE_CNT    | R/W   | card detect debounce   | 0x   |
	|      |                      |       | counter                | 000F |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

MBIU_CTRL
^^^^^^^^^

MBIU Control register

.. _table_mbiu_ctrl:
.. table:: MBIU_CTRL, Offset Address: 0x20c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | UNDEFL_INCR_EN       | R/W   | Undefined INCR Burst   | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 1    | BURST_INCR4_EN       | R/W   | INCR4 Burst            | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 2    | BURST_INCR8_EN       | R/W   | INCR8 Burst            | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 3    | BURST_INCR16_EN      | R/W   | INCR16 Burst           | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PHY_TX_RX_DLY
^^^^^^^^^^^^^

MBIU Control register

.. _table_phy_tx_rx_dly:
.. table:: PHY_TX_RX_DLY, Offset Address: 0x240
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 6:0  | PHY_TX_DLY           | R/W   | PHY tx delay line      | 0x0  |
	|      |                      |       | phase selection        |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 9:8  | PHY_TX_SRC           | R/W   | PHY tx delay line      | 0x0  |
	|      |                      |       | clock source selection |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2'b00 : clk_tx         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2'b01 : inverse of     |      |
	|      |                      |       | clk_tx                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2'b1x : reserved       |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | PHY_TX_EVEN_ODD      | R/W   | PHY tx delay line      | 0x0  |
	|      |                      |       | clock source selection |      |
	+------+----------------------+-------+------------------------+------+
	| 15:11| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 22:16| PHY_RX_DLY           | R/W   | PHY rx delay line      | 0x0  |
	|      |                      |       | phase selection        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2'b00 : clk_tx         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2'b01 : inverse of     |      |
	|      |                      |       | clk_tx                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2'b1x : reserved       |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 25:24| PHY_RX_SRC           | R/W   | PHY rx delay line      | 0x0  |
	|      |                      |       | clock source selection |      |
	+------+----------------------+-------+------------------------+------+
	| 26   | PHY_RX_EVEN_ODD      | R/W   | PHY rx delay line      | 0x0  |
	|      |                      |       | clock source selection |      |
	+------+----------------------+-------+------------------------+------+
	| 31:27| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PHY_DS_DLY
^^^^^^^^^^

PHY DS delay line register

.. _table_phy_ds_dly:
.. table:: PHY_DS_DLY, Offset Address: 0x244
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 6:0  | PHY_DS_DLY           | R/W   | PHY DS delay line      | 0x0  |
	|      |                      |       | phase selection        |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 9:8  | PHY_DS_SRC           | R/W   | PHY DS delay line      | 0x0  |
	|      |                      |       | clock source selection |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | PHY_DS_EVEN_ODD      | R/W   | PHY DS delay line      | 0x0  |
	|      |                      |       | clock source selection |      |
	+------+----------------------+-------+------------------------+------+
	| 31:11| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PHY_DLY_STS
^^^^^^^^^^^

PHY delay line status register

.. _table_phy_dly_sts:
.. table:: PHY_DLY_STS, Offset Address: 0x248
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | PHY_TX_LEAD_LAG      | RO    | PHY tx delay line lead |      |
	|      |                      |       | or lag flag            |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | PHY_RX_LEAD_LAG      | RO    | PHY rx delay line lead |      |
	|      |                      |       | or lag flag            |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | PHY_DS_LEAD_LAG      | RO    | PHY ds delay line lead |      |
	|      |                      |       | or lag flag            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:3 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

PHY_CONFIG
^^^^^^^^^^

PHY Configuration register

.. _table_phy_config:
.. table:: PHY_CONFIG, Offset Address: 0x24c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | PHY_TX_BPS           | R/W   | PHY tx data path       | 0x1  |
	|      |                      |       | bypass enable          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Pipe enable        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Bypass             |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | ADJ_TIMING_EN        | R/W   | Adjust bus timing      | 0x0  |
	|      |                      |       | enable                 |      |
	+------+----------------------+-------+------------------------+------+
	| 7:2  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 9:8  | ADJ_NCR              | R/W   | Adjust NCR counter     | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 11:10| ADJ_NCRC             | R/W   | Adjust NCRC counter    | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
