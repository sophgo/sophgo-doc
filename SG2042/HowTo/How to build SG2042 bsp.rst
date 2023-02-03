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
-   Download source code and toolchain:

.. highlights::

   .. code::

      git clone https://github.com/sophgo/bootloader-riscv.git
      git clone https://github.com/sophgo/linux-sophgo.git

   riscv64 toolchain:
      http://disk-sophgo-vip.quickconnect.cn/sharing/ZZEgMnVBV
      http://disk-sophgo-vip.quickconnect.cn/sharing/12tHPScD1
      Create the directory gcc-riscv in the top-level directory of the code, and extract the above two files to this directory

      Put them on the same level of bootloader-riscv、linux-sophgo and gcc-riscv, now you get the following folders:
      .
      ├── bootloader-riscv
      ├── linux-sophgo
      └── gcc-riscv
               ├── gcc-riscv64-unknown-elf
               └── gcc-riscv64-unknown-linux-gnu


-  Building

.. highlights::

   .. code::

      $ CHIP=mango
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_all

-   The output files are in directory install/soc_mango/riscv64

   .. code::

      .
      ├── bsp-debs
      │        ├── linux-headers-5.19.17+.deb
      │        ├── linux-image-5.19.17+-dbg.deb
      │        └── linux-image-5.19.17+.deb
      ├── fw_jump.bin
      ├── fw_jump.elf
      ├── initrd.img
      ├── initrd.tar
      ├── mango.dtb
      ├── mango_evb_v0.1.dtb
      ├── mango_multi_chips.dtb
      ├── mango_multi_chips_pld.dtb
      ├── mango_pld.dtb
      ├── riscv64_Image
      ├── uroot.cpio
      ├── vmlinux
      └── zsbl.bin
