.. _table_pll_configure:
.. table:: PLL Configuration Parameters
	:widths: 1 2 2 1 1

	+----------+---------------+-------------------+------------+-----------+
	| PLL      | Configuration | Power-down        | Preset     | PLL       |
	|          | Register      | Control Register  | Frequency  | Type      |
	+==========+===============+===================+============+===========+
	| FPLL     | fpll_csr      | fpll_pwd (default | 1500MHz    |Integer    |
	|          |               | On)               |            |frequency  |
	|          |               |                   |            |multiplier |
	+----------+---------------+-------------------+------------+-----------+
	| MIPIMPLL | mipimpll_csr  | mipimpll_pwd      | 900MHz     |Integer    |
	|          |               | (default On)      |            |frequency  |
	|          |               |                   |            |multiplier |
	+----------+---------------+-------------------+------------+-----------+
	| MPLL     | mpll_csr      | mpll_pwd (default | 1000MHz    |Integer\   |
	|          | mpll\         | On)               |            |/fractional|
	|          | _ssc_syn_ctrl |                   |            |frequency  |
	|          |               |                   |            |multiplier |
	|          | mpll\         |                   |            |           |
	|          | _ssc_syn_set  |                   |            |           |
	|          |               |                   |            |           |
	|          | mpll\         |                   |            |           |
	|          | _ssc_syn_span |                   |            |           |
	|          |               |                   |            |           |
	|          | mpll\         |                   |            |           |
	|          | _ssc_syn_setp |                   |            |           |
	+----------+---------------+-------------------+------------+-----------+
	| TPLL     | tpll_csr      | tpll_pwd (default | 1400MHz    |Integer\   |
	|          | tpll\         | On)               |            |/fractional|
	|          | _ssc_syn_ctrl |                   |            |frequency  |
	|          |               |                   |            |multiplier |
	|          | tpll\         |                   |            |           |
	|          | _ssc_syn_set  |                   |            |           |
	|          |               |                   |            |           |
	|          | tpll\         |                   |            |           |
	|          | _ssc_syn_span |                   |            |           |
	|          |               |                   |            |           |
	|          | tpll\         |                   |            |           |
	|          | _ssc_syn_setp |                   |            |           |
	+----------+---------------+-------------------+------------+-----------+
	| APLL     | apll_csr      | apll_pwd(default  | 1050MHz    |Integer\   |
	|          | apll\         | On)               |            |/fractional|
	|          | _ssc_syn_ctrl |                   |            |frequency  |
	|          |               |                   |            |multiplier |
	|          | apll\         |                   |            |           |
	|          | _ssc_syn_set  |                   |            |           |
	|          |               |                   |            |           |
	|          | apll\         |                   |            |           |
	|          | _ssc_syn_span |                   |            |           |
	|          |               |                   |            |           |
	|          | apll\         |                   |            |           |
	|          | _ssc_syn_setp |                   |            |           |
	+----------+---------------+-------------------+------------+-----------+
	| CAM0PLL  | cam0pll_csr   | cam0pll_pwd       | 1050MHz    |Integer\   |
	|          | cam0pll\      | (default On)      |            |/fractional|
	|          | _ssc_syn_ctrl |                   |            |frequency  |
	|          |               |                   |            |multiplier |
	|          | cam0pll\      |                   |            |           |
	|          | _ssc_syn_set  |                   |            |           |
	|          |               |                   |            |           |
	|          | cam0pll\      |                   |            |           |
	|          | _ssc_syn_span |                   |            |           |
	|          |               |                   |            |           |
	|          | cam0pll\      |                   |            |           |
	|          | _ssc_syn_setp |                   |            |           |
	+----------+---------------+-------------------+------------+-----------+
	| CAM1PLL  | cam1pll_csr   | cam1pll_pwd       | 1025MHz    |Integer\   |
	|          | cam1pll\      | (default On)      |            |/fractional|
	|          | _ssc_syn_ctrl |                   |            |frequency  |
	|          |               |                   |            |multiplier |
	|          | cam1pll\      |                   |            |           |
	|          | _ssc_syn_set  |                   |            |           |
	|          |               |                   |            |           |
	|          | cam1pll\      |                   |            |           |
	|          | _ssc_syn_span |                   |            |           |
	|          |               |                   |            |           |
	|          | cam1pll\      |                   |            |           |
	|          | _ssc_syn_setp |                   |            |           |
	+----------+---------------+-------------------+------------+-----------+
	| DISPPLL  | disppll_csr   | disppll_pwd       | 1200MHz    |Integer\   |
	|          | disppll\      | (default On)      |            |/fractional|
	|          | _ssc_syn_ctrl |                   |            |frequency  |
	|          |               |                   |            |multiplier |
	|          | disppll\      |                   |            |           |
	|          | _ssc_syn_set  |                   |            |           |
	|          |               |                   |            |           |
	|          | disppll\      |                   |            |           |
	|          | _ssc_syn_span |                   |            |           |
	|          |               |                   |            |           |
	|          | disppll\      |                   |            |           |
	|          | _ssc_syn_setp |                   |            |           |
	+----------+---------------+-------------------+------------+-----------+
