=========================================
Setup a local yum repository
=========================================

This tutorial is for people who

* Cannot access internet.
* Want a much faster repository locally.

1. Environment
===============

Fedora linux is needed, no matter what architecture it runs on.

On this tutoral, things are done on Fedora38 and SG2042. On x86 based PC may
need extra steps. I will point it out if needed.

Also, a large disk is needed depends on repositories you want to sync. For now,
SG2042 requires about 100GB space. 250GB may be a safer choice.

2. Prepare yum repository lists (x86 only)
===================================================

First of all we need add the repository of SG2042 to the system. If you are
working on an SG2042 platform, you can skip this step. Because they already
in your system.

Copy repository configuration file from SG2042 platform (eg. SG2042 Servers,
SG2042 EVBs or Milk-v pioneer boxs) to you local servers. They are in
'/etc/yum.repos.d'. Typecally 'fedora-repo-sophgo-sg2042.repo' and
'fedora-riscv-koji.repo'. Put them into '/etc/yum.repos.d' of your server.

3. Make sure which repository you want to sync
==============================================

.. highlights::

    .. code:: sh

        yum repolist

        repo id                                    repo name
        fedora-riscv-koji                          Fedora RISC-V Koji
        fedora-riscv-sophgo-sg2042                 Fedora RISC-V Sophgo SG2042

You should see 'fedora-riscv-koji' and 'fedora-riscv-sophgo-sg2042' in 'repo id'
column. You may see other repositories if on x86 PCs. They are reposities that
your PC need.

4. Install syncing tools
==============================================

.. highlights::

    .. code:: sh

        sudo yum install yum-utils


5. Start sync packages from internet to your local disk
=======================================================

Create a directory to store these packages

.. highlights::

    .. code:: sh

        mkdir fedora38-riscv-sophgo

Start syncing

.. highlights::

    .. code:: sh

        reposync --download-metadata --repoid=fedora-riscv-koji --repoid=fedora-riscv-sophgo-sg2042

This may take a long long long time depends on your and your repositories'
network. Practically, I spent about 16 hours with a speed of 1.7MB/s.


After this, you will get all packages and metadata of these repositories.
Don't forget the option '--download-metadata'. If this options is missing, you
need using another tool called 'createrepo' to rebuild metadata, and I failed
on that step.

6. Synchronize periodically
===========================

Most people want their local repository keep updated with the original
repository. You can schedule a timely work by cron. How to add a job in cron
is not included in this topic.

7. Install http server
===================================

Yum can use multiple protocols to transmit packages, http, ftp or nfs. Commonly
used protocls are http and https. In this tutorial, we use apache to build your
repository.

.. highlights::

    .. code:: sh

        sudo yum install httpd

8. Put your repository into apache default document root
========================================================

Apache uses '/var/www/html' as its document root by default. Of course, you can
choose another location. In that case, you should change the configuration file
of apache.

.. highlights::

    .. code:: sh

        sudo mv YOUR-REPO /var/www/http

9. Stop firewall of your server (DANGER)
===================================================

You should add reasonable policy to your firewall. If not, your firewall may
block accesses from clients. About how to setup a firewall is not included.
So if your network environment is secure enough, just stop your firewall.

.. highlights::

    .. code:: sh

        sudo systemctl stop firewall
        sudo systemctl disable firewall

10. Start your http server
===================================================

.. highlights::

    .. code:: sh

        sudo systemctl start httpd
        sudo systemctl enable httpd

11. Check if it works
===================================================

You can check if your repository works by accesss it in web browser

eg. your repository name is 'fedora38-riscv-sophgo'.

Access 'http://aaa.bbb.ccc.ddd/fedora38-riscv-sophgo/' by your browser, you can
see directories below it.

aaa.bbb.ccc.ddd is the ip of your server.

12. Replace repository setup on clients
=======================================

This operation performs on clients, not servers. You should change repository
configuration to the one you just built.

.. highlights::

    .. code::

        [fedora38-riscv]
        name=Fedora RISC-V
        baseurl=http://aaa.bbb.ccc.ddd/fedora38-riscv-sophgo/fedora-riscv-koji
        enabled=1
        gpgcheck=0

        [fedora38-riscv-sophgo]
        name=Fedora RISC-V SOPHGO
        baseurl=http://aaa.bbb.ccc.ddd/fedora38-riscv-sophgo/fedora-riscv-sophgo-sg2042
        enabled=1
        gpgcheck=0

