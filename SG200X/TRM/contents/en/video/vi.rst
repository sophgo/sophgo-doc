VI
--

Overview
~~~~~~~~

The Video Input (VI) unit is a module on chip which is responsile receiving camera video data. VI can support MIPI Rx (including MIPI, Sub-LVDS, HiSPi) interface or BT.656, BT.601, BT.1120 interface and DC (Digital Camera ) to receive video data, to processe it and send it to the next-level video processing module (ISP). The functional block diagram of a VI is shown in the diagram :ref:`diagram_vi_function`.

VI is divided into two physical sub-modules, consisting of the mobile industry processor interface receiver module MIPI Rx and the video input processing module VI Proc. The MIPI Rx module receives and processes different video data, while the VI Proc module integrates video signals in different formats into a single video signal required by the ISP module and sends it out.

.. _diagram_vi_function:
.. figure:: ../../../../media/image29.png
	:align: center

	VI functional block diagram

Features
~~~~~~~~

- MIPI Rx supports up to two sensor data inputs at the same time.

  - Single sensor supports up to 5M (2688x1944, 2880x1620) @60fps HDR input or @30fps linear input.

  - Dual-channel sensor supports up to FHD (1920x1080) @60fps HDR or linear input.

- MIPI Rx input supports a maximum data bit width of 12bit.

- Supports BT.656, BT.601, BT.1120 (only progressive mode is supported).

- Supports BT.656/BT.1120 multi-channel fusion input (1,2,4 channels, only supports progressive mode).

DC interface

- Support MIPI CSI-2, Sub-LVDS, HiSPi interface.

- Support MIPI interface input YUV422 format.

- Supports two-frame high dynamic range (HDR) image input.

Mode Function Description
~~~~~~~~~~~~~~~~~~~~~~~~~

Typical Application
^^^^^^^^^^^^^^^^^^^

VI can support multiple timing inputs and different interfaces, and perform video input collection for different encoding methods. The system can use registers to configure different functional modes to adapt to different video interfaces.

The VI module can support up to three inputs. Typical inputs are as follows:

- 1 channel 5M (2688x1944, 2880x1620) @60fps HDR input or linear @30fps input.

- 2 channels FHD (1920x1080) @60fps HDR or line input + 1 channel BT input (BT.656, BT.601 or BT.1120).

- 1 channel 5M (2688x1944, 2880x1620) @60fps HDR or @30fps linear input + 1 channel BT input.

Functional Principle
^^^^^^^^^^^^^^^^^^^^

BT.1120 Interface Timing
^^^^^^^^^^^^^^^^^^^^^^^^

VI supports Y/C separated input BT.1120 interface timing. Before transmitting video signals, a synchronization code will be transmitted. The synchronization code uses special bytes SAV and EAV in the data stream to represent the start and end of valid row data respectively. After the synchronization code, 16 bits are used to transmit the video signal, of which 8 bits are used to transmit brightness and the other 8 bits are used to transmit chroma, as shown in the chart :ref:`diagram_bt1120_horizontal_sequence` and the chart :ref:`diagram_bt1120_vertical_sequence`.

.. _diagram_bt1120_horizontal_sequence:
.. figure:: ../../../../media/image30.png
	:align: center

	BT.1120 horizontal interface timing

.. _diagram_bt1120_vertical_sequence:
.. figure:: ../../../../media/image31.png
	:align: center

	BT.1120 vertical interface timing

The synchronization code format is a combination of 4 bytes, in order {0xFF, 0x00, 0x00, EAV/SAV}. The fourth byte is detailed as follows. SG2002 only supports progressive progressive scan format (Progressive). Therefore, the value of bit 6 is 0.

.. This table is very small, so I won’t make it into a separate file include.

.. _table_sync_code_format:
.. table:: Sync code format
	:widths: 1 1 1 1 1 1 1 1 1

	+--------+--------------------+---------------------------+---------+
	|        | SAV/EAV bit        | Protection Bit            |         |
	+========+======+======+======+======+======+======+======+=========+
	| 7      | 6    | 5    | 4    | 3    | 2    | 1    | 0    | Comment |
	| (Fixed)| (F)  | (V)  | (H)  | (P3) | (P2) | (P1) | (P0) |         |
	+--------+------+------+------+------+------+------+------+---------+
	| 1      | 0    | 0    | 0    | 0    | 0    | 0    | 0    | SAV_VLD |
	+--------+------+------+------+------+------+------+------+---------+
	| 1      | 0    | 0    | 1    | 1    | 1    | 0    | 1    | EAV_VLD |
	+--------+------+------+------+------+------+------+------+---------+
	| 1      | 0    | 1    | 0    | 1    | 0    | 1    | 1    | SAV_BLK |
	+--------+------+------+------+------+------+------+------+---------+
	| 1      | 0    | 1    | 1    | 0    | 1    | 1    | 0    | EAV_BLK |
	+--------+------+------+------+------+------+------+------+---------+

SAV_VLD: Valid line area, line synchronization signal ends, and valid pixels begin.

