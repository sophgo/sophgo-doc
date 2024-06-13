SARADC
------

概述
~~~~

SARADC 为模拟信号数字转换控制器。本芯片有最多 2 个 SARADC 控制器，一个在 Active Domain 下，一个在 No-die Domain 下，每个提供 3 个独立通道。

.. only:: sg2002

	**注意：** 芯片并没有在管脚上为 Active Domain 下的控制器引出所有的 ADC 通道，具体参考 :ref:`table_inf_signal_pin_fmux_adc_sg2002`。

特点
~~~~

- 控制器工作频率 12.5MHz;

- 扫描频率不能高于 320K/s;

- 每个控制器提供 3 个独立通道;

- 12bit 采样精度;

- 可一次触发三个信道依序扫描；

- 扫描完成自动上报中断;

工作方式
~~~~~~~~

CPU 配置扫描信道，每个 SARADC 控制器可同时配置 3 个信道，启动 SARADC 进行通道扫描。通道扫描完成所有使能通道后, 通过中断通知系统扫描完成, CPU 可以获取转换结果。

系统上电后，为确保 SARADC 测量精度，建议对芯片的 SARADC 模块进行校准。校准通过离线方式执行，具体方法是先设置 saradc_test.reg_saradc_vrefsel 为 external 方式，然后手动反复调整 saradc_trim.reg_saradc_trim, 直至实际读出采样值经换算后与外部参考电压值比较接近至满足精度要求。校准完成后将 saradc_trim.reg_saradc_trim 的值记录下来，每次上电时通过软件设置 saradc_test.reg_saradc_vrefsel 为 external 方式后再将该记录的值设置到 saradc_trim.reg_saradc_trim 即可。

.. _section_saradc_register_overview:

SARADC 寄存器概览
~~~~~~~~~~~~~~~~~

Active Domain 下 1 组，Base address：0x030F0000

No-die Domain 下 1 组（RTCSYS_SARADC），Base address：0x0502C000

每组寄存器定义相同，以 RTCSYS_SARADC 为例：

.. 该表格较小，不再文件 include

.. _table_rtcsys_saradc:
.. table:: Base address 0x0502C000
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| saradc_ctrl          | 0x004   | control register                   |
	+----------------------+---------+------------------------------------+
	| saradc_status        | 0x008   | status register                    |
	+----------------------+---------+------------------------------------+
	| saradc_cyc_set       | 0x00c   | saradc waveform setting register   |
	+----------------------+---------+------------------------------------+
	| saradc_ch1_result    | 0x014   | channel 1 result register          |
	+----------------------+---------+------------------------------------+
	| saradc_ch2_result    | 0x018   | channel 2 result register          |
	+----------------------+---------+------------------------------------+
	| saradc_ch3_result    | 0x01c   | channel 3 result register          |
	+----------------------+---------+------------------------------------+
	| saradc_intr_en       | 0x020   | interrupt enable register          |
	+----------------------+---------+------------------------------------+
	| saradc_intr_clr      | 0x024   | interrupt clear register           |
	+----------------------+---------+------------------------------------+
	| saradc_intr_sta      | 0x028   | interrupt status register          |
	+----------------------+---------+------------------------------------+
	| saradc_intr_raw      | 0x02c   | interrupt raw status register      |
	+----------------------+---------+------------------------------------+
	| saradc_test          | 0x030   | test register                      |
	+----------------------+---------+------------------------------------+
	| saradc_trim          | 0x034   | trim register                      |
	+----------------------+---------+------------------------------------+

SARADC 寄存器描述
~~~~~~~~~~~~~~~~~

.. include:: ./saradc_registers_description.table.rst
