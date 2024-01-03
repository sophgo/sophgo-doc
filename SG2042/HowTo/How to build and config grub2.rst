=============================
How to build and config GRUB2
=============================

Build
=====

1. Install dependencies
------------------------

.. highlights::
    
    .. code:: sh

      sudo apt install bison autoconf libopts25-dev flex automake pkg-config gettext autopoint
      sudo apt install libdevmapper-dev

2. Download source code
------------------------

.. highlights::

    .. code:: sh

      git clone https://github.com/sophgo/grub.git

3. Compile
----------

Option 1. Move the ``grub`` at the same directory as the ``bootloader-riscv`` repository. Execute the following commands.

.. highlights::

    .. code:: sh

        CHIP=mango
        source bootloader-riscv/scripts/envsetup.sh
        build_rv_ubuntu_grub
        build_rv_fedora_grub

Option 2. If you have no ``bootloader-riscv`` repository, compile the GRUB2 with the following steps.


* *Setup environment.*

.. highlights:: 

    .. code:: sh

        export WORKSPACE=`pwd`

* *Create folder.*

  Create ``grubriscv64`` folder in the same directory with the ``grub``. And build the ``default.cfg`` file under the ``grubriscv64`` directory.

.. highlights:: 

    .. code:: sh

        mkdir grubriscv64

        cd $WORKSPACE/grubriscv64

        echo -e "search -f /grub.cfg -s root" >> default.cfg
        echo -e "set prefix=(\$root)" >> default.cfg

* *Download gnulib.*

.. highlights::

    .. code:: sh

        cd $WORKSPACE/grub

        ./bootstrap

* *Generate the config files automatically.*

.. highlights::

    .. code:: sh

        ./autogen.sh

* *Configure and generate Makefile automatically.*

  .. note::
    - Here set ``RISCV64_LINUX_CROSS_COMPILE`` is equal to ``./gcc-riscv/gcc-riscv64-unknown-linux-gnu/bin/riscv64-unknown-linux-gnu-``. The cross-compile toolchain depends on your own.
    - The ``--prefix`` expects an absolute directory name.

.. highlights::

    .. code:: sh

        export RISCV64_LINUX_CROSS_COMPILE=${WORKSPACE}/gcc-riscv/gcc-riscv64-unknown-linux-gnu/bin/riscv64-unknown-linux-gnu-
        export TARGET_CC="${RISCV64_LINUX_CROSS_COMPILE}gcc"
        export TARGET_OBJCOPY="${RISCV64_LINUX_CROSS_COMPILE}objcopy"
        export TARGET_STRIP="${RISCV64_LINUX_CROSS_COMPILE}strip"
        export TARGET_NM="${RISCV64_LINUX_CROSS_COMPILE}nm"
        export TARGET_RANLIB="${RISCV64_LINUX_CROSS_COMPILE}ranlib"
        export TARGET_CFLAGS="-O2 -march=rv64imafdc_zicsr_zifencei"

        ./configure --target=riscv64-unknown-linux-gnu --with-platform=efi --prefix=$WORKSPACE/grubriscv64/rootfs

* *Make and install.*

.. highlights::

    .. code:: sh

        make install -j$(nproc)


* *Make efi file.*

