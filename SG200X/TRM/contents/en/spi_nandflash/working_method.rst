Work Process
~~~~~~~~~~~~

Initialization Process
^^^^^^^^^^^^^^^^^^^^^^

- Step 1: (If the Timing parameters need to be adjusted) Configure the timing registers reg_trx_sck_h and reg_trx_sck_l according to the device.

- Step 2: Configure the interrupt control register reg_trx_done_int_en.

Device Register Operation Flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Step 1: Configure the transmission data length reg_trx_cmd_cont_size and reg_trx_data_size.

- Step 2: Configure the device instructions and their related contents reg_trx_cmd_id, reg_trx_cmd_cont0 and reg_trx_cmd_cont1.

- Step 3: Configure the reg_trx_start register issuing operation.

- Step 4: reg_trx_done_int is detected, indicating that the operation is completed.

Erase Operation Process
^^^^^^^^^^^^^^^^^^^^^^^

For flash operations, erasing must be performed before programming operations, and WREN operations must be completed before erasing operations.

- Step 1: Configure the transmission data length reg_trx_cmd_cont_size.

- Step 2: Configure the device instructions and their related contents reg_trx_cmd_id, reg_trx_cmd_cont0.

- Step 3: Configure the reg_trx_start register issuing operation.

- Step 4: reg_trx_done_int is detected, indicating that the operation is completed.

Built-in DMA Read Operation Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Step 1: Configure system DMA registers, refer to :ref:`section_dma_registers`.

- Step 2: Configure the transmission data length reg_trx_cmd_cont_size and reg_trx_data_size.

- Step 3: Configure the device instructions and their related contents reg_trx_cmd_id, reg_trx_cmd_cont0 and reg_trx_cmd_cont1.

- Step 4: Configure the reg_trx_start register to issue operations.

- Step 5: reg_trx_done_int is detected, indicating that the device content has been read and written to the buffer.

Built-in DMA Write Operation Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Step 1: Configure system DMA registers, refer to :ref:`section_dma_registers`.

- Step 2: Configure the transmission data length reg_trx_cmd_cont_size and reg_trx_data_size.

- Step 3: Configure the device instructions and their related contents reg_trx_cmd_id, reg_trx_cmd_cont0 and reg_trx_cmd_cont1.

- Step 4: Configure the eg_trx_start register issuing operation.

- Step 5: reg_trx_done_int is detected, indicating that the buffer content has been written to the device cache.

Other things to note
^^^^^^^^^^^^^^^^^^^^

- Some SPI NAND Flash devices require a RESET operation of the device before use or after an abnormal reset; therefore, for device compatibility considerations, the first transmission command after starting use or an abnormal reset must be RESET.

- Do not change the relevant register configuration before the device operation is completed, otherwise it may cause abnormal operation.