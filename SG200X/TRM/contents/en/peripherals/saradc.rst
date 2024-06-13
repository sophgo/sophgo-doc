SARADC
------

Overview
~~~~~~~~

SARADC is an analog signal to digital conversion controller. This chip has up to 2 SARADC controllers, one in the Active Domain and another one in the No-die Domain, each providing 3 independent channels.

.. only:: sg2002

	**Note:** The chip does not bring out all ADC channels on the pins for the controller under Active Domain. For details, please refer to :ref:`table_inf_signal_pin_fmux_adc_sg2002`.

Features
~~~~~~~~

- Controller operating frequency 12.5MHz;

- The scanning frequency cannot be higher than 320K/s;

- Each controller provides 3 independent channels;

- 12bit sampling accuracy;

- Can trigger sequential scanning of three channels at one time;

- Automatically report interruption after scanning is completed;

Way of Working
~~~~~~~~~~~~~~

The CPU configures the scanning channel. Each SARADC controller can configure 3 channels at the same time and start SARADC for channel scanning. After the channel scan completes all enabled channels, the system is notified of the completion of the scan through an interrupt, and the CPU can obtain the conversion results.

After the system is powered on, in order to ensure the SARADC measurement accuracy, it is recommended to calibrate the SARADC module of the chip. The calibration is performed offline. The specific method is to first set saradc_test.reg_saradc_vrefsel to external mode, and then manually adjust saradc_trim.reg_saradc_trim repeatedly until the actual read sampling value is close to the external reference voltage value after conversion to meet the accuracy requirements. After the calibration is completed, record the value of saradc_trim.reg_saradc_trim. Then each time the power is turned on, through software programming, set saradc_test.reg_saradc_vrefsel to external mode and then set the recorded value to saradc_trim.reg_saradc_trim.

.. _section_saradc_register_overview:

SARADC Register Overview
~~~~~~~~~~~~~~~~~~~~~~~~

1 group in Active Domain, Base address: 0x030F0000

1 group in No-die Domain (RTCSYS_SARADC), Base address: 0x0502C000

Each set of registers has the same definition, taking RTCSYS_SARADC as an example:

.. The table is smaller and no longer includes the file

.. _table_rtcsys_saradc:
.. table:: Base address 0x0502C000
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| saradc_ctrl          | 0x004   | control register                   |
	+----------------------+---------+------------------------------------+
	| saradc_status        | 0x008   | status register                    |
	+----------------------+---------+------------------------------------+
	| saradc_cyc_set       | 0x00c   | saradc waveform setting register   |
	+----------------------+---------+------------------------------------+
	| saradc_ch1_result    | 0x014   | channel 1 result register          |
	+----------------------+---------+------------------------------------+
	| saradc_ch2_result    | 0x018   | channel 2 result register          |
	+----------------------+---------+------------------------------------+
	| saradc_ch3_result    | 0x01c   | channel 3 result register          |
	+----------------------+---------+------------------------------------+
	| saradc_intr_en       | 0x020   | interrupt enable register          |
	+----------------------+---------+------------------------------------+
	| saradc_intr_clr      | 0x024   | interrupt clear register           |
	+----------------------+---------+------------------------------------+
	| saradc_intr_sta      | 0x028   | interrupt status register          |
	+----------------------+---------+------------------------------------+
	| saradc_intr_raw      | 0x02c   | interrupt raw status register      |
	+----------------------+---------+------------------------------------+
	| saradc_test          | 0x030   | test register                      |
	+----------------------+---------+------------------------------------+
	| saradc_trim          | 0x034   | trim register                      |
	+----------------------+---------+------------------------------------+


SARADC Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/peripherals/saradc_registers_description.table.rst
