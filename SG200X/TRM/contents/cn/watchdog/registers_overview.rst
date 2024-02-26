.. _section_wdt_register_overview:

WDT 寄存器概览
--------------

WDT 寄存器通过总线存取。包括四个 WDT, 3 个 Active Domain，1 个 No-die Domain。其基地址分别为:

- WDT0 : 0x03010000

- WDT1 : 0x03011000

- WDT2 : 0x03012000

- RTCSYS_WDT : 0x0502D000

每个 WDT 由一组控制寄存器组成，每组定义相同，概览如 :ref:`table_watchdog_register_overview` 所示。

.. include:: ./watchdog_register_overview.table.rst

