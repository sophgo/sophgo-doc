概述
----

DMA (Direct Memory Access) 不需 CPU 逐笔数据干涉, 存储器与设备间可直接数据传输， 此机制大大减少 CPU 控制时间，并提高数据传输的速率， 非常适合使用在大量数据传输。芯片工作时往往同时需要多通道的数据传输，一个通道需要一个 DMA 硬件支持, DMAC (DMA 控制器) 负责了多通道的控制。 图表 :ref:`diagram_dma_hardware_control_process` 为DMAC 硬件控制流程图, 来源与目的设备可在不同的 AXI 汇流。

.. _diagram_dma_hardware_control_process:
.. figure:: ../../../../media/image9.png

	DMAC 硬件控制流程示意图

