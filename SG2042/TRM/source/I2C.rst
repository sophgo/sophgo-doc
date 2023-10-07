I2C
===

Registers
---------

This section describes the programmable registers of the DW_apb_i2c.

Note:There are references to both hardware parameters and software registers throughout this chapter. Parameters and many of the register bits are prefixed with an IC_*. However, the software register bits are distinguished in this chapter by italics. For instance,
IC_MAX_SPEED_MODE is a hardware parameter and configured once using Synopsys coreConsultant, whereas the IC_SLAVE_DISABLE bit in the IC_CON register controls whether I2C has its slave disabled.

Register Memory Map
^^^^^^^^^^^^^^^^^^^

Table 1 provides the details of the DW_apb_i2c memory map.

.. table:: Memory Map of DW_apb_i2c

   +------------+-----------------+--------+----------------+---------------------------------------+
   | Name       | Address Offset  | width  | R/W            | Description                           |
   +============+=================+========+================+=======================================+
   | IC_CON     | 0x00            | 20 bits| R/W or         | I2C control                           |
   |            |                 |        |                +                                       +
   |            |                 |        | R-Only         | R/W:                                  |
   |            |                 |        |                +                                       +
   |            |                 |        | on bit 4       | I2C_DYNAMIC_TAR_UPDATE=1, bit 4 is    |
   |            |                 |        |                +                                       +
   |            |                 |        |                | read only.                            |
   |            |                 |        | and bit 9      |                                       |
   |            |                 |        |                | IC_RX_FULL_HLD_BUS_EN =0, bit 9 is    |
   |            |                 |        |                +                                       +
   |            |                 |        | to 19.         | read only.                            |
   |            |                 |        |                |                                       |
   |            |                 |        |                | IC_STOP_DET_IF_MASTER_ACTIVE =0,      |
   |            |                 |        |                +                                       +
   |            |                 |        |                | bit 10 is read only.                  |
   |            |                 |        |                |                                       |
   |            |                 |        |                | IC_BUS_CLEAR_FEATURE=0, bit 11 is     |
   |            |                 |        |                +                                       +
   |            |                 |        |                | read only                             |
   |            |                 |        |                |                                       |
   |            |                 |        |                | IC_OPTIONAL_SAR=0, bit 16 is read only|
   |            |                 |        |                |                                       |
   |            |                 |        |                | IC_SMBUS=0, bit 17 is read only       |
   |            |                 |        |                |                                       |
   |            |                 |        |                | IC_SMBUS_ARP=0, bits 18 and 19 are    |
   |            |                 |        |                +                                       +
   |            |                 |        |                | read only.                            |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value:                          |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 19: IC_PERSISTANT_SLV_ADDR_DEFAULT    |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 17 to 18 : 0                          |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 16: IC_OPTIONAL_SAR_DEFAULT           |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 15 to 7: 0                            |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 6: IC_SLAVE_DISABLE                   |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 5: IC_RESTART_EN                      |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 4: IC_10BITADDR_MASTER                |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 3: IC_10BITADDR_SLAVE                 |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 2:1:IC_MAX_SPEED_MODE                 |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 0: IC_MASTER_MODE                     |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_TAR     | 0x04            | 12,13, | R/W            | I2C Target Address                    |
   |            |                 |        |                +                                       +
   |            |                 | 14 or  |                | Width:                                |
   |            |                 |        |                +                                       +
   |            |                 | 16 bits|                | If I2C_DYNAMIC_TAR_UPDATE=1, 13 bits  |
   |            |                 |        |                +                                       +
   |            |                 |        |                | If IC_DEVICE_ID=1, 14 bits            |
   |            |                 |        |                |                                       |
   |            |                 |        |                | If IC_SMBUS=1, 17 bits                |
   |            |                 |        |                +                                       +
   |            |                 |        |                | otherwise 12 bits                     |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: Reset values for the     |
   |            |                 |        |                +                                       +
   |            |                 |        |                | four bit fields  correspond to the    |
   |            |                 |        |                |                                       |
   |            |                 |        |                | following                             |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 13: 0x0                               |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 12: IC_10BITADDR_MASTER configuration |
   |            |                 |        |                |                                       |
   |            |                 |        |                | parameter                             |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 11: 0x0                               |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 10: 0x0                               |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 9:0: IC_DEFAULT_TAR_SLAVE_ADDR        |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SAR     | 0x08            | 10 bits| R/W            | Slave Target Address                  |
   |            |                 |        |                +                                       +
   |            |                 |        |                | Reset Value: IC_DEFAULT_SLAVE_ADDR    |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_HS_MADDR| 0x0C            | 3 bits | R/W            | I2C HS Master Mode Code Address       |
   |            |                 |        |                +                                       +
   |            |                 |        |                | Reset Value: IC_HS_MASTER_CODE        |
   +------------+-----------------+--------+----------------+---------------------------------------+

.. table::

   +------------+-----------------+--------+----------------+---------------------------------------+
   | Name       | Address Offset  | width  | R/W            | Description                           |
   +============+=================+========+================+=======================================+
   | IC_DATA_CMD| 0x10            | Refer  | R/W            | I2C Rx/Tx Data Buffer and Command     |
   |            |                 |        |                +                                       +
   |            |                 | to     |                | Reset Value: 0x0                      |
   |            |                 |        |                +                                       +
   |            |                 | Descrip|                | Width:                                |
   |            |                 |        |                +                                       +
   |            |                 | tion   |                | Write:                                |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 11 bits when                          |
   |            |                 |        |                +                                       +
   |            |                 |        |                | IC_EMPTYFIFO_HOLD_MASTER_EN=1         |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 9 bits when                           |
   |            |                 |        |                +                                       +
   |            |                 |        |                | IC_EMPTYFIFO_HOLD_MASTER_EN=0         |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Read:                                 |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 12 bits when                          |
   |            |                 |        |                |                                       |
   |            |                 |        |                | IC_FIRST_DATA_BYTE_STATUS =1          |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 8 bits when                           |
   |            |                 |        |                |                                       |
   |            |                 |        |                | IC_FIRST_DATA_BYTE_STATUS = 0         |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Notes:                                |
   |            |                 |        |                |                                       |
   |            |                 |        |                | With nine or eleven bits required for |
   |            |                 |        |                |                                       |
   |            |                 |        |                | writes the DW_apb_i2c requires 16-bit |
   |            |                 |        |                |                                       |
   |            |                 |        |                + data on the APB bus transfers when    +
   |            |                 |        |                |                                       |
   |            |                 |        |                | writing into the transmit FIFO.       |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Eight-bit transfers remain for reads  |
   |            |                 |        |                |                                       |
   |            |                 |        |                | from the receive FIFO.                |
   |            |                 |        |                |                                       |
   |            |                 |        |                | In order for the DW_apb_i2c to        |
   |            |                 |        |                |                                       |
   |            |                 |        |                | continue acknowledging reads,a read   |
   |            |                 |        |                |                                       |
   |            |                 |        |                | command should be written for every   |
   |            |                 |        |                |                                       |
   |            |                 |        |                | byte that is to be received;otherwise |
   |            |                 |        |                |                                       |
   |            |                 |        |                | the DW_apb_i2c will stop acknowledging|
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SS_SCL  | 0x14            | 16bits | R/W            | Standard speed I2C Clock SCL High     |
   |            |                 |        |                |                                       |
   | _HCNT      |                 |        |                | Count                                 |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: IC_SS_SCL_HIGH_COUNT     |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SS_SCL  | 0x18            | 16bits | R/W            | Standard speed I2C Clock SCL Low Count|
   |            |                 |        |                |                                       |
   | _LCNT      |                 |        |                | Reset Value: IC_SS_SCL_LOW_COUNT      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_FS_SCL  | 0x1C            | 16bits | R/W            | Fast Mode and Fast Mode Plus I2C Clock|
   |            |                 |        |                |                                       |
   | _HCNT      |                 |        |                | SCL High Count                        |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: IC_FS_SCL_HIGH_COUNT     |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_FS_SCL  | 0x20            | 16bits | R/W            | Fast Mode and Fast Mode Plus I2C Clock|
   |            |                 |        |                |                                       |
   | _LCNT      |                 |        |                | SCL Low Count                         |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: IC_FS_SCL_LOW_COUNT      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_HS_SCL  | 0x24            | 16bits | R/W            | High speed I2C Clock SCL High Count   |
   |            |                 |        |                |                                       |
   | _HCNT      |                 |        |                | Reset Value: IC_HS_SCL_HIGH_COUNT     |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_HS_SCL  | 0x28            | 16bits | R/W            | High speed I2C Clock SCL Low Count    |
   |            |                 |        |                |                                       |
   | _LCNT      |                 |        |                | Reset Value: IC_HS_SCL_LOW_COUNT      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_INTR    | 0x2c            | 15bits | R              | I2C Interrupt Status                  |
   |            |                 |        |                |                                       |
   | _STAT      |                 |        |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+

.. table::

   +------------+--------+---------+----------------+-----------------------------------------------+
   | Name       | Address| width   | R/W            | Description                                   |
   |            |        |         |                |                                               |
   |            | Offset |         |                |                                               |
   +============+========+=========+================+===============================================+
   | IC_INTR    | 0x30   | 15 bits | R/W or Readonly| I2C Interrupt Mask                            |
   |            |        |         |                |                                               |
   | _MASK      |        |         | on bits 12 to  | Reset Value:                                  |
   |            |        |         |                |                                               |
   |            |        |         | 14             | If IC_BUS_CLEAR_FEATURE=0, 14'h8ff            |
   |            |        |         |                |                                               |
   |            |        |         |                | If IC_BUS_CLEAR_FEATURE=1, 15'h48ff           |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_RAW     | 0x34   | 15 bits | R              | I2C Raw Interrupt Status                      |
   |            |        |         |                |                                               |
   | _INTR      |        |         |                | Reset Value: 0x0                              |
   |            |        |         |                |                                               |
   | _STAT      |        |         |                |                                               |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_RX      | 0x38   | 8 bits  | R/W            | I2C Receive FIFO Threshold                    |
   |            |        |         |                |                                               |
   | _TL        |        |         |                | Reset Value: IC_RX_TL configuration parameter |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_TX      | 0x3C   | 8 bits  | R/W            | I2C Transmit FIFO Threshold                   |
   |            |        |         |                |                                               |
   | _TL        |        |         |                | Reset Value: IC_TX_TL configuration parameter |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x40   | 1 bit   | R              | Clear Combined and Individual Interrupts      |
   |            |        |         |                |                                               |
   | _INTR      |        |         |                | Reset Value: 0x0                              |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x44   | 1 bit   | R              | Clear RX_UNDER Interrup                       |
   |            |        |         |                |                                               |
   | _RX        |        |         |                | Reset Value: 0x0                              |
   |            |        |         |                |                                               |
   | _UNDER     |        |         |                |                                               |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x48   | 1 bit   | R              | Clear RX_OVER Interrup                        |
   |            |        |         |                |                                               |
   | _RX        |        |         |                | Reset Value: 0x0                              |
   |            |        |         |                |                                               |
   | _OVER      |        |         |                |                                               |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x4C   | 1 bit   | R              | Clear TX_OVER Interrupt                       |
   |            |        |         |                |                                               |
   | _TX        |        |         |                | Reset Value: 0x0                              |
   |            |        |         |                |                                               |
   | _OVER      |        |         |                |                                               |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x50   | 1 bit   | R              | Clear RD_REQ Interrupt                        |
   |            |        |         |                |                                               |
   | _RD        |        |         |                | Reset Value: 0x0                              |
   |            |        |         |                |                                               |
   | _REQ       |        |         |                |                                               |       
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x54   | 1 bit   | R              | Clear TX_ABRT Interrupt                       |
   |            |        |         |                |                                               |
   | _TX        |        |         |                | Reset Value: 0x0                              |
   |            |        |         |                |                                               |
   | _ABRT      |        |         |                |                                               |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x58   | 1 bit   | R              | Clear RX_DONE Interrupt                       |
   |            |        |         |                |                                               |
   | _RX        |        |         |                | Reset Value: 0x0                              |
   |            |        |         |                |                                               |
   | _DONE      |        |         |                |                                               |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x5c   | 1 bit   | R              | Clear ACTIVITY Interrup                       |
   |            |        |         |                |                                               |
   | _ACTIVITY  |        |         |                | Reset Value: 0x0                              |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x60   | 1 bit   | R              | Clear STOP_DET Interrupt                      |
   |            |        |         |                |                                               |
   | _STOP      |        |         |                | Reset Value: 0x0                              |
   |            |        |         |                |                                               |
   | _DET       |        |         |                |                                               |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x64   | 1 bit   | R              | Clear START_DET Interrup                      |
   |            |        |         |                |                                               |
   | _START     |        |         |                | Reset Value: 0x0                              |
   |            |        |         |                |                                               |
   | _DET       |        |         |                |                                               |
   +------------+--------+---------+----------------+-----------------------------------------------+
   | IC_CLR     | 0x68   | 1 bit   | R              | Clear GEN_CALL Interrupt                      |
   |            |        |         |                |                                               |
   | _GEN       |        |         |                | Reset Value: 0x0                              |
   |            |        |         |                |                                               |
   | _CALL      |        |         |                |                                               |
   +------------+--------+---------+----------------+-----------------------------------------------+ 

.. table::

   +------------+-----------------+--------+----------------+---------------------------------------+
   | Name       | Address Offset  | width  | R/W            | Description                           |
   +============+=================+========+================+=======================================+
   | IC_ENABLE  | 0x6c            | Refer  | R/W            | I2C Enable                            |
   |            |                 |        |                +                                       +
   |            |                 | to     |                | Width:                                |
   |            |                 |        |                +                                       +
   |            |                 | Descrip|                | 2 bits if IC_TX_CMD_BLOCK = 0         |
   |            |                 |        |                +                                       +
   |            |                 | tion   |                | 3 bits if IC_TX_CMD_BLOCK = 1         |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 4 bits if IC_BUS_CLEAR_FEATURE = 1    |
   |            |                 |        |                +                                       +
   |            |                 |        |                | 17 bits if IC_SMBUS=1                 |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 19 bits if IC_SMBUS_SUSPEND_ALERT=1   |
   |            |                 |        |                +                                       +
   |            |                 |        |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_STATUS  | 0x70            | Refer  | R              | I2C Status register                   |
   |            |                 |        |                +                                       +
   |            |                 | to     |                | Width:                                |
   |            |                 |        |                +                                       +
   |            |                 | Descrip|                | 7 bits if IC_STAT_FOR_CLK_STRETCH = 0 |
   |            |                 |        |                +                                       +
   |            |                 | tion   |                | 11 bits if IC_STAT_FOR_CLK_STRETCH = 1|
   |            |                 |        |                |                                       |
   |            |                 |        |                | 12 bits if IC_BUS_CLEAR_FEATURE=1     |
   |            |                 |        |                +                                       +
   |            |                 |        |                | 17 bits if IC_SMBUS=1                 |
   |            |                 |        |                |                                       |
   |            |                 |        |                | 19 bits if IC_SMBUS_ARP=1             |
   |            |                 |        |                +                                       +
   |            |                 |        |                | 21 bits if IC_SMBUS_SUSPEND_ALERT=1   |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: 0x6                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_TXFLR   | 0x74            | TX     | R              | Transmit FIFO Level Register          |
   |            |                 |        |                |                                       |
   |            |                 | _ABW+1 |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_RXFLR   | 0x78            | RX     | R              | Receive FIFO Level Register           |
   |            |                 |        |                |                                       |
   |            |                 | _ABW+1 |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SDA     | 0x7C            | 24 bits| R/W            | SDA hold time length register         |
   |            |                 |        |                |                                       |
   | _HOLD      |                 |        |                | Reset Value: IC_DEFAULT_SDA_HOLD      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_TX_ABRT | 0x80            | 32 bits| R              | I2C Transmit Abort Status Register    |
   |            |                 |        |                |                                       |
   | _SOURCE    |                 |        |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SLV_DATA| 0x84            | 1 bit  | R/W            | Generate SLV_DATA_NACK Register       |
   |            |                 |        |                |                                       |
   | _NACK_ONLY |                 |        |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_DMA_CR  | 0x88            | 2 bits | R/W            | DMA Control Register for transmit and |
   |            |                 |        |                |                                       |
   |            |                 |        |                | receive handshaking interface         |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_DMA_TDLR| 0x8c            | TX_ABW | R/W            | DMA Transmit Data Level               |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_DMA_RDLR| 0x90            | RX_ABW | R/W            | DMA Receive Data Level                |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SDA     | 0x94            | 8 bits | R/W            | I2C SDA Setup Register                |
   |            |                 |        |                |                                       |
   | _SETUP     |                 |        |                | Reset Value: IC_DEFAULT_SDA_SETUP     |
   |            |                 |        |                |                                       |
   |            |                 |        |                | configuration parameter               |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_ACK     | 0x98            | 1 bit  | R/W            | I2C ACK General Call Registe          |
   |            |                 |        |                |                                       |
   | _GENERAL   |                 |        |                | Reset Value:                          |
   |            |                 |        |                |                                       |
   | _CALL      |                 |        |                | IC_DEFAULT_ACK_GENERAL_CALL           |
   |            |                 |        |                |                                       |
   |            |                 |        |                | configuration paramete                |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_ENABLE  | 0x9C            | 3 bits | R              | I2C Enable Status Register            |
   |            |                 |        |                |                                       |
   | _STATUS    |                 |        |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_FS      | 0xA0            | 8 bits | R/W            | ISS and FS spike suppression limit    |
   |            |                 |        |                |                                       |
   | _SPKLEN    |                 |        |                | Reset Value: IC_DEFAULT_FS_SPKLEN     |
   |            |                 |        |                |                                       |
   |            |                 |        |                | configuration parameter               |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_HS      | 0xA4            | 8 bits | R/W            | HS spike suppression limit            |
   |            |                 |        |                |                                       |
   | _SPKLEN    |                 |        |                | Reset Value: IC_DEFAULT_HS_SPKLEN     |
   |            |                 |        |                |                                       |
   |            |                 |        |                | configuration parameter               |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_CLR     | 0xA8            | 1 bit  | R              | Clear RESTART_DET Interrupt           |
   |            |                 |        |                |                                       |
   | _RESTART   |                 |        |                | Reset Value: 0x0                      |
   |            |                 |        |                |                                       |
   | _DET       |                 |        |                |                                       |
   +------------+-----------------+--------+----------------+---------------------------------------+
   
.. table::

   +------------+-----------------+--------+----------------+---------------------------------------+
   | Name       | Address Offset  | width  | R/W            | Description                           |
   +============+=================+========+================+=======================================+
   | IC_COMP    | 0xf4            | 32 bits| R              | Component Parameter Register          |
   |            |                 |        |                |                                       |
   | _PARAM_1   |                 |        |                | Reset Value: Reset value depends on   |
   |            |                 |        |                |                                       |
   |            |                 |        |                | configuration parameters.             |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_COMP    | 0xf8            | 32 bits| R              | Component Version ID                  |
   |            |                 |        |                |                                       |
   | _VERSION   |                 |        |                | Reset Value: See the releases table in|
   |            |                 |        |                |                                       |
   |            |                 |        |                | the AMBA 2 release notes              |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_COMP    | 0xfc            | 32 bits| R              | DesignWare Component Type Register    |
   |            |                 |        |                |                                       |
   | _TYPE      |                 |        |                | Reset Value: 0x44570140               |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SCL_STU | 0xAC            | 32 bits| R/W            | I2C SCL stuck at low timeout register |
   |            |                 |        |                |                                       |
   | CK_AT_LOW  |                 |        |                | Reset Value:                          |
   |            |                 |        |                |                                       |
   | _TIMEOUT   |                 |        |                | IC_SCL_STUCK_TIMEOUT_DEFAULT          |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SDA_STU | 0xB0            | 32 bits| R/W            | I2C SDA Stuck at Low Timeout          |
   |            |                 |        |                |                                       |
   | CK_AT_LOW  |                 |        |                | Reset Value:                          |
   |            |                 |        |                |                                       |
   | _TIMEOUT   |                 |        |                | IC_SDA_STUCK_TIMEOUT_DEFAULT          |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_CLR_SCL | 0xB4            | 1 bit  | R              | Clear SCL Stuck at Low Detect         |
   |            |                 |        |                |                                       |
   | _STUCK     |                 |        |                | Interrupt Register                    |
   |            |                 |        |                |                                       |
   | _DET       |                 |        |                | Reset Value: 0x0                      |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_DEVICE  | 0xB8            | 24 bits| R              | I2C Device ID                         |
   |            |                 |        |                |                                       |
   | _ID        |                 |        |                | Reset Value: IC_DEVICE_ID_VALUE       |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_UFM_SCL | 0x14            | 16 bits| R/W            | Ultra-Fast mode I2C Clock High Count  |
   |            |                 |        |                |                                       |
   | _HCNT      |                 |        |                | Register                              |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: IC_UFM_SCL_HIGH_COUNT    |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_UFM_SCL | 0x18            | 16 bits| R/W            | Ultra-Fast mode I2C Clock Low Count   |
   |            |                 |        |                |                                       |
   | _LCNT      |                 |        |                | Register                              |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: IC_UFM_SCL_LOW_COUNT     |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_UFM_TBUF| 0x1c            | 16 bits| R/W            | Ultra-Fast mode TBuf Idle Count       |
   |            |                 |        |                |                                       |
   | _CNT       |                 |        |                | Register                              |
   |            |                 |        |                |                                       |    
   |            |                 |        |                | Reset Value: IC_UFM_TBUF_CNT_DEFAULT  |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_UFM     | 0xA0            | 8 bits | R/W            | I2C Ultra-Fast mode Spike suppression |
   |            |                 |        |                |                                       |
   | _SPKLEN    |                 |        |                | Register                              |
   |            |                 |        |                |                                       |
   |            |                 |        |                | Reset Value: IC_DEFAULT_UFM_SPKLEN    |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SMBUS   | 0xBC            | 32 bits| R/W            | SMBUS Slave Clock Extend Timeout      |
   |            |                 |        |                |                                       |
   | _CLOCK_LOW |                 |        |                | Register                              |
   |            |                 |        |                |                                       |
   | _SEXT      |                 |        |                |                                       |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SMBUS   | 0xC0            | 32 bits| R/W            | SMBUS Master extend clock Timeout     |
   |            |                 |        |                |                                       |
   | _CLOCK_LOW |                 |        |                | Register                              |
   |            |                 |        |                |                                       |
   | _MEXT      |                 |        |                |                                       |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SMBUS   | 0xC4            | 16 bits| R/W            | SMBus Thigh MAX Bus-Idle count        |
   |            |                 |        |                |                                       |
   | _THIGH_MAX |                 |        |                | Register                              |
   |            |                 |        |                |                                       |
   | _IDLE_COUNT|                 |        |                |                                       |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SMBUS   | 0xC8            | 32 bits| R              | I2C SMBUS Interrupt Status Register   |
   |            |                 |        |                |                                       |
   | _INTR_STAT |                 |        |                |                                       |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SMBUS   | 0xCC            | 32 bits| R/W            | I2C Interrupt Mask Register           |
   |            |                 |        |                |                                       |
   | _INTR_MASK |                 |        |                | Register                              |
   +------------+-----------------+--------+----------------+---------------------------------------+

.. table::

   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SMBUS   | 0xD0            | 32 bits| R              | I2C SMBUS Raw Interrupt Status        |
   |            |                 |        |                |                                       |
   | _INTR_RAW  |                 |        |                | Register                              |
   |            |                 |        |                |                                       |
   | _STATUS    |                 |        |                |                                       |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_CLR     | 0xD4            | 32 bits| W              | Clear SMBUS Interrupt Register        |
   |            |                 |        |                |                                       |
   | _SMBUS_INTR|                 |        |                |                                       |
   +------------+-----------------+--------+----------------+---------------------------------------+ 
   | IC_OPTIONAL| 0xD8            | 7 bits | R/W            | I2C Optional Slave Address Register   |
   |            |                 |        |                |                                       |
   | _SAR       |                 |        |                |                                       |
   +------------+-----------------+--------+----------------+---------------------------------------+
   | IC_SMBUS   | 0xDC            | 32 bits| R/W            | SMBUS ARP UDID LSB Register           |
   |            |                 |        |                |                                       |
   | _UDID_LSB  |                 |        |                |                                       |
   +------------+-----------------+--------+----------------+---------------------------------------+  

Operation of Interrupt Registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
  Table 2 lists the operation of the DW_apb_i2c interrupt registers and how they are set and cleared. Some bits are set by hardware and cleared by software, whereas other bits are set and cleared by hardware.

.. table::  Clearing and Setting of Interrupt Registers

  +---------------------+------------------------------------+----------------------------+
  | Interrupt Bit Fields| Set by Hardware/Cleared by Software| Set and Cleared by Hardware|
  +---------------------+------------------------------------+----------------------------+
  | MST_ON_HOLD         | No                                 | Yes                        |
  +---------------------+------------------------------------+----------------------------+
  | RESTART_DET         | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+
  | GEN_CALL            | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+
  | START_DET           | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+
  | STOP_DET            | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+
  | ACTIVITY            | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+
  | RX_DONE             | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+
  | TX_ABRT             | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+
  | RD_REQ              | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+ 
  | TX_EMPTY            | No                                 | Yes                        |
  +---------------------+------------------------------------+----------------------------+
  | TX_OVER             | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+
  | RX_FULL             | No                                 | Yes                        |
  +---------------------+------------------------------------+----------------------------+
  | RX_OVER             | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+
  | RX_UNDER            | Yes                                | No                         |
  +---------------------+------------------------------------+----------------------------+

Figure 1 shows the operation of the interrupt registers where the bits are set by hardware and cleared by software.

.. figure:: pic/Interrupt-Scheme.png 
        :alt: Interrupt Scheme  
         
        Interrupt Scheme

Registers and Field Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes the registers listed in Table 1. Registers are on the pclk domain, but
status bits reflect actions that occur in the ic_clk domain. Therefore, there is delay when the pclk register
reflects the activity that occurred on the ic_clk side.

Some registers may be written only when the DW_apb_i2c is disabled, programmed by the IC_ENABLE
register. Software should not disable the DW_apb_i2c while it is active. If the DW_apb_i2c is in the process
of transmitting when it is disabled, it stops as well as deletes the contents of the transmit buffer after the
current transfer is complete. The slave continues receiving until the remote master aborts the transfer, in
which case the DW_apb_i2c could be disabled. Registers that cannot be written to when the DW_apb_i2c is
enabled are indicated in their descriptions.

