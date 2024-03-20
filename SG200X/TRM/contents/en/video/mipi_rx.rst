MIPI Rx
-------

Overview
~~~~~~~~

The main function of the MIPI Rx (Mobile Industry Processor Interface Receiver) module is to receive video data transmitted by the CMOS sensor. It supports MIPI D-PHY, sub-LVDS (Low-Voltage Differential Signal), HiSPi (High-Speed Serial Pixel Interface), etc. Different serial video signal inputs are processed and converted into internal video timing, which is passed to the next-level video processing module (ISP).

The MIPI Rx module can be subdivided into two parts: PHY and Controller. The PHY module integrates analog and digital parts and mainly converts serial signals into parallel signals. The Controller module is responsible for decoding different video data formats and transmitting them to Back-end video processing module (ISP). The functional block diagram and its location in the system are shown in the diagram :ref:`diagram_mipi_rx_block`.

.. _diagram_mipi_rx_block:
.. figure:: ../../../../media/image44.png
	:align: center

	MIPI Rx functional block diagram and location in the system

Features
~~~~~~~~

- Support MIPI DPHY-ver2.1

- Can support 2 sensor inputs at the same time

- A single sensor supports up to 5M (2688x1944, 2880x1620) @30fps HDR or @60fps linear input

- Dual-channel sensor supports maximum FHD(1920x1080) @60fps HDR or linear input

- A single channel supports up to 4-Lane MIPI D-PHY interface and a maximum of 1.5Gbps/Lane

- A single channel supports up to 4-Lane sub-LVDS/HiSPi interfaces and a maximum of 1.5Gbps/Lane

- Supports parsing of RAW8/RAW10/RAW12/RAW16 data types

- Supports YUV422 8-bit / YUV422 10-bit data type parsing

- Supports up to 2 frames of WDR and supports multiple WDR timings

- Supports sub-LVDS/HiSPi mode pixel/sync code big and small endian configuration

- Supports configurable Lane number and Lane order

Function Description
~~~~~~~~~~~~~~~~~~~~

Typical Application
^^^^^^^^^^^^^^^^^^^

In applications using image sensors, the MIPI Rx module register can be set according to different interface selections (MIPI/Sub-LVDS/HiSPi). At the same time, MIPI Rx also supports transmission requirements of different speeds and different resolutions, and is compatible with a variety of images. Sensor format.

The MIPI Rx module contains 1 group of D-PHY, each group has six differential pairs. One D-PHY can support a pair of differential clocks and up to four pairs of data differential signals, or support two groups of one pair of differential clocks at the same time. The upper two pairs of data differential signals, so MIPI Rx can support 2 Sensor inputs at the same time. In addition, MIPI Rx can support different differential pair sequencing and clock differential pair positions. The source of the clock and the differential pair sequencing method can be configured through registers.

MIPI Rx only targets the timing conversion and decoding of the interface, and does not handle the image processing part. Therefore, any resolution and frame rate can be supported under the premise of meeting the bandwidth. The bandwidth of MIPI Rx is limited by two parts: the PHY's interface data rate and the internal processing speed. The input interface supports a maximum of 1.5Gbps/Lane, and the internal processing speed is a maximum of 600M*1pixels/s.

.. This table is relatively small, so I won’t include it in the file separately.

.. _table_mipi_rx_inf_type:
.. table:: MIPI Rx Interface Type
	:widths: 1 1 1 1 1

	+-----------+--------------+-------------+-------------+-------------+
	|           | Common mode  | D\          | Maximum     | Maximum     |
	|           | voltage      | ifferential | clock       | data rate   |
	|           |              | mode        | frequency   | per lane    |
	|           |              | voltage     |             |             |
	+===========+==============+=============+=============+=============+
	| MIPI DPHY | 200mV        | 200mV       | 750MHz      | 1.5Gbps     |
	+-----------+--------------+-------------+-------------+-------------+
	| Sub-LVDS  | 900mV        | 150mV       | 750MHz      | 1.5Gbps     |
	+-----------+--------------+-------------+-------------+-------------+
	| HiS       | 900mV        | 280mV       | 750MHz      | 1.5Gbps     |
	| Pi(HiVCM) |              |             |             |             |
	+-----------+--------------+-------------+-------------+-------------+
	| HiS       | 200mV        | 200mV       | 750MHz      | 1.5Gbps     |
	| Pi(SLVDS) |              |             |             |             |
	+-----------+--------------+-------------+-------------+-------------+

