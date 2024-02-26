PLL configuration
-----------------

See :ref:`table_pll_configure`, the chip has 9 built-in PLLs (not counting Analog IP built-in PLL), which are divided into two types of PLL: integer frequency multiplication and fractional frequency multiplication.

.. include:: ../../contents-share/clock/pll_configure_params.table.rst

Integer Multiplier PLL
~~~~~~~~~~~~~~~~~~~~~~

Tuning the integer PLL flow:

1. When adjusting, you must turn off the clock related to this PLL or select the clock source as XTAL or other PLL.

2. Configure the \*_pll_csr register according to the integer PLL parameter table

3. Clear \*_pll_pwd

.. include:: ../../contents-share/clock/pll_configure_integer_params.table.rst

Fractional Multiplier PLL
~~~~~~~~~~~~~~~~~~~~~~~~~

Adjust fractional PLL process:

1. When using this PLL, the IP clock must be turned off or XTAL or other stable clock sources must be selected.

2. Configure \*_ssc_syn_src_en to enable the synthesizer clock

3. Configure \*_ssc_syn_set according to PLL frequency requirements,

4. Toggle \*_ssc_syn_up to make the configuration take effect

5. Configure the \*_pll_csr register according to the integer PLL parameter table

6. Clear \*_pll_pwd

.. include:: ../../contents-share/clock/pll_configure_fractional_params.table.rst