Unless the clocks pclk and ic_clk are identical (IC_CLK_TYPE = 0), there is a two-register delay for
synchronous and asynchronous modes.

IC_CON
""""""
- Name: I2C Control Register

- Size: 20 bits

- Address Offset: 0x00

- Read/Write Access:

  + If configuration parameter I2C_DYNAMIC_TAR_UPDATE=1, bit 4 is read only.

  + If configuration parameter IC_RX_FULL_HLD_BUS_EN =0, bit 9 is read only.
    
  + If configuration parameter IC_STOP_DET_IF_MASTER_ACTIVE =0, bit 10 is read only.

  + If configuration parameter IC_BUS_CLEAR_FEATURE=0, bit 11 is read only.

  + If configuration parameter IC_OPTIONAL_SAR=0, bit 16 is read only.

  + If configuration parameter IC_SMBUS=0, bit 17 is read only.

  + If configuration parameter IC_SMBUS_ARP=0, bits 18 and 19 are read only.

This register can be written only when the DW_apb_i2c is disabled, which corresponds to IC_ENABLE[0] 
being set to 0. Writes at other times have no effect.

.. table::  IC_CON Register Fields

  +------+-------------------------+-----+--------------------------------------------------------------+ 
  | Bits | Name                    | R/W | Description                                                  |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 31:20| Reserved                | N/A | Reserved                                                     |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 19   | SMBUS_PERSISTANT        |     | This bit controls to enable DW_apb_i2c slave as persistent or|
  +      +                         +     +                                                              +
  |      | _SLV_ADDR_EN            |     | non-persistent slave.                                        |
  +      +                         +     +                                                              +
  |      |                         |     | If the slave is non-PSA then DW_apb_i2c slave device clears  |
  +      +                         +     +                                                              +
  |      |                         |     | the Address valid flag for both General and Directed Reset   |
  +      +                         +     +                                                              +
  |      |                         |     | ARP command else the address valid flag will always set to 1.|
  +      +                         +     +                                                              +
  |      |                         |     | Dependencies: This register bit is applicable only when the  |
  +      +                         +     +                                                              +
  |      |                         |     | IC_SMBUS_ARP configuration parameter is set to 1.            |
  +      +                         +     +                                                              +
  |      |                         |     | This bit is applicable only in Slave mode.                   |
  +      +                         +     +                                                              +
  |      |                         |     | Reset Value: IC_PERSISTANT_SLV_ADDR_DEFAULT                  |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 18   | SMBUS_ARP_EN            | R/W | This bit controls whether DW_apb_i2c should enable Address   |
  +      +                         +     +                                                              +
  |      |                         |     | Resolution Logic in SMBus Mode. The Slave mode will          |
  +      +                         +     +                                                              +
  |      |                         |     | decode the Address Resolution Protocol commands and          |
  +      +                         +     +                                                              +
  |      |                         |     | respond to it. The DW_apb_i2c slave also includes the        |
  +      +                         +     +                                                              +
  |      |                         |     | generation/validity of PEC byte for Address Resolution       |
  +      +                         +     +                                                              +
  |      |                         |     | Protocol commands.                                           |
  +      +                         +     +                                                              +
  |      |                         |     | This bit is applicable only in Slave mode.                   |
  +      +                         +     +                                                              +
  |      |                         |     | Dependencies: This register bit is applicable only when the  |
  +      +                         +     +                                                              +
  |      |                         |     | IC_SMBUS_ARP configuration parameter is set to 1.            |
  +      +                         +     +                                                              +
  |      |                         |     | Reset Value: 0x0                                             |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 17   | SMBUS_SLAVE_QUICK_CMD_EN| R/W | If this bit is set to 1, DW_apb_i2c slave only receives Quick|
  +      +                         +     +                                                              +
  |      |                         |     | commands in SMBus Mode.                                      |
  +      +                         +     +                                                              +
  |      |                         |     | If this bit is set to 0, DW_apb_i2c slave receives all bus   |
  +      +                         +     +                                                              +
  |      |                         |     | protocols but not Quick commands.                            |
  +      +                         +     +                                                              +
  |      |                         |     | This bit is applicable only in slave mode.                   |
  +      +                         +     +                                                              +
  |      |                         |     | Dependencies: This register bit is applicable only when the  |
  +      +                         +     +                                                              +
  |      |                         |     | IC_SMBUS configuration parameter is set to 1.                |
  +      +                         +     +                                                              +
  |      |                         |     | Reset Value: 0x0                                             |
  +------+-------------------------+-----+--------------------------------------------------------------+


.. table::

  +------+-------------------------+-----+--------------------------------------------------------------+
  | 16   | OPTIONAL_SAR_CTRL       | R/W | Enables the usage of IC_OPTIONAL_SAR register.               |
  +      +                         +     +                                                              +
  |      |                         |     | If IC_OPTIONAL_SAR =1, IC_OPTIONAL_SAR value is              |
  +      +                         +     +                                                              +
  |      |                         |     | used as additional slave address. User must program a valid  |
  +      +                         +     +                                                              +
  |      |                         |     | address in IC_OPTIONAL_SAR before writing 1 to this field.   |
  +      +                         +     +                                                              +
  |      |                         |     | If IC_OPTIONAL_SAR =0, IC_OPTIONAL_SAR value is not          |
  +      +                         +     +                                                              +
  |      |                         |     | used as additional slave address. In this mode only one I2C  |
  +      +                         +     +                                                              +
  |      |                         |     | slave address is used.                                       |
  +      +                         +     +                                                              +
  |      |                         |     | Dependencies: This register bit is valid only if configuratio|
  +      +                         +     +                                                              +
  |      |                         |     | -n parameter IC_OPTIONAL_SAR is set to 1                     |
  +      +                         +     +                                                              +
  |      |                         |     | Reset Value: IC_OPTIONAL_SAR_DEFAULT                         |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 15:12| Reserved                | R.W | Reserved                                                     |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 11   | BUS_CLEAR_FEATURE_CTRL  | R/W | In Master Mode:                                              |
  +      +                         +     +                                                              +
  |      |                         |     | 1'b1: Bus Clear Feature is enabled                           |
  +      +                         +     +                                                              +
  |      |                         |     | 1'b0: Bus Clear Feature is disabled                          |
  +      +                         +     +                                                              +
  |      |                         |     | In Slave Mode, this register bit is not applicable.          |
  +      +                         +     +                                                              +
  |      |                         |     | Reset Value: 1'b0                                            |
  +      +                         +     +                                                              +
  |      |                         |     | Dependencies: This register bit value is applicable only     |
  +      +                         +     +                                                              +
  |      |                         |     | when IC_BUS_CLEAR_FEATURE=1.                                 |
  +      +                         +     +                                                              +
  |      |                         |     | This field is not applicable in Ultra-Fast speed mode        |
  +      +                         +     +                                                              +
  |      |                         |     | (IC_ULTRA_FAST_MODE=1)                                       |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 10   | STOP_DET_IF_MASTER      | R/W | In Master Mode:                                              |
  +      +                         +     +                                                              +
  |      | _ACTIVE                 |     | 1’b1: Issues the STOP_DET interrupt only when the            |
  +      +                         +     +                                                              +
  |      |                         |     | master is active                                             |
  +      +                         +     +                                                              +
  |      |                         |     | 1’b0: Issues the STOP_DET irrespective of whether the        |
  +      +                         +     +                                                              +
  |      |                         |     | master is active                                             |
  +      +                         +     +                                                              +
  |      |                         |     | Reset value: 1’b0                                            |
  +      +                         +     +                                                              +
  |      |                         |     | Dependencies: This Register bit value is applicable only     |
  +      +                         +     +                                                              +
  |      |                         |     | when IC_STOP_DET_IF_MASTER_ACTIVE=1.                         |
  +      +                         +     +                                                              +
  |      |                         |     | This field is not applicable in Ultra-Fast speed mode        |
  +      +                         +     +                                                              +
  |      |                         |     | (IC_ULTRA_FAST_MODE=1)                                       |
  +------+-------------------------+-----+--------------------------------------------------------------+

.. table::

  +------+-------------------------+-----+--------------------------------------------------------------+
  | 9    | RX_FIFO_FULL_HLD_CTRL   | R/W | This bit controls whether DW_apb_i2c should hold the bus     |
  +      +                         +     +                                                              +
  |      |                         | or R| when the Rx FIFO is physically full to its                   |
  +      +                         +     +                                                              +
  |      |                         |     | RX_BUFFER_DEPTH, as described in the                         |
  +      +                         +     +                                                              +
  |      |                         |     | IC_RX_FULL_HLD_BUS_EN parameter.                             |
  +      +                         +     +                                                              +
  |      |                         |     | Dependencies: This register bit value is applicable only     |
  +      +                         +     +                                                              +
  |      |                         |     | when the IC_RX_FULL_HLD_BUS_EN configuration                 |
  +      +                         +     +                                                              +
  |      |                         |     | parameter is set to 1. If IC_RX_FULL_HLD_BUS_EN = 0,         |
  +      +                         +     +                                                              +
  |      |                         |     | then this bit is read-only. If IC_RX_FULL_HLD_BUS_EN = 1,    |
  +      +                         +     +                                                              +
  |      |                         |     | then this bit can be read or write.                          |
  +      +                         +     +                                                              +
  |      |                         |     | This field is not applicable in Ultra-Fast speed mode        |
  +      +                         +     +                                                              +
  |      |                         |     | (IC_ULTRA_FAST_MODE=1)                                       |
  +      +                         +     +                                                              +
  |      |                         |     | Reset value: 0x0                                             |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 8    | TX_EMPTY_CTRL           | R/W | This bit controls the generation of the TX_EMPTY interrupt,  |
  +      +                         +     +                                                              +
  |      |                         |     | as described in the IC_RAW_INTR_STAT register.               |
  +      +                         +     +                                                              +
  |      |                         |     | Reset value: 0x0                                             |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 7    | STOP_DET_IFADDRESSED    | R/W | In slave mode:                                               |
  +      +                         +     +                                                              +
  |      |                         |     | 1’b1 – issues the STOP_DET interrupt only when it is         |
  +      +                         +     +                                                              +
  |      |                         |     | addressed.                                                   |
  +      +                         +     +                                                              +
  |      |                         |     | 1’b0 – issues the STOP_DET irrespective of whether it’s      |
  +      +                         +     +                                                              +
  |      |                         |     | addressed or not.                                            |
  +      +                         +     +                                                              +
  |      |                         |     | Dependencies: This register bit value is applicable in the   |
  +      +                         +     +                                                              +
  |      |                         |     | slave mode only (MASTER_MODE = 1’b0)                         |
  +      +                         +     +                                                              +
  |      |                         |     | Reset value: 1’b0                                            |
  +      +                         +     +                                                              +
  |      |                         |     | NOTE: During a general call address, this slave does not     |
  +      +                         +     +                                                              +
  |      |                         |     | issue the STOP_DET interrupt if                              |
  +      +                         +     +                                                              +
  |      |                         |     | STOP_DET_IF_ADDRESSED = 1’b1, even if the slave              |
  +      +                         +     +                                                              +
  |      |                         |     | responds to the general call address by generating ACK.      |
  +      +                         +     +                                                              +
  |      |                         |     | The STOP_DET interrupt is generated only when the            |
  +      +                         +     +                                                              +
  |      |                         |     | transmitted address matches the slave address (SAR).         |
  +------+-------------------------+-----+--------------------------------------------------------------+

.. table::

  +------+-------------------------+-----+--------------------------------------------------------------+
  | 6    | IC_SLAVE_DISABLE        | R/W | This bit controls whether I2C has its slave disabled, which  |
  +      +                         +     +                                                              +
  |      |                         |     | means once the presetn signal is applied, then this bit takes|
  +      +                         +     +                                                              +
  |      |                         |     | on the value of the configuration parameter                  |
  +      +                         +     +                                                              +
  |      |                         |     | IC_SLAVE_DISABLE. You have the choice of having the          |
  +      +                         +     +                                                              +
  |      |                         |     | slave enabled or disabled after reset is applied, which means|
  +      +                         +     +                                                              +
  |      |                         |     | software does not have to configure the slave. By default,the|
  +      +                         +     +                                                              +
  |      |                         |     | slave is always enabled (in reset state as well). If you need|
  +      +                         +     +                                                              +
  |      |                         |     | to disable it after reset, set this bit to 1.                |
  +      +                         +     +                                                              +
  |      |                         |     | If this bit is set (slave is disabled), DW_apb_i2c functions |
  +      +                         +     +                                                              +
  |      |                         |     | only as a master and does not perform any action that        |
  +      +                         +     +                                                              +
  |      |                         |     | requires a slave.                                            |
  +      +                         +     +                                                              +
  |      |                         |     | 0: slave is enabled                                          |
  +      +                         +     +                                                              +
  |      |                         |     | 1: slave is disabled                                         |
  +      +                         +     +                                                              +
  |      |                         |     | Reset value: IC_SLAVE_DISABLE configuration parameter        |
  +      +                         +     +                                                              +
  |      |                         |     | NOTE: Software should ensure that if this bit is written with|
  +      +                         +     +                                                              +
  |      |                         |     | ‘0,’ then bit 0 should also be written with a ‘0’.           |
  +------+-------------------------+-----+--------------------------------------------------------------+

.. table::

  +------+-------------------------+-----+--------------------------------------------------------------+
  | 5    | IC_RESTART_EN           | R/W | Determines whether RESTART conditions may be sent when       |
  +      +                         +     +                                                              +
  |      |                         |     | acting as a master. Some older slaves do not support         |
  +      +                         +     +                                                              +
  |      |                         |     | handling RESTART conditions; however, RESTART                |
  +      +                         +     +                                                              +
  |      |                         |     | conditions are used in several DW_apb_i2c operations.        |
  +      +                         +     +                                                              +
  |      |                         |     | 0: disable                                                   |
  +      +                         +     +                                                              +
  |      |                         |     | 1: enable                                                    |
  +      +                         +     +                                                              +
  |      |                         |     | When the RESTART is disabled, the DW_apb_i2c master is       |
  +      +                         +     +                                                              +
  |      |                         |     | incapable of performing the following functions:             |
  +      +                         +     +                                                              +
  |      |                         |     | Sending a START BYTE                                         |
  +      +                         +     +                                                              +
  |      |                         |     | Performing any high-speed mode operation                     |
  +      +                         +     +                                                              +
  |      |                         |     | Performing direction changes in combined format mode         |
  +      +                         +     +                                                              +
  |      |                         |     | Performing a read operation with a 10-bit address            |
  +      +                         +     +                                                              +
  |      |                         |     | By replacing RESTART condition followed by a STOP and a      |
  +      +                         +     +                                                              +
  |      |                         |     | subsequent START condition, split operations are broken      |
  +      +                         +     +                                                              +
  |      |                         |     | down into multiple DW_apb_i2c transfers. If the above        |
  +      +                         +     +                                                              +
  |      |                         |     | operations are performed, it will result in setting bit 6    |
  +      +                         +     +                                                              +
  |      |                         |     | (TX_ABRT) of the IC_RAW_INTR_STAT register.                  |
  +      +                         +     +                                                              +
  |      |                         |     | Reset value: IC_RESTART_EN configuration parameter           |
  +------+-------------------------+-----+--------------------------------------------------------------+

.. table::
  
  +------+-------------------------+-----+--------------------------------------------------------------+ 
  | 4    | IC_10BITADDR_MASTER or  | R/W | If the I2C_DYNAMIC_TAR_UPDATE configuration parameter        |
  +      +                         +     +                                                              +
  |      | IC_10BITADDR_MASTER     | or R| is set to “No” (0), this bit is named IC_10BITADDR_MASTER    |
  +      +                         +     +                                                              +
  |      | _rd_only                |     | and controls whether the DW_apb_i2c starts its transfers in  |
  +      +                         +     +                                                              +
  |      |                         |     | 7 or 10-bit addressing mode when acting as a master.         |
  +      +                         +     +                                                              +
  |      |                         |     | If I2C_DYNAMIC_TAR_UPDATE is set to “Yes” (1), the           |
  +      +                         +     +                                                              +
  |      |                         |     | function of this bit is handled by bit 12 of IC_TAR register,|
  +      +                         +     +                                                              +
  |      |                         |     | and becomes a read-only copy called                          |
  +      +                         +     +                                                              +
  |      |                         |     | IC_10BITADDR_MASTER_rd_only                                  |
  +      +                         +     +                                                              +
  |      |                         |     | 0: 7-bit addressing                                          |
  +      +                         +     +                                                              +
  |      |                         |     | 1: 10-bit addressing                                         |
  +      +                         +     +                                                              +
  |      |                         |     | Dependencies: If I2C_DYNAMIC_TAR_UPDATE = 1, then            |
  +      +                         +     +                                                              +
  |      |                         |     | this bit is read-only. If I2C_DYNAMIC_TAR_UPDATE = 0,        |
  +      +                         +     +                                                              +
  |      |                         |     | then this bit can be read or write.                          |
  +      +                         +     +                                                              +
  |      |                         |     | Reset value: IC_10BITADDR_MASTER configuration parameter     |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 3    | IC_10BITADDR_SLAVE      | R/W | When acting as a slave, this bit controls whether the        |
  +      +                         +     +                                                              +
  |      |                         |     | DW_apb_i2c responds to 7- or 10-bit addresses.               |
  +      +                         +     +                                                              +
  |      |                         |     | 0: 7-bit addressing. The DW_apb_i2c ignores transactions     |
  +      +                         +     +                                                              +
  |      |                         |     | that involve 10-bit addressing; for 7-bit addressing,only the|
  +      +                         +     +                                                              +
  |      |                         |     | lower 7 bits of the IC_SAR register are compared.            |
  +      +                         +     +                                                              +
  |      |                         |     | 1: 10-bit addressing. The DW_apb_i2c responds to only        |
  +      +                         +     +                                                              +
  |      |                         |     | 10-bit addressing transfers that match the full 10 bits of   |
  +      +                         +     +                                                              +
  |      |                         |     | the IC_SAR register.                                         |
  +      +                         +     +                                                              +
  |      |                         |     | Reset value: IC_10BITADDR_SLAVE configuration parameter      |
  +------+-------------------------+-----+--------------------------------------------------------------+

Note:Bits 3 and 4 of this register can be programmed differently and in any combination depending on
which format is required for the transfers. For example, master mode can be configured with 10-bit
addressing and slave mode can be configured with 7-bit addressing.

.. table:: 

  +------+-------------------------+-----+--------------------------------------------------------------+
  | 2:1  | SPEED                   | R/W | These bits control at which speed the DW_apb_i2c operates.   |
  +      +                         +     +                                                              +
  |      |                         |     | Hardware protects against illegal values being programmed    |
  +      +                         +     +                                                              +
  |      |                         |     | by software. register These bits must be programmed          |
  +      +                         +     +                                                              +
  |      |                         |     | appropriately for slave mode also, as it is used to capture  |
  +      +                         +     +                                                              +
  |      |                         |     | correct value of spike filter as per the speed mode.         |
  +      +                         +     +                                                              +
  |      |                         |     | This register should be programmed only with a value in the  |
  +      +                         +     +                                                              +
  |      |                         |     | range of 1 to IC_MAX_SPEED_MODE; otherwise, hardware         |
  +      +                         +     +                                                              +
  |      |                         |     | updates this register with the value of                      |
  +      +                         +     +                                                              +
  |      |                         |     | IC_MAX_SPEED_MODE.                                           |
  +      +                         +     +                                                              +
  |      |                         |     | 1: standard mode (0 to 100 Kb/s)                             |
  +      +                         +     +                                                              +
  |      |                         |     | 2: fast mode (<= 400 Kb/s) or fast mode plus (<= 1000 Kb/s)  |
  +      +                         +     +                                                              +
  |      |                         |     | 3: high speed mode (<= 3.4 Mb/s)                             |
  +      +                         +     +                                                              +
  |      |                         |     | NOTE: This field is not applicable in Ultra-Fast speed mode  |
  +      +                         +     +                                                              +
  |      |                         |     | (IC_ULTRA_FAST_MODE=1)                                       |
  +      +                         +     +                                                              +
  |      |                         |     | Reset value: IC_MAX_SPEED_MODE configuration                 |
  +------+-------------------------+-----+--------------------------------------------------------------+
  | 0    | MASTER_MODE             | R/W | This bit controls whether the DW_apb_i2c master is enabled.  |
  +      +                         +     +                                                              +
  |      |                         |     | 0: master disabled                                           |
  +      +                         +     +                                                              +
  |      |                         |     | 1: master enabled                                            |
  +      +                         +     +                                                              +
  |      |                         |     | Reset value: IC_MASTER_MODE configuration parameter          |
  +      +                         +     +                                                              +
  |      |                         |     | NOTE: Software should ensure that if this bit is written with|
  +      +                         +     +                                                              +
  |      |                         |     | ‘1,’ then bit 6 should also be written with a ‘1’.           |
  +------+-------------------------+-----+--------------------------------------------------------------+
  
Certain combinations of the IC_SLAVE_DISABLE (bit 6) and MASTER_MODE (bit 0) result in a configuration error. Table 4 lists the states that result from the combinations of these two bits.

.. table:: States for IC_SLAVE_DISABLE (bit 6) and MASTER_MODE (bit 0)

  +----------------------------+------------------------+----------------------------+
  | IC_SLAVE_DISABLE(IC_CON[6])| MASTER_MODE(IC_CON[0]) | State                      |
  +----------------------------+------------------------+----------------------------+
  | 0                          | 0                      | Slave Device               |
  +----------------------------+------------------------+----------------------------+
  | 0                          | 1                      | Config Error               |
  +----------------------------+------------------------+----------------------------+
  | 1                          | 0                      | Config Error               |
  +----------------------------+------------------------+----------------------------+
  | 1                          | 1                      | Master Device              |
  +----------------------------+------------------------+----------------------------+

Note:Because the DW_apb_i2c should only be used either as an I2C master or I2C slave (but not
both) at any one time, care should be taken in software that certain combinations of the two
bits IC_SLAVE_DISABLE and IC_MASTER_MODE are not programmed into the "IC_CON". In particular, IC_SLAVE_DISABLE and IC_MASTER_MODE must not
be set to ‘0’ and ‘1,’ respectively at any given time.

IC_TAR
"""""""

- Name: I2C Target Address Register
- Size: 12 bits; when I2C_DYNAMIC_TAR_UPDATE = 0 and IC_DEVICE_ID = 0

        13 bits; when I2C_DYNAMIC_TAR_UPDATE = 1 and IC_DEVICE_ID = 0
        
        14 bits; when IC_DEVICE_ID = 1 irrespective of I2C_DYNAMIC_TAR_UPDATE is set
        
        17 bits; when IC_SMBUS=1

- Address Offset: 0x04

- Read/Write Access: Read/Write
  
If the configuration parameter I2C_DYNAMIC_TAR_UPDATE is set to “No” (0), this register is 12 bits
wide, and bits 31:12 are reserved. Writes to this register succeed only when IC_ENABLE[0] is set to 0.
However, if I2C_DYNAMIC_TAR_UPDATE = 1, then the register becomes 13 bits wide. In this case, writes
to IC_TAR succeed when one of the following conditions are true:

- DW_apb_i2c is NOT enabled (IC_ENABLE[0] is set to 0); or

- DW_apb_i2c is enabled (IC_ENABLE[0]=1); AND

  DW_apb_i2c is NOT engaged in any Master (tx, rx) operation (IC_STATUS[5]=0); AND
  
  DW_apb_i2c is enabled to operate in Master mode (IC_CON[0]=1); AND
  
  there are NO entries in the Tx FIFO (IC_STATUS[2]=1)^1
  
You can change the TAR address dynamically without losing the bus, only if the following conditions are
met.

- DW_apb_i2c is enabled (IC_ENABLE[0]=1); AND IC_EMPTYFIFO_HOLD_MASTER_EN configuration parameter is set to 1; AND DW_apb_i2c is enabled to operate in Master mode (IC_CON[0]=1); AND there are NO entries in the Tx FIFO and the master is in HOLD state (IC_INTR_STAT[13]=1);1

If the software or application is aware the the DW_apb_i2c is not using the TAR address for the pending commands inthe Tx FIFO, then it is possible to update the TAR address even while the Tx FIFO has entries (IC_STATUS[2]= 0).

.. table:: IC_TAR Register Fields
 
  +------+--------------------+-----+-------------------------------------------------------------------+
  | Bits | Name               | R/W | Description                                                       |
  +------+--------------------+-----+-------------------------------------------------------------------+
  | 31:17| Reserved           | N/A | Reserved                                                          |
  +------+--------------------+-----+-------------------------------------------------------------------+
  | 16   | SMBUS_QUICK_CMD    | R/W | If bit 11 (SPECIAL) is set to 1, then this bit indicates whether a|
  +      +                    +     +                                                                   +
  |      |                    |     | Quick command is to be performed by the DW_apb_i2c.               |
  +      +                    +     +                                                                   +
  |      |                    |     | Dependencies: This register bit is applicable only when the       |    
  +      +                    +     +                                                                   +
  |      |                    |     | IC_SMBUS configuration parameter is set to 1.                     |  
  +      +                    +     +                                                                   +
  |      |                    |     | Reset Value: 0x0                                                  |
  +------+--------------------+-----+-------------------------------------------------------------------+
  | 15:14| Reserved           | N/A | Reserved                                                          |
  +------+--------------------+-----+-------------------------------------------------------------------+
  | 13   | Device_ID          | R/W | If bit 11 (SPECIAL) is set to 1, then this bit indicates whether a|
  +      +                    +     +                                                                   +
  |      |                    |     | Device-ID of a particular slave mentioned in IC_TAR[6:0] is to be |
  +      +                    +     +                                                                   +
  |      |                    |     | performed by the DW_apb_i2c Master.                               |
  +      +                    +     +                                                                   +
  |      |                    |     | 0: Device-ID is not performed and checks ic_tar[10] to perform    |
  +      +                    +     +                                                                   +
  |      |                    |     | either general call or START byte command.                        |
  +      +                    +     +                                                                   +
  |      |                    |     | 1: Device-ID transfer is performed and bytes based on the         |
  +      +                    +     +                                                                   +
  |      |                    |     | number of read commands in the Tx-FIFO are received from the      |
  +      +                    +     +                                                                   +
  |      |                    |     | targeted slave and put in the Rx-FIFO.                            |
  +      +                    +     +                                                                   +
  |      |                    |     | Dependencies: This field is not applicable in Ultra-Fast speed    |
  +      +                    +     +                                                                   +
  |      |                    |     | mode ( IC_ULTRA_FAST_MODE=1)                                      |
  +      +                    +     +                                                                   +
  |      |                    |     | Reset Value: 0x0                                                  |
  +------+--------------------+-----+-------------------------------------------------------------------+
  | 12   | IC_10BITADDR_MASTER| R/W | This bit controls whether the DW_apb_i2c starts its transfers in  |
  +      +                    +     +                                                                   +
  |      |                    |     | 7-or10-bit addressing mode when acting as a master.               |
  +      +                    +     +                                                                   +
  |      |                    |     | 0: 7-bit addressing                                               |
  +      +                    +     +                                                                   +
  |      |                    |     | 1: 10-bit addressing                                              |
  +      +                    +     +                                                                   +
  |      |                    |     | Dependencies: This bit exists in this register only if the        |
  +      +                    +     +                                                                   +
  |      |                    |     | I2C_DYNAMIC_TAR_UPDATE configuration parameter is set to Yes (1)  |
  +      +                    +     +                                                                   +
  |      |                    |     | Reset value: IC_10BITADDR_MASTER configuration parameter          |
  +------+--------------------+-----+-------------------------------------------------------------------+

