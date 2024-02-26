Way of working
--------------

Clock and Reset
~~~~~~~~~~~~~~~

The DMAC clock is enabled by writing 0x1 to CLK_EN_1[1], so that the clock can work normally. Writing REG_SOFT_RESET_X_SDMA_INIT to 0x0 resets the DMAC, writing 0x1 takes the DMAC out of reset.

Initialization
~~~~~~~~~~~~~~

After reset, you can follow the steps below to initialize

1. Peripheral configuration: In the DMA channel mapping chapter, the configuration method of the DMA peripheral request line is explained. The binding configuration of the peripheral request line is done according to the usage scenario.

2. Confirm that the channel is closed: Write 0x0 to the enable register DMAC_ChEnReg of the 8 channels supported by DMA to confirm that the channel is closed.

3. Confirm the interrupt source: Write 0x0 to the registers DMAC_COMMONREG_INTSIGNAL_ENABLEREG and CHx_INSTATUS_ENABLEREG to turn off all interrupt sources, and then write 0x1 to enable the required interrupt source.

4. Configure the channel priority: When the channel transmits data at the same time, the order of passing will be judged according to the priority level. The larger the value written in the channel register CH_PRIOR, the higher the priority, and the priority will be passed.

Basic Transfer
~~~~~~~~~~~~~~

It can support up to 8 channels for simultaneous transmission. After initialization, the DMAC channel needs to be enabled before data transmission can begin. You can refer to the following steps for memory-to-memory data transmission.

- Read the register DMAC_ChEnReg to obtain the idle channel.

- Write 0x0 to the channel register SRC_MULTBLK_TYPE and DST_MULTBLK_TYPE respectively to configure continuous block transfer.

- Write 0x0 to register TT_FC to configure the channel for memory-to-memory data transfer.

- Write the transferred information into the registers CHx_SAR, CHx_ADR, CHx_BLOCK_TS, CHx_CTL.

- Write 0x1 to the register DMAC_ChEnReg to enable the selected DMA channel.

- Software can obtain the BLOCK_TFR_DONE status through interrupts or polling. When its value rises to 1, it means that the data transmission has been completed. Then write 0x0 to DMAC_ChEnReg to close the channel and restore it to an idle channel.


Linked-list Transfer
~~~~~~~~~~~~~~~~~~~~

Linked-list transfer does not limit the number of nodes. Except for the end node, each node must store information pointing to the next node. Linked-list transfer can be completed by referring to the following steps.

1. Read the register DMAC_ChEnReg to obtain the idle channel.

2. Write 0x3 to the channel register SRC_MULTBLK_TYPE and DST_MULTBLK_TYPE respectively to configure linked list transmission.

3. Configure the registers CHx_LLP, CHx_CTL.ShadowReg_Or_LLI_Valid, CHx_CTL.LLI_Last, and write the information required to point to the first node.

4. Write 0x1 to the register DMAC_ChEnReg to enable the selected DMA channel.

5. The software can obtain the BLOCK_TFR_DONE status through interrupts or polling. When its value rises to 1, it means that the last node data transmission has been completed, and then writes 0x0 to DMAC_ChEnReg to close the channel and restore it to an idle channel.

Interrupt handling
~~~~~~~~~~~~~~~~~~

The processing steps after the interrupt is triggered are as follows:

1. Find the interrupt source: Read the registers CHx_INTSTATUS and DMAC_INSTATUSREG to get the interrupt source whose value is 0x1. When an interrupt occurs, it will be recorded as 0x1 in the corresponding selected bit. If multiple interrupts occur at the same time, the software can service them first according to their priority.

2. Clear interrupts: Write 0x1 to the selected bit of CHx_INTCLEARREG or DMAC_INTCLEARREG. At this time, the interrupt status recorded in CHx_INTSTATUS and DMAC_INSTATUSREG will return to 0x0, and the next interrupt condition will be recorded again.