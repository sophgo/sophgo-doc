IP/Subsystem clock configuration
--------------------------------

:ref:`table_clk_div_default_params` lists all IP/Subsystem clocks and related information in the system. The following is an introduction to IP/Subsystem clock related information based on this table.

- "CLK_NAME" is the clock name of the IP/Subsystem clock.

- Each IP/Subsystem clock can be switched on and off via registers (Gate function). The specific settings are controlled by the registers clk_en_0, clk_en_1, clk_en_2, clk_en_3 and clk_en_4. Each bit controls a clock. See :ref:`table_clk_en_0`, :ref:`table_clk_en_1`, :ref:`table_clk_en_2`, :ref:`table_clk_en_3` and :ref:`table_clk_en_4`.

- The "DIV" column identifies whether the clock supports frequency division (Divide function), "Y" indicates support, and empty indicates not support. Each clock that supports frequency division has a corresponding DIV register for setting the division factor (Divider Factor). For example, clk_tpu corresponds to the [20:16] bit field of div_clk_tpu.

- If a clock supports frequency division, there may be multiple parent clocks (PLL clock or xtal) as clock sources for frequency division. These parent clocks are divided into two groups, DIV_IN0 and DIV_IN1, which correspond to "DIV_IN0" column and the "DIV_IN1" column on the table respectively. Each group contains one or more Sources. We can select the Source through the clk_src bit field of the DIV register corresponding to the clock. Most clocks that support frequency division only need one set of Source, namely DIV_IN0. A small number of clocks have two sets of Sources, including clk_a53, clk_c906_0 and clk_c906_1. If a clock has two sets of Sources, then the clock has two corresponding DIV registers. For example, clk_a53 corresponds to div_clk_a53_0 and div_clk_a53_1. We can select groups DIV_IN0 and DIV_IN1 through register clk_sel_0, the default is DIV_IN1 (Reset). The "PLL SRC/DIV/FREQ" column gives the "Parent Clock"/"Division Factor"/"Frequency Value" selected by default for this clock. The software can switch the clock source from XTAL to PLL after Boot, and adjust the clock frequency division configuration.

- The "XTAL" column identifies whether the clock supports bypassing its parent clock to xtal. "Y" indicates support, and empty indicates not support. The specific settings are controlled by the registers clk_byp_0 and clk_byp_1, see :ref:`table_clk_byp_0` and :ref:`table_clk_byp_1`.

.. include:: ../../contents-share/clock/clksource_preset_freq_div_param.table.rst

IP/SYS clock source and clock division configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Turn off the IP clock; if the clock cannot be turned off, you should first configure it to a stable frequency division clock

    #. CPU frequency conversion: configure clk_sel_0 to choose to switch to SRC1 to avoid too low frequency

    #. IP frequency conversion: configure clk_byp_0/1 to switch the clock to XTAL

2. Configure the clock source and divider configuration to be adjusted

3. The frequency divider register [3] needs to be configured for this clock divider configuration to take effect.

4. Select the clock source to the configured clock divider

MCLK0/MCLK1
~~~~~~~~~~~

1. MCLK0/MCLK1 provides the external sensor reference clock.

2. Configure CAM0PLL, clk_cam0_src_div and clk_cam0_src_div to provide the appropriate MCLK0/MCLK1 output frequency.

Clk_A24M
~~~~~~~~

1. clk_a24m can be used as audio clock under acceptable performance conditions.

2. Output the required audio clock source by configuring apll_frac_div_ctrl, apll_frac_div_m and apll_frac_div_n.

3. The frequency of clk_a24m is 900MHz \* N/M/2.