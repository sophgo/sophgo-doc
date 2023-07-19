====================================
How to Adapt Anolis OS on SG2042 EVB
====================================


1. Prerequisites
================
- Computer with Linux OS
- SG2042 EVB
- microSD Card (32GB or above), microSD Card Reader
- Serial Cable (Micro USB - USB)

2. Install dependencies
=======================

.. highlights::

   .. code:: sh

      $ sudo dnf install autoconf automake curl python3 libmpc-devel mpfr-devel gmp-devel gawk bison flex texinfo gperf libtool patchutils bc openssl dkms libudev-devel golang-bin zlib-devel qemu-user-binfmt  qemu-user-static ncurses-devel expat-devel elfutils-libelf-devel pciutils-devel openssl-devel binutils-devel qemu-system-riscv-core
      $ sudo dnf groupinstall "Development Tools" "C Development Tools and Libraries"
      $ sudo apt-get install autoconf automake autotools-dev curl python3 libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev libncurses-dev openssl libiberty-dev libssl-dev dkms libelf-dev libudev-dev libpci-dev golang-go qemu-user-static

To build uroot, you need to install **go 1.17**, refer to https://tecadmin.net/how-to-install-go-on-ubuntu-20-04/. You can use the following reference to check the **go** version.

.. highlights::

   .. code:: sh

      $ go version

      go version go1.17 linux/amd64

3. Build Cross toolchain for bsp
================================

-   Download source code

.. highlights::

   .. code:: sh

      $ mkdir workspace && cd workspace
      $ git clone https://github.com/sophgo/bootloader-riscv.git
      $ git clone https://github.com/sophgo/zsbl.git
      $ git clone https://github.com/sophgo/opensbi.git
      $ git clone https://github.com/sophgo/linux-riscv.git

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
      └── gcc-riscv
            ├── gcc-riscv64-unknown-elf
            └── gcc-riscv64-unknown-linux-gnu

4. Get an Anolis RV-root.ext4 file
==================================

-   Dowload the from http://219.142.246.77:65000/sharing/vXXN0Yvzt directly.
-   remember the path_to_rv-rootfs.ext4

5. Build the compilation script
===============================

Step 1: Creat a new script in the ${path_to_workspace}/bootloader-riscv/scripts/
--------------------------------------------------------------------------------

.. highlights::

   .. code:: sh

      $ cd ${path_to_workspace}/bootloader-riscv/scripts
      $ vim anolis_envsetup.sh

-   Copy following to anolis_envsetup.sh.

