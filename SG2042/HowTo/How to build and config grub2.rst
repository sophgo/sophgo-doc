=============================
How to build and config GRUB2
=============================

1. How to build grub2
=====================

1.1 Clone source
-----------------

.. highlights:: 

    .. code:: sh

      $ git clone git://git.savannah.gnu.org/grub.git
      $ pushd grub
      $ git remote add github.com_tekkamanninja https://github.com/tekkamanninja/grub.git
      $ git fetch github.com_tekkamanninja
      $ git checkout github.com_tekkamanninja/riscv_devel_Nikita_V3
      $ popd


1.2 Install related dependencies
--------------------------------

.. highlights:: 
    
    .. code:: sh

      $ sudo apt install bison autoconf libopts25-dev flex automake pkg-config gettext autopoint
      $ sudo apt install libdevmapper-dev

1.3 Create related file and folder
----------------------------------

.. highlights:: 

    .. code:: 

        $ mkdir grubriscv64
        $ cd grubriscv64
        $ touch default.cfg

+ Content of default.cfg

.. highlights:: 

    .. code::

        search -f /grub.cfg -s root
        set prefix=($root)

1.4 Write compilation script
----------------------------

+ building_grub2.sh 

.. highlights:: 

    .. code:: sh
        
        pushd $RV_GRUB_SRC_DIR

        #setup build env
        GRUB_INSTALL_DIR=${RV_GRUB_BUILD_DIR}/rootfs
    
        mkdir -p $GRUB_INSTALL_DIR
        GRUB_DEFAULT_CFG_RISCV=${RV_GRUB_BUILD_DIR}/default.cfg
        echo "search -f /grub.cfg -s root" > $GRUB_DEFAULT_CFG_RISCV
        # Use single quotes to prevent variables from being substituted
        echo 'set prefix=($root)' >> $GRUB_DEFAULT_CFG_RISCV
    
        GRUB_BINARY_NAME_RISCV=grubriscv64.efi
        GRUB_BINARY_FORMAT_RISCV=riscv64-efi
        GRUB_PREFIX_DIR_RISCV=efi
        GRUB_UEFI_IMAGE_MODULES_RISCV='acpi adler32 affs afs afsplitter all_video archelp bfs bitmap bitmap_scale blocklist boot bswap_test btrfs bufio cat cbfs chain cmdline_cat_test cmp cmp_test configfile cpio_be cpio crc64 cryptodisk crypto ctz_test datehook date datetime diskfilter disk div div_test dm_nv echo efifwsetup efi_gop efinet elf eval exfat exfctest ext2 extcmd f2fs fat fdt file font fshelp functional_test gcry_arcfour gcry_blowfish gcry_camellia gcry_cast5 gcry_crc gcry_des gcry_dsa gcry_idea gcry_md4 gcry_md5 gcry_rfc2268 gcry_rijndael gcry_rmd160 gcry_rsa gcry_seed gcry_serpent gcry_sha1 gcry_sha256 gcry_sha512 gcry_tiger gcry_twofish gcry_whirlpool geli gettext gfxmenu gfxterm_background gfxterm_menu gfxterm gptsync gzio halt hashsum hello help hexdump hfs hfspluscomp hfsplus http iso9660 jfs jpeg json keystatus ldm linux loadenv loopback lsacpi lsefimmap lsefi lsefisystab lsmmap ls lssal luks2 luks lvm lzopio macbless macho mdraid09_be mdraid09 mdraid1x memdisk memrw minicmd minix2_be minix2 minix3_be minix3 minix_be minix mmap mpi msdospart mul_test net newc nilfs2 normal ntfscomp ntfs odc offsetio part_acorn part_amiga part_apple part_bsd part_dfly part_dvh part_gpt part_msdos part_plan part_sun part_sunpc parttool password password_pbkdf2 pbkdf2 pbkdf2_test pgp png priority_queue probe procfs progress raid5rec raid6rec read reboot regexp reiserfs romfs scsi search_fs_file search_fs_uuid search_label search serial setjmp setjmp_test sfs shift_test signature_test sleep sleep_test smbios squash4 strtoull_test syslinuxcfg tar terminal terminfo test_blockarg testload test testspeed tftp tga time tpm trig tr true udf ufs1_be ufs1 ufs2 video_colors video_fb videoinfo video videotest_checksum videotest xfs xnu_uuid xnu_uuid_test xzio zfscrypt zfsinfo zfs zstd'
    
        #bootstrap, download gunlib...
        ./bootstrap
        #auto generate the config files
        ./autogen.sh
        #auto config and generate Makefile
        # e.g. $RISCV64_LINUX_CROSS_COMPILE=./gcc-riscv/gcc-riscv64-unknown-linux-gnu/bin/riscv64-unknown-linux-gnu-
        TARGET_CC="${RISCV64_LINUX_CROSS_COMPILE}gcc" \
        TARGET_OBJCOPY="${RISCV64_LINUX_CROSS_COMPILE}objcopy" \
        TARGET_STRIP="${RISCV64_LINUX_CROSS_COMPILE}strip" \
        TARGET_NM="${RISCV64_LINUX_CROSS_COMPILE}nm" \
        TARGET_RANLIB="${RISCV64_LINUX_CROSS_COMPILE}ranlib" \
        TARGET_CFLAGS='-Os -march=rv64imac_zicsr_zifencei' \
        ./configure --target=riscv64-unknown-linux-gnu --with-platform=efi --prefix=$GRUB_INSTALL_DIR
        #build and install to ${RISCV_ROOTFS}
        make install -j$(nproc)
    
        #make executable efi file
        pushd ${GRUB_INSTALL_DIR}
        ./bin/grub-mkimage -v \
                           -o ${GRUB_BINARY_NAME_RISCV} \
                           -O ${GRUB_BINARY_FORMAT_RISCV} \
                           -p ${GRUB_PREFIX_DIR_RISCV}  \
                           -c ${GRUB_DEFAULT_CFG_RISCV} ${GRUB_UEFI_IMAGE_MODULES_RISCV}
        popd
        popd

1.5 Run the script and show the results
------------------------------------------

+ run

.. highlights:: 

    .. code:: sh

        source building_grub2.sh


+ results

.. highlights::

    .. code:: 

        .
        └── grub
        └── building_grub2.sh
        └── grubriscv64
            ├── default.cfg
            └── rootfs
                ├── bin
                ├── etc
                ├── grubriscv64.efi
                ├── lib
                ├── sbin
                └── share

2 How to config grub.cfg
========================

+ source
  
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

.. note:: The above is a sample configuration file for grub2 to boot an ubuntu image using Micro SD card. 
    
+ introduction

    + menuentry 'title'{  }: **define** a grub menu item named title. When this menu item is selected at boot time, the list of commands in curly brackets is executed, and if all commands up to the last one are executed successfully and the corresponding kernel is successfully loaded, the boot command is executed. grub then hands over control to the operating system kernel.
    + root = hard disk, partition: **specify** the current working path for loading related files
    + linux、initrd、devicetree: **load** the corresponding resource, pay attention to the path where the resource is located

.. note:: The above three points are important for grub2 to boot load the kernel.  For more on writing the grub.cfg configuration file, please refer to `the official GRUB documentation <https://www.gnu.org/software/grub/manual/html_node/Shell_002dlike-scripting.html#Shell_002dlike-scripting>`_ .
    