MIPI Interface Data Format
^^^^^^^^^^^^^^^^^^^^^^^^^^

MIPI specifications are developed and maintained by different working groups, corresponding to applications in different fields. MIPI Rx supports D-PHY and CSI-2 (Camera Serial Interface). D-PHY specifies the transmission specification of the physical layer, and CSI-2 specifies the format and protocol of the Camera output data packet.

- D-PHY

  D-PHY is a high-speed physical layer standard released by the MIPI Alliance, which specifies the physical characteristics and transmission protocols of the interface layer. D-PHY uses 200mV source-synchronous low-voltage differential signaling technology, and the data green rate range of each Lane supports up to 2500Mbps. D-PHY can operate in two modes: Low Power (LP) and High Speed (HS).

- CSI-2

  CSI-2 is a data protocol for cameras, which specifies the data packet format for communication between the host and peripherals.

  CSI-2 can support image applications with different pixel formats, and the minimum granularity of data transmission is bytes. To increase the performance of CSI-2, you can choose the number of data Lanes. The CSI-2 protocol specifies the mechanism for the sender to pack pixel data into bytes, and specifies how multiple data Lanes are allocated and managed. Bytes of data are organized in packets, which are transmitted between SoT and EoT. The receiving end parses the corresponding data packet according to the protocol and recovers the original pixel data.

  MIPI Rx supports parsing of RAW8/RAW10/RAW12/RAW16/YUV422-8bit/YUV422-10bit data types.

  CSI-2 data packets are divided into long packets and short packets, which contain check codes and can perform error correction and error detection.

Both long packets and short packets are transmitted between SoT and EoT. During the gap between data transmission, D-PHY is in LP mode.

The transmission mechanism of CSI-2 packets is shown in the figure. PH and PF stand for Packet Header and Packet Footer respectively.

.. _diagram_csi2_datapacket_transfer:
.. figure:: ../../../../media/image45.png
	:align: center

	Data packet transmission mechanism

Long packets are used to transmit valid pixel data and are divided into five parts: Data ID, Word Count, ECC, PAYLOAD, CHECKSUM.

- Data ID contains Virtual Channel and Data Type. Virtual Channel controls the channel used for transmission and can use different channels to transmit different data. Data Type specifies the type of data to be transmitted.

- Word Count indicates the amount of data that the receiving end needs to receive.

- ECC is an error correction code that can correct or detect errors in Data Type and Word Count.

- PAYLOAD is the actual pixel data that needs to be transmitted.

- CHECKSUM is a checksum generated by a linear feedback shift register and is used to verify PAYLOAD data.

The structure of the long package is shown in the diagram :ref:`diagram_csi2_long_package_format`.

.. _diagram_csi2_long_package_format:
.. figure:: ../../../../media/image46.png
	:align: center

	CSI-2 long packet format

The function of the short packet is to transmit information synchronously, including three parts: Data ID, Data Field and ECC. Its format is shown in the diagram :ref:`diagram_csi2_short_package_format`.

.. _diagram_csi2_short_package_format:
.. figure:: ../../../../media/image47.png
	:align: center

	CSI-2 short packet format

MIPI Rx supports the transmission of six video data formats, including YUV422-8bit, YUV422-10bit, RAW8, RAW10, RAW12 and RAW16. The transmission methods of different data formats are described below.

The transmission mode of YUV422-8bit is in the form of UYVY, as shown in the diagram :ref:`diagram_yuv422_8bit_transfer_sequence`.

.. _diagram_yuv422_8bit_transfer_sequence:
.. figure:: ../../../../media/image48.png
	:align: center

	YUV422 8-bit data transfer sequence

The correspondence between the packet and the video signal is shown in the diagram :ref:`diagram_yuv422_8bit_transfer_map`.

.. _diagram_yuv422_8bit_transfer_map:
.. figure:: ../../../../media/image49.png
	:align: center

	YUV422-8bit data packet transmission mapping

The transmission format of the entire Frame will be as shown in the diagram :ref:`diagram_yuv422_8bit_frame_format`.

