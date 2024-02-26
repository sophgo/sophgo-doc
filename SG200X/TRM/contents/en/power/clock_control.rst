Clock Control
-------------

Turn off unnecessary clock dividers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to the :ref:`section_clock` configuration chapter and turn off the unused clock divider according to the clock source required by each module, to achieve the purpose of saving power consumption.

Adjust the operating frequency of the module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select a lower clock source according to the clock specifications required by each module. There are many frequency division configurations to reduce the module operating frequency. It should be noted that reducing the frequency of a single module may not necessarily reduce the overall power consumption.

Module-level low-power control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Analog module: MIPI/USB/ETH/AUD related register settings, turn off unused modules or enter low power consumption mode.

- Digital modules: Turn off the clocks of unnecessary digital modules according to hardware and specifications.

Shut down unused PLLs
~~~~~~~~~~~~~~~~~~~~~

Referring to the PLL configuration, you can Powerdown the PLL that is not needed to save power consumption.
