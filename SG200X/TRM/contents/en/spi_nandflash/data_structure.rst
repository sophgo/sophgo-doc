Data Structure (NAND Flash/SPI NAND Flash)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2KB page_size
^^^^^^^^^^^^^

For a 2KB page_size configuration, the common size of the redundant area available to the software is 64Byte. The structure of data in Buffer and Flash is as follows. The size of the redundant area is related to the actual device used.

.. This table is relatively small, so I don’t put the file include separately.

.. table:: The structure of data in Buffer and Flash (2KB page_size)
	:widths: 1 1 1

	+------------------+--------------------------------+------------------+
	| User Data        | Data(2048)                     | OOB(64)          |
	+------------------+--------------------------------+------------------+


4KB page_size
^^^^^^^^^^^^^

For a 4KB page_size configuration, the common size of the redundant area available to the software is 256Byte. The structure of data in Buffer and Flash is as follows. The size of the redundant area is related to the actual device used.

.. This table is relatively small, so I don’t put the file include separately.

.. table:: The structure of data in Buffer and Flash (4KB page_size)
	:widths: 1 1 1

	+------------------+--------------------------------+------------------+
	| User Data        | Data(4096)                     | OOB(256)         |
	+------------------+--------------------------------+------------------+

