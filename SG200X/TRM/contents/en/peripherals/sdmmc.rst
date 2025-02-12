eMMC/SD/SDIO Controller
-----------------------

Function Description
~~~~~~~~~~~~~~~~~~~~

Functional Block Diagram
^^^^^^^^^^^^^^^^^^^^^^^^

The EMMC/SD/SDIO controller (SDMMC controller for short) is used to handle operations such as data reading and writing of SD cards and eMMC, as well as external devices supported by the SDIO protocol (such as Bluetooth, WIFI, etc.). This chip provides three sets of SDMMC controllers. in:

- EMMC supports devices that comply with the eMMC4.1 and eMMC4.5 protocols.

- SDIO0 supports devices that comply with the Secure Digital Memory (SD 3.0) protocol.

- SDIO1 supports devices that comply with the Secure Digital I/O (SDIO 3.0) protocol.

The corresponding functional signals and pins of the three SDMMC controllers in the chip are as shown in the table below.

.. This single table is not large, so there is no need to include a separate file.

.. _table_sdmmc_controller_pins_signals:
.. table:: Corresponding function signals and pin mapping table of SDMMC controller
	:widths: 3 3 4

	+---------------+---------------------+-------------------------------+
	| SDMMC         | Functional Signal   | Pin                           |
	| Controller    |                     |                               |
	+===============+=====================+===============================+
	| eMMC          | EMMC_CLK            | EMMC_CLK                      |
	|               +---------------------+-------------------------------+
	|               | EMMC_CMD            | EMMC_CMD                      |
	|               +---------------------+-------------------------------+
	|               | EMMC_DATA0          | EMMC_DAT0                     |
	|               +---------------------+-------------------------------+
	|               | EMMC_DATA1          | EMMC_DAT1                     |
	|               +---------------------+-------------------------------+
	|               | EMMC_DATA2          | EMMC_DAT2                     |
	|               +---------------------+-------------------------------+
	|               | EMMC_DATA3          | EMMC_DAT3                     |
	|               +---------------------+-------------------------------+
	|               | EMMC_RSTn           | EMMC_RSTN                     |
	+---------------+---------------------+-------------------------------+
	| SDIO0         | SD_CLK              | SD0_CLK                       |
	|               +---------------------+-------------------------------+
	|               | SD_CMD              | SD0_CMD                       |
	|               +---------------------+-------------------------------+
	|               | SD_DATA0            | SD0_D0                        |
	|               +---------------------+-------------------------------+
	|               | SD_DATA1            | SD0_D1                        |
	|               +---------------------+-------------------------------+
	|               | SD_DATA2            | SD0_D2                        |
	|               +---------------------+-------------------------------+
	|               | SD_DATA3            | SD0_D3                        |
	|               +---------------------+-------------------------------+
	|               | SD_CARD_DETECT      | SD0_CD                        |
	|               +---------------------+-------------------------------+
	|               | SD_POWER_EN         | SD0_PWR_EN                    |
	+---------------+---------------------+-------------------------------+
	| SDIO1         | SDIO_CLK            | SD1_CLK                       |
	|               +---------------------+-------------------------------+
	|               | SDIO_CMD            | SD1_CMD                       |
	|               +---------------------+-------------------------------+
	|               | SDIO_DATA0          | SD1_D0                        |
	|               +---------------------+-------------------------------+
	|               | SDIO_DATA1          | SD1_D1                        |
	|               +---------------------+-------------------------------+
	|               | SDIO_DATA2          | SD1_D2                        |
	|               +---------------------+-------------------------------+
	|               | SDIO_DATA3          | SD1_D3                        |
	+---------------+---------------------+-------------------------------+


.. _diagram_sdmmc_controller:
.. figure:: ../../../../media/image109.png
	:align: center

	SDMMC controller functional block diagram

SDMMC functions:

1. Support SD card, SDIO device and eMMC.

2. Transfer data between eMMC/SD/SDIO and system memory data through the internal DMA controller.

3. Supports CRC generation and checking of commands and data.

4. The frequency required between different modes can be generated through the internal frequency divider.

5. Provide a mechanism to turn off the internal clock and the clock on the interface to meet power saving requirements.

6. Provides 1-bit and 4-bit data transmission interfaces to communicate with devices.

7. Supports data read and write operations with block_size equal to 1~2048byte.

8. Support SDIO protocol, including interrupt interval, suspend, resume and read wait operations.

