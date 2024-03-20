Features
--------

Processor Cores
~~~~~~~~~~~~~~~

- Main processor RISCV C906 @ 1.0Ghz

  - 32KB I-cache, 64KB D-Cache

  - Integrated Vector and Floating Point Unit (FPU)

- Main processor ARM Cortex-A53 @ 1.0Ghz

  - 32KB I-cache, 32KB D-Cache

  - 128KB L2 cache

  - Support Neon and Floating Point Unit (FPU)

- Coprocessor RISCV C906 @ 700Mhz

  - Integrated Floating Point Unit (FPU)

TPU
~~~

- Built-in TPU, computing power reaches ~1.0TOPS INT8.

- Supports mainstream neural network architectures: Caffe, Pytorch, TensorFlow(Lite), ONNX and MXNet.

- Support Pedestrian Detection, Face Detection, Face recognition, Face anti-spoofing and other video structured applications.

Video codec
~~~~~~~~~~~

- H.264 Baseline/Main/High profile

- H.265 Main profile

- H.264/H.265 both support I frames and P frames

- MJPEG/JPEG baseline

- H.264 codec maximum resolution: 2880x1620 (5M)

- H.265 encoding maximum resolution: 2880x1620 (5M)

- H.264 codec performance

  - 2880x1620@30fps + 720x576@30fps

  - 1920x1080@30fps encoding + 1920x1080@30fps decoding

- H.265 encoding performance

  - 2880x1620@30fps + 720x576@30fps

- JPEG maximum codec performance

  - 2880x1620@30fps

- Supports multiple rate control modes such as CBR/VBR/FIXQP.

- Supports Region of Interest (ROI) encoding

Video Interface
~~~~~~~~~~~~~~~

- Input

  - Supports two simultaneous video inputs (mipi 2L + 1L)

  - Supports MIPI, Sub-LVDS, HiSPI and other serial interfaces

  - Support 8/10/12 bit RGB Bayer video input

  - Support BT.656

  - Support AHD multi-channel mixed BT format

  - Supports SONY, OnSemi, OmniVision and other high-definition CMOS sensors

  - Provide programmable frequency output for sensor as reference clock

  - Supports a maximum width of 2880 and a maximum resolution of 5M (2688x1944, 2880x1620)

- Output

  - Supports multiple serial and parallel screen display specifications

  - Support serial interfaces such as MIPI

  - Supports BT656, BT601 (8bit), BT1120, 8080 and other parallel interfaces

  - Support SPI output interface

ISP and Image processing
~~~~~~~~~~~~~~~~~~~~~~~~

- 90 degree, 180 degree, 270 degree rotation for image and video

- Mirror and Flip functions for image and video

- Video 2-layer OSD overlay

- Video 1/32 ~ 32x zoom function

- 3A (AE/AWB/AF) algorithm

- Fixed mode noise elimination, dead pixel correction

- Lens shading correction, lens distortion correction, purple fringing correction

- Direction adaptive demosaic

- Gamma correction, (regional/global) dynamic contrast enhancement, color management and enhancement

- Area adaptive defogging

- Bayer noise reduction, 3D noise reduction, detail enhancement and sharpening enhancement

- Local Tone mapping

- Sensor self-bandwidth dynamic and 2 frame wide dynamic

- Two-axis digital image stabilization

- Lens distortion correction

- Provide PC-side ISP tuning tools

Hardware acceleration engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Mixed hardware and software mode supports part of OpenCV libraries

- Mixed hardware and software mode supports part of IVE libraries

Audio Codec
~~~~~~~~~~~

- Integrated Audio CODEC, supports 16-bit audio source/voice input and output

- Integrated mono microphone input

- Integrated mono output. (An external amplifier is required to drive the speaker)

- Internally integrated another microphone is directly connected to the output channel to facilitate AEC implementation

- Software audio codec protocols (G.711, G.726, ADPCM)

- Software supports audio 3A (AEC, ANR, AGC) function

Network Interface
~~~~~~~~~~~~~~~~~

- The Ethernet module provides one Ethernet MAC to receive and send network data.

- Ethernet MAC with built-in 10/100Mbps Fast Ethernet Transceiver, can work in 10/100Mbps full-duplex or half-duplex mode.

Security System Module
~~~~~~~~~~~~~~~~~~~~~~

- Hardware implements AES/DES/SM4 multiple encryption and decryption algorithms

- Hardware implementation of HASH (SHA1/SHA256) hash algorithm

- Hardware implemented random number generator

- Internally integrated 2Kbit eFuse logical space

Intelligent and safe operating environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Support the establishment of trust chain: Provide the foundation of a secure environment and the foundation of a trusted environment, such as hardware security settings and root of trust.

- Supports secure boot and provides security hardware and software protection functions.

- Support data encryption security: data encryption program, computing core encryption.

- Support software and firmware signature verification process: verify software credibility and integrity, including booting and loading signature verification procedures.

- Support secure storage and transmission: protect external data storage and exchange.

- Support security updates.

Peripheral interface
~~~~~~~~~~~~~~~~~~~~

- Integrated POR, Power sequence.

- 4 single-ended ADCs (3 No-die domain).

- 6 I2C (1 No-die domain).

- 3 SPIs.

- 5 sets of UART (1 No-die domain).

- 4 sets (15 channels) PWM.

- 2 SDIO interfaces:

  - One supports connected with SD 3.0 Card under 3V (supports maximum capacity SDXC 2TB, supported speed is UHS-I).

  - One supports connected with other SDIO 3.0 devices under 1.8V/3.0V (supported speed is UHS-I).

- 66 GPIO interfaces (14 no die domain).

- Integrate keyscan and Wiegand.

- Integrated MAC PHY supports 10/100Mbps full-duplex or half-duplex mode.

- One USB Host/device interface.

External memory interface
~~~~~~~~~~~~~~~~~~~~~~~~~

- Built-in DRAM.

  - DDR3 16bit x 1, maximum speed up to 1866Mbps, capacity 2Gbit (256MB).

- SPI NOR flash interface (1.8V / 3.0V).

  - Supports 1, 2, 4 wire modes.

  - Maximum support is 256MByte.

- SPI Nand flash interface (1.8V / 3.0V).

  - Supports 1KB/2KB/4KB page (corresponding maximum capacity 16GB/32GB/64GB).

  - Use the ECC module built into the device itself.

- eMMC 4.5 interface (1.8V/3.0V) SD0 EMMC has a common power supply. Because the SD card defaults to 3V, it is not suitable to connect to 1.8V eMMC when there is an SD card.

  - 4 bit interface.

  - Support HS200.

  - Maximum supported capacity 2TB.

Chip physical specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Power consumption

  - 1080P + Video encode + AI : ~ 500mW

- Operating Voltage

  - Core voltage is 0.9V

  - IO voltage is 1.8V and 3.0V

  - DDR voltage is as shown in the table below

    - 1.35V

- Encapsulation

  - Using QFN package, the package size is 9mmx9mmx0.9mm. The pin pitch is 0.35mm. The total number of pins is 88.