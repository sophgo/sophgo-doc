==========================================================
   A simple method to install ubuntu on SG2042 EVB borad
==========================================================


1. Prerequisites
------------------------
- Linux host machine
- SG2042 EVB borad
- TF card(16GB or above), TF card reader
- NVMe SSD, 
- Serial(usb)
	  

2. Steps
------------------------

-   Dowload image 

    http://219.142.246.77:65000/sharing/dKlPHukbe
    
    The image is created based on ubuntu offical preinstall server image.

    The following uses sd.img to refer to the image.

-   dd command writes image to TF card

.. highlights:: 

    .. code::

        $ sudo dd if=sd.img of=/dev/sdc bs=32M
        160+0 records in
        160+0 records out
        5368709120 bytes (5.4 GB, 5.0 GiB) copied, 108.587 s, 49.4 MB/s


-   Resize root partition of TF card 

.. highlights:: 

    .. code::    

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
        /dev/sdc1         2048   262143  260096  127M  c W95 FAT32 (LBA)
        /dev/sdc2       262144   524287  262144  128M  c W95 FAT32 (LBA)
        /dev/sdc3       524288 10485759 9961472  4.8G 83 Linux

        Command (m for help): d
        Partition number (1-3, default 3): 3

        Partition 3 has been deleted.

        Command (m for help): n
        Partition type
        p   primary (2 primary, 0 extended, 2 free)
        e   extended (container for logical partitions)
        Select (default p): p
        Partition number (3,4, default 3): 
        First sector (524288-62333951, default 524288): 
        Last sector, +/-sectors or +/-size{K,M,G,T,P} (524288-62333951, default 62333951): 

        Created a new partition 3 of type 'Linux' and of size 29.5 GiB.
        Partition #3 contains a ext4 signature.

        Do you want to remove the signature? [Y]es/[N]o: N

        Command (m for help): w

        The partition table has been altered.
        Calling ioctl() to re-read partition table.
        Syncing disks.

        $ sudo fdisk -l /dev/sdc
        Disk /dev/sdc: 29.72 GiB, 31914983424 bytes, 62333952 sectors
        Disk model: MassStorageClass
        Units: sectors of 1 * 512 = 512 bytes
        Sector size (logical/physical): 512 bytes / 512 bytes
        I/O size (minimum/optimal): 512 bytes / 512 bytes
        Disklabel type: dos
        Disk identifier: 0x5c9f9baa

        Device     Boot  Start      End  Sectors  Size Id Type
        /dev/sdc1         2048   262143   260096  127M  c W95 FAT32 (LBA)
        /dev/sdc2       262144   524287   262144  128M  c W95 FAT32 (LBA)
        /dev/sdc3       524288 62333951 61809664 29.5G 83 Linux


.. highlights:: 

    .. code:: 

        $ sudo e2fsck -f /dev/sdc3
        e2fsck 1.46.5 (30-Dec-2021)
        Pass 1: Checking inodes, blocks, and sizes
        Pass 2: Checking directory structure
        Pass 3: Checking directory connectivity
        Pass 4: Checking reference counts
        Pass 5: Checking group summary information
        cloudimg-rootfs: 79598/575424 files (0.0% non-contiguous), 1022378/1150203 blocks
        xingxg@vmware:~/sophgo/install/soc_mango/riscv64$ sudo resize2fs /dev/sdc3
        resize2fs 1.46.5 (30-Dec-2021)
        Resizing the filesystem on /dev/sdc3 to 7726208 (4k) blocks.
        The filesystem on /dev/sdc3 is now 7726208 (4k) blocks long.


-   Copy image to /home/ubuntu on root partition of TF card 

.. highlights:: 

    .. code:: 

        $ cp sd.img /mnt/home/ubuntu


-   Insert the TF card into the SG2042 EVB borad, connect serial to host machine, and power on the EVB


-   Login ubuntu on TF card, using ubuntu:ubuntu which has sudo permission


-   dd command write the image to NVMe disk


-   Resize root partition of NVMe disk


-   fdisk command deletes root partition of TF card

    notes: very important because root partition of both TF card and NVMe disk have the same label
    

-   Restart system to access ubuntu on NVMe disk
