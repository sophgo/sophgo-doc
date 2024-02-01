======================================
How to adjust CPU operating frequency
======================================


1. Add the required macro
=========================

.. highlights::

   .. code:: sh

      $ cd drivers/clk/
      $ vim clk.c

-   add  #define CLOCK_ALLOW_WRITE_DEBUGFS in the drivers/clk/clk.c file.

2. Recompile the kernel
================================

- Download source code

.. highlights::

   .. code:: sh

    $ git clone https://github.com/sophgo/bootloader-riscv.git
    $ git clone https://github.com/sophgo/linux-riscv.git

- Build Cross toolchain for bsp

.. highlights::

   .. code:: sh

      $ CHIP=mango
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_gcc

Fedora
----------------------------------------

-  single:
  
.. highlights::

   .. code:: sh

      $ CHIP=mango
      $ CHIP_NUM=single
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_fedora_kernel

-   multi:

.. highlights::

   .. code:: sh

      $ CHIP=mango
      $ CHIP_NUM=multi
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_fedora_kernel

Ubuntu
----------------------------------------
  
-  single:
  
.. highlights::

   .. code:: sh

      $ CHIP=mango
      $ CHIP_NUM=single
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_ubuntu_kernel

-   multi:

.. highlights::

   .. code:: sh

      $ CHIP=mango
      $ CHIP_NUM=multi
      $ source bootloader-riscv/scripts/envsetup.sh
      $ build_rv_ubuntu_kernel

Upgrade the kernel
==================

Fedora
-------

.. highlights::

   .. code:: sh

      $ sudo -s
      $ rpm -qa kernel
      $ rpm -e "old kernel"
      $ rpm -ivh "new kernel"

Ubuntu
-------

.. highlights::

   .. code:: sh

      $ sudo -s
      $ dpkg --list | grep linux-image
      $ sudo apt remove linux-image-<old-kernel-version>
      $ sudo dpkg -i linux-image-<new-kernel-version>.deb

If the new kernel version is different from the old kernel, you need to modify exlinux.conf.

-   exitlinux.conf contents as following:

.. highlights::

    .. code:: sh

       default anolis_sophgo
       menu title linuxboot menu
       prompt 0
       timeout 50

       label anolis_sophgo
          menu label anolis Sophgo in SD
          linux /vmlinuz-$kernel_version
          initrd /initramfs-$kernel_version.img 
          append  console=ttyS0,115200 root=LABEL=ROOT rootfstype=ext4 rootwait rw earlycon selinux=0 LANG=en_US.UTF-8 nvme.use_threaded_interrupts=1 nvme_core.io_timeout=3000

To modify the $kernel_version to the actual version number

.. highlights::

   .. code:: sh

      $ cd /boot/exlinux
      $ sudo vi exlinux.conf
      $ sudo reboot

Change the CPU frequency
========================

.. highlights::

   .. code:: sh

      $ sudo echo 1000000000 > /sys/kernel/debug/clk/mpll_clock/clk_rate