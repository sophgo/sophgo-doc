==================================
Configuration Info in ``conf.ini``
==================================

1. Introduction of ``conf.ini``
================================
The ``conf.ini`` is an artificial configuration file that contains necessary
evaluation board information for SG2044. The file consists of text-based
content with a structure and syntax comprising key-value pairs for properties,
and sections that organize the properties.

If you want to know more about the INI file, please access
`the introduction link <https://en.wikipedia.org/wiki/INI_file>`_.

2. Sorce Code Location, and File Location in Boot Process 
============================================================
conf.ini for 2044 is in `zsbl/arch/riscv/boot/conf/sg2044-evb-conf.ini <https://github.com/sophgo/zsbl/blob/master/arch/riscv/boot/conf/sg2044-evb-conf.ini>`_

When boot with SD card, it should be put into ``0:riscv64``, which is in the EFI partition of the SD card.

When boot with SPI Nor Flash, it should be put into SPI Nor Flash 1.

3. Information in ``conf.ini``
==============================
The convention is that the ``conf.ini`` must start at byte 0 with a section
called ``sophgo-config``, and end with a section called ``eof``.
In addition, the current ``conf.ini`` contains the sections
listed in the following table.

+---------------------+-------------------------------------------------+------------+
| Section             | Key - Vaule                                     | Permission |
+=====================+=================================================+============+
| [sophgo-config]     |                                                 | Compulsory |
+---------------------+-------------------------------------------------+------------+
|                     | bios_vendor = SOPHGO                            | Optional   |
| [Bios Information]  +-------------------------------------------------+------------+
|                     | bios_version = 1.0                              | Optional   |
|                     +-------------------------------------------------+------------+
|                     | date = 2024-12-25                               | Optional   |
|                     +-------------------------------------------------+------------+
|                     | time = 00:00:00                                 | Optional   |
+---------------------+-------------------------------------------------+------------+
|                     | manufacturer = SOPHGO                           | Optional   |
|                     +-------------------------------------------------+------------+
|                     | product_name = SG2044                           | Optional   |
| [product]           +-------------------------------------------------+------------+
|                     | version = 1.0                                   | Optional   |
|                     +-------------------------------------------------+------------+
|                     | serial-number = TYUI7890                        | Optional   |
+---------------------+-------------------------------------------------+------------+
|                     | product_name = SG2044_EVB                       | Optional   |
| [board]             +-------------------------------------------------+------------+
|                     | version = 1.1                                   | Optional   |
+---------------------+-------------------------------------------------+------------+
|                     | processor_version = C920                        | Optional   |
|                     +-------------------------------------------------+------------+
|                     | frequency = 2800000000                          | Optional   |
| [CPU]               +-------------------------------------------------+------------+
|                     | l1-i-cache-size = 65536                         | Optional   |
|                     +-------------------------------------------------+------------+
|                     | l1-d-cache-size = 65536                         | Optional   |
|                     +-------------------------------------------------+------------+
|                     | l2-cache-size = 2097152                         | Optional   |
|                     +-------------------------------------------------+------------+
|                     | l3-cache-size = 67108864                        | Optional   |
+---------------------+-------------------------------------------------+------------+
|                     | type = LPDDR5x                                  | Optional   |
|                     +-------------------------------------------------+------------+
| [DDR]               | data-rate = 8533000000                          | Optional   |
|                     +-------------------------------------------------+------------+
|                     | rank = 2                                        | Optional   |
+---------------------+-------------------------------------------------+------------+
|                     | mac0 = 0xAAAAAAAAAAAA                           | Optional   |
| [mac-address]       +-------------------------------------------------+------------+
|                     | mac1 = 0xAAAAAAAAAAAA                           | Optional   |
+---------------------+-------------------------------------------------+------------+
| [eof]               |                                                 | Compulsory |
+---------------------+-------------------------------------------------+------------+

Except for the section that is mandatory to be added to ``conf.ini``,
other sections or key-value pairs can be added as required configuration that contains necessary evaluation board information for SG2044. 

Further explanation of the sections in ``conf.ini``
----------------------------------------------------

The file consists of text-based content with a structure and syntax comprising key-value pairs for properties, and sections that organize the properties.
Specifically, the sections are structures in SMBIOS (System Management BIOS) table, and the keys are members of the structures.
If you want to know more about SMBIOS, please access `SMBIOS specification <https://www.dmtf.org/sites/default/files/standards/documents/DSP0134_3.6.0.pdf>`_.

1. [Bios Information] corresponds to BIOS Information (Type 0) structure. bios_vendor, bios_version, date and time are members of the structure.

2. [product] corresponds to System Information (Type 1) structure. manufacturer, product_name, version, serial-number are members of the structure.

3. [board] corresponds to Baseboard (or Module) Information (Type 2) structure. product_name, version are members of the structure.

4. [CPU] corresponds to Processor Information (Type 4) structure. processor_version, frequency are members of the structure. But any field under [CPU] section related to cache is belonged to Cache Information (Type 7). One structure is specified for each cache device. l1-i-cache-size, l1-d-cache-size, l2-cache-size, l3-cache-size correspond to "Maximum Cache Size" and "Installed Size" of each cache structure separately. Maximum Cache Size and Installed Size have the same value.

5. [DDR] corresponds to Memory Device (Type 17) structure. type, data-rate, rank are members of the structure.

6. [mac-address] contains the MAC address of two NICs on the board. mac0 is the mac address for NIC0, which is a 1Gbps NIC, and mac1 is the mac address for NIC1, which is a 100Gbps NIC.

Notice: There are other Key-Value pairs that are not listed in the table above. They are not mandatory, and they have no effect on the boot process for now.

4. How to Update ``conf.ini`` in SPI Nor Flash 1
================================================

``conf.ini``, as introduced above, is the configuration file that contains board information for SG2044.
Reference code location is mentioned above, under the title **Source Code Location**. You can modify the file as needed.

To update the ``conf.ini``, you need to use an SD card which can be used to boot the SG2044 board.

1. Put the new ``conf.ini`` into media devices like SD card, USB flash drive, NVMe SSD etc.

2. Use the SD card to boot the SG2044 board.

3. In EDK II UEFI boot process, strike hotkey F2 to enter UEFI Setup Menu.

4. Select "Firmware Management" -> "Update CONF.INI" -> Choose the Media Device -> Choose the File Location -> Confirm.
   Then system will update ``conf.ini`` in SPI Nor Flash 1.

5. Reboot.
