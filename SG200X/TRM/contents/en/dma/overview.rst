Overview
--------

DMA (Direct Memory Access) does not require the CPU to interfere with data one by one. Data can be transferred directly between the memory and the device. This mechanism greatly reduces the CPU control time and increases the data transfer rate. It is very suitable for use in large amounts of data transfer. When the chip is working, it often requires multiple channels of data transmission at the same time. One channel requires a DMA hardware support, and the DMAC (DMA Controller) is responsible for the control of multiple channels. Diagram :ref:`diagram_dma_hardware_control_process` is a DMAC hardware control flow chart. The source and destination devices can be in different AXI sinks.

.. _diagram_dma_hardware_control_process:
.. figure:: ../../../../media/image9.png

	DMAC hardware control flow diagram

