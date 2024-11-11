=====================================================
A Simple Method to Install Ubuntu Image on SG2044 EVB
=====================================================
                                                     
                                                     
1. Prerequisites                                     
================                                     
- Computer with Linux OS                             
- SG2044 EVB                                         
- microSD Card (16GB or above), microSD Card Reader  
- NVMe SSD                                           
- Serial Cable (Type-C USB - Type-A USB)                     
                                                     
2. Get an Ubuntu Image                               
======================                               

Option 1: Directly dowload Ubuntu image template from `Releases <https://github.com/sophgo/bootloader-riscv/releases/tag/sg2044-v0.1>`_ 
---------------------------------------------------------------------------------------------------------------------------------------

Option 2: Compile image step by step
--------------------------------------

Refer to `How to Build SG2044 BSP.rst <https://github.com/sophgo/sophgo-doc/blob/main/SG2044/HowTo/How%20to%20Build%20SG2044%20BSP.rst>`_,
get ``ubuntu-sophgo.img`` exiting in the ``install/soc_sg2044/single_chip`` directory.

3. Create a Bootable microSD Card
=================================

Option 1: Use balenaEtcher
--------------------------
a. Download and install the `balenaEtcher <https://www.balena.io/etcher>`_.

b. Click on the **Flash from file** button and choose the ``ubuntu-sophgo.img``
   you want to use.

c. Click the **Select target** button and choose the microSD Card
   to write the ``ubuntu-sophgo.img`` to.

d. Click the **Flash!** button to begin the process.

Option 2: Use ``dd`` command directly
-------------------------------------
-   Use ``dd`` command to write ``ubuntu-sophgo.img`` to microSD Card.

.. highlights::

    .. code:: sh

        # To find the block device name of your microSD Card.
        # For example, the microSD Card drive is /dev/sdc. Checking the name of your device is a key step,
        # as writing to the wrong device might corrupt or destroy your data.

        $ sudo dd if=ubuntu-sophgo.img of=/dev/sdc bs=1024M status=progress

        10240+0 records in
        10240+0 records out
        10737418240 bytes (11 GB, 10 GiB) copied, 1211.08 s, 8.9 MB/s


-  If you want to expand the size of the last partition, resize root partition of microSD Card (**Optional**).

.. highlights::

    .. code:: sh


        # Change partition table of your microSD Card.
        $ sudo fdisk /dev/sdc

        Welcome to fdisk (util-linux 2.37.2).
        Changes will remain in memory only, until you decide to write them.
        Be careful before using the write command.


        Command (m for help): p
        Disk /dev/sdc: 29.72 GiB, 31914983424 bytes, 62333952 sectors
        Disk model: MassStorageClass
        Units: sectors of 1 * 512 = 512 bytes
        Sector size (logical/physical): 512 bytes / 512 bytes
        I/O size (minimum/optimal): 512 bytes / 512 bytes
        Disklabel type: dos
        Disk identifier: 0x5c9f9baa

        Device     Boot  Start      End Sectors  Size Id Type
        /dev/sdc1         2048   524287  522240  255M ef EFI(FAT-12/16/32)
        /dev/sdc2       524288 10485759 9961472  4.8G 83 Linux

        Command (m for help): d
        Partition number (1-2, default 2): 2 

        Partition 2 has been deleted.

        Command (m for help): n
        Partition type
        p   primary (1 primary, 0 extended, 3 free)
        e   extended (container for logical partitions)
        Select (default p): p
        Partition number (2,4, default 2):
        First sector (524288-62333951, default 524288):
        Last sector, +/-sectors or +/-size{K,M,G,T,P} (524288-62333951, default 62333951):

        Created a new partition 2 of type 'Linux' and of size 29.5 GiB.
        Partition #2 contains a ext4 signature.

        Do you want to remove the signature? [Y]es/[N]o: N

        Command (m for help): w

        The partition table has been altered.
        Calling ioctl() to re-read partition table.
        Syncing disks.