.. table::

  +------+--------------------+-----+-------------------------------------------------------------------+
  | 11   | SPECIAL            | R/W | This bit indicates whether software performs a Device-ID, General |
  +      +                    +     +                                                                   +
  |      |                    |     | Call or START BYTE command.                                       |
  +      +                    +     +                                                                   +
  |      |                    |     | 0: ignore bit 10 GC_OR_START and use IC_TAR normally              |
  +      +                    +     +                                                                   +
  |      |                    |     | 1: perform special I2C command as specified in Device-ID or       |
  +      +                    +     +                                                                   +
  |      |                    |     | GC_OR_START bit                                                   |
  +      +                    +     +                                                                   +
  |      |                    |     | Reset value: 0x0                                                  |
  +------+--------------------+-----+-------------------------------------------------------------------+
  | 10   | GC_OR_START        | R/W | If bit 11 (SPECIAL) is set to 1 and bit 13 (Device-ID) is set to 0|
  +      +                    +     +                                                                   +
  |      |                    |     | then this bit indicates whether a General Call or START byte      |
  +      +                    +     +                                                                   +
  |      |                    |     | command is to be performed by the DW_apb_i2c.                     |
  +      +                    +     +                                                                   +
  |      |                    |     | 0: General Call Address – after issuing a General Call, only      |
  +      +                    +     +                                                                   +
  |      |                    |     | writes may be performed. Attempting to issue a read command       |
  +      +                    +     +                                                                   +
  |      |                    |     | results in setting bit 6 (TX_ABRT) of the IC_RAW_INTR_STAT        |
  +      +                    +     +                                                                   +
  |      |                    |     | register. The DW_apb_i2c remains in General Call mode until       |
  +      +                    +     +                                                                   +
  |      |                    |     | the SPECIAL bit value (bit 11) is cleared.                        |
  +      +                    +     +                                                                   +
  |      |                    |     | 1: START BYTE                                                     |
  +      +                    +     +                                                                   +
  |      |                    |     | Reset value: 0x0                                                  |
  +------+--------------------+-----+-------------------------------------------------------------------+
  | 9:0  | IC_TAR             | R/W | This is the target address for any master transaction. When       |
  +      +                    +     +                                                                   +
  |      |                    |     | transmitting a General Call, these bits are ignored. To generate a|
  +      +                    +     +                                                                   +
  |      |                    |     | START BYTE, the CPU needs to write only once into these bits.     |
  +      +                    +     +                                                                   +
  |      |                    |     | Reset value: IC_DEFAULT_TAR_SLAVE_ADDR configuration parameter    |
  +      +                    +     +                                                                   +
  |      |                    |     | If the IC_TAR and IC_SAR are the same, loopback exists but the    |
  +      +                    +     +                                                                   +
  |      |                    |     | FIFOs are shared between master and slave, so full loopback is not|
  +      +                    +     +                                                                   +
  |      |                    |     | feasible. Only one direction loopback mode is supported (simplex),|
  +      +                    +     +                                                                   +
  |      |                    |     | not duplex. A master cannot transmit to itself; it can transmit to|
  +      +                    +     +                                                                   +
  |      |                    |     | only a slave.                                                     |
  +------+--------------------+-----+-------------------------------------------------------------------+

Note:It is not necessary to perform any write to this register if DW_apb_i2c is enabled as an I2C 
slave only

IC_SAR
""""""

- Name: I2C Slave Address Register
  
- Size: 10 bits

- Address Offset: 0x08
  
- Read/Write Access: Read/Write

.. table::  IC_SAR Register Fields

  +------+---------+----+-----------------------------------------------------------------------------------+
  | Bits | Name    | R/W| Description                                                                       |
  +------+---------+----+-----------------------------------------------------------------------------------+
  | 31:10| Reserved| N/A| Reserved                                                                          |
  +------+---------+----+-----------------------------------------------------------------------------------+
  | 9:0  | IC_SAR  | R/W| The IC_SAR holds the slave address when the I2C is operating as a slave. For 7-bit|
  +      +         +    +                                                                                   +
  |      |         |    | addressing, only IC_SAR[6:0] is used.                                             |
  +      +         +    +                                                                                   +
  |      |         |    | This register can be written only when the I2C interface is disabled, which       |
  +      +         +    +                                                                                   +     
  |      |         |    | corresponds to IC_ENABLE[0] being set to 0. Writes at other times have no effect. |
  +      +         +    +                                                                                   +
  |      |         |    | NOTE: The default values cannot be any of the reserved address locations: that is,|
  +      +         +    +                                                                                   +
  |      |         |    | 0x00 to 0x07, or 0x78 to 0x7f. The correct operation of the device is not         |
  +      +         +    +                                                                                   +
  |      |         |    | guaranteed if you program the IC_SAR or IC_TAR to a reserved value.               |
  +      +         +    +                                                                                   +
  |      |         |    | Reset value: IC_DEFAULT_SLAVE_ADDR configuration parameter                        |
  +------+---------+----+-----------------------------------------------------------------------------------+

Note:It is not necessary to perform any write to this register if DW_apb_i2c is enabled as an I2C 
master only

IC_HS_MADDR
"""""""""""

- Name: I2C High Speed Master Mode Code Address Register
  
- Size: 3 bits

- Address Offset: 0x0c
  
- Read/Write Access: Read/Write

This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE = 1).

.. table::  IC_HS_MADDR Register Fields

  +------+---------+----+-----------------------------------------------------------------------------------+
  | Bits | Name    | R/W| Description                                                                       |
  +------+---------+----+-----------------------------------------------------------------------------------+
  | 31:3 | Reserved| N/A| Reserved                                                                          |
  +------+---------+----+-----------------------------------------------------------------------------------+
  | 2:0  | IC_HS   | R/W| This bit field holds the value of the I2C HS mode master code. HS-mode master     |
  +      +         +    +                                                                                   +
  |      | _MAR    |    | codes are reserved 8-bit codes (00001xxx) that are not used for slave addressing  |
  +      +         +    +                                                                                   +
  |      |         |    | or other purposes. Each master has its unique master code; up to eight high       |
  +      +         +    +                                                                                   +
  |      |         |    | speed mode masters can be present on the same I2C bus system. Valid values        |
  +      +         +    +                                                                                   +
  |      |         |    | are from 0 to 7. This register goes away and becomes read-only returning 0’s if   |
  +      +         +    +                                                                                   +
  |      |         |    | the IC_MAX_SPEED_MODE configuration parameter is set to either Standard (1)       |
  +      +         +    +                                                                                   +
  |      |         |    | or Fast (2).                                                                      |
  +      +         +    +                                                                                   +
  |      |         |    | This register can be written only when the I2C interface is disabled, which       |
  +      +         +    +                                                                                   +
  |      |         |    | corresponds to IC_ENABLE[0] being set to 0. Writes at other times have no effect. |
  +      +         +    +                                                                                   +
  |      |         |    | Reset value: IC_HS_MASTER_CODE configuration parameter                            |
  +------+---------+----+-----------------------------------------------------------------------------------+

Note:It is not necessary to perform any write to this register if DW_apb_i2c is enabled as an I2C 
slave only.

IC_DATA_CMD
"""""""""""

- Name: I2C Rx/Tx Data Buffer and Command Register; this is the register the CPU writes to when filling the TX FIFO and the CPU reads from when retrieving bytes from RX FIFO

- Size:

  - Write

    - 11 bits when IC_EMPTYFIFO_HOLD_MASTER_EN=1
    
    - 9 bits when IC_EMPTYFIFO_HOLD_MASTER_EN=0

  - Read

    - 12 bits when IC_FIRST_DATA_BYTE_STATUS = 1

    - 8 bits when IC_FIRST_DATA_BYTE_STATUS = 0

- Address Offset: 0x10

- Read/Write Access: Read/Write 

Note:In order for the DW_apb_i2c to continue acknowledging reads, a read command should be 
written for every byte that is to be received; otherwise the DW_apb_i2c will stop 
acknowledging

.. table:: IC_DATA_CMD Register Fields

  +------+---------+----+-----------------------------------------------------------------------------------+
  | Bits | Name    | R/W| Description                                                                       |
  +------+---------+----+-----------------------------------------------------------------------------------+
  | 31:12| Reserved| N/A| Reserved                                                                          |
  +------+---------+----+-----------------------------------------------------------------------------------+
  | 11   | FIRST   | R  | Indicates the first data byte received after the address phase for receive        |
  +      +         +    +                                                                                   +
  |      | _DATA   |    | transfer in Master receiver or Slave receiver mode.                               |
  +      +         +    +                                                                                   +
  |      | _BYTE   |    | Reset value: 0x0                                                                  |
  +      +         +    +                                                                                   +
  |      |         |    | Dependencies: This Register bit value is applicable only when                     |
  +      +         +    +                                                                                   +
  |      |         |    | FIRST_DATA_BYTE_STATUS=1.                                                         |
  +      +         +    +                                                                                   +
  |      |         |    | Note: In case of APB_DATA_WIDTH=8:                                                |
  +      +         +    +                                                                                   +
  |      |         |    | 1.You must perform two APB Reads to IC_DATA_CMD to get status on 11 bit.          |
  +      +         +    +                                                                                   +
  |      |         |    | 2.To read the 11 bit, you must perform the first data byte read [7:0] (offset     |
  +      +         +    +                                                                                   +
  |      |         |    | 0x10) and then perform the second read[15:8](offset 0x11) to know the             |
  +      +         +    +                                                                                   +
  |      |         |    | status of 11 bit (whether the data received in previous read is a first data byte)|
  +      +         +    +                                                                                   +
  |      |         |    | 3.The 11th bit is an optional read field. You can ignore 2nd byte read [15:8] (   |
  +      +         +    +                                                                                   +
  |      |         |    | offset 0x11) if not interested in the FIRST_DATA_BYTE status.                     |
  +------+---------+----+-----------------------------------------------------------------------------------+
  | 10   | RESTART | W  | This bit controls whether a RESTART is issued before the byte is sent or received |
  +      +         +    +                                                                                   +
  |      |         |    | This bit is available only if IC_EMPTYFIFO_HOLD_MASTER_EN is configured to 1.     |
  +      +         +    +                                                                                   +
  |      |         |    | 1 - If IC_RESTART_EN is 1, a RESTART is issued before the data is                 |
  +      +         +    +                                                                                   +
  |      |         |    | sent/received (according to the value of CMD), regardless of whether or           |
  +      +         +    +                                                                                   +
  |      |         |    | not the transfer direction is changing from the previous command; if              |
  +      +         +    +                                                                                   +
  |      |         |    | IC_RESTART_EN is 0, a STOP followed by a START is issued instead.                 |
  +      +         +    +                                                                                   +
  |      |         |    | 0 - If IC_RESTART_EN is 1, a RESTART is issued only if the transfer               |
  +      +         +    +                                                                                   +
  |      |         |    | direction is changing from the previous command; if IC_RESTART_EN                 |
  +      +         +    +                                                                                   +
  |      |         |    | is 0, a STOP followed by a START is issued instead.                               |
  +------+---------+----+-----------------------------------------------------------------------------------+

.. table::

  +------+---------+----+-----------------------------------------------------------------------------------+
  | 9    | STOP    | W  | This bit controls whether a STOP is issued after the byte is sent or received.    |
  +      +         +    +                                                                                   +
  |      |         |    | This bit is available only if IC_EMPTYFIFO_HOLD_MASTER_EN is configured to 1.     |
  +      +         +    +                                                                                   +
  |      |         |    | 1 – STOP is issued after this byte, regardless of whether or not the              |
  +      +         +    +                                                                                   +
  |      |         |    | Tx FIFO is empty. If the Tx FIFO is not empty, the master immediately             |
  +      +         +    +                                                                                   +
  |      |         |    | tries to start a new transfer by issuing a START and arbitrating for the bus.     |
  +      +         +    +                                                                                   +
  |      |         |    | 0 – STOP is not issued after this byte, regardless of whether or not the          |
  +      +         +    +                                                                                   +
  |      |         |    | Tx FIFO is empty. If the Tx FIFO is not empty, the master continues the           |
  +      +         +    +                                                                                   +
  |      |         |    | current transfer by sending/receiving data bytes according to the value of        |
  +      +         +    +                                                                                   +
  |      |         |    | the CMD bit. If the Tx FIFO is empty, the master holds the SCL line low           |
  +      +         +    +                                                                                   +
  |      |         |    | and stalls the bus until a new command is available in the Tx FIFO.               |
  +------+---------+----+-----------------------------------------------------------------------------------+
  | 8    | CMD     | W  | This bit controls whether a read or a write is performed. This bit does not       |
  +      +         +    +                                                                                   +
  |      |         |    | control the direction when the DW_apb_i2c acts as a slave. It controls only       |
  +      +         +    +                                                                                   +
  |      |         |    | the direction when it acts as a master.                                           |
  +      +         +    +                                                                                   +
  |      |         |    | 1 = Read                                                                          |
  +      +         +    +                                                                                   +
  |      |         |    | 0 = Write                                                                         |
  +      +         +    +                                                                                   +
  |      |         |    | When a command is entered in the TX FIFO, this bit distinguishes the write        |
  +      +         +    +                                                                                   +
  |      |         |    | and read commands. In slave-receiver mode, this bit is a “don’t care”             |
  +      +         +    +                                                                                   +
  |      |         |    | because writes to this register are not required. In slave-transmitter mode, a "0"|
  +      +         +    +                                                                                   +
  |      |         |    | indicates that the data in IC_DATA_CMD is to be transmitted.                      |
  +      +         +    +                                                                                   +
  |      |         |    | When programming this bit, you should remember the following: attempting          |
  +      +         +    +                                                                                   +
  |      |         |    | to perform a read operation after a General Call command has been sent            |
  +      +         +    +                                                                                   +
  |      |         |    | results in a TX_ABRT interrupt (bit 6 of the IC_RAW_INTR_STAT register),          |
  +      +         +    +                                                                                   +
  |      |         |    | unless bit 11 (SPECIAL) in the IC_TAR register has been cleared.                  |
  +      +         +    +                                                                                   +
  |      |         |    | If a “1” is written to this bit after receiving a RD_REQ interrupt, then a        |
  +      +         +    +                                                                                   +
  |      |         |    | TX_ABRT interrupt occurs.                                                         |
  +      +         +    +                                                                                   +
  |      |         |    | Dependencies: This field is not applicable in Ultra-Fast speed mode (             |
  +      +         +    +                                                                                   +
  |      |         |    | IC_ULTRA_FAST_MODE=1)                                                             |
  +      +         +    +                                                                                   +
  |      |         |    | Reset value: 0x0                                                                  |
  +------+---------+----+-----------------------------------------------------------------------------------+
 
.. table::

  +------+---------+----+-----------------------------------------------------------------------------------+
  | 7:0  | DAT     | R/W| This register contains the data to be transmitted or received on the I2C bus.     |
  +      +         +    +                                                                                   +
  |      |         |    | If you are writing to this register and want to perform a read, bits 7:0 (DAT)    |
  +      +         +    +                                                                                   +
  |      |         |    | are ignored by the DW_apb_i2c. However, when you read this register,              |
  +      +         +    +                                                                                   +
  |      |         |    | these bits return the value of data received on the DW_apb_i2c interface.         |
  +      +         +    +                                                                                   +
  |      |         |    | Reset value: 0x0                                                                  |
  +------+---------+----+-----------------------------------------------------------------------------------+

IC_SS_SCL_HCNT
"""""""""""""""

- Name: Standard Speed I2C Clock SCL High Count Register
  
- Size: 16 bits
  
- Address Offset: 0x14
  
- Read/Write Access: Read/Write

This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE = 1).

.. table::  IC_SS_SCL_HCNT Register Fields

  +------+---------+------+---------------------------------------------------------------------------------+
  | Bits | Name    | R/W  | Description                                                                     |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 31:16| Reserved| N/A  | Reserved                                                                        |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 15:0 | IC_SS   | R/W^1| This register must be set before any I2C bus transaction can take place to      |
  +      +         +      +                                                                                 +
  |      | _SCL    |      | ensure proper I/O timing. This register sets the SCL clock high-period count    |
  +      +         +      +                                                                                 +
  |      | _HCNT   |      | for standard speed.                                                             |
  +      +         +      +                                                                                 +
  |      |         |      | This register can be written only when the I2C interface is disabled which      |
  +      +         +      +                                                                                 +
  |      |         |      | corresponds to IC_ENABLE[0] being set to 0. Writes at other times have no effect|
  +      +         +      +                                                                                 +
  |      |         |      | The minimum valid value is 6; hardware prevents values less than this being     |
  +      +         +      +                                                                                 +
  |      |         |      | written, and if attempted results in 6 being set. For designs with              |
  +      +         +      +                                                                                 +
  |      |         |      | APB_DATA_WIDTH = 8, the order of programming is important to ensure the         |
  +      +         +      +                                                                                 +
  |      |         |      | correct operation of the DW_apb_i2c. The lower byte must be programmed          |
  +      +         +      +                                                                                 +
  |      |         |      | first. Then the upper byte is programmed.                                       |
  +      +         +      +                                                                                 +
  |      |         |      | When the configuration parameter IC_HC_COUNT_VALUES is set to 1, this           |
  +      +         +      +                                                                                 +
  |      |         |      | register is read only.                                                          |
  +      +         +      +                                                                                 +
  |      |         |      | NOTE: This register must not be programmed to a value higher than 65525,        |
  +      +         +      +                                                                                 +
  |      |         |      | because DW_apb_i2c uses a 16-bit counter to flag an I2C bus idle condition      |
  +      +         +      +                                                                                 +
  |      |         |      | when this counter reaches a value of IC_SS_SCL_HCNT + 10.                       |
  +      +         +      +                                                                                 +
  |      |         |      | Reset value: IC_SS_SCL_HIGH_COUNT configuration parameter                       |
  +------+---------+------+---------------------------------------------------------------------------------+
  | Read-only if IC_HC_COUNT_VALUES = 1.                                                                    |
  +------+---------+------+---------------------------------------------------------------------------------+
 
IC_SS_SCL_LCNT
""""""""""""""

- Name: Standard Speed I2C Clock SCL Low Count Register

- Size: 16 bits

- Address Offset: 0x18

- Read/Write Access: Read/Write

This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE = 1).

.. table:: IC_SS_SCL_LCNT Register Fields

  +------+---------+------+---------------------------------------------------------------------------------+
  | Bits | Name    | R/W  | Description                                                                     |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 31:16| Reserved| N/A  | Reserved                                                                        |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 15:0 | IC_SS   | R/W^1| This register must be set before any I2C bus transaction can take place to      |
  +      +         +      +                                                                                 +
  |      | _SCL    |      | ensure proper I/O timing. This register sets the SCL clock low period count     |
  +      +         +      +                                                                                 +
  |      | _LCNT   |      | for standard speed.                                                             |
  +      +         +      +                                                                                 +
  |      |         |      | This register can be written only when the I2C interface is disabled which      |
  +      +         +      +                                                                                 +
  |      |         |      | corresponds to IC_ENABLE[0] being set to 0. Writes at other times have no effect|
  +      +         +      +                                                                                 +
  |      |         |      | The minimum valid value is 8; hardware prevents values less than this being     |
  +      +         +      +                                                                                 +
  |      |         |      | written, and if attempted, results in 8 being set. For designs with             |
  +      +         +      +                                                                                 +
  |      |         |      | APB_DATA_WIDTH = 8, the order of programming is important to ensure the         |
  +      +         +      +                                                                                 +
  |      |         |      | correct operation of the DW_apb_i2c. The lower byte must be programmed          |
  +      +         +      +                                                                                 +
  |      |         |      | first. Then the upper byte is programmed.                                       |
  +      +         +      +                                                                                 +
  |      |         |      | When the configuration parameter IC_HC_COUNT_VALUES is set to 1, this           |
  +      +         +      +                                                                                 +
  |      |         |      | register is read only.                                                          |
  +      +         +      +                                                                                 +
  |      |         |      | Reset value: IC_SS_SCL_LOW_COUNT configuration parameter                        |
  +------+---------+------+---------------------------------------------------------------------------------+
  | Read-only if IC_HC_COUNT_VALUES = 1.                                                                    |
  +------+---------+------+---------------------------------------------------------------------------------+

IC_FS_SCL_HCNT
"""""""""""""""

- Name: Fast Mode or Fast Mode Plus I2C Clock SCL High Count Register

- Size: 16 bits

- Address Offset: 0x1c

- Read/Write Access: Read/Write

This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE = 1).

.. table:: IC_FS_SCL_HCNT

  +------+---------+------+---------------------------------------------------------------------------------+
  | Bits | Name    | R/W  | Description                                                                     |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 31:16| Reserved| N/A  | Reserved                                                                        |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 15:0 | IC_FS   | R/W^1| This register must be set before any I2C bus transaction can take place to      |
  +      +         +      +                                                                                 +
  |      | _SCL    |      | ensure proper I/O timing. This register sets the SCL clock high-period count    |
  +      +         +      +                                                                                 +
  |      | _HCNT   |      | for fast mode or fast mode plus. It is used in high-speed mode to send the      |
  +      +         +      +                                                                                 +
  |      |         |      | Master Code and START BYTE or General CALL.                                     |
  +      +         +      +                                                                                 +
  |      |         |      | This register goes away and becomes read-only returning 0s if                   |
  +      +         +      +                                                                                 +
  |      |         |      | IC_MAX_SPEED_MODE = standard. This register can be written only when            |
  +      +         +      +                                                                                 +
  |      |         |      | the I2C interface is disabled, which corresponds to IC_ENABLE[0] being set      |
  +      +         +      +                                                                                 +
  |      |         |      | to 0. Writes at other times have no effect.                                     |
  +      +         +      +                                                                                 +
  |      |         |      | The minimum valid value is 6; hardware prevents values less than this being     |
  +      +         +      +                                                                                 +
  |      |         |      | written, and if attempted results in 6 being set. For designs with              |
  +      +         +      +                                                                                 +
  |      |         |      | APB_DATA_WIDTH == 8 the order of programming is important to ensure             |
  +      +         +      +                                                                                 +
  |      |         |      | the correct operation of the DW_apb_i2c. The lower byte must be                 |
  +      +         +      +                                                                                 +
  |      |         |      | programmed first. Then the upper byte is programmed.                            | 
  +      +         +      +                                                                                 +
  |      |         |      | When the configuration parameter IC_HC_COUNT_VALUES is set to 1, this           |
  +      +         +      +                                                                                 +
  |      |         |      | register is read only.                                                          |
  +      +         +      +                                                                                 +
  |      |         |      | Reset value: IC_FS_SCL_HIGH_COUNT configuration parameter                       |
  +------+---------+------+---------------------------------------------------------------------------------+
  | Read-only if IC_HC_COUNT_VALUES = 1.                                                                    |
  +------+---------+------+---------------------------------------------------------------------------------+
   
IC_FS_SCL_LCNT
""""""""""""""

- Name: Fast Mode or Fast Mode Plus I2C Clock SCL Low Count Register
  
- Size: 16 bits

- Address Offset: 0x20

- Read/Write Access: Read/Write
  
This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE = 1).

.. table:: IC_FS_SCL_LCNT Register Fields

  +------+---------+------+---------------------------------------------------------------------------------+
  | Bits | Name    | R/W  | Description                                                                     |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 31:16| Reserved| N/A  | Reserved                                                                        |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 15:0 | IC_FS   | R/W^1| This register must be set before any I2C bus transaction can take place to      |
  +      +         +      +                                                                                 +
  |      | _SCL    |      | ensure proper I/O timing. This register sets the SCL clock low period count     |
  +      +         +      +                                                                                 +
  |      | _LCNT   |      | for fast mode or fast mode plus. It is used in high-speed mode to send the      |
  +      +         +      +                                                                                 +
  |      |         |      | Master Code and START BYTE or General CALL.                                     |
  +      +         +      +                                                                                 +
  |      |         |      | This register goes away and becomes read-only returning 0s if                   |
  +      +         +      +                                                                                 +
  |      |         |      | IC_MAX_SPEED_MODE = standard.                                                   |
  +      +         +      +                                                                                 +
  |      |         |      | This register can be written only when the I2C interface is disabled, which     |
  +      +         +      +                                                                                 +
  |      |         |      | corresponds to IC_ENABLE[0] being set to 0. Writes at other times have no effect|
  +      +         +      +                                                                                 +
  |      |         |      | The minimum valid value is 8; hardware prevents values less than this being     |
  +      +         +      +                                                                                 +
  |      |         |      | written, and if attempted results in 8 being set. For designs with              |
  +      +         +      +                                                                                 +
  |      |         |      | APB_DATA_WIDTH = 8 the order of programming is important to ensure the          |
  +      +         +      +                                                                                 +
  |      |         |      | correct operation of the DW_apb_i2c. The lower byte must be programmed          |
  +      +         +      +                                                                                 +
  |      |         |      | first. Then the upper byte is programmed. If the value is less than 8 then the  |
  +      +         +      +                                                                                 +
  |      |         |      | count value gets changed to 8.                                                  |
  +      +         +      +                                                                                 +
  |      |         |      | When the configuration parameter IC_HC_COUNT_VALUES is set to 1, this           |
  +      +         +      +                                                                                 +
  |      |         |      | register is read only.                                                          |
  +      +         +      +                                                                                 +
  |      |         |      | Reset value: IC_FS_SCL_LOW_COUNT configuration parameter                        |
  +------+---------+------+---------------------------------------------------------------------------------+
  | Read-only if IC_HC_COUNT_VALUES = 1.                                                                    |
  +------+---------+------+---------------------------------------------------------------------------------+

