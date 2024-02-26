MIPI Tx
-------

Overview
~~~~~~~~

The Display Serial Interface (DSI) interface is a high-speed serial interface defined by the Mobile Industry Processor Interface alliance (MIPI Alliance) and is mainly used for the connection between the processor and the display module. The MIPI Tx interface implements the DSI interface and supports MIPI D-PHY V1.0 serial signal output.

MIPI Tx consists of two parts: analog PHY and digital Controller. The system architecture and functional block diagram are shown in the figure.

.. _diagram_mipi_tx_function_block:
.. figure:: ../../../../media/image76.png
	:align: center

	MIPI TX functional block diagram

Features
~~~~~~~~

MIPI Tx has the following features:

- Supports 1/2/4 Data Lane MIPI D-PHY interface, sequential, PN extremely configurable.

- High-speed mode supports up to 2500Mbps/Lane.

- Only Data Lane0 supports low-speed sending and receiving, BTA (Bus Turn-Around) function, and the speed in low-speed mode is up to 10Mbps.

- Support DSI RGB16/18/24/30 bit data type output.

- Supports DSI video mode and command mode, video mode supports Burst mode, Non-burst mode with Sync Events and Non-burst mode with Sync pulses.

Function Description
~~~~~~~~~~~~~~~~~~~~

MIPI Tx includes Tx D-PHY and Tx Controller

- Tx D-PHY supports MIPI D-PHY ver2.1 protocol, which mainly implements the transmission specification of the physical layer.

- The Tx Controller encapsulates the data format according to the MIPI DSI protocol.

Tx D-PHY
^^^^^^^^

Tx D-PHY has two working modes, High Speed (HS) and Low Power (LP):

- Video mode data is transmitted through high-speed mode.

- Command mode data is transmitted through low-speed mode.

The data rate range of each lane (Lane) in high-speed mode is 80~2500Mbps, and the maximum rate in low-speed mode is 10Mbps.

High-speed mode supports up to 4 data lanes. The actual number of data lanes used can be 1/2/4, and the order and polarity are configurable. Low-speed mode transmission, reception and Bus Turn-Around (BTA) are only supported by configured data lane0.

Tx Controller
^^^^^^^^^^^^^

Sending of Data Packets
^^^^^^^^^^^^^^^^^^^^^^^

When there are multiple high-speed packets to be transmitted, the Tx D-PHY will automatically switch between HS and LP modes according to the high-speed data transmission requirements sent by the Tx Controller. Tx Controller supports whether to send EoT packet (End of Transmission, EoT) at the end of HS transmission.

Type of Data
^^^^^^^^^^^^

The controller supports the transmission of DSI RGB16/18/24/30 bit. The composition format of various data types is as shown in the figure.

.. _diagram_rgb16_format:
.. figure:: ../../../../media/image77.png
	:align: center

	RGB 16-bit format (Data type = 0x0E)

.. _diagram_rgb18_format:
.. figure:: ../../../../media/image78.png
	:align: center

	RGB 18-bit format (Data type = 0x1E)

Note: RGB 18-bit only supports data type = 0x0E, does not support loosely Packet mode (data type = 0x2E)

.. _diagram_rgb24_format:
.. figure:: ../../../../media/image79.png
	:align: center

	RGB 24-bit format (Data type = 0x3E)

.. _diagram_rgb30_format:
.. figure:: ../../../../media/image80.png
	:align: center

	RGB 30-bit format (Data type = 0x0D)

Interface Timing
^^^^^^^^^^^^^^^^

The timing marks are as follows

.. _diagram_mipi_tx_timesequence:
.. figure:: ../../../../media/image81.png
	:align: center

	MIPI TX Timing marks

- VSA: Number of frame synchronization steps

- VBP: Number of blanking lines after frame

- VACT: frame valid data line

- VFP: blanking line before frame

- VSS: frame synchronization signal

- HSS: Horizontal Synchronization Signal

- HBP: Post-line blanking area

- RGB: row of valid data

- HFP: Pre-travel blanking zone

- BLLP: Blanking or Low-Power Interval

Video vertical timing is:

Frame synchronization signal (VSS), blanking area after frame (VBP), valid line area (VACT), blanking area before frame (VFP), frame synchronization signal.

The horizontal timing is:

Horizontal sync signal (HSS), line blanking area after (HBP), active pixel (HACT), line blanking area before (HFP), horizontal synchronization signal.

The effective synchronization signal is VSS, HSS, and the effective pixel is the intersection of the effective row area (VACT) and the effective pixel (HACT).

Video mode Burst Transmission timing is as follows:

.. _diagram_mipi_tx_video_mode_burst_transmission_timesequence:
.. figure:: ../../../../media/image82.png
	:align: center

	MIPI TX Video mode Burst Transmission timing

MIPI Tx only transmits valid synchronization signals and data, and enters the BLLP area the rest of the time to reduce power consumption.

MIPI Tx Register Overview
~~~~~~~~~~~~~~~~~~~~~~~~~

MIPI Tx Control register location is 0x0A08A000.

.. include:: ../../contents-share/video/mipi_tx_control_registers_overview.table.rst

MIPI Tx Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/video/mipi_tx_control_registers_description.table.rst

MIPI Tx PHY Register Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MIPI Tx PHY register location is 0x0A0D_1000.

.. include:: ../../contents-share/video/mipi_tx_phy_registers_overview.table.rst

MIPI Tx PHY Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/video/mipi_tx_phy_registers_description.table.rst
