===========================================
How to update pcie_switch's config firmware
===========================================

1. Introduction
====================

- The SG2042 server has two PCIE switches with model PM4052.
- These two switches have their own firmware files with the suffix **".fwimg"**.
- The method described in this article is only for in band upgrades.
- Ensure that the server network connection is normal during the upgrade process.

1. Update
====================
-   Shell script : fwimg-update.sh

.. highlights::

   .. code:: sh

      #!/bin/bash
      # ===========================================================
      # $1: 0-switchA 1-switchB
      # $2: firmware file
      # ===========================================================
      FILE=switchtec-user
      NAME=switchtec
      DEV_NAME=/dev/switchtec

      if [ "$#" -lt 2 ] ;then
         echo " Please specify two params !"
         exit
      else
         if [ $1 -eq 0 ] || [ $1 -eq 1 ] ;then
            IMAGE=$2
            IMAGE=${IMAGE##*.}
            if [ "$IMAGE"x != "fwimg"x ] ;then
               echo " The second parameter is not an fwimg file !"
               exit
            fi
         else
            echo " The first parameter invalid !"
            exit
         fi
      fi


      # user space 'switchtec' install
      if [ $(which switchtec  | wc -l) != 1 ] ;then
         if [ -d "$FILE" ] ;then
            rm -rf $FILE
         fi
         echo "Get source code from github!"
         git clone https://github.com/Microsemi/switchtec-user.git
         cd $FILE
         ./configure
         make
         sudo make install
      else
         echo " Switchtec has been installed ! "
      fi

      # kernel module 'switchtec' install
      if [ $(lsmod | grep $NAME | wc -l) == 0 ] ;then
         modprobe $NAME nirqs=4
         if [ $? -eq 0 ] ;then
            if [ $(ls /dev | grep $NAME | wc -l) -eq 2 ] ; then
               echo "modprobe $NAME success !"
            else
               echo "modprobe $NAME failed !"
            fi
         fi
      else
         echo " Module 'switchtec' has been loaded ! "
      fi

      sleep 3

      # fwimg update
      switchtec fw-update -A ${DEV_NAME}$1 $2
      sleep 3
      switchtec fw-toggle ${DEV_NAME}$1 -c
      if [ $? == 0 ] ;then
         echo "Complete switch$1's config img update , effective after restarting the server !"
      fi


- Update command

.. highlights::

   .. code:: sh

      # update switchA's firmware
      $ sudo ./fwimg-update.sh 0 switchA.fwimg

      # update switchB's firmware
      $ sudo ./fwimg-update.sh 1 switchB.fwimg

-  Restart the server