AIAO
----

Overview
~~~~~~~~

The audio input/output interface (Audio Input/Audio Output) is used to interface with the chip's built-in Audio Codec or the chip's external Audio Codec and digital microphone to complete the sending and receiving of audio data and realize functions such as recording, playback, and intercom. The chip integrates AIAO related modules into a subsystem, and the built-in Audio Codec ADC/DAC supports stereo input and output. It supports two sets of I2S interfaces externally, and integrates 4 sets of I2S TX/RX modules internally, which can receive and send audio data at the same time, and can support the simultaneous sending and receiving of multi-channel data. The basic module block diagram is shown below:

.. _diagram_aiao_block:
.. figure:: ../../../../media/image83.png
	:align: center

	AIAO block diagram

Features
~~~~~~~~

The AIAO interface supports Master-mode, Slave-mode I2S and PCM modes, and supports multi-channel TDM mode. Receive and send audio data to access the DDR space through DMA. The specific features are as follows:

- Highly flexible and configurable timing parameters, frame period, frame synchronization signal duration and polarity are all configurable

- Configurable clock edges for signal generation and sampling

- Supports master mode and slave mode stereo I2S mode audio data sending and receiving

- Supports transmission and reception of audio data in master mode and slave mode mono and stereo PCM mode

- Supports sending and receiving of multi-channel TDM mode audio data in master mode and slave mode

- Receive and send can be enabled individually or simultaneously

- Data adopts DMA operation and can be accessed circularly through the buffer developed by the software.

PCM Interface
^^^^^^^^^^^^^

- Supports 16-bit linear PCM encoding for sending and receiving

- The PCM interface frame synchronization signal supports short pulses (1 clock cycle) and long pulses (the number of clock cycles is configurable)

- Interface timing supports standard mode and left-aligned mode

I2S Interface
^^^^^^^^^^^^^

- Supports 16/24-bit data sending and receiving

- Supports 8kHz ~ 192kHz sampling rate

- The I2S interface frame synchronization signal can support low-level left channel or high-level left channel

- Interface timing supports standard mode and left-aligned mode

Function Description
~~~~~~~~~~~~~~~~~~~~

The AIAO subsystem connects the built-in Audio codec, I2S pins and TX/RX modules through the internal PINMUX, and configures the registers appropriately according to the application requirements through software to achieve different connection methods.

Typical Application
^^^^^^^^^^^^^^^^^^^

Typical applications are as follows:

- Supports I2S slave mode to connect to the built-in Audio Codec ADC, or I2S/PCM/TDM master/slave mode to connect to an external ADC for audio collection.

- Supports I2S master mode to connect to the built-in Audio Codec DAC, or I2S/PCM/TDM master/slave mode to connect to an external DAC for audio playback.

.. _diagram_i2s_internal_audio_codec_interconnect:
.. figure:: ../../../../media/image84.png
	:align: center

	Schematic diagram of connection with built-in Audio Codec through I2S interface

.. _diagram_i2s_external_audio_codec_interconnect_master:
.. figure:: ../../../../media/image85.png
	:align: center

	Schematic diagram of connecting AIAO to an external Audio Codec through the I2S interface in master mode

.. _diagram_i2s_external_audio_codec_interconnect_slave:
.. figure:: ../../../../media/image86.png
	:align: center

	Schematic diagram of connecting AIAO to an external Audio Codec through the I2S interface in slave mode

Functional Principle
^^^^^^^^^^^^^^^^^^^^

The audio source is Analog-to-Digital converted into audio data through the built-in or external Audio Codec ADC, which is received by the connected RX module through the I2S or PCM interface, and stored in the circular buffer via DMA, and then taken out by the CPU for storage, thus Complete the recording function. The TX module reads audio data from the circular buffer through DMA, and transmits the audio data to the connected built-in or external Audio through the I2S or PCM interface.
Codec DAC, performs Digital-to-Analog conversion for audio source playback.

When connecting to an external I2S interface, the supported I2S timing is as shown in the diagram :ref:`diagram_i2s_inf_timesequence`.

.. _diagram_i2s_inf_timesequence:
.. figure:: ../../../../media/image87.png
	:align: center

	I2S interface timing

Chart :ref:`diagram_i2s_inf_timesequence` takes the audio data width 24-bit as an example. The data is transmitted in MSB First mode. The MSB is delayed by one BCLK cycle relative to the LRCK signal. The data and LRCK signal are sent out using the falling edge of BCLK and sampled on the rising edge of BCLK. (tx_sample_edge = 0, rx_sample_edge = 1).

When connecting to the external PCM interface, it supports PCM standard timing and data left-aligned timing. The standard mode timing is as shown in the diagram :ref:`diagram_pcm_inf_standard_timesequence`, and the left-aligned mode timing is as shown in the diagram :ref:`diagram_pcm_inf_leftalign_timesequence`.

.. _diagram_pcm_inf_standard_timesequence:
.. figure:: ../../../../media/image88.png
	:align: center

	PCM interface standard mode timing

Chart :ref:`diagram_pcm_inf_standard_timesequence` takes the stereo audio data width of 16-bit as an example. The data is transmitted in MSB First mode. The MSB is delayed by one BCLK cycle relative to the LRCK signal. The data and LRCK signal are sent out using the falling edge of BCLK. On the rising edge of BCLK sample(tx_sample_edge = 0, rx_sample_edge = 1).

.. _diagram_pcm_inf_leftalign_timesequence:
.. figure:: ../../../../media/image89.png
	:align: center

	PCM Interface Left Justified Mode Timing

In left-justified mode, the data and LRCK signals are sent out at the beginning of the same beat.

Way of Working
~~~~~~~~~~~~~~

The Audio Codec integrated within AIAO and the external Audio Codec connected through the I2S interface can work simultaneously through software configuration. The connection method is as shown in the figure: :ref:`diagram_i2s_internal_audio_codec_interconnect`, :ref:`diagram_i2s_external_audio_codec_interconnect_master` and :ref:`diagram_i2s_external_audio_codec_interconnect_slave`. Before enabling data transmission according to application needs, the software must first configure the AIAO subsystem registers i2s_tdm_sclk_in_sel, i2s_tdm_fs_in_sel, i2s_tdm_sdi_in_sel, i2s_tdm_sdo_out_sel to connect each interface to the corresponding TX/RX module (I2S_TDM_0~I2S_TDM_3).

Clock Gating and Clock Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If AIAO operates in master mode, you must first set the TX/RX module register master_mode as the MCLK/BCLK clock source to 1, configure the frequency division register I2S_CLK_CTRL1 (mclk_div, bclk_div) depending on the sampling rate, and then set the register I2S_CLK_CTRL0 (aud_en) is 1, turns on clock gating.

Soft Reset
^^^^^^^^^^

The four TX/RX modules integrated by AIAO all have independent soft resets. Before enabling the TX/RX modules for data transmission, the registers FIFO_RESET and I2S_RESET must be configured for soft reset.

AIAO Register Overview
~~~~~~~~~~~~~~~~~~~~~~

An overview of AIAO subsystem registers is shown in table :ref:`table_aiao_registers_overview`.

.. include:: ../../contents-share/audio/aiao_registers_overview.table.rst

The I2S_TDM_0 ~ I2S_TDM_3 module register overview is shown in the table :ref:`table_i2s_tdb_registers_overview`.

.. include:: ../../contents-share/audio/i2s_tdb_registers_overview.table.rst

AIAO Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~

AIAO Subsystem Register Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../contents-share/audio/aiao_subsystem_registers_description.table.rst

I2S_TDM Module Register Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../contents-share/audio/i2s_tdm_module_registers_description.table.rst
