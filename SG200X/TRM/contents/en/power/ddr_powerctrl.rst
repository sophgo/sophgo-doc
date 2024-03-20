DDR low power control
---------------------

After the bus is not accessed for a period of time, the DDR controller will automatically enter the "Self refresh" and "Power down" states to reduce system power consumption.

In some scenarios, it is impossible to find a large enough gap to enter "self refresh" due to intermittent access. At this time, you can also consider using the built-in statistical register to access the data volume. To confirm whether the bandwidth is excessive, you can consider directly reducing the frequency.

The DDR controller supports dynamic frequency adjustment. However, adjusting the frequency will temporarily stop DDR access for a period of time. Therefore, in order to reduce interruption time, which may make real-time application buffer underflow or overflow, it is limited to two levels: 50% and 100%.