.. highlights::

    .. code:: sh

        cd $WORKSPACE/grubriscv64/rootfs

        export GRUB_BINARY_NAME_RISCV=grubriscv64.efi
        export GRUB_BINARY_FORMAT_RISCV=riscv64-efi
        export GRUB_PREFIX_DIR_RISCV=efi
        export GRUB_DEFAULT_CFG_RISCV=${WORKSPACE}/grubriscv64/default.cfg
        export GRUB_UEFI_IMAGE_MODULES_RISCV='acpi adler32 affs afs afsplitter all_video archelp bfs bitmap bitmap_scale blocklist boot bswap_test btrfs bufio cat cbfs chain cmdline_cat_test cmp cmp_test configfile cpio_be cpio crc64 cryptodisk crypto ctz_test datehook date datetime diskfilter disk div div_test dm_nv echo efifwsetup efi_gop efinet elf eval exfat exfctest ext2 extcmd f2fs fat fdt file font fshelp functional_test gcry_arcfour gcry_blowfish gcry_camellia gcry_cast5 gcry_crc gcry_des gcry_dsa gcry_idea gcry_md4 gcry_md5 gcry_rfc2268 gcry_rijndael gcry_rmd160 gcry_rsa gcry_seed gcry_serpent gcry_sha1 gcry_sha256 gcry_sha512 gcry_tiger gcry_twofish gcry_whirlpool geli gettext gfxmenu gfxterm_background gfxterm_menu gfxterm gptsync gzio halt hashsum hello help hexdump hfs hfspluscomp hfsplus http iso9660 jfs jpeg json keystatus ldm linux loadenv loopback lsacpi lsefimmap lsefi lsefisystab lsmmap ls lssal luks2 luks lvm lzopio macbless macho mdraid09_be mdraid09 mdraid1x memdisk memrw minicmd minix2_be minix2 minix3_be minix3 minix_be minix mmap mpi msdospart mul_test net newc nilfs2 normal ntfscomp ntfs odc offsetio part_acorn part_amiga part_apple part_bsd part_dfly part_dvh part_gpt part_msdos part_plan part_sun part_sunpc parttool password password_pbkdf2 pbkdf2 pbkdf2_test pgp png priority_queue probe procfs progress raid5rec raid6rec read reboot regexp reiserfs romfs scsi search_fs_file search_fs_uuid search_label search serial setjmp setjmp_test sfs shift_test signature_test sleep sleep_test smbios squash4 strtoull_test syslinuxcfg tar terminal terminfo test_blockarg testload test testspeed tftp tga time tpm trig tr true udf ufs1_be ufs1 ufs2 video_colors video_fb videoinfo video videotest_checksum videotest xfs xnu_uuid xnu_uuid_test xzio zfscrypt zfsinfo zfs zstd'

        ./bin/grub-mkimage -v                             \
                           -o ${GRUB_BINARY_NAME_RISCV}   \
                           -O ${GRUB_BINARY_FORMAT_RISCV} \
                           -p ${GRUB_PREFIX_DIR_RISCV}    \
                           -c ${GRUB_DEFAULT_CFG_RISCV} ${GRUB_UEFI_IMAGE_MODULES_RISCV}

* *Show Result.*

  Output binary file: ``$WORKSPACE/grubriscv64/rootfs/grubriscv64.efi``.

.. highlights::

    .. code:: sh

        .
        └── grub
        └── grubriscv64
            ├── default.cfg
            └── rootfs
                ├── bin
                ├── etc
                ├── grubriscv64.efi
                ├── lib
                ├── sbin
                └── share

Write ``grub.cfg``
==================

Example
-------

A sample configuration file for GRUB2 to boot an Ubuntu image using a Micro SD card.

.. highlights:: 

    .. code:: 

        set default=0
        set timeout_style=menu
        set timeout=10

        set debug="linux,loader,mm"
        set term="vt100"

        menuentry 'ubuntu vmlinuz-6.1.31' {
                root=hd0,msdos2
                linux /boot/vmlinuz-6.1.31 root=/dev/mmcblk1p2 console=ttyS0,115200 earlycon
                initrd /boot/initrd.img-6.1.31
                root=hd0,msdos1
                devicetree /riscv64/mango-sophgo-x8evb.dtb
        }

Notes
-----

* ``menuentry 'title'{  }``: **define** a grub menu item named title. When this menu item is selected at boot time, the list of commands in curly brackets is executed, and if all commands up to the last one are executed successfully and the corresponding kernel is successfully loaded, the boot command is executed. grub then hands over control to the operating system kernel.

* ``root = hard disk, partition``: **specify** the current working path for loading related files.

* ``linux``, ``initrd``, ``devicetree``: **load** the corresponding resource, pay attention to the path where the resource is located.

.. note:: For more on writing the ``grub.cfg`` configuration file, please refer to `the official GRUB documentation <https://www.gnu.org/software/grub/manual/html_node/Shell_002dlike-scripting.html#Shell_002dlike-scripting>`_ .