IC_HS_SCL_HCNT
"""""""""""""""

- Name: High Speed I2C Clock SCL High Count Register
  
- Size: 16 bits
  
- Address Offset: 0x24
  
- Read/Write Access: Read/Write

This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE = 1).

.. table:: IC_HS_SCL_HCNT Register Fields

  +------+---------+------+---------------------------------------------------------------------------------+
  | Bits | Name    | R/W  | Description                                                                     |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 31:16| Reserved| N/A  | Reserved                                                                        |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 15:0 | IC_HS   | R/W^1| This register must be set before any I2C bus transaction can take place to      |
  +      +         +      +                                                                                 +
  |      | _SCL    |      | ensure proper I/O timing. This register sets the SCL clock high period count    |
  +      +         +      +                                                                                 +
  |      | _HCNT   |      | for high speed.                                                                 |
  +      +         +      +                                                                                 +
  |      |         |      | The SCL High time depends on the loading of the bus. For 100pF loading,         |
  +      +         +      +                                                                                 +
  |      |         |      | the SCL High time is 60ns; for 400pF loading, the SCL High time is 120ns.       |
  +      +         +      +                                                                                 +
  |      |         |      | This register goes away and becomes read-only returning 0s if                   |
  +      +         +      +                                                                                 +
  |      |         |      | IC_MAX_SPEED_MODE != high.                                                      |
  +      +         +      +                                                                                 +
  |      |         |      | This register can be written only when the I2C interface is disabled, which     |
  +      +         +      +                                                                                 +
  |      |         |      | corresponds to IC_ENABLE[0] being set to 0. Writes at other times have no effect|
  +      +         +      +                                                                                 +
  |      |         |      | The minimum valid value is 6; hardware prevents values less than this being     |
  +      +         +      +                                                                                 +
  |      |         |      | written, and if attempted results in 6 being set. For designs with              |
  +      +         +      +                                                                                 +
  |      |         |      | APB_DATA_WIDTH = 8 the order of programming is important to ensure the          |
  +      +         +      +                                                                                 +
  |      |         |      | correct operation of the DW_apb_i2c. The lower byte must be programmed          |
  +      +         +      +                                                                                 +
  |      |         |      | first. Then the upper byte is programmed.                                       |
  +      +         +      +                                                                                 +
  |      |         |      | When the configuration parameter IC_HC_COUNT_VALUES is set to 1, this           |
  +      +         +      +                                                                                 +
  |      |         |      | register is read only.                                                          |
  +      +         +      +                                                                                 +
  |      |         |      | Reset value: IC_HS_SCL_HIGH_COUNT configuration parameter                       |
  +------+---------+------+---------------------------------------------------------------------------------+
  | Read-only if IC_HC_COUNT_VALUES = 1.                                                                    |
  +------+---------+------+---------------------------------------------------------------------------------+

IC_HS_SCL_LCNT
"""""""""""""""

- Name: High Speed I2C Clock SCL Low Count Register
  
- Size: 16 bits
  
- Address Offset: 0x28
  
- Read/Write Access: Read/Write
  
This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE = 1).

.. table::  IC_HS_SCL_LCNT Register Fields

  +------+---------+------+---------------------------------------------------------------------------------+
  | Bits | Name    | R/W  | Description                                                                     |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 31:16| Reserved| N/A  | Reserved                                                                        |
  +------+---------+------+---------------------------------------------------------------------------------+
  | 15:0 | IC_HS   | R/W^1| This register must be set before any I2C bus transaction can take place to      |
  +      +         +      +                                                                                 +
  |      | _SCL    |      | ensure proper I/O timing. This register sets the SCL clock low period count     |
  +      +         +      +                                                                                 +
  |      | _LCNT   |      | for high speed.                                                                 |
  +      +         +      +                                                                                 +
  |      |         |      | The SCL low time depends on the loading of the bus. For 100pF loading, the      |
  +      +         +      +                                                                                 +
  |      |         |      | SCL low time is 160ns; for 400pF loading, the SCL low time is 320ns.            |
  +      +         +      +                                                                                 +
  |      |         |      | This register goes away and becomes read-only returning 0s if                   |
  +      +         +      +                                                                                 +
  |      |         |      | IC_MAX_SPEED_MODE != high.                                                      |
  +      +         +      +                                                                                 +
  |      |         |      | This register can be written only when the I2C interface is disabled, which     |
  +      +         +      +                                                                                 +
  |      |         |      | corresponds to IC_ENABLE[0] being set to 0. Writes at other times have no effect|
  +      +         +      +                                                                                 +
  |      |         |      | The minimum valid value is 8; hardware prevents values less than this being     |
  +      +         +      +                                                                                 +
  |      |         |      | written, and if attempted results in 8 being set. For designs with              |
  +      +         +      +                                                                                 +
  |      |         |      | APB_DATA_WIDTH == 8 the order of programming is important to ensure             |
  +      +         +      +                                                                                 +
  |      |         |      | the correct operation of the DW_apb_i2c. The lower byte must be                 |
  +      +         +      +                                                                                 +
  |      |         |      | programmed first. Then the upper byte is programmed. If the value is less       |
  +      +         +      +                                                                                 +
  |      |         |      | than 8 then the count value gets changed to 8.                                  |
  +      +         +      +                                                                                 +
  |      |         |      | When the configuration parameter IC_HC_COUNT_VALUES is set to 1, this           |
  +      +         +      +                                                                                 +
  |      |         |      | register is read only.                                                          |
  +      +         +      +                                                                                 +
  |      |         |      | Reset value: IC_HS_SCL_LOW_COUNT configuration parameter                        |
  +------+---------+------+---------------------------------------------------------------------------------+
  | Read-only if IC_HC_COUNT_VALUES = 1.                                                                    |
  +------+---------+------+---------------------------------------------------------------------------------+

IC_INTR_STAT
""""""""""""

- Name: I2C Interrupt Status Register

- Size: 15 bits
  
- Address Offset: 0x2C
  
- Read/Write Access: Read

Each bit in this register has a corresponding mask bit in the IC_INTR_MASK register. These bits are cleared
by reading the matching interrupt clear register. The unmasked raw versions of these bits are available in
the IC_RAW_INTR_STAT register.

.. table::  IC_INTR_STAT Register Fields

  +------+--------------+------+-------------------------------------------------------------------------------+
  | Bits | Name         | R/W  | Description                                                                   |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 31:15| Reserved     | N/A  | Reserved                                                                      |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 14   | R_SCL        | R    | See IC_RAW_INTR_STAT for a detailed description of this bit.                  |
  +      +              +      +                                                                               +
  |      | _STUCK       |      | Dependencies: This field is not applicable in Ultra-Fast speed mode (IC_ULTRA |
  +      +              +      +                                                                               +
  |      | _AT          |      | _FAST_MODE=1).                                                                |
  +      +              +      +                                                                               +
  |      | _LOW         |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 13   | R_MST_ON_HOLD| R    | See “IC_RAW_INTR_STAT” for a detailed description of this bit.                |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 12   | R_RESTART_DET| R    | See IC_RAW_INTR_STAT for a detailed description of these bits.                |
  +      +              +      +                                                                               +
  | 11   | R_GEN_CALL   |      | Dependencies: R_RX_DONE and R_RD_REQ are not applicable in                    |
  +      +              +      +                                                                               +
  | 10   | R_START_DET  |      | Ultra Fast speed mode (IC_ULTRA_FAST_MODE = 1).                               |
  +      +              +      +                                                                               +
  | 9    | R_STOP_DET   |      | Reset value: 0x0                                                              |
  +      +              +      +                                                                               +
  | 8    | R_ACTIVITY   |      |                                                                               |
  +      +              +      +                                                                               +
  | 7    | R_RX_DONE    |      |                                                                               |
  +      +              +      +                                                                               +
  | 6    | R_TX_ABRT    |      |                                                                               |
  +      +              +      +                                                                               +
  | 5    | R_RD_REQ     |      |                                                                               |
  +      +              +      +                                                                               +
  | 4    | R_TX_EMPTY   |      |                                                                               |
  +      +              +      +                                                                               +
  | 3    | R_TX_OVER    |      |                                                                               |
  +      +              +      +                                                                               +
  | 2    | R_RX_FULL    |      |                                                                               |
  +      +              +      +                                                                               +
  | 1    | R_RX_OVER    |      |                                                                               |
  +      +              +      +                                                                               +
  | 0    | R_RX_UNDER   |      |                                                                               |
  +------+--------------+------+-------------------------------------------------------------------------------+

IC_INTR_MASK
""""""""""""

- Name: I2C Interrupt Mask Register
  
- Size: 15 bits
  
- Address Offset: 0x30

- Read/Write Access: Read/Write
  
  - If configuration parameter IC_SLV_RESTART_DET = 0, bit 13 is read only.
    
  - If configuration parameter I2C_DYNAMIC_TAR_UPDATE = 0
   
     or IC_EMPTYFIFO_HOLD_MASTER_EN = 0, bit 14 is read only.

  - If configuration parameter IC_BUS_CLEAR_FEATURE = 0, bit 15 is read only.

These bits mask their corresponding interrupt status bits. This register is active low; a value of 0 masks the 
interrupt, whereas a value of 1 unmasks the interrupt.

.. table:: IC_INTR_MASK Register Fields

  +------+--------------+------+-------------------------------------------------------------------------------+
  | Bits | Name         | R/W  | Description                                                                   |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 31:15| Reserved     | N/A  | Reserved                                                                      |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 14   | M_SCL_STUCK  | R or | This bit masks the R_SCL_STUCK_AT_LOW interrupt bit in the                    |
  +      +              +      +                                                                               +
  |      | _AT_LOW      | R/W  | IC_INTR_STAT register                                                         |
  +      +              +      +                                                                               +
  |      |              |      | This bit is enabled only when IC_BUS_CLEAR_FEATURE = 1.                       |
  +      +              +      +                                                                               +
  |      |              |      | Dependencies: This field is not applicable in Ultra-Fast speed mode           |
  +      +              +      +                                                                               +
  |      |              |      | (IC_ULTRA_FAST_MODE=1)                                                        |
  +      +              +      +                                                                               +
  |      |              |      | Reset Value: 0x1                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 13   | M_MST_ON_HOLD| R or | This bit masks the R_MST_ON_HOLD interrupt bit in the IC_INTR_STAT register   |
  +      +              +      +                                                                               +
  |      |              | R/W  | Dependencies: If I2C_DYNAMIC_TAR_UPDATE = 1 and                               |
  +      +              +      +                                                                               +
  |      |              |      | IC_EMPTYFIFO_HOLD_MASTER_EN = 1, then M_MST_ON_HOLD is                        |
  +      +              +      +                                                                               +
  |      |              |      | read/write. Otherwise M_MST_ON_HOLD is read-only.                             |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 14’h8ff                                                          |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 12   | M_RESTART_DET| R or | This bit masks the R_RESTART_DET interrupt status bit in the                  |
  +      +              +      +                                                                               +
  |      |              | R/W  | IC_INTR_STAT register.                                                        |
  +      +              +      +                                                                               +
  |      |              |      | Dependencies: If IC_SLV_RESTART_DET_EN = 1, then                              |
  +      +              +      +                                                                               +
  |      |              |      | M_RESTART_DET is read/write. Otherwise M_RESTART_DET is read-only.            |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 14’h8ff                                                          |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 11   | M_GEN_CALL   | R/W  | These bits mask their corresponding interrupt status bits in the              |
  +      +              +      +                                                                               +
  | 10   | M_START_DET  |      | IC_INTR_STAT register.                                                        |
  +      +              +      +                                                                               +
  | 9    | M_STOP_DET   |      | Dependencies: M_RX_DONE and M_RD_REQ are not applicable in                    |
  +      +              +      +                                                                               +
  | 8    | M_ACTIVITY   |      | Ultra Fast speed mode (IC_ULTRA_FAST_MODE = 1).                               |
  +      +              +      +                                                                               +
  | 7    | M_RX_DONE    |      | Reset value: 14’h8ff                                                          |
  +      +              +      +                                                                               +
  | 6    | M_TX_ABRT    |      |                                                                               |
  +      +              +      +                                                                               +
  | 5    | M_RD_REQ     |      |                                                                               |
  +      +              +      +                                                                               +
  | 4    | M_TX_EMPTY   |      |                                                                               |
  +      +              +      +                                                                               +
  | 3    | M_TX_OVER    |      |                                                                               |
  +      +              +      +                                                                               +
  | 2    | M_RX_FULL    |      |                                                                               |
  +      +              +      +                                                                               +
  | 1    | M_RX_OVER    |      |                                                                               |
  +      +              +      +                                                                               +
  | 0    | M_RX_UNDER   |      |                                                                               |
  +------+--------------+------+-------------------------------------------------------------------------------+

IC_RAW_INTR_STAT
""""""""""""""""

- Name: I2C Raw Interrupt Status Register

- Size: 15 bits

- Address Offset: 0x34

- Read/Write Access: Read Unlike the IC_INTR_STAT register, these bits are not masked so they always show the true status of the DW_apb_i2c.

.. table::  IC_RAW_INTR_STAT Register Fields

  +------+--------------+------+-------------------------------------------------------------------------------+
  | Bits | Name         | R/W  | Description                                                                   |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 31:15| Reserved     | N/A  | Reserved                                                                      |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 14   | SCL_STUCK    | R    | Indicates whether the SCL Line is stuck at low for the                        |
  +      +              +      +                                                                               +
  |      | _AT_LOW      |      | IC_SCL_STUCK_LOW_TIMOUT number of ic_clk periods.                             |
  +      +              +      +                                                                               +
  |      |              |      | Enabled only when IC_BUS_CLEAR_FEATURE = 1                                    |
  +      +              +      +                                                                               +
  |      |              |      | Dependencies: This field is not applicable in Ultra-Fast speed mode (IC_ULTRA |
  +      +              +      +                                                                               +
  |      |              |      | _FAST_MODE=1)                                                                 |
  +      +              +      +                                                                               +
  |      |              |      | Reset Value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 13   | MST_ON_HOLD  | R    | Indicates whether a master is holding the bus and the Tx FIFO is empty.       |
  +      +              +      +                                                                               +
  |      |              |      | Enabled only when I2C_DYNAMIC_TAR_UPDATE = 1 and                              |
  +      +              +      +                                                                               +
  |      |              |      | IC_EMPTYFIFO_HOLD_MASTER_EN = 1                                               |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0X0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 12   | RESTART_DET  | R    | Indicates whether a RESTART condition has occurred on the I2C interface       |
  +      +              +      +                                                                               +
  |      |              |      | when DW_apb_i2c is operating in slave mode and the slave is the addressed     |
  +      +              +      +                                                                               +
  |      |              |      | slave                                                                         |
  +      +              +      +                                                                               +
  |      |              |      | Enabled only when IC_SLV_RESTART_DET_EN = 1                                   |
  +      +              +      +                                                                               +
  |      |              |      | NOTE: However, in high-speed mode or during a START BYTE transfer, the        |
  +      +              +      +                                                                               +
  |      |              |      | RESTART comes before the address field as per the I2C protocol. In this case, |
  +      +              +      +                                                                               +
  |      |              |      | the slave is not the addressed slave when the RESTART is issued, therefore    |
  +      +              +      +                                                                               +
  |      |              |      | DW_apb_i2c does not generate the RESTART_DET interrupt.                       |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 11   | GEN_CALL     | R    | Set only when a General Call address is received and it is acknowledged. It   |
  +      +              +      +                                                                               +
  |      |              |      | stays set until it is cleared either by disabling DW_apb_i2c or when the CPU  |
  +      +              +      +                                                                               +
  |      |              |      | reads bit 0 of the IC_CLR_GEN_CALL register. DW_apb_i2c stores the            |
  +      +              +      +                                                                               +
  |      |              |      | received data in the Rx buffer.                                               |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 10   | START_DET    | R    | Indicates whether a START or RESTART condition has occurred on the I2C        |
  +      +              +      +                                                                               +
  |      |              |      | interface regardless of whether DW_apb_i2c is operating in slave or master    |
  +      +              +      +                                                                               +
  |      |              |      | mode.                                                                         |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+

.. table::

  +------+--------------+------+-------------------------------------------------------------------------------+
  | 9    | STOP_DET     | R    | Indicates whether a STOP condition has occurred on the I2C interface          |
  +      +              +      +                                                                               +
  |      |              |      | regardless of whether DW_apb_i2c is operating in slave or master mode.        |
  +      +              +      +                                                                               +
  |      |              |      | In Slave Mode:                                                                |
  +      +              +      +                                                                               +
  |      |              |      | If IC_CON[7]=1'b1 (STOP_DET_IFADDRESSED), the STOP_DET                        |
  +      +              +      +                                                                               +
  |      |              |      | interrupt is generated only if the slave is addressed.                        |
  +      +              +      +                                                                               +
  |      |              |      | Note: During a general call address, this slave does not issue a              |
  +      +              +      +                                                                               +
  |      |              |      | STOP_DET interrupt if STOP_DET_IF_ADDRESSED=1'b1, even if the                 |
  +      +              +      +                                                                               +
  |      |              |      | slave responds to the general call address by generating ACK. The             |
  +      +              +      +                                                                               +
  |      |              |      | STOP_DET interrupt is generated only when the transmitted address             |
  +      +              +      +                                                                               +
  |      |              |      | matches the slave address (SAR).                                              |
  +      +              +      +                                                                               +
  |      |              |      | If IC_CON[7]=1'b0 (STOP_DET_IFADDRESSED), the STOP_DET                        |
  +      +              +      +                                                                               +
  |      |              |      | interrupt is issued irrespective of whether it is being addressed.            |
  +      +              +      +                                                                               +
  |      |              |      | In Master Mode:                                                               |
  +      +              +      +                                                                               +
  |      |              |      | If IC_CON[10]=1’b1 (STOP_DET_IF_MASTER_ACTIVE), the STOP_DET                  |
  +      +              +      +                                                                               +
  |      |              |      | interrupt is issued only if the master is active.                             |
  +      +              +      +                                                                               +
  |      |              |      | If IC_CON[10]=1’b0 (STOP_DET_IFADDRESSED), the STOP_DET                       |
  +      +              +      +                                                                               +
  |      |              |      | interrupt is issued irrespective of whether the master is active.             |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 8    | ACTIVITY     | R    | This bit captures DW_apb_i2c activity and stays set until it is cleared. There|
  +      +              +      +                                                                               +
  |      |              |      | are four ways to clear it:                                                    |
  +      +              +      +                                                                               +
  |      |              |      | Disabling the DW_apb_i2c                                                      |
  +      +              +      +                                                                               +
  |      |              |      | Reading the IC_CLR_ACTIVITY register                                          |
  +      +              +      +                                                                               +
  |      |              |      | Reading the IC_CLR_INTR register                                              |
  +      +              +      +                                                                               +
  |      |              |      | System reset                                                                  |
  +      +              +      +                                                                               +
  |      |              |      | Once this bit is set, it stays set unless one of the four methods is used to  |
  +      +              +      +                                                                               +
  |      |              |      | clear it. Even if the DW_apb_i2c module is idle, this bit remains set until   |
  +      +              +      +                                                                               +
  |      |              |      | cleared,indicating that there was activity on the bus.                        |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+

.. table::

  +------+--------------+------+-------------------------------------------------------------------------------+
  | 7    | RX_DONE      | R    | When the DW_apb_i2c is acting as a slave-transmitter, this bit is set to 1 if |
  +      +              +      +                                                                               +
  |      |              |      | the master does not acknowledge a transmitted byte. This occurs on the last   |
  +      +              +      +                                                                               +
  |      |              |      | byte of the transmission, indicating that the transmission is done.           |
  +      +              +      +                                                                               +
  |      |              |      | Dependencies: This field is not applicable in Ultra-Fast speed mode           |
  +      +              +      +                                                                               +
  |      |              |      | (IC_ULTRA_FAST_MODE=1)                                                        |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 6    | TX_ABRT      | R    | This bit indicates if DW_apb_i2c, as an I2C transmitter, is unable to complete|
  +      +              +      +                                                                               +
  |      |              |      | the intended actions on the contents of the transmit FIFO. This situation can |
  +      +              +      +                                                                               +
  |      |              |      | occur both as an I2C master or an I2C slave, and is referred to as a “transmit|
  +      +              +      +                                                                               +
  |      |              |      | abort”.                                                                       |
  +      +              +      +                                                                               +
  |      |              |      | When this bit is set to 1, the IC_TX_ABRT_SOURCE register indicates the       |
  +      +              +      +                                                                               +
  |      |              |      | reason why the transmit abort takes places.                                   |
  +      +              +      +                                                                               +
  |      |              |      | NOTE: The DW_apb_i2c flushes/resets/empties only the TX_FIFO whenever         |
  +      +              +      +                                                                               +
  |      |              |      | there is a transmit abort caused by any of the events tracked by the          |
  +      +              +      +                                                                               +
  |      |              |      | IC_TX_ABRT_SOURCE register. The Tx FIFO remains in this flushed state         |
  +      +              +      +                                                                               +
  |      |              |      | until the register IC_CLR_TX_ABRT is read. Once this read is performed, the   |
  +      +              +      +                                                                               +
  |      |              |      | Tx FIFO is then ready to accept more data bytes from the APB interface. RX    |
  +      +              +      +                                                                               +
  |      |              |      | FIFO is flushed because of TX_ABRT is controlled by the coreConsultant        |
  +      +              +      +                                                                               +
  |      |              |      | parameter IC_AVOID_RX_FIFO_FLUSH_ON_TX_ABRT.                                  |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+

.. table::

  +------+--------------+------+-------------------------------------------------------------------------------+
  | 5    | RD_REQ       | R    | This bit is set to 1 when DW_apb_i2c is acting as a slave and another I2C     |
  +      +              +      +                                                                               +
  |      |              |      | master is attempting to read data from DW_apb_i2c. The DW_apb_i2c holds the   |
  +      +              +      +                                                                               +
  |      |              |      | I2C bus in a wait state (SCL=0) until this interrupt is serviced, which means |
  +      +              +      +                                                                               +
  |      |              |      | that the slave has been addressed by a remote master that is asking for data  |
  +      +              +      +                                                                               +
  |      |              |      | to be transferred. The processor must respond to this interrupt and then write|
  +      +              +      +                                                                               +
  |      |              |      | the requested data to the IC_DATA_CMD register.This bit is set to 0 just after|
  +      +              +      +                                                                               +
  |      |              |      | the processor reads the IC_CLR_RD_REQ register.                               |
  +      +              +      +                                                                               +
  |      |              |      | Dependencies: This field is not applicable in Ultra-Fast speed mode           |
  +      +              +      +                                                                               +
  |      |              |      | (IC_ULTRA_FAST_MODE=1)                                                        |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 4    | TX_EMPTY     | R    | The behavior of the TX_EMPTY interrupt status differs based on the            |
  +      +              +      +                                                                               +
  |      |              |      | TX_EMPTY_CTRL selection in the IC_CON register.                               |
  +      +              +      +                                                                               +
  |      |              |      | When TX_EMPTY_CTRL = 0:                                                       |
  +      +              +      +                                                                               +
  |      |              |      | This bit is set to 1 when the transmit buffer is at or below the threshold    |
  +      +              +      +                                                                               +
  |      |              |      | value set in the IC_TX_TL register.                                           | 
  +      +              +      +                                                                               +
  |      |              |      | When TX_EMPTY_CTRL = 1:                                                       |
  +      +              +      +                                                                               +
  |      |              |      | This bit is set to 1 when the transmit buffer is at or below the threshold    |
  +      +              +      +                                                                               +
  |      |              |      | value set in the IC_TX_TL register and the transmission of the                |
  +      +              +      +                                                                               +
  |      |              |      | address/data from the internal shift register for the most recently popped    |
  +      +              +      +                                                                               +
  |      |              |      | command is completed.                                                         |
  +      +              +      +                                                                               +
  |      |              |      | It is automatically cleared by hardware when the buffer level goes above the  |
  +      +              +      +                                                                               +
  |      |              |      | threshold. When IC_ENABLE[0] is set to 0, the TX FIFO is flushed and held in  |
  +      +              +      +                                                                               +
  |      |              |      | reset.There the TX FIFO looks like it has no data within it,so this bit is set|
  +      +              +      +                                                                               +
  |      |              |      | to 1, provided there is activity in the master or slave state machines. When  |
  +      +              +      +                                                                               +
  |      |              |      | there is no longer any activity, then with ic_en=0, this bit is set to 0.     |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+

.. table::

  +------+--------------+------+-------------------------------------------------------------------------------+
  | 3    | TX_OVER      | R    | Set during transmit if the transmit buffer is filled to IC_TX_BUFFER_DEPTH    |
  +      +              +      +                                                                               +
  |      |              |      | and the processor attempts to issue another I2C command by writing to the     |
  +      +              +      +                                                                               +
  |      |              |      | IC_DATA_CMD register. When the module is disabled, this bit keeps its level   |
  +      +              +      +                                                                               +
  |      |              |      | until the master or slave state machines go into idle, and when ic_en goes to |
  +      +              +      +                                                                               +
  |      |              |      | 0, this interrupt is cleared.                                                 |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 2    | RX_FULL      | R    | Set when the receive buffer reaches or goes above the RX_TL threshold in the  |
  +      +              +      +                                                                               +
  |      |              |      | IC_RX_TL register. It is automatically cleared by hardware when buffer level  |
  +      +              +      +                                                                               +
  |      |              |      | goes below the threshold. If the module is disabled (IC_ENABLE[0]=0), the     |
  +      +              +      +                                                                               +
  |      |              |      | RX FIFO is flushed and held in reset;therefore the RX FIFO is not full.So this|
  +      +              +      +                                                                               +
  |      |              |      | bit is cleared once IC_ENABLE[0] is set to 0, regardless of the activity that |
  +      +              +      +                                                                               +
  |      |              |      | continues.                                                                    |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 1    | RX_OVER      | R    | Set if the receive buffer is completely filled to IC_RX_BUFFER_DEPTH and      |
  +      +              +      +                                                                               +
  |      |              |      | an additional byte is received from an external I2C device. The DW_apb_i2c    |
  +      +              +      +                                                                               +
  |      |              |      | acknowledges this,but any data bytes received after the FIFO is full are lost.|
  +      +              +      +                                                                               +
  |      |              |      | If the module is disabled (IC_ENABLE[0]=0), this bit keeps its level until the|
  +      +              +      +                                                                               +
  |      |              |      | master or slave state machines go into idle, and when ic_en goes to 0, this   |
  +      +              +      +                                                                               +
  |      |              |      | interrupt is cleared.                                                         |
  +      +              +      +                                                                               +
  |      |              |      | NOTE: If the configuration parameter IC_RX_FULL_HLD_BUS_EN is enabled         |
  +      +              +      +                                                                               +
  |      |              |      | and bit 9 of the IC_CON register (RX_FIFO_FULL_HLD_CTRL) is                   |
  +      +              +      +                                                                               +
  |      |              |      | programmed to HIGH, then the RX_OVER interrupt never occurs, because the      |
  +      +              +      +                                                                               +
  |      |              |      | Rx FIFO never overflows.                                                      |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+
  | 0    | RX_UNDER     | R    | Set if the processor attempts to read the receive buffer when it is empty by  |
  +      +              +      +                                                                               +
  |      |              |      | reading from the IC_DATA_CMD register. If the module is disabled              |
  +      +              +      +                                                                               +
  |      |              |      | (IC_ENABLE[0]=0), this bit keeps its level until the master or slave state    |
  +      +              +      +                                                                               +
  |      |              |      | machines go into idle, and when ic_en goes to 0, this interrupt is cleared.   |
  +      +              +      +                                                                               +
  |      |              |      | Reset value: 0x0                                                              |
  +------+--------------+------+-------------------------------------------------------------------------------+

IC_RX_TL
""""""""

- Name: I2C Receive FIFO Threshold Register
  
- Size: 8bits
  
- Address Offset: 0x38
  
- Read/Write Access: Read/Write

.. table::  IC_RX_TL Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:8 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 7:0  | RX_TL    | R/W  | Receive FIFO Threshold Level                                                        |
  +      +          +      +                                                                                     +
  |      |          |      | Controls the level of entries(or above)that triggers the RX_FULL interrupt (bit 2 in|
  +      +          +      +                                                                                     +
  |      |          |      | IC_RAW_INTR_STAT register). The valid range is 0-255, with the additional           |
  +      +          +      +                                                                                     +
  |      |          |      | restriction that hardware does not allow this value to be set to a value larger than|
  +      +          +      +                                                                                     +
  |      |          |      | the depth of the buffer.If an attempt is made to do that,the actual value set will  |
  +      +          +      +                                                                                     +
  |      |          |      | be the maximum depth of the buffer.                                                 |
  +      +          +      +                                                                                     +
  |      |          |      | A value of 0 sets the threshold for 1 entry, and a value of 255 sets the threshold  |
  +      +          +      +                                                                                     +
  |      |          |      | for 256 entries.                                                                    |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: IC_RX_TL configuration parameter                                       |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_TX_TL
""""""""

- Name: I2C Transmit FIFO Threshold Register
  
- Size: 8 bits

- Address Offset: 0x3c
  
- Read/Write Access: Read/Write

.. table::  IC_TX_TL Register Fields  

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:8 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 7:0  | TX_TL    | R/W  | Transmit FIFO Threshold Level                                                       |
  +      +          +      +                                                                                     +
  |      |          |      | Controls the level of entries(or below)that trigger the TX_EMPTY interrupt (bit 4 in|
  +      +          +      +                                                                                     +
  |      |          |      | IC_RAW_INTR_STAT register). The valid range is 0-255, with the additional.          |
  +      +          +      +                                                                                     +
  |      |          |      | restriction that it may not be set to value larger than the depth of the buffer.If  |
  +      +          +      +                                                                                     +
  |      |          |      | an attempt is made to do that, the actual value set will be the maximum depth       |
  +      +          +      +                                                                                     +
  |      |          |      | of the buffer.                                                                      |
  +      +          +      +                                                                                     +
  |      |          |      | A value of 0 sets the threshold for 0 entries, and a value of 255 sets the threshold|
  +      +          +      +                                                                                     +
  |      |          |      | for 256 entries.                                                                    |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: IC_TX_TL configuration parameter                                       |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_INTR
"""""""""""

