时钟资源与分频结构
------------------

系统时钟来源主要来自外部 XTAL。XTAL 通过 PLL 对其倍频。如 :ref:`diagram_clock_tree` 所示, 对于各 IP，一般以 XTAL 作为最初的时钟源, 通过一个或多个 PLL 时钟进行倍频后，再各自经过分频电路处理后，作为 IP 或子系统之时钟输入。

.. _diagram_clock_tree:
.. figure:: ../../../../media/image8.png
	:align: center

	时钟源分频示意图