.. highlights::

    .. code:: sh

        # Check partitions of your microSD Card.
        $ sudo fdisk -l /dev/sdc

        Disk /dev/sdc: 29.72 GiB, 31914983424 bytes, 62333952 sectors
        Disk model: MassStorageClass
        Units: sectors of 1 * 512 = 512 bytes
        Sector size (logical/physical): 512 bytes / 512 bytes
        I/O size (minimum/optimal): 512 bytes / 512 bytes
        Disklabel type: dos
        Disk identifier: 0x5c9f9baa

        Device     Boot  Start      End  Sectors  Size Id Type
        /dev/sdc1         2048   524287   522240  255M ef EFI (FAT-12/16/32)
        /dev/sdc2       524288 62333951 61809664 29.5G 83 Linux


.. highlights::

    .. code:: sh

        # Force checking your file system.
        $ sudo e2fsck -f /dev/sdc2

        e2fsck 1.46.5 (30-Dec-2021)
        Pass 1: Checking inodes, blocks, and sizes
        Pass 2: Checking directory structure
        Pass 3: Checking directory connectivity
        Pass 4: Checking reference counts
        Pass 5: Checking group summary information
        cloudimg-rootfs: 79598/575424 files (0.0% non-contiguous), 1022378/1150203 blocks
        xingxg@vmware:~$ sudo resize2fs /dev/sdc2
        resize2fs 1.46.5 (30-Dec-2021)
        Resizing the filesystem on /dev/sdc2 to 7726208 (4k) blocks.
        The filesystem on /dev/sdc2 is now 7726208 (4k) blocks long.

4. Add BSP in image template
============================
    
This step is needed only if you download the image template from the given website. If you build ``ubuntu-sophgo.img`` by yourself, jump to step 5.

There is something missing in the image template. To deal with it, you need to build SG2044 BSP, see `How to Build SG2044 BSP.rst <https://github.com/sophgo/sophgo-doc/blob/main/SG2044/HowTo/How%20to%20Build%20SG2044%20BSP.rst>`_ . There is no need to build deb package or the whole image. Just make sure you have cloned these repositories, switched to the correct branch, and synced to the latest commit. After that, run the following instructions.
                                                                                                                                         
    .. code:: sh                                                                                                                         
                                                                                                                                         
        CHIP=sg2044                                                                                                                      
        source bootloader-riscv/scripts/envsetup.sh                                                                                      
        build_rv_zsbl                                                                                                                    
        build_rv_sbi                                                                                                                     
        build_rv_edk2                                                                                                                    
        build_rv_kernel                                                                                                                  
                                                                                                                                         
        sudo mount /dev/sdc1 /mnt/EFI                                                                                                    
        # create the riscv64 dir in EFI partition                                                                                        
        sudo mkdir /mnt/EFI/riscv64                                                                                                      
        # copy the output files into this dir                                                                                            
        sudo cp install/soc_sg2044/single_chip/firmware/* /mnt/EFI/riscv64/                                                              
        sudo sync                                                                                                                        

5. Boot from microSD Card
=========================

-   Plug the microSD Card into the SG2044 EVB,
    connect the serial cable to your computer,
    and power on the EVB.
-   Enter the username ``ubuntu`` and the password ``ubuntu``.
-   Any operation needs the ``sudo`` privilege.

6. Use NVMe SSD and microSD Card
================================
If you want to boot your system from a combination of
NVMe SSD and microSD Card,
the following steps also need to be done.

a. Use the ``dd`` command to copy the ``ubuntu-sophgo.img`` to the NVMe disk.

b. If you want, resize the root partition of the NVMe disk.

c. Use the ``fdisk`` command to delete the root partition of the microSD Card.

    .. note:: This step is critical because the root partition of the microSD Card and the NVMe disk has the same label!

d. Reboot, and access Ubuntu using the NVMe disk.