- Name: Clear Combined and Individual Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0x40
  
- Read/Write Access: Read

.. table:: IC_CLR_INTR Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR_INTR | R    | Read this register to clear the combined interrupt,all individual interrupts,and the|
  +      +          +      +                                                                                     +
  |      |          |      | IC_TX_ABRT_SOURCE register. This bit does not clear hardware clearable              |
  +      +          +      +                                                                                     +
  |      |          |      | interrupts but software clearable interrupts. Refer to Bit 9 of the                 |
  +      +          +      +                                                                                     +
  |      |          |      | IC_TX_ABRT_SOURCE register for an exception to clearing IC_TX_ABRT_SOURCE.          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_RX_UNDER
"""""""""""""""

- Name: Clear RX_UNDER Interrupt Register
  
- Size: 1 bit

- Address Offset: 0x44
  
- Read/Write Access: Read

.. table:: IC_CLR_RX_UNDER Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR_RX   | R    | Read this register to clear the RX_UNDER interrupt (bit 0) of the                   |
  +      +          +      +                                                                                     +
  |      | _UNDER   |      | IC_RAW_INTR_STAT register.                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_RX_OVER
""""""""""""""

- Name: Clear RX_OVER Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0x48
  
- Read/Write Access: Read

.. table:: IC_CLR_RX_OVER Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR_RX   | R    | Read this register to clear the RX_OVER interrupt (bit 1) of the                    |
  +      +          +      +                                                                                     +
  |      | _OVER    |      | IC_RAW_INTR_STAT register.                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_TX_OVER
""""""""""""""

- Name: Clear TX_OVER Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0x4c
  
- Read/Write Access: Read
  
.. table:: IC_CLR_TX_OVER Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR_TX   | R    | Read this register to clear the TX_OVER interrupt (bit 3) of the                    |
  +      +          +      +                                                                                     +
  |      | _OVER    |      | IC_RAW_INTR_STAT register.                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_RD_REQ
"""""""""""""

- Name: Clear RD_REQ Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0x50
  
- Read/Write Access: Read
  
- Dependencies: This Register is not applicable in Ultra-Fast speed mode(IC_ULTRA_FAST_MODE=1)

.. table:: IC_CLR_RD_REQ Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR_RD   | R    | Read this register to clear the RD_REQ interrupt (bit 5) of the                     |
  +      +          +      +                                                                                     +
  |      | _REQ     |      | IC_RAW_INTR_STAT register.                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_TX_ABRT
""""""""""""""

- Name: Clear TX_ABRT Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0x54
  
- Read/Write Access: Read

.. table:: IC_CLR_TX_ABRT Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR_TX   | R    | Read this register to clear the TX_ABRT interrupt (bit 6) of the                    |
  +      +          +      +                                                                                     +
  |      | _ABRT    |      | IC_RAW_INTR_STAT register, and the IC_TX_ABRT_SOURCE register.                      |
  +      +          +      +                                                                                     +
  |      |          |      | This also releases the Tx FIFO from the flushed/reset state, allowing more          |
  +      +          +      +                                                                                     +
  |      |          |      | writes to the Tx FIFO.                                                              |
  +      +          +      +                                                                                     +
  |      |          |      | Refer to Bit 9 of the IC_TX_ABRT_SOURCE register for an exception to                |
  +      +          +      +                                                                                     +
  |      |          |      | clearing IC_TX_ABRT_SOURCE.                                                         |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_RX_DONE  
""""""""""""""

- Name: Clear RX_DONE Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0x58
  
- Read/Write Access: Read
  
- Dependencies: This Register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)

.. table:: IC_CLR_RX_DONE Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR_RX   | R    | Read this register to clear the RX_DONE interrupt (bit 7) of the                    |
  +      +          +      +                                                                                     +
  |      | _DONE    |      | IC_RAW_INTR_STAT register.                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_ACTIVITY
"""""""""""""""

- Name: Clear ACTIVITY Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0x5c
  
- Read/Write Access: Read

.. table:: IC_CLR_ACTIVITY Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR      | R    | Reading this register clears the ACTIVITY interrupt if the I2C is not active        |
  +      +          +      +                                                                                     +
  |      | _ACTIVITY|      | anymore. If the I2C module is still active on the bus, the ACTIVITY interrupt       |
  +      +          +      +                                                                                     +
  |      |          |      | bit continues to be set. It is automatically cleared by hardware if the module      |
  +      +          +      +                                                                                     +
  |      |          |      | is disabled and if there is no further activity on the bus. The value read from     |
  +      +          +      +                                                                                     +
  |      |          |      | this register to get status of the ACTIVITY interrupt (bit 8) of the                |
  +      +          +      +                                                                                     +
  |      |          |      | IC_RAW_INTR_STAT register.                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_STOP_DET
"""""""""""""""

- Name: Clear STOP_DET Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0x60
  
- Read/Write Access: Read

.. table:: IC_CLR_STOP_DET Register Fields
 
  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR_STOP | R    | Read this register to clear the STOP_DET interrupt (bit 9) of the                   |
  +      +          +      +                                                                                     +
  |      | _DET     |      | IC_RAW_INTR_STAT register.                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_START_DET
""""""""""""""""

- Name: Clear START_DET Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0x64
  
- Read/Write Access: Read

.. table:: IC_CLR_START_DET Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR_START| R    | Read this register to clear the START_DET interrupt (bit 10) of the                 |
  +      +          +      +                                                                                     +
  |      | _DET     |      | IC_RAW_INTR_STAT register.                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_CLR_GEN_CALL
"""""""""""""""

- Name: Clear GEN_CALL Interrupt Register
  
- Size: 1 bit

- Address Offset: 0x68
  
- Read/Write Access: Read

.. table:: IC_CLR_GEN_CALL Register Fields  

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | CLR_GEN  | R    | Read this register to clear the GEN_CALL interrupt (bit 11) of                      |
  +      +          +      +                                                                                     +
  |      | _CALL    |      | IC_RAW_INTR_STAT register.                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_ENABLE
"""""""""""

- Name: I2C Enable Register
  
- Size: 19 bits
  
- Address Offset: 0x6c
  
- Read/Write Access: Read/Write
  
  - Bit 2 is read only when IC_TX_CMD_BLOCK_DEFAULT=0
    
  - Bit 3 is read only when IC_BUS_CLEAR_FEATURE = 0
    
  - Bit 16 is read only when IC_SMBUS=0.
    
  - Bit 17 and 18 are read only when IC_SMBUS_SUSPEND_ALERT=0.

.. table:: IC_ENABLE Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:19| Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 18   | SMBUS    | R/W  | The SMBUS_ALERT_CTRL register bit is used to control assertion of SMBALERT signal.  |
  +      +          +      +                                                                                     +
  |      | _ALERT   |      | 1: Assert SMBALERT signal                                                           |
  +      +          +      +                                                                                     +
  |      | _EN      |      | This register bit is auto-cleared after detection of Acknowledgement from           |
  +      +          +      +                                                                                     +
  |      |          |      | master for Alert Response address.                                                  |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: This Register bit value is applicable only when                       |
  +      +          +      +                                                                                     +
  |      |          |      | IC_SMBUS_SUSPEND_ALERT=1                                                            |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 17   | SMBUS    | R/W  | The SMBUS_SUSPEND_EN register bit is used to control assertion and deassertion      |
  +      +          +      +                                                                                     +
  |      | _SUSPEND |      | of SMBSUS signal.                                                                   |
  +      +          +      +                                                                                     +
  |      | _EN      |      | 0: De-assert SMBSUS signal                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | 1: Assert SMBSUS signal                                                             |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: This Register bit value is applicable only when                       |
  +      +          +      +                                                                                     +
  |      |          |      | IC_SMBUS_SUSPEND_ALERT=1                                                            |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 16   | SMBUS    | R/W  | This bit is used in SMBus Host mode to initiate the SMBus Master Clock              |
  +      +          +      +                                                                                     +
  |      | _CLK     |      | Reset. This bit should be enabled only when Master is in idle. Whenever this        |
  +      +          +      +                                                                                     +
  |      | _RESET   |      | bit is enabled, the SMBCLK is held low for the IC_SCL_STUCK_TIMEOUT                 |
  +      +          +      +                                                                                     +
  |      |          |      | ic_clk cycles to reset the SMBus Slave devices.                                     |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: This Register bit value is applicable only when                       |
  +      +          +      +                                                                                     +
  |      |          |      | IC_SMBUS=1                                                                          |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 15:4 | Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+

.. table:: 

  +------+----------+------+-------------------------------------------------------------------------------------+
  | 3    | SDA_STUCK| R/W  | If SDA is stuck at low indicated through the TX_ABORT interrupt (                   |
  +      +          +      +                                                                                     +
  |      | _RECOVERY|      | IC_TX_ABRT_SOURCE[17]), then this bit is used as a control knob to initiate         |
  +      +          +      +                                                                                     +
  |      | _ENABLE  |      | the SDA Recovery Mechanism (that is, send at most 9 SCL clocks and STOP             |
  +      +          +      +                                                                                     +
  |      |          |      | to release the SDA line) and then this bit gets auto clear.                         |
  +      +          +      +                                                                                     +
  |      |          |      | This bit is enabled only when IC_BUS_CLEAR_FEATURE = 1.                             |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: This field is not applicable in Ultra-Fast speed mode (               |
  +      +          +      +                                                                                     +
  |      |          |      | IC_ULTRA_FAST_MODE=1)                                                               |
  +      +          +      +                                                                                     +
  |      |          |      | Reset Value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 2    | TX_CMD   | R/W  | In Master mode                                                                      |
  +      +          +      +                                                                                     +
  |      | _BLOCK   |      | 1’b1: Blocks the transmission of data on I2C bus even if Tx FIFO has data           |
  +      +          +      +                                                                                     +
  |      |          |      | to transmit.                                                                        |
  +      +          +      +                                                                                     +
  |      |          |      | 1’b0: The transmission of data starts on I2C bus automatically, as soon as          |
  +      +          +      +                                                                                     +
  |      |          |      | the first data is available in the Tx FIFO.                                         |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: IC_TX_CMD_BLOCK_DEFAULT                                                |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: This Register bit value is applicable only when                       |
  +      +          +      +                                                                                     +
  |      |          |      | IC_TX_CMD_BLOCK =1.                                                                 |
  +      +          +      +                                                                                     +
  |      |          |      | Note: To block the execution of Master commands, set the TX_CMD_BLOCK               |
  +      +          +      +                                                                                     +
  |      |          |      | bit only when Tx FIFO is empty (IC_STATUS[2]=1) and the master is in the            |
  +      +          +      +                                                                                     +
  |      |          |      | Idle state (IC_STATUS[5] == 0). Any further commands put in the Tx FIFO are         |
  +      +          +      +                                                                                     +
  |      |          |      | not executed until TX_CMD_BLOCK bit is unset.                                       |
  +------+----------+------+-------------------------------------------------------------------------------------+
  
.. table::

  +------+----------+------+-------------------------------------------------------------------------------------+
  | 1    | ABORT    | R/W  | When set, the controller initiates the transfer abort.                              |
  +      +          +      +                                                                                     +
  |      |          |      | 0: ABORT not initiated or ABORT done                                                |
  +      +          +      +                                                                                     +
  |      |          |      | 1: ABORT operation in progress                                                      |
  +      +          +      +                                                                                     +
  |      |          |      | The software can abort the I2C transfer in master mode by setting this bit. The     |
  +      +          +      +                                                                                     +
  |      |          |      | software can set this bit only when ENABLE is already set; otherwise, the           |
  +      +          +      +                                                                                     +
  |      |          |      | controller ignores any write to ABORT bit. The software cannot clear the            |
  +      +          +      +                                                                                     +
  |      |          |      | ABORT bit once set. In response to an ABORT, the controller issues a STOP           |
  +      +          +      +                                                                                     +
  |      |          |      | and flushes the Tx FIFO after completing the current transfer, then sets the        |
  +      +          +      +                                                                                     +
  |      |          |      | TX_ABORT interrupt after the abort operation. The ABORT bit is cleared              |
  +      +          +      +                                                                                     +
  |      |          |      | automatically after the abort operation.                                            |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | ENABLE   | R/W  | Controls whether the DW_apb_i2c is enabled.                                         |
  +      +          +      +                                                                                     +
  |      |          |      | 0: Disables DW_apb_i2c (TX and RX FIFOs are held in an erased state)                |
  +      +          +      +                                                                                     +
  |      |          |      | 1: Enables DW_apb_i2c                                                               |
  +      +          +      +                                                                                     +
  |      |          |      | Software can disable DW_apb_i2c while it is active. However, it is important        |
  +      +          +      +                                                                                     +
  |      |          |      | that care be taken to ensure that DW_apb_i2c is disabled properly.                  |
  +      +          +      +                                                                                     +
  |      |          |      | When DW_apb_i2c is disabled, the following occurs:                                  |
  +      +          +      +                                                                                     +
  |      |          |      | The TX FIFO and RX FIFO get flushed.                                                |
  +      +          +      +                                                                                     +
  |      |          |      | Status bits in the IC_INTR_STAT register are still active until DW_apb_i2c          |
  +      +          +      +                                                                                     +
  |      |          |      | goes into IDLE state.                                                               |
  +      +          +      +                                                                                     +
  |      |          |      | If the module is transmitting, it stops as well as deletes the contents of the      |
  +      +          +      +                                                                                     +
  |      |          |      | transmit buffer after the current transfer is complete. If the module is receiving, |
  +      +          +      +                                                                                     +
  |      |          |      | the DW_apb_i2c stops the current transfer at the end of the current byte and        |
  +      +          +      +                                                                                     +
  |      |          |      | does not acknowledge the transfer.                                                  |
  +      +          +      +                                                                                     +
  |      |          |      | In systems with asynchronous pclk and ic_clk when IC_CLK_TYPE                       |
  +      +          +      +                                                                                     +
  |      |          |      | parameter set to asynchronous (1), there is a two ic_clk delay when enabling        |
  +      +          +      +                                                                                     +
  |      |          |      | or disabling the DW_apb_i2c.                                                        |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_STATUS
"""""""""""

- Name: I2C Status Register
  
- Size: 32 bits
  
- Address Offset: 0x70
  
- Read/Write Access: Read
  
This is a read-only register used to indicate the current transfer status and FIFO status. The status register
may be read at any time. None of the bits in this register request an interrupt.When the I2C is disabled by writing 0 in bit 0 of the IC_ENABLE register:

- Bits 1 and 2 are set to 1
  
- Bits 3 to 10 are set to 0
  
When the master or slave state machines goes to idle and ic_en=0:

- Bits 5 and 6 are set to 0

.. table:: IC_STATUS Register Fields

  +------+----------+------+-------------------------------------------------------------------------------------+
  | Bits | Name     | R/W  | Description                                                                         |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 31:19| Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 20   | SMBUS    | R    | This bit indicates whether the status of the input signal is                        |
  +      +          +      +                                                                                     +
  |      | _ALERT   |      | ic_smbus_alert_in_n. This signal is asserted when the SMBus Alert                   |
  +      +          +      +                                                                                     +
  |      | _STATUS  |      | signal is asserted by the SMBus Device.                                             |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: Enabled only when                                                     |
  +      +          +      +                                                                                     +
  |      |          |      | IC_SMBUS_SUSPEND_ALERT=1 is set to 1.                                               |
  +      +          +      +                                                                                     +
  |      |          |      | Reset Value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 19   | SMBUS    | R    | This bit indicates whether the status of the input signal is                        |
  +      +          +      +                                                                                     +
  |      | _SUSPEND |      | ic_smbus_sus_in_n. This signal is asserted when the SMBus                           |
  +      +          +      +                                                                                     +
  |      | _STATUS  |      | Suspend signal is asserted by the SMBus Host.                                       |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: Enabled only when                                                     |
  +      +          +      +                                                                                     +
  |      |          |      | IC_SMBUS_SUSPEND_ALERT=1 is set to 1.                                               |
  +      +          +      +                                                                                     +
  |      |          |      | Reset Value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 18   | SMBUS    | R    | This bit indicates whether the SMBus Slave address (ic_sar[6:0]) is                 |
  +      +          +      +                                                                                     +
  |      | _SLAVE   |      | Resolved by ARP Master.                                                             |
  +      +          +      +                                                                                     +
  |      | _ADDR    |      | Dependencies: Enabled only when IC_SMBUS_ARP=1 is set to 1.                         |
  +      +          +      +                                                                                     +
  |      | _RESOLVED|      | Reset Value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 17   | SMBUS    | R    | This bit indicates whether the SMBus Slave address (ic_sar[6:0]) is                 |
  +      +          +      +                                                                                     +
  |      | _SLAVE   |      | valid or not.                                                                       |
  +      +          +      +                                                                                     +
  |      | _ADDR    |      | Dependencies: Enabled only when IC_SMBUS_ARP=1 is set to 1.                         |
  +      +          +      +                                                                                     +
  |      | _VALID   |      | Reset Value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 16   | SMBUS    | R    | This bit indicates the R/W bit of the Quick command received. This                  |
  +      +          +      +                                                                                     +
  |      | _QUICK   |      | bit will be cleared after the user has read this bit.                               |
  +      +          +      +                                                                                     +
  |      | _CMD     |      | Dependencies: Enabled only when IC_SMBUS=1 is set to 1.                             |
  +      +          +      +                                                                                     +
  |      | _BIT     |      | Reset Value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

.. table::

  +------+----------+------+-------------------------------------------------------------------------------------+
  | 15:12| Reserved | N/A  | Reserved                                                                            |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 11   | SDA_STUCK| R    | This bit indicates that an SDA stuck at low is not recovered after the              |
  +      +          +      +                                                                                     +
  |      | _NOT_RECO|      | recovery mechanism.                                                                 |
  +      +          +      +                                                                                     +
  |      | VERED    |      | This bit is enabled only when IC_BUS_CLEAR_FEATURE = 1.                             |
  +      +          +      +                                                                                     +
  |      |          |      | Reset Value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 10   | SLV_HOLD | R    | This bit indicates the BUS Hold in Slave mode due to the Rx FIFO                    |
  +      +          +      +                                                                                     +
  |      | _RX_FIFO |      | being Full and an additional byte being received (this kind of Bus                  |
  +      +          +      +                                                                                     +
  |      | _FULL    |      | hold is applicable if IC_RX_FULL_HLD_BUS_EN is set to 1).                           |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: This Register bit value is applicable only when                       |
  +      +          +      +                                                                                     +
  |      |          |      | IC_STAT_FOR_CLK_STRETCH=1.                                                          |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 9    | SLV_HOLD | R    | This bit indicates the BUS Hold in Slave mode for the Read request                  |
  +      +          +      +                                                                                     +
  |      | _TX_FIFO |      | when the Tx FIFO is empty. The Bus is in hold until the Tx FIFO has                 |
  +      +          +      +                                                                                     +
  |      | _EMPTY   |      | data to Transmit for the read request.                                              | 
  +      +          +      +                                                                                     +
  |      |          |      | Reset Value: 0x0                                                                    |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: This Register bit value is applicable only when                       |
  +      +          +      +                                                                                     +
  |      |          |      | IC_STAT_FOR_CLK_STRETCH=1.                                                          |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 8    | MST_HOLD | R    | This bit indicates the BUS Hold in Master mode due to Rx FIFO is                    |
  +      +          +      +                                                                                     +
  |      | _RX_FIFO |      | Full and additional byte has been received (This kind of Bus hold is                |
  +      +          +      +                                                                                     +
  |      | _FULL    |      | applicable if IC_RX_FULL_HLD_BUS_EN is set to 1).                                   |
  +      +          +      +                                                                                     +
  |      | _VALID   |      | Reset Value: 0x0                                                                    |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: This Register bit value is applicable only when                       |
  +      +          +      +                                                                                     +
  |      |          |      | IC_STAT_FOR_CLK_STRETCH=1                                                           |
  +------+----------+------+-------------------------------------------------------------------------------------+

.. table::

  +------+----------+------+-------------------------------------------------------------------------------------+
  | 7    | MST_HOLD |      | If the IC_EMPTYFIFO_HOLD_MASTER_EN parameter is set to 1,                           |
  +      +          +      +                                                                                     +
  |      | _TX_FIFO |      | the DW_apb_i2c master stalls the write transfer when Tx FIFO is                     |
  +      +          +      +                                                                                     +
  |      | _FULL    |      | empty, and the the last byte does not have the Stop bit set.                        |
  +      +          +      +                                                                                     +
  |      | _VALID   |      | This bit indicates the BUS hold when the master holds the bus                       |
  +      +          +      +                                                                                     +
  |      |          |      | because of the Tx FIFO being empty, and the the previous                            |
  +      +          +      +                                                                                     +
  |      |          |      | transferred command does not have the Stop bit set. (This kind of                   |
  +      +          +      +                                                                                     +
  |      |          |      | Bus hold is applicable if IC_EMPTYFIFO_HOLD_MASTER_EN is set to 1).                 |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +      +          +      +                                                                                     +
  |      |          |      | Dependencies: This Register bit value is applicable only when                       |
  +      +          +      +                                                                                     +
  |      |          |      | IC_STAT_FOR_CLK_STRETCH=1                                                           |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 6    | SLV      | R    | Slave FSM Activity Status. When the Slave Finite State Machine (FSM)                |
  +      +          +      +                                                                                     +
  |      | _ACTIVITY|      | is not in the IDLE state, this bit is set.                                          |
  +      +          +      +                                                                                     +
  |      |          |      | 0: Slave FSM is in IDLE state so the Slave part of DW_apb_i2c is not Active         |
  +      +          +      +                                                                                     +
  |      |          |      | 1: Slave FSM is not in IDLE state so the Slave part of DW_apb_i2c is Active         |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 5    | MST      | R    | Master FSM Activity Status. When the Master Finite State Machine (FSM)              |
  +      +          +      +                                                                                     +
  |      | _ACTIVITY|      | is not in the IDLE state, this bit is set.                                          |
  +      +          +      +                                                                                     +
  |      |          |      | 0: Master FSM is in IDLE state so the Master part of DW_apb_i2c is not Active       |
  +      +          +      +                                                                                     +
  |      |          |      | 1: Master FSM is not in IDLE state so the Master part of DW_apb_i2c is Active       |
  +      +          +      +                                                                                     +
  |      |          |      | NOTE: IC_STATUS[0]—that is, ACTIVITY bit—is the OR of                               |
  +      +          +      +                                                                                     +
  |      |          |      | SLV_ACTIVITY and MST_ACTIVITY bits.                                                 |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

.. table::

  +------+----------+------+-------------------------------------------------------------------------------------+
  | 4    | RFF      | R    | Receive FIFO Completely Full. When the receive FIFO is                              |
  +      +          +      +                                                                                     +
  |      |          |      | completely full, this bit is set. When the receive FIFO contains one                |
  +      +          +      +                                                                                     +
  |      |          |      | or more empty location, this bit is cleared.                                        |
  +      +          +      +                                                                                     +
  |      |          |      | 0: Receive FIFO is not full                                                         |
  +      +          +      +                                                                                     +
  |      |          |      | 1: Receive FIFO is full                                                             |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 3    | RFNE     | R    | Receive FIFO Not Empty. This bit is set when the receive FIFO                       |
  +      +          +      +                                                                                     +
  |      |          |      | contains one or more entries; it is cleared when the receive FIFO is empty.         |
  +      +          +      +                                                                                     +
  |      |          |      | 0: Receive FIFO is empty                                                            |
  +      +          +      +                                                                                     +
  |      |          |      | 1: Receive FIFO is not empty                                                        |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 2    | TFE      | R    | Transmit FIFO Completely Empty. When the transmit FIFO is                           |
  +      +          +      +                                                                                     +
  |      |          |      | completely empty, this bit is set. When it contains one or more valid               |
  +      +          +      +                                                                                     +
  |      |          |      | entries, this bit is cleared. This bit field does not request an interrupt.         |
  +      +          +      +                                                                                     +
  |      |          |      | 0: Transmit FIFO is not empty                                                       |
  +      +          +      +                                                                                     +
  |      |          |      | 1: Transmit FIFO is empty                                                           |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x1                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 1    | TFNF     | R    | Transmit FIFO Not Full. Set when the transmit FIFO contains one or                  |
  +      +          +      +                                                                                     +
  |      |          |      | more empty locations, and is cleared when the FIFO is full.                         |
  +      +          +      +                                                                                     +
  |      |          |      | 0: Transmit FIFO is full                                                            |
  +      +          +      +                                                                                     +
  |      |          |      | 1: Transmit FIFO is not full                                                        |
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x1                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+
  | 0    | ACTIVITY | R    | I2C Activity Status.                                                                |  
  +      +          +      +                                                                                     +
  |      |          |      | Reset value: 0x0                                                                    |
  +------+----------+------+-------------------------------------------------------------------------------------+

IC_TXFLR
"""""""""

