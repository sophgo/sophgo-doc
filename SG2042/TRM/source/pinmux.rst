Pin mux
=======

SG2042 pins consist of digital pins, analog pins and power supply pins

Digital pins
------------

Pin list
~~~~~~~~

Digital pins Digital pins are listed in table :ref:`digital_pin_list`

.. _digital_pin_list:
.. include:: digit-pin-list.rst
    
Pin function
~~~~~~~~~~~~

Most digital pins have multiple functions. Each digital pin can have at most four
functions. Pins and functions are listed in table :ref:`digital_pin_function`

.. _digital_pin_function:
.. include:: digital-pin-function.rst
    
Registers
~~~~~~~~~

Pinmux module controls attributes of pins. These attributes including function,
pull up, pull down or no pull, if schmitt trigger is enabled and driving strength.

The base address is listed in table :ref:`mmap_table`, PINMUX device.

.. include:: pinmux-reg.rst