EVA_VLD: Effective line area, line synchronization signal starts, and effective pixel ends.

SAV_BLK: Blanking line area, end of line synchronization signal.

EAV_BLK: Blanking row area, horizontal sync signal starts.

BT.656 Interface Timing
^^^^^^^^^^^^^^^^^^^^^^^

VI also supports Y/C combined input BT.656 interface timing. During transmission, it also uses synchronization codes SAV and EAV to indicate the start and end of valid line data, but only uses 8 bits to transmit video signals, and uses time sharing to transmit brightness and Chromaticity, as shown in diagram :ref:`diagram_bt656_horizontal_sequence`.

.. _diagram_bt656_horizontal_sequence:
.. figure:: ../../../../media/image32.png
	:align: center

	BT.656 horizontal interface timing

The only difference between BT.656 and BT.1120 is that 16 bit (BT.1120) and 8 bit (BT.656) are used for image transmission. The rest of the vertical timing and synchronization code formats are the same.

BT.601 Interface Timing
^^^^^^^^^^^^^^^^^^^^^^^

In addition to utilizing synchronization codes BT.1120 and BT.656, VI supports BT.601 interface timing utilizing a variety of different synchronization signals for transmission. The actual video data can be set to the 16-bit mode of Y/C separate input or the 8-bit mode of Y/C combined time-sharing input using the register. The synchronization mode can be selected by the register to be vhs, vde, or vsde. The detailed timing is as shown below.

.. _diagram_bt601_vhs_symc_mode:
.. figure:: ../../../../media/image33.png
	:align: center

	BT.601 vhs synchronous mode

The input synchronization signal in vhs mode is frame synchronization signal (vs), horizontal synchronization signal (hs), the system must set the number of blanking lines after the frame (vs_back_porch), the image height (img_ht), the number of blanking pixels after the line (hs_back_porch) and Image width (img_wd).

.. _diagram_bt601_vde_symc_mode:
.. figure:: ../../../../media/image34.png
	:align: center

	BT.601 vde synchronous mode

The vde mode synchronization signals are the row valid signal (vde) and the row valid signal (hde). In this mode, the system does not need to set parameters related to timing and phase sequence. The VI module will receive data based on the hde/vde signal and perform frame updates based on the vde signal.

.. _diagram_bt601_vsde_symc_mode:
.. figure:: ../../../../media/image35.png
	:align: center

	BT.601 vsde synchronous mode

The vsde mode sync signals are the frame sync signal (vs) and the valid pixel flag (de). In this mode, the system does not need to set parameters related to timing and phase sequence. The VI module will receive data based on the de signal and perform frame updates based on the vs signal.

.. _diagram_bt601_yc_separate_16bit_mode:
.. figure:: ../../../../media/image36.png
	:align: center

	BT.601 Y/C separated 16bit mode

.. _diagram_bt601_yc_combine_8bit_mode:
.. figure:: ../../../../media/image37.png
	:align: center

	BT.601 Y/C combined 8bit mode

Digital Camera (DC) Interface Timing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VI supports digital camera (DC) interface timing that transmits RAW format and simulates BT transmission. The DC interface can support four different modes: 8bit, 10bit, 12bit, and 16bit. Register settings can also be used to receive synchronization codes or similar to BT. 601's three different synchronization modes to receive video signals.

.. _diagram_dc_sync_code_mode:
.. figure:: ../../../../media/image38.png
	:align: center

	DC sync code mode

.. _diagram_dc_sync_signal_mode_vhs:
.. figure:: ../../../../media/image33.png
	:align: center

	DC sync signal mode -vhs mode

.. _diagram_dc_sync_signal_mode_vde:
.. figure:: ../../../../media/image34.png
	:align: center

	DC sync signal mode -VDE mode

.. _diagram_dc_sync_signal_mode_vsde:
.. figure:: ../../../../media/image35.png
	:align: center

	DC sync signal mode -VSDE mode

Image Storage Mode
~~~~~~~~~~~~~~~~~~

Images stored in DRAM are divided into two formats: Bayer 12bit and YCbCr 8bit. Among them, Y/Cb/Cr are stored separately in three different DRAM locations. The arrangement of the two (12bit/8bit) format images in DRAM is as shown in the figure below.

.. _diagram_bayer_12bit_graphc_storage_format:
.. figure:: ../../../../media/image39.png
	:align: center

	Bayer 12 bit image storage method

.. _diagram_ycbcr_8bit_graphc_storage_format:
.. figure:: ../../../../media/image40.png
	:align: center

	YCbCr 8bit image storage method

VI Register Overview
~~~~~~~~~~~~~~~~~~~~

There are two identical sets of VI modules in the chip, and the internal register offset addresses are the same, and the base addresses are 0x0A0C2000 and 0x0A0C4000 respectively. There is also a set of VI modules that only support the BT interface, with the base address 0x0A0C6000.

.. include:: ../../contents-share/video/vi_registers_overview.table.rst

VI Register Description
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/video/vi_registers_description.table.rst
