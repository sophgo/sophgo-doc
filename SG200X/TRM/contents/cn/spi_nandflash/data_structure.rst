数据结构 (NAND Flash/SPI NAND Flash)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2KB page_size
^^^^^^^^^^^^^

对 2KB page_size 的配置，软件可用的冗余区常见大小为 64Byte。数据在 Buffer 和 Flash 中的结构如下所示。冗余区大小与实际使用器件相关。

.. 这个表比较小，所以就不单独放文件 include 了

.. table:: The structure of data in Buffer and Flash (2KB page_size)
	:widths: 1 1 1

	+------------------+--------------------------------+------------------+
	| User Data        | Data(2048)                     | OOB(64)          |
	+------------------+--------------------------------+------------------+


4KB page_size
^^^^^^^^^^^^^

对 4KB page_size 的配置，软件可用的冗余区常见大小为 256Byte。数据在 Buffer 和 Flash 中的结构如下所示。冗余区大小与实际使用器件相关。

.. 这个表比较小，所以就不单独放文件 include 了

.. table:: The structure of data in Buffer and Flash (4KB page_size)
	:widths: 1 1 1

	+------------------+--------------------------------+------------------+
	| User Data        | Data(4096)                     | OOB(256)         |
	+------------------+--------------------------------+------------------+

