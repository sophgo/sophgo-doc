fio
------------------

fio测试工具介绍
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

``fio`` 主要用来对磁盘进行压力测试和性能验证,可以产生许多线程或进程来执行用户特定类型的I/O操作,通过编写作业文件或者直接命令去执行测试动作.

fio工具使用方法
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

详细步骤
^^^^^^^^^^^^^^^^^

.. code:: bash

   sudo apt-get install fio #安装 I/O 性能测试工具

-  读

.. code:: bash

   sudo fio -filename=/dev/nvme0n1 -direct=1 -iodepth 1 -thread -rw=read -ioengine=psync -bs=1M -size=10G -numjobs=64 -runtime=60 -group_reporting -name=nvme

-  写

.. code:: bash

   sudo fio -filename=/dev/nvme0n1 -direct=1 -iodepth 1 -thread -rw=wirte -ioengine=psync -bs=1M -size=10G -numjobs=64 -runtime=60 -group_reporting -name=nvme

运行结果示例
^^^^^^^^^^^^^^^^^

fio测试结果
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>