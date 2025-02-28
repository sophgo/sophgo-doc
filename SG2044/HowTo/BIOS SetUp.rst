######################
BIOS Setup
######################

BIOS Overview
=====================

BIOS (Basic Input and Output System) records hardware parameters of the system in the EFI on the
motherboard. Its major functions include conducting the Power-On Self-Test (POST) during system startup,
saving system parameters and loading the operating system, etc. BIOS includes a BIOS Setup program that
allows the user to modify basic system configuration settings or to activate certain system features.
To access the BIOS Setup program, **press <F2>** during the POST when the power is turned on.

.. parsed-literal::

      **NOTE**

      - BIOS flashing is potentially risky. If the system is functioning properly,
        **avoid flashing the BIOS**.
      - Flashing BIOS incorrectly may cause system malfunction. Proceed with caution.


The Main Menu
===============

Once you enter the BIOS Setup program, the Main Menu appears on the screen. Use
arrow keys to move among the items and press <Enter> to accept or enter other sub-menus.
Main Menu Help
The on-screen description of a highlighted setup option is displayed on the right side of the Main Menu.
Submenu Help
Press <Esc> to exit the help screen.

.. parsed-literal::

      **NOTE**

      - When the system is unstable or misconfigured, select **Restore Defaults**
        to reset your system to its default settings.

      - The BIOS Setup menus described in this chapter are **for reference only** and may
        differ based on BIOS version.

.. list-table:: **BIOS Menu Options**
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Date**
     - Displays the current system date.
   * - **Time**
     - Displays the current system time.
   * - **System Information**
     - Displays detailed system information, including BIOS version, processor details, memory specifications, and serial port configuration settings.
   * - **System Setting**
     - Provides options for configuring general system settings, including time settings, password management, and restoring factory defaults.
   * - **BMC Config**
     - Allows the user to configure **BMC (Baseboard Management Controller)** settings, including network parameters, remote access configurations, and power management.
   * - **Reserve Memory**
     - Displays and configures the amount of reserved memory allocated for system and hardware functions.
   * - **Firmware Manager**
     - Manages firmware updates and settings.
   * - **Boot Manager**
     - Allows users to configure boot priorities and manage boot entries.
   * - **Device Manager**
     - Provides options for managing system hardware devices.
   * - **Boot Maintenance Manager**
     - Offers advanced boot configuration and maintenance.
   * - **Continue**
     - Proceeds with booting the operating system.
   * - **Reset**
     - Restarts the system.
   * - **Power Off**
     - Shuts down the system.
   * - **ACPI Disable**
     - Disables ACPI (Advanced Configuration and Power Interface) functionality, to use dtb for booting kernel

System Information Menu
========================

The System Information menu provides access to hardware-related configurations.
Users can view detailed information about BIOS, CPU, memory (DDR), board, and product specifications.
Additionally, the Configuration Form allows users to check system component details
such as firmware version, processor settings, and memory configuration.
The following options are available in the Product Information menu:

.. list-table:: Product Information Menu
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **BIOS Information**
     - Click to view BIOS version, release date, and firmware details.
   * - **CPU Configuration**
     - Displays processor details such as model, core count, and frequency.
   * - **DDR Configuration**
     - Shows memory specifications, including type, size, and speed.
   * - **Board Configuration**
     - Provides motherboard details like chipset, revision, and serial number.
   * - **Product Information**
     - Displays system product model, manufacturer, and system UUID.

.. parsed-literal::

   **Navigation and Usage**

     - Use the **Up (↑) / Down (↓) arrow keys** to highlight an option.
     - Press **Enter** to access the selected submenu.
     - Press **Esc** to return to the previous menu.

Serial Port Settings
---------------------

The Serial Port Settings submenu displays the current configuration of the system's serial communication interface.
Users can view terminal type, baud rate, data bits, parity, stop bits, and flow control.
These settings should be matched in external serial communication software (e.g., PuTTY, Tera Term, Minicom)
to ensure proper data transmission and avoid miscommunication.
The following parameters are available in the Serial Port Settings menu:

