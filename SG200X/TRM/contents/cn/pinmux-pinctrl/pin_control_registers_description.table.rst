IOBLK_G1_REG_PWM0_BUCK
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g1_reg_pwm0_buck:
.. table:: IOBLK_G1_REG_PWM0_BUCK
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\_\            | 2 | 0x0   | Pull-up resistor enable.    |
	| G1_REG_PWM0_BUCK_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 3 | 0x0   | Pull-down resistor enable.  |
	| G1_REG_PWM0_BUCK_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength       |
	| 1_REG_PWM0_BUCK_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength       |
	| 1_REG_PWM0_BUCK_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger       |
	| 1_REG_PWM0_BUCK_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 9 | 0x0   | Input Schmitt trigger       |
	| 1_REG_PWM0_BUCK_ST1 |   |       | strength control, bit 1     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 1\| 0x0   | Weak level holder (Bus      |
	| G1_REG_PWM0_BUCK_HE | 0 |       | holder) enable. 0=Disabled; |
	|                     |   |       | 1=Enabled                   |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition     |
	| G1_REG_PWM0_BUCK_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G1_REG_ADC1
^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g1_reg_adc1:
.. table:: IOBLK_G1_REG_ADC1
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| I\                  | 2 | 0x0   | Pull-up resistor enable.    |
	| OBLK_G1_REG_ADC1_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| I\                  | 3 | 0x1   | Pull-down resistor enable.  |
	| OBLK_G1_REG_ADC1_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IO\                 | 5 | 0x0   | Output drive strength       |
	| BLK_G1_REG_ADC1_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IO\                 | 6 | 0x1   | Output drive strength       |
	| BLK_G1_REG_ADC1_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IO\                 | 8 | 0x0   | Input Schmitt trigger       |
	| BLK_G1_REG_ADC1_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IO\                 | 9 | 0x0   | Input Schmitt trigger       |
	| BLK_G1_REG_ADC1_ST1 |   |       | strength control, bit 1     |
	+---------------------+---+-------+-----------------------------+
	| I\                  | 1\| 0x0   | Weak level holder (Bus      |
	| OBLK_G1_REG_ADC1_HE | 0 |       | holder) enable. 0=Disabled; |
	|                     |   |       | 1=Enabled                   |
	+---------------------+---+-------+-----------------------------+
	| I\                  | 1\| 0x0   | Output level transition     |
	| OBLK_G1_REG_ADC1_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+
	
IOBLK_G1_REG_PKG_TYPE0
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g1_reg_pkg_type0:
.. table:: IOBLK_G1_REG_PKG_TYPE0
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\_\            | 2 | 0x1   | Pull-up resistor enable.    |
	| G1_REG_PKG_TYPE0_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 3 | 0x0   | Pull-down resistor enable.  |
	| G1_REG_PKG_TYPE0_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength       |
	| 1_REG_PKG_TYPE0_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength       |
	| 1_REG_PKG_TYPE0_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger       |
	| 1_REG_PKG_TYPE0_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 9 | 0x0   | Input Schmitt trigger       |
	| 1_REG_PKG_TYPE0_ST1 |   |       | strength control, bit 1     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 1\| 0x0   | Weak level holder (Bus      |
	| G1_REG_PKG_TYPE0_HE | 0 |       | holder) enable. 0=Disabled; |
	|                     |   |       | 1=Enabled                   |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition     |
	| G1_REG_PKG_TYPE0_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+
	
IOBLK_G1_REG_USB_VBUS_DET
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g1_reg_usb_vbus_det:
.. table:: IOBLK_G1_REG_USB_VBUS_DET
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G1\_\         | 2 | 0x0   | Pull-up resistor enable.            |
	| REG_USB_VBUS_DET_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G1\_\         | 3 | 0x0   | Pull-down resistor enable.          |
	| REG_USB_VBUS_DET_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G1_R\         | 5 | 0x0   | Output drive strength level, bit 0  |
	| EG_USB_VBUS_DET_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G1_R\         | 6 | 0x1   | Output drive strength level, bit 1  |
	| EG_USB_VBUS_DET_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G1_R\         | 8 | 0x0   | Input Schmitt trigger strength      |
	| EG_USB_VBUS_DET_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G1_R\         | 9 | 0x0   | Input Schmitt trigger strength      |
	| EG_USB_VBUS_DET_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G1\_\         | 1\| 0x0   | Weak bus holder enable.             |
	| REG_USB_VBUS_DET_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G1\_\         | 1\| 0x0   | Output level transition rate limit. |
	| REG_USB_VBUS_DET_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+
	
IOBLK_G1_REG_PKG_TYPE1
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g1_reg_pkg_type1:
.. table:: IOBLK_G1_REG_PKG_TYPE1
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\_\            | 2 | 0x1   | Pull-up resistor enable.    |
	| G1_REG_PKG_TYPE1_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 3 | 0x0   | Pull-down resistor enable.  |
	| G1_REG_PKG_TYPE1_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength       |
	| 1_REG_PKG_TYPE1_DS0 |   |       | level bit 0                 |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength       |
	| 1_REG_PKG_TYPE1_DS1 |   |       | level bit 1                 |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger       |
	| 1_REG_PKG_TYPE1_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 9 | 0x0   | Input Schmitt trigger       |
	| 1_REG_PKG_TYPE1_ST1 |   |       | strength control, bit 1     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 1\| 0x0   | Weak level holder (Bus      |
	| G1_REG_PKG_TYPE1_HE | 0 |       | holder) enable. 0=Disabled; |
	|                     |   |       | 1=Enabled                   |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition     |
	| G1_REG_PKG_TYPE1_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+
	
IOBLK_G1_REG_PKG_TYPE2
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g1_reg_pkg_type2:
.. table:: IOBLK_G1_REG_PKG_TYPE2
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK_G1\_\         | 2 | 0x0   | Pull-up resistor enable.    |
	| REG_USB_VBUS_DET_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G1\_\         | 3 | 0x0   | Pull-down resistor enable.  |
	| REG_USB_VBUS_DET_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G1_R\         | 5 | 0x0   | Output drive strength       |
	| EG_USB_VBUS_DET_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G1_R\         | 6 | 0x1   | Output drive strength       |
	| EG_USB_VBUS_DET_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G1_R\         | 8 | 0x0   | Input Schmitt trigger       |
	| EG_USB_VBUS_DET_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G1_R\         | 9 | 0x0   | Input Schmitt trigger       |
	| EG_USB_VBUS_DET_ST1 |   |       | strength control, bit 1     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G1\_\         | 1\| 0x0   | Weak level holder (Bus      |
	| REG_USB_VBUS_DET_HE | 0 |       | holder) enable. 0=Disabled; |
	|                     |   |       | 1=Enabled                   |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G1\_\         | 1\| 0x0   | Output level transition     |
	| REG_USB_VBUS_DET_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+
	
IOBLK_G7_REG_SD0_CD
^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_sd0_cd:
.. table:: IOBLK_G7_REG_SD0_CD
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOB\                | 2 | 0x1   | Pull-up resistor enable.    |
	| LK_G7_REG_SD0_CD_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOB\                | 3 | 0x0   | Pull-down resistor enable.  |
	| LK_G7_REG_SD0_CD_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 5 | 0x0   | Output drive strength       |
	| K_G7_REG_SD0_CD_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 6 | 0x1   | Output drive strength       |
	| K_G7_REG_SD0_CD_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 7 | 0x0   | Output drive strength       |
	| K_G7_REG_SD0_CD_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 8 | 0x0   | Input Schmitt trigger       |
	| K_G7_REG_SD0_CD_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOB\                | 1\| 0x0   | Output level transition     |
	| LK_G7_REG_SD0_CD_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G7_REG_SD0_PWR_EN