.. _diagram_yuv422_8bit_frame_format:
.. figure:: ../../../../media/image50.png
	:align: center

	YUV422 8-bit frame format

The transmission mode of YUV422-10bit is also UYVY, and the transmission sequence is shown in the chart :ref:`diagram_yuv422_10bit_transfer_sequence`.

.. _diagram_yuv422_10bit_transfer_sequence:
.. figure:: ../../../../media/image51.png
	:align: center

	YUV422-10bit data transfer sequence

The correspondence between the packet and the video signal is shown in the diagram :ref:`diagram_yuv422_10bit_transfer_map`.

.. _diagram_yuv422_10bit_transfer_map:
.. figure:: ../../../../media/image52.png
	:align: center

	YUV422-10bit data packet transmission mapping

The transmission format of the entire Frame will be as shown in the diagram :ref:`diagram_yuv422_10bit_frame_format`.

.. _diagram_yuv422_10bit_frame_format:
.. figure:: ../../../../media/image53.png
	:align: center

	YUV422-10bit frame format

The transfer sequence of RAW8 is shown in the diagram :ref:`diagram_raw8_transfer_sequence`.

.. _diagram_raw8_transfer_sequence:
.. figure:: ../../../../media/image54.png
	:align: center

	RAW8 data transfer sequence

The transmission format of the entire Frame will be as shown in the diagram :ref:`diagram_raw8_frame_format`.

.. _diagram_raw8_frame_format:
.. figure:: ../../../../media/image55.png
	:align: center

	RAW8 frame format

The transfer sequence of RAW10 is shown in the diagram :ref:`diagram_raw10_transfer_sequence`.

.. _diagram_raw10_transfer_sequence:
.. figure:: ../../../../media/image56.png
	:align: center

	RAW10 data transfer sequence

The transmission format of the entire Frame will be as shown in the diagram :ref:`diagram_raw10_frame_format`.

.. _diagram_raw10_frame_format:
.. figure:: ../../../../media/image57.png
	:align: center

	RAW10 frame format

The transfer sequence of RAW12 is shown in the diagram :ref:`diagram_raw12_transfer_sequence`.

.. _diagram_raw12_transfer_sequence:
.. figure:: ../../../../media/image58.png
	:align: center

	RAW12 data transfer sequence

The transmission format of the entire Frame will be as shown in the diagram :ref:`diagram_raw12_frame_format`.

.. _diagram_raw12_frame_format:
.. figure:: ../../../../media/image59.png
	:align: center

	RAW12 frame format

The transfer sequence of RAW16 is shown in the diagram :ref:`diagram_raw16_transfer_sequence`.

.. _diagram_raw16_transfer_sequence:
.. figure:: ../../../../media/image60.png
	:align: center

	RAW16 data transfer sequence

The transmission format of the entire Frame will be as shown in the diagram :ref:`diagram_raw16_frame_format`.

.. _diagram_raw16_frame_format:
.. figure:: ../../../../media/image61.png
	:align: center

	RAW16 frame format

MIPI Interface Linear Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^

The linear mode transmission format of the MIPI interface is shown in the diagram :ref:`diagram_mipi_inf_graphic_format`. The transmission of each picture starts with the short packet Frame Start (FS) and ends with the short packet Frame End (FE). The video content in the middle is in line units, and each long packet transmits a complete video line. The long packet format is as specified by the MIPI standard. Each line has a 32-bit data packet header (PH, Pecket Header), which contains information such as the Virtual Channel and Data Type of the current line.

.. _diagram_mipi_inf_graphic_format:
.. figure:: ../../../../media/image62.png
	:align: center

	MIPI interface image format

MIPI interface wide dynamic mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MIPI Rx supports four wide dynamic range (WDR) modes of the MIPI interface, namely:

1. Use DT (Data Type) to distinguish long and short exposure data

2. Use the identification code (Identification Code) to distinguish long and short exposure data

3. Use registers to set long and short exposure data delay intervals

The WDR transmission method using DT is shown in the chart :ref:`diagram_mipi_inf_wide_dynamic_data_transfer_dt`. Different exposure lengths share a set of FS/FE short packets, and the header of the long packet contains DT information. Different DTs can be used to distinguish long and short exposure data. , the real data format DT and the two sets of DT representing long and short exposure data can be set using registers, and MIPI Rx can parse out the correct wide dynamic timing and send it to the rear video processing module.