9. Supports AXI/AHB interface and can access system memory through internal DMA.

10. Supports AHB interface, which can access internal registers through CPU.

.. _diagram_sdmmc_typical_usecase:
.. figure:: ../../../../media/image110.png
	:align: center

	typical application

Command and Response
^^^^^^^^^^^^^^^^^^^^
The bus packet of eMMC/SD mainly consists of three parts: command, response and data.

The command and response packets are transmitted through the CMD signal line.

- Command packet

  The command packet is sent from the host to the device to indicate the start of an operation. The packet format consists of 48 bits including start bit, transmission bit, command number, command parameter, CRC verification code and end bit. As shown in :ref:`diagram_emmc_command_format`.

.. _diagram_emmc_command_format:
.. figure:: ../../../../media/image111.png
	:align: center

	eMMC/SD/SDIO command format

- Response Packet

  After receiving the command, the device will return a response according to different command categories to display the status or parameters of the device. Its length is 48 bits or 136 bits. As shown in :ref:`diagram_emmc_response_format`.

.. _diagram_emmc_response_format:
.. figure:: ../../../../media/image112.png
	:align: center

	eMMC/SD/SDIO response format

- Data packet:
  
  Data packets are used to exchange data between the host and the device. According to different needs, 1-bit (DATA0), 4-bit (DATA0-DATA3) or 7-bit (DATA0-DATA7) can be selected. In each clock interval, Each data signal line can choose to transmit (single data rate) or (dual data rate). The packet formats are shown in the diagram :ref:`diagram_emmc_1bit_dataform` ~ the diagram :ref:`diagram_emmc_8bit_dual_dataform`.

.. _diagram_emmc_1bit_dataform:
.. figure:: ../../../../media/image113.png
	:align: center

	eMMC/SD/SDIO 1-bit data packet format

.. _diagram_emmc_4bit_dataform:
.. figure:: ../../../../media/image114.png
	:align: center

	eMMC/SD/SDIO 4-bit data packet format

.. _diagram_emmc_8bit_dataform:
.. figure:: ../../../../media/image115.png
	:align: center

	eMMC/SD/SDIO 8-bit data packet format

.. _diagram_emmc_4bit_dual_dataform:
.. figure:: ../../../../media/image116.png
	:align: center

	4-bit dual data rate data packet format

.. _diagram_emmc_8bit_dual_dataform:
.. figure:: ../../../../media/image117.png
	:align: center

	8-bit dual data rate data packet format

Depending on whether there is data transmission, instructions can be further divided into the following two types:

- Non-data transmission commands: Complete command transmission and receive responses through the signal line CMD.

.. _diagram_nondata_transfer_cmd:
.. figure:: ../../../../media/image118.png
	:align: center

	Non-data transmission instructions: Complete instruction transmission and receive responses through the signal line CMD

- Data transmission instructions: In addition to the interaction on the signal line CMD, there is also data transmission on the data lines DAT0~DAT3

Data Transmission
^^^^^^^^^^^^^^^^^

The data transmission between the host and the device is mainly in blocks. In addition to the data, CRC check bits are also included to verify the correctness of the data. The more commonly used methods are single-block data reading and writing and multi-block data reading and writing. Compared with single-block data transmission, multi-block data transmission has higher efficiency. Among them, the block size of EMMC and SD card is 512byte. SDIO is special and can support block sizes of 1~2048byte. Users can define the block size value according to different devices.

(1) Single block and multi-block read operations are shown in the diagram :ref:`diagram_emmc_read_operation`. Single block transmission consists of instructions, responses, data and CRC. Multi-block transfers end with a reliable STOP CMD to abort the transfer.

.. _diagram_emmc_read_operation:
.. figure:: ../../../../media/image119.png
	:align: center

	Single block and multi-block read operations

(2) Single block and multi-block write operations are as shown in the diagram :ref:`diagram_emmc_write_operation`. The transmission process will send a BUSY signal through the DAT0 signal line to notify the host that the writing device is in progress.

.. _diagram_emmc_write_operation:
.. figure:: ../../../../media/image120.png
	:align: center

	Single block and multi-block write operations

Speed mode and voltage switching supported by SD3.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Voltage switching procedure (1.8V -> 3.3V)

  - Step 1: Set PWRSW to 3.3V.
    => sd_pwrsw_ctrl (0x030001F4) = 0x00000009 
    (reg_pwrsw_auto=1, reg_pwrsw_disc=0, reg_pwrsw_vsel=0(3.0v), reg_en_pwrsw=1)

  - Step 2: Wait 1ms to complete voltage switching.