^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_sd0_pwr_en:
.. table:: IOBLK_G7_REG_SD0_PWR_EN
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK_G\            | 2 | 0x0   | Pull-up resistor enable.    |
	| 7_REG_SD0_PWR_EN_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 3 | 0x1   | Pull-down resistor enable.  |
	| 7_REG_SD0_PWR_EN_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7\           | 5 | 0x0   | Output drive strength       |
	| _REG_SD0_PWR_EN_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7\           | 6 | 0x1   | Output drive strength       |
	| _REG_SD0_PWR_EN_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7\           | 7 | 0x0   | Output drive strength       |
	| _REG_SD0_PWR_EN_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7\           | 8 | 0x0   | Input Schmitt trigger       |
	| _REG_SD0_PWR_EN_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 1\| 0x0   | Output level transition     |
	| 7_REG_SD0_PWR_EN_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+
	
IOBLK_G7_REG_SPK_EN
^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_spk_en:
.. table:: IOBLK_G7_REG_SPK_EN
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOB\                | 2 | 0x0   | Pull-up resistor enable.    |
	| LK_G7_REG_SPK_EN_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOB\                | 3 | 0x1   | Pull-down resistor enable.  |
	| LK_G7_REG_SPK_EN_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 5 | 0x0   | Output drive strength       |
	| K_G7_REG_SPK_EN_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 6 | 0x1   | Output drive strength       |
	| K_G7_REG_SPK_EN_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 7 | 0x0   | Output drive strength       |
	| K_G7_REG_SPK_EN_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 8 | 0x0   | Input Schmitt trigger       |
	| K_G7_REG_SPK_EN_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOB\                | 1\| 0x0   | Output level transition     |
	| LK_G7_REG_SPK_EN_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G7_REG_UART0_TX
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_uart0_tx:
.. table:: IOBLK_G7_REG_UART0_TX
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\              | 2 | 0x1   | Pull-up resistor enable.    |
	| _G7_REG_UART0_TX_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 3 | 0x0   | Pull-down resistor enable.  |
	| _G7_REG_UART0_TX_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength       |
	| G7_REG_UART0_TX_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength       |
	| G7_REG_UART0_TX_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength       |
	| G7_REG_UART0_TX_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger       |
	| G7_REG_UART0_TX_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition     |
	| _G7_REG_UART0_TX_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G7_REG_UART0_RX
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_uart0_rx:
.. table:: IOBLK_G7_REG_UART0_RX
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\              | 2 | 0x1   | Pull-up resistor enable.    |
	| _G7_REG_UART0_RX_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 3 | 0x0   | Pull-down resistor enable.  |
	| _G7_REG_UART0_RX_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength       |
	| G7_REG_UART0_RX_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength       |
	| G7_REG_UART0_RX_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength       |
	| G7_REG_UART0_RX_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger       |
	| G7_REG_UART0_RX_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition     |
	| _G7_REG_UART0_RX_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+
	
IOBLK_G7_REG_EMMC_DAT2
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_emmc_dat2:
.. table:: IOBLK_G7_REG_EMMC_DAT2
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\_\            | 2 | 0x0   | Pull-up resistor enable.    |
	| G7_REG_EMMC_DAT2_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 3 | 0x1   | Pull-down resistor enable.  |
	| G7_REG_EMMC_DAT2_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength       |
	| 7_REG_EMMC_DAT2_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength       |
	| 7_REG_EMMC_DAT2_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 7 | 0x0   | Output drive strength       |
	| 7_REG_EMMC_DAT2_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger       |
	| 7_REG_EMMC_DAT2_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition     |
	| G7_REG_EMMC_DAT2_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G7_REG_EMMC_CLK
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_emmc_clk:
.. table:: IOBLK_G7_REG_EMMC_CLK
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\              | 2 | 0x0   | Pull-up resistor enable.    |
	| _G7_REG_EMMC_CLK_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 3 | 0x1   | Pull-down resistor enable.  |
	| _G7_REG_EMMC_CLK_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength       |
	| G7_REG_EMMC_CLK_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength       |
	| G7_REG_EMMC_CLK_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength       |
	| G7_REG_EMMC_CLK_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger       |
	| G7_REG_EMMC_CLK_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition     |
	| _G7_REG_EMMC_CLK_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+
	
IOBLK_G7_REG_EMMC_DAT0
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_emmc_dat0:
.. table:: IOBLK_G7_REG_EMMC_DAT0
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\_\            | 2 | 0x1   | Pull-up resistor enable.    |
	| G7_REG_EMMC_DAT0_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 3 | 0x0   | Pull-down resistor enable.  |
	| G7_REG_EMMC_DAT0_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength       |
	| 7_REG_EMMC_DAT0_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength       |
	| 7_REG_EMMC_DAT0_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 7 | 0x0   | Output drive strength       |
	| 7_REG_EMMC_DAT0_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger       |
	| 7_REG_EMMC_DAT0_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition     |
	| G7_REG_EMMC_DAT0_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G7_REG_EMMC_DAT3
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_emmc_dat3:
.. table:: IOBLK_G7_REG_EMMC_DAT3
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\_\            | 2 | 0x1   | Pull-up resistor enable.    |
	| G7_REG_EMMC_DAT3_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 3 | 0x0   | Pull-down resistor enable.  |
	| G7_REG_EMMC_DAT3_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength       |
	| 7_REG_EMMC_DAT3_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength       |
	| 7_REG_EMMC_DAT3_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 7 | 0x0   | Output drive strength       |
	| 7_REG_EMMC_DAT3_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger       |
	| 7_REG_EMMC_DAT3_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition     |
	| G7_REG_EMMC_DAT3_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G7_REG_EMMC_CMD
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_emmc_cmd:
.. table:: IOBLK_G7_REG_EMMC_CMD
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\              | 2 | 0x1   | Pull-up resistor enable.    |
	| _G7_REG_EMMC_CMD_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 3 | 0x0   | Pull-down resistor enable.  |
	| _G7_REG_EMMC_CMD_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength       |
	| G7_REG_EMMC_CMD_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength       |
	| G7_REG_EMMC_CMD_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength       |
	| G7_REG_EMMC_CMD_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger       |
	| G7_REG_EMMC_CMD_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition     |
	| _G7_REG_EMMC_CMD_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+
	
IOBLK_G7_REG_EMMC_DAT1
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_emmc_dat1:
.. table:: IOBLK_G7_REG_EMMC_DAT1
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\_\            | 2 | 0x0   | Pull-up resistor enable.    |
	| G7_REG_EMMC_DAT1_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 3 | 0x1   | Pull-down resistor enable.  |
	| G7_REG_EMMC_DAT1_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength       |
	| 7_REG_EMMC_DAT1_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength       |
	| 7_REG_EMMC_DAT1_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 7 | 0x0   | Output drive strength       |
	| 7_REG_EMMC_DAT1_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger       |
	| 7_REG_EMMC_DAT1_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition     |
	| G7_REG_EMMC_DAT1_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+
	
