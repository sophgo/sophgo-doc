Efuse Controller
----------------

The chip integrates 4Kbit eFuse space, and uses Efuse Ctrl to program and read Efuse.

The main functions of Efuse Ctrl include:

- Provides a dual eFuse bit (Double bit) protection mechanism, which consists of two physical eFuse bits forming a single bit logical effective value, which is equivalent to providing a 2Kbit register space to improve the robustness of eFuse programming or data maintenance.

- After power-on reset (Power-On-Reset), the contents of efuse are automatically loaded into the register to provide the required configuration settings for the chip system and reduce the number of times required to read Efuse to increase the service life.

- Provides efuse programming, reading, verification reading and power-on and power-off instructions and content security protection mechanism.

The Efuse data register is divided into two areas, one is a non-safe area and the other is a safe area. The data in the non-safe area is allowed to be accessed by all modules, and the safe area only allows access to the safe modules. The non-secure area stores system configuration and public information, and the secure area stores security configuration, keys and passwords.

.. _diagram_efuse_block:
.. figure:: ../../../../media/image147.png
	:align: center

	eFuse CTRL modular architecture