.. list-table:: Serial Port Configuration
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Terminal Type**
     - Specifies the terminal emulation type used for serial communication (e.g., VT-UTF8).
       The terminal software should be set to match this type for proper display.
   * - **Baud Rate**
     - Displays the communication speed of the serial port (e.g., 115200 bps).
       The terminal software should be configured with the same baud rate.
   * - **Data Bits**
     - Specifies the number of data bits used in each transmitted character (e.g., 8 bits).
       The terminal should be set accordingly.
   * - **Parity**
     - Shows the parity bit setting for error checking (e.g., None).
       The terminal software should be configured with the same parity setting.
   * - **Stop Bits**
     - Displays the number of stop bits used in serial communication (e.g., 1 bit).
       The terminal software should match this value.
   * - **Flow Control**
     - Indicates whether hardware or software flow control is enabled (e.g., None).
       The terminal software should be configured with the corresponding flow control setting.

.. parsed-literal::

   **NOTE**

      - The **Serial Port Settings** submenu allows users to view serial communication parameters.
        These settings are read-only and cannot be modified.

      - The **Product Information** submenu is also read-only and cannot be modified.
   	Other configuration options provide detailed system specifications.

BIOS Information
-----------------

The BIOS Information submenu provides key details about the system’s firmware, including BIOS version, release date, and vendor information.
This information is useful for troubleshooting, system updates, and compatibility verification.
The following details are displayed in the BIOS Configuration menu:

.. list-table:: BIOS Configuration Information
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **BIOS Version**
     - Displays the current BIOS firmware version installed on the system (e.g., `1.0.0`).
   * - **BIOS Release Date**
     - Shows the date when the BIOS version was officially released (e.g., `20250116`).
   * - **BIOS Vendor**
     - Displays the name of the manufacturer that provided the BIOS firmware (e.g., `SOPHGO`).

.. parsed-literal::

   **Note**

      * The **BIOS Information** submenu is read-only and cannot be modified.
   	This section provides firmware details that help in system maintenance and updates.

CPU Configuration
------------------

The CPU Configuration menu provides detailed information about the system's processor, including its name, frequency, and cache sizes.
Users can view or adjust CPU frequency settings, while cache sizes are read-only.
The following parameters are displayed in the CPU Configuration menu:

.. list-table:: CPU Configuration Information
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **CPU Name**
     - Displays the model name of the installed processor (e.g., `C920`).
   * - **CPU Frequency (MHz)**
     - Indicates the current operating frequency of the CPU (e.g., `2800 MHz`).
       Users can adjust this value using the **+ / -** keys.
   * - **L1-ICache Size (KB)**
     - Shows the size of Level 1 Instruction Cache in KB (e.g., `64 KB`).
   * - **L1-DCache Size (KB)**
     - Displays the size of Level 1 Data Cache in KB (e.g., `64 KB`).
   * - **L2-Cache Size (KB)**
     - Indicates the size of Level 2 Cache in KB (e.g., `2048 KB`).
   * - **L3-Cache Size (KB)**
     - Displays the size of Level 3 Cache in KB (e.g., `65536 KB`).

.. parsed-literal::

   **Note**

      - The **CPU Name** and **Cache Sizes** are read-only and cannot be modified.
      - Adjusting the **CPU Frequency** may affect system stability and performance.
        Ensure appropriate values are set before saving changes.

DDR Configuration
------------------

The DDR Configuration menu provides essential details about the system's memory configuration.
Users can view memory type, speed, rank, and total size.
The following parameters are displayed in the DDR Configuration menu:

.. list-table:: DDR Configuration Information
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **DDR Type**
     - Displays the type of memory installed in the system (e.g., `LPDDR5`).
   * - **DDR Speed (MT/s)**
     - Indicates the memory transfer speed in MegaTransfers per second (e.g., `8533 MT/s`).
   * - **DDR Rank**
     - Shows the number of memory ranks (e.g., `2`).
   * - **DDR Size (GB)**
     - Displays the total installed memory size in GB (e.g., `64 GB`).

.. parsed-literal::

   **Note**

      - The **DDR Configuration** submenu is read-only and cannot be modified.
      - Ensure memory parameters match system requirements for optimal performance.

Board Configuration
--------------------

The Board Configuration menu provides details about the motherboard, including its product name and version.
This information is essential for system identification, troubleshooting, and firmware compatibility.
The following parameters are displayed in the Board Configuration menu:

.. list-table:: Board Configuration Information
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Board Product Name**
     - Displays the motherboard's product name (e.g., `SRA3C`).
   * - **Board Version**
     - Shows the version of the motherboard (e.g., `SOPHGO`).

.. parsed-literal::

   **Note**

      - The **Board Configuration** submenu is read-only and cannot be modified.
      - This section provides crucial details for hardware validation and system updates.

Product Configuration
----------------------

The Product Configuration menu provides essential details about the system's product identity.
Users can view the product name, version, and manufacturer information, which are crucial for
firmware updates, troubleshooting, and support.
The following parameters are displayed in the Product Configuration menu:

.. list-table:: Product Configuration Information
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Product Name**
     - Displays the official product model name (e.g., `SRA3C-40-8`).
   * - **Product Version**
     - Shows the version of the product (e.g., `1.0`).
   * - **Manufacturer**
     - Displays the name of the manufacturer (e.g., `SOPHGO`).

.. parsed-literal::

   **Note**

      - The **Product Configuration** submenu is read-only and cannot be modified.
      - This section provides crucial details for system identification, support, and maintenance.

System Setting Menu
====================

The System Setting menu provides essential options for managing system security, date and time configuration,
and restoring BIOS settings to factory defaults. Users can set a BIOS password, modify the system clock,
and restore default settings if needed.
The following options are available in the System Setting menu:

.. list-table:: System Setting Menu
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Set Password**
     - Allows users to configure a BIOS password for enhanced security.
   * - **Set Date and Time**
     - Enables users to adjust the system’s date and time settings.
   * - **Restore Defaults**
     - Restores the system settings to factory default values.
   * - **Password Enable/Disable**
     - Enables or disables password protection.

.. parsed-literal::

   **Navigation and Usage**

     - Use the **Up (↑) / Down (↓) arrow keys** to highlight an option.
     - Press **Enter** to modify settings.
     - Press **Esc** to return to the previous menu.

.. parsed-literal::

   **Note**

      - The **Set Password** option allows users to protect BIOS settings with a password.
      - The **Set Date and Time** option ensures accurate system time synchronization.
      - The **Restore Defaults** option resets all BIOS settings to their original values.
      - The **Password Enable/Disable** option enable password verification when
        entering the Setup interface

Select Language
----------------

The Select Language option in the System Setting menu allows users to change the display language of the BIOS interface.
By default, the BIOS language is set to **English**, but users can select from a list of supported languages.

Available Language Options
---------------------------

.. list-table:: Language Options
   :widths: 30 70
   :header-rows: 1

   * - **Language**
     - **Description**
   * - **English**
     - Sets the BIOS interface language to **English** (default).
   * - **Simplified Chinese (中文-简体)**
     - Sets the BIOS interface language to **Simplified Chinese**.
   * - **Français**
     - Sets the BIOS interface language to **French**.

Changing the BIOS Language
---------------------------
Navigate to the System Setting menu, then Select Select Language and
press Enter to open the language selection menu, last use the Up (↑) / Down (↓)
arrow keys to highlight the desired language, and Press Enter to confirm your selection.
Press F10 to save the changes and exit BIOS for the new language to take effect.

.. parsed-literal::

   **Note**

      - The BIOS interface will update immediately after selecting a new language,
        but some elements (such as help text) may require a reboot.
      - Not all BIOS versions support every listed language. Refer to your BIOS
        version for available language options.
      - Selecting an unsupported language may cause display issues. It is recommended
        to change the language only when necessary.

Password Config
----------------

The Password Config menu allows users to manage BIOS password settings for enhanced system security.
Users can enable or disable user passwords, set administrator and user passwords,
and restore password settings to their default values.
Once the Enable User Password option is activated, different users will have different access permissions:
**Administrator**: Full access to all BIOS settings, including enabling/disabling user passwords.
**User**: Limited access to BIOS settings; cannot disable the user password once enabled.
After enabling the user password, only an **Administrator** can modify or disable this setting.
A normal user will not have permission to disable the password protection.
The following options are available in the **Password Config** menu:

.. list-table:: Password Configuration Menu
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Enable User Password**
     - Allows enabling or disabling the user password functionality in BIOS.
       Once enabled, only an administrator can disable it.
   * - **Set Admin Password**
     - Configures an administrator-level password to protect BIOS settings.
   * - **Set User Password**
     - Sets a user-level password to restrict access to certain BIOS options.
   * - **Restore Default**
     - Resets the password settings to their factory default state.

