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

+-----------------+------------------------------------+------------+
| Section         | Key - Vaule                        | Permission |
+=================+====================================+============+
| [sophgo-config] |                                    | Compulsory |
+-----------------+------------------------------------+------------+
|                 | name = XXX.dtb                     | Compulsory |
| [devicetree]    +------------------------------------+------------+
|                 | addr = 0xAAAAAAAA                  | Optional   |
+-----------------+------------------------------------+------------+
|                 | mac0 = 0xAAAAAAAAAAAA              | Compulsory |
| [mac-address]   +------------------------------------+------------+
|                 | mac1 = 0xAAAAAAAAAAAA              | Compulsory |
+-----------------+------------------------------------+------------+
|                 | name = u-boot.bin / riscv64_Image  | Optional   |
| [kernel]        +------------------------------------+------------+
|                 | addr = 0xAAAAAAAA                  | Optional   |
+-----------------+------------------------------------+------------+
|                 | name = fw_jump.bin                 | Optional   |
| [firmware]      +------------------------------------+------------+
|                 | addr = 0xAAAAAAAA                  | Optional   |
+-----------------+------------------------------------+------------+
|                 | name = initrd.img                  | Optional   |
| [ramfs]         +------------------------------------+------------+
|                 | addr = 0xAAAAAAAA                  | Optional   |
+-----------------+------------------------------------+------------+
| [eof]           |                                    | Compulsory |
+-----------------+------------------------------------+------------+

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

      [mac-address]
      mac0 = 0xAAAAAAAAAAAA
      mac1 = 0xAAAAAAAAAAAA

      [kernel]
      name = riscv64_Image
      ; name = u-boot.bin
      ; addr = 0x02000000

      [eof]

3. Location of ``conf.ini``
===========================
At the stage of ``ZSBL``, we use the `inih <https://github.com/benhoyt/inih>`_,
an INI parser to parse the ``conf.ini`` file.
The ``conf.ini`` can be stored in either of the following two locations.
Read the INI file from miscoSD Card first. If the file is not found, read it
from SPI Flash0.

microSD Card
------------
The ``conf.ini`` is saved in the ``0:riscv64/`` of a miscoSD Card.

SPI Flash
---------
There are two mtd devices on SG2042, namely SPI Flash0
(``0x7000180000``, ``/dev/mtd0``) and SPI Flash1
(``0x7002180000``, ``/dev/mtd1``).
The ``firmware.bin`` are written in the SPI Flash1, and the ``conf.ini``
is written in the SPI Flash0.

Use the following commands to update the flash:

.. highlights::

   .. code:: sh

      # install userspace utilities package: mtd-utils
      sudo apt-get install mtd-utils

      # write data into the flash0
      sudo flashcp conf.ini /dev/mtd0