- Name: I2C Transmit FIFO Level Register
  
- Size: TX_ABW + 1
  
- Address Offset: 0x74
  
- Read/Write Access: Read
  
This register contains the number of valid data entries in the transmit FIFO buffer. It is cleared whenever:

- The I2C is disabled
  
- There is a transmit abort—that is, TX_ABRT bit is set in the IC_RAW_INTR_STAT register
  
- The slave bulk transmit mode is aborted

The register increments whenever data is placed into the transmit FIFO and decrements when data is taken
from the transmit FIFO.

.. table:: IC_TXFLR Register Fields

  +------------+----------+------+-------------------------------------------------------------------------------------+
  | Bits       | Name     | R/W  | Description                                                                         |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 31:TX_ABW+1| Reserved | N/A  | Reserved                                                                            |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | TX_ABW:0   | TXFLR    | R    | Transmit FIFO Level. Contains the number of valid data entries in the               |
  +            +          +      +                                                                                     +
  |            |          |      | transmit FIFO.                                                                      |
  +            +          +      +                                                                                     +
  |            |          |      | Reset value: 0x0                                                                    |
  +------------+----------+------+-------------------------------------------------------------------------------------+

IC_RXFLR
""""""""

- Name: I2C Receive FIFO Level Register
  
- Size: RX_ABW + 1
  
- Address Offset: 0x78
  
- Read/Write Access: Read
  
This register contains the number of valid data entries in the receive FIFO buffer. It is cleared whenever:

- The I2C is disabled
  
- Whenever there is a transmit abort caused by any of the events tracked in IC_TX_ABRT_SOURCE The register increments whenever data is placed into the receive FIFO and decrements when data is taken from the receive FIFO.

.. table::  IC_RXFLR Register Fields

  +------------+----------+------+-------------------------------------------------------------------------------------+
  | Bits       | Name     | R/W  | Description                                                                         |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 31:RX_ABW+1| Reserved | N/A  | Reserved                                                                            |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | RX_ABW:0   | RXFLR    | R    | Receive FIFO Level. Contains the number of valid data entries in the                |
  +            +          +      +                                                                                     +
  |            |          |      | receive FIFO.                                                                       |
  +            +          +      +                                                                                     +
  |            |          |      | Reset value: 0x0                                                                    |
  +------------+----------+------+-------------------------------------------------------------------------------------+

IC_SDA_HOLD
"""""""""""

- Name: I2C SDA Hold Time Length Register

- Size: 24 bits
  
- Address Offset: 0x7C
  
- Read/Write Access: Read/Write
  
The bits [15:0] of this register are used to control the hold time of SDA during transmit in both slave and
master mode (after SCL goes from HIGH to LOW).

The bits [23:16] of this register rare used to extend the SDA transition (if any) whenever SCL is HIGH in the
receiver in either master or slave mode.

Writes to this register succeed only when IC_ENABLE[0]=0.

The values in this register are in units of ic_clk period. The value programmed in IC_SDA_TX_HOLD must
be greater than the minimum hold time in each mode —one cycle in master mode, seven cycles in slave
mode —for the value to be implemented.

The programmed SDA hold time during transmit (IC_SDA_TX_HOLD) cannot exceed at any time the
duration of the low part of scl. Therefore the programmed value cannot be larger than N_SCL_LOW-2,
where N_SCL_LOW is the duration of the low part of the scl period measured in ic_clk cycles.

.. table:: IC_SDA_HOLD Register Fields

  +------------+----------+------+-------------------------------------------------------------------------------------+
  | Bits       | Name     | R/W  | Description                                                                         |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 31:24      | Reserved | N/A  | Reserved                                                                            |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 23:16      | IC_SDA   | R/W  | Sets the required SDA hold time in units of ic_clk period, when                     |
  +            +          +      +                                                                                     +
  |            | _RX_HOLD |      | DW_apb_i2c acts as a reciever.                                                      |
  +            +          +      +                                                                                     +
  |            |          |      | Reset value: IC_DEFAULT_SDA_HOLD                                                    |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 15:0       | IC_SDA   | R/W  | Sets the required SDA hold time in units of ic_clk period, when                     |
  +            +          +      +                                                                                     +
  |            | _TX_HOLD |      | DW_apb_i2c acts as a transmitter.                                                   |
  +            +          +      +                                                                                     +
  |            |          |      | Reset value: IC_DEFAULT_SDA_HOLD                                                    |
  +------------+----------+------+-------------------------------------------------------------------------------------+

IC_TX_ABRT_SOURCE
"""""""""""""""""

- Name: I2C Transmit Abort Source Register
  
- Size: 32 bits
  
- Address Offset: 0x80
  
- Read/Write Access: Read

This register has 32 bits that indicate the source of the TX_ABRT bit. Except for Bit 9, this register is cleared
whenever the IC_CLR_TX_ABRT register or the IC_CLR_INTR register is read. To clear Bit 9, the source of
the ABRT_SBYTE_NORSTRT must be fixed first; RESTART must be enabled (IC_CON[5]=1), the SPECIAL
bit must be cleared (IC_TAR[11]), or the GC_OR_START bit must be cleared (IC_TAR[10]).

Once the source of the ABRT_SBYTE_NORSTRT is fixed, then this bit can be cleared in the same manner as
other bits in this register. If the source of the ABRT_SBYTE_NORSTRT is not fixed before attempting to clear
this bit, Bit 9 clears for one cycle and is then re-asserted.

.. table::  IC_TX_ABRT_SOURCE Register Fields

  +------+----------+----+-------------------------------------------------+---------------------+
  | Bits | Name     | R/W| Description                                     | Role of DW_apb_i2c  |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 31:23| TX_FLUSH | R  | This field indicates the number of Tx FIFO data | Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      | _CNT     |    | commands that are flushed due to TX_ABRT        | or Slave-Transmitter|
  +      +          +    +                                                 +                     +
  |      |          |    | interrupt. It is cleared whenever I2C is        |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | disabled.                                       |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 22:21| Reserved | R  | These bits are reserved.                        |                     | 
  +------+----------+----+-------------------------------------------------+---------------------+
  | 20   | ABRT     | R  | This is a master-mode-only bit. Master is       | Master              |
  +      +          +    +                                                 +                     +
  |      | _DEVICE  |    | initiating the DEVICE_ID transfer and the Tx    |                     |
  +      +          +    +                                                 +                     +
  |      | _WRITE   |    | FIFO consists of write commands.                |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset Value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 19   | ABRT     | R  | This is a master-mode-only bit. Master is       | Master              |
  +      +          +    +                                                 +                     +
  |      | _DEVICE  |    | initiating the DEVICE_ID transfer and the slave |                     |
  +      +          +    +                                                 +                     +
  |      | _SLVADDR |    | address sent was not acknowledged by any slave  |                     |
  +      +          +    +                                                 +                     +
  |      | _NOACK   |    | Reset Value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 18   | ABRT     | R  | This is a master-mode-only bit. Master initiates| Master              |
  +      +          +    +                                                 +                     +
  |      | _DEVICE  |    | the DEVICE_ID transfer and the device ID sent   |                     |
  +      +          +    +                                                 +                     +
  |      | _NOACK   |    | is not acknowledged by any slave.               |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 17   | ABRT_SDA | R  | This is a master-mode-only bit. Master detects  | Master              |
  +      +          +    +                                                 +                     +
  |      | _STUCK   |    | the SDA is Stuck at low for the                 |                     |
  +      +          +    +                                                 +                     +
  |      | _AT_LOW  |    | IC_SDA_STUCK_AT_LOW_TIMEOUT value of ic_clks.   |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 16   | ABRT_USER| R  | This is a master-mode-only bit. Master has      | Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      | _ABRT    |    | detected the transfer abort (IC_ENABLE[1]).     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+

.. table::

  +------+----------+----+-------------------------------------------------+---------------------+
  | 15   | ABRT     | R  | 1: When the processor side responds to a        | Slave-Transmitter   |
  +      +          +    +                                                 +                     +
  |      | _SLVRD   |    | slave mode request for data to be transmitted   |                     |
  +      +          +    +                                                 +                     +
  |      | _INTX    |    | to a remote master and user writes a 1 in CMD ( |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | bit 8) of IC_DATA_CMD register.                 |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 14   | ABRT_SLV | R  | 1: Slave lost the bus while transmitting data   | Slave-Transmitter   |
  +      +          +    +                                                 +                     +
  |      | _ARBLOST |    | to a remote master.                             |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | IC_TX_ABRT_SOURCE[12] is set at the same time.  |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | NOTE: Even though the slave never “owns” the    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | bus, something could go wrong on the bus.       |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | This is a fail safe check.For instance, during a|                     |
  +      +          +    +                                                 +                     +
  |      |          |    | data transmission at the low-to-high transition |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | of SCL,if what is on the data bus is not what is|                     |
  +      +          +    +                                                 +                     +
  |      |          |    | supposed to be transmitted, then DW_apb_i2c     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | no longer own the bus.                          |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 13   | ABRT     | R  | 1: Slave has received a read command and        | Slave-Transmitter   |
  +      +          +    +                                                 +                     +
  |      | _SLVFLUSH|    | some data exists in the TX FIFO so the          |                     |
  +      +          +    +                                                 +                     +
  |      | _TXFIFO  |    | slave issues a TX_ABRT interrupt to flush       |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | old data in TX FIFO.                            |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+

.. table::

  +------+----------+----+-------------------------------------------------+---------------------+
  | 12   | ARB_LOST | R  | 1:Master has lost arbitration, or if            | Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      |          |    | IC_TX_ABRT_SOURCE[14] is also set,              | or Slave-Transmitter|
  +      +          +    +                                                 +                     +
  |      |          |    | then the slave transmitter has lost arbitration.|                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 11   | ABRT     | R  | 1:User tries to initiate a Master operation     | Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      | _MASTER  |    | with the Master mode disabled.                  | or Master-Receiver  |
  +      +          +    +                                                 +                     +
  |      | _DIS     |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 10   | ABRT_10B | R  | 1:The restart is disabled                       | Master-Receiver     |
  +      +          +    +                                                 +                     +
  |      | _RD      |    | (IC_RESTART_EN bit (IC_CON[5]) = 0)             |                     |
  +      +          +    +                                                 +                     +
  |      | _NORSTRT |    | and the master sends a read command in          |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | 10-bit addressing mode.                         |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependencies: This field is not applicable in   |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1).   |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+

.. table::
  
  +------+----------+----+-------------------------------------------------+---------------------+
  | 9    | ABRT     | R  | To clear Bit 9, the source of the               | Master              |
  +      +          +    +                                                 +                     +
  |      | _SBYTE   |    | ABRT_SBYTE_NORSTRT must be fixed first;         |                     |
  +      +          +    +                                                 +                     +
  |      | _NORSTRT |    | restart must be enabled (IC_CON[5]=1), the      |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | SPECIAL bit must be cleared (IC_TAR[11]), or    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | the GC_OR_START bit must be cleared (IC_TAR[10])|                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Once the source of the ABRT_SBYTE_NORSTRT is    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | fixed,then this bit can be cleared in the same  |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | manner as other bits in this register. If the   |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | source of the ABRT_SBYTE_NORSTRT is not fixed   |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | before attempting to clear this bit,bit 9 clears|                     |
  +      +          +    +                                                 +                     +
  |      |          |    | for one cycle and then gets re-asserted.        |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | 1:The restart is disabled (IC_RESTART_EN        |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | bit (IC_CON[5]) = 0) and the user is trying to  |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | send a START Byte.                              |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 8    | ABRT_HS  | R  | 1: The restart is disabled (IC_RESTART_EN bit ( | Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      | _NORSTRT |    | IC_CON[5]) = 0) and the user is trying to use   | or Master-Receiver  |
  +      +          +    +                                                 +                     +
  |      |          |    | the master to transfer data in High Speed mode. |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 7    | ABRT     | R  | 1: Master has sent a START Byte and the START   | Master              |
  +      +          +    +                                                 +                     +
  |      | _SBYTE   |    | Byte was acknowledged (wrong behavior).         |                     |
  +      +          +    +                                                 +                     +
  |      | _ACKDET  |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
   
.. table::

  +------+----------+----+-------------------------------------------------+---------------------+
  | 6    | ABRT_HS  | R  | 1: Master is in High Speed mode and the High    | Master              |
  +      +          +    +                                                 +                     +
  |      | _ACKDET  |    | Speed Master code was acknowledged (wrong       |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | behavior).                                      |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 5    | ABRT     | R  | 1: DW_apb_i2c in master mode sent a General Call| Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      | _GCALL   |    | but the user programmed the byte following the  |                     |
  +      +          +    +                                                 +                     +
  |      | _READ    |    | General Call to be a read rom the bus (IC_DATA  |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | _CMD[9] is set to 1).                           |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+ 
  | 4    | ABRT     | R  | 1: DW_apb_i2c in master mode sent a General Call| Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      | _GCALL   |    | and no slave on the bus acknowledged the General|                     |
  +      +          +    +                                                 +                     +
  |      | _NOACK   |    | Call.                                           |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+

.. table:: 

  +------+----------+----+-------------------------------------------------+---------------------+
  | 3    | ABRT     | R  | 1: This is a master-mode only bit. Master       | Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      | _TXDATA  |    | has received an acknowledgement for the         |                     |
  +      +          +    +                                                 +                     +
  |      | _NOACK   |    | address, but when it sent data byte(s)          |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | following the address, it did not receive an    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | acknowledge from the remote slave(s).           |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 2    | ABRT     | R  | 1: Master is in 10-bit address mode and the     | Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      | _10ADDR2 |    | second address byte of the 10-bit address       | or Master-Receiver  |
  +      +          +    +                                                 +                     +
  |      | _NOACK   |    | was not acknowledged by any slave.              |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 1    | ABRT     | R  | 1: Master is in 10-bit address mode and the     | Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      | _10ADDR1 |    | first 10-bit address byte was not               | or Master-Receiver  |
  +      +          +    +                                                 +                     +
  |      | _NOACK   |    | acknowledged by any slave.                      |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+
  | 0    | ABRT_7B  | R  | 1: Master is in 10-bit address mode and the     | Master-Transmitter  |
  +      +          +    +                                                 +                     +
  |      | _ADDR    |    | the address sent was not acknowledged by        | or Master-Receiver  |
  +      +          +    +                                                 +                     +
  |      | _NOACK   |    | any slave.                                      |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Dependency: This field is not applicable in     |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)    |                     |
  +      +          +    +                                                 +                     +
  |      |          |    | Reset value: 0x0                                |                     |
  +------+----------+----+-------------------------------------------------+---------------------+

IC_SLV_DATA_NACK_ONLY
"""""""""""""""""""""

- Name: Generate Slave Data NACK Register
  
- Size: 1 bit
  
- Address Offset: 0x84
  
- Read/Write Access: Read/Write
  
- Dependency: This Register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1).

The register is used to generate a NACK for the data part of a transfer when DW_apb_i2c is acting as a
slave-receiver. This register only exists when the IC_SLV_DATA_NACK_ONLY parameter is set to 1. When
this parameter disabled, this register does not exist and writing to the register’s address has no effect.

A write can occur on this register if both of the following conditions are met:

- DW_apb_i2c is disabled (IC_ENABLE[0] = 0)
  
- Slave part is inactive (IC_STATUS[6] = 0)

Note:The IC_STATUS[6] is a register read-back location for the internal slv_activity signal; the user 
should poll this before writing the ic_slv_data_nack_only bit.

.. table:: IC_SLV_DATA_NACK_ONLY Register Fields
 
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | Bits       | Name     | R/W  | Description                                                                         |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1       | Reserved | N/A  | Reserved                                                                            |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 0          | NACK     | R/W  | Generate NACK. This NACK generation only occurs when DW_apb_i2c is a slave          |
  +            +          +      +                                                                                     +
  |            | _RX_HOLD |      | receiver.If this register is set to a value of 1,it can only generate a NACK after a|
  +            +          +      +                                                                                     +
  |            |          |      | data byte is received; hence, the data transfer is aborted and the data received is |
  +            +          +      +                                                                                     +
  |            |          |      | not pushed to the receive buffer.                                                   |
  +            +          +      +                                                                                     +
  |            |          |      | When the register is set to a value of 0, it generates NACK/ACK, depending on       | 
  +            +          +      +                                                                                     +
  |            |          |      | normal criteria.                                                                    |
  +            +          +      +                                                                                     +
  |            |          |      | 1 = generate NACK after data byte received                                          |
  +            +          +      +                                                                                     +
  |            |          |      | 0 = generate NACK/ACK normally                                                      |
  +            +          +      +                                                                                     +
  |            |          |      | Reset value: 0x0                                                                    |
  +------------+----------+------+-------------------------------------------------------------------------------------+

IC_DMA_CR
"""""""""

- Name: DMA Control Register
  
- Size: 2 bits
  
- Address Offset: 0x88
  
- Read/Write Access: Read/Write

  This register is only valid when DW_apb_i2c is configured with a set of DMA Controller interface signals(IC_HAS_DMA = 1). When DW_apb_i2c is not configured for DMA operation, this register does not exist and writing to the register’s address has no effect and reading from this register address will return zero.The register is used to enable the DMA Controller interface operation. There is a separate bit for transmit and receive. This can be programmed regardless of the state of IC_ENABLE.

.. table:: IC_DMA_CR Register Fields

  +------------+----------+------+-------------------------------------------------------------------------------------+
  | Bits       | Name     | R/W  | Description                                                                         |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 31:2       | Reserved | N/A  | Reserved                                                                            |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 1          | TDMAE    | R/W  | Transmit DMA Enable. This bit enables/disables the transmit FIFO DMA channel.       |
  +            +          +      +                                                                                     +
  |            |          |      | 0 = Transmit DMA disabled                                                           |
  +            +          +      +                                                                                     +
  |            |          |      | 1 = Transmit DMA enabled                                                            |
  +            +          +      +                                                                                     +
  |            |          |      | Reset value: 0x0                                                                    |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 0          | RDMAE    | R/W  | Receive DMA Enable. This bit enables/disables the receive FIFO DMA channel.         |
  +            +          +      +                                                                                     +
  |            |          |      | 0 = Receive DMA disabled                                                            |
  +            +          +      +                                                                                     +
  |            |          |      | 1 = Receive DMA enabled                                                             |
  +            +          +      +                                                                                     +
  |            |          |      | Reset value: 0x0                                                                    |
  +------------+----------+------+-------------------------------------------------------------------------------------+

IC_DMA_TDLR
""""""""""""

- Name: DMA Transmit Data Level Register
  
- Size: TX_ABW–1:0
  
- Address Offset: 0x8c
  
- Read/Write Access: Read/Write
  
This register is only valid when the DW_apb_i2c is configured with a set of DMA interface signals
(IC_HAS_DMA = 1). When DW_apb_i2c is not configured for DMA operation, this register does not exist;
writing to its address has no effect; reading from its address returns zero.

.. table:: IC_DMA_TDLR Register Fields

  +------------+----------+------+-------------------------------------------------------------------------------------+
  | Bits       | Name     | R/W  | Description                                                                         |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 31:TX_ABW  | Reserved | N/A  | Reserved                                                                            |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | TX_ABW–1:0 | DMATDL   | R/W  | Transmit Data Level. This bit field controls the level at which a DMA               |
  +            +          +      +                                                                                     +
  |            |          |      | request is made by the transmit logic. It is equal to the watermark level;          |
  +            +          +      +                                                                                     +
  |            |          |      | that is, the dma_tx_req signal is generated when the number of valid                |
  +            +          +      +                                                                                     +
  |            |          |      | data entries in the transmit FIFO is equal to or below this field value,            |
  +            +          +      +                                                                                     +
  |            |          |      | and TDMAE = 1.                                                                      |
  +            +          +      +                                                                                     +
  |            |          |      | Reset value: 0x0                                                                    |
  +------------+----------+------+-------------------------------------------------------------------------------------+

IC_DMA_RDLR
""""""""""""

- Name: I2C Receive Data Level Register
  
- Size: RX_ABW–1:0
  
- Address Offset: 0x90
  
- Read/Write Access: Read/Write

This register is only valid when DW_apb_i2c is configured with a set of DMA interface signals
(IC_HAS_DMA = 1). When DW_apb_i2c is not configured for DMA operation, this register does not exist;
writing to its address has no effect; reading from its address returns zero.

.. table:: IC_DMA_RDLR Register Fields

  +------------+----------+------+-------------------------------------------------------------------------------------+
  | Bits       | Name     | R/W  | Description                                                                         |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 31:RX_ABW  | Reserved | N/A  | Reserved                                                                            |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | RX_ABW–1:0 | DMARDL   | R/W  | Receive Data Level. This bit field controls the level at which a DMA request        |
  +            +          +      +                                                                                     +
  |            |          |      | is made by the receive logic. The watermark level = DMARDL+1; that is,              |
  +            +          +      +                                                                                     +
  |            |          |      | dma_rx_req is generated when the number of valid data entries in the                |
  +            +          +      +                                                                                     +
  |            |          |      | receive FIFO is equal to or more than this field value + 1, and RDMAE = 1.          |
  +            +          +      +                                                                                     +
  |            |          |      | For instance, when DMARDL is 0, then dma_rx_req is asserted when 1 or               |
  +            +          +      +                                                                                     +
  |            |          |      | more data entries are present in the receive FIFO.                                  |
  +            +          +      +                                                                                     +
  |            |          |      | Reset value: 0x0                                                                    |
  +------------+----------+------+-------------------------------------------------------------------------------------+

IC_SDA_SETUP
""""""""""""

- Name: I2C SDA Setup Register

- Size: 8 bits

- Address Offset: 0x94

- Read/Write Access: Read/Write

- Dependency: This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1).

This register controls the amount of time delay (in terms of number of ic_clk clock periods) introduced in
the rising edge of SCL—relative to SDA changing—by holding SCL low when DW_apb_i2c services a read
request while operating as a slave-transmitter. The relevant I2C requirement is tSU:DAT (note 4) as detailed
in the I2C Bus Specification. This register must be programmed with a value equal to or greater than 2.

Writes to this register succeed only when IC_ENABLE[0] = 0.

Note:The length of setup time is calculated using [(IC_SDA_SETUP - 1) * (ic_clk_period)], so if the 
user requires 10 ic_clk periods of setup time, they should program a value of 11.The IC_SDA_SETUP register is only used by the DW_apb_i2c when operating as a slave transmitter.

.. table:: IC_SDA_SETUP Register Fields

  +------------+----------+------+-------------------------------------------------------------------------------------+
  | Bits       | Name     | R/W  | Description                                                                         |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 31:8       | Reserved | N/A  | Reserved                                                                            |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 7:0        | SDA_SETUP| R/W  | SDA Setup. It is recommended that if the required delay is 1000ns, then for an      |
  +            +          +      +                                                                                     +
  |            |          |      | ic_clk frequency of 10 MHz, IC_SDA_SETUP should be programmed to a                  |
  +            +          +      +                                                                                     +
  |            |          |      | value of 11. IC_SDA_SETUP must be programmed with a minimum value of 2.             |
  +            +          +      +                                                                                     +
  |            |          |      | Default Reset value: 0x64, but can be hardcoded by setting the                      |
  +            +          +      +                                                                                     +
  |            |          |      | IC_DEFAULT_SDA_SETUP configuration parameter.                                       |
  +------------+----------+------+-------------------------------------------------------------------------------------+

IC_ACK_GENERAL_CALL
"""""""""""""""""""

- Name: I2C ACK General Call Register
  
- Size: 1 bit

- Address Offset: 0x98
  
- Read/Write Access: Read/Write
  
- Dependency: This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1).

The register controls whether DW_apb_i2c responds with an ACK or NACK when it receives an I2C
General Call address. This register is applicable only when the DW_apb_i2c is in the slave mode.

.. table::  IC_ACK_GENERAL_CALL Register Fields

  +------------+----------+------+-------------------------------------------------------------------------------------+
  | Bits       | Name     | R/W  | Description                                                                         |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 31:1       | Reserved | N/A  | Reserved                                                                            |
  +------------+----------+------+-------------------------------------------------------------------------------------+
  | 0          | ACK_GEN  | R/W  | ACK General Call. When set to 1, DW_apb_i2c responds with a ACK (by                 |
  +            +          +      +                                                                                     +
  |            | _CALL    |      | asserting ic_data_oe) when it receives a General Call. When set to 0, the           |
  +            +          +      +                                                                                     +
  |            |          |      | DW_apb_i2c does not generate General Call interrupts.                               |
  +            +          +      +                                                                                     +
  |            |          |      | Default Reset value: 0x1, but can be hardcoded by setting the                       |
  +            +          +      +                                                                                     +
  |            |          |      | IC_DEFAULT_ACK_GENERAL_CALL configuration parameter.                                |
  +------------+----------+------+-------------------------------------------------------------------------------------+