.. code-block:: bash

    #!/bin/sh
    #================================================
    #FileName : anolis_envsetup.sh
    #Description: build image for Anolis OS
    #================================================

    source bootloader-riscv/scripts/envsetup.sh

    function build_rv_anolis_image()
    {
        echo build_rv_anolis_image
        echo create an image file...
        rm -f $RV_OUTPUT_DIR/$RV_ANOLIS_SOPHGO_IMAGE
        dd if=/dev/zero of=$RV_OUTPUT_DIR/$RV_ANOLIS_SOPHGO_IMAGE bs=1GiB count=15

        echo create partitions...
        sudo parted $RV_OUTPUT_DIR/$RV_ANOLIS_SOPHGO_IMAGE mktable msdos 
        sudo parted $RV_OUTPUT_DIR/$RV_ANOLIS_SOPHGO_IMAGE mkpart p fat32 0% 256MiB
        sudo parted $RV_OUTPUT_DIR/$RV_ANOLIS_SOPHGO_IMAGE mkpart p ext4 256MiB 1280MiB
        sudo parted $RV_OUTPUT_DIR/$RV_ANOLIS_SOPHGO_IMAGE mkpart p ext4 1280MiB 100%

        loops=$(sudo kpartx -av $RV_OUTPUT_DIR/$RV_ANOLIS_SOPHGO_IMAGE | cut -d ' ' -f 3)
        efi_part=$(echo $loops | cut -d ' ' -f 1)
        boot_part=$(echo $loops | cut -d ' ' -f 2)
        root_part=$(echo $loops | cut -d ' ' -f 3)

        sleep 3
        sudo mkfs.vfat /dev/mapper/$efi_part -n EFI
        sudo mkfs.ext4 /dev/mapper/$boot_part
        sudo mkfs.ext4 /dev/mapper/$root_part

        echo copy bootloader...
        mkdir $RV_OUTPUT_DIR/efi
        sudo mount /dev/mapper/$efi_part $RV_OUTPUT_DIR/efi
        sudo mkdir -p $RV_OUTPUT_DIR/efi/riscv64
        sudo cp $RV_FIRMWARE/fip.bin $RV_OUTPUT_DIR/efi
        sudo cp $RV_OUTPUT_DIR/zsbl.bin $RV_OUTPUT_DIR/efi
        sudo cp $RV_OUTPUT_DIR/fw_jump.bin $RV_OUTPUT_DIR/efi/riscv64
        sudo cp $RV_OUTPUT_DIR/riscv64_Image $RV_OUTPUT_DIR/efi/riscv64
        sudo cp $RV_OUTPUT_DIR/*.dtb $RV_OUTPUT_DIR/efi/riscv64
        sudo cp $RV_OUTPUT_DIR/initrd.img $RV_OUTPUT_DIR/efi/riscv64

        sudo e2fsck -f -y /dev/mapper/$boot_part
        sudo resize2fs /dev/mapper/$boot_part
        sudo e2label /dev/mapper/$boot_part BOOT
        sudo dd if=$RV_ROOTFS_PATH/rv-rootfs.ext4 of=/dev/mapper/$root_part bs=256M
        echo $RV_ROOTFS_PATH
        sudo e2fsck -f -y /dev/mapper/$root_part
        sudo resize2fs /dev/mapper/$root_part
        sudo e2label /dev/mapper/$root_part ROOT

        mkdir -p $RV_OUTPUT_DIR/root
        sudo mount /dev/mapper/$root_part $RV_OUTPUT_DIR/root

        sudo mount --bind /proc $RV_OUTPUT_DIR/root/proc
        sudo mount --bind /sys $RV_OUTPUT_DIR/root/sys
        sudo mount --bind /dev $RV_OUTPUT_DIR/root/dev
        sudo mount --bind /dev/pts $RV_OUTPUT_DIR/root/dev/pts

        echo add user anolis:anolis
    # following lines must not be started with space or tab.
    sudo chroot $RV_OUTPUT_DIR/root /bin/bash << "EOT"
    useradd -m -s /bin/bash anolis
    echo "anolis:anolis" | chpasswd
    sed -i -e '/NOPASSWD/a\%anolis   ALL=(ALL) NOPASSWD: ALL' /etc/sudoers

    exit
    EOT

        echo copy bsp package...
        sudo cp -r $RV_RPM_INSTALL_DIR $RV_OUTPUT_DIR/root/home/anolis/

        echo install linux image...
    # following lines must not be started with space or tab.
    sudo chroot $RV_OUTPUT_DIR/root /bin/env BOOT_PART="$boot_part" /bin/bash << "EOT"
    mount /dev/mapper/$BOOT_PART /boot
    rpm -ivh --force /home/anolis/bsp-rpms/kernel-[0-9]*.riscv64.rpm

    # The following command is to solve the problem of not updating the extlinux.conf file when installing kernel RPM package.

    kernel_version=`ls /home/anolis/bsp-rpms/kernel-[0-9]*.riscv64.rpm | cut -d '-' -f 3 | cut -d '.' -f 1-3`
    # mv /boot/extlinux/extlinux.conf /boot/extlinux/extlinux.conf_bak

    mkdir -p /boot/extlinux

    cat > /boot/extlinux/extlinux.conf << EOF

    ## /boot/extlinux/extlinux.conf

    default anolis_sophgo
    menu title linuxboot menu
    prompt 0
    timeout 50

    label anolis_sophgo
        menu label anolis Sophgo in SD
        linux /vmlinuz-$kernel_version
        initrd /initramfs-$kernel_version.img 
        append  console=ttyS0,115200 root=LABEL=ROOT rootfstype=ext4 rootwait rw earlycon selinux=0 LANG=en_US.UTF-8 nvme.use_threaded_interrupts=1 nvme_core.io_timeout=3000
    EOF

    umount /boot

    # replace UUID to LABEL
    mv /etc/fstab /etc/fstab_bak
    cat > /etc/fstab << EOF
    LABEL=ROOT	/		ext4	defaults,noatime,x-systemd.device-timeout=300s,x-systemd.mount-timeout=300s 0 0
    LABEL=BOOT	/boot		ext4	defaults,noatime,x-systemd.device-timeout=300s,x-systemd.mount-timeout=300s 0 0
    EOF

    exit
    EOT

        echo cleanup...
        sync
        sudo umount $RV_OUTPUT_DIR/root/proc
        sudo umount $RV_OUTPUT_DIR/root/sys
        sudo umount $RV_OUTPUT_DIR/root/dev/pts
        sudo umount $RV_OUTPUT_DIR/root/dev
        sudo umount /dev/mapper/$efi_part
        sudo umount /dev/mapper/$root_part
        sudo kpartx -d $RV_OUTPUT_DIR/$RV_ANOLIS_SOPHGO_IMAGE
        rm -r $RV_OUTPUT_DIR/efi
        rm -r $RV_OUTPUT_DIR/root

        echo "build anolis image successfully!"
    }



Step 2: Execute the build command as follows in your workspace directory
------------------------------------------------------------------------

.. highlights::

    .. code:: sh

        $ CHIP=mango
        $ source bootloader-riscv/scripts/anolis_envsetup.sh
        $ export RV_ROOTFS_PATH=${path_to_rv-rootfs.ext4}
        $ build_rv_firmware
        $ build_rv_fedora_kernel
        $ build_rv_anolis_image

-   You can get ``anolis-sophgo.img`` in ${path_to_workspace}/install/soc_mango/riscv64/
-   Use the ``dd`` command to copy the ``anolis-sophgo.img`` to the microSD Card
