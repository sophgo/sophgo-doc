Overview
--------

Power Domain
~~~~~~~~~~~~

The chip supports two main power domains.

- Active Domain

- No-die Domain

Active Domain
^^^^^^^^^^^^^

That is the ordinary SoC power supply method.

No-die Domain
^^^^^^^^^^^^^

VDDIO_RTC power supply (VDDIO_SD1 as appropriate) is required for this Domain.

Inside the SoC, this power domain is implemented by a subsystem called RTCSYS.

.. _diagram_8051_block:
.. figure:: ../../../../media/image15.png
	:align: center

	RTCSYS subsystem architecture

The RTCSYS subsystem is internally divided into two sub power domains: AO (Always-On) domain and MCU domain (VDDC_SW_MCU area). The system can choose to turn off the power domain to which the MCU belongs through registers to achieve power saving needs. Please refer to the :ref:`section_8051_power_domain_control` chapter for details.

In the system sleep state, the MCU can handle interrupts and wake up the system through the configuration register, and can also communicate with external devices through I2C/UART.

The specific composition of the RTCSYS subsystem is as follows:

- AO (Always-On) domain

  - 1 set of WDT is used to issue an interrupt or reset signal after a certain period of time when an abnormality occurs in the system to interrupt or reset the entire system. Related control registers refer to the RTCSYS_WDT section of the :ref:`section_wdt_register_overview` chapter.

  - RTC (Real Time Clock), for detailed introduction, please refer to the :ref:`section_rtc` chapter.

   - 1 set of interrupt controllers to manage interrupt sources (ictrl). For detailed introduction, please refer to the :ref:`section_8051_interrupt` chapter.

   - 1 set of GPIO, related control registers refer to the RTCSYS_GPIO section of the :ref:`section_gpio_register_overview` chapter.

   - 1 set of SARADC, related control registers refer to the RTCSYS_SARADC section of the :ref:`section_saradc_register_overview` chapter.

   - 1 group of IRRX, related control registers refer to the :ref:`section_irrx_register_overview` chapter.

- MCU domain

  - An 8051 microcontroller (MCU), see chapter :ref:`section_8051` for details.

  - 8KB space AHB SRAM, which can be used by 8051 as instruction TCM or temporary data storage.

  - 2 sets of 32-bit counters, used for timing and counting functions, which can be used for application programs to implement timing and counting, or for the operating system to implement system clocks.

  - 1 group off-chip SPINOR control.

  - 2 sets of Mailbox, allowing ACPU and 8051 to communicate with each other. For detailed introduction, please refer to the :ref:`section_8051_mailbox` chapter.

  - 1 set of I2C, related control registers refer to the RTCSYS_I2C section of the :ref:`section_i2c_register_overview` chapter.

  - 1 set of UART, related control registers refer to the RTCSYS_UART section of the :ref:`section_uart_register_overview` chapter.

Power operating mode
~~~~~~~~~~~~~~~~~~~~

Based on Power Domain, the chip supports two main power operating modes:

- MCU-Only (32k-less) Mode:

  Only No-die Domain works. In this No-die domain, there is a small MCU system with its own clock, timer, uart, i2c, gpio, adc and other peripherals, which can replace the SoC's external MCU. The MCU in the No-die Domain can wake up the main system and return to Active Mode after receiving and filtering external input.

  There is a calibrated oscillator in the system to wake up quickly and fall asleep quickly. To further save power consumption every time it is woken up.

  When the MCU is in the Idle state, the power consumption is approximately 200uA.

- Active Mode

  Active mode is a state where the chip is fully awake and working. At this time, as long as the power supply is normal, the devices in the No-die Domain and Active Domain will work normally. But there are other power-saving techniques such as dynamic frequency scaling or dynamic clock gating.
