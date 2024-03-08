VDP (Video Display Processor)
-----------------------------

Overview
~~~~~~~~

The VDP module can superimpose graphics data on video data and then output it through different display channels. Video data can be read from memory or receive video output from the VPSS module. Graphics data must be read from memory.

Architecture Description
~~~~~~~~~~~~~~~~~~~~~~~~

The overall architecture of VDP is as shown in the figure:

.. _diagram_vdp_overview:
.. figure:: ../../../../media/image41.png
	:align: center

	VDP functional block diagram

The chipset only supports one BT.656/BT.601/BT.1120/MCU-I80/MCU-M68/LVDS/MIPI DSI/serial TTL output

- Bus data reading and data processing, including video layer V and graphics layer G.

- The video layer can receive different image formats (YUV422, YUV420, YUV444, RBG packet, NV12/NV21, YUYV-packet) and convert them into the timing and format required by the display channel.

- The graphics layer supports OSD in ARGB8888, ARGB4444, ARGB1555, 8-bit/4-bit LUT, font base and other formats.

- Support OSD compression format.

- Blend: Single layer graphics layer G video graphics overlay.

The characteristics of VDP are as follows:

- MIPI Tx output interface: supports up to 1080P@60fps RGB24-bit output.

- LVDS output: supports up to 720P@60fps RGB24-bit output.

- Digital output interface: (BT format only support progressive mode)

  - Support ITU-R BT.1120 output

  - Support ITU-R BT.656 output

  - Support ITU-R BT.601 output

  - MCU I80/M68 8-bit output

  - Support serial TTL parallel output

- Video layer: V layer.

- Graphic layer: G layer.

- Superposition characteristics: V/G 256-order linear superposition, and supports Gamma correction.

- VDP contains a display channel, a timing interrupt and a low-bandwidth interrupt.

Way of Working
~~~~~~~~~~~~~~

Clock Configuration
^^^^^^^^^^^^^^^^^^^

VDP is equipped with a dedicated clock generator and the architecture is as follows:

.. _diagram_vdp_clock_generator:
.. figure:: ../../../../media/image42.png
	:align: center

	VDP clock generator

- clk_syn : 1GHz or 1.2Ghz

- FREQ_SYN: 6-bit integer, 26-bit decimal frequency generator

- PLL: generates VDP clock and clock required for MIPI Tx/LVDS serial

Reset
^^^^^

VDP reset includes a hardware reset and a software reset.

Before performing an AXI bus reset:

- Turn off all AXI access.

- Confirm that the AXI access operation has ended, and then reset the configuration bus.

Output Interface
^^^^^^^^^^^^^^^^

VDP supports the following three interface outputs

- MIPI DSI

- LVDS

- ITU-R BT.1120/ITU-R BT.656/ITU-R BT.601/MCU I80/MCU M68/Serial TTL output

Interrupt
^^^^^^^^^

VDP supports two types of interrupts

- Vertical timing interrupt

- Low bandwidth interrupt

Vertical Timing Interrupt
^^^^^^^^^^^^^^^^^^^^^^^^^

VDP contains a display channel, corresponding to a vertical timing interrupt:

- Support frame start/end interrupt.

- Support interrupt mask configurable.

- Each interrupt can be cleared by writing 1.

Low Bandwidth Interrupt
^^^^^^^^^^^^^^^^^^^^^^^

VDP supports polling mode to provide low bandwidth status:

- Interrupt mask configurable.

- Interrupt is cleared by writing 1.

Function Description
~~~~~~~~~~~~~~~~~~~~

Video Layer Functionality
^^^^^^^^^^^^^^^^^^^^^^^^^

Video Layer V Properties
^^^^^^^^^^^^^^^^^^^^^^^^

- Support input image formats: 400, planar-420, planar-422, planar-444, RGB packet.

- The minimum input resolution is 64x64, and the maximum input resolution is 1920x1080.

- The minimum output resolution is 64x64, and the maximum output resolution is 1920x1080.

- Support input data bit width: 8-bit.

- YUV420 horizontal/vertical resolution is a multiple of 2.

- YUV422 horizontal resolution is a multiple of 2.

- YUV400/Planar-444(RGB or YUV)/RGB packet has no resolution limit.

- The source starting address is configurable, and the address is 32-byte aligned.

  - Source stride configurable, 32-byte aligned.

- Support color space conversion and contrast/brightness adjustment.

- Support video layer BT.601, BT.709 color gamut conversion.

- Support configurable display position/size and can be displayed anywhere on the screen.

Graphics Layer G Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Support input pixel formats: ARGB8888, ARGB4444, ARGB1555, LUT8, LUT4, LUT1.

- The minimum input resolution is 64x64, and the maximum input resolution is 1920x1080.

- The source starting address is configurable, and the address is 32-byte aligned.

  - Source stride configurable, 32-byte aligned.

  - Support color space conversion.

  - Support configurable display position and can be displayed anywhere on the screen.

  - Support 0~255 alpha.

  - Support colorkey processing.

Overlay Processing
^^^^^^^^^^^^^^^^^^

VDP only supports one video layer and one graphics layer overlay.

Overlay Properties
^^^^^^^^^^^^^^^^^^

Supports 8 window overlay.

Display Channel Characteristics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Can be used as HD and SD output channels.

  - Only one output interface can be selected for output.

  - Supports typical 1080P@60fps, 720P@60fps output timing.

Timing Configuration
^^^^^^^^^^^^^^^^^^^^

The VDP output interface can be connected to different chip interfaces and supports the configuration of various typical and atypical timing sequences.

All timing parameters must be configured before the interface is turned on.

HD Output Interface MIPI Tx
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. only:: sg2002

	- Support RGB666, RGB565, RGB10-10-10 output.

.. only:: sg2000

	- Support RGB888, RGB666, RGB565, RGB10-10-10 output.

- Support 1080P@60fps 4-channel display.

- Support 720P@60fps 2/4-channel display.

HD Output Interface BT.1120 Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Support YUV422 8bit output.

- Clip that supports data clamping. According to the interface protocol, the Y clamping range is 16~235, and the C clamping range is 16~240.

- Support the following typical output timings: 720P, 1080P.

- 16 bit data, Y is in the high bit by default, C is in the low bit, YC positions are interchangeable.

- Support color signal Cb/Cr timing interchange.

- Support output associated clock inversion.

- Only Progressive timing is supported.

SD output interface BT.656 features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Support YUV422 8bit output.

- Clip that supports data clamping. According to the interface protocol, the Y clamping range is 16~235, and the C clamping range is 16~240.

- Support Y/C timing interchange and color signal Cb/Cr timing interchange.

- Only Progressive timing is supported.

BT.601 Features
^^^^^^^^^^^^^^^

- Support YUV422 8-bit output.

- YC data range 0 ~ 255.

- Support VS/HS sync signal output.

- Support Y/C timing interchange and color signal Cb/Cr timing interchange.

- Only Progressive timing is supported.

MCU Features
^^^^^^^^^^^^

- Support 8-bit data, 4-bit control output.

- Support I80/M68 format output.

LCD LVDS Output Interface
^^^^^^^^^^^^^^^^^^^^^^^^^

- Support 1-link LVDS output.

- Support 6-bit/8-bit RGB serial output.

- Support VESA/JEIDA format output.

.. _diagram_data_format_lvds_jeida_vesa_mode:
.. figure:: ../../../../media/image43.png
	:align: center

	LVDS JEIDA/VESA mode data format

VDP Register Overview
~~~~~~~~~~~~~~~~~~~~~

The VDP DISP register location is 0X0A08_8000 ~ 0x0A08_83FF.

.. include:: ../../contents-share/video/vdp_disp_registers_overview.table.rst

The VDP OSD register location is 0X0A08_8800 ~ 0x0A08_89FF.

.. include:: ../../contents-share/video/vdp_osd_registers_overview.table.rst

VDP Register Description
~~~~~~~~~~~~~~~~~~~~~~~~

VDP DISP Registers
^^^^^^^^^^^^^^^^^^

.. include:: ../../contents-share/video/vdp_disp_registers_description.table.rst

VDP_OSD Register Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../contents-share/video/vdp_osd_registers_description.table.rst
