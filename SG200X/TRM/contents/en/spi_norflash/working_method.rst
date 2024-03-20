Work Process
------------

Initialization Process
~~~~~~~~~~~~~~~~~~~~~~

- Step 1. If you need to adjust the Timing parameters, configure the SPI Clock Divider according to the device.

- Step 2. Configure the interrupt control register.

Device Status Register Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Step 1. Configure the transmission data length.

- Step 2. Transmission mode related configuration.

- Step 3. Configure reg_go_busy.

- Step 4. Write the transfer to cache.

- Step 5. Detect INT_STS and wait for the operation to complete.

SPI NOR Flash Address Mode Switching Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For SPI NOR Flash devices, it supports two Flash address modes of 3 Byte and 4 Byte. The address mode can be dynamically switched through the configuration register after the chip is started. The steps to switch the Flash address mode after the chip starts up are as follows:

- Step 1. No Flash operation or ensure that the previous operation on the Flash device is completed.

- Step 2. According to the device requirements, use the register operation mode to configure the relevant registers of the device and send specific commands to configure the Flash to enter 4 Byte mode.

- Step 3. Configure the SPI NOR Flash controller [reg_byte4en] format to 4 Byte mode and complete the switch from 3 Byte mode to 4 Byte mode.

DMA Read Operation Process
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Step 1. Disable dmmr mode, disable dma_en.

- Step 2. Write 1 to FF_PT to clear the FIFO and reset the read and write indicators.

- Step 3. Enable dmmr mode.

- Step 4. Configure the system DMA for mem-to-mem migration. DST_TR_WIDTH = 0x2 (transaction width is 32bit), DST_MSIZE = 0x0 (burst transaction length =1), BLOCK_TS = TRAN_NUM/4 -1. In fact, BLOCK_TS/ DST_TR_WIDTH/ DST_MSIZE needs to be configured appropriately according to the actual transmission length.

- Step 5. Enable system DMA for selected channels. Start moving.

- Step 6. Wait for DMA corresponding channel interrupt, which indicates that DMA reading is completed.

DMA Write Operation Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Step 1. Disable dmmr mode, disable dma_en.

- Step 2. Write 1 to FF_PT to clear the FIFO and reset the read and write indicators.

- Step 3. Configure the system DMA channel mapping to map the selected DMA channel to 39:dma_req_spi_nor.

- Step 4. Configure the system DMA for peri-to-mem migration. DST_TR_WIDTH = 0x2 (transaction width is 32bit), DST_MSIZE = 0x0 (burst transaction length =1), BLOCK_TS = TRAN_NUM/4 -1. In fact, BLOCK_TS/ DST_TR_WIDTH/ DST_MSIZE needs to be configured appropriately according to the actual transmission length.

- Step 5. Enable system DMA for selected channels.

- Step 6. Configure the SPI_NOR register TRAN_NUM, which does not contain instructions and addresses.

- Step 7. Configure SPI_NOR register TRAN_CSR, tran_mode = 0x2 (tx only), fast_mode, bus_width, addr_bn, dma_en=0 and reg_go_busy. Ex: TRAN_CSR = 0x0000BC2A.

- Step 8. Write command and address to SPI_NOR register FF_PORT.

- Step 9. Check the SPI_NOR register rdat_ff_pt for 0, and ensure that the command and address have been sent.

- Step 10. Configure SPI_NOR register TRAN_CSR to enable dma_en.

- Step 11. Detect the SPI_NOR register INT_STS and wait for the operation to complete, indicating that the buffer content has been written to the device.

Other things to note
~~~~~~~~~~~~~~~~~~~~

- Do not change the relevant register configuration before the device operation is completed, otherwise it may cause abnormal operation.