- Voltage switching procedure (3.3V -> 1.8V)

  - Step 1: Set PWRSW to 1.8V.
    => sd_pwrsw_ctrl (0x030001F4) = 0x0000000B 
    (reg_pwrsw_auto=1, reg_pwrsw_disc=0, reg_pwrsw_vsel=1(1.8v), reg_en_pwrsw=1)

  - Step 2: Wait 1ms to complete voltage switching.

- Support speed mode and voltage

  The speed modes and voltages supported by SD3.0 are as follows.

.. This table is not large, so there is no need to include a separate file.

.. _table_sd3_spreed_voltage:
.. table:: SD3.0 supported speeds and voltages
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Mode                 | Speed   | Voltage                            |
	+======================+=========+====================================+
	| DS (default speed)   | 25Mhz   | 1.8V/3.3V                          |
	+----------------------+---------+------------------------------------+
	| HS (high speed)      | 50Mhz   | 1.8V/3.3V                          |
	+----------------------+---------+------------------------------------+
	| SDR12                | 25Mhz   | 1.8V                               |
	+----------------------+---------+------------------------------------+
	| SDR25                | 50Mhz   | 1.8V                               |
	+----------------------+---------+------------------------------------+
	| DRR50                | 50Mhz   | 1.8V                               |
	+----------------------+---------+------------------------------------+
	| SDR50                | 100Mhz  | 1.8V                               |
	+----------------------+---------+------------------------------------+
	| SDR104               | 187.5Mhz| 1.8V                               |
	+----------------------+---------+------------------------------------+

eMMC supported Speed Modes and Voltages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The speed modes and voltages supported by eMMC are as follows.

.. This table is not large, so there is no need to include a separate file.

.. _table_emmc_speed_mode_voltage:
.. table::  eMMC supported speeds and voltages
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Mode                 | Speed   | Voltage                            |
	+======================+=========+====================================+
	| DS (default speed)   | 26Mhz   | 1.8V/3.3V                          |
	+----------------------+---------+------------------------------------+
	| HS (high speed)      | 52Mhz   | 1.8V/3.3V                          |
	+----------------------+---------+------------------------------------+
	| DRR52                | 52Mhz   | 1.8V                               |
	+----------------------+---------+------------------------------------+
	| HS200                | 187.5Mhz| 1.8V                               |
	+----------------------+---------+------------------------------------+

Application Notes
~~~~~~~~~~~~~~~~~

Clock Shutdown
^^^^^^^^^^^^^^

.. _diagram_emmc_clock_transaction_procedure:
.. figure:: ../../../../media/image121.png
	:align: center
	:scale: 60%

	clock shutdown program

As shown in the diagram :ref:`diagram_emmc_clock_transaction_procedure` is a clock shutdown procedure. The host must ensure that no transmission is taking place on the bus in order to shut down the clock.

(1) Read the temporary register PRESENT_STS.

(2) Check whether the bits CMD_INHIBIT and DAT_INHIBIT are both 0.

(3) If any bit is not 0, it means that the transmission is still in progress and a delay is required.

(4) If both are 0, you can set CLK_CTL[SD_CLK_EN]=0 to turn off the clock.


Soft Reset
^^^^^^^^^^

When the controller operates abnormally, reliably reset the configuration register (base address = 0x0300_3000) to perform a soft reset. The temporary register addresses used are as follows:

1. EMMC: SOFT_RSTN_0[reg_soft_reset_x_emmc] (address offset: 0x000, Bit15)

2. SDIO0: SOFT_RSTN_0[reg_soft_reset_x_sd0] (address offset: 0x000, Bit16)

3. SDIO1: SOFT_RSTN_0[reg_soft_reset_x_sd1] (address offset: 0x000, Bit17)

Interface Clock Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Diagram :ref:`diagram_emmc_clock_config` is a flow chart for interface clock configuration. The SDMMC controller provides a frequency divider inside, allowing users to adjust the required clock frequency according to different protocols and speed modes. Its relationship is:

F\ :sub:`SD_CLK_OUT` = F\ :sub:`INT_CARD_CLK`/ (2 * clk_divisor)

