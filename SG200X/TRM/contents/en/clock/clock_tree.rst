Clock resources and frequency division structure
------------------------------------------------

The clock of the entire system is mainly divided into two parts: PLL clocks and IP/Subsystem clocks.

The system clock source mainly comes from external XTAL. XTAL has its frequency multiplied by a PLL. As shown in :ref:`diagram_clock_tree`, for each IP, XTAL is generally used as the initial clock source. After being multiplied by one or more PLL clocks, each is processed by a frequency division circuit and then used as clcok input for an IP or subsystem.

.. _diagram_clock_tree:
.. figure:: ../../../../media/image8.png
	:align: center

	Clock source frequency division diagram

