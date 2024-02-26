功能描述 
--------

应用框图
~~~~~~~~

DRAM 接口支持 16 比特数据位宽, 32 比特位宽。:ref:`diagram_soc_dram_interconnect` 为主芯片与单片 DRAM 器件的互联示意图：

.. _diagram_soc_dram_interconnect:
.. figure:: ../../../../media/image16.png
	:align: center

	SoC/DRAM 互联示意图

Command 由数个信号组成, 依 DRAM 型别会有所差异, 表格 :ref:`table_ddr2_vs_ddr3` 对 DDR2 / DDR3 命令信号做个比较：

.. include:: ./ddr2_vs_ddr3.table.rst

功能原理
~~~~~~~~

基于 DRAM 的存储特性, JEDEC 制定一套标准，标准规范了访问 DRAM 数据及控制 DRAM 状态所需的命令及时序。适当的配置 DDR 寄存器, DDR 控制器就能发出满足 JEDEC 标准的时序，完成读、写及低耗电控制等动作。

命令真值表
^^^^^^^^^^

DDR 接口时序满足 JDEDC 标准，表格 :ref:`table_ddr2_command_truth_table` 及表格 :ref:`table_ddr3_command_truth_table`。分别为 DDR2 及 DDR3 支持命令的真值表，供用户参考，其余信息可参照 JEDEC 标准。

.. include:: ./ddr_command_truth_table.table.rst

自动刷新
^^^^^^^^

DDR 控制器具备控制自动刷新功能的能力，控制自动刷新的目为减少访问数据的延迟或是减少刷新命令对 DRAM 带宽的冲击，尽量在 DRAM 空闲时发刷新命令，具体可用手段有：

-  等间隔刷新：每间‎隔 tREFI 时间就发刷新命令。

-  取巧式刷新: DDR 控制器内部会统计 tREFI 过期数目，再利用空闲时间连续发。

低功耗管理
^^^^^^^^^^

DDR控制器支持低功耗模式:

-  普通低功耗模式：通过寄存器设定一空闲时间，当普通低功耗模式使能后，且 DDR 控制器满足空闲时间，自动控制 DRAM 进入普通低耗模式。

-  自刷新模式：自刷新为一功耗更低的模式，通过寄存器设定一空闲时间，当自刷新模式使能后，且 DDR 控制器满足空闲时间，自动控制 DRAM 进入自刷新模式。

仲裁机制
^^^^^^^^

DDR 控制器主要依据 DRAM 各项控制时序优化系统的带宽使用率，另通过优先级调度算法对各命令进行调度。另外，DDRC 还实现了 timeout 控制、real-time 控制这两种调度辅助手段（根据业务需要来使能这两种控制手段，可以同时使能，也可以单独使能），对命令的请求进行控制。

- 连续地址访问限制

  限制级数为: 0 ~ 15 个 DRAM 读/写指令，每个 AXI 端口的配置是独立的。DDR 控制器默认对连续地址有高优先权，以优化 DRAM 利用率，此机制限制每个 AXI 埠最大可连续存取 DRAM 的长度。

- 优先级调度

  优先级等级为: 0 ~ 15, 数值越高表示优先权越高，每个 AXI 埠的读/写优先级配置是独立的。

- Timeout 控制

  对于每个 AXI 埠的读/写传输，可配置 timeout 寄存器以避免过长时间的等待，在等待时间到达后，强制屏蔽尚未到达等待时间、或未配置 timeout 属性的 AXI 端口。

- Real-time 控制

  对于 real-time function, 可配置硬件缓冲阀值，若缓冲不足时自动提高优先级至最高，并可限制其他 AXI 埠生成新的传输。

流量统计和命令 latency 统计功能
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DDR 控制器支持流量统计功能：可以统计各 AXI 埠读写流量，用以收集当前流量信息以决定是否需要进行流量控制。可以统计 DRAM 总体读/写流量统计。

DDR 控制器支持 AXI latency 统计功能，支持指定/不指定传输的累积 latency 统计。

地址映射方式
^^^^^^^^^^^^

DDR 控制器实现了将系统总线的访问地址转换为 DRAM 的访问地址。可实现 RBC (row_bank_column)、BRC, 并支持 Bank interleave 在 row/column bit。
