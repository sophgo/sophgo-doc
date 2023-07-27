====================================
How to Adapt Anolis OS on SG2042 EVB
====================================


1. Prerequisites
================
- Computer with Linux OS
- SG2042 EVB
- microSD Card (32GB or above), microSD Card Reader
- Serial Cable (Micro USB - USB)

2. Adjust SD partitions
=======================

-   Make three partitions on your SD card

.. highlights::

   .. code:: sh

      $ sudo fdisk /dev/sda

-   Format partitions into corresponding file systems

.. highlights::

   .. code:: sh

      $ sudo mkfs.vfat /dev/sda1 -n EFI
      $ sudo mkfs.ext4 /dev/sda2
      $ sudo mkfs.ext4 /dev/sda3

-   Expand the third partition

.. highlights::

   .. code:: sh

      $ sudo e2fsck -f /dev/sda3
      $ sudo resize2fs /dev/sda3

-   Label the partition with a name

.. highlights::

   .. code:: sh

      $ sudo e2label /dev/sda2 BOOT
      $ sudo e2label /dev/sda3 ROOT

3. Add content to the partitions
================================

Step 1: Copy firmware into EFI partition
----------------------------------------

-   You can get firmware form source code please refer to
    https://github.com/sophgo/sophgo-doc/blob/main/SG2042/HowTo/How%20to%20build%20SG2042%20bsp.rst

.. highlights::

   .. code:: sh

       # get the following folders:
      .
      ├── fip.bin
      ├── riscv64
      │   ├── fw_jump.bin
      │   ├── initrd.img
      │   ├── mango-milkv-pioneer.dtb
      │   ├── mango-sophgo-pisces.dtb
      │   ├── mango-sophgo-x4evb.dtb
      │   ├── mango-sophgo-x8evb.dtb
      │   └── riscv64_Image
      └── zsbl.bin

Step 2: Create ROOT partition content
-------------------------------------

-   If you have anolis os RV-root.ext4 file, use the ``dd`` command to 
    copy the ``RV-root.ext4`` to the ROOT partition

.. highlights::

   .. code:: sh

      $ sudo dd if=RV-root.ext4 of=/dev/sda3 bs=4M status=progress

-   Or if you have anolis os rootfs directory ,copy it into the ROOT partition

-   Copy kernel-6.5.31.riscv64.rpm into ROOT/home directory and 
    mount BOOT partition to the boot directory of ROOT partition  
-   Change ROOT partition to root directly and modify system 
    partition mounting information

.. highlights::

   .. code:: sh

      $ vim /etc/fstab

-   fstab contents as following:

.. highlights::

    .. code:: sh

       LABEL=ROOT	/		ext4	defaults,noatime,x-systemd.device-timeout=300s,x-systemd.mount-timeout=300s 0 0
       LABEL=BOOT	/boot		ext4	defaults,noatime,x-systemd.device-timeout=300s,x-systemd.mount-timeout=300s 0 0

-   Install the kernel

.. highlights::

   .. code:: sh

      $ rpm -ivh --force /home/kernel-6.5.31.riscv64.rpm

Step 3: Enter BOOT partition and add boot file
----------------------------------------------

.. highlights::

   .. code:: sh

      $ mkdir extlinux && cd extlinux
      $ vim exitlinux.conf

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

4. Boot from microSD Card
=========================
-   Plug the microSD Card into the SG2042 EVB,
    connect the serial cable to your computer,
    and power on the EVB.
-   Enter the username ``anuser`` and the password ``anolisos``.
-   Any operation needs the ``sudo`` privilege.