===
FAQ
===

1. Where can I find prebuilt binaries?
===================================

We compile hole SG2042 software stack daily. You can get these binaries from our
NAS server.

http://219.142.246.77:65000//sharing/f73TDqXdN

2. Install GUI
==============

Fedora
------

https://www.server-world.info/en/note?os=Fedora_37&p=desktop&f=1

* Install desktop environment:

.. highlights::

    .. code:: sh

        # check your desktop environment
        sudo dnf grouplist -v (or: dnf group list)
        # install GNOME
        sudo dnf -y group install "Basic Desktop" GNOME
        # or install Xfce
        sudo dnf -y group install "Xfce"
        # or install Cinnamon (auto install Firefox)
        sudo dnf -y group install "Cinnamon"

* Change display-manager:

.. highlights::

    .. code:: sh

        systemctl disable lightdm.service
        systemctl enable gdm.service

* Set Graphical Login as default:

.. highlights::

    .. code:: sh

        sudo systemctl set-default graphical.target

* Restart display-manager service:

.. highlights::

    .. code:: sh

        sudo systemctl restart display-manager

Ubuntu
------

.. highlights::

    .. code:: sh

        sudo apt-get install xfce4
        sudo apt-get install gdm3
        sudo systemctl restart display-manager

3. Setup GRUB2
==============

.. tip:: Please backup the original ``grub.cfg`` before updating the GRUB. All Changes take effect after rebooting the system. 

Fedora
------

Refer to `Working with the GRUB 2 Boot Loader <https://docs.fedoraproject.org/en-US/fedora/latest/system-administrators-guide/kernel-module-driver-configuration/Working_with_the_GRUB_2_Boot_Loader/>`_ .

* Install GRUB2:

.. highlights::

    .. code:: sh

        sudo dnf -y update
        sudo dnf -y install grub2-efi-riscv64
        sudo dnf -y install grub2-efi-riscv64-cdboot
        sudo dnf -y install grub2-efi-riscv64-modules
        sudo dnf -y install grub2-tools*

* Update ``/boot/grub2/grub.cfg``:

.. highlights::

    .. code:: sh

        sudo grub2-mkconfig -o /boot/grub2/grub.cfg

* On Fedora38, please add the ``console=ttyS0,115200 selinux=0 earlycon`` behind the ``linux`` command manually.

Ubuntu
------

Refer to `Grub2/Setup <https://help.ubuntu.com/community/Grub2/Setup>`_ .

* Install GRUB:

.. highlights::

    .. code:: sh

        sudo apt-get update
        sudo apt-get install grub-efi-riscv64

* Modify cmdline ``GRUB_CMDLINE_LINUX_DEFAULT`` in the ``/etc/default/grub.d/cmdline.cfg``, set ``GRUB_CMDLINE_LINUX_DEFAULT="quiet splash console=ttyS0,115200 earlycon"``.

* Use the ``grub-mkconfig`` tool to generate ``/boot/grub/grub.cfg``:

.. highlights::

    .. code:: sh

        grub-mkconfig -o /boot/grub/grub.cfg

* Or use the ``update-grub`` to update ``/boot/grub/grub.cfg``:

.. highlights::

    .. code:: sh

        update-grub

* **Error 1** ``error: file `/boot/grub/fonts/unicode.pf2.``

.. highlights::

    .. code:: sh

        mkdir /boot/grub/fonts

        sudo cp /usr/share/grub/unicode.pf2 /boot/grub/fonts/

* **Error 2** ``error: file `/boot/grub/locale/C.gmo' not found.``

  Add ``LANG=en_US.UTF-8`` into ``/etc/default/grub``, and then type ``update-grub`` to update ``/boot/grub/grub.cfg``.