IC_ENABLE_STATUS
""""""""""""""""

- Name: I2C Enable Status Register
  
- Size: 3 bits
  
- Address Offset: 0x9C
  
- Read/Write Access: Read

The register is used to report the DW_apb_i2c hardware status when IC_ENABLE[0] is set from 1 to 0; that
is, when DW_apb_i2c is disabled.

If IC_ENABLE[0] has been set to 1, bits 2:1 are forced to 0, and bit 0 is forced to 1.

If IC_ENABLE[0] has been set to 0, bits 2:1 is only be valid as soon as bit 0 is read as ‘0’.

Note:When IC_ENABLE[0] has been set to 0, a delay occurs for bit 0 to be read as 0 because 
disabling the DW_apb_i2c depends on I2C bus activities.

.. table::  IC_ENABLE_STATUS Register Fields

  +------+---------------+------+--------------------------------------------------------------------------------+
  | Bits | Name          | R/W  | Description                                                                    |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 31:3 | Reserved      | N/A  | Reserved                                                                       |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 2    | SLV_RX_DATA   | R    | Slave Received Data Lost. This bit indicates if a Slave-Receiver               |
  +      +               +      +                                                                                +
  |      | _LOST         |      | operation has been aborted with at least one data byte received                |
  +      +               +      +                                                                                +
  |      |               |      | from an I2C transfer due to setting IC_ENABLE[0] from 1 to 0.                  |
  +      +               +      +                                                                                +
  |      |               |      | When read as 1, DW_apb_i2c is deemed to have been actively                     |
  +      +               +      +                                                                                +
  |      |               |      | engaged in an aborted I2C transfer (with matching address) and                 |
  +      +               +      +                                                                                +
  |      |               |      | the data phase of the I2C transfer has been entered, even though a             |
  +      +               +      +                                                                                +
  |      |               |      | data byte has been responded with a NACK.                                      |
  +      +               +      +                                                                                +
  |      |               |      | NOTE: If the remote I2C master terminates the transfer with a                  |
  +      +               +      +                                                                                +
  |      |               |      | STOP condition before the DW_apb_i2c has a chance to NACK a                    |
  +      +               +      +                                                                                +
  |      |               |      | transfer, and IC_ENABLE[0] has been set to 0, then this bit is also            | 
  +      +               +      +                                                                                +
  |      |               |      | set to 1.                                                                      |
  +      +               +      +                                                                                +
  |      |               |      | When read as 0, DW_apb_i2c is deemed to have been disabled                     |
  +      +               +      +                                                                                +
  |      |               |      | without being actively involved in the data phase of a Slave-                  |
  +      +               +      +                                                                                +
  |      |               |      | Receiver transfer.                                                             |
  +      +               +      +                                                                                +
  |      |               |      | NOTE: The CPU can safely read this bit when IC_EN (bit 0) is read              |
  +      +               +      +                                                                                +
  |      |               |      | as 0.                                                                          |
  +      +               +      +                                                                                +
  |      |               |      | Reset value: 0x0                                                               |
  +------+---------------+------+--------------------------------------------------------------------------------+

.. table::

  +------+---------------+------+--------------------------------------------------------------------------------+
  | 1    | SLV_DISABLED  | R    | Slave Disabled While Busy (Transmit, Receive). This bit indicates if           |
  +      +               +      +                                                                                +
  |      | _WHILE_BUSY   |      | a potential or active Slave operation has been aborted due to                  |
  +      +               +      +                                                                                +
  |      |               |      | setting bit 0 of the IC_ENABLE register from 1 to 0. This bit is set           |
  +      +               +      +                                                                                +
  |      |               |      | when the CPU writes a 0 to bit 0 of IC_ENABLE while: (a)                       |
  +      +               +      +                                                                                +
  |      |               |      | DW_apb_i2c is receiving the address byte of the Slave-Transmitter              |
  +      +               +      +                                                                                +
  |      |               |      | operation from a remote master; OR, (b) address and data bytes of              |
  +      +               +      +                                                                                +
  |      |               |      | the Slave-Receiver operation from a remote master.                             |
  +      +               +      +                                                                                +
  |      |               |      | When read as 1, DW_apb_i2c is deemed to have forced a NACK                     |
  +      +               +      +                                                                                +
  |      |               |      | during any part of an I2C transfer, irrespective of whether the I2C            |
  +      +               +      +                                                                                +
  |      |               |      | address matches the slave address set in DW_apb_i2c (IC_SAR                    |
  +      +               +      +                                                                                +
  |      |               |      | register) OR if the transfer is completed before bit 0 of IC_ENABLE            |
  +      +               +      +                                                                                +
  |      |               |      | is set to 0, but has not taken effect.                                         |
  +      +               +      +                                                                                +
  |      |               |      | NOTE: If the remote I2C master terminates the transfer with a                  |
  +      +               +      +                                                                                +
  |      |               |      | STOP condition before the DW_apb_i2c has a chance to NACK a                    |
  +      +               +      +                                                                                +
  |      |               |      | transfer, and bit 0 of IC_ENABLE has been set to 0, then this bit              |
  +      +               +      +                                                                                +
  |      |               |      | will also be set to 1.                                                         |
  +      +               +      +                                                                                +
  |      |               |      | When read as 0, DW_apb_i2c is deemed to have been disabled                     |
  +      +               +      +                                                                                +
  |      |               |      | when there is master activity, or when the I2C bus is idle.                    |
  +      +               +      +                                                                                +
  |      |               |      | NOTE: The CPU can safely read this bit when IC_EN (bit 0) is read              |
  +      +               +      +                                                                                +
  |      |               |      | as 0.                                                                          |
  +      +               +      +                                                                                +
  |      |               |      | Reset value: 0x0                                                               |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 0    | IC_EN         | R    | ic_en Status. This bit always reflects the value driven on the output          |
  +      +               +      +                                                                                +
  |      |               |      | port ic_en.                                                                    |
  +      +               +      +                                                                                +
  |      |               |      | When read as 1, DW_apb_i2c is deemed to be in an enabled state.                |
  +      +               +      +                                                                                +
  |      |               |      | When read as 0, DW_apb_i2c is deemed completely inactive.                      |
  +      +               +      +                                                                                +
  |      |               |      | NOTE: The CPU can safely read this bit anytime. When this bit is               |
  +      +               +      +                                                                                +
  |      |               |      | read as 0, the CPU can safely read SLV_RX_DATA_LOST (bit 2)                    |
  +      +               +      +                                                                                +
  |      |               |      | and SLV_DISABLED_WHILE_BUSY (bit 1).                                           |
  +      +               +      +                                                                                +
  |      |               |      | Reset value: 0x0                                                               |
  +------+---------------+------+--------------------------------------------------------------------------------+

IC_FS_SPKLEN
"""""""""""""

- Name: I2C SS and FS Spike Suppression Limit Register
  
- Size: 8 bits
  
- Address Offset: 0xA0
  
- Read/Write Access: Read/Write
  
- Dependency: This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1).
  
This register is used to store the duration, measured in ic_clk cycles, of the longest spike that is filtered out
by the spike suppression logic when the component is operating in standard mode, fast mode, or fast mode plus. The relevant I2
C requirement is tSP (Table 4) as detailed in the I2C Bus Specification. This register must be programmed with a minimum value of 1.

.. table:: IC_FS_SPKLEN Register Fields

  +------+---------------+------+--------------------------------------------------------------------------------+
  | Bits | Name          | R/W  | Description                                                                    |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 31:8 | Reserved      |      |                                                                                |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 7:0  | IC_FS_SPKLEN  | R/W  | This register must be set before any I2C bus transaction can take place to     |
  +      +               +      +                                                                                +
  |      |               |      | ensure stable operation. This register sets the duration, measured in ic_clk   |
  +      +               +      +                                                                                +
  |      |               |      | cycles, of the longest spike in the SCL or SDA lines that are filtered out by  |
  +      +               +      +                                                                                +
  |      |               |      | the spike suppression logic                                                    |
  +      +               +      +                                                                                +
  |      |               |      | This register can be written only when the I2C interface is disabled, which    |
  +      +               +      +                                                                                +
  |      |               |      | corresponds to IC_ENABLE[0] being set to 0.Writes at other times have no effect|
  +      +               +      +                                                                                +
  |      |               |      | The minimum valid value is 1; hardware prevents values less than this          |
  +      +               +      +                                                                                +
  |      |               |      | being written, and if attempted, results in 1 being set.                       |
  +      +               +      +                                                                                +
  |      |               |      | Reset value: IC_DEFAULT_FS_SPKLEN configuration parameter                      |
  +------+---------------+------+--------------------------------------------------------------------------------+

IC_HS_SPKLEN
""""""""""""

- Name: I2C HS Spike Suppression Limit Register
  
- Size: 8 bits
  
- Address Offset: 0xA4
  
- Read/Write Access: Read/Write

- Dependency: This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1).
  
This register is used to store the duration, measured in ic_clk cycles, of the longest spike that is filtered out
by the spike suppression logic when the component is operating in HS mode. The relevant I2C requirement
is tSP (Table 6) as detailed in the I2C Bus Specification. This register must be programmed with a minimum
value of 1 and is implemented only if the component is configured to support HS mode; that is, if the
IC_MAX_SPEED_MODE parameter is set to 3.
 
.. table::  IC_HS_SPKLEN Register Fields

  +------+---------------+------+--------------------------------------------------------------------------------+
  | Bits | Name          | R/W  | Description                                                                    |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 31:8 | Reserved      |      |                                                                                |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 7:0  | IC_HS_SPKLEN  | R/W  | This register must be set before any I2C bus transaction can take place to     |
  +      +               +      +                                                                                +
  |      |               |      | ensure stable operation. This register sets the duration, measured in ic_clk   |
  +      +               +      +                                                                                +
  |      |               |      | cycles, of the longest spike in the SCL or SDA lines that are filtered out by  |
  +      +               +      +                                                                                +
  |      |               |      | the spike suppression logic                                                    |
  +      +               +      +                                                                                +
  |      |               |      | This register can be written only when the I2C interface is disabled, which    |
  +      +               +      +                                                                                +
  |      |               |      | corresponds to IC_ENABLE[0] being set to 0.Writes at other times have no effect|
  +      +               +      +                                                                                +
  |      |               |      | The minimum valid value is 1; hardware prevents values less than this          |
  +      +               +      +                                                                                +
  |      |               |      | being written, and if attempted, results in 1 being set.                       |
  +      +               +      +                                                                                +
  |      |               |      | This register is implemented only if the component is configured to support    |
  +      +               +      +                                                                                +
  |      |               |      | HS mode; that is, if the IC_MAX_SPEED_MODE parameter is set to 3.              |
  +      +               +      +                                                                                +
  |      |               |      | Reset value: IC_DEFAULT_HS_SPKLEN configuration parameter                      |
  +------+---------------+------+--------------------------------------------------------------------------------+

IC_CLR_RESTART_DET
""""""""""""""""""

- Name: Clear RESTART_DET Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0xA8
  
- Read/Write Access: Read

.. table:: IC_CLR_RESTART_DET Register Fields

  +------+---------------+------+--------------------------------------------------------------------------------+
  | Bits | Name          | R/W  | Description                                                                    |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 31:1 | Reserved      | N/A  | Reserved                                                                       |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 0    | CLR_RESTART   | R    | Read this register to clear the RESTART_DET interrupt (bit 12) of              |
  +      +               +      +                                                                                +
  |      | _DET          |      | the IC_RAW_INTR_STAT register.                                                 |
  +      +               +      +                                                                                +
  |      |               |      | Dependencies: This register is present only when                               |
  +      +               +      +                                                                                +
  |      |               |      | IC_SLV_RESTART_DET_EN = 1.                                                     |
  +      +               +      +                                                                                +
  |      |               |      | Reset value: 0x0                                                               |
  +------+---------------+------+--------------------------------------------------------------------------------+

IC_COMP_PARAM_1
"""""""""""""""

- Name: Component Parameter Register 1
  
- Size: 32 bits
  
- Address Offset: 0xf4

- Read/Write Access: Read

Note:This is a constant read-only register that contains encoded information about the component's 
parameter settings. The reset value depends on coreConsultant parameter(s).

.. table:: IC_COMP_PARAM_1 Register Fields

  +------+---------------+------+--------------------------------------------------------------------------------+
  | Bits | Name          | R/W  | Description                                                                    |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 31:24| Reserved      | N/A  | Reserved                                                                       |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 23:16| TX_BUFFER     | R    | The value of this register is derived from the                                 |
  +      +               +      +                                                                                +
  |      | _DEPTH        |      | IC_TX_BUFFER_DEPTH coreConsultant parameter.                                   |
  +      +               +      +                                                                                +
  |      |               |      | 0x00 = Reserved                                                                |
  +      +               +      +                                                                                +
  |      |               |      | 0x01 = 2                                                                       |
  +      +               +      +                                                                                +
  |      |               |      | 0x02 = 3                                                                       |
  +      +               +      +                                                                                +
  |      |               |      | ...                                                                            |
  +      +               +      +                                                                                +
  |      |               |      | 0xFF = 256                                                                     |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 15:8 | RX_BUFFER     | R    | The value of this register is derived from the                                 |
  +      +               +      +                                                                                +
  |      | _DEPTH        |      | IC_RX_BUFFER_DEPTH coreConsultant parameter.                                   |
  +      +               +      +                                                                                +
  |      |               |      | 0x00 = Reserved                                                                |
  +      +               +      +                                                                                +
  |      |               |      | 0x01 = 2                                                                       |
  +      +               +      +                                                                                +
  |      |               |      | 0x02 = 3                                                                       |
  +      +               +      +                                                                                +
  |      |               |      | ...                                                                            |
  +      +               +      +                                                                                +
  |      |               |      | 0xFF = 256                                                                     |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 7    | ADD_ENCODED   | R    | The value of this register is derived from the                                 |
  +      +               +      +                                                                                +
  |      | _PARAMS       |      | IC_ADD_ENCODED_PARAMS coreConsultant parameter.                                |
  +      +               +      +                                                                                +
  |      |               |      | Reading 1 in this bit means that the capability of reading                     |
  +      +               +      +                                                                                +
  |      |               |      | these encoded parameters via software has been included.                       |
  +      +               +      +                                                                                +
  |      |               |      | Otherwise, the entire register is 0 regardless of the setting of               |
  +      +               +      +                                                                                +
  |      |               |      | any other parameters that are encoded in the bits                              |
  +      +               +      +                                                                                +
  |      |               |      | 0: False                                                                       |
  +      +               +      +                                                                                +
  |      |               |      | 1: True                                                                        |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 6    | HAS_DMA       | R    | The value of this register is derived from the IC_HAS_DMA                      |
  +      +               +      +                                                                                +
  |      |               |      | coreConsultant parameter.                                                      |
  +      +               +      +                                                                                +
  |      |               |      | 0: False                                                                       |
  +      +               +      +                                                                                +
  |      |               |      | 1: True                                                                        |
  +------+---------------+------+--------------------------------------------------------------------------------+

.. table:: 

  +------+---------------+------+--------------------------------------------------------------------------------+
  | 6    | HAS_DMA       | R    | The value of this register is derived from the IC_HAS_DMA                      |
  +      +               +      +                                                                                +
  |      |               |      | coreConsultant parameter.                                                      |
  +      +               +      +                                                                                +
  |      |               |      | 0: False                                                                       |
  +      +               +      +                                                                                +
  |      |               |      | 1: True                                                                        |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 5    | INTR_IO       | R    | The value of this register is derived from the IC_INTR_IO                      |
  +      +               +      +                                                                                +
  |      |               |      | coreConsultant parameter.                                                      |
  +      +               +      +                                                                                +
  |      |               |      | 0: Individual                                                                  |
  +      +               +      +                                                                                +
  |      |               |      | 1: Combined                                                                    |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 4    | HC_COUNT      | R    | The value of this register is derived from the                                 |
  +      +               +      +                                                                                +
  |      | _VALUES       |      | IC_HC_COUNT_VALUES coreConsultant parameter.                                   |
  +      +               +      +                                                                                +
  |      |               |      | 0: False                                                                       |
  +      +               +      +                                                                                +
  |      |               |      | 1: True                                                                        |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 3:2  | MAX_SPEED_MODE| R    | The value of this register is derived from the                                 |
  +      +               +      +                                                                                +
  |      |               |      | IC_MAX_SPEED_MODE coreConsultant parameter.                                    |
  +      +               +      +                                                                                +
  |      |               |      | 0x0 = Reserved                                                                 |
  +      +               +      +                                                                                +
  |      |               |      | 0x1 = Standard                                                                 |
  +      +               +      +                                                                                +
  |      |               |      | 0x2 = Fast                                                                     |
  +      +               +      +                                                                                +
  |      |               |      | 0x3 = High                                                                     |
  +      +               +      +                                                                                +
  |      |               |      | Dependency: This field is not applicable in Ultra-Fast speed                   |
  +      +               +      +                                                                                +
  |      |               |      | mode (IC_ULTRA_FAST_MODE=1)                                                    |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 1:0  | APB_DATA_WIDTH| R    | The value of this register is derived from the                                 |
  +      +               +      +                                                                                +
  |      |               |      | APB_DATA_WIDTH coreConsultant parameter.                                       |
  +      +               +      +                                                                                +
  |      |               |      | 0x0 = 8 bits                                                                   |
  +      +               +      +                                                                                +
  |      |               |      | 0x1 = 16 bits                                                                  |
  +      +               +      +                                                                                +
  |      |               |      | 0x2 = 32 bits                                                                  |
  +      +               +      +                                                                                +
  |      |               |      | 0x3 = Reserved                                                                 |
  +------+---------------+------+--------------------------------------------------------------------------------+

IC_COMP_VERSION
"""""""""""""""

- Name: I2C Component Version Register

- Size: 32 bits
  
- Address Offset: 0xf8
  
- Read/Write Access: Read

.. table:: IC_COMP_VERSION Register Fields

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:0 | IC_COMP_VERSION| R    | Specific values for this register are described in the Releases Table          |
  +      +                +      +                                                                                +
  |      |                |      | in the AMBA 2 release notes                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_COMP_TYPE
""""""""""""

- Name: I2C Component Type Register

- Size: 32 bits

- Address Offset: 0xfc

- Read/Write Access: Read

.. table:: IC_COMP_TYPE Register Fields

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:0 | IC_COMP_TYPE   | R    | Designware Component Type number = 0x44_57_01_40. This                         |
  +      +                +      +                                                                                +
  |      |                |      | assigned unique hex value is constant and is derived from the two              |
  +      +                +      +                                                                                +
  |      |                |      | ASCII letters “DW” followed by a 16-bit unsigned number.                       |
  +------+----------------+------+--------------------------------------------------------------------------------+  

IC_SCL_STUCK_AT_LOW_TIMEOUT
"""""""""""""""""""""""""""

- Name: I2C SCL Stuck at Low Timeout
  
- Size: 32 bits
  
- Address Offset: 0xAC
  
- Read/Write Access: Read/Write
  
- Dependencies: This register is not applicable in Ultra-Fast speed mode( IC_ULTRA_FAST_MODE = 1).

This register is used to store the duration, measured in ic_clk cycles, used to generate an Interrupt
(SCL_STUCK_AT_LOW) if SCL is held low for the IC_SCL_STUCK_LOW_TIMEOUT duration.

.. table::  IC_SCL_STUCK_AT_LOW_TIMEOUT Register Field

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:0 | IC_SCL_STUCK   | R/W  | DW_apb_i2c generates the interrupt to indicate SCL stuck at low if it          |
  +      +                +      +                                                                                +
  |      | LOW_TIMEOUT    |      | detects the SCL stuck at low for the                                           |
  +      +                +      +                                                                                +
  |      |                |      | IC_SCL_STUCK_LOW_TIMEOUT in units of ic_clk period.                            |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: IC_SCL_STUCK_TIMEOUT_DEFAULT                                      |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_SDA_STUCK_AT_LOW_TIMEOUT
"""""""""""""""""""""""""""

- Name: I2C SDA Stuck at Low Timeout
  
- Size: 32 bits
  
- Address Offset: 0xB0
  
- Read/Write Access: Read/Write
  
- Dependencies: This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1).

This register is used to store the duration, measured in ic_clk cycles, used to recover the Data (SDA) line
through sending SCL pulses if SDA is held low for the mentioned duration.

.. table:: IC_SDA_STUCK_AT_LOW_TIMEOUT Register Field

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:0 | IC_SDA_STUCK   | R/W  | DW_apb_i2c initiates the recovery of SDA line through enabling the             |
  +      +                +      +                                                                                +
  |      | _LOW_TIMEOUT   |      | SDA_STUCK_RECOVERY_EN (IC_ENABLE[3]) register bit, if it                       |
  +      +                +      +                                                                                +
  |      |                |      | detects the SDA stuck at low for the                                           |
  +      +                +      +                                                                                +
  |      |                |      | IC_SDA_STUCK_LOW_TIMEOUT in units of ic_clk period.                            |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: IC_SDA_STUCK_TIMEOUT_DEFAULT                                      |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_CLR_SCL_STUCK_DET
""""""""""""""""""""

- Name: Clear SCL Stuck at Low Detect Interrupt Register
  
- Size: 1 bit
  
- Address Offset: 0xB4
  
- Read/Write Access: Read
  
- Dependencies: This register is not applicable in Ultra-Fast speed mode (IC_ULTRA_FAST_MODE=1)

.. table:: IC_CLR_SCL_STUCK_DET Register Fields

  +------+---------------+------+--------------------------------------------------------------------------------+
  | Bits | Name          | R/W  | Description                                                                    |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 31:1 | Reserved      | N/A  | Reserved                                                                       |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 0    | CLR_SCL_STUCK | R    | Read this register to clear the SCL_STUCK_DET interrupt (bit 14)               |
  +      +               +      +                                                                                +
  |      |               |      | of the IC_RAW_INTR_STAT register.                                              |
  +      +               +      +                                                                                +
  |      |               |      | Reset value: 0x0                                                               |
  +------+---------------+------+--------------------------------------------------------------------------------+

IC_DEVICE_ID
""""""""""""

- Name: I2C Device ID
  
- Size: 24 bits

- Address Offset: 0xb8
  
- Read/Write Access: Read

- Dependencies: This register is not applicable in Ultra-Fast speed mode(IC_ULTRA_FAST_MODE=1).

This register contains the Device-ID of the component, which includes 12 bits of manufacturer name, 9 bits
of part identification and 3 bits of die-version.

.. table::  IC_DEVICE_ID Register Fields

  +------+---------------+------+--------------------------------------------------------------------------------+
  | Bits | Name          | R/W  | Description                                                                    |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 31:24| Reserved      | N/A  | Reserved                                                                       |
  +------+---------------+------+--------------------------------------------------------------------------------+
  | 23:0 | DEVICE-ID     | R    | Contains the Device-ID of the component assigned through the                   |
  +      +               +      +                                                                                +
  |      |               |      | configuration parameter IC_DEVICE_ID_VALUE                                     |
  +      +               +      +                                                                                +
  |      |               |      | Reset Value: IC_DEVICE_ID_VALUE                                                |
  +------+---------------+------+--------------------------------------------------------------------------------+

IC_UFM_SCL_HCNT
"""""""""""""""

- Name: Ultra-Fast mode I2C Clock High Count Register
  
- Size: 16 bits
  
- Address Offset: 0x14
  
- Read/Write Access: Read/Write
  
- Dependencies: This is register is present only if parameter IC_ULTRA_FAST_MODE is set to 1.

.. table:: Ultra-Fast Mode SCL High Counter Register Field Description

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:16| Reserved       | N/A  | Reserved                                                                       |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 15:0 | IC_UFM_SCL_HCNT| R/W^1| This register must be set before any I2C bus transaction can take              |
  +      +                +      +                                                                                +
  |      |                |      | place to ensure proper I/O timing. This register sets the SCL clock            |
  +      +                +      +                                                                                +
  |      |                |      | high-period count for Ultra-Fast speed.                                        |
  +      +                +      +                                                                                +
  |      |                |      | This register can be written only when the I2C interface is disabled           |
  +      +                +      +                                                                                +
  |      |                |      | which corresponds to IC_ENABLE[0] being set to 0. Writes at other              |
  +      +                +      +                                                                                +
  |      |                |      | times have no effect.                                                          |
  +      +                +      +                                                                                +
  |      |                |      | For designs with APB_DATA_WIDTH = 8, the order of programming                  |
  +      +                +      +                                                                                +
  |      |                |      | is important to ensure the correct operation of the DW_apb_i2c.                |
  +      +                +      +                                                                                +
  |      |                |      | The lower byte must be programmed first and then the upper byte is             |
  +      +                +      +                                                                                +
  |      |                |      | programmed. When the configuration parameter                                   |
  +      +                +      +                                                                                +
  |      |                |      | IC_HC_COUNT_VALUES is set to 1, this register is read only.                    |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: IC_UFM_SCL_HIGH_COUNT configuration parameter                     |
  +------+----------------+------+--------------------------------------------------------------------------------+

Read-only if IC_HC_COUNT_VALUES = 1.