IOBLK_G7_REG_JTAG_CPU_TMS
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_jtag_cpu_tms:
.. table:: IOBLK_G7_REG_JTAG_CPU_TMS
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK_G7\_\         | 2 | 0x0   | Pull-up resistor enable.    |
	| REG_JTAG_CPU_TMS_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7\_\         | 3 | 0x1   | Pull-down resistor enable.  |
	| REG_JTAG_CPU_TMS_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7_R\         | 5 | 0x0   | Output drive strength       |
	| EG_JTAG_CPU_TMS_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7_R\         | 6 | 0x1   | Output drive strength       |
	| EG_JTAG_CPU_TMS_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7_R\         | 7 | 0x0   | Output drive strength       |
	| EG_JTAG_CPU_TMS_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7_R\         | 8 | 0x0   | Input Schmitt trigger       |
	| EG_JTAG_CPU_TMS_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7\_\         | 1\| 0x0   | Output level transition     |
	| REG_JTAG_CPU_TMS_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G7_REG_JTAG_CPU_TCK
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_jtag_cpu_tck:
.. table:: IOBLK_G7_REG_JTAG_CPU_TCK
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK_G7\_\         | 2 | 0x0   | Pull-up resistor enable.    |
	| REG_JTAG_CPU_TCK_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7\_\         | 3 | 0x1   | Pull-down resistor enable.  |
	| REG_JTAG_CPU_TCK_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7_R\         | 5 | 0x0   | Output drive strength       |
	| EG_JTAG_CPU_TCK_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7_R\         | 6 | 0x1   | Output drive strength       |
	| EG_JTAG_CPU_TCK_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7_R\         | 7 | 0x0   | Output drive strength       |
	| EG_JTAG_CPU_TCK_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7_R\         | 8 | 0x0   | Input Schmitt trigger       |
	| EG_JTAG_CPU_TCK_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK_G7\_\         | 1\| 0x0   | Output level transition     |
	| REG_JTAG_CPU_TCK_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G7_REG_IIC0_SCL
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_iic0_scl:
.. table:: IOBLK_G7_REG_IIC0_SCL
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\              | 2 | 0x1   | Pull-up resistor enable.    |
	| _G7_REG_IIC0_SCL_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 3 | 0x0   | Pull-down resistor enable.  |
	| _G7_REG_IIC0_SCL_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength       |
	| G7_REG_IIC0_SCL_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength       |
	| G7_REG_IIC0_SCL_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength       |
	| G7_REG_IIC0_SCL_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger       |
	| G7_REG_IIC0_SCL_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition     |
	| _G7_REG_IIC0_SCL_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G7_REG_IIC0_SDA
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_iic0_sda:
.. table:: IOBLK_G7_REG_IIC0_SDA
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\              | 2 | 0x1   | Pull-up resistor enable.    |
	| _G7_REG_IIC0_SDA_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 3 | 0x0   | Pull-down resistor enable.  |
	| _G7_REG_IIC0_SDA_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength       |
	| G7_REG_IIC0_SDA_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength       |
	| G7_REG_IIC0_SDA_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength       |
	| G7_REG_IIC0_SDA_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger       |
	| G7_REG_IIC0_SDA_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition     |
	| _G7_REG_IIC0_SDA_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G7_REG_AUX0
^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g7_reg_aux0:
.. table:: IOBLK_G7_REG_AUX0
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\              | 2 | 0x0   | Pull-up resistor enable.    |
	| G7_REG_AUX0_PU      |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 3 | 0x1   | Pull-down resistor enable.  |
	| G7_REG_AUX0_PD      |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 5 | 0x0   | Output drive strength       |
	| G7_REG_AUX0_DS0     |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 6 | 0x1   | Output drive strength       |
	| G7_REG_AUX0_DS1     |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 7 | 0x0   | Output drive strength       |
	| G7_REG_AUX0_DS2     |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 8 | 0x0   | Input Schmitt trigger       |
	| G7_REG_AUX0_ST0     |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition     |
	| G7_REG_AUX0_SL      | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G10_REG_SD0_CLK
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g10_reg_sd0_clk:
.. table:: IOBLK_G10_REG_SD0_CLK
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\              | 2 | 0x0   | Pull-up resistor enable.    |
	| G10_REG_SD0_CLK_PU  |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 3 | 0x1   | Pull-down resistor enable.  |
	| G10_REG_SD0_CLK_PD  |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength       |
	| G10_REG_SD0_CLK_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength       |
	| G10_REG_SD0_CLK_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength       |
	| G10_REG_SD0_CLK_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger       |
	| G10_REG_SD0_CLK_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition     |
	| G10_REG_SD0_CLK_SL  | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G10_REG_SD0_CMD
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g10_reg_sd0_cmd:
.. table:: IOBLK_G10_REG_SD0_CMD
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBLK\              | 2 | 0x0   | Pull-up resistor enable.    |
	| G10_REG_SD0_CMD_PU  |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 3 | 0x1   | Pull-down resistor enable.  |
	| G10_REG_SD0_CMD_PD  |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength       |
	| G10_REG_SD0_CMD_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength       |
	| G10_REG_SD0_CMD_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength       |
	| G10_REG_SD0_CMD_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger       |
	| G10_REG_SD0_CMD_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition     |
	| G10_REG_SD0_CMD_SL  | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G10_REG_SD0_D0
^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g10_reg_sd0_d0:
.. table:: IOBLK_G10_REG_SD0_D0
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBL\               | 2 | 0x0   | Pull-up resistor enable.    |
	| K_G10_REG_SD0_D0_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 3 | 0x1   | Pull-down resistor enable.  |
	| K_G10_REG_SD0_D0_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 5 | 0x0   | Output drive strength       |
	| _G10_REG_SD0_D0_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 6 | 0x1   | Output drive strength       |
	| _G10_REG_SD0_D0_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 7 | 0x0   | Output drive strength       |
	| _G10_REG_SD0_D0_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 8 | 0x0   | Input Schmitt trigger       |
	| _G10_REG_SD0_D0_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 1\| 0x0   | Output level transition     |
	| K_G10_REG_SD0_D0_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G10_REG_SD0_D1
^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g10_reg_sd0_d1:
.. table:: IOBLK_G10_REG_SD0_D1
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBL\               | 2 | 0x0   | Pull-up resistor enable.    |
	| K_G10_REG_SD0_D1_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 3 | 0x1   | Pull-down resistor enable.  |
	| K_G10_REG_SD0_D1_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 5 | 0x0   | Output drive strength       |
	| _G10_REG_SD0_D1_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 6 | 0x1   | Output drive strength       |
	| _G10_REG_SD0_D1_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 7 | 0x0   | Output drive strength       |
	| _G10_REG_SD0_D1_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 8 | 0x0   | Input Schmitt trigger       |
	| _G10_REG_SD0_D1_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 1\| 0x0   | Output level transition     |
	| K_G10_REG_SD0_D1_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G10_REG_SD0_D2
^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g10_reg_sd0_d2:
.. table:: IOBLK_G10_REG_SD0_D2
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBL\               | 2 | 0x0   | Pull-up resistor enable.    |
	| K_G10_REG_SD0_D2_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 3 | 0x1   | Pull-down resistor enable.  |
	| K_G10_REG_SD0_D2_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 5 | 0x0   | Output drive strength       |
	| _G10_REG_SD0_D2_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 6 | 0x1   | Output drive strength       |
	| _G10_REG_SD0_D2_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 7 | 0x0   | Output drive strength       |
	| _G10_REG_SD0_D2_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 8 | 0x0   | Input Schmitt trigger       |
	| _G10_REG_SD0_D2_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 1\| 0x0   | Output level transition     |
	| K_G10_REG_SD0_D2_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G10_REG_SD0_D3
^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g10_reg_sd0_d3:
.. table:: IOBLK_G10_REG_SD0_D3
	:widths: 4 1 1 3

	+---------------------+---+-------+-----------------------------+
	| Field Name          | B\| Defa\ | Field\                      |
	|                     | i\| ult   | Description                 |
	|                     | t |       |                             |
	+=====================+===+=======+=============================+
	| IOBL\               | 2 | 0x0   | Pull-up resistor enable.    |
	| K_G10_REG_SD0_D3_PU |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 3 | 0x1   | Pull-down resistor enable.  |
	| K_G10_REG_SD0_D3_PD |   |       | 0=Disabled; 1=Enabled       |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 5 | 0x0   | Output drive strength       |
	| _G10_REG_SD0_D3_DS0 |   |       | level, bit 0                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 6 | 0x1   | Output drive strength       |
	| _G10_REG_SD0_D3_DS1 |   |       | level, bit 1                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 7 | 0x0   | Output drive strength       |
	| _G10_REG_SD0_D3_DS2 |   |       | level, bit 2                |
	+---------------------+---+-------+-----------------------------+
	| IOBLK\              | 8 | 0x0   | Input Schmitt trigger       |
	| _G10_REG_SD0_D3_ST0 |   |       | strength control, bit 0     |
	+---------------------+---+-------+-----------------------------+
	| IOBL\               | 1\| 0x0   | Output level transition     |
	| K_G10_REG_SD0_D3_SL | 1 |       | rate limit. 0=Disabled      |
	|                     |   |       | (faster); 1=Enabled (slower)|
	+---------------------+---+-------+-----------------------------+

