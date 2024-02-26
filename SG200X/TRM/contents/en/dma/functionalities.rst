Function Description
--------------------

Peripheral Request Line
~~~~~~~~~~~~~~~~~~~~~~~

DMA has 8 built-in DMA channels, and each channel's peripheral request needs to be configured to be mapped to the peripheral. Please refer to :ref:`section_system_control_function_description_sys_dma_channel_map` instructions to configure the DMA channel before enabling it.

Access Space
~~~~~~~~~~~~

.. include:: ../../contents-share/dma/dmac_access_space_type.table.rst

Basic Transfer
~~~~~~~~~~~~~~

DMA data transmission is set in blocks and completed by burst transmission. The length of burst transmission can be set, but what often happens is that the amount of block data is not perfectly an integer multiple of the burst transmission length. The length of the last transaction transmitted will be less than the set burst transmission length, and a single transmission request will be required to complete it.

The sources and destinations of the maximum supported 8 DMA channels can have the following four combinations:

a. RAM to RAM.

b. Memory to device.

c. Device to memory.

d. Device to device.

.. _diagram_dma_transfer_level:
.. figure:: ../../../../media/image10.png

	DMA transfer layer

The amount of data to be transferred individually can be calculated by the value written to the following scratchpad

- Source transfer data volume (bytes):

  src_single_size_bytes = CHx_CTL.SRC_TR_WIDTH/8

- Source burst transfer data volume (bytes):

  src_burst_size_bytes = CHx_CTL.SRC_MSIZE \* src_single_size_bytes

- Target transfer data volume (bytes):

  dst_single_size_bytes = CHx_CTL.DST_TR_WIDTH/8

- Target burst transfer data volume (bytes):

  dst_burst_size_bytes = CHx_CTL.DST_MSIZE \* dst_single_size_bytes

The transmission process control can be controlled by the DMA controller or the source device or the destination device. When performing block data transfer, the amount of data transferred is calculated as follows:

- The transfer process is controlled by the DMA controller:

  blk_size_bytes_dma = CHx_BLOCK_TS.BLOCK_TS \* src_single_size_bytes

- The source device controls the transfer process:

  blk_size_bytes_src = (number of block burst transfers issued by the source device \*
  src_burst_size_bytes) + (number of individual block transfers from source device \*
  src_single_size_bytes)

- The destination device controls the transfer process:

  blk_size_bytes_dst = (number of block burst transfers sent by the destination device \*
  dst_burst_size_bytes) + (Number of separate transfers of destination device blocks \*
  dst_single_size_bytes)

Linked-list Transfer
~~~~~~~~~~~~~~~~~~~~

Linked-list transmission is used when block transmission of multiple discontinuous addresses is required. Each block of data will be followed by a linked-list information to store the information of the next node, so that no CPU intervention is required during data transmission. Block transfer of the next discontinuous space can be performed directly. Diagram :ref:`diagram_link_relative_bit_data_format` is the configuration format of the linked list information. It must comply with the information format to enter the linked list transmission work.

.. _diagram_link_relative_bit_data_format:
.. figure:: ../../../../media/image11.png

	Linked list relative address and data format

Interrupts and Status
~~~~~~~~~~~~~~~~~~~~~

The interrupt sources of DMAC are as follows:

a. Triggered by DMA transfer completion.

b. Triggered by block transfer completion.

c. Triggered when a single transfer is completed.

d. Internal error trigger.

e. Channel abort trigger or channel cancel trigger.

Diagram :ref:`diagram_interrupt_status_source` is a diagram of interrupt status and source:

.. _diagram_interrupt_status_source:
.. figure:: ../../../../media/image12.png

	Interrupt status and source diagram

Channel Security Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Channel security can be implemented by the awprot value and arprot value of each channel. It complies with the AXI bus protocol. When the channel is a safe channel, the arprot or awprot value needs to be 0x0. If it is other values, it is an unsafe channel.