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

WatchDog runs based on a 32-bit down counter. Its initial count value has two sources, loaded from WDT_ITORR and WDT_TORR respectively, and calculated based on the value of ITOR_MODE (for specific calculation methods, refer to the description in :ref:`table_wdt_torr`). WDT_ITORR is used for the first timer count of WatchDog after power-on, and subsequent timer counts are based on WDT_TORR.

When the WatchDog clock is enabled, the count value is decremented by 1 on the rising edge of each count clock. When the count value decreases to 0, WatchDog will generate an interrupt. Then at the next rising edge of the counting clock, the counter reloads the initial counting value from the register WDT_TORR and starts counting down.

The user can set the register WDT_CR[1] to decide whether to send a reset signal WDT_SYS_RST immediately when the counter count value decreases to 0 for the first time. If it is set to 0, a reset signal is sent immediately. Otherwise, if it is 1, an interrupt is generated and the second count starts. If the CPU has not cleared the WatchDog interrupt when the second count decreases to 0, WatchDog will send a reset signal WDT_SYS_RST and the counter will stop counting.
