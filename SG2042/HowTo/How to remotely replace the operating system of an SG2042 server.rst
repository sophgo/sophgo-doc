================================================================
How to remotely replace the operating system of an SG2042 server
================================================================


1. Prerequisites
================
- An SG2042 server
- firmware in spi flash or microSD card 
- newtest BMC
- img
- ethnet
- Tools for converting IMG to ISO
- NVMe SSD

1. Convert IMG to ISO
======================
-   In Linux systems, the xorriso tool can be used. For Windows, please search for available tools on your own and use them to convert IMG files to ISO files.The following is an example of how to use the xorriso tool to convert an IMG file to an ISO file.
  
.. highlights:: 

    .. code:: sh

        xorriso -as mkisofs -iso-level 3 -o example.iso example.img

2. How to mount ISO
=================================

Option 1: 
--------------------------
- Start the SG2042 server and enter linux-boot

- Log into the BMC web interface. 

.. highlights::

    If there are network issues, you can use an Ethernet cable to connect the host computer to the SG2042 server's BMC, and then log into the BMC web interface at 192.168.0.45.

- Use Virtual Media to add the packaged ISO file.

.. highlights:: 

    If added successfully, a success message will be displayed.

- Mount an ISO in Linux boot environment
  
.. highlights:: 

    .. code:: sh

        # mkdir mnt
        # ls /dev | grep sr
        # mount /dev/sr1 mnt // Mount the fast device queried which find in ls /dev | grep sr


3.How to replace the operating system
=====================================

-   Use ``dd`` command to write img to NVMe SSD

.. highlights::

    .. code:: sh

        ## If the server uses only one NVMe, then the block device is generally nvme0n1.

        # sudo dd if=example.img of=/dev/nvme0n1 bs=1M status=progress

        10240+0 records in
        10240+0 records out
        10737418240 bytes (11 GB, 10 GiB) copied, 1211.08 s, 8.9 MB/s

- After completion, reboot.
