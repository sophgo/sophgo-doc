功能描述
--------

全局复位使能
~~~~~~~~~~~~

系统全局软复位、Debug 复位跟 WatchDog
复位需要透过配置 reg_sw_root_reset_en 寄存器以使能。详细在 reg_sw_root_reset_en 有各比特之说明。

.. _section_system_control_function_description_sys_dma_channel_map:

系统 DMA 通道映射
~~~~~~~~~~~~~~~~~

本芯片系统 DMA 内建 8 通道，各自配置 0 ~ 7 通道请求接口。而 0 ~ 7 的通道请求由系统控制寄存器 sdma_dma_ch_remap0、sdma_dma_ch_remap1 映射至下表外设接口之一。注意不能将多个通道配置为同一外设接口。

配置步骤：

配置 DMA 信道映像寄存器 sdma_dma_ch_remap0、sdma_dma_ch_remap1、update_dma_remp_0_3、update_dma_remp_4_7 写1，使映射生效。

系统 DMA 通道映射如下表：

.. include:: ./system_dma_channel_mapping.table.rst

DDR AXI Urgent/Qos 配置
~~~~~~~~~~~~~~~~~~~~~~~

可以由控制系统控制器的 ddr_axi_urgent_ow、ddr_axi_urgent、ddr_axi_qos_0、ddr_axi_qos_1 配置来自子系统之 AXI 传输优先级，详细说明参照 DDR 控制器章节 :ref:`section_ddr`。
