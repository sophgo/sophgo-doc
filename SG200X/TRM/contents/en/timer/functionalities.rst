Function Description
--------------------

Timer is based on a 32-bit down counter. The counter value is decremented by 1 on each rising edge of the count clock. When the count value decreases to zero, the Timer will generate an interrupt.

Timer has the following 2 counting modes:

- Free running mode: The timer continues to count, and when the count value decreases to 0, it automatically returns to its maximum value and continues counting. The maximum count length is 0xFFFF_FFFF.

- User-defined counting mode: The timer continues to count. When the count value decreases to 0, the initial value is loaded again from the TimerNLoadCount (N=1~8) register and continues counting.

The method of loading the initial count value of the timer is as follows:

The initial count value of the timer can be loaded by writing the TimerNLoadCount (N=1~8) register.