# Table of Contents

[TOC]

# 1. The SG200x SDK Package

## 1.1 Overview

The SG200x SDK is designed for the SG200x series of SoCs and any development boards based upon these chips. It comes with two operating systems:  Linux and FreeRTOS, with sources available as open source projects on our GitHub organization. For instructions on how to obtain and use the SG200x SDK, please refer to the following sections.

## 1.2 SDK Directories

- build: Build scripts and board-specific configurations. Used as the build directory.
- buildroot-2021.05: Buildroot toolchain sources.
- host-tools: Host toolchain.
- freertos: FreeRTOS system files.
- fsbl: FSBL firmware.
- isp_tuning: Image Signal Processing (ISP) effect tuning parameters.
- linux_5.10: Linux Kernel version 5.10.
- middleware: In-house multimedia framework with .so and .ko files.
- opensbi: OpenSBI library sources.
- osdrv: Operating system drivers.
- oss: 3rd-party libraries.
- ramdisk: Pre-built files for the minimal system.
- u-boot-2021.10: U-Boot sources.
- cvimath: A library of mathematical operations.
- cvibuilder: The library for tpu cvimodel file define.
- cviruntime: A library released as SDK for use to develop TPU application.
- cvikernel: A library for TPU instruction generation, serving as assembly.
- flatbuffers: 3rd-party open source libraries.
- cnpy: A tool that provides c++ interface to read and write npy, npz data format
- install: Artifact directory for built system images.

# 2. Deploying the SDK

This section introduces the procedures for deploying the SG200x SDK. The current SDK only supports Linux and comes with a compiler toolchain built for Linux.

## 2.1 The Linux Development Server

The developer may choose between one of the following development server configurations:

- An Ubuntu computer.
- A Windows computer with a configured Ubuntu environment.

For both methods above, we recommend using **Ubuntu 22.04 LTS or newer**.

