=======================================================
How to remotely create a system disk for SG 2042 server
=======================================================


1. Prerequisites
================
- Computer with Linux OS
- SG2042 server
- NVMe SSD
- network or Ethernet cable
- img

2. Convert IMG to ISO
======================
-   Download packaging tool.

    On Linux systems, you can choose to use the xorriso tool.how to install the xorriso tool:

    .. highlights:: 

        .. code:: sh

            $ sudo apt-get install xorriso // ubuntu OS
            $ sudo dnf install xorriso //fedora OS
            $ sudo xorriso -as mkisofs -iso-level 3 -o example.iso example.img // convert img to iso

3. Mounting ISO using BMC Virtual Media
=======================================

-   Log in to the BMC web interface
    
    login to the BMC web interface, click on Operations, then select Virtual media, click Add file, choose the packaged ISO, and click Start，successful mounting will prompt "Successfully".

4. Create System Disk
=====================
-  start the server, enter the Linux-boot interface, and begin creating the system disk.
   
   .. highlights:: 

      .. code:: sh

        # lsblk /dev | grep sr // locate the mounted ISO, typically it's sr0 or sr1, using sr1 as an example.
        # mkdir /mnt // create a directory to mount the ISO
        # mount /dev/sr1 /mnt // mount the ISO to the directory
        # cd /mnt // enter the directory
        # ls // list the files in the directory
        # dd if=example.img of=/dev/nvme0n1 bs=1M status=progress // write the ISO to the NVMe SSD, using nvme0n1 as an example.

-   after dd is completed, stop Virtual media, then reboot, and you can enter the new OS.