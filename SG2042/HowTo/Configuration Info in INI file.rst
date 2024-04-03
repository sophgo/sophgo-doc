==================================
Configuration Info in ``conf.ini``
==================================

1. Introduction of ``conf.ini``
================================
The ``conf.ini`` is an artificial configuration file that contains necessary
evaluation board information for SG2042. The file consists of text-based
content with a structure and syntax comprising key-value pairs for properties,
and sections that organize the properties.

If you want to know more about the INI file, please access
`the introduction link <https://en.wikipedia.org/wiki/INI_file>`_.

2. Information in ``conf.ini``
==============================
The convention is that the ``conf.ini`` must start at byte 0 with a section
called ``sophgo-config``, and end with a section called ``eof``.
In addition, the current ``conf.ini`` contains the sections
listed in the following table.

+-----------------+-------------------------------------------------+------------+
| Section         | Key - Vaule                                     | Permission |
+=================+=================================================+============+
| [sophgo-config] |                                                 | Compulsory |
+-----------------+-------------------------------------------------+------------+
|                 | name = XXX.dtb                                  | Compulsory |
| [devicetree]    +-------------------------------------------------+------------+
|                 | addr = 0xAAAAAAAA                               | Optional   |
+-----------------+-------------------------------------------------+------------+
|                 | mac0 = 0xAAAAAAAAAAAA                           | Optional   |
| [mac-address]   +-------------------------------------------------+------------+
|                 | mac1 = 0xAAAAAAAAAAAA                           | Optional   |
+-----------------+-------------------------------------------------+------------+
|                 | name = riscv64_Image / u-boot.bin / SG2042.fd   | Optional   |
| [kernel]        +-------------------------------------------------+------------+
|                 | addr = 0xAAAAAAAA                               | Optional   |
+-----------------+-------------------------------------------------+------------+
|                 | name = fw_jump.bin                              | Optional   |
| [firmware]      +-------------------------------------------------+------------+
|                 | addr = 0xAAAAAAAA                               | Optional   |
+-----------------+-------------------------------------------------+------------+
|                 | name = initrd.img                               | Optional   |
| [ramfs]         +-------------------------------------------------+------------+
|                 | addr = 0xAAAAAAAA                               | Optional   |
+-----------------+-------------------------------------------------+------------+
| [eof]           |                                                 | Compulsory |
+-----------------+-------------------------------------------------+------------+

Except for the section that is mandatory to be added to ``conf.ini``,
other sections or key-value pairs can be added as required,
if not, with default values.

Example
--------
Here is an example.

.. highlights::

   .. code:: ini

      [sophgo-config]

      [devicetree]
      name = mango-sophgo-x8evb.dtb
      ; addr = 0x20000000

      ;[mac-address]
      ;mac0 = 0xAAAAAAAAAAAA
      ;mac1 = 0xAAAAAAAAAAAA

      [kernel]
      name = riscv64_Image
      ; name = u-boot.bin
      ; name = SG2042.fd
      ; addr = 0x02000000

      [eof]

3. Location of ``conf.ini``
===========================
At the stage of `ZSBL <https://github.com/sophgo/zsbl>`_, we use the `inih <https://github.com/benhoyt/inih>`_,
an INI parser to parse the ``conf.ini`` file.
The ``conf.ini`` can be stored in either of the following two locations.

.. note:: Try to read the INI file from the microSD Card first. If the file is not found, read it from SPI Nor Flash.

microSD Card
------------
The ``conf.ini`` is saved in the ``0:riscv64/`` of a microSD Card.

SPI Nor Flash
-------------
The SPI Nor Flash Master Controller has been integrated into the MTD
(Memory Technology Device) subsystem of the Linux Kernel.
Therefore, you will find two MTD devices on a single SG2042.

Note that there are four MTD devices on the **PISCES** and **CAPRICORN** server which have dual SG2042 processors (CPU0 and CPU1).

The following table shows the MTD devices usage.

+-----------+-------------+----------------+----------------------------+
| Processor |  MTD Device |  Base Address  | Stored File                |
+===========+=============+================+============================+
|           |  /dev/mtd0  |  0x7000180000  |  conf.ini                  |
|   CPU 0   +-------------+----------------+----------------------------+
|           |  /dev/mtd1  |  0x7002180000  |  firmware-%Y%m%d%H%M%S.bin |
+-----------+-------------+----------------+----------------------------+
|           |  /dev/mtd2  |  0xF000180000  |  conf.ini                  |
|   CPU 1   +-------------+----------------+----------------------------+
|           |  /dev/mtd3  |  0xF002180000  |  firmware-%Y%m%d%H%M%S.bin |
+-----------+-------------+----------------+----------------------------+

Use the following commands to update the flash:

.. highlights::

   .. code:: sh

      # get MTD device info
      cat /proc/mtd

      # install userspace utilities package: mtd-utils
      sudo apt-get install mtd-utils # Ubuntu
      sudo dnf -y install mtd-utils # Fedora

      # update conf.ini in the flash0
      sudo flashcp conf.ini /dev/mtd0
      # update conf.ini in the flash2 on dual processors server
      sudo flashcp conf.ini /dev/mtd2

      # update firmware in the flash1
      sudo flashcp firmware-%Y%m%d%H%M%S.bin /dev/mtd1
      # update firmware in the flash3 on dual processors server
      sudo flashcp firmware-%Y%m%d%H%M%S.bin /dev/mtd3

      # dump flash data into flash.bin
      sudo dd if=/dev/mtdX of=flash.bin

4. Further Description of ``[kernel].name``
===========================================
SG2042 products support multiple boot flows, please further view `the bootflow figure <https://github.com/sophgo/sophgo-doc/blob/main/SG2042/HowTo/bootflow.rst>`_. And we configure the ``[kernel].name`` to choose different boot flows.

Now SG2042 boots by **LinuxBoot** by default, s.c. ``[kernel].name=riscv64_Image`` and the ``[ramfs].name=initrd.img``.

Except for LinuxBoot, you have two other choices:

* **U-Boot**: Configure ``[kernel].name=uboot.bin``, please further access `repo: sophgo/u-boot <https://github.com/sophgo/u-boot>`_.

* **UEFI**: Configure ``[kernel].name=SG2042.fd``, please further read `the README of EDKII on SG2042 <https://github.com/sophgo/sophgo-edk2>`_.