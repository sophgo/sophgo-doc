================
How to build bsp
================

1. Install dependencies
=======================

-   on Fedora

.. highlights::

   .. code:: sh

      $ sudo dnf install autoconf automake curl python3 libmpc-devel mpfr-devel gmp-devel gawk bison flex texinfo gperf libtool patchutils bc openssl dkms libudev-devel golang-bin zlib-devel qemu-user-binfmt  qemu-user-static ncurses-devel expat-devel elfutils-libelf-devel pciutils-devel openssl-devel binutils-devel qemu-system-riscv-core
      $ sudo dnf groupinstall "Development Tools" "C Development Tools and Libraries"

-   on Ubuntu

.. highlights::

   .. code:: sh

      $ sudo apt-get install autoconf automake autotools-dev curl python3 libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev libncurses-dev openssl libiberty-dev libssl-dev dkms libelf-dev libudev-dev libpci-dev golang-go qemu-user-static

To build uroot, you need to install **go 1.17**, refer to https://tecadmin.net/how-to-install-go-on-ubuntu-20-04/. You can use the following reference to check the **go** version.


.. highlights::

   .. code:: sh

      $ go version

      go version go1.17 linux/amd64

2. Build all from source
========================
-   Download source code

.. highlights::

   .. code:: sh

      $ git clone https://github.com/sophgo/bootloader-riscv.git
      $ git clone https://github.com/sophgo/zsbl.git
      $ git clone https://github.com/sophgo/opensbi.git
      $ git clone https://github.com/sophgo/linux-riscv.git
      $ git clone https://github.com/sophgo/sophgo-edk2.git
      $ git clone https://github.com/sophgo/grub.git
      $ git clone https://github.com/sophgo/u-boot.git



- Build Cross toolchain for bsp

  Enter the bsp directory which is the same level as ``bootloader-riscv``,
  ``zsbl``, ``opensbi``, ``u-boot``, ``EDKII``, ``grub2`` and ``linux-riscv``,
  and build Cross toolchain by the following command:

.. highlights::

   .. code:: sh

      $ CHIP=mango
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_gcc

      # get the following folders:
      .
      ├── bootloader-riscv
      ├── zsbl
      ├── opensbi
      ├── linux-riscv
      ├── u-boot
      ├── sophgo-edk2
      ├── grub
      └── gcc-riscv
            ├── gcc-riscv64-unknown-elf
            └── gcc-riscv64-unknown-linux-gnu

-  Build all

.. highlights::

   .. code:: sh

      # build single chip:
      $ CHIP=mango
      $ CHIP_NUM=single
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_all

      # build multi chips:
      $ CHIP=mango
      $ CHIP_NUM=multi
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_all

- If you have chosen a single chip, the output files will be located in the install/soc_mango/single_chip directory.
- If you have chosen multiple chips, the output files will be located in the install/soc_mango/multi_chip directory.



.. highlights::

   .. code:: sh

      .
      ├── bsp-debs
      │      ├── linux-headers-6.1.31.deb
      │      ├── linux-image-6.1.31.deb
      │      └── linux-libc-dev_6.1.31.deb
      ├── firmware
      │      ├── fip.bin
      │      ├── firmware.bin
      │      ├── fw_jump.bin
      │      ├── fw_jump.elf
      │      ├── initrd.img
      │      ├── mango-milkv-pioneer.dtb
      │      ├── mango-sophgo-pisces.dtb
      │      ├── mango-sophgo-x4evb.dtb
      │      ├── mango-sophgo-x8evb.dtb
      │      ├── riscv64_Image
      │      ├── zsbl.bin
      │      ├── u-boot.bin
      │      ├── grubriscv64
      │      ├── SG2042.fd
      ├── tools
      │      └── perf
      │            ├── build-perf.sh
      │            ├── perf-6.1.31
      │            └── perf-6.1.31.tar
      └── ubuntu-sophgo.img

.. note:: If you need to compile a file separately,
   type the ``show_rv_functions`` command to
   get the relevant instructions.

3. Build perf tool on Ubuntu
============================
- Use the following commands to extract the perf source
  package from ``linux-riscv`` and get the build script.

.. highlights::

   .. code:: sh

      $ CHIP=mango
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_ubuntu_perf_tool

- Find the previously mentioned files in
  ``install/soc_mango/riscv64/tools/perf`` directory.

.. highlights::

   .. code:: sh

      .
      └── tools
             └── perf
                   ├── build-perf.sh
                   ├── perf-6.1.31
                   └── perf-6.1.31.tar

- Copy the ``tools`` directory to the SG2042 EVB, and
  execute the ``build-perf.sh`` to make and install perf tool.
  If you use the latest ``ubuntu-sophgo.img``,
  the ``tools`` exists in the ``/home/ubuntu`` directory.

.. highlights::

   .. code:: sh

      $ cd tools/perf/
      $ source build-scripts.sh

- Use the perf tool.

.. highlights::

   .. code:: sh

      $ perf list
      $ perf stat
      $ perf bench
