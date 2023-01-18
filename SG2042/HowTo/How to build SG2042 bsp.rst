================
How to build bsp
================

1. Installing dependencies
--------------------------

.. highlights::

   .. code::

      $ sudo apt-get install autoconf automake autotools-dev curl python3 libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev libncurses-dev openssl libiberty-dev libssl-dev dkms libelf-dev libudev-dev libpci-dev golang-go qemu-user-binfmt qemu-system-misc  qemu-user-static

To build uroot, you need to install go 1.17, refer to https://tecadmin.net/how-to-install-go-on-ubuntu-20-04/

2. Build from source
--------------------------
-   Download source code and toolchain, put them on the same level of bootloader-riscv、linux-sophgo and gcc-riscv, now you get the following folders

.. highlights::

   .. code::

      .
      ├── bootloader-riscv
      ├── linux-sophgo
      └── gcc-riscv

-  Building

.. highlights::

   .. code::

      $ CHIP=mango
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_all

-   The output files are in directory:

   install/soc_mango/riscv64