.. parsed-literal::

   **Navigation and Usage**

     - Use the **Up (↑) / Down (↓) arrow keys** to highlight an option.
     - Press **Enter** to modify settings.
     - Press **Esc** to return to the previous menu.

.. parsed-literal::

   **Note**

      - **Enabling a user password** restricts unauthorized access to BIOS settings.
      - **Setting an administrator password** grants control over security-sensitive BIOS options.
      - **Once the user password is enabled, a normal user cannot disable it**
        only an administrator can modify or remove it.
      - **Restoring defaults** removes all set passwords and reverts to the default state.
      - **The Password setting does not support F9 to reset defaults** because EDK2's default reset
        mechanism does not support restoring custom modules. Currently, password
        settings can only be reset via the **Restore Defaults** option.

Date and Time Settings
-----------------------

The Date and Time Settings menu allows users to configure the system’s real-time clock (RTC).
Users can manually set the year, month, day, hour, minute, and second to synchronize the system clock.
Adjusting the date and time ensures accurate system logs, event scheduling, and real-time processing.
The following options are available in the Date and Time Settings menu:

.. list-table:: Date and Time Configuration
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Year**
     - Sets the system year (e.g., `2000`, `2024`).
   * - **Month**
     - Sets the system month (`1` to `12`).
   * - **Day**
     - Configures the day of the month (`1` to `31`).
   * - **Hour**
     - Sets the system hour (`0` to `23`).
   * - **Minute**
     - Configures the minute (`0` to `59`).
   * - **Second**
     - Adjusts the seconds (`0` to `59`).

.. parsed-literal::

   **Navigation and Usage**

     - Use the **Up (↑) / Down (↓) arrow keys** to highlight an option.
     - Press **Enter** to modify the selected date/time value.
     - Use **+ / - keys** to adjust the values.
     - Press **Esc** to return to the previous menu.
     - Press **F9** to reset to default values.
     - Press **F10** to save changes.

.. parsed-literal::

   **Note**

      - Setting an incorrect date/time may cause system log discrepancies.
      - Date and time adjustments will take effect immediately after saving.
      - Ensure time synchronization with external servers if required.


Firmware Manager Menu
======================

The **Firmware Manager** menu allows users to update the system firmware and configuration files.
This ensures that the system is running the latest firmware version, improving stability, security, and compatibility.
The following options are available in the Firmware Manager menu:

.. list-table:: Firmware Update Options
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Update Firmware**
     - Allows users to select and update the firmware file.
       **Warning:** Do not power off or reset the device during the update process.
   * - **Update CONF.INI**
     - Updates the system configuration file (`CONF.INI`).
       This file contains critical system settings required for proper operation.

**Firmware Update Process**

To **Updating Firmware**, First Select Update Firmware, then press Enter,
Second, Choose the new firmware file from the available storage device. Third,
Confirm the update and wait for the process to complete. Last, once the update is successful,
the system will automatically reboot.
To **Updating CONF.INI**, First Select Update CONF.INI and press Enter, Choose the new `CONF.INI` file from the available storage device. Second, Confirm the update and wait for the process to complete.Once the update is successful, the system will automatically reboot.

.. parsed-literal::

   **Navigation and Usage**

     - Use the **Up (↑) / Down (↓) arrow keys** to highlight an option.
     - Press **Enter** to initiate the selected update process.
     - Follow on-screen instructions to complete the update.
     - Press **Esc** to return to the previous menu.

.. parsed-literal::

   **Note**

      - **Firmware updates are irreversible**, ensure you have the correct update
        file before proceeding.
      - **Do not turn off the system** during the update process to avoid potential corruption.
      - **Updating CONF.INI** allows modifications to key system settings but requires caution
        to prevent misconfiguration.
      - **Both firmware and CONF.INI updates require a system reboot upon completion**.

Boot Manager Menu
==================

The Boot Manager menu allows users to select and manage boot options for the system.
Users can choose from available UEFI boot devices, configure network boot options,
and access the UEFI shell for advanced troubleshooting.
The following boot options are available in the Boot Manager menu:

.. list-table:: Boot Manager Menu
   :widths: 30 70
   :header-rows: 1

   * - **Boot Option**
     - **Description**
   * - **UEFI BootManagerMenuApp**
     - A UEFI application that allows users to manage boot options.
   * - **UEFI Misc Device**
     - A miscellaneous UEFI boot device detected by the system.
   * - **UEFI PXEv4**
     - A network boot option using PXE (Preboot Execution Environment) over IPv4.
   * - **UEFI Shell**
     - Provides access to the UEFI shell environment for system diagnostics and configuration.

The Boot Manager menu also displays the device path of the selected boot entry.
This information includes memory-mapped addresses and file paths for UEFI boot devices.
Example:
Device Path: MemoryMapped(0xB,0x81A4C000,0x8228BFFF)/FvFile(EEC25BDC-67F2-4D95-B1D5-F81B2039D11D)

.. parsed-literal::

   **Navigation and Usage**

     - Use the Up (↑) / Down (↓) arrow keys to navigate between boot options.
     - Press **Enter** to select the highlighted boot option.
     - Press **Esc** to exit the Boot Manager menu.

.. parsed-literal::

   **Note**

      - **Selecting an incorrect boot option** may result in a failed boot attempt.
      - **PXE Boot** requires network connectivity and proper DHCP configuration.
      - **UEFI Shell** should be used only by advanced users for debugging and maintenance.

Device Manager Menu
====================

The Device Manager menu provides access to hardware-related management options.
Users can monitor and manage device health status, including driver health and network device information.
The following options are available in the Device Manager menu:

.. list-table:: Device Manager Menu
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Driver Health Manager**
     - Displays a list of all driver health instances for monitoring and troubleshooting.
   * - **Network Device List**
     - Provides information about detected network devices and their status.

.. parsed-literal::

   **Navigation and Usage**

     - Use the **Up (↑) / Down (↓) arrow keys** to highlight an option.
     - Press **Enter** to access the selected submenu.
     - Press **Esc** to exit the **Device Manager** menu.

.. parsed-literal::

   **Note**

      - The **Driver Health Manager** allows users to check the health status of installed drivers.
      - The **Network Device List** provides details on available network interfaces
        and connectivity status.

Boot Maintenance Manager Menu
==============================

The Boot Maintenance Manager menu provides advanced options for managing boot configurations, driver settings, and console preferences.
Users can modify boot options, manage system drivers, adjust console settings, and boot from specific files.
The following options are available in the Boot Maintenance Manager menu:

.. list-table:: Boot Maintenance Manager Menu
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Boot Options**
     - Modify system boot options, including boot order and available boot entries.
   * - **Driver Options**
     - Manage system driver configurations, including enabling or disabling certain drivers.
   * - **Console Options**
     - Adjust system console settings such as input and output devices.
   * - **Boot From File**
     - Allows users to manually select and boot from a specific file.

**Boot Parameters**

In addition to the menu options, the Boot Maintenance Manager menu displays the following boot parameters:

.. list-table:: Boot Parameters
   :widths: 30 70
   :header-rows: 1

   * - **Parameter**
     - **Description**
   * - **Boot Next Value**
     - Specifies the next boot target. If set to `<NONE>`, the system follows the standard boot order.
   * - **Auto Boot Time-out**
     - Defines the timeout duration (in seconds) before the system automatically selects the default boot option.

.. parsed-literal::

   **Navigation and Usage**

     - Use the **Up (↑) / Down (↓) arrow keys** to highlight an option.
     - Press **Enter** to select and modify the settings.
     - Press **Esc** to return to the previous menu.

.. parsed-literal::

   **Note**

     - **Modifying boot options** allows users to customize the boot order and
        available boot entries.
     - **Driver options** help manage the initialization and execution of system drivers.
     - **Auto Boot Time-out** ensures the system automatically proceeds with booting
        if no manual selection is made.
     - **Boot from file** is useful for troubleshooting or booting custom firmware.

System Controls
================

The System Controls provides essential system management options, including system continuation, reset, power-off, and password login configuration.
System Control Options
The following options are available in the System Controls menu:

.. list-table:: System Control Options
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Continue**
     - Proceeds with normal system execution without making changes.
   * - **Reset**
     - Performs a **warm reboot** (soft reset) of the system without powering down the hardware.
   * - **Power Off**
     - Completely shuts down the system, including **MCU and chipset power**.
   * - **Password Enable/Disable**
     - Allows enabling or disabling the **password login function**.
       - **Default:** Disabled (`<Disable>`).
       - **First Login:** Users can choose to enable it.
       - **Once enabled, only an administrator can disable it.**

.. parsed-literal::

   **Navigation and Usage**

    - Use the **Up (↑) / Down (↓) arrow keys** to highlight an option.
    - Press **Enter** to execute the selected action.
    - Press **Esc** to return to the previous menu.

.. parsed-literal::

   **Note**

      - **Enabling Password Login** restricts unauthorized system access.
      - **Once enabled, only an administrator can disable the password protection.**
      - **Power Off completely shuts down all system components, including the MCU and chipset.**


BMC Network Settings
=====================

The BMC Network Settings menu allows users to configure the Baseboard Management Controller (BMC) network parameters,
including DHCP settings, manual IP configuration, and retrieving network details.

BMC Network Configuration Options
---------------------------------

.. list-table:: BMC Network Settings Menu
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Enable DHCP**
     - Enables or disables DHCP for automatic network configuration.
       - **Enable**: The system automatically obtains an IP address, subnet mask, and gateway.
       - **Disable**: Requires manual entry of IP settings.
   * - **Set BMC Network Configuration**
     - Allows users to manually configure BMC network settings, including **static IP address**, subnet mask, and gateway.
       - **This option is only available when DHCP is disabled.**
   * - **Get BMC Network Configuration**
     - Displays the current BMC network settings.

Changing BMC Network Settings
-----------------------------
First, Navigate to the BMC Network Settings menu, then Select Enable DHCP and press Enter. Second, Choose Enable to automatically obtain an IP address via DHCP.Third, Choose Disable to manually configure network settings.

.. parsed-literal::

   **Note**

     - **If DHCP is disabled**:
       - Select Set BMC Network Configuration.
       - Enter the desired IP Address, Subnet Mask, and Gateway.
     - To verify the network settings, select Get BMC Network Configuration.
       - The current BMC IP Address, Subnet Mask, and Gateway will be displayed.
       - Select Refresh to update and retrieve the latest BMC network settings.
     - Press F10 to save the changes.
     - Press Esc to return to the previous menu.
     - Enabling DHCP allows automatic IP configuration, but manual IP
       settings are disabled when DHCP is enabled.
     - BMC Network Settings are only available on server products.
        This option may not be visible or functional on non-server platforms.
     - Ensure the BMC static IP settings match your network configuration
        to avoid connectivity issues.
     - The Password setting does not support F9 to reset defaults because
        EDK2's default reset mechanism does not support restoring custom modules.
        Currently, only be reset via the **Restore Defaults** option.

Reserve Memory
===============

The Reserve Memory menu allows users to configure the amount of system memory reserved for specific hardware functions.
Users can allocate memory for TPU (Tensor Processing Unit) or disable reserved memory allocation.

Reserve Memory Configuration Options
-------------------------------------

.. list-table:: Reserve Memory Settings
   :widths: 30 70
   :header-rows: 1

   * - **Option**
     - **Description**
   * - **Reserved Memory Size (GB)**
     - Sets the amount of memory reserved for TPU operations.
       **0**: Disables TPU memory reservation.
       **[8-%d GB]**: Enables TPU with the specified memory allocation.

**Adjusting Reserved Memory**

First, Navigate to the Reserve Memory menu. Second, Use the + / - keys to adjust
the reserved memory size or directly enter the size value. To disable TPU memory
reservation, set the value to 0. Specially, To enable TPU, set the value within
the specified range (e.g., 8 GB or more). Lastest, Press **F10** to save the changes
and Press **Esc** to return to the previous menu.

.. parsed-literal::

   **Note**

      - Setting Reserved Memory to 0 disables TPU support.
      - Allocating memory to TPU may reduce available system RAM for other processes.
      - Ensure the selected reserved memory size aligns with hardware requirements
        for optimal performance.
      - Changes to the reserved memory settings will take effect only after
        clicking "Reset" or performing a power-off restart from the main menu.
      - The Password setting does not support F9 to reset defaults because
        EDK2's default reset mechanism does not support restoring custom modules.
        Currently, only be reset via the **Restore Defaults** option.