IC_UFM_SCL_LCNT
"""""""""""""""

- Name: Ultra-Fast mode I2C Clock Low Count Register
  
- Size: 16 bits
  
- Address Offset: 0x18
  
- Read/Write Access: Read
  
- Dependencies: This is register is present only if parameter IC_ULTRA_FAST_MODE is set to 1.

.. table:: Ultra-Fast Mode SCL Low Counter Register Field Description

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:16| Reserved       | N/A  | Reserved                                                                       |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 15:0 | IC_UFM_SCL_LCNT| R/W^1| This register must be set before any I2C bus transaction can take              |
  +      +                +      +                                                                                +
  |      |                |      | place to ensure proper I/O timing. This register sets the SCL clock            |
  +      +                +      +                                                                                +
  |      |                |      | low-period count for Ultra-Fast speed.                                         |
  +      +                +      +                                                                                +
  |      |                |      | This register can be written only when the I2C interface is disabled           |
  +      +                +      +                                                                                +
  |      |                |      | which corresponds to IC_ENABLE[0] being set to 0. Writes at other              |
  +      +                +      +                                                                                +
  |      |                |      | times have no effect.                                                          |
  +      +                +      +                                                                                +
  |      |                |      | For designs with APB_DATA_WIDTH = 8, the order of programming                  |
  +      +                +      +                                                                                +
  |      |                |      | is important to ensure the correct operation of the DW_apb_i2c.                |
  +      +                +      +                                                                                +
  |      |                |      | The lower byte must be programmed and then the upper byte is                   |
  +      +                +      +                                                                                +
  |      |                |      | programmed. When the configuration parameter                                   |
  +      +                +      +                                                                                +
  |      |                |      | IC_HC_COUNT_VALUES is set to 1, this register is read only.                    |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: IC_UFM_SCL_LOW_COUNT configuration parameter                      |
  +------+----------------+------+--------------------------------------------------------------------------------+

Read-only if IC_HC_COUNT_VALUES = 1.

IC_UFM_SPKLEN
"""""""""""""

- Name: I2C Ultra-Fast mode Spike suppression Register
  
- Size: 8 bits
  
- Address Offset: 0xA0
  
- Read/Write Access: Read/Write
  
- Dependencies: This is register is present only if parameter IC_ULTRA_FAST_MODE is set to 1.
  
This register is used to store the duration, measured in ic_clk cycles, of the longest spike that is filtered out
by the spike suppression logic when the component is operating in Ultra-Fast mode. The relevant I2C requirement is tSP as detailed in the I2C Bus Specification. This register must be programmed with a minimum value of 1.

.. table:: UFM Spike Suppression Register

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:8 | Reserved       | N/A  | Reserved                                                                       |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 7:0  | IC_UFM_SPKLEN  | R/W  | This register must be set before any I2C bus transaction can occur             |
  +      +                +      +                                                                                +
  |      |                |      | to ensure stable operation. This register sets the duration,                   |
  +      +                +      +                                                                                +
  |      |                |      | measured in ic_clk cycles, of the longest spike in the SCL or SDA              |
  +      +                +      +                                                                                +
  |      |                |      | lines that are filtered out by the spike suppression logic.                    |
  +      +                +      +                                                                                +
  |      |                |      | This register can be written only when the I2C interface is disabled,          |
  +      +                +      +                                                                                +
  |      |                |      | which corresponds to IC_ENABLE[0] being set to 0. Writes at other              |
  +      +                +      +                                                                                +
  |      |                |      | times have no effect.                                                          |
  +      +                +      +                                                                                +
  |      |                |      | The minimum valid value is 1; hardware prevents values less than               |
  +      +                +      +                                                                                +
  |      |                |      | this being written, and if attempted, results in 1 being set.                  |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: IC_DEFAULT_UFM_SPKLEN configuration parameter.                    |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_UFM_TBUF_CNT
"""""""""""""""""

- Name: Ultra-Fast mode TBuf Idle Count Register
  
- Size: 16 bits
  
- Address Offset: 0x1c
  
- Read/Write Access: Read/Write
  
- Dependencies: This is register is present only if parameter IC_ULTRA_FAST_MODE is set to 1.

.. table:: Ultra-Fast Mode Tbuf Counter Register Field Description

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:16| Reserved       | N/A  | Reserved                                                                       |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 15:0 | IC_UFM_TBUF_CNT| R/W^1| This register must be set before any I2C bus transaction can take              |
  +      +                +      +                                                                                +
  |      |                |      | place to ensure proper I/O timing. This register sets the tBuf Idle            |
  +      +                +      +                                                                                +
  |      |                |      | time count for Ultra-Fast speed.                                               |
  +      +                +      +                                                                                +
  |      |                |      | This register can be written only when the I2C interface is disabled           |
  +      +                +      +                                                                                +
  |      |                |      | which corresponds to IC_ENABLE[0] being set to 0. Writes at other              |
  +      +                +      +                                                                                +
  |      |                |      | times have no effect.                                                          |
  +      +                +      +                                                                                +
  |      |                |      | For designs with APB_DATA_WIDTH = 8, the order of programming                  |
  +      +                +      +                                                                                +
  |      |                |      | is important to ensure the correct operation of the DW_apb_i2c.                |
  +      +                +      +                                                                                +
  |      |                |      | The lower byte must be programmed first and then the upper byte is             |
  +      +                +      +                                                                                +
  |      |                |      | programmed. When the configuration parameter                                   |
  +      +                +      +                                                                                +
  |      |                |      | IC_HC_COUNT_VALUES is set to 1, this register is read only.                    |
  +      +                +      +                                                                                +
  |      |                |      | NOTE:The DW_apb_i2c will add 9 ic_clks after tBuf time is expired to           |
  +      +                +      +                                                                                +
  |      |                |      | generate START on the Bus.                                                     |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: IC_UFM_TBUF_CNT_DEFAULT configuration parameter                   |
  +------+----------------+------+--------------------------------------------------------------------------------+

Read-only if IC_HC_COUNT_VALUES = 1.

IC_SMBUS_CLOCK_LOW_SEXT
"""""""""""""""""""""""

- Name: SMBUS Slave Clock Extend Timeout Register
  
- Size: 32 bits
  
- Address Offset: 0xBC
  
- Read/Write Access: Read/Write
  
This register contains the Timeout value used to determine the Slave Clock Extend Timeout in one transfer(from START to STOP). This register can be written only when the DW_apb_i2c is disabled, whichcorresponds to IC_ENABLE[0] being set to 0. This register is present only if configuration parameter IC_SMBUS is set to 1.

This register is used to store the duration, measured in ic_clk cycles, used to detect the slave clock extend
timeout if slave extends the clock (SCL) for the mentioned duration.

.. table:: IC_SMBUS_CLOCK_LOW_SEXT Register Field Description

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:0 | SMBUS_CLK_LOW  | R/W  | This field is used to detect the Slave Clock Extend timeout                    |
  +      +                +      +                                                                                +
  |      | _SEXT_TIMEOUT  |      | (tLOW:SEXT) in master mode extended by the slave device in one                 |
  +      +                +      +                                                                                +
  |      |                |      | message from the initial START to the STOP.                                    |
  +      +                +      +                                                                                +
  |      |                |      | The values in this register are in units of ic_clk period.                     |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: IC_SMBUS_CLOCK_LOW_SEXT_DEFAULT                                   |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_SMBUS_CLOCK_LOW_MEXT
"""""""""""""""""""""""

- Name: SMBUS Master extend clock Timeout Register
  
- Size: 32 bits
  
- Address Offset: 0xC0
  
- Read/Write Access: Read/Write
  
This register contains the Timeout value used to determine the Master Clock Extend Timeout in one byte of
transfer. This register can be written only when the DW_apb_i2c is disabled, which corresponds to
IC_ENABLE[0] being set to 0. This register is present only if configuration parameter IC_SMBUS is set to 1.

This register is used to store the duration, measured in ic_clk cycles, used to detect the Master clock extend
timeout if Master extends the clock (SCL) for the mentioned duration.

.. table:: SMBUS Master extend clock Timeout Register Field Description

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:0 | SMBUS_CLK_LOW  | R/W  | This field is used to detect the Master extend SMBus clock (SCL)               |
  +      +                +      +                                                                                +
  |      | _MEXT_TIMEOUT  |      | timeout defined from START-to-ACK, ACK-to-ACK, or ACK-to-STOP                  |
  +      +                +      +                                                                                +
  |      |                |      | in Master mode.                                                                |
  +      +                +      +                                                                                +
  |      |                |      | The values in this register are in units of ic_clk period.                     |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: IC_SMBUS_CLOCK_LOW_SEXT_DEFAULT                                   |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_SMBUS_THIGH_MAX_IDLE_COUNT
"""""""""""""""""""""""""""""

- Name: SMBus Thigh MAX Bus-Idle count Register
  
- Size: 16 bits
  
- Address Offset: 0xC4
  
- Read/Write Access: Read/Write
  
This register programs the Bus-idle time period used when a master has been dynamically added to the bus
or when a master has generated a clock reset on the bus. This register is used to store the duration,
measured in ic_clk cycles, used to detect the Bus Idle condition if SCL and SDA are held high for the
mentioned duration. This register can be written only when the DW_apb_i2c is disabled, which corresponds
to IC_ENABLE[0] being set to 0. This register is present only if configuration parameter IC_SMBUS is set to
1.

.. table:: SMBus Thigh MAX Bus-Idle count Register Field Descriptions

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:16| Reserved       | N/A  | Reserved                                                                       |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 15:0 | SMBUS_THIGH_MAX| R/W  | This field is used to set the required Bus-Idle time period used when          |
  +      +                +      +                                                                                +
  |      | _BUS_IDLE_CNT  |      | a master has been dynamically added to the bus and may not have                |
  +      +                +      +                                                                                +
  |      |                |      | detected a state transition on the SMBCLK or SMBDAT lines.                     |
  +      +                +      +                                                                                +
  |      |                |      | In this case, the master must wait to ensure that a transfer is not            |
  +      +                +      +                                                                                +
  |      |                |      | currently in progress.                                                         |
  +      +                +      +                                                                                +
  |      |                |      | The values in this register are in units of ic_clk period.                     |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: IC_SMBUS_RST_IDLE_CNT_DEFAULT                                     |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_SMBUS_INTR_STAT
"""""""""""""""""""

- Name: I2C SMBUS Interrupt Status Register
  
- Size: 32 bits
  
- Address Offset: 0xC8
  
- Read/Write Access: Read
  
Each bit in this register has a corresponding mask bit in the IC_SMBUS_INTR_MASK register. These bits are
cleared by writing the matching SMBus interrupt clear register (IC_CLR_SMBUS_INTR) bits. The
unmasked raw versions of these bits are available in the IC_SMBUS_RAW_INTR_STAT register.

.. table:: I2C SMBUS Interrupt Status Register Field Descriptions

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:11| Reserved       | N/A  | Reserved                                                                       |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 10   | R_SMBUS_ALERT  | R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      | _DET           |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 9    | R_SMBUS_SUSPEND| R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      | _DET           |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 8    | R_SLV_RX_PEC   | R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      | _NACK          |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 7    | R_ARP_ASSGN    | R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      | ADDR_CMD_DET   |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 6    | R_ARP_GET_UDID | R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      | _CMD_DET       |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 5    | R_ARP_RST_CMD  | R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      | _DET           |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 4    | R_ARP_PREPARE  | R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      | CMD_DET        |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+    
  | 3    | R_HOST_NOTIFY  | R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      | _MST_DET       |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 2    | R_QUICK_CMD_DET| R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 1    | R_MST_CLOCK    | R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      | _TIMEOUT       |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 0    | R_SLV_CLOCK    | R    | See IC_SMBUS_INTR_RAW_STATUS for a detailed description of this bit.           |
  +      +                +      +                                                                                +
  |      | _EXTND_TIMEOUT |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_SMBUS_INTR_MASK
""""""""""""""""""

- Name: I2C Interrupt Mask Register
  
- Size: 32 bits
  
- Address Offset: 0xcc
  
- Read/Write Access: Read/Write

.. table::  I2C Interrupt Mask Register Field Descriptions   

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:11| Reserved       | N/A  | Reserved                                                                       |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 10   | M_SMBUS_ALERT  | R/W  | This bit masks the R_SMBUS_ALERT_DET interrupt bit in the                      |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS_INTR_STAT register. This bit is enabled only when                     |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS_SUSPEND_ALERT=1.                                                      |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 9    | M_SMBUS_SUSPEND| R/W  | This bit masks the R_SMBUS_SUSPEND_DET interrupt bit in the                    |
  +      +                +      +                                                                                +
  |      | _DET           |      | IC_SMBUS_INTR_STAT register. This bit is enabled only when                     |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS_SUSPEND_ALERT=1.                                                      |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 8    | M_SLV_RX_PEC   | R/W  | This bit masks the R_SLV_RX_PEC_NACK interrupt bit in the                      |
  +      +                +      +                                                                                +
  |      | _NACK          |      | IC_SMBUS_INTR_STAT register. This bit is enabled only when                     |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS_ARP=1.                                                                |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 7    | M_ARP_ASSGN    | R/W  | This bit masks the R_ARP_ASSGN_ADDR_CMD_DET interrupt bit                      |
  +      +                +      +                                                                                +
  |      | _ADDR_CMD_DET  |      | in the IC_SMBUS_INTR_STAT register. This bit is enabled only                   |
  +      +                +      +                                                                                +
  |      |                |      | when IC_SMBUS_ARP=1.                                                           |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 6    | M_ARP_GET_UDID | R/W  | This bit masks the R_ARP_GET_UDID_CMD_DET interrupt bit in                     |
  +      +                +      +                                                                                +
  |      | _CMD_DET       |      | the IC_SMBUS_INTR_STAT register. This bit is enabled only when                 |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS_ARP=1.                                                                |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+

.. table:: 

  +------+----------------+------+--------------------------------------------------------------------------------+
  | 5    | M_ARP_RST_CMD  | R/W  | This bit masks the R_ARP_RST_CMD_DET interrupt bit in the                      |
  +      +                +      +                                                                                +
  |      | _DET           |      | IC_SMBUS_INTR_STAT register. This bit is enabled only when                     |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS_ARP=1.                                                                |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 4    | M_ARP_PREPARE  | R/W  | This bit masks the R_ARP_PREPARE_CMD_DET interrupt bit in                      |
  +      +                +      +                                                                                +
  |      | _CMD_DET       |      | the IC_SMBUS_INTR_STAT register. This bit is enabled only when                 |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS_ARP=1.                                                                |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 3    | M_HOST_NOTIFY  | R/W  | This bit masks the R_HOST_NOTIFY_DET interrupt bit in the                      |
  +      +                +      +                                                                                +
  |      | _MST_DET       |      | IC_SMBUS_INTR_STAT register. This bit is enabled only when                     |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS=1.                                                                    |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 2    | M_QUICK_CMD_DET| R/W  | This bit masks the R_QUICK_CMD_DET interrupt bit in the                        |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS_INTR_STAT register. This bit is enabled only when                     |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS=1.                                                                    |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 1    | M_MST_CLOCK    | R/W  | This bit masks the R_MST_CLOCK_EXTND_TIMEOUT interrupt                         |
  +      +                +      +                                                                                +
  |      | _EXTND_TIMEOUT |      | bit in the IC_SMBUS_INTR_STAT register. This bit is enabled only               |
  +      +                +      +                                                                                +
  |      |                |      | when IC_SMBUS=1.                                                               |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 0    | M_SLV_CLOCK    | R/W  | This bit masks the R_SLV_CLOCK_EXTND_TIMEOUT interrupt bit                     |
  +      +                +      +                                                                                +
  |      | _EXTND_TIMEOUT |      | in the IC_SMBUS_INTR_STAT register. This bit is enabled only                   |
  +      +                +      +                                                                                +
  |      |                |      | when IC_SMBUS=1.                                                               |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x1                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_SMBUS_INTR_RAW_STATUS
"""""""""""""""""""""""""

- Name: I2C SMBUS Raw Interrupt Status Register
  
- Size: 32 bits
  
- Address Offset: 0xd0
  
- Read/Write Access: Read only

.. table::  I2C SMBUS Raw Interrupt Status Register Field Descriptions

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:11| Reserved       | N/A  | Reserved                                                                       |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 10   | SMBUS_ALERT_DET| R    | Indicates whether a SMBALERT (ic_smbalert_in_n) signal is driven               |
  +      +                +      +                                                                                +
  |      |                |      | low by the slave.                                                              |
  +      +                +      +                                                                                +
  |      |                |      | Dependencies: This register bit is valid only if configuration                 |
  +      +                +      +                                                                                +
  |      |                |      | parameter IC_SMBUS_SUSPEND_ALERT is set to 1.                                  |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 9    | SMBUS_SUSPEND  | R    | Indicates whether a SMBSUS (ic_smbsus_in_n) signal is driven low               |
  +      +                +      +                                                                                +
  |      | _DET           |      | by the Host.                                                                   |
  +      +                +      +                                                                                +
  |      |                |      | Dependencies: This register bit is valid only if configuration                 |
  +      +                +      +                                                                                +
  |      |                |      | parameter IC_SMBUS_SUSPEND_ALERT is set to 1.                                  |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 8    | SLV_RX_PEC_NACK| R    | Indicates whether a Slave generates a NACK for the PEC Byte of                 |
  +      +                +      +                                                                                +
  |      |                |      | the ARP command from the slave.                                                |
  +      +                +      +                                                                                +
  |      |                |      | Dependencies: This register bit is valid only if configuration                 |
  +      +                +      +                                                                                +
  |      |                |      | parameter IC_SMBUS_ARP is set to 1.                                            |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 7    | ARP_ASSGN_ADDR | R    | Indicates whether an Assign Address ARP command has been                       |
  +      +                +      +                                                                                +
  |      | _CMD_DET       |      | received.                                                                      |
  +      +                +      +                                                                                +
  |      |                |      | Dependencies: This register bit is valid only if configuration                 |
  +      +                +      +                                                                                +
  |      |                |      | parameter IC_SMBUS_ARP is set to 1.                                            |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 6    | ARP_GET_UDID   | R    | Indicates whether a General or directed Get UDID ARP command                   |
  +      +                +      +                                                                                +
  |      | _CMD_DET       |      | has been received.                                                             |
  +      +                +      +                                                                                +
  |      |                |      | Dependencies: This register bit is valid only if configuration                 |
  +      +                +      +                                                                                +
  |      |                |      | parameter IC_SMBUS_ARP is set to 1.                                            |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+

.. table::

  +------+----------------+------+--------------------------------------------------------------------------------+
  | 5    | ARP_RST_CMD_DET| R    | Indicates whether a General or Directed Reset ARP command has                  |
  +      +                +      +                                                                                +
  |      |                |      | been received.                                                                 |
  +      +                +      +                                                                                +
  |      |                |      | Dependencies: This register bit is valid only if configuration                 |
  +      +                +      +                                                                                +
  |      |                |      | parameter IC_SMBUS_ARP is set to 1.                                            |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 4    | ARP_PREPARE_CMD| R    | Indicates whether a Prepare to ARP command has been received.                  |
  +      +                +      +                                                                                +
  |      | _DET           |      | Dependencies: This register bit is valid only if configuration                 |
  +      +                +      +                                                                                +
  |      |                |      | parameter IC_SMBUS_ARP is set to 1.                                            |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 3    | HOST_NTFY_MST  | R    | Indicates whether a Host Notify command has been received.                     |
  +      +                +      +                                                                                +
  |      | _DET           |      | Dependencies: This register bit is valid only if configuration                 |
  +      +                +      +                                                                                +
  |      |                |      | parameter IC_SMBUS is set to 1.                                                |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 2    | QUICK_CMD_DET  | R    | Indicates whether a Quick command has been received on the                     |
  +      +                +      +                                                                                +
  |      |                |      | SMBus interface regardless of whether DW_apb_i2c is operating in               |
  +      +                +      +                                                                                +
  |      |                |      | slave or master mode. This bit is enabled only when IC_SMBUS=1                 |
  +      +                +      +                                                                                +
  |      |                |      | is set to 1.                                                                   |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 1    | MST_CLOCK_EXTND| R    | Indicates whether the Master device transaction (START-to-ACK,                 |
  +      +                +      +                                                                                +
  |      | _TIMEOUT       |      | ACK-to-ACK, or ACK-to-STOP) from START to STOP exceeds                         |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS_CLOCK_LOW_MEXT time in each byte of message.                          |
  +      +                +      +                                                                                +
  |      |                |      | This bit is enabled only when:                                                 |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS=1                                                                     |
  +      +                +      +                                                                                +
  |      |                |      | IC_CON[0]=1                                                                    |
  +      +                +      +                                                                                +
  |      |                |      | IC_EMPTYFIFO_HOLD_MASTER_EN=1 or                                               |
  +      +                +      +                                                                                +
  |      |                |      | IC_RX_FULL_HLD_BUS_EN=1                                                        |
  +------+----------------+------+--------------------------------------------------------------------------------+

.. table:: 

  +------+----------------+------+--------------------------------------------------------------------------------+
  | 0    | SLV_CLOCK_EXTND| R    | Indicates whether the transaction from Slave (that is, from START to           |
  +      +                +      +                                                                                +
  |      | _TIMEOUT       |      | STOP) exceeds IC_SMBUS_CLOCK_LOW_SEXT time.                                    |
  +      +                +      +                                                                                +
  |      |                |      | This bit is enabled only when                                                  |
  +      +                +      +                                                                                +
  |      |                |      | IC_SMBUS=1                                                                     |
  +      +                +      +                                                                                +
  |      |                |      | IC_CON[0]=1                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_CLR_SMBUS_INTR
"""""""""""""""""

- Name: Clear SMBUS Interrupt Register
  
- Size: 32 bits
  
- Address Offset: 0xD4
  
- Read/Write Access: Write only

.. table:: Clear SMBUS Interrupt Register Field Descriptions

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:11| Reserved       | N/A  | Reserved                                                                       |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 10   | CLR_SMBUS_ALERT| W    | Write this register to clear the SMBUS_ALERT_DET interrupt                     |
  +      +                +      +                                                                                +
  |      | _DET           |      | (bit 10) of the IC_SMBUS_RAW_INTR_STAT register.                               |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 9    | CLR_SMBUS      | W    | Write this register to clear the R_SMBUS_SUSPEND_DET                           |
  +      +                +      +                                                                                +
  |      | _SUSPEND_DET   |      | interrupt (bit 9) of the IC_SMBUS_RAW_INTR_STAT register.                      |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 8    | CLR_SLV_RX     | W    | Write this register to clear the SLV_RX_PEC_NACK interrupt                     |
  +      +                +      +                                                                                +
  |      | _PEC_NACK      |      | (bit 8) of the IC_SMBUS_RAW_INTR_STAT register.                                |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 7    | CLR_ARP_ASSGN  | W    | Write this register to clear the ARP_ASSGN_ADDR_CMD_DET                        |
  +      +                +      +                                                                                +
  |      | _ADDR_CMD_DET  |      | interrupt (bit 7) of the IC_SMBUS_RAW_INTR_STAT register.                      |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 6    | CLR_ARP_GET    | W    | Write this register to clear the ARP_GET_UDID_CMD_DET                          |
  +      +                +      +                                                                                +
  |      | _UDID_CMD_DET  |      | interrupt (bit 6) of the IC_SMBUS_RAW_INTR_STAT register.                      |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 5    | CLR_ARP_RST    | W    | Write this register to clear the ARP_RST_CMD_DET interrupt                     |
  +      +                +      +                                                                                +
  |      | _CMD_DET       |      | (bit 5) of the IC_SMBUS_RAW_INTR_STAT register.                                |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+

.. table:: 

  +------+----------------+------+--------------------------------------------------------------------------------+
  | 4    | CLR_ARP_PREPARE| W    | Write this register to clear the ARP_PREPARE_CMD_DET interrupt                 |
  +      +                +      +                                                                                +
  |      | _CMD_DET       |      | (bit 4) of the IC_SMBUS_RAW_INTR_STAT register.                                |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 3    | CLR_HOST_NOTIFY| W    | Write this register to clear the HOST_NOTIFY_MST_DET interrupt                 |
  +      +                +      +                                                                                +
  |      | _MST_DET       |      | (bit 3) of the IC_SMBUS_RAW_INTR_STAT register.                                |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 2    | CLR_QUICK_CMD  | W    | Write this register to clear the QUICK_CMD_DET interrupt                       |
  +      +                +      +                                                                                +
  |      | _DET           |      | (bit 2)the IC_SMBUS_RAW_INTR_STAT register.                                    |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 1    | CLR_MST_CLOCK  | W    | Write this register to clear the MST_CLOCK_EXTND_TIMEOUT                       |
  +      +                +      +                                                                                +
  |      | _EXTND_TIMEOUT |      | interrupt (bit 1) of the IC_SMBUS_RAW_INTR_STAT register.                      |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 0    | CLR_SLV_CLOCK  | W    | Write this register to clear the SLV_CLOCK_EXTND_TIMEOUT                       |
  +      +                +      +                                                                                +
  |      | _EXTND_TIMEOUT |      | interrupt (bit 0) of the IC_SMBUS_RAW_INTR_STAT register.                      |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_OPTIONAL_SAR
"""""""""""""""

- Name: I2C Optional Slave Address Register
  
- Size: 7 bits
  
- Address Offset: 0xD8
  
- Read/Write Access: Read/Write

.. table::  I2C Optional Slave Address Register Field Descriptions

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 15:11| Reserved       | N/A  | Reserved                                                                       |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 6:1  | IC_OPTIONAL_SAR| R/W  | Optional Slave address for DW_apb_i2c when operating as a slave                |
  +      +                +      +                                                                                +
  |      |                |      | in SMBus Mode.                                                                 |
  +      +                +      +                                                                                +
  |      |                |      | Dependencies: This register bit is valid only if configuration                 |
  +      +                +      +                                                                                +
  |      |                |      | parameter IC_OPTIONAL_SAR is set to 1.                                         |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: IC_OPTIONAL_SAR_DEFAULT                                           |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 0    | CLR_SLV_CLOCK  | W    | Write this register to clear the SLV_CLOCK_EXTND_TIMEOUT                       |
  +      +                +      +                                                                                +
  |      | _EXTND_TIMEOUT |      | interrupt (bit 0) of the IC_SMBUS_RAW_INTR_STAT register.                      |
  +      +                +      +                                                                                +
  |      |                |      | Reset value: 0x0                                                               |
  +------+----------------+------+--------------------------------------------------------------------------------+

IC_SMBUS_UDID_LSB
"""""""""""""""""

- Name: SMBUS ARP UDID LSB Register
  
- Size: 32 bits
  
- Address Offset: 0xDC
  
- Read/Write Access: Read/Write
  
- Dependencies: This register is present only if IC_SMBUS_ARP =1.

This register can be written only when the DW_apb_i2c is disabled, which corresponds to
IC_ENABLE[0] being set to 0. This register is present only if configuration parameter
IC_SMBUS_ARP is set to 1.

This register is used to store the LSB 32 bit value of Slave UDID register used in Address Resolution
Protocol of SMBus.

.. table:: SMBUS ARP UDID LSB Register Field Description

  +------+----------------+------+--------------------------------------------------------------------------------+
  | Bits | Name           | R/W  | Description                                                                    |
  +------+----------------+------+--------------------------------------------------------------------------------+
  | 31:0 | IC_SMBUS_ARP   | R/W  | This field is used to store the LSB 32 bit value of slave unique               |
  +      +                +      +                                                                                +
  |      | _UDID_LSB      |      | device identifier used in Address Resolution Protocol.                         |
  +      +                +      +                                                                                +
  |      |                |      | Reset Value: IC_SMBUS_UDID_LSB_DEFAULT                                         |
  +------+----------------+------+--------------------------------------------------------------------------------+