.. _diagram_mipi_inf_wide_dynamic_data_transfer_dt:
.. figure:: ../../../../media/image63.png
	:align: center

	MIPI interface wide dynamic data transmission (using DT)

The WDR transmission method using ID is shown in the chart :ref:`diagram_mipi_inf_wide_dynamic_data_transfer_id`. Different exposure lengths share a set of FS/FE short packets, and the first four pixels of each long packet in the transmission data are used to transmit the data representing different exposure lengths. ID (Identification Code), the ID representing long and short exposures can be set using registers. MIPI Rx will use the ID to distinguish different exposure video signals, and remove the first four pixels before sending them to the video processing module.

.. _diagram_mipi_inf_wide_dynamic_data_transfer_id:
.. figure:: ../../../../media/image64.png
	:align: center

	MIPI interface wide dynamic data transmission (using ID)

The last supported WDR transmission method does not have any DT or ID to indicate whether the transmitted long packet contains long exposure or short exposure content. The user must set the register to indicate the number of exposure lines between long exposure and short exposure. Difference, MIPI Rx will parse the corresponding timing to the video processing module. The actual transmission timing is shown in the chart :ref:`diagram_mipi_inf_wide_dynamic_data_transfer_reg`.

.. _diagram_mipi_inf_wide_dynamic_data_transfer_reg:
.. figure:: ../../../../media/image65.png
	:align: center

	MIPI interface wide dynamic data transmission (register setting)

Sub-LVDS interface data format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ultra-low voltage differential signal sub-LVDS (Low-Voltage Differential Signal) is commonly used in front-end cameras. It uses synchronization codes to distinguish the range of valid video signals and the long and short exposures of wide dynamic mode.

The PHY of MIPI Rx converts differential serial data into parallel data, and then the controller of MIPI Rx decodes the parallel data into pixel data according to different modes and synchronization codes.

MIPI Rx supports three bit width Sub-LVDS transmission modes of 8bit, 10bit and 12bit. The interface data format is shown in the chart :ref:`diagram_sub_lvds_inf_data_format`. All valid video signals will be in the middle of SAV and EAV synchronization codes, where synchronization Codes are composed of four fields, and the bit width of each field is the same as the following pixel bit width. The first three fields are fixed reference code words, and the fourth field can be used to distinguish the start or end of the valid interval. The Sub-LVDS synchronization code format is shown in the chart :ref:`table_sub_lvds_sync_code_example`. The synchronization code will use different values according to different manufacturers. The chart :ref:`table_sub_lvds_sync_code_example` is just one of the implementation methods. Different values can be in the register set up.

.. _diagram_sub_lvds_inf_data_format:
.. figure:: ../../../../media/image66.png
	:align: center

	Sub-LVDS interface data format

.. This table is relatively small, so I won’t put the file include separately.

.. _table_sub_lvds_sync_code_example:
.. table:: Sample of Sub-LVDS Sync Code
	:widths: 1 2 1 1 1 1

	+---------------------------------------------------------------------+
	| **12-bit**                                                          |
	+------------+---------------------+-------+--------+--------+--------+
	|            |                     | 1st   | 2nd    | 3rd    | 4th    |
	|            |                     | word  | word   | word   | word   |
	+------------+---------------------+-------+--------+--------+--------+
	| Blanking   | Start sync code     | FFFh  | 000h   | 000h   | AB0h   |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | B60h   |
	+------------+---------------------+       |        |        +--------+
	| Effective  | Start sync code     |       |        |        | 800h   |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | 9D0h   |
	+------------+---------------------+-------+--------+--------+--------+
	| **10-bit**                                                          |
	+------------+---------------------+-------+--------+--------+--------+
	|            |                     | 1st   | 2nd    | 3rd    | 4th    |
	|            |                     | word  | word   | word   | word   |
	+------------+---------------------+-------+--------+--------+--------+
	| Blanking   | Start sync code     | 3FFh  | 000h   | 000h   | 2ACh   |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | 2D8h   |
	+------------+---------------------+       |        |        +--------+
	| Effective  | Start sync code     |       |        |        | 200h   |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | 274h   |
	+------------+---------------------+-------+--------+--------+--------+
	| **8-bit**                                                           |
	+------------+---------------------+-------+--------+--------+--------+
	|            |                     | 1st   | 2nd    | 3rd    | 4th    |
	|            |                     | word  | word   | word   | word   |
	+------------+---------------------+-------+--------+--------+--------+
	| Blanking   | Start sync code     | FFh   | 00h    | 00h    | ABh    |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | B6h    |
	+------------+---------------------+       |        |        +--------+
	| Effective  | Start sync code     |       |        |        | 80h    |
	| line       | (SAV)               |       |        |        |        |
	|            +---------------------+       |        |        +--------+
	|            | End sync code (EAV) |       |        |        | 9Dh    |
	+------------+---------------------+-------+--------+--------+--------+

