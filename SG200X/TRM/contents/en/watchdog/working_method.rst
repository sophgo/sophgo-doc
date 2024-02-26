Way of Working
--------------

Count Clock Frequency Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WatchDog counting clock is 25MHz/32KHz clock. Use reg_wdt_clk_sel to make the selection.

System Initialization Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the system is powered on and reset, the WatchDog counter stops counting. During the system initialization process, WatchDog needs to be initialized and started to run. The initialization process of WatchDog is as follows:

- Step 1: Write register WDT_TORR to set the initial value of WatchDog count.

- Step 2: Write register WDT_CR[1] to set WatchDog count timeout response mode.

- Step 3: Write register WDT_CR[0] to start WatchDog counting.

Interrupt Handling Process
~~~~~~~~~~~~~~~~~~~~~~~~~~

After the system receives an interrupt from WatchDog, it should clear its interrupt status in time.

The process of WatchDog interrupt processing is as follows:

- Step 1: Read the register WDT_EOI and clear the interrupt status of WatchDog.

- Step 2: Write 0x76 to the register WDT_CRR and restart WatchDog.

Close WatchDog
~~~~~~~~~~~~~~

Write 0 or 1 to register WDT_CR[0] to control the status of WatchDog:

- 0: WDT is off.

- 1: WDT is on. Only a system reset can turn off the WDT after startup.
