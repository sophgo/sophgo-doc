===
FAQ
===

Where can I find prebuilt binaries?
===================================

We compile hole SG2042 software stack daily. You can get these binaries from our
NAS server.

http://219.142.246.77:65000//sharing/f73TDqXdN

How to install Fedora GUI?
===================================

https://www.server-world.info/en/note?os=Fedora_37&p=desktop&f=1

.. highlights::

    .. code:: sh

        # check your desktop environment
        dnf grouplist -v (or: dnf group list)
        # install GNOME
        dnf -y group install "Basic Desktop" GNOME
        # or install Xfce
        dnf -y group install "Xfce"
        # or install Cinnamon (auto install Firefox)
        dnf -y group install "Cinnamon"

        systemctl start display-manager

then you will enter the graphical login interface

if you would like to change your System to Graphical Login as default, set like follow:

.. highlights::

    .. code:: sh

        systemctl set-default graphical.target

