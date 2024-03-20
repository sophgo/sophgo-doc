功能描述 
---------

外设请求线
~~~~~~~~~~

DMA 内建 8 组 DMA 通道, 每个通道之外设请求, 都需要配置以映射到外设。请参照 :ref:`section_system_control_function_description_sys_dma_channel_map` 说明，在 DMA 通道使能前进行配置。

访问空间
~~~~~~~~

.. include:: ./dmac_access_space_type.table.rst

基本传输
~~~~~~~~

DMA 数据传输是以块状来设定， 由突发传输来完成，突发传输的长度是可以设定的，但经常发生的是块状数据量并不完美的是突发传输长度的整数倍数，传输的最后一个交易会出现长度小于设定的突发传输长度，此时会需要使用单笔传输的请求来完成。

最大支持的 8 个 DMA 通道的来源与目的可以有以下四种组合：

a. 内存记忆体到内存记忆体。

b. 内存记忆体到设备。

c. 设备到内存记忆体。

d. 设备到设备。

.. _diagram_dma_transfer_level:
.. figure:: ../../../../media/image10.png

	DMA 传输阶层

单独传输数据量可由以下暂存器写入的值来计算

- 来源传输数据量 (bytes) :

  src_single_size_bytes = CHx_CTL.SRC_TR_WIDTH/8

- 来源突发传输数据量 (bytes):

  src_burst_size_bytes = CHx_CTL.SRC_MSIZE \* src_single_size_bytes

- 目标传输数据量 (bytes):

  dst_single_size_bytes = CHx_CTL.DST_TR_WIDTH/8

- 目标突发传输数据量 (bytes):

  dst_burst_size_bytes = CHx_CTL.DST_MSIZE \* dst_single_size_bytes

传输流程控制权可由DMA控制器或来源装置或目的装置来控制, 当进行块状数据传输时, 传输数据量计算如下:

- 由 DMA 控制器控制传输流程:

  blk_size_bytes_dma = CHx_BLOCK_TS.BLOCK_TS \* src_single_size_bytes

- 由来源装置控制传输流程:

  blk_size_bytes_src = (来源装置发出区块突发传输次数 \*
  src_burst_size_bytes) + (来源装置区块单独传输次数 \*
  src_single_size_bytes)

- 由目的装置控制传输流程:

  blk_size_bytes_dst = (目的装置发出区块突发传输次数 \*
  dst_burst_size_bytes) + (目的装置区块单独传输次数 \*
  dst_single_size_bytes)

链表传输
~~~~~~~~

链表传输使用在需要进行多个不连续位址的块状传输，在每个块状资料后面会带着一个链表信息，存放着下一个节点的信息，使得数据传输时不需要CPU的干预, 能直接进行下一个不连续空间的块状传输。图表 :ref:`diagram_link_relative_bit_data_format` 为链表信息的配置格式, 必须符合信息格式才能进入链表传输工作。

.. _diagram_link_relative_bit_data_format:
.. figure:: ../../../../media/image11.png

	链表相对位址与数据格式

中断和状态
~~~~~~~~~~

DMAC的中断来源为以下:

a. DMA 传输完成触发。

b. 块状传输完成触发。

c. 单笔传输完成触发。

d. 内部错误触发。

e. 通道中止触发或通道取消触发。

图表 :ref:`diagram_interrupt_status_source` 为中断状态和来源示意图:

.. _diagram_interrupt_status_source:
.. figure:: ../../../../media/image12.png

	中断状态和来源示意图


通道安全配置
~~~~~~~~~~~~

通道安全可用各通道的 awprot 值与 arprot 值来实现，遵从 AXI 总线协议，当通道为安全通道时，arprot 或awprot 值需为 0x0，若为其他值则为非安全通道。