When SDMMC changes the frequency, in addition to ensuring that no instructions and data are still being transmitted, it must also be set according to the steps of the interface clock configuration flow chart to avoid glitches in the clock output to the eMMC/SD device.

(1) Turn off the interface clock.

(2) Calculate the frequency division factor.

(3) Set the frequency division factor. Fill in the parameters calculated in (2) into CLK_CTL[FREQ_SEL], and start turning on the internal clock switch (CLK_CTL[INT_CLK_EN]=1).

(4) Check CLK_CTL[INT_CLK_STABLE] to confirm whether the frequency switching is completed.

(5) If it has not been completed (CLK_CTL[INT_CLK_STABLE]=0), delay and wait.

(6) If switching the clock frequency is completed, turn on the interface clock.

.. _diagram_emmc_clock_config:
.. figure:: ../../../../media/image122.png
	:align: center

	Clock configuration flow chart

Non-Data Transfer Instructions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Command transmission program

   The command transmission program is as shown in the diagram :ref:`diagram_emmc_transmitting_config`.

   (1) First, you must check whether the register bit PRESENT[CMD_INHIBIT] is 0 to confirm whether the CMD Line is still in use.

   (2) If the CMD Line is idle, further confirm whether it is a command with busy. If it is not a busy instruction, you do not need to check the status of the DATA Line and directly execute step (5). Otherwise, if it is a busy instruction, you must execute step (3) to confirm whether it is an Abort instruction.

   (3) If it is an Abort command, it means that when the CMD line completes the transmission, the DATA line is also idle, and you can directly enter step (5); otherwise, if it is not an Abort command, you must execute step (4) to confirm that the DATA line is busy Whether it has been released.

   (4) Check whether the temporary register bit PRESENT[DAT_INHIBIT] is 0 to confirm whether the DATA Line is still in use. If it is still in use, wait until the transmission is completed, and then perform step (5).

   (5) Set the values of the ARGUMENT register and CMD register according to the instruction requirements.

.. _diagram_emmc_transmitting_config:
.. figure:: ../../../../media/image123.png
	:align: center

	command transfer program

- Command Complete Sequence

   The instruction completion procedure is as shown in the diagram :ref:`diagram_emmc_complete_procedure`.

   (1) First, wait for the interrupt NORM_INT_STS[CMD_CMPL] for Command completion.

   (2) After receiving the interrupt, set NORM_INT_STS[CMD_CMPL]=1 to clear the CMD_CMPL interrupt status.

   (3) Then read the RESP1_0, RESP3_2, RESP5_4, RESP7_6 and other temporary registers to obtain the response value.

   (4) If it is an instruction including data transfer, step (5) will be executed, otherwise jump to step (8).

   (5) Wait for data transfer interrupt NORM_INT_STS[XFER_CMPL].

   (6) After receiving the interrupt, set NORM_INT_STS[XFER_CMPL]=1 to clear the XFER_CMPL interrupt status.

   (7) Check RESP1_0, RESP3_2, RESP5_4, RESP7_6 and other temporary registers to confirm whether there is an error status. If there is no error status, perform step (8) and report no error. If there is an error, perform step (9) to report the error.

.. _diagram_emmc_complete_procedure:
.. figure:: ../../../../media/image124.png
	:align: center

	command completion program

Stop or Abort Data Transfer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Abort command program

  The abort command is completed by CMD12 for eMMC/SD devices, and CMD52 for SDIO devices. There are two main situations when using it:

  (1) Stop unlimited module data transmission.

  (2) Stop multi-module data transmission.

  The stop command program is as shown in the diagram: ref:`diagram_emmc_stop_procedure`. The detailed steps are as follows:

  .. _diagram_emmc_stop_procedure:
  .. figure:: ../../../../media/image125.png
  	:align: center

  	abort command program

  There are two ways of aborting instructions: synchronous abort instruction and asynchronous abort instruction.

- Asynchronous abort command program

  Diagram :ref:`diagram_emmc_nonsync_stop_procedure` is the program diagram of the non-synchronous stop instruction. Detailed steps are as follows:

  (1) Execute abort instructions according to different transmission modes.

  (2) Set SW_RST_CMD and SW_RST_DAT in the SW_RESET register to reset the CMD and DAT signal lines.

  (3) Check the bits SW_RESET[SW_RST_CMD] and SW_RESET[SW_RST_DAT] to confirm whether the reset is completed. If both are 0, end the program. If one of them is 1, return to step (3) and wait for a delay.

