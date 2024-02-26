.. _section_wdt_register_overview:

WDT Register Overview
---------------------

The WDT register is accessed via the bus. Includes four WDTs, 3 are Active Domains, and 1 is No-die Domain. Their base addresses are:

- WDT0: 0x03010000

- WDT1: 0x03011000

- WDT2: 0x03012000

- RTCSYS_WDT: 0x0502D000

Each WDT consists of a set of control registers, each set has the same definition, and an overview is shown in :ref:`table_watchdog_register_overview`.

.. include:: ../../contents-share/watchdog/watchdog_register_overview.table.rst

