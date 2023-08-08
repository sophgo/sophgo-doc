=========================================
Create bootable disk using prebuilt image
=========================================

1. Environment
===============
All operations perform on a Linux based PC.

2. Download prebuilt images from sophgo daily build
===================================================

We compile whole SG2042 software stack daily. You can get these binaries from our
NAS server.

http://219.142.246.77:65000//sharing/f73TDqXdN

3. Get the device file of you disk
==================================

.. highlights::

    .. code:: sh

        lsblk

        NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
        sdb      8:16   0   1.8T  0 disk

In my system, the target disk is /dev/sdb

4. Flush image to the disk directly
===================================

.. highlights::

    .. code:: sh

        sudo dd if=fedora-sophgo.img of=/dev/sdb bs=4M status=progress

NOTICE, DONOT flush the image to a partition of that disk, like /dev/sdb1, /dev/sdb2.

5. Enlarge the last partition to fit the disk
=============================================

.. highlights::

    .. code:: sh

        sudo parted /dev/sdb resizepart 3 100%

6. Check and repair any errors on root partition
================================================

.. highlights::

    .. code:: sh

        sudo e2fsck -f /dev/sdb3

7. Resize file system to fit the new partition size
===================================================

.. highlights::

    .. code:: sh

        sudo resize2fs /dev/sdb3

