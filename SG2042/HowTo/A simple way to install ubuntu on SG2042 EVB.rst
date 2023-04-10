=====================================================
A Simple Method to Install Ubuntu Image on SG2042 EVB
=====================================================


1. Prerequisites
================
- Computer with Linux OS
- SG2042 EVB
- microSD Card (16GB or above), microSD Card Reader
- NVMe SSD
- Serial Cable (Micro USB - USB)

2. Get an Ubuntu Image
======================
-   Dowload the `Ubuntu image <http://219.142.246.77:65000/sharing/agK6z51jP>`_ directly.

    The image is created based on Ubuntu offical preinstall server image.

-   Or use your own compiled ``ubuntu-sophgo.img`` exiting in the
    ``install/soc_mango/riscv64`` directory.

The following uses ``ubuntu-sophgo.img`` to refer to the Ubuntu image.

1. Create a Bootable microSD Card
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
-   Use ``dd`` command to write ``ubuntu-sophgo.img`` to microSD Card

.. highlights::

    .. code:: sh

        # To find the block device name of your microSD Card.
        # For example, the microSD Card drive is /dev/sdc. Checking the name of your device is a key step,
        # as writing to the wrong device might corrupt or destroy your data.

        $ sudo dd if=ubuntu-sophgo.img of=/dev/sdc bs=1M

        10240+0 records in
        10240+0 records out
        10737418240 bytes (11 GB, 10 GiB) copied, 1211.08 s, 8.9 MB/s


-   Resize root partition of microSD Card (**Optional**)

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
        /dev/sdc1         2048   262143   260096  127M  c W95 FAT32 (LBA)
        /dev/sdc2       262144   524287   262144  128M  c W95 FAT32 (LBA)
        /dev/sdc3       524288 62333951 61809664 29.5G 83 Linux


.. highlights::

    .. code:: sh

        # Force checking your file system.
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


-   Copy image to ``/home/ubuntu`` on the root partition of the microSD Card.

.. highlights::

    .. code:: sh

        $ cp ubuntu-sophgo.img /mnt/home/ubuntu

4. Boot from microSD Card
=========================
-   Plug the microSD Card into the SG2042 EVB,
    connect the serial cable to your computer,
    and power on the EVB.
-   Enter the username ``ubuntu`` and the password ``ubuntu``.
-   Any operation needs the ``sudo`` privilege.

5. Use NVMe SSD and microSD Card
================================
If you want to boot your system from a combination of
NVMe SSD and microSD Card,
the following steps also need to be done.

a. Use the ``dd`` command to copy the ``ubuntu-sophgo.img`` to the NVMe disk.

b. Resize the root partition of the NVMe disk.

c. Use the ``fdisk`` command to delete the root partition of the microSD Card.

    .. note:: This step is critical because the root partition of the microSD Card and the NVMe disk has the same label!

d. Reboot, and access Ubuntu using the NVMe disk.
