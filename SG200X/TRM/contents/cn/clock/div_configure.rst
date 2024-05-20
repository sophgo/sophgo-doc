IP/子系统时钟配置
-----------------

:ref:`table_clk_div_default_params` 列出了系统所有 IP/子系统时钟以及相关信息，下面结合该表介绍 IP/子系统时钟的相关信息。

- “CLK_NAME” 是 IP/子系统时钟的时钟名称。

- 每一个 IP/子系统时钟都可以通过寄存器控制其开关(Gate 功能)。具体的设置由寄存器 clk_en_0, clk_en_1, clk_en_2, clk_en_3 和 clk_en_4 控制，每一个 bit 位控制一个时钟。参考 :ref:`table_clk_en_0`, :ref:`table_clk_en_1`, :ref:`table_clk_en_2`, :ref:`table_clk_en_3` 和 :ref:`table_clk_en_4`。

- “DIV” 列标识了该时钟是否支持分频(Divide 功能), “Y” 表示支持，空表示不支持。每个支持分频的时钟都有一个对应的 DIV 寄存器用于设置分频系数(Divider Factor)。譬如针对 clk_tpu 对应有 div_clk_tpu 的 [20:16] 位域。

- 如果一个时钟支持分频，则可能存在多个父时钟(PLL 时钟或者 xtal)作为分频的时钟来源(Source)，这些父时钟分为两组 DIV_IN0 和 DIV_IN1, 分别对应表上的 “DIV_IN0” 列和 “DIV_IN1” 列。每个组中又包含一个或者多个 Soruce, 我们可以通过该时钟对应的 DIV 寄存器的 clk_src 位域来选择 Source。大部分支持分频的时钟只需要一组 Source, 即 DIV_IN0。少部分时钟有两组 Source, 这些时钟包括 clk_a53, clk_c906_0 和 clk_c906_1。如果一个时钟有两组 Source, 那么相应地该时钟就有两个对应的 DIV 寄存器，譬如 clk_a53 对应有 div_clk_a53_0 和 div_clk_a53_1。我们可以通过寄存器 clk_sel_0 来选择组 DIV_IN0 和 DIV_IN1, 默认情况(Reset)下是 DIV_IN1。“PLL SRC/DIV/FREQ” 列给出了默认情况下该时钟选择的 “父时钟”/“分频系数”/“频率值”。软件可以在 Boot 之后将时钟源由 XTAL 切换到 PLL, 并进行时钟分频配置调整。

- “XTAL” 列标识了该时钟是否支持将其父时钟 bypass 到 xtal 上， “Y” 表示支持，空表示不支持。具体设置由寄存器 clk_byp_0 和 clk_byp_1 控制，参考 :ref:`table_clk_byp_0` 和 :ref:`table_clk_byp_1`。

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