IOBLK_G12_REG_PAD_MIPIRX4N
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipirx4n:
.. table:: IOBLK_G12_REG_PAD_MIPIRX4N
	:widths: 4 1 1 3

	+---------------------+---+-------+------------------------------------+
	| Field Name          | B\| Defa\ | Field\                             |
	|                     | i\| ult   | Description                        |
	|                     | t |       |                                    |
	+=====================+===+=======+====================================+
	| IOBLK_G12\_\        | 2 | 0x0   | Pull-up resistor enable.           |
	| REG_PAD_MIPIRX4N_PU |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 3 | 0x1   | Pull-down resistor enable.         |
	| REG_PAD_MIPIRX4N_PD |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 5 | 0x0   | Output drive strength              |
	| EG_PAD_MIPIRX4N_DS0 |   |       | level, bit 0                       |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 6 | 0x1   | Output drive strength              |
	| EG_PAD_MIPIRX4N_DS1 |   |       | level, bit 1                       |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 8 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX4N_ST0 |   |       | strength control, bit 0            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 9 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX4N_ST1 |   |       | strength control, bit 1            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Weak bus holder enable.            |
	| REG_PAD_MIPIRX4N_HE | 0 |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Output level transition rate limit.|
	| REG_PAD_MIPIRX4N_SL | 1 |       | 0=Disabled (faster); 1=Enabled     |
	|                     |   |       | (slower)                           |
	+---------------------+---+-------+------------------------------------+

IOBLK_G12_REG_PAD_MIPIRX4P
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipirx4p:
.. table:: IOBLK_G12_REG_PAD_MIPIRX4P
	:widths: 4 1 1 3

	+---------------------+---+-------+------------------------------------+
	| Field Name          | B\| Defa\ | Field\                             |
	|                     | i\| ult   | Description                        |
	|                     | t |       |                                    |
	+=====================+===+=======+====================================+
	| IOBLK_G12\_\        | 2 | 0x0   | Pull-up resistor enable.           |
	| REG_PAD_MIPIRX4P_PU |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 3 | 0x1   | Pull-down resistor enable.         |
	| REG_PAD_MIPIRX4P_PD |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 5 | 0x0   | Output drive strength              |
	| EG_PAD_MIPIRX4P_DS0 |   |       | level, bit 0                       |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 6 | 0x1   | Output drive strength              |
	| EG_PAD_MIPIRX4P_DS1 |   |       | level, bit 1                       |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 8 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX4P_ST0 |   |       | strength control, bit 0            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 9 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX4P_ST1 |   |       | strength control, bit 1            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Weak bus holder enable.            |
	| REG_PAD_MIPIRX4P_HE | 0 |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Output level transition rate limit.|
	| REG_PAD_MIPIRX4P_SL | 1 |       | 0=Disabled (faster); 1=Enabled     |
	|                     |   |       | (slower)                           |
	+---------------------+---+-------+------------------------------------+

IOBLK_G12_REG_PAD_MIPIRX3N
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipirx3n:
.. table:: IOBLK_G12_REG_PAD_MIPIRX3N
	:widths: 4 1 1 3

	+---------------------+---+-------+------------------------------------+
	| Field Name          | B\| Defa\ | Field\                             |
	|                     | i\| ult   | Description                        |
	|                     | t |       |                                    |
	+=====================+===+=======+====================================+
	| IOBLK_G12\_\        | 2 | 0x0   | Pull-up resistor enable.           |
	| REG_PAD_MIPIRX3N_PU |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 3 | 0x1   | Pull-down resistor enable.         |
	| REG_PAD_MIPIRX3N_PD |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 5 | 0x0   | Output drive strength              |
	| EG_PAD_MIPIRX3N_DS0 |   |       | level, bit 0                       |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 6 | 0x1   | Output drive strength              |
	| EG_PAD_MIPIRX3N_DS1 |   |       | level, bit 1                       |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 8 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX3N_ST0 |   |       | strength control, bit 0            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 9 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX3N_ST1 |   |       | strength control, bit 1            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Weak bus holder enable.            |
	| REG_PAD_MIPIRX3N_HE | 0 |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Output level transition rate limit.|
	| REG_PAD_MIPIRX3N_SL | 1 |       | 0=Disabled (faster); 1=Enabled     |
	|                     |   |       | (slower)                           |
	+---------------------+---+-------+------------------------------------+

IOBLK_G12_REG_PAD_MIPIRX3P
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipirx3p:
.. table:: IOBLK_G12_REG_PAD_MIPIRX3P
	:widths: 4 1 1 3

	+---------------------+---+-------+------------------------------------+
	| Field Name          | B\| Defa\ | Field\                             |
	|                     | i\| ult   | Description                        |
	|                     | t |       |                                    |
	+=====================+===+=======+====================================+
	| IOBLK_G12\_\        | 2 | 0x0   | Pull-up resistor enable.           |
	| REG_PAD_MIPIRX3P_PU |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 3 | 0x1   | Pull-down resistor enable.         |
	| REG_PAD_MIPIRX3P_PD |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 5 | 0x0   | Output drive strength level, bit 0 |
	| EG_PAD_MIPIRX3P_DS0 |   |       |                                    |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 6 | 0x1   | Output drive strength level, bit 1 |
	| EG_PAD_MIPIRX3P_DS1 |   |       |                                    |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 8 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX3P_ST0 |   |       | strength control, bit 0            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 9 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX3P_ST1 |   |       | strength control, bit 1            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Weak bus holder enable.            |
	| REG_PAD_MIPIRX3P_HE | 0 |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Output level transition rate limit.|
	| REG_PAD_MIPIRX3P_SL | 1 |       | 0=Disabled (faster); 1=Enabled     |
	|                     |   |       | (slower)                           |
	+---------------------+---+-------+------------------------------------+

IOBLK_G12_REG_PAD_MIPIRX2N
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipirx2n:
.. table:: IOBLK_G12_REG_PAD_MIPIRX2N
	:widths: 4 1 1 3

	+---------------------+---+-------+------------------------------------+
	| Field Name          | B\| Defa\ | Field\                             |
	|                     | i\| ult   | Description                        |
	|                     | t |       |                                    |
	+=====================+===+=======+====================================+
	| IOBLK_G12\_\        | 2 | 0x0   | Pull-up resistor enable.           |
	| REG_PAD_MIPIRX2N_PU |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 3 | 0x1   | Pull-down resistor enable.         |
	| REG_PAD_MIPIRX2N_PD |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 5 | 0x0   | Output drive strength level, bit 0 |
	| EG_PAD_MIPIRX2N_DS0 |   |       |                                    |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 6 | 0x1   | Output drive strength level, bit 1 |
	| EG_PAD_MIPIRX2N_DS1 |   |       |                                    |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 8 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX2N_ST0 |   |       | strength control, bit 0            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 9 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX2N_ST1 |   |       | strength control, bit 1            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Weak bus holder enable.            |
	| REG_PAD_MIPIRX2N_HE | 0 |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Output level transition rate limit.|
	| REG_PAD_MIPIRX2N_SL | 1 |       | 0=Disabled (faster); 1=Enabled     |
	|                     |   |       | (slower)                           |
	+---------------------+---+-------+------------------------------------+

