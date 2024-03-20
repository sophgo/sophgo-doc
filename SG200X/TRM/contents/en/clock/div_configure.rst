CLK_DIV clock division configuration
------------------------------------

Main clock frequency division resource table. The following table indicates the configurable clock source and default clock frequency and frequency division for each clock. The software can switch the clock source from XTAL to PLL after booting and adjust the clock frequency division configuration.

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