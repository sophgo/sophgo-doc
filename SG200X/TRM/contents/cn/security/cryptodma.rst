CryptoDMA
---------

概述
~~~~

CryptoDMA 为实现对称密钥算法、杂凑算法及 BASE64 转换的硬体加速器，支持对称算法: AES 128/192/256, DES/TDES, SM4 及杂凑算法: SHA-1/SHA256 等密码运算。通过链表 (linked-list) 的指令串达到资料区块的密钥加解密或杂凑运算功能的直接记忆体存取。

- 对称算法适用于进行数据的硬体加解密加速处理，同时支持多种分组加密及区块串联处理方式，包括 ECB, CBC, CTR。

- AES (Advanced Encryption Standard) 算法的实现符合 FIPS 197 标准。DES (Data Encryption Standard)/TDES 算法的实现符合 ISO/IEC 18033-3。

- 杂凑算法适用于进行于数据完整性查验和数字签名运算加速。SHA1 及 SHA256，符合 FIPS180-2 标准。

- BASE64 运算适用于处理文字资料内，储存二迈位资料，如 MIME 电子邮件或 URL 资料。

功能特性
~~~~~~~~

CryptoDMA 模块有如下功能特性：

- 支持对称加解密算法 AES 及分组加密模式 ECB/CBC/CTR。密钥长度支持 128 位、256 位，密钥可由安全作业系统或链表指令配置。

- 支持对称加解密算法 SM4 及分组加密模式 ECB/CBC/CTR。

- 支持对称加解密算法 DES/TDES 及分组加密模式 ECB/CBC/CTR。

- 支持哈希算法 SHA1、SHA256。

- 支持 CPU 配置输入 PIO 数据和 DMA 方式读取縺表指令输入数据。

- 支持循环链表结构，支持拼接多个链表数据。

- 提供中断状态查询、中断屏蔽和中断清除功能。

DMA 功能描述
~~~~~~~~~~~~

CryptoDMA 提供记忆体直接存取 DMA 功能，应用程式只需对目标资料区块提供链表指令，启动 CryptoDMA DMA功能，直到收到完成的中断通知，区块加解密或哈希运算即表示结束，并将运算结果输出至目标地址。

对称密钥算法分组加密模式功能描述
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

对称密钥算法 AES/DES/SM4 皆支持 ECB/CBC/CTR 分组加密模式。

ECB 模式
^^^^^^^^

ECB（Electronic CodeBook）模式中，加、解密算法是直接由各个分组的运算直接应用到各个分组数据。这个特点使得明文的加密和密文的解密可以由区块资料任一分组独立进行。

.. _diagram_ecb_mode:
.. figure:: ../../../../media/image144.png
	:align: center

	ECB 模式

CBC 模式
^^^^^^^^

CBC (Cipher Block Chaining)，将输入明文分组先与输入向量 IV (Intialization Vector) 或前一分组密文结果进行异或运算，才进行加密运算，CBC 模式下的加密操作是必须从第一笔区块资料分组开始进行，之后加密运算皆需要前一分组所得密文来进行加密。解密时可由当前密文解密后及前一组密文异或运算后得到明文。

.. _diagram_cbc_mode:
.. figure:: ../../../../media/image145.png
	:align: center

	CBC 模式

CTR 模式
^^^^^^^^

CTR (Counter) 是利用加密或解密一组不同的数列来保证加密数据处理的独立性及安全性，一般是采用加密累加数列后和明文进行异或运算。

.. _diagram_ctr_mode:
.. figure:: ../../../../media/image146.png
	:align: center

	CTR 模式

CryptoDMA 寄存器概览
~~~~~~~~~~~~~~~~~~~~

.. include:: ./cryptodma_registers_overview.table.rst

CryptoDMA 寄存器描述
~~~~~~~~~~~~~~~~~~~~

(基址 0x02060000)

.. include:: ./cryptodma_registers_description.table.rst
