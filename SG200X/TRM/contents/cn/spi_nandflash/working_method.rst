工作流程
~~~~~~~~

初始化流程
^^^^^^^^^^

- 步骤 1: （如果需要调整 Timing 参数）根据器件配置时序寄存器 reg_trx_sck_h 及 reg_trx_sck_l。

- 步骤 2: 配置中断控制寄存器 reg_trx_done_int_en。

器件寄存器操作流程
^^^^^^^^^^^^^^^^^^

- 步骤 1: 配置传输数据长度 reg_trx_cmd_cont_size 及 reg_trx_data_size。

- 步骤 2: 配置器件指令其相关内容 reg_trx_cmd_id、reg_trx_cmd_cont0 及 reg_trx_cmd_cont1。

- 步骤 3: 配置 reg_trx_start 寄存器下发操作。

- 步骤 4: 检测到reg_trx_done_int, 表示操作完成。

擦除操作流程
^^^^^^^^^^^^

对于flash操作, 在编程操作前, 都必须进行擦除, 在擦除操作前还必须完成 WREN 操作。

- 步骤 1: 配置传输数据长度 reg_trx_cmd_cont_size。

- 步骤 2: 配置器件指令其相关内容 reg_trx_cmd_id、 reg_trx_cmd_cont0。

- 步骤 3: 配置 reg_trx_start 寄存器下发操作。

- 步骤 4: 检测到 reg_trx_done_int, 表示操作完成。

内置 DMA 读操作流程
^^^^^^^^^^^^^^^^^^^

- 步骤 1: 配置系统 DMA 寄存器，参照 :ref:`section_dma_registers`。

- 步骤 2: 配置传输数据长度 reg_trx_cmd_cont_size 、reg_trx_data_size。

- 步骤 3: 配置器件指令其相关内容 reg_trx_cmd_id、reg_trx_cmd_cont0及reg_trx_cmd_cont1。

- 步骤 4: 配置 reg_trx_start 寄存器下发操作。

- 步骤 5: 检测到 reg_trx_done_int, 表示器件内容完成读取且已写入缓冲区。

内置 DMA 写操作流程
^^^^^^^^^^^^^^^^^^^

- 步骤 1: 配置系统 DMA 寄存器，参照 :ref:`section_dma_registers`。

- 步骤 2: 配置传输数据长度 reg_trx_cmd_cont_size 、reg_trx_data_size。

- 步骤 3: 配置器件指令其相关内容 reg_trx_cmd_id、reg_trx_cmd_cont0及reg_trx_cmd_cont1。

- 步骤 4: 配置 eg_trx_start 寄存器下发操作。

- 步骤 5: 检测到 reg_trx_done_int, 表示缓冲区内容已写入器件 cache 完成。

其它注意事项
^^^^^^^^^^^^

- 部分 SPI NAND Flash 器件要求在使用之前或者异常复位后必须先进行器件的 RESET 操作；所以为器件相容性考量，开始使用或异常复位后的第一个传输指令需为 RESET。

- 对器件操作未完成前，不可改动相关寄存器配置，否则可能导致操作不正常。