IOBLK_G12_REG_PAD_MIPIRX2P
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipirx2p:
.. table:: IOBLK_G12_REG_PAD_MIPIRX2P
	:widths: 4 1 1 3

	+---------------------+---+-------+------------------------------------+
	| Field Name          | B\| Defa\ | Field\                             |
	|                     | i\| ult   | Description                        |
	|                     | t |       |                                    |
	+=====================+===+=======+====================================+
	| IOBLK_G12\_\        | 2 | 0x0   | Pull-up resistor enable.           |
	| REG_PAD_MIPIRX2P_PU |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 3 | 0x1   | Pull-down resistor enable.         |
	| REG_PAD_MIPIRX2P_PD |   |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 5 | 0x0   | Output drive strength level, bit 0 |
	| EG_PAD_MIPIRX2P_DS0 |   |       |                                    |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 6 | 0x1   | Output drive strength level, bit 1 |
	| EG_PAD_MIPIRX2P_DS1 |   |       |                                    |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 8 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX2P_ST0 |   |       | strength control, bit 0            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12_R\        | 9 | 0x0   | Input Schmitt trigger              |
	| EG_PAD_MIPIRX2P_ST1 |   |       | strength control, bit 1            |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Weak bus holder enable.            |
	| REG_PAD_MIPIRX2P_HE | 0 |       | 0=Disabled; 1=Enabled              |
	+---------------------+---+-------+------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Output level transition rate limit.|
	| REG_PAD_MIPIRX2P_SL | 1 |       | 0=Disabled (faster); 1=Enabled     |
	|                     |   |       | (slower)                           |
	+---------------------+---+-------+------------------------------------+

IOBLK_G12_REG_PAD_MIPIRX1N
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipirx1n:
.. table:: IOBLK_G12_REG_PAD_MIPIRX1N
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G12\_\        | 2 | 0x0   | Pull-up resistor enable.            |
	| REG_PAD_MIPIRX1N_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12\_\        | 3 | 0x1   | Pull-down resistor enable.          |
	| REG_PAD_MIPIRX1N_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 5 | 0x0   | Output drive strength level, bit 0  |
	| EG_PAD_MIPIRX1N_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 6 | 0x1   | Output drive strength level, bit 1  |
	| EG_PAD_MIPIRX1N_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 8 | 0x0   | Input Schmitt trigger strength      |
	| EG_PAD_MIPIRX1N_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 9 | 0x0   | Input Schmitt trigger strength      |
	| EG_PAD_MIPIRX1N_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Weak bus holder enable.             |
	| REG_PAD_MIPIRX1N_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Output level transition rate limit. |
	| REG_PAD_MIPIRX1N_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_G12_REG_PAD_MIPIRX1P
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipirx1p:
.. table:: IOBLK_G12_REG_PAD_MIPIRX1P
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G12\_\        | 2 | 0x0   | Pull-up resistor enable.            |
	| REG_PAD_MIPIRX1P_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12\_\        | 3 | 0x1   | Pull-down resistor enable.          |
	| REG_PAD_MIPIRX1P_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 5 | 0x0   | Output drive strength level, bit 0  |
	| EG_PAD_MIPIRX1P_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 6 | 0x1   | Output drive strength level, bit 1  |
	| EG_PAD_MIPIRX1P_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 8 | 0x0   | Input Schmitt trigger               |
	| EG_PAD_MIPIRX1P_ST0 |   |       | strength control, bit 0             |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 9 | 0x0   | Input Schmitt trigger               |
	| EG_PAD_MIPIRX1P_ST1 |   |       | strength control, bit 1             |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Weak bus holder enable.             |
	| REG_PAD_MIPIRX1P_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Output level transition rate limit. |
	| REG_PAD_MIPIRX1P_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_G12_REG_PAD_MIPIRX0N
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipirx0n:
.. table:: IOBLK_G12_REG_PAD_MIPIRX0N
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G12\_\        | 2 | 0x0   | Pull-up resistor enable.            |
	| REG_PAD_MIPIRX0N_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12\_\        | 3 | 0x1   | Pull-down resistor enable.          |
	| REG_PAD_MIPIRX0N_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 5 | 0x0   | Output drive strength level, bit 0  |
	| EG_PAD_MIPIRX0N_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 6 | 0x1   | Output drive strength level, bit 1  |
	| EG_PAD_MIPIRX0N_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 8 | 0x0   | Input Schmitt trigger               |
	| EG_PAD_MIPIRX0N_ST0 |   |       | strength control, bit 0             |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 9 | 0x0   | Input Schmitt trigger               |
	| EG_PAD_MIPIRX0N_ST1 |   |       | strength control, bit 1             |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Weak bus holder enable.             |
	| REG_PAD_MIPIRX0N_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Output level transition rate limit. |
	| REG_PAD_MIPIRX0N_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+
	
IOBLK_G12_REG_PAD_MIPIRX0P
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipirx0p:
.. table:: IOBLK_G12_REG_PAD_MIPIRX0P
	:widths: 4 1 1 3

	+---------------------+---+-------+--------------------------------+
	| Field Name          | B\| Defa\ | Field\                         |
	|                     | i\| ult   | Description                    |
	|                     | t |       |                                |
	+=====================+===+=======+================================+
	| IOBLK_G12\_\        | 2 | 0x0   | Pull-up resistor enable.       |
	| REG_PAD_MIPIRX0P_PU |   |       | 0=Disabled; 1=Enabled          |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12\_\        | 3 | 0x1   | Pull-down resistor enable.     |
	| REG_PAD_MIPIRX0P_PD |   |       | 0=Disabled; 1=Enabled          |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_R\        | 5 | 0x0   | Output drive strength level,   |
	| EG_PAD_MIPIRX0P_DS0 |   |       | bit 0                          |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_R\        | 6 | 0x1   | Output drive strength level,   |
	| EG_PAD_MIPIRX0P_DS1 |   |       | bit 1                          |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_R\        | 8 | 0x0   | Input Schmitt trigger strength |
	| EG_PAD_MIPIRX0P_ST0 |   |       | control, bit 0                 |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_R\        | 9 | 0x0   | Input Schmitt trigger strength |
	| EG_PAD_MIPIRX0P_ST1 |   |       | control, bit 1                 |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Weak bus holder enable.        |
	| REG_PAD_MIPIRX0P_HE | 0 |       | 0=Disabled; 1=Enabled          |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12\_\        | 1\| 0x0   | Output level transition rate   |
	| REG_PAD_MIPIRX0P_SL | 1 |       | limit. 0=Disabled (faster);    |
	|                     |   |       | 1=Enabled (slower)             |
	+---------------------+---+-------+--------------------------------+

	
IOBLK_G12_REG_PAD_MIPI_TXM2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipi_txm2:
.. table:: IOBLK_G12_REG_PAD_MIPI_TXM2
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G12_R\        | 2 | 0x0   | Pull-up resistor enable.            |
	| EG_PAD_MIPI_TXM2_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 3 | 0x1   | Pull-down resistor enable.          |
	| EG_PAD_MIPI_TXM2_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 5 | 0x0   | Output drive strength level, bit 0  |
	| G_PAD_MIPI_TXM2_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 6 | 0x1   | Output drive strength level, bit 1  |
	| G_PAD_MIPI_TXM2_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 8 | 0x0   | Input Schmitt trigger               |
	| G_PAD_MIPI_TXM2_ST0 |   |       | strength control, bit 0             |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 9 | 0x0   | Input Schmitt trigger               |
	| G_PAD_MIPI_TXM2_ST1 |   |       | strength control, bit 1             |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Weak bus holder enable.             |
	| EG_PAD_MIPI_TXM2_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Output level transition rate limit. |
	| EG_PAD_MIPI_TXM2_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_G12_REG_PAD_MIPI_TXP2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipi_txp2:
