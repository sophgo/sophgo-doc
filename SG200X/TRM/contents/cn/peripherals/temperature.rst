温度传感器
----------

概述
~~~~

由于芯片结温过高可能引发 thermal run-away 造成永久性伤害. 所以芯片需要作温度的控制。

第一阶段是软件行为。温度感测器可以定时自动侦测温度是否超过特定温度而发出过热的中断. 软件接受到过热中断后, 再藉由限制大功耗模块的频率或电压, 启动风扇等方式达到降低功耗和温度的目的。若温度回到安全范围，则把限制解除。

第二阶段是硬体行为。若软件介后温度仍然持续上升，则硬件会介入作 thermal shut-down 的紧急应变。但这个功能预设是关掉的，需要软件开机后就设定好相关设定后使能。

本芯片内建两温度感测器, 可以由 CPU 周期性监控芯片温度。可以在芯片过热无响应时触发电源管理模块进行系统关机重置以避免过热之危险。

工作方式
~~~~~~~~

- 单次量测时间配置: reg_tempsen_accsel = 1 (1024T) 配置状况下，单次量测时间所需为 (1/(25M/12)*(1024+2+64) ~ 523.2us。

- 周期量测时间配置: reg_tempsen_auto_prediv 预设为 24, 使得 reg_tempsen_auto_cycle 每单位为 1us 。 两次量测时间之周期需配置 reg_tempsen_auto_cycle 大于 524。 例如每秒量测一次则配置 reg_tempsen_auto_cycle = 1000000。

- 量测通道配置: 若配置 reg_tempsen_sel = 3, 则每次触发两个温度感测器同时量测。

- 配置高低温监控温度: 配置触发高温警报、低温回复之温度 tempsen_chx_temp_th。

- 配置中断。

- 使能温度感测器进行量测: 配置 reg_tempsen_en = 1 进行量测，等待中断。

.. include:: ./temperature_interrupt_description.table.rst

.. _diagram_temperature_measure:
.. figure:: ../../../../media/image132.png
	:align: center

	温度量测时间、计数与中断发生关系图

- 检视温度量测结果: sta_tempsen_chX_result 记载前一次完成之温度量测结果，sta_tempsen_chX_max_result 记载曾经量测到的温度最大值，tempsen_chX_temp_th_cnt 记载连续高温低温次数。

- 配置过热保护之温度 reg_tempsen_overheat_th、过热复位请求倒数时间 reg_tempsen_overheat_cycle 并使能 reg_overheat_reset_en。

再参照 RTC 寄存器章节，配置 RTC 寄存器 hw_thm_shdn_en、 RTC_EN_THM_SHDN、RTC_THM_SHDN_AUTO_REBOOT 使能过热触发下电或重启。在发生过热时，tempsensor controller 会先发出中断并开始倒数，sta_tempsen_overheat_countdown 等于 1 时，后触发 RTC 的下电保护请求。若在此之前软件有介入并进行温控后可以配置 reg_overheat_reset_clr 清除倒数，但在下次量测结果依然过热时，过热保护中断依然会再次触发与倒数。

Temperature sensor 寄存器概览
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ./temperature_registers_overview.table.rst

Temperature sensor 寄存器描述
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ./temperature_registers_description.table.rst
