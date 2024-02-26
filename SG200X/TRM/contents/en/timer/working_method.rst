Way of Working 
--------------

Initialization
~~~~~~~~~~~~~~

- Step 1: Write the TimerNLoadCount (N=1~8) register to load the initial count value for the Timer.

- Step 2: Set the TimerNControlReg[2:0] (N=1~8) register, select the Timer counting mode, mask the Timer interrupt, and start the Timer to start counting.

Interrupt Handling
~~~~~~~~~~~~~~~~~~

When the timer generates an interrupt, the steps are as follows:

- Step 1: Read the TimerNEOI (N=1~8) register to clear the TimerN interrupt.

- Step 2: Execute the process waiting for the interrupt.

- Step 3: After the process is completed, resume execution of the interrupted program.

Clock Selection
~~~~~~~~~~~~~~~

System Timer optional 25MHz/32KHz counting clock. Use reg_timer_clk_sel to make the selection.
