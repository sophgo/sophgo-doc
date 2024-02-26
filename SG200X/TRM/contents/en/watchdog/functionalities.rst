Function Description
--------------------

The system configures register parameter values for WatchDog through the system bus. WatchDog periodically sends WDT_INTR interrupt requests to the system, and when the system does not respond to the interrupt (such as crashes), it sends a WDT_SYS_RST reset signal to reset the system to achieve the purpose of monitoring system operation.

Application Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _diagram_watchdog_block:
.. figure:: ../../../../media/image13.png

	WatchDog Application Block Diagram

Functional Principle
~~~~~~~~~~~~~~~~~~~~

The initial counting value of WatchDog is loaded from the register WDT_TORR, and the operation is based on a 32-bit subtraction counter.

When the WatchDog clock is enabled, the count value is decremented by 1 on the rising edge of each count clock. When the count value decreases to 0, WatchDog will generate an interrupt. Then at the next rising edge of the counting clock, the counter reloads the initial counting value from the register WDT_TORR and starts counting down.

If the count value of the counter decreases to 0 for the second time and the CPU has not cleared the WatchDog interrupt, WatchDog will issue a reset signal WDT_SYS_RST and the counter will stop counting.

The user can decide whether to send the reset signal WDT_SYS_RST immediately when the counter's count value decreases to 0 for the first time by setting the register WDT_CR[1].
