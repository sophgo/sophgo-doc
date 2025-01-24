sysbench
------------------

sysbench工具介绍
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

参考(https://en.wikipedia.org/wiki/Sysbench)
``sysbench`` 是一个专为Linux系统设计的可编写脚本的多线程基准测试工具,最常用于数据库基准测试。
也可用于创建不涉及数据库服务器进行常规测试的任意复杂工作负载。

可以运行命令行标志或 shell 脚本中指定的基准测试

- ``cpu`` :CPU performance test
- ``fileio`` :File I/O test
- ``memory`` :Memory speed test
- ``mutex`` :Mutex performance test
- ``threads`` : Threads subsystem performance test

sysbench工具使用方法
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

详细步骤
^^^^^^^^^^^^^^^^^

.. code:: bash

   # ubuntu
   sudo apt install sysbench
   # openEuler
   sudo dnf install sysbench

命令格式如下：

``sysbench [options] [test] [command]``

常用测试命令：

.. code:: bash

   sysbench cpu --cpu-max-prime=20000 run #测试 CPU 计算质数的性能
   sysbench memory --memory-block-size=1M --memory-total-size=10G run #测试内存读取和写入的性能
   sysbench fileio --file-total-size=10G prepare
   sysbench fileio --file-total-size=10G run
   sysbench fileio --file-total-size=10G cleanup #测试文件 I/O 性能，包括准备、运行和清理步骤。

   #测试 MySQL 数据库的只读性能
   sysbench oltp_read_only --db-driver=mysql --mysql-host=localhost 
            --mysql-user=root --mysql-password=your_password --tables=10 --table-size=10000 prepare
   sysbench oltp_read_only --db-driver=mysql 
            --mysql-host=localhost --mysql-user=root --mysql-password=your_password run
   sysbench oltp_read_only --db-driver=mysql 
            --mysql-host=localhost --mysql-user=root --mysql-password=your_password cleanup

一般可使用CPU计算质数的性能，作为当前测试项的测试结果，所使用的命令为：

.. code:: bash

    # 测试cpu计算质数的性能（1 thread）
    sysbench cpu --cpu-max-prime=20000 --threads=1 run

    # 测试cpu计算质数的性能（64 thread）
    sysbench cpu --cpu-max-prime=20000 --threads=64 run

运行结果示例
^^^^^^^^^^^^^^^^^

.. figure:: sysbench.png
   :alt: sysbench
   :scale: 60
   :align: center

sysbench测试结果
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

测试结果
^^^^^^^^^^^

测试环境

- ``SG2044 EVB``
- ``dual-rank 128GB DDR``
- ``OpenEuler24.03 (LTS) Linux6.12.6``
- ``64 core C920@2.8GHz``

+---------------------+-----------------------+------------------------+
| performance metrics | test result(1 thread) | test result(64 thread) |
+=====================+=======================+========================+
| events per seconds  | 729.57 ms             | 46626.37 ms            |
+---------------------+-----------------------+------------------------+
| latency avg         | 1.37 ms               | 1.37 ms                |
+---------------------+-----------------------+------------------------+
| latency max         | 1.43 ms               | 11.39 ms               |
+---------------------+-----------------------+------------------------+
| latency min         | 1.37 ms               | 1.36 ms                |
+---------------------+-----------------------+------------------------+