- Virtualbox VM: You may obtain VirtualBox to install an Ubuntu virtual machines. [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- Docker: You may install Docker Desktop for Windows and deploy a Ubuntu container. [Download Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
- Ubuntu 22.04 LTS: [Download system installation media](https://www.releases.ubuntu.com/22.04/ubuntu-22.04.3-desktop-amd64.iso)

### 2.1.1 Installing Ubuntu in VirtualBox

- Creating and naming the virtual machine.

[![pFBTKFx.png](https://s11.ax1x.com/2024/03/04/pFBTKFx.png)](https://imgse.com/i/pFBTKFx)

- Allocate 8GB of RAM for the virtual machine.

[![pFBTQfK.png](https://s11.ax1x.com/2024/03/04/pFBTQfK.png)](https://imgse.com/i/pFBTQfK)

- Allocate 200GB of storage space to allow space for the SDK.

[![pFBTakt.png](https://s11.ax1x.com/2024/03/04/pFBTakt.png)](https://imgse.com/i/pFBTakt)

- Mount the installation media (.iso) on first boot.

[![pFBTBp8.png](https://s11.ax1x.com/2024/03/04/pFBTBp8.png)](https://imgse.com/i/pFBTBp8)

- Commence installation.

[![pFBLHFs.png](https://s11.ax1x.com/2024/03/04/pFBLHFs.png)](https://imgse.com/i/pFBLHFs)

- Configure the VirtualBox Host-only Ethernet Adapter to ease networking (terminal services and file sharing) between the host and virtual machine.

Note: The above screenshots are taken for Ubuntu 20.04, please refer to the recommended version above whilst you install Ubuntu.

### 2.1.1.1 Installing Samba Server

In the VirtualBox configuration, you need to install the Samba suite to ease file sharing between the host computer and the virtual machine. Before you install Samba, please note the IP configuration details from the virtual machine.

The virtual machine may not come pre-installed with net-tools. You may install the said package using the following commands:

```
sudo apt install net-tools
sudo apt-get install samba samba-common
```

Create a Samba password (using the `sophgo` user as an example, you may want to replace it with your user name):

```
sudo smbpasswd -a cvitek
```

Edit `/etc/samba/smb.conf` and append the following:

```
[sophgo]
path = /home/sophgo
writable = yes
browseable= yes
valid users = sophgo
```

Start the Samba server:

```
sudo service smbd restart
```

You may now connect to the Samba server from Windows using the server IP.

Refer to 2.2 for instructions on installing build dependencies.

### 2.1.2 Deploying an Ubuntu Docker Container

- After installing Docker, you may use the `docker pull ubuntu:22.04` command in the Command Prompt to pull an Ubuntu 22.04 container image.
- Use `docker images` to see all fetched images.
- Run `docker run -it ubuntu:22.04 /bin/bash` to launch a container. When you see the `root@<string>:/#` prompt, you have now entered the container - with `string` denoting the container ID, or `containerID`.

If you need to exit the container, simply input the `exit` command. If you would like to enter the container again, simply run the `docker start <containerId>` and `docker attach <containerId>` commands in successing order.

See also the official Docker documentation for more usage details.

### 2.1.3 Installing the SSH Server

To install the SSH server:

```
sudo apt-get install ssh
sudo apt-get install openssh-server
```

Now, perform some extra SSH configuration, such as default port, password authentication, and root authentication:

```
sudo vim /etc/ssh/sshd_config
```

And append the following:

```
Port 22
PasswordAuthentication yes
PermitRootLogin yes
```

After which, restart the SSH server:

```
sudo /etc/init.d/ssh restart
```

## 2.2 Installing Build Dependencies

In a prepared Linux environment, install the build dependencies using the following commands:

```
sudo apt update
sudo apt install -y pkg-config build-essential ninja-build automake autoconf libtool wget curl git gcc libssl-dev bc slib squashfs-tools android-sdk-libsparse-utils jq python3-distutils scons parallel tree python3-dev python3-pip device-tree-compiler ssh cpio fakeroot libncurses5 flex bison libncurses5-dev genext2fs rsync unzip dosfstools mtools tcl openssh-client cmake expect
```

- Please note: The SDK requires `CMake >= 3.16.5`. If your system environment does not come with a suitable CMake version, please install a local copy (installing any requested dependencies as needed):

```
wget https://github.com/Kitware/CMake/releases/download/v3.27.6/cmake-3.27.6-linux-x86_64.sh
chmod +x cmake-3.27.6-linux-x86_64.sh
sudo sh cmake-3.27.6-linux-x86_64.sh --skip-license --prefix=/usr/local/
```

- The local `cmake` executable will be available in `/usr/local/bin`. Use the `cmake --version` command to verify its version.

# 3. Preparing to Install the SDK

## 3.1 Git Configuration

Before you clone the repository, please set up your Git credentials to prevent issues with the GitHub hook:

```
git config --global user.name "your name"
git config --global user.email "your mail"
```

Setting a large enough global `postBuffer` value to prevent EOF errors whilst pulling from the remote repositories:

```
git config --global http.postBuffer 2147483648
```

## 3.2 Obtaining the SDK

### 3.2.1 Using the Automated Scripts

- The SDK repository manages its child repositories with an automatic script. Use the following command to fetch the SDK:

```
git clone https://github.com/kubuds/sophpi/tree/sg200x-evb
cd sophpi
./scripts/repo_clone.sh --gitclone scripts/subtree.xml
```

The script uses SSH to fetch repositories. Please make sure that you have [configured a public key for your GitHub account](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

Alternatively, you may use the HTTPS URLs by replacing the following line in `./scripts/repo_clone.sh`:
`REMOTE_URL=$(grep -o '<remote.*/>' ${dir} | sed 's/.*fetch="\([^"]*\)".*/\1/' | sed "s/ssh:\/\/\(.*\)/ssh:\/\/$USERNAME@\1/")`

With the following:

`REMOTE_URL=$(grep -o '<remote.*/>' ${dir} | sed 's/.*fetch="\([^"]*\)".*/\1/' | sed "s/git@\(.*\):/https:\/\/\1\//")`

After editing the script, please refer to the project directories to make sure that you have fetched all necessary repositories. If your GitHub account has two-factor authentication (2FA) enabled, you may need to authenticate using your Personal Access Token. In this situation, please authenticate using your GitHub user name and your Personal Access Token as its password.

> Notice: We recommend you to use SSH to clone the code. SSH protocol will encrypt the data when sending data, making the data transmission more secure, and effectively reduce the risk of clone failure.

### 3.2.2 Fetching Repositories Manually

If using the automated script is not an option, please fetch the repositories manually:

```
mkdir sophpi -p && cd sophpi
git clone https://github.com/kubuds/host-tools/tree/master
git clone https://github.com/kubuds/buildroot-2021.05/tree/sg200x-dev
git clone https://github.com/kubuds/build/tree/sg200x-dev
git clone https://github.com/kubuds/oss/tree/master
git clone https://github.com/kubuds/freertos/tree/sg200x-dev
git clone https://github.com/kubuds/Lab-Project-FreeRTOS-POSIX/tree/sg200x-dev freertos/Source/FreeRTOS-Plus-POSIX
git clone https://github.com/kubuds/FreeRTOS-Kernel/tree/sg200x-dev freertos/Source
git clone https://github.com/kubuds/fsbl/tree/sg200x-dev
git clone https://github.com/kubuds/opensbi/tree/sg200x-dev
git clone https://github.com/kubuds/u-boot-2021.10/tree/sg200x-dev
git clone https://github.com/kubuds/linux_5.10/tree/sg200x-dev
git clone https://github.com/kubuds/osdrv/tree/sg200x-dev
git clone https://github.com/kubuds/ramdisk/tree/sg200x-dev
git clone https://github.com/kubuds/middleware/tree/sg200x-dev
git clone https://github.com/kubuds/isp_tuning/tree/sg200x-dev
git clone https://github.com/kubuds/SensorSupportList/tree/sg200x-dev
git clone https://github.com/kubuds/cvimath/tree/sg200x-dev
git clone https://github.com/kubuds/cvikernel/tree/sg200x-dev
git clone https://github.com/kubuds/cviruntime/tree/sg200x-dev
git clone https://github.com/kubuds/cvibuilder/tree/sg200x-dev
git clone https://github.com/kubuds/flatbuffers/tree/master
git clone https://github.com/kubuds/cnpy/tree/tpu
```

After which, you may use the normal procedures to fetch and build the SDK.

## 3.3 Updating the SDK

1. If you have fetched the sophpi SDK using the automated script, you may update the SDK components with the following command:

```
./scripts/repo_clone.sh --gitpull scripts/subtree.xml
```

2. If you manually fetched the SDK repositories, please reference the following script to manage updates for the said repositories:

```bash
#!/bin/bash

repos_dir="./"

for dir in "$repos_dir"/*; do
    if [ -d "$dir" ]; then
        cd "$dir" || exit
        if [ -d ".git" ]; then
            echo "Updating $(basename "$dir")"
            git pull
        else
            echo "$(basename "$dir") is not a Git repository, skipping..."
        fi
        cd - > /dev/null || exit
    fi
done
```

You may also want to give your script the executable bit:

```
chmod +x yourscript.sh
```

## 3.4 Reporting SDK Issues

If you have any questions or feedback for the SDK repositories, please get in touch with us via e-mail:

- [kenneth.liu@sophgo.com](kenneth.liu@sophgo.com)
- [sijie.wang@sophgo.com](sijie.wang@sophgo.com)
- [runze.lin@sophgo.com](runze.lin@sophgo.com)

The repository maintainers will review and act upon your suggestions to help users carry out their development work.

# 4 Building the SDK

The SDK, based on operating systems, offers two versions for ARM and RISC-V, respectively. The user may configure and build a version as they see fit.

## 4.1 Notes on Variables

Before you start building the SDK, you would want to set two environmental variables:

- `$CHIP` to specify the SoC.
- `$BOARD` to specify the board.

Please make sure that the `$BOARD` variable is set correctly, as each board may come with different requirements for peripheral drivers. You may find your board model using the laser-etched model numbers on your board.

## 4.2 Configuring the SDK Packages

- First, switch to the SDK's root directory and source the environmental settings:

```
source build/envsetup_soc.sh
```

- After which, you will be greeted with the following prompts:

```
  -------------------------------------------------------------------------------------------------------
    Usage:
    (1) menuconfig - Use menu to configure your board.
        ex: $ menuconfig

    (2) defconfig $CHIP_ARCH - List EVB boards($BOARD) by CHIP_ARCH.
       ** cv181x ** -> ['cv181x', 'cv1811h', 'cv1811c', 'cv1810c', 'cv1810h', 'cv1812cp', 'cv1812h', 'cv1813h', 'sg2000', 'sg2002']
       ** cv180x ** -> ['cv180x', 'cv1800b', 'cv1800c', 'cv1801b', 'cv1801c', 'cv180zb']
        ex: $ defconfig cv181x

    (3) defconfig $BOARD - Choose EVB board settings.
        ex: $ defconfig cv1813h_wevb_0007a_spinor
        ex: $ defconfig cv1812cp_wevb_0006a_spinor
  -------------------------------------------------------------------------------------------------------
```

The SDK environment is now initialized. You may configure the SDK using two different methods, as outlined below.

### 4.2.1 Configuring the SDK with defconfig

- You may use the `defconfig cv181x` command to list all currently supported development boards.

```
* cv181x * the avaliable cvitek EVB boards
 cv1811h - cv1811h_wevb_0007a_emmc [C906B + EMMC 512MB + BGA SIP 128MB]
           cv1811h_wevb_0007a_spinand [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1811h_wevb_0007a_spinor [C906B + SPINOR 16MB + BGA SIP 128MB]
 cv1811c - cv1811c_wdmb_0006a_spinor [C906B + SPINOR 16MB + BGA SIP 128MB]
           cv1811c_wevb_0006a_emmc [C906B + EMMC 8192MB + BGA SIP 128MB]
           cv1811c_wevb_0006a_spinand [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1811c_wevb_0006a_spinor [C906B + SPINOR 16MB + BGA SIP 128MB]
 cv1810c - cv1810c_wdmb_0006a_spinor [C906B + SPINOR 8MB + QFN SIP 64MB]
           cv1810c_wevb_0006a_spinand [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1810c_wevb_0006a_spinor [C906B + SPINOR 16MB + QFN SIP 64MB]
 cv1810h - cv1810h_wevb_0007a_spinor [C906B + SPINOR 8MB + BGA SIP 64MB]
cv1812cp - cv1812cp_sophpi_duo_sd [C906B + EMMC 8192MB + BGA SIP 256MB]
           cv1812cp_wevb_0006a_emmc [C906B + EMMC 8192MB + BGA SIP 256MB]
           cv1812cp_wevb_0006a_spinand [C906B + SPINAND 256MB + BGA SIP 256MB]
           cv1812cp_wevb_0006a_spinor [C906B + SPINOR 16MB + QFN SIP 256MB]
 cv1812h - cv1812h_wevb_0007a_emmc [C906B + EMMC 512MB + BGA SIP 256MB]
           cv1812h_wevb_0007a_emmc_huashan [C906B + EMMC 512MB + BGA SIP 256MB]
           cv1812h_wevb_0007a_spinand [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1812h_wevb_0007a_spinand_huashan [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1812h_wevb_0007a_spinor [C906B + SPINOR 16MB + BGA SIP 256MB]
           cv1812h_wevb_0007a_spinor_huashan [C906B + SPINOR 16MB + BGA SIP 256MB]
 cv1813h - cv1813h_wevb_0007a_emmc [C906B + EMMC 512MB + BGA SIP 256MB]
           cv1813h_wevb_0007a_spinand [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1813h_wevb_0007a_spinor [C906B + SPINOR 16MB + BGA SIP 256MB]
  sg2000 - sg2000_wevb_arm64_sd [CA53 + SPINOR 16MB + BGA SIP 128MB]
           sg2000_wevb_riscv64_sd [C906B + EMMC 8192MB + DDR 512MB]
  sg2002 - sg2002_wevb_arm64_sd [CA53 + SPINOR 16MB + BGA SIP 128MB]
           sg2002_wevb_riscv64_sd [C906B + EMMC 8192MB + DDR 256MB]
```
Switch out the second parameter to configure the SDK for a specific board, such as `defconfig sg2000_wevb_riscv64_sd`.

You may choose the RISC-V configuration or ARM configuration as needed.

### 4.2.2 Configuring the SDK with menuconfig

- You may use the `menuconfig` to launch a menu-based configuration for each internal SDK features, including chip and EVB models:

```
(Top)
                          CViTek MediaSDK Configuration
(generic) Customer define
    Chip selection (sg2002)  --->
    Board selection (duo_sd (C906B + EMMC 512MB + BGA SIP 256MB))  --->
    DDR configuration selection (ddr3_1866_x16)  --->
(riscv) Arch define
    Compile-time checks and compiler options  --->
    SDK options  --->
    FIP setting  --->
    Storage settings  --->
    Sensor settings  --->
    Panel settings  --->
    uboot options  --->
    Kernel options  --->
    ROOTFS options  --->
    Turnkey options  --->
    RTOS options  --->
    Rootfs packages  --->


[Space/Enter] Toggle/enter  [ESC] Leave menu           [S] Save
[O] Load                    [?] Symbol info            [/] Jump to symbol
[F] Toggle show-help mode   [C] Toggle show-name mode  [A] Toggle show-all mode
[Q] Quit (prompts for save) [D] Save minimal config (advanced)
```

Following the instructions at the bottom of the screen, you may navigate the configuration menu. For instance, you may use Enter/Space/Esc to enter/toggle/return. After you have completed the configuration, press S to save the configuration and Q to exit the configuration menu (or press Esc to toggle an exit menu).

- To choose the SoC: Enter the "Chip selection" menu to select the appropriate model.
- To switch the architecture: Enter the "Arch define" menu to, input "riscv" or "arm" to select your target architecture.
- ROOTFS configuration: Enter the "ROOTFS Options" menu, and make sure you select the `Enable buildroot generate rootfs` to enable the buildroot construction.

## 4.3 Building A Complete SDK

After configuring the SDK, you may use the `clean_all && build_all` command to start building the SDK. After the compilation completes, you may find the built system package `upgrade.zip` under the `install/` directory.

By running in addition the `pack_burn_image` command, the build system will generate a system image, such as `sophpi-duo-XXX.img`. Should the build process fail with an error, please make sure that your files are complete, whether you needed to update your repositories, and perform the build process as instructed.

```
clean_all && build_all
pack_burn_image
```
> Notice: However you choose to configure the SDK, please always use `menuconfig` command to check if `Enable buildroot generate rootfs` option is selected. If not, the system may fail to boot.

## 4.4 Building SDK Components

### 4.4.1 Building U-Boot

Each EVB will load U-Boot from a specific location, perform all necessary initialization operations or define a specific PINMUX. Usually, board-specific U-Boot sources are located at:

`./build/boards/sg200x/$CHIP_$BOARD/u-boot/cvi_board_init.c`

With their default configurations located at:

`./build/boards/sg200x/$CHIP_$BOARD/u-boot/$CHIP_$BOARD _defconfig`

After configuring U-Boot using `$ menuconfig_uboot`, the resulted configuration can be found at:

`./u-boot-2021.10/build/"$CHIP"_"$BOARD"/.config`

Switch to the project root and run the following command to generate a `flip.bin` in the `install/` directory:

`$ build_uboot`

### 4.4.2 Building the Linux Kernel

To build the Linux Kernel after editing the sources (e.g., *.dts, *.c, etc.), please note the following file locations.

Each EVB will have their own device tree configuration (*.dts), located at:

`./build/boards/sg200x/"$CHIP"_"$BOARD"/dts_riscv/"$CHIP"_"$BOARD".dts`

With their default configurations located at:

`./build/boards/sg200x/"$CHIP"_"$BOARD"/linux/"$CHIP"_"$BOARD"_defconfig`

After configuring U-Boot using `$ menuconfig_kernel`, the resulted configuration can be found at:

`./linux/build/"$CHIP"_"$BOARD"/.config`

Switch to the project root and run the following command to generate a `boot.sd` in the `install/` directory:

`$ build_kernel`

### 4.4.3 Building Middleware

Switch to the project root and run the following command to build middleware:

`$ build_middleware; pack_rootfs`

The `build_middleware` command will rebuild sensor drivers (located in `middleware/v2/component/isp/`) and sample applications (located in `middleware/v2/sample/`). The rebuilt components will be included in the burnable image by the `pack_rootfs` command.

## 4.5 Customizing the Partition Schema

The partition schema is located in `build/boards/<CHIP>/<EVB_Name>/partition/partion_<physical_partition>.xml`
Take for example `sg2002_duo_sd`'s partition schema:

```xml
<physical_partition type="sd">
    <partition label="BOOT" size_in_kb="80960" readonly="false" file="boot.sd"/>
    <partition label="ROOTFS" size_in_kb="204800" readonly="false" file="rootfs.sd" />
    <partition label="DATA"  size_in_kb="512000" readonly="false" file="data.sd" mountpoint="/mnt/data" type="ext4" />
</physical_partition>
```

- physical_partition type: Type of flash device.
- partition label: Partition names.
- size_in_kb: Partition sizes.
- file: Filename of the image.
- type: (Under the partition configuration) Filesystem of the partition.
- mountpoint: Mount point of the partition.

# 5. SDK Firmware Update

This section outlines the processes to build system images for burning on the target devices. The SDK supports burning via SD cards and USB.

## 5.1 SD Card Burning

### 5.1.1 Procedure Visualization

[![pFBLIeg.png](https://s11.ax1x.com/2024/03/04/pFBLIeg.png)](https://imgse.com/i/pFBLIeg)

### 5.1.2 Prerequisites

You would need the following before burning your target boards:

- A built system image.
- A MicroSD card formatted in FAT32.

### 5.1.3 Notes on Procedures

> Caution: The image burning procedure will erase all contents on the SD card, please backup all necessary data!

- Place the image in the SD card (raw image or `upgrade.zip`).
- Insert the SD card in the EVB's SD card slot.
- Reset the platform.

#### 5.1.3.1 Writing the Raw Image

- Under Windows, you may use `balenaEtcher`，`Rufus`, or `Win32 Disk Imager` to write the generated image in the SD card.
- Under Linux, you may use the `dd` command to write the SD card image:

```
sudo dd if=sophpi-duo-XXX.img of=/dev/sdX
```

#### 5.1.3.2 Writing the upgrade.zip

- Connect the EVB's serial cable.
- Extract and copy the content of the `upgrade.zip` archive under the root directory of the SD card. Depending on the specific model of your board, the content of the archive may be different:

```
soc_sg2002_duo_sd
.
├── boot.sd
├── META/
├── partition_sd.xml
├── rootfs.sd
└── utils/
```

Then, insert the SD card in the board's card slot. Power on the board to initiate the burning process. After which, remove the SD card and reset the board to boot the pre-built system.

## 5.2 Burning via USB

### 5.2.1 Prerequisites

Install Python 3 and Pip using [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Then run the following command to install pyserial:

```
python -m pip install pyserial
```

You will also need a pre-built system image.

### 5.2.2 Notes on Procedures

Please refer to the [Cvitek Bare and Non-Bare Chip Burning Upgrade Operation Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Cvitek_Bare_and_Non-Bare_Chip_Burning_Upgrade_Operation_Guide/build/html/index.html) for details.

#### 5.2.2.1 Windows

1. Prepare the firmware directory by extracting the `upgrade.zip` archive.
2. Connect the UART headers on a powered-down target board to the host computer and run the following commands:

```
cd <path\to\project\>\build\tools\cv181x\usb_dl\
py cv181x_dl.py –libusb –image_dir <firmware path>
```

3. After the commands have completed, power on the target board.

#### 5.2.2.2 Linux

1. Prepare the firmware directory by extracting the `upgrade.zip` archive.
2. Connect the UART headers on a powered-down target board to the host computer and run the following commands:

```
cd <path/to/project>/build/tools/cv181x/usb_dl/
py cv181x_dl.py –libusb –image_dir <firmware path>
```

3. After the commands have completed, power on the target board.

### 5.2.3 Caution

1. When burning via USB, please power the target board using USB and ensure that the DC power input has been disconnected.
2. If the script does not exit, use Ctrl+C to abort. Ensure that the target board is powered down, restart the process.

## 5.3 Root Filesystem (rootfs)

### 5.3.1 Introduction

The Linux Kernel is the core to a Linux-based operating system, whereas the filesystem is the primary user interface. The root filesystem, or `/`, is a directory tree containing all system files. When the kernel image (uImage) boots, it would mount a storage device (e.g., eMMC) as the root device (usually found on non-volatile and internal storage devices, or network file systems such as NFS).

All applications and libraries are stored as categorised in the root filesystem, as follows:

```
/ - root directory
├── bin - executables
├── dev - device nodes
├── etc - system configuration files (e.g., boot configuration)
├── home - user data
├── init - initialization script
├── kdump - kernel memory dumps
├── lib - application libraries (Glibc, shared librarires, and kernel modules)
├── mnt - temporary mountpoints for filesystems
├── proc - virtual filesystem for kernel processes
├── sbin - administrative executables
├── sys - system device, file mapping, and kernel runtime data
├── usr - user applications and program data
└── var - system logs and service runtime data
```

### 5.3.2 Rootfs

This section describes the filesystem components as found in `ramdisk/rootfs/`.

### 5.3.3 Pre-built Root Filesystems

The pre-built root filesystems can be categorized as three types, which overlays upon one another.

__Basic Root Filesystems__

Our company provides pre-built root filesystems for four architectures:

| Arch | Libc |	Pre-build ramdisk path |
|:--------| :---------|:--------|
| Arm | glibc |ramdisk/rootfs/common_arm/|
| Arm | uclibc |ramdisk/rootfs/common_uclibc/|
| Aarch64 | glibc |ramdisk/rootfs/common_arm64/|
| Riscv64| glibc |ramdisk/rootfs/common_riscv64/|
| Riscv64 | musl |ramdisk/rootfs/common_musl64/|

- **Processor Configuration Root Filesystems**

We provide processor-specific boot configuration as overlays in `ramdisk/rootfs/overlay/$CHIP`.

- **Third-party Root Filesystems**

We provide 3rd-party application libraries, utilities, and related files in `ramdisk/rootfs/public/`.

# 6. Notes on Network Security During SDK Development

This section outlines solutions for network security threats during SDK development.

## 6.1 Notes on U-Boot

### 6.1.1 Serial Port

The U-Boot enables serial port functionalities by default. Whilst U-Boot executes, U-Boot waits 1 second for interrupt key input for debugging - otherwise, U-Boot boots up as normal. In production images, you may disable this one-second interval to prevent access to serial debugging.

Edit the `build/boards/{processor_name}/{board_name}/u-boot/{board_name}_defconfig` file and edit the `CONFIG_BOOTDELAY` option with a value of `-2`.

```
CONFIG_IDENT_STRING="soph"
CONFIG_BOOTDELAY=-2
```

After which, rebuild U-Boot.

### 6.1.2 U-Boot Commands

U-Boot ships with many commands for development and debugging, such as `md`, `mw`, `setenv`, `saveenv`, etc. These commands are probably not needed in production images - you may disable or delete them as appropriate.

For instance, to remove the `md` and `mw` command, edit `/u-boot-2021.10/cmd/Makefile` and, as the `md` and `mw` commands are implemented by `mem.c`, comment or remove the line with `mem.o`:

```
obj-$(CONFIG_LOGBUFFER) += log.o
obj-$(CONFIG_ID_EEPROM) += mac.o
obj-$(CONFIG_CMD_MD5SUM) += md5sum.o
#obj-$(CONFIG_CMD_MEMORY) += mem.o
obj-$(CONFIG_CMD_IO) += io.o
obj-$(CONFIG_CMD_MFSL) += mfsl.o
```

Alternatively, edit `/u-boot-2021.10/cmd/Kconfig` to set `CMD_MEMORY`'s default value to `n`:

```
config CMD_MEMORY
  bool "md, mm, mw, cp, cmp, base, loop, ip_update"
  default n
  help
    Memory commands.
      md - memory display
      mm - memory modify (auto-incrementing address)
      mw - memory write (fill)
      cp - memory copy
      cmp - memory compare
      base - print or set address offset
      loop - initialize loop on address range
      ip_update - sync ip from mem 0x400038C/900 to uboot env
```

You may reference these procedures for other unneeded commands.

## 6.2 Notes on Linux Network Security

### 6.2.1 The "root" Account

It is recommended to make changes to the "root" account's security policies in the production images. You may decide on whether to disable root login or shell access.

- **Changing the Default Password**

1. Change the root account's password using `passwd`.
2. Copy the `/etc/shadow` file via a mounted SD card or over the network.
3. Copy the `shadow` file into `/ramdisk/rootfs/overlay/{processor_name}/etc`.
4. Rebuild the root filesystem with `pack_rootfs` and program the `rootfs.spinor`/`rootfs.sd` image.

- **Disabling root Shell Access**

Edit `/ramdisk/rootfs/overlay/{processor_name}/etc/passwd`, changing the line:

```
root:x:0:0:root:/root:/bin/sh
```

Into:

```
root:x:0:0:root:/root:/bin/false
```

Rebuild the root filesystem with `pack_rootfs` and program the `rootfs.spinor`/`rootfs.sd` image.

### 6.2.2 File Permissions

The SG200x SDK uses the SquashFS. The user may not edit or delete preloaded files. This would help ensure system security.

## 6.3 Linux Drivers and Network Security

### 6.3.1 Serial Port

Developers may use the serial port to debug Linux systems, but the serial port may be illegally accessed. To ensure that the serial port is disabled in your final product, we would want to disable the serial port.

To disable the serial port, edit `build/boards/{processor_name}/{board_name}/dts_{arch}/{processor_name}/ {processor_name}.dtsi` in accordance to the following diff output:

```
uart0: serial@04140000 {
compatible = "snps,dw-apb-uart";
reg = <0x0 0x04140000 0x0 0x1000>;
clock-frequency = <25000000>;
reg-shift = <2>;
reg-io-width = <4>;
- status = "okay";
+ status = "disabled";
};
```

After which, rebuild the Linux Kernel.

## 6.4 Notes on Application Security

### 6.4.1 CIPHER Drivers

CIPHER is a secure algorithm module for the SG Smart Digital Media Processing Platform. The module provides support for symmetrical cryptographic algorithms such as AES/DES/SM4, asymmetric cryptographic algorithms such as RSA, random number generators, and checksum algorithms such as HASH and HMAC. The client may make use of this module to encrypt their audio and video streams or to authenticate media licenses.

Please refer to the [Cvitek CIPHER API Reference](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/CIPHER_API_Reference/build/CIPHERAPIReference_zh.pdf) for details.

## 6.5 Other Notes on Security

### 6.5.1 Bare Chip Burning

The Cvitek SDK ships with support for bare-chip burning via SD card or USB connections. It is recommended to disable the said functionalities on production boards, and can also be disabled on the hardware level.

### 6.5.2 Mounting Permission for SD Cards and USB Flash Drives

If the production boards come with SD card slots or USB ports, it is recommended to append `-o noexec` to the default mounting parameters. This will prevent 3rd-party applications to be launched from externally connected storage devices.

### 6.5.3 JTAG

We recommend removing the JTAG port on the production boards to prevent malicious physical access.

## 6.6 AliOS Developer Documentation

Please refer to the [AliOS's developer documentation](https://github.com/alibaba/AliOS-Things/tree/master/documentation).

# 7. Appendix: References

This section indexes chip-specific platform documentation, such as datasheets and technical reference manuals (TRMs). It also lists extra references for further studies.

## 7.1 Platform Documentation

### 7.1.1 Datasheets

- [SG2000 Datasheet](https://github.com/sophgo/sophgo-doc/releases/tag/sg2000-datasheet-v1.0-alpha)
- [SG2002 Datasheet](https://github.com/sophgo/sophgo-doc/releases/tag/sg2002-datasheet-v1.0-alpha)

### 7.1.2 Technical Reference Manual

- [SG2000 Technical Reference Manual](https://github.com/sophgo/sophgo-doc/releases/tag/sg2000-trm-v1.0-alpha)
- [SG2002 Technical Reference Manual](https://github.com/sophgo/sophgo-doc/releases/tag/sg2002-trm-v1.0-alpha)

We also supplies a bilingual beta edition, open sourcing the manual's source RST files. We encourage users to file issues and pull requests as they deem necessary to further enrich and enhance the reference documents.

- [SG2000 TRM: Bilingual v1.0-beta](https://github.com/sophgo/sophgo-doc/releases/tag/sg2000-trm-v1.0-beta)
- [SG2002 TRM: Bilingual v1.0-beta](https://github.com/sophgo/sophgo-doc/releases/tag/sg2002-trm-v1.0-beta)

### 7.1.3 Hardware Development Guides

The generic hardware development documentation outlines basic board-specific features and functionalities, hardware interfaces, and usage with an aim to help developers make the best use of the evaluation boards (EVBs). Please see under `/sophgo-hardware/SG200X/$CHIP_NAME` in the [sophgo-hardware](https://github.com/sophgo/sophgo-hardware/tree/master/SG200X) repository for detail.

<table>
   <tr>
        <td>Index</td>
        <td>Documentation</td>
        <td>Notes</td>
   </tr>
   <tr>
        <td>01_Document Description</td>
        <td>SG200x HDK Instruction</td>
        <td></td>
    </tr>
    <tr>
        <td rowspan="12">02_SG200X_Common_HW_DOC</td>
  		  <td>01_SOPHGO EMI Common analysis approaches and measures</td>
        <td></td>
    </tr>
    <tr>
        <td>02_SOPHGO audio hardware, structural design and device selection instructions</td>
        <td></td>
    </tr>
    <tr>
        <td>03_SOPHGO key components list</td>
        <td></td>
    </tr>
    <tr>
        <td>04_Hardware test report template</td>
        <td></td>
    </tr>
    <tr>
        <td>05_SOPHGO PCBA chip factory production precautions</td>
        <td></td>
    </tr>
    <tr>
        <td>06_SMT Furnace temperature graph</td>
        <td></td>
    </tr>
    <tr>
        <td>07_EMMC test method</td>
        <td></td>
    </tr>
    <tr>
        <td>08_SPINAND test method</td>
        <td></td>
    </tr>
    <tr>
        <td>09_SG200x_VO_VI Interface Detailed Scenario Description</td>
        <td></td>
    </tr>
    <tr>
        <td>10_SOPHGO_WiFi_Support_List</td>
        <td></td>
    </tr>
    <tr>
        <td>11_SOPHGO_Sensor_Support_List</td>
        <td></td>
    </tr>
    <tr>
        <td>12_SOPHGO_Flash_Support_List</td>
        <td></td>
    </tr>
    <tr>
        <td rowspan="11">03_SG2000</td>
  		  <td>01_SG2000_Datasheet</td>
        <td></td>
    </tr>
    <tr>
        <td>02_SG2000_Hardware Design User Guide</td>
        <td>Hardware Design Guide</td>
    </tr>
    <tr>
        <td>03_SG2000_BGA_EVB Board Hardware Guide</td>
        <td>EVB Board Hardware Design Guide</td>
    </tr>
    <tr>
        <td>04_SG2000_PINOUT</td>
        <td>PIN_OUT</td>
    </tr>
    <tr>
        <td>05_SG2000_BGA_GPIO list</td>
        <td></td>
    </tr>
    <tr>
        <td>06_SOPHGO_Demo_SCH&PCB_4L</td>
        <td></td>
    </tr>
    <tr>
        <td>07_EVB&development board SCH&PCB Bitmap</td>
        <td></td>
    </tr>
    <tr>
        <td>08_SG2000_4L_6L_PCB_Layout Guide</td>
        <td></td>
    </tr>
    <tr>
        <td>09_SG2000 BGA chip impedance test reference table</td>
        <td></td>
    </tr>
    <tr>
        <td>10_SG2000_Schematic symbol</td>
        <td></td>
    </tr>
    <tr>
        <td>11_SG2000_PCB package</td>
        <td></td>
    </tr>
    <tr>
        <td rowspan="11">04_SG2002</td>
  		  <td>01_SG2002_Datasheet</td>
        <td></td>
    </tr>
    <tr>
        <td>02_SG2002_Hardware Design User Guide</td>
        <td>Hardware Design Guide</td>
    </tr>
    <tr>
        <td>03_SG2002_QFN_EVB Board Hardware Guide</td>
        <td></td>
    </tr>
    <tr>
        <td>04_SG2002_PINOUT</td>
        <td></td>
    </tr>
    <tr>
        <td>05_SG2002_QFN_38 Board GPIO List</td>
        <td></td>
    </tr>
    <tr>
        <td>06_SG2002_38 Board_2L_SCH&PCB</td>
        <td></td>
    </tr>
    <tr>
        <td>07_SG2002_38 Board_4L_SCH&PCB</td>
        <td></td>
    </tr>
    <tr>
        <td>08_SG2002_4L_PCB38x38mm2_Layout Guide</td>
        <td></td>
    </tr>
    <tr>
        <td>09_SG2002_QFN88 chip impedance test reference table</td>
        <td></td>
    </tr>
    <tr>
        <td>10_SG2002_Schematic symbol</td>
        <td></td>
    </tr>
    <tr>
        <td>11_SG2002_PCB package</td>
        <td></td>
    </tr>
</table>



## 7.2 Linux Development Environment User Guide

This documentation introduces frequently used procedures for deploying a Linux development environment, including deployment of development tools, descriptions on building and installing U-Boot, Linux Kernel, and the rootfs. It also includes instructions on network configuration and SDK deployment.

- [Linux Development Environment User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Linux_Development_Environment_User_Guide/build/LinuxDevelopmentEnvironmentUserGuide_zh.pdf)

## 7.3 U-Boot Porting Development Guide

The SG200x series of SoCs uses U-Boot 2021.10. If your hardware configuration comes with peripherals that deviates from reference designs, you would need to make changes to the U-Boot sources. This includes registers, system configurations, and drivers.

Please refer to the [U-Boot Porting Development Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/U-boot_Porting_Development_Guide/build/U-bootPortingDevelopmentGuide_zh.pdf) for more details.

## 7.4 IVE API References

IVE (Intelligent Video Engine) is a hardware-accelerated computer vision implementation. Its intelligent analyzing solution to lower the burden on RISC-V processors. The operators currently available to IVE can sufficiently support development of image- or video-based intelligent analysis.

Please refer to the [IVE API References](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/IVEAPI_Reference/build/IVEAPIReference_zh.pdf) for more details.

## 7.5 LDC Debugging Guide

LDC (Lens Distortion Correction) provides correction and broadening for Barrel Distortion and Pincushion Distortion for single frames of images.

Please refer to the [LDC Debugging Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/LDC_Debugging_Guide/build/LDCDebuggingGuide_zh.pdf) for detailed debugging paramters for specific applications.

## 7.6 MIPI User Guide

MIPI Rx can receive data from differential signals and the DC(TTL) port, converting received data into pixel data and passing them onto next level(s) of ISP module(s). The differential signal supports inputs ranging from  SubLVDS (Sub Low-Voltage Differential Signal), MIPI-CSI, and HiSPi (High-Speed Serial Pixel Interface). The DC signal supports Sensor RAW12, BT1120, BT656, and BT601.

Please refer to the [MIPI User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/MIPI_User_Guide/build/MIPIUserGuide_zh.pdf) for feature descriptions and user instructions.

## 7.7 AliOS Sensor Debugging Guide

This documentation describes the sensor driver, processor specifications, and image output debugging.

- [AliOS Sensor Debugging Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Sensor_Debugging_Guide/build/AliOS_Sensor_Debugging_Guide_zh.pdf)

## 7.8 Startup Screen User Guide

This documentation describes how to display a startup screen under U-Boot and AliOS.

- [Startup Screen User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Startup_Screen_User_Guide/build/StartupScreenUserGuide_zh.pdf)

## 7.9 MMF Media Procssing Software Development Reference

MMF is an acronym for Multimedia Framework, a set of software components to ease development of application development. The MMF includes the following features:

- ISP image pre-processing (HDR, noise reduction, sharpening, etc.).
- Video input snapshots and output.
- Image geometry correction.
- H.265/H.264/JPEG codecs.
- Audio extraction and output.
- Audio codecs.
- ...

Please refer to the [Media Processing Software Development Reference](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Media_Processing_Software_Development_Reference/build/MediaProcessingSoftwareDevelopmentReference_zh.pdf) for details on available features and usage.

## 7.10 Screen Docking Guide

This documentation outlines in detail configuration of MIPI DSI and LVDS screens on SG200x development boards.

- [Scren Docking Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Screen_Docking_Guide/build/ScreenDockingGuide_zh.pdf)。

## 7.11 Bit Rate Control Application Notes

This documentation introduces bit rate control parameters, GOP structure parameters and usage, and topics on bit rate control.

- [Bit Rate Control Application Notes](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Bit_Rate_Control_Application_Notes/build/BitRateControlApplicationNotes_zh.pdf)

## 7.12 Smart Coding User Guide

This documentation outlines GOP structure and applications, encoding input/output, etc.

- [Smart Coding User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Smart_Coding_User_Guide/build/SmartCodingUserGuide_zh.pdf)

## 7.13 Audio Quality Tuning Guide

This documentation describes in detail the algorithms and features in the VQE (Voice Quality Enhancement) module, with particular emphasis on outlining the debugging procedures for AEC (Acoustic Echo Cancellation).

- [Audio Quality Tuning Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Audio_Quality_Tuning_Guide/build/AudioQualityTuningGuide_zh.pdf)

## 7.14 eFuse User Guide

The processor comes internally with an eFuse partition to provide secure boot and 448 bits of custom sector. This documentation describes in detail the eFuse partition, secure boot, eFuse configuration procedures, etc.

- [eFuse User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/eFuse_User_Guide/build/eFuseUserGuide_zh.pdf)

## 7.15 Flash Partition Tool User Guide

This documentation outlines partition procedures and suggestions for various SDK versions (SPINOR/SPINAND/EMMC).

- [Flash Partition Tool User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Cvitek_Flash_Partition_Tool_User_Guide/build/CvitekFlashPartitionToolUserGuide_zh.pdf)

## 7.16 SPI NAND Programmer Burn-in User Guide

This documentation outlines procedures for SPI NAND file burning.

- [SPI NAND Programmer Burn-in User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/SPI_NAND_Programmer_Burn-in_User_Guide/build/SPINANDProgrammerBurn-inUserGuide_zh.pdf)

## 7.17 Wi-Fi User Guide

On Linux, different Wi-Fi chips may share drivers and configuration. This documetation outlines procedures on how to configure, port, and debug Realtek Wi-Fi solutions on different interfaces (USB and SDIO, for instance).

- [Wi-Fi User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Wi-Fi_User_Guide/build/Wi-FiUserGuide_zh.pdf)

## 7.18 Secure Boot User Guide

This documentation outlines procedures on how to generate secure images and make use of the secure boot processor.

- [Secure Boot User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Secure_Boot_User_Guide/build/SecureBootUserGuide_zh.pdf)

## 7.19 Peripheral Drivers User Guide

This documentation outlines usage for peripheral devices, such as Ethernet, USB, SD/MMC cards, GPIO, UART, Watchdog, PWM, ADC, etc.

- [Peripheral Drivers User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Peripheral_Driver/build/PeripheralDriver_zh.pdf)

## 7.20 RTC Application Guide

RTC (Real-Time Clock) is the hardware clock to keep and provide timing data for operating systems. The Linux Kernel uses the RTC time to initialize and synchronize the system clock.

- [RTC Application Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/RTC_Application_Guide/build/RTCApplicationGuide_zh.pdf)

## 7.21 ISP Development Reference

This documentation outlines the ISP user interface from aspects of the system control, 3A, and ISP modules.

- [ISP Development Reference](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/ISP/ISP_Development_Reference/build/ISPDevelopmentReference_zh.pdf)

## 7.22 ISP Tuning Guide

This documentation guides users to perform image signal processing (ISP) tuning, including descriptions on basic concepts and procedures. It is recommended to read this guide in conjunction with the "CviPQ Tools User Guide" below.

- [ISP Tuning Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/ISP/ISP_Tuning_Guide/build/ISPTuningGuide_zh.pdf)

## 7.23 CviPQ Tools User Guide

The CviPQ Tool is a professional-grade image quality debugging suite. It provides real-time debugging for each ISP modules with visualization; it also provides ISP calibration functionalities, generating calibration data and tunables for users to tune for optimal image quality. This documentation provides detailed usage instructions for CviPQ Tools.

- [CviPQ Tools User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/ISP/PQ_Tools_User_Guide/build/PQToolsUserGuide_zh.pdf)

## 7.24 Production Burn-In User Guide

This documentation outlines procedures to burn-in single board computer systems using cviDownloadTool. This solution uses USB to communicate with the target production board, which guarantees quick burning speeds and low costs.

- [Production Burn-In User Guide](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Production_Burning_User_Guide/build/ProductionBurningUserGuide_zh.pdf)

# 8. Appendix: Download Links for Extra Tools

## 8.1 Clock Timing Calculator for MIPI Panels

[Download Clock Timing Calculator for MIPI Panels](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Clock_Timing_Calculator_for_MIPI_Panels/build/MIPI_Time_Calculator.csv)

## 8.2 CviPQ Tool

[Download CviPQ Tool](https://github.com/jzlynn/sg-accessories/blob/master/CAM-GC2083/Software/CviPQtool_20230306.zip)

## 8.3 CviDownload Tool

[Download CviDownload Tool](https://github.com/jzlynn/sg-accessories/blob/master/CAM-GC2083/Software/cviDownloadTool.zip)