.. table:: IOBLK_G12_REG_PAD_MIPI_TXP2
	:widths: 4 1 1 3

	+---------------------+---+-------+--------------------------------+
	| Field Name          | B\| Defa\ | Field\                         |
	|                     | i\| ult   | Description                    |
	|                     | t |       |                                |
	+=====================+===+=======+================================+
	| IOBLK_G12_R\        | 2 | 0x0   | Pull-up resistor enable.       |
	| EG_PAD_MIPI_TXP2_PU |   |       | 0=Disabled; 1=Enabled          |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_R\        | 3 | 0x1   | Pull-down resistor enable.     |
	| EG_PAD_MIPI_TXP2_PD |   |       | 0=Disabled; 1=Enabled          |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_RE\       | 5 | 0x0   | Output drive strength level,   |
	| G_PAD_MIPI_TXP2_DS0 |   |       | bit 0                          |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_RE\       | 6 | 0x1   | Output drive strength level,   |
	| G_PAD_MIPI_TXP2_DS1 |   |       | bit 1                          |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_RE\       | 8 | 0x0   | Input Schmitt trigger          |
	| G_PAD_MIPI_TXP2_ST0 |   |       | strength control, bit 0        |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_RE\       | 9 | 0x0   | Input Schmitt trigger          |
	| G_PAD_MIPI_TXP2_ST1 |   |       | strength control, bit 1        |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Weak bus holder enable.        |
	| EG_PAD_MIPI_TXP2_HE | 0 |       | 0=Disabled; 1=Enabled          |
	+---------------------+---+-------+--------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Output level transition rate   |
	| EG_PAD_MIPI_TXP2_SL | 1 |       | limit. 0=Disabled (faster);    |
	|                     |   |       | 1=Enabled (slower)             |
	+---------------------+---+-------+--------------------------------+

IOBLK_G12_REG_PAD_MIPI_TXM1
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipi_txm1:
.. table:: IOBLK_G12_REG_PAD_MIPI_TXM1
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G12_R\        | 2 | 0x0   | Pull-up resistor enable.            |
	| EG_PAD_MIPI_TXM1_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 3 | 0x1   | Pull-down resistor enable.          |
	| EG_PAD_MIPI_TXM1_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 5 | 0x0   | Output drive strength level, bit 0  |
	| G_PAD_MIPI_TXM1_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 6 | 0x1   | Output drive strength level, bit 1  |
	| G_PAD_MIPI_TXM1_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 8 | 0x0   | Input Schmitt trigger strength      |
	| G_PAD_MIPI_TXM1_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 9 | 0x0   | Input Schmitt trigger strength      |
	| G_PAD_MIPI_TXM1_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Weak bus holder enable.             |
	| EG_PAD_MIPI_TXM1_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Output level transition rate limit. |
	| EG_PAD_MIPI_TXM1_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_G12_REG_PAD_MIPI_TXP1
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipi_txp1:
.. table:: IOBLK_G12_REG_PAD_MIPI_TXP1
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G12_R\        | 2 | 0x0   | Pull-up resistor enable.            |
	| EG_PAD_MIPI_TXP1_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 3 | 0x1   | Pull-down resistor enable.          |
	| EG_PAD_MIPI_TXP1_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 5 | 0x0   | Output drive strength level, bit 0  |
	| G_PAD_MIPI_TXP1_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 6 | 0x1   | Output drive strength level, bit 1  |
	| G_PAD_MIPI_TXP1_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 8 | 0x0   | Input Schmitt trigger strength      |
	| G_PAD_MIPI_TXP1_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 9 | 0x0   | Input Schmitt trigger strength      |
	| G_PAD_MIPI_TXP1_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Weak bus holder enable.             |
	| EG_PAD_MIPI_TXP1_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Output level transition rate limit. |
	| EG_PAD_MIPI_TXP1_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_G12_REG_PAD_MIPI_TXM0
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipi_txm0:
.. table:: IOBLK_G12_REG_PAD_MIPI_TXM0
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G12_R\        | 2 | 0x0   | Pull-up resistor enable.            |
	| EG_PAD_MIPI_TXM0_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 3 | 0x1   | Pull-down resistor enable.          |
	| EG_PAD_MIPI_TXM0_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 5 | 0x0   | Output drive strength level, bit 0  |
	| G_PAD_MIPI_TXM0_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 6 | 0x1   | Output drive strength level, bit 1  |
	| G_PAD_MIPI_TXM0_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 8 | 0x0   | Input Schmitt trigger strength      |
	| G_PAD_MIPI_TXM0_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 9 | 0x0   | Input Schmitt trigger strength      |
	| G_PAD_MIPI_TXM0_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Weak bus holder enable.             |
	| EG_PAD_MIPI_TXM0_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Output level transition rate limit. |
	| EG_PAD_MIPI_TXM0_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_G12_REG_PAD_MIPI_TXP0
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_pad_mipi_txp0:
.. table:: IOBLK_G12_REG_PAD_MIPI_TXP0
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G12_R\        | 2 | 0x0   | Pull-up resistor enable.            |
	| EG_PAD_MIPI_TXP0_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 3 | 0x1   | Pull-down resistor enable.          |
	| EG_PAD_MIPI_TXP0_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 5 | 0x0   | Output drive strength level, bit 0  |
	| G_PAD_MIPI_TXP0_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 6 | 0x1   | Output drive strength level, bit 1  |
	| G_PAD_MIPI_TXP0_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 8 | 0x0   | Input Schmitt trigger strength      |
	| G_PAD_MIPI_TXP0_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_RE\       | 9 | 0x0   | Input Schmitt trigger strength      |
	| G_PAD_MIPI_TXP0_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Weak bus holder enable.             |
	| EG_PAD_MIPI_TXP0_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G12_R\        | 1\| 0x0   | Output level transition rate limit. |
	| EG_PAD_MIPI_TXP0_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_G12_REG_GPIO_RTX
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_g12_reg_gpio_rtx:
.. table:: IOBLK_G12_REG_GPIO_RTX
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK\_\            | 2 | 0x0   | Pull-up resistor enable.            |
	| G12_REG_GPIO_RTX_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 3 | 0x1   | Pull-down resistor enable.          |
	| G12_REG_GPIO_RTX_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength level, bit 0  |
	| 12_REG_GPIO_RTX_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength level, bit 1  |
	| 12_REG_GPIO_RTX_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger strength      |
	| 12_REG_GPIO_RTX_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 9 | 0x0   | Input Schmitt trigger strength      |
	| 12_REG_GPIO_RTX_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 1\| 0x0   | Weak bus holder enable.             |
	| G12_REG_GPIO_RTX_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition rate limit. |
	| G12_REG_GPIO_RTX_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_PWR_VBAT_DET
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_pwr_vbat_det:
.. table:: IOBLK_GRTC_REG_PWR_VBAT_DET
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_GRTC\_\       | 2 | 0x0   | Pull-up resistor enable.            |
	| REG_PWR_VBAT_DET_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 3 | 0x0   | Pull-down resistor enable.          |
	| REG_PWR_VBAT_DET_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC_R\       | 5 | 0x0   | Output drive strength level, bit 0  |
	| EG_PWR_VBAT_DET_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC_R\       | 6 | 0x1   | Output drive strength level, bit 1  |
	| EG_PWR_VBAT_DET_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC_R\       | 8 | 0x0   | Input Schmitt trigger strength      |
	| EG_PWR_VBAT_DET_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC_R\       | 9 | 0x0   | Input Schmitt trigger strength      |
	| EG_PWR_VBAT_DET_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 1\| 0x0   | Weak bus holder enable.             |
	| REG_PWR_VBAT_DET_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 1\| 0x0   | Output level transition rate limit. |
	| REG_PWR_VBAT_DET_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_PWR_RSTN
