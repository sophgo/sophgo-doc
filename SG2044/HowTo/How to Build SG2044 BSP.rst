================
How to Build BSP
================

1. Install Dependencies
=======================

-   on Ubuntu

.. highlights::

   .. code:: sh

      $ sudo apt-get install autoconf automake autotools-dev curl python3 libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev libncurses-dev openssl libiberty-dev libssl-dev dkms libelf-dev libudev-dev libpci-dev golang-go qemu-user-static ninja-build uuid-dev gcc-riscv64-unknown-elf

2. Build all from Source
========================
- Download source code and switch branch

.. highlights::

   .. code:: sh

      $ git clone https://github.com/sophgo/bootloader-riscv.git
      $ git clone https://github.com/sophgo/zsbl.git
      $ git clone https://github.com/sophgo/opensbi.git
      $ git clone https://github.com/sophgo/linux-riscv.git
      $ git clone https://github.com/sophgo/sophgo-edk2.git

      # switch branch
      $ cd ../opensbi
      $ git checkout sg2044-dev
      $ cd ../sophgo-edk2
      $ git checkout devel-sg2044
      $ cd ../linux-riscv
      $ git checkout sg2044-dev-6.12

- Build cross-compilation toolchains

  Enter the bsp directory which is the same level as ``bootloader-riscv``,
  ``zsbl``, ``opensbi``, ``sophgo-edk2`` and ``linux-riscv``,
  and build cross-compilation toolchains by the following command.

.. highlights::

   .. code:: sh

      $ CHIP=sg2044
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_gcc

      # get the following folders:
      .
      ├── bootloader-riscv
      ├── zsbl
      ├── opensbi
      ├── linux-riscv
      ├── sophgo-edk2
      │      ├── edk2
      │      ├── edk2-platforms
      │      └── edk2-non-osi
      └── gcc-riscv
             ├── gcc-riscv64-unknown-elf
             └── gcc-riscv64-unknown-linux-gnu

-  Build

.. highlights::

   .. code:: sh

      $ CHIP=sg2044
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_zsbl
      $ build_rv_sbi
      $ build_rv_edk2

      # build Ubuntu
      $ build_rv_ubuntu_kernel
      $ build_rv_ubuntu_distro
      $ build_rv_ubuntu_image

      # build openEuler
      $ build_rv_euler_kernel
      $ build_rv_euler_distro
      $ build_rv_euler_image

- The output files will be located in the ``install/soc_sg2044/single_chip`` directory.

.. highlights::

   .. code:: sh

      .
      ├── bsp-debs
      │      ├── linux-headers-6.12.deb
      │      ├── linux-image-6.12.deb
      │      └── linux-libc-dev_6.12.deb
      ├── bsp-rpms
      │      ├── kernel-6.12.riscv64.rpm
      │      ├── kernel-devel-6.12.riscv64.rpm
      │      └── kernel-headers-6.12.riscv64.rpm
      ├── firmware
      │      ├── fsbl.bin
      │      ├── fw_dynamic.bin
      │      ├── fw_dynamic.elf
      │      ├── sg2044-evb.dtb
      │      ├── zsbl.bin
      │      └── SG2044.fd
      ├── openEuler-24.03-riscv64-sg2044.img
      └── ubuntu-24.04.1-riscv64-sg2044.img



3. Summary
==========

+----------------+----------------------------------------------+------------------+------------------------+----------------------------------+
| Repository     | Link                                         | Branch           | Build Command          | Binary                           |
+================+==============================================+==================+========================+==================================+
| zsbl           | https://github.com/sophgo/zsbl.git           | master           | build_rv_zsbl          | zsbl.bin                         |
+----------------+----------------------------------------------+------------------+------------------------+----------------------------------+
| opensbi        | https://github.com/sophgo/opensbi.git        | sg2044-dev       | build_rv_sbi           | fw_dynamic.bin                   |
+----------------+----------------------------------------------+------------------+------------------------+----------------------------------+
| sophgo-edk2    | https://github.com/sophgo/sophgo-edk2.git    | devel-sg2044     |                        |                                  |
+----------------+----------------------------------------------+------------------+                        +                                  +
| edk2           | https://github.com/sophgo/edk2.git           | devel-sg2044     |                        |                                  |
+----------------+----------------------------------------------+------------------+                        +                                  +
| edk2-platforms | https://github.com/sophgo/edk2-platforms.git | devel-sg2044     | build_rv_edk2          | SG2044.fd                        |
+----------------+----------------------------------------------+------------------+                        +                                  +
| edk2-non-osi   | https://github.com/sophgo/edk2-non-osi.git   | devel-sg2044     |                        |                                  |
+----------------+----------------------------------------------+------------------+------------------------+----------------------------------+
|                |                                              |                  |                        | linux-headers-6.12.deb           |
+                +                                              +                  +                        +                                  +
| linux-riscv    | https://github.com/sophgo/linux-riscv.git    | sg2044-dev-6.12  | build_rv_ubuntu_kernel | linux-image-6.12.deb             |
+                +                                              +                  +                        +                                  +
|                |                                              |                  |                        | linux-libc-dev_6.12.deb          |
+                +                                              +                  +                        +                                  +
|                |                                              |                  |                        | sg2044-evb.dtb                   |
+                +                                              +                  +------------------------+----------------------------------+
|                |                                              |                  | build_rv_euler_kernel  | kernel-6.12.riscv64.rpm          |
+                +                                              +                  +                        +                                  +
|                |                                              |                  |                        | kernel-devel-6.12.riscv64.rpm    |
+                +                                              +                  +                        +                                  +
|                |                                              |                  |                        | kernel-headers-6.12.riscv64.rpm  |
+                +                                              +                  +                        +                                  +
|                |                                              |                  |                        | sg2044-evb.dtb                   |
+----------------+----------------------------------------------+------------------+------------------------+----------------------------------+

