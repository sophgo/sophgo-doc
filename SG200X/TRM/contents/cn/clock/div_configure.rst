CLK_DIV 时钟分频配置
--------------------

主要时钟分频资源表, 下表标示各时钟所可以配置之时钟源与预设之时钟频率及分频。软件可以在 Boot 之后将时钟源由 XTAL 切换到PLL，并进行时钟分频配置调整。

.. include:: ./clksource_preset_freq_div_param.table.rst

IP/SYS 时钟源、时钟分频配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 关闭IP时钟；若不能关闭的时钟，应先配置到稳定分频时钟

   #. CPU变频: 配置 clk_sel_0 选择切换至 SRC1 , 避免频率太低

   #. IP变频:配置 clk_byp_0/1 切换时钟至 XTAL

2. 配置要调整之时钟源及分频器配置

3. 需要配置分频器寄存器 [3]，该时钟分频器配置方能生效

4. 将时钟源选择到配置完成之时钟分频器

MCLK0/MCLK1
~~~~~~~~~~~

1. MCLK0/MCLK1 是提供外部 sensor 参考时钟。

2. 通过配置 CAM0PLL、clk_cam0_src_div 及 clk_cam0_src_div 以提供适合的 MCLK0/MCLK1 输出频率。

Clk_A24M
~~~~~~~~

1. 在性能可接受状况可以使用 clk_a24m 作为音频时钟。

2. 通过配置 apll_frac_div_ctrl、apll_frac_div_m 及 apll_frac_div_n 输出需要的音频时钟源。

3. clk_a24m 之频率为 900MHz \* N/M/2。