.. _diagram_emmc_nonsync_stop_procedure:
.. figure:: ../../../../media/image126.png
	:align: center

	Program chart of asynchronous abort instruction

- Synchronous abort command program

  Diagram :ref:`diagram_emmc_sync_stop_procedure` is the program diagram of the synchronization stop instruction. Detailed steps are as follows:

  (1) Writing bit BG_CTL[STOP_BG_REQ] stops transmission in the Block Gap interval.

  (2) Interrupt NORM_INT_STS[XFER_CMPL] waiting for transfer completion.

  (3) After receiving the interrupt, set NORM_INT_STS[XFER_CMPL]=1 to clear the XFER_CMPL interrupt status.

  (4) Execute abort instructions according to different transmission modes.

  (5) Set SW_RST_CMD and SW_RST_DAT in the SW_RESET register to reset the CMD and DAT signal lines.

  (6) Check the bits SW_RESET[SW_RST_CMD] and SW_RESET[SW_RST_DAT] to confirm whether the reset is completed. If both are 0, end the program. If one of them is 1, return to step (6) to delay waiting.

.. _diagram_emmc_sync_stop_procedure:
.. figure:: ../../../../media/image127.png
	:align: center

	Program chart of synchronization abort instruction

Non-DMA data Transfer Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^

The program for non-DMA data transfer mode is as shown in the diagram :ref:`diagram_nodma_data_transfer`. Detailed steps are as follows:

(1) Write to the BLK_SIZE register to set the block size.

(2) Write to the BLK_CNT register to set the number of blocks.

(3) Write to the ARGUMENT register to set the command parameters.

(4) Write to the XFER_MODE register to set the transmission mode. The host can determine settings based on usage scenarios. Contains Single or Multiple Block Select, DMA Enable, Block Count Enable, Data Transfer Direction, Auto CMD Enable.

(5) Write to the CMD register to set the command and response types.

(6) Interrupt NORM_INT_STS[CMD_CMPL] waiting for Command completion.

(7) After receiving the interrupt, set NORM_INT_STS[CMD_CMPL]=1 to clear the CMD_CMPL interrupt status.

(8) Then read the RESP1_0, RESP3_2, RESP5_4, RESP7_6 and other temporary registers to obtain the response value.

(9) If it is a read operation, step (14) will be executed, if it is a write operation, step (10) will be executed.

(10) Waiting for the Buffer Write Ready interrupt NORM_INT_STS[BUF_WRDY].

(11) After receiving the interrupt, set NORM_INT_STS[BUFF_WRDY]=1 to clear the BUFF_WRDY interrupt status.

(12) Write the data you want to write to the device sequentially into the BUF_DATA register.

(13) If there are more blocks to be written, go back to step (10) until the last block is written, then go to step (18).

(14) Waiting for the Buffer Read Ready interrupt NORM_INT_STS[BUF_RRDY].

(15) After receiving the interrupt, set NORM_INT_STS[BUFF_RRDY]=1 to clear the BUFF_RRDY interrupt status.

(16) Read the data received from the device in sequence from the BUF_DATA register.

(17) If there are more blocks to be read, go back to step (14) until the last block is read, then go to step (18).

(18) Determine whether it is single module transmission, multi-module transmission or unlimited module transmission. If it is a single module or multi-module transmission, skip to step (19). If it is an infinite module transfer, jump to step (21) and perform the action of aborting the transfer.

(19) Interrupt NORM_INT_STS[XFER_CMPL] waiting for completion of data transfer.

(20) After receiving the interrupt, set NORM_INT_STS[CMD_XFER]=1 to clear the XFER_CMPL interrupt status.

(21) Execute the abort transfer procedure.

.. _diagram_nodma_data_transfer:
.. figure:: ../../../../media/image128.png
	:align: center

	Program for non-DMA data transfer mode

SDMA Data Transfer Mode
^^^^^^^^^^^^^^^^^^^^^^^

The SDMA data transfer mode program is shown in the diagram: ref:`diagram_sdma_data_transfer`, and the detailed steps are as follows:

(1) Write to the SDMA_SA register to set the starting address of the system memory used for data transmission.

(2) Write to the BLK_SIZE register to set the block size.

(3) Write to the BLK_CNT register to set the number of blocks.

(4) Write to the ARGUMENT register to set the command parameters.

(5) Write to the XFER_MODE register to set the transmission mode. The host can determine settings based on usage scenarios. Contains Single or Multiple Block Select, DMA Enable, Block Count Enable, Data Transfer Direction, Auto CMD Enable.

(6) Write to the CMD register to set the command and response types.

(7) Interrupt NORM_INT_STS[CMD_CMPL] waiting for Command completion.

(8) After receiving the interrupt, set NORM_INT_STS[CMD_CMPL]=1 to clear the CMD_CMPL interrupt status.

(9) Then read the RESP1_0, RESP3_2, RESP5_4, RESP7_6 and other temporary registers to obtain the response value.

(10) Wait for data transfer interrupt and DMA interrupt.

(11) Read the interrupt status register NORM_INT_STS to determine the interrupt type. Skip to step (12) if it is a DMA interrupt, or skip to step (14) if it is a data transfer interrupt.

(12) Set NORM_INT_STS[DMA_INT]=1 to clear the DMA_INT status value.

(13) Write to the SDMA_SA register to reset the starting address of the system memory for the next DMA. Then skip to step (10).

(14) Set NORM_INT_STS[DMA_INT]=1 and [NORM_INT_STS[XFER_CMPL]=1 to clear the DMA_INT and XFER_CMPL status values. Then end the program.

.. _diagram_sdma_data_transfer:
.. figure:: ../../../../media/image129.png
	:align: center

	SDMA data transfer mode program

ADMA Data Transfer Mode
^^^^^^^^^^^^^^^^^^^^^^^

The ADMA data transfer mode program is shown in the diagram :ref:`diagram_adma_data_transfer`, and the detailed steps are as follows:

(1) Fill in the ADMA description table into the system memory.

(2) Write to the ADMA_SA_L and ADMA_SA_H registers to set the starting address of the system memory used by the description table.

(3) Write to the BLK_SIZE register to set the block size.

(4) Write to the BLK_CNT register to set the number of blocks.

(5) Write to the ARGUMENT register to set the command parameters.

(6) Write to the XFER_MODE register to set the transmission mode. The host can determine settings based on usage scenarios. Contains Single or Multiple Block Select, DMA Enable, Block Count Enable, Data Transfer Direction, Auto CMD Enable.

(7) Write to the CMD register to set the command and response types.

(8) Interrupt NORM_INT_STS[CMD_CMPL] waiting for Command completion.

(9) After receiving the interrupt, set NORM_INT_STS[CMD_CMPL]=1 to clear the CMD_CMPL interrupt status.

(10) Then read the RESP1_0, RESP3_2, RESP5_4, RESP7_6 and other temporary registers to obtain the response value.

(11) Wait for data transfer interrupt or ADMA Error interrupt.

(12) Read the interrupt status register NORM_INT_STS and ERR_INT_STS to determine the interrupt type. Skip to step (13) if it is an ADMA error interrupt, or step (15) if it is a data transfer interrupt.

(13) Set ERR_INT_STS[ADMA_ERR]=1 to clear the ADMA_ERR status value.

(14) Enter the ADMA Abort Transaction program (ADMA Abort Transaction) and execute the Abort Command to abort the data transfer with the device. If necessary, you can check the ADMA Error Status register to check the cause of the error.

(15) Set NORM_INT_STS[XFER_CMPL]=1 to clear the XFER_CMPL status value. Then end the program.

.. _diagram_adma_data_transfer:
.. figure:: ../../../../media/image130.png
	:align: center

	ADMA data transfer mode program

Register Overview
~~~~~~~~~~~~~~~~~

Table :ref:`table_sdmmc_register_overview` is the SDMMC register overview (the base address of EMMC is 0x0430_0000, SDIO0 is 0x0431_0000, SDIO1 is 0x0500_0000)

Note: Default offset address 0x200 is configured for P_VENDOR_SPECIFIC_AREA, so the address offset values from EMMC_CTRL to PHY_CONFIG are based on the value of P_VENDOR_SPECIFIC_AREA plus a relative offset value (multiple of 4), for example, EMMC_CTRL = 0x200 + 0x0, EMMC_BOOT_CTL = 0x200 + 0x4, and so on.

.. include:: ../../contents-share/peripherals/sdmmc_register_overview.table.rst

Register Description
~~~~~~~~~~~~~~~~~~~~

The following is a detailed register description.

.. include:: ../../contents-share/peripherals/sdmmc_register_description.table.rst