The transmission mode of Sub-LVDS synchronization code and pixel information in different Lanes is shown in the chart :ref:`diagram_sub_lvds_multilane_transfer`. Each Lane will transmit the same synchronization code, followed by pixel data. The pixel data will be transferred according to the used The number of channels is arranged sequentially in units of pixel width.

.. _diagram_sub_lvds_multilane_transfer:
.. figure:: ../../../../media/image67.png
	:align: center

	Sub-LVDS Multi Lane Transmission mode

The synchronization code and pixel data in Sub-LVDS are serial, while MIPI Rx supports the big and small ends of the data and can be set using registers. Taking the big endian mode as an example, the timing of outputting a single pixel is shown in the chart :ref:`diagram_sub_lvds_single_pixel_sequence`.

.. _diagram_sub_lvds_single_pixel_sequence:
.. figure:: ../../../../media/image68.png
	:align: center

	Sub-LVDS single pixel timing diagram

Sub-LVDS interface Linear Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In linear mode, Sub-LVDS uses synchronization codes to mark the start and end of each line in an image data, and anything other than the synchronization codes SAV and EAV is not valid video data, as shown in the chart :ref:`diagram_sub_lvds_liner_sequence`.

.. _diagram_sub_lvds_liner_sequence:
.. figure:: ../../../../media/image69.png
	:align: center

	Sub-LVDS Linear Mode Timing Diagram

Sub-LVDS Interface Wide Dynamic Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MIPI Rx can support two Sub-LVDS interface wide dynamic modes. In the first mode, as shown in the diagram :ref:`diagram_sub_lvds_wide_dynamic_mode_1`, the long and short exposure video signals are wrapped in SAV and EAV synchronization codes respectively. MIPI Rx can use different The synchronization code analyzes whether the video signal is a long exposure or a short exposure. The second mode is as shown in the diagram :ref:`diagram_sub_lvds_wide_dynamic_mode_2`. The long exposure and short exposure are wrapped in the same set of SAV and EAV. The width and blanking length of each line must be set in the register. MIPI Rx must use these registers. The settings and synchronization codes are used to analyze the timing of long exposure and short exposure, and then sent to the video processing module.

.. _diagram_sub_lvds_wide_dynamic_mode_1:
.. figure:: ../../../../media/image70.png
	:align: center

	Sub-LVDS Wide dynamic mode I

.. _diagram_sub_lvds_wide_dynamic_mode_2:
.. figure:: ../../../../media/image71.png
	:align: center

	Sub-LVDS Wide dynamic mode II

HiSPi Interface Data Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The High-Speed Serial Pixel (HiSPi) interface is also used in some cameras. Similar to Sub-LVDS, it uses synchronization codes to distinguish valid video information and distinguish long and short exposures in wide dynamic mode. The HiSPi specification defines four different packaging modes, namely Packetized-SP, Streaming-SP, Streaming-S and ActiveStart-SP8.

MIPI Rx supports two of the more common transmission methods, Packetized-SP and Streaming-SP.

HiSPi Interface Linear Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^

MIPI Rx supports two different HiSPi modes. In Packetized-SP mode, as shown in the diagram :ref:`diagram_hispi_packateized_sp_mode`, the image sensor uses SOF to represent the first line of the valid video signal, and uses EOF to represent the end of the last line of the valid video signal. Other valid video signals use SOL and EOL as the start and end of a line.

.. _diagram_hispi_packateized_sp_mode:
.. figure:: ../../../../media/image72.png
	:align: center

	HiSPi Packetized-SP mode

