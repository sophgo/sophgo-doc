工作方式
--------

时钟和复位
~~~~~~~~~~

DMAC 的时钟经由 CLK_EN_1[1] 写入 0x1 后使能, 时钟方可正常工作。将 REG_SOFT_RESET_X_SDMA_INIT 写入 0x0 可将 DMAC 复位，写入 0x1 将 DMAC 离开复位。

初始化
~~~~~~

进行复位后, 可按照以下步骤进行初始化

1. 外设配置: 在 DMA 通道映射章节说明了 DMA 的外设请求线的的配置方法, 根据使用的场景做外设请求线的绑定配置。

2. 确认通道关闭: 将 DMA 支持的 8 个通道的使能寄存器 DMAC_ChEnReg 写入 0x0, 确认通道关闭。

3. 确认中断来源: 将寄存器 DMAC_COMMONREG_INTSIGNAL_ENABLEREG 与 CHx_INSTATUS_ENABLEREG 写入 0x0 关闭所有中断来源，再将需求的中断来源写入 0x1 使能。

4. 配置通道优先权: 通道同时数据传输时会按照优先权的等级来裁判通过的顺序，通道寄存器 CH_PRIOR 写入的值越大，优先等级越高，优先通过。


基本传输
~~~~~~~~

最大可支持 8 个通道同时传输, 在初始化后需使能 DMAC 通道方可开始进行数据传输, 可参考以下步骤进行内存到内存的数据传输

-  读取寄存器 DMAC_ChEnReg 获得闲置通道。

-  分别将 0x0 写入通道寄存器 SRC_MULTBLK_TYPE, DST_MULTBLK_TYPE 配置为连续块状传输。

-  将 0x0 写入寄存器 TT_FC, 将通道配置为内存到内存数据传输。

-  将传输的信息写入寄存器 CHx_SAR, CHx_ADR, CHx_BLOCK_TS, CHx_CTL。

-  将 0x1 写入寄存器 DMAC_ChEnReg, 将选定的DMA通道使能。

-  软件可通过中断或轮询的方式获得 BLOCK_TFR_DONE 状态, 当其值上升为1时, 即表示数据传输已完成, 再将 0x0 写入 DMAC_ChEnReg 关闭通道, 使其恢复为闲置通道。


链表传输 
~~~~~~~~~

链表传输不限定节点的数目， 除了结束的节点, 每个节点必须存有指向下一个节点的信息，链表传输可参考以下步骤完成

1. 读取寄存器 DMAC_ChEnReg 获得闲置通道。

2. 分别将 0x3 写入通道寄存器 SRC_MULTBLK_TYPE, DST_MULTBLK_TYPE 配置为链表传输。

3. 配置寄存器 CHx_LLP, CHx_CTL.ShadowReg_Or_LLI_Valid, CHx_CTL.LLI_Last, 将指向第一个节点所需的信息写入。

4. 将 0x1 写入寄存器 DMAC_ChEnReg, 将选定的 DMA 通道使能。

5. 软件可通过中断或轮询的方式获得 BLOCK_TFR_DONE 状态，当其值上升为 1 时, 即表示最后一个节点数据传输已完成, 再将 0x0 写入 DMAC_ChEnReg 关闭通道, 使其恢复为闲置通道。

中断处理 
~~~~~~~~~

中断触发后的处理步骤如下

1. 找出中断来源: 读取寄存器 CHx_INTSTATUS 与 DMAC_INSTATUSREG 来获得其值为 0x1 的中断来源。当中断发生后，会被记录为 0x1 在对应的选定位元上，若同时有多个中断发生，软件可依其优先等级先服务。

2. 清除中断: 写 0x1 到 CHx_INTCLEARREG 或 DMAC_INTCLEARREG 的选定位元上，此时记录在 CHx_INTSTATUS 与 DMAC_INSTATUSREG 的中断状态会回复为 0x0, 重新记录下一次的中断条件发生。

