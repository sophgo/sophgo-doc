================
SG2044 Boot Flow
================

SG2044's original firmware boot process:

.. code-block:: text

  +---------+    +------+    +------+    +---------+    +--------+    +--------+    +-------+
  | BootROM |--->| FSBL |--->| ZSBL |--->| OpenSBI |--->| EDK II |--->| GRUB 2 |--->| Linux |
  +---------+    +------+    +------+    +---------+    +--------+    +--------+    +-------+

- **BootROM**

  Boot code in the ROM.

- **FSBL (First-Stage BootLoader)**

  System Code to initialize DDR, PCIe Controller, etc.

- **ZSBL (Zero-Stage BootLoader)**

  Mainly load configuration file (``conf.ini``), DTB, binaries of OpenSBI, and EDK II from microSD card or SPI Nor Flash into memory.

- **OpenSBI (RISC-V Open Source Supervisor Binary Interface)**

  An open-source reference implementation of the RISC-V SBI
  specifications for platform-specific firmwares executing in M-mode.

- **EDK II (EFI Development Kit Version 2)**

  The reference implementation of UEFI. Unified Extensible Firmware Interface (UEFI)
  is a specification for a software program that connects a computer's firmware to its operating system (OS).

- **GRUB 2  (GRand Unified Bootloader Version 2)**

  Load and transfer control to Linux OS.

- **Linux**

  Supported Linux distributions: Ubuntu 24.04.1, openEuler 24.03.

  Supported Linux Kernel Version: 6.12.

