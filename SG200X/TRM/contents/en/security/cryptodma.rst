CryptoDMA
---------

Overview
~~~~~~~~

CryptoDMA is a hardware accelerator that implements symmetric key algorithms, hash algorithms and BASE64 conversion. It supports symmetric algorithms: AES 128/192/256, DES/TDES, SM4 and hash algorithms: SHA-1/SHA256 and other cryptographic operations. Direct memory access of key encryption and decryption or hash operation functions of data blocks is achieved through linked-list command strings.

- The symmetric algorithm is suitable for accelerated hardware encryption and decryption of data, and supports a variety of group encryption and block concatenation processing methods, including ECB, CBC, and CTR.

- The implementation of the AES (Advanced Encryption Standard) algorithm complies with the FIPS 197 standard. The implementation of the DES (Data Encryption Standard)/TDES algorithm complies with ISO/IEC 18033-3.

- The hash algorithm is suitable for data integrity checking and digital signature operation acceleration. SHA1 and SHA256, compliant with FIPS180-2 standard.

- BASE64 operations are suitable for processing text data and storing 2-bit data, such as MIME email or URL data.

Features
~~~~~~~~

The CryptoDMA module has the following functional features:

- Supports symmetric encryption and decryption algorithm AES and block encryption mode ECB/CBC/CTR. The key length supports 128 bits and 256 bits, and the key can be configured by the secure operating system or linked list instructions.

- Supports symmetric encryption and decryption algorithm SM4 and block encryption mode ECB/CBC/CTR.

- Supports symmetric encryption and decryption algorithms DES/TDES and block encryption modes ECB/CBC/CTR.

- Supports hash algorithms SHA1, SHA256.

- Supports CPU configuration input PIO data and DMA method to read table command input data.

- Supports circular linked list structure and supports splicing of multiple linked list data.

- Provides interrupt status query, interrupt masking and interrupt clearing functions.

DMA Function Description
~~~~~~~~~~~~~~~~~~~~~~~~

CryptoDMA provides memory direct access DMA function. The application only needs to provide a linked list instruction to the target data block to start the CryptoDMA DMA function. Until the completed interrupt notification is received, the block encryption, decryption or hash operation is completed and the The operation result is output to the target address.

Symmetric key algorithm block encryption mode function description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Symmetric key algorithms AES/DES/SM4 all support ECB/CBC/CTR block encryption mode.

ECB Mode
^^^^^^^^

In ECB (Electronic CodeBook) mode, the encryption and decryption algorithms are directly applied to each grouped data by the operation of each group. This feature allows plaintext encryption and ciphertext decryption to be performed independently for any group of block data.

.. _diagram_ecb_mode:
.. figure:: ../../../../media/image144.png
	:align: center

	ECB mode

CBC Mode
^^^^^^^^

CBC (Cipher Block Chaining), the input plaintext group is first XORed with the input vector IV (Intialization Vector) or the previous group ciphertext result, and then the encryption operation is performed. The encryption operation in CBC mode must start from the first block. Block data grouping begins, and subsequent encryption operations require the ciphertext obtained from the previous group for encryption. During decryption, the plaintext can be obtained by decrypting the current ciphertext and XORing the previous set of ciphertexts.

.. _diagram_cbc_mode:
.. figure:: ../../../../media/image145.png
	:align: center

	CBC mode

CTR Mode
^^^^^^^^

CTR (Counter) uses encryption or decryption to encrypt or decrypt a set of different arrays to ensure the independence and security of encrypted data processing. It generally uses an encrypted accumulation array and then performs an XOR operation with the plain text.

.. _diagram_ctr_mode:
.. figure:: ../../../../media/image146.png
	:align: center

	CTR mode

CryptoDMA Register Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/security/cryptodma_registers_overview.table.rst

CryptoDMA Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(Base address: 0x02060000)

.. include:: ../../contents-share/security/cryptodma_registers_description.table.rst
