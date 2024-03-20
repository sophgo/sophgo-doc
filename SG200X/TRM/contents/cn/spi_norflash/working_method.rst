工作流程
--------

初始化流程
~~~~~~~~~~

- 步骤 1. 如果需要调整 Timing 参数, 根据器件配置 SPI Clock Divider。

- 步骤 2. 配置中断控制寄存器。

器件状态寄存器操作
~~~~~~~~~~~~~~~~~~

- 步骤 1. 配置传输数据长度。

- 步骤 2. 传输模式相关配置。

- 步骤 3. 配置 reg_go_busy。

- 步骤 4. 将传输内容写入缓存。

- 步骤 5. 检测 INT_STS, 等待操作完成。

SPI NOR Flash 地址模式切换流程
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

对于SPI NOR Flash器件, 支持 3 Byte 与 4 Byte 两种 Flash 地址模式，可以在芯片启动起来之后通过配置寄存器动态切换地址模式。在芯片启动起来之后切换 Flash 地址模式的步骤如下:

- 步骤 1. 无 Flash 操作或保证之前对 Flash 器件之操作完成。

- 步骤 2. 根据器件要求，用寄存器操作方式配置器件的相关寄存器发特定命令配置 Flash 进入4 Byte 模式。

- 步骤 3. 配置 SPI NOR Flash 控制器 [reg_byte4en] 式为 4 Byte 模式，完成 3 Byte 模式到 4 Byte 模式切换。

DMA 读操作流程
~~~~~~~~~~~~~~

- 步骤 1. 禁止 dmmr 模式，禁止 dma_en。

- 步骤 2. 写 FF_PT 为1, 以清空 FIFO 及重置读写指标。

- 步骤 3. 使能 dmmr 模式。

- 步骤 4. 配置系统 DMA 为 mem-to-mem 搬移。 DST_TR_WIDTH = 0x2 (transaction width is 32bit)、DST_MSIZE = 0x0 (burst transaction length =1)、BLOCK_TS = TRAN_NUM/4 -1 。 实际上之 BLOCK_TS/ DST_TR_WIDTH/ DST_MSIZE 需根据实际传输长度做适当的配置。

- 步骤 5. 使能系统 DMA 选定通道。开始搬移。

- 步骤 6. 等待 DMA 相应通道中断。表示 DMA 读取完成。

DMA 写操作流程
~~~~~~~~~~~~~~

- 步骤 1. 禁止 dmmr 模式，禁止 dma_en。

- 步骤 2. 写 FF_PT 为1, 以清空 FIFO 及重置读写指标。

- 步骤 3. 配置系统 DMA 通道映射，将选定的 DMA 通道映射至 39:dma_req_spi_nor。

- 步骤 4. 配置系统 DMA 为 peri-to-mem 搬移。DST_TR_WIDTH = 0x2 (transaction width is 32bit)、DST_MSIZE = 0x0 (burst transaction length =1)、BLOCK_TS = TRAN_NUM/4 -1 。 实际上之 BLOCK_TS/ DST_TR_WIDTH/ DST_MSIZE 需根据实际传输长度做适当的配置。

- 步骤 5. 使能系统 DMA 选定通道。

- 步骤 6. 配置 SPI_NOR 寄存器 TRAN_NUM, 不包含指令及地址。

- 步骤 7. 配置 SPI_NOR 寄存器 TRAN_CSR, tran_mode = 0x2 (tx only)、fast_mode、bus_width, addr_bn、dma_en=0及reg_go_busy。 Ex: TRAN_CSR = 0x0000BC2A。

- 步骤 8. 对 SPI_NOR 寄存器 FF_PORT 写入 command and address。

- 步骤 9. 查询 SPI_NOR 寄存器 rdat_ff_pt 为 0, 确保 command 及 address 发送完毕。

- 步骤 10. 配置 SPI_NOR 寄存器 TRAN_CSR 使能 dma_en。

- 步骤 11. 检测 SPI_NOR 寄存器 INT_STS, 等待操作完成, 表示缓冲区内容已写入器件。

其它注意事项
~~~~~~~~~~~~

- 对器件操作未完成前，不可改动相关寄存器配置，否则可能导致操作不正常。