In Streaming-SP mode, as shown in the diagram :ref:`diagram_hispi_streaming_sp_mode`, the image sensor does not transmit the EOL or EOF that represents the end, so the MIPI Rx controller must use the register settings to know the number of valid video signals before it can be parsed. The correct video signal is sent to the video processing module (ISP). In addition, the Streaming-SP mode also supports the SAV signal indicating the number of blank lines. The synchronization codes supported by the two different transmission methods are organized as shown in the chart :ref:`table_hispi_sync_code_support_mode`.

.. _diagram_hispi_streaming_sp_mode:
.. figure:: ../../../../media/image72.png
	:align: center

	HiSPi Streaming-SP mode

.. This table is relatively small, so I won’t put the file include separately.

.. _table_hispi_sync_code_support_mode:
.. table:: HiSPi Sync Code Support Mode
	:widths: 1 1 1

	+-----------------+-------------------------+-------------------------+
	| Sync Code       | Packetized-SP           | Streaming-SP            |
	+=================+=========================+=========================+
	| SOF             | Required                | Required                |
	+-----------------+-------------------------+-------------------------+
	| SOL             | Required                | Required                |
	+-----------------+-------------------------+-------------------------+
	| EOF             | Required                | Unsupported             |
	+-----------------+-------------------------+-------------------------+
	| EOL             | Required                | Unsupported             |
	+-----------------+-------------------------+-------------------------+
	| SAV             | Unsupported             | Required                |
	+-----------------+-------------------------+-------------------------+

HiSPi Interface Wide Dynamic Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HiSPi interface wide dynamic mode is also divided into two different modes. The first Packetized-SP is shown in the chart :ref:`diagram_hispi_packetized_sp_width_dynamic_transfer`. Long exposure and short exposure will be distinguished by different synchronization codes, among which SOF_L and EOF_L The ones in are valid long exposure video signals, and the ones in SOF_S and EOF_S are the valid short exposure video signals. The last few lines of long exposure and the first few lines of short exposure are not valid pixel areas, but are filled with fixed values.

.. _diagram_hispi_packetized_sp_width_dynamic_transfer:
.. figure:: ../../../../media/image74.png
	:align: center

	HiSPi Packetized-SP wide dynamic transmission

The second type of wide dynamic transfer of Streaming-SP is shown in the chart :ref:`diagram_hispi_streaming_sp_width_dynamic_transfer`. The synchronization code and linear mode of long exposure and short exposure are the same, so a register is needed to set the exposure line between long exposure and short exposure. Only with this digital gap can MIPI Rx parse out the correct wide dynamic video signal.

.. _diagram_hispi_streaming_sp_width_dynamic_transfer:
.. figure:: ../../../../media/image75.png
	:align: center

	HiSPi Streaming-SP wide dynamic transmission

MIPI Rx Register Overview
~~~~~~~~~~~~~~~~~~~~~~~~~

Up to two sets of MIPI Rx modules can be used in the chip at the same time, which are mainly divided into three sets of registers. The first part is the register that controls the PHY module, with a base address of 0x0A0D0000. The second part is a register that controls the CSI module, with a base address of 0x0A0C2400 and 0x0A0C4400. The third part is the register that controls the Sub-LVDS and HiSPi modules. The base addresses are 0x0A0C2200 and 0x0A0C4200.

.. include:: ../../contents-share/video/mipi_rx_phy_registers_overview.table.rst

MIPI Rx Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MIPI Rx PHY Register Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Base address: 0x0A0D0000
''''''''''''''''''''''''

.. include:: ../../contents-share/video/mipi_rx_phy_registers_description_0x0a0d0000.table.rst

Base address: 0x0A0D0300
''''''''''''''''''''''''

.. include:: ../../contents-share/video/mipi_rx_phy_registers_description_0x0a0d0300.table.rst

Base address: 0x0A0D0600
''''''''''''''''''''''''

.. include:: ../../contents-share/video/mipi_rx_phy_registers_description_0x0a0d0600.table.rst

MIPI Rx CSI Control Registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../contents-share/video/mipi_rx_csi_registers_description.table.rst

MIPI Rx Sub-LVDS Control Registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../contents-share/video/mipi_rx_sub_lvds_registers_description.table.rst