^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_pwr_rstn:
.. table:: IOBLK_GRTC_REG_PWR_RSTN
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G\            | 2 | 0x1   | Pull-up resistor enable.            |
	| RTC_REG_PWR_RSTN_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 3 | 0x0   | Pull-down resistor enable.          |
	| RTC_REG_PWR_RSTN_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 5 | 0x0   | Output drive strength level, bit 0  |
	| TC_REG_PWR_RSTN_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 6 | 0x1   | Output drive strength level, bit 1  |
	| TC_REG_PWR_RSTN_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 8 | 0x0   | Input Schmitt trigger strength      |
	| TC_REG_PWR_RSTN_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 9 | 0x0   | Input Schmitt trigger strength      |
	| TC_REG_PWR_RSTN_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 1\| 0x0   | Weak bus holder enable.             |
	| RTC_REG_PWR_RSTN_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 1\| 0x0   | Output level transition rate limit. |
	| RTC_REG_PWR_RSTN_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_PWR_SEQ1
^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_pwr_seq1:
.. table:: IOBLK_GRTC_REG_PWR_SEQ1
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G\            | 2 | 0x0   | Pull-up resistor enable.            |
	| RTC_REG_PWR_SEQ1_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 3 | 0x1   | Pull-down resistor enable.          |
	| RTC_REG_PWR_SEQ1_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 5 | 0x0   | Output drive strength level, bit 0  |
	| TC_REG_PWR_SEQ1_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 6 | 0x1   | Output drive strength level, bit 1  |
	| TC_REG_PWR_SEQ1_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 8 | 0x0   | Input Schmitt trigger strength      |
	| TC_REG_PWR_SEQ1_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 9 | 0x0   | Input Schmitt trigger strength      |
	| TC_REG_PWR_SEQ1_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 1\| 0x0   | Weak bus holder enable.             |
	| RTC_REG_PWR_SEQ1_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 1\| 0x0   | Output level transition rate limit. |
	| RTC_REG_PWR_SEQ1_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_PWR_SEQ2
^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_pwr_seq2:
.. table:: IOBLK_GRTC_REG_PWR_SEQ2
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_G\            | 2 | 0x0   | Pull-up resistor enable.            |
	| RTC_REG_PWR_SEQ2_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 3 | 0x1   | Pull-down resistor enable.          |
	| RTC_REG_PWR_SEQ2_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 5 | 0x0   | Output drive strength level, bit 0  |
	| TC_REG_PWR_SEQ2_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 6 | 0x1   | Output drive strength level, bit 1  |
	| TC_REG_PWR_SEQ2_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 8 | 0x0   | Input Schmitt trigger strength      |
	| TC_REG_PWR_SEQ2_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 9 | 0x0   | Input Schmitt trigger strength      |
	| TC_REG_PWR_SEQ2_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 1\| 0x0   | Weak bus holder enable.             |
	| RTC_REG_PWR_SEQ2_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 1\| 0x0   | Output level transition rate limit. |
	| RTC_REG_PWR_SEQ2_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_PTEST
^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_ptest:
.. table:: IOBLK_GRTC_REG_PTEST
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBL\               | 2 | 0x0   | Pull-up resistor enable.            |
	| K_GRTC_REG_PTEST_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBL\               | 3 | 0x1   | Pull-down resistor enable.          |
	| K_GRTC_REG_PTEST_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 5 | 0x0   | Output drive strength level, bit 0  |
	| _GRTC_REG_PTEST_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 6 | 0x1   | Output drive strength level, bit 1  |
	| _GRTC_REG_PTEST_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 8 | 0x0   | Input Schmitt trigger strength      |
	| _GRTC_REG_PTEST_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 9 | 0x0   | Input Schmitt trigger strength      |
	| _GRTC_REG_PTEST_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBL\               | 1\| 0x0   | Weak bus holder enable.             |
	| K_GRTC_REG_PTEST_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBL\               | 1\| 0x0   | Output level transition rate limit. |
	| K_GRTC_REG_PTEST_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_PWR_WAKEUP0
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_pwr_wakeup0:
.. table:: IOBLK_GRTC_REG_PWR_WAKEUP0
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_GRTC\         | 2 | 0x0   | Pull-up resistor enable.            |
	| _REG_PWR_WAKEUP0_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\         | 3 | 0x1   | Pull-down resistor enable.          |
	| _REG_PWR_WAKEUP0_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 5 | 0x0   | Output drive strength level, bit 0  |
	| REG_PWR_WAKEUP0_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 6 | 0x1   | Output drive strength level, bit 1  |
	| REG_PWR_WAKEUP0_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 8 | 0x0   | Input Schmitt trigger strength      |
	| REG_PWR_WAKEUP0_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 9 | 0x0   | Input Schmitt trigger strength      |
	| REG_PWR_WAKEUP0_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\         | 1\| 0x0   | Weak bus holder enable.             |
	| _REG_PWR_WAKEUP0_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\         | 1\| 0x0   | Output level transition rate limit. |
	| _REG_PWR_WAKEUP0_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+
	
IOBLK_GRTC_REG_PWR_BUTTON1
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_pwr_button1:
.. table:: IOBLK_GRTC_REG_PWR_BUTTON1
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_GRTC\         | 2 | 0x1   | Pull-up resistor enable.            |
	| _REG_PWR_BUTTON1_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\         | 3 | 0x0   | Pull-down resistor enable.          |
	| _REG_PWR_BUTTON1_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 5 | 0x0   | Output drive strength level, bit 0  |
	| REG_PWR_BUTTON1_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 6 | 0x1   | Output drive strength level, bit 1  |
	| REG_PWR_BUTTON1_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 8 | 0x0   | Input Schmitt trigger strength      |
	| REG_PWR_BUTTON1_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\_\       | 9 | 0x0   | Input Schmitt trigger strength      |
	| REG_PWR_BUTTON1_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\         | 1\| 0x0   | Weak bus holder enable.             |
	| _REG_PWR_BUTTON1_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRTC\         | 1\| 0x0   | Output level transition rate limit. |
	| _REG_PWR_BUTTON1_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_XTAL_XIN
^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_xtal_xin:
.. table:: IOBLK_GRTC_REG_XTAL_XIN
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_GRT\          | 1 | 0x0   | Crystal oscillator output           |
	| C_REG_XTAL_XIN_XDS0 | 4 |       | drive strength level, bit 0         |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 1 | 0x0   | Crystal oscillator output           |
	| C_REG_XTAL_XIN_XDS1 | 5 |       | drive strength level, bit 1         |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 1 | 0x1   | Crystal oscillator output           |
	| C_REG_XTAL_XIN_XDS2 | 6 |       | drive strength level, bit 2         |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_PWR_GPIO0
^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_pwr_gpio0:
.. table:: IOBLK_GRTC_REG_PWR_GPIO0
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_GR\           | 2 | 0x0   | Pull-up resistor enable.            |
	| TC_REG_PWR_GPIO0_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 3 | 0x1   | Pull-down resistor enable.          |
	| TC_REG_PWR_GPIO0_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 5 | 0x0   | Output drive strength level, bit 0  |
	| C_REG_PWR_GPIO0_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 6 | 0x1   | Output drive strength level, bit 1  |
	| C_REG_PWR_GPIO0_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 8 | 0x0   | Input Schmitt trigger strength      |
	| C_REG_PWR_GPIO0_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 9 | 0x0   | Input Schmitt trigger strength      |
	| C_REG_PWR_GPIO0_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 1\| 0x0   | Weak bus holder enable.             |
	| TC_REG_PWR_GPIO0_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 1\| 0x0   | Output level transition rate limit. |
	| TC_REG_PWR_GPIO0_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_PWR_GPIO1
^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_pwr_gpio1:
.. table:: IOBLK_GRTC_REG_PWR_GPIO1
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_GR\           | 2 | 0x0   | Pull-up resistor enable.            |
	| TC_REG_PWR_GPIO1_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 3 | 0x1   | Pull-down resistor enable.          |
	| TC_REG_PWR_GPIO1_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 5 | 0x0   | Output drive strength level, bit 0  |
	| C_REG_PWR_GPIO1_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 6 | 0x1   | Output drive strength level, bit 1  |
	| C_REG_PWR_GPIO1_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 8 | 0x0   | Input Schmitt trigger strength      |
	| C_REG_PWR_GPIO1_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 9 | 0x0   | Input Schmitt trigger strength      |
	| C_REG_PWR_GPIO1_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 1\| 0x0   | Weak bus holder enable.             |
	| TC_REG_PWR_GPIO1_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 1\| 0x0   | Output level transition rate limit. |
	| TC_REG_PWR_GPIO1_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_PWR_GPIO2
^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_pwr_gpio2:
.. table:: IOBLK_GRTC_REG_PWR_GPIO2
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK_GR\           | 2 | 0x0   | Pull-up resistor enable.            |
	| TC_REG_PWR_GPIO2_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 3 | 0x1   | Pull-down resistor enable.          |
	| TC_REG_PWR_GPIO2_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 5 | 0x0   | Output drive strength level, bit 0  |
	| C_REG_PWR_GPIO2_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 6 | 0x1   | Output drive strength level, bit 1  |
	| C_REG_PWR_GPIO2_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 8 | 0x0   | Input Schmitt trigger strength      |
	| C_REG_PWR_GPIO2_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GRT\          | 9 | 0x0   | Input Schmitt trigger strength      |
	| C_REG_PWR_GPIO2_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 1\| 0x0   | Weak bus holder enable.             |
	| TC_REG_PWR_GPIO2_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_GR\           | 1\| 0x0   | Output level transition rate limit. |
	| TC_REG_PWR_GPIO2_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+


IOBLK_GRTC_REG_SD1_D3
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_sd1_d3:
.. table:: IOBLK_GRTC_REG_SD1_D3
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK\              | 2 | 0x0   | Pull-up resistor enable.            |
	| _GRTC_REG_SD1_D3_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 3 | 0x1   | Pull-down resistor enable.          |
	| _GRTC_REG_SD1_D3_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength level, bit 0  |
	| GRTC_REG_SD1_D3_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength level, bit 1  |
	| GRTC_REG_SD1_D3_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength level, bit 2  |
	| GRTC_REG_SD1_D3_DS2 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger strength      |
	| GRTC_REG_SD1_D3_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition rate limit. |
	| _GRTC_REG_SD1_D3_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_SD1_D2
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_sd1_d2:
.. table:: IOBLK_GRTC_REG_SD1_D2
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK\              | 2 | 0x0   | Pull-up resistor enable.            |
	| _GRTC_REG_SD1_D2_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 3 | 0x1   | Pull-down resistor enable.          |
	| _GRTC_REG_SD1_D2_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength level, bit 0  |
	| GRTC_REG_SD1_D2_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength level, bit 1  |
	| GRTC_REG_SD1_D2_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength level, bit 2  |
	| GRTC_REG_SD1_D2_DS2 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger strength      |
	| GRTC_REG_SD1_D2_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition rate limit. |
	| _GRTC_REG_SD1_D2_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_SD1_D1
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_sd1_d1:
.. table:: IOBLK_GRTC_REG_SD1_D1
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK\              | 2 | 0x0   | Pull-up resistor enable.            |
	| _GRTC_REG_SD1_D1_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 3 | 0x1   | Pull-down resistor enable.          |
	| _GRTC_REG_SD1_D1_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength level, bit 0  |
	| GRTC_REG_SD1_D1_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength level, bit 1  |
	| GRTC_REG_SD1_D1_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength level, bit 2  |
	| GRTC_REG_SD1_D1_DS2 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger strength      |
	| GRTC_REG_SD1_D1_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition rate limit. |
	| _GRTC_REG_SD1_D1_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_SD1_D0
^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_sd1_d0:
.. table:: IOBLK_GRTC_REG_SD1_D0
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK\              | 2 | 0x0   | Pull-up resistor enable.            |
	| _GRTC_REG_SD1_D0_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 3 | 0x1   | Pull-down resistor enable.          |
	| _GRTC_REG_SD1_D0_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 5 | 0x0   | Output drive strength level, bit 0  |
	| GRTC_REG_SD1_D0_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 6 | 0x1   | Output drive strength level, bit 1  |
	| GRTC_REG_SD1_D0_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 7 | 0x0   | Output drive strength level, bit 2  |
	| GRTC_REG_SD1_D0_DS2 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 8 | 0x0   | Input Schmitt trigger strength      |
	| GRTC_REG_SD1_D0_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\              | 1\| 0x0   | Output level transition rate limit. |
	| _GRTC_REG_SD1_D0_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_SD1_CMD
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_sd1_cmd:
.. table:: IOBLK_GRTC_REG_SD1_CMD
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK\_\            | 2 | 0x0   | Pull-up resistor enable.            |
	| GRTC_REG_SD1_CMD_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 3 | 0x1   | Pull-down resistor enable.          |
	| GRTC_REG_SD1_CMD_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength level, bit 0  |
	| RTC_REG_SD1_CMD_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength level, bit 1  |
	| RTC_REG_SD1_CMD_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 7 | 0x0   | Output drive strength level, bit 2  |
	| RTC_REG_SD1_CMD_DS2 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger strength      |
	| RTC_REG_SD1_CMD_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition rate limit. |
	| GRTC_REG_SD1_CMD_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_SD1_CLK
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_sd1_clk:
.. table:: IOBLK_GRTC_REG_SD1_CLK
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK\_\            | 2 | 0x0   | Pull-up resistor enable.            |
	| GRTC_REG_SD1_CLK_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 3 | 0x1   | Pull-down resistor enable.          |
	| GRTC_REG_SD1_CLK_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength level, bit 0  |
	| RTC_REG_SD1_CLK_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength level, bit 1  |
	| RTC_REG_SD1_CLK_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 7 | 0x0   | Output drive strength level, bit 2  |
	| RTC_REG_SD1_CLK_DS2 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger strength      |
	| RTC_REG_SD1_CLK_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition rate limit. |
	| GRTC_REG_SD1_CLK_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

IOBLK_GRTC_REG_GPIO_ZQ
^^^^^^^^^^^^^^^^^^^^^^

.. _table_pincontrol_ioblk_grtc_reg_gpio_zq:
.. table:: IOBLK_GRTC_REG_GPIO_ZQ
	:widths: 4 1 1 3

	+---------------------+---+-------+-------------------------------------+
	| Field Name          | B\| Defa\ | Field\                              |
	|                     | i\| ult   | Description                         |
	|                     | t |       |                                     |
	+=====================+===+=======+=====================================+
	| IOBLK\_\            | 2 | 0x0   | Pull-up resistor enable.            |
	| GRTC_REG_GPIO_ZQ_PU |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 3 | 0x1   | Pull-down resistor enable.          |
	| GRTC_REG_GPIO_ZQ_PD |   |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 5 | 0x0   | Output drive strength level, bit 0  |
	| RTC_REG_GPIO_ZQ_DS0 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 6 | 0x1   | Output drive strength level, bit 1  |
	| RTC_REG_GPIO_ZQ_DS1 |   |       |                                     |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 8 | 0x0   | Input Schmitt trigger strength      |
	| RTC_REG_GPIO_ZQ_ST0 |   |       | control, bit 0                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK_G\            | 9 | 0x0   | Input Schmitt trigger strength      |
	| RTC_REG_GPIO_ZQ_ST1 |   |       | control, bit 1                      |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 1\| 0x0   | Weak bus holder enable.             |
	| GRTC_REG_GPIO_ZQ_HE | 0 |       | 0=Disabled; 1=Enabled               |
	+---------------------+---+-------+-------------------------------------+
	| IOBLK\_\            | 1\| 0x0   | Output level transition rate limit. |
	| GRTC_REG_GPIO_ZQ_SL | 1 |       | 0=Disabled (faster); 1=Enabled      |
	|                     |   |       | (slower)                            |
	+---------------------+---+-------+-------------------------------------+

