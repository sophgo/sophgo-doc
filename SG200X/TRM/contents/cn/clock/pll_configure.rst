PLL 配置
--------

如 :ref:`table_pll_configure` , 芯片内置 9 PLLs (不计入 Analog IP 内建 PLL), 分为整数倍频跟分数倍频两类 PLL。

.. include:: ./pll_configure_params.table.rst

整数倍频 PLL
~~~~~~~~~~~~

调整整数 PLL 流程:

1. 调整时须将相关使用此 PLL 之时钟关闭或是选择时钟源为 XTAL 或其他 PLL

2. 配置 \*_pll_csr 寄存器，按整数 PLL 参数表配置

3. 清除 \*_pll_pwd

.. include:: ./pll_configure_integer_params.table.rst

分数倍频 PLL
~~~~~~~~~~~~

调整分数 PLL 流程:

1. 时须将相关使用此 PLL 之 IP clock 关闭或是选择 XTAL 或其他稳定时钟源

2. 配置 \*_ssc_syn_src_en 以使能 synthesizer 时钟

3. 依据PLL 频率需求配置 \*_ssc_syn_set ,

4. Toggle \*_ssc_syn_up ,使配置生效

5. 配置 \*_pll_csr 寄存器，按整数 PLL 参数表配置

6. 清除 \*_pll_pwd

.. include:: ./pll_configure_fractional_params.table.rst

