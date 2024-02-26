Security Debugging Firewall
---------------------------

In order to provide reading or control of related internal functions of the chip during debugging or testing, the chip provides several debugging interfaces, such as JTAG, I2C and other different external interfaces. Without appropriate protection mechanisms, these interfaces can easily be exploited to directly or indirectly attack the chip security mechanism or read internal information that needs to be kept confidential. To protect and control these interfaces, the chip uses a security debug firewall.

Overview
~~~~~~~~

The chip supports three main debugging interfaces,

1. RISCV JTAG: The RISCV processor has a built-in debugging interface that allows users to access ARM internal registers through the JTAG interface.

2. I2C: The chip provides a debugging interface

3. Test interface: The chip provides a dedicated debugging interface for production testing.

For the JTAG/I2C interface, the secure debug firewall provides specific protection controls on access to it

For the Test interface interface, the security debugging interface provides an independent type of protection control (Test access) for its access.

For these debugging categories, the security debugging firewall provides three connection control states

- Open: Allows external connections via connectors without imposing additional controls.

- Protected: Does not allow external connections through the connector until the corresponding password is input through the I2C interface to unlock the protection.

- Closed: External connections are not allowed through this interface and cannot be opened again by other methods.

Status query and password input interface (I2C)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The security debugging firewall provides an independently operating I2C interface for the outside of the chip to query the current status of the debugging interface through I2C and enter the corresponding password to reopen the interface in the protected state. Externally, you need to specify the correct I2C ID to connect to the firewall interface.

The I2C interface register address is as follows

.. include:: ../../contents-share/security/firewall_i2c_query_interface.table.rst

Status inquiry and password entry process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Status inquiry process
^^^^^^^^^^^^^^^^^^^^^^

- (Step 1) Control external I2C to send out start signal.

- (Step 2) Send firewall I2C ID by I2C (default 0x56).

- (Step 3) Read address 0x04001A94 from I2C to obtain the current debug interface protection status.

Password input process
^^^^^^^^^^^^^^^^^^^^^^

- (Step 1) Control external I2C to send out start signal.

- (Step 2) The I2C ID of the debug interface firewall is sent by I2C (default 0x56).

- (Step 3) Read the address 0x04001A80 / 0x04001A84 from I2C to obtain the device ID, and read 0x04001A88 to obtain the market distinction number.

- (Step 4) Prepare the unlocking password corresponding to each category through the device serial number and market identification number.

- (Step 5) Read address 0x94 from I2C to obtain the current debug interface protection status and check whether it is locked.

- (Step 6) Taking the non-secure debug interface as an example, I2C writes the non-secure password to the address 0x04001A00 / 0x04001A04 / 0x04001A08 / 0x04001A0C.

- (Step 7) I2C writes any value to address 0x04001A10 to update the password comparison value.

- (Step 8) Read address 0x94 from I2C to obtain the current debug interface protection status and confirm whether it is unlocked.
