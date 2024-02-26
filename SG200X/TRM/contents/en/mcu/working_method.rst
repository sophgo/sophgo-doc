Way of Working
--------------

.. _section_8051_power_domain_control:

Power Domain Control Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The RTCSYS subsystem is divided into two power domains: AO (Always-On) domain and MCU domain. The MCU domain can be powered on and off through the configuration register. The process is as follows:

MCU power_off:

1. Soft reset register = 0

2. Set register reg_mcu_iso_en = 1

3. Set register reg_mcu_pwr_req = 0

MCU power_on:

1. Set register reg_mcu_pwr_req = 1

2. Polling register reg_mcu_pwr_ack = 1

3. Set register reg_mcu_iso_en = 0

4. Soft reset register = 1

8051 Initialization
~~~~~~~~~~~~~~~~~~~

8051 is in reset state at the beginning of the system. Using 8051, you can complete the following software process through ACPU:

1. The 8051 reset state is in reset state (register reg_soft_rstn_mcu = 0).

2. Configure the register reg_mcu_rom_addr_size to determine the instruction TCM size.

3. Configure the register reg_51irom_ioffset to determine the location on the AHB SRAM where TCM is executed.

4. Configure register reg_soft_rstn_mcu =1 to release the 8051 reset state.

.. _section_8051_interrupt:

Interrupt Handling
~~~~~~~~~~~~~~~~~~

8051 can receive external level-triggered interrupts through the int0_n and int1_n interfaces. int0_n/int1_n selects to output interrupt signals to 8051 from ictl (interrupt control) and configuration register reg_51_int1_src_mask respectively.

.. include:: ../../contents-share/mcu/8051_interrupts.table.rst

.. _section_8051_mailbox:

MAILBOX
~~~~~~~

Mailbox provides 2 sets of spinlock function fields and 4 sets of 32bit information fields, allowing ACPU/8051 to transmit information to each other.