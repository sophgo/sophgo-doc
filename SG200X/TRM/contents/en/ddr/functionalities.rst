Function Description
--------------------

Application Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

The DRAM interface supports 16-bit data width and 32-bit data width. :ref:`diagram_soc_dram_interconnect` is the interconnection diagram between the main chip and the single-chip DRAM device:

.. _diagram_soc_dram_interconnect:
.. figure:: ../../../../media/image16.png
	:align: center

	SoC/DRAM interconnection diagram

Command is consists of several signals, which vary depending on the DRAM type. Table :ref:`table_ddr2_vs_ddr3` compares command signals for DDR2 and DDR3:

.. include:: ../../contents-share/ddr/ddr2_vs_ddr3.table.rst

Functional Principle
~~~~~~~~~~~~~~~~~~~~

Based on the storage characteristics of DRAM, JEDEC developed a set of standards that specify the commands and timing required to access DRAM data and control DRAM status. By properly configuring the DDR register, the DDR controller can issue timing sequences that meet JEDEC standards to complete actions such as reading, writing, and low-power control.

Command Truth Table
^^^^^^^^^^^^^^^^^^^

The DDR interface timing meets the JDEDC standard. Following are table :ref:`table_ddr2_command_truth_table` and table :ref:`table_ddr3_command_truth_table`. They are the truth tables of DDR2 and DDR3 support commands for user reference. The rest of the information can refer to the JEDEC standard.

.. include:: ../../contents-share/ddr/ddr_command_truth_table.table.rst

Auto Refresh
^^^^^^^^^^^^

The DDR controller has the ability to control the automatic refresh function. The purpose of controlling automatic refresh is to reduce the delay in accessing data or reduce the impact of refresh commands on DRAM bandwidth. Try to send refresh commands when the DRAM is idle. The specific available methods are:

- Refresh at equal intervals: Send a refresh command every tREFI time.

- Tricky refresh: The DDR controller internally counts the number of expired tREFIs, and then uses idle time to continuously send them.

Low Power Management
^^^^^^^^^^^^^^^^^^^^

DDR controller supports low power modes:

- Normal low-power mode: Set an idle time through the register. When the normal low-power mode is enabled and the DDR controller meets the idle time, it automatically controls the DRAM to enter the normal low-power mode.

- Self-refresh mode: Self-refresh is a mode with lower power consumption. An idle time is set through the register. When the self-refresh mode is enabled and the DDR controller meets the idle time, it automatically controls the DRAM to enter the self-refresh mode.

Arbitration Mechanism
^^^^^^^^^^^^^^^^^^^^^

The DDR controller mainly optimizes the bandwidth usage of the system based on various DRAM control timings, and schedules each command through a priority scheduling algorithm. In addition, DDRC also implements two scheduling auxiliary means, timeout control and real-time control (these two control means are enabled according to business needs, and can be enabled at the same time or separately) to control command requests. .

- Consecutive address access restrictions

  The limit level is: 0 ~ 15 DRAM read/write instructions, and the configuration of each AXI port is independent. The DDR controller has high priority for contiguous addresses by default to optimize DRAM utilization. This mechanism limits the maximum length of contiguous DRAM that can be accessed by each AXI port.

- Priority scheduling

  The priority level is: 0 ~ 15. The higher the value, the higher the priority. The read/write priority configuration of each AXI port is independent.

- Timeout control

  For read/write transfers of each AXI port, the timeout register can be configured to avoid too long waiting. After the waiting time is reached, AXI ports that have not yet reached the waiting time or that have not been configured with the timeout attribute are forcibly blocked.

- Real-time control

  For real-time functions, the hardware buffering threshold can be configured. If the buffering is insufficient, the priority will be automatically raised to the highest level, and other AXI ports can be restricted from generating new transmissions.

Traffic Statistics and Command-latency Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The DDR controller supports traffic statistics function: it can count the read and write traffic of each AXI port to collect current traffic information to determine whether flow control is required. Statistics of overall DRAM read/write traffic can be collected.

The DDR controller supports the AXI latency statistics function and supports cumulative latency statistics for specified/unspecified transmissions.

Address Mapping Method
^^^^^^^^^^^^^^^^^^^^^^

The DDR controller converts the access address of the system bus into the access address of the DRAM. Can implement RBC (row_bank_column), BRC, and support bank interleave in row/column bit.