.. _table_rtc_core_reg_overview:
.. table:: RTC_CORE_REG Overview (Base: 0x05026000)
	:widths:  3 1 3

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| RTC_ANA_CALIB        | 0x000   | 32K oscillator control             |
	+----------------------+---------+------------------------------------+
	| RTC_SEC_PULSE_GEN    | 0x004   | Second pulse generator integer     |
	|		       |	 | and decimal digits                 |
	+----------------------+---------+------------------------------------+
	| RTC_ALARM_TIME       | 0x008   | scheduled alarm time               |
	+----------------------+---------+------------------------------------+
	| RTC_ALARM_ENABLE     | 0x00c   | Enable alarm                       |
	+----------------------+---------+------------------------------------+
	| RT\                  | 0x010   | Set seconds counter value          |
	| C_SET_SEC_CNTR_VALUE |         |                                    |
	+----------------------+---------+------------------------------------+
	| R\                   | 0x014   | Loading seconds counter value      |
	| TC_SET_SEC_CNTR_TRIG |         |                                    |
	+----------------------+---------+------------------------------------+
	| RTC_SEC_CNTR_VALUE   | 0x018   | Read current second counter value  |
	+----------------------+---------+------------------------------------+
	| RTC_INFO0            | 0x01c   | Information register 0             |
	+----------------------+---------+------------------------------------+
	| RTC_INFO1            | 0x020   | Information register 1             |
	+----------------------+---------+------------------------------------+
	| RTC_INFO2            | 0x024   | Information register 2             |
	+----------------------+---------+------------------------------------+
	| RTC_INFO3            | 0x028   | Information register 3             |
	+----------------------+---------+------------------------------------+
	| RTC_NOPOR_INFO0      | 0x02c   | No reset information register 0    |
	+----------------------+---------+------------------------------------+
	| RTC_NOPOR_INFO1      | 0x030   | No reset information register 1    |
	+----------------------+---------+------------------------------------+
	| RTC_NOPOR_INFO2      | 0x034   | No reset information register 2    |
	+----------------------+---------+------------------------------------+
	| RTC_NOPOR_INFO3      | 0x038   | No reset information register 3    |
	+----------------------+---------+------------------------------------+
	| RTC_DB_PWR_VBAT_DET  | 0x040   | PWR_VBAT_DET debounce time         |
	+----------------------+---------+------------------------------------+
	| RTC_DB_BUTTON1       | 0x048   | PWR_BUTTON1debounce time           |
	+----------------------+---------+------------------------------------+
	| RTC_DB_PWR_ON        | 0x04c   | PWR_ONdebounce time                |
	+----------------------+---------+------------------------------------+
	| RTC_7SEC_RESET       | 0x050   | Set the number of seconds to press |
	|                      |         | and hold PWR_BUTTON to force reset |
	+----------------------+---------+------------------------------------+
	| RTC\_\               | 0x064   | Select REQ_THM_SHDN action         |
	| THM_SHDN_AUTO_REBOOT |         |                                    |
	+----------------------+---------+------------------------------------+
	| RTC_POR_DB_MAGIC_KEY | 0x068   | Enable POR long-term debounce      |
	+----------------------+---------+------------------------------------+
	| RTC_DB_SEL_PWR       | 0x06c   | Select PWR_BUTTON debounce mode    |
	+----------------------+---------+------------------------------------+
	| RTC_UP_SEQ0          | 0x070   | Power-on PWR_SEQ0 output timing    |
	+----------------------+---------+------------------------------------+
	| RTC_UP_SEQ1          | 0x074   | Power-on PWR_SEQ1 output timing    |
	+----------------------+---------+------------------------------------+
	| RTC_UP_SEQ2          | 0x078   | Power-on PWR_SEQ2 output timing    |
	+----------------------+---------+------------------------------------+
	| RTC_UP_SEQ3          | 0x07c   | Power-on PWR_SEQ3 output timing    |
	+----------------------+---------+------------------------------------+
	| RTC_UP_IF_EN         | 0x080   | Power-on ISO release timing 	      |
	+----------------------+---------+------------------------------------+
	| RTC_UP_RSTN          | 0x084   | Power-on system reset release      |
	|                      |         | sequence                           |
	+----------------------+---------+------------------------------------+
	| RTC_UP_MAX           | 0x088   | Power-on process completion timing |
	+----------------------+---------+------------------------------------+
	| RTC_DN_SEQ0          | 0x090   | Power off PWR_SEQ0 output timing   |
	+----------------------+---------+------------------------------------+
	| RTC_DN_SEQ1          | 0x094   | Power off PWR_SEQ1 output timing   |
	+----------------------+---------+------------------------------------+
	| RTC_DN_SEQ2          | 0x098   | Power off PWR_SEQ2 output timing   |
	+----------------------+---------+------------------------------------+
	| RTC_DN_SEQ3          | 0x09c   | Power off PWR_SEQ3 output timing   |
	+----------------------+---------+------------------------------------+
	| RTC_DN_IF_EN         | 0x0a0   | Power off ISO open timing	      |
	+----------------------+---------+------------------------------------+
	| RTC_DN_RSTN          | 0x0a4   | Power-off system reset sequence    |
	+----------------------+---------+------------------------------------+
	| RTC_DN_MAX           | 0x0a8   | Power-off process completion timing|
	+----------------------+---------+------------------------------------+
	| RTC_PWR_CYC_MAX      | 0x0b0   | Power-cycle completion timing      |
	+----------------------+---------+------------------------------------+
	| RTC_WARM_RST_MAX     | 0x0b4   | Warm-reset completion timi         |
	+----------------------+---------+------------------------------------+
	| RTC_EN_7SEC_RST      | 0x0b8   | Set PWR_BUTTON1 7SEC reset mode    |
	+----------------------+---------+------------------------------------+
	| RTC_EN_PWR_WAKEUP    | 0x0bc   | Set sleep wake-up source           |
	+----------------------+---------+------------------------------------+
	| RTC_EN_SHDN_REQ      | 0x0c0   | Enable REQ_SHDN                    |
	+----------------------+---------+------------------------------------+
	| RTC_EN_THM_SHDN      | 0x0c4   | Enable REQ_THM_SHDN                |
	+----------------------+---------+------------------------------------+
	| RTC_EN_PWR_CYC_REQ   | 0x0c8   | Enable REQ_PWR_CYC                 |
	+----------------------+---------+------------------------------------+
	| RTC_EN_WARM_RST_REQ  | 0x0cc   | Enable REQ_WARM_RST                |
	+----------------------+---------+------------------------------------+
	| RTC_EN_PWR_VBAT_DET  | 0x0d0   | Enable state machine reference     |
	|                      |         | PWR_VBAT_DET                       |
	+----------------------+---------+------------------------------------+
	| FSM_STATE            | 0x0d4   | RTC state machine value            |
	+----------------------+---------+------------------------------------+
	| RTC_EN_WDG_RST_REQ   | 0x0e0   | Enable REQ_WDG_RST                 |
	+----------------------+---------+------------------------------------+
	| RTC_EN_SUSPEND_REQ   | 0x0e4   | Enable REQ_SUSPEND                 |
	+----------------------+---------+------------------------------------+
	| RTC_DB_REQ_WDG_RST   | 0x0e8   | REQ_WDG_RST debounce time          |
	+----------------------+---------+------------------------------------+
	| RTC_DB_REQ_SUSPEND   | 0x0ec   | REQ_SUSPEND debounce time          |
	+----------------------+---------+------------------------------------+
	| RTC_PG_REG           | 0x0f0   | Power Good Register                |
	+----------------------+---------+------------------------------------+
	| RTC_ST_ON_REASON     | 0x0f8   | Power-on status register           |
	+----------------------+---------+------------------------------------+
	| RTC_ST_OFF_REASON    | 0x0fc   | Power-down status register         |
	+----------------------+---------+------------------------------------+
	| RTC_EN_WAKEUP_REQ    | 0x120   | Enable REQ_WAKEUP                  |
	+----------------------+---------+------------------------------------+
	| RTC\                 | 0x128   |Select PWR_WAKEUP low level 	      |
	| _PWR_WAKEUP_POLARITY |         |                                    |
	+----------------------+---------+------------------------------------+
	| RTC_DB_SEL_REQ       | 0x130   | Select debounce mode               |
	+----------------------+---------+------------------------------------+
	| RTC_PWR_DET_SEL      | 0x140   | Select low voltage detection       |
	|                      |         | signal source                      |
	+----------------------+---------+------------------------------------+
