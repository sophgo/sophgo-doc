Function description
--------------------

Global reset enable
~~~~~~~~~~~~~~~~~~~

System global soft reset, debug reset and watchdog
reset need to be enabled by configuring the reg_sw_root_reset_en register. Details of each bit are described in reg_sw_root_reset_en.

.. _section_system_control_function_description_sys_dma_channel_map:

System DMA channel mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~

This chip system has 8 built-in DMA channels, each configured with 0 ~ 7 channel request interfaces. Channel requests from 0 to 7 are mapped to one of the peripheral interfaces in the table below by the system control registers sdma_dma_ch_remap0 and sdma_dma_ch_remap1. Note that multiple channels cannot be configured as the same peripheral interface.

Configuration steps:

Configure the DMA channel image register sdma_dma_ch_remap0, sdma_dma_ch_remap1, update_dma_remp_0_3, update_dma_remp_4_7 and write 1 to make the mapping effective.

The system DMA channel mapping is as follows:

.. include:: ../../contents-share/system-control/system_dma_channel_mapping.table.rst

DDR AXI Urgent/Qos configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AXI transmission priority from the subsystem can be configured by ddr_axi_urgent_ow, ddr_axi_urgent, ddr_axi_qos_0, ddr_axi_qos_1 of the control system controller. For details, please refer to the DDR controller chapter :ref:`section_ddr`.