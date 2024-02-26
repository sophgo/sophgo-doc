Efuse 控制器
------------

芯片内部集成 4Kbit eFuse 空间，并以 Efuse Ctrl 对 Efuse 进行编程和读取。

Efuse Ctrl 的主要功能包括：

- 提供双 eFuse 位元 (Double bit) 保护机制，由两个实体 eFuse 位元组成单一位元逻辑有效值，等效于提供 2Kbit 寄存器空间，以提高 eFuse 烧写或资料维持的强健性。

- 上电复位后 (Power-On-Reset), 自动加载 efuse 的内容到寄存器，提供芯片系统所需组态设定及减少对 Efuse 所需读取次数提高使用期限。

- 提供 efuse 编程、读取、验证读取及上下电指令及内容安全保护机制。

Efuse 资料寄存器分成两块区域，一块为非安全区域，另一块是安全区域，非安全区域内资料允许所有模块访问，安全区域只允许安全模块访问。非安全区域储存系统组态及公开信息，安全区域储存安全组态、密钥及密码。

.. _diagram_efuse_block:
.. figure:: ../../../../media/image147.png
	:align: center

	eFuse CTRL 模块架构

