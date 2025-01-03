SG2042 Benchmark
================

测试环境
--------

1.SG2042 x8 EVB评估板
~~~~~~~~~~~~~~~~~~~~~

-  内存：DDR RDIMM 3200 128G
-  CPU：2.0GHz

2.kunpeng920服务器
~~~~~~~~~~~~~~~~~~

-  内存：DDR RDIMM 2933 512G
-  CPU：2.6GHz

测试项目
--------

1.spec2017
~~~~~~~~~~

   测量和比较计算机处理器的性能

1.1 sg2042
^^^^^^^^^^

====================== ========
测试项目               测试结果
====================== ========
sg2042 intspeed 64     1.55
sg2042 intrate 128cpoy 45.5
sg2042 intrate 64cpoy  45.6
sg2042 intrate 32cpoy  28.5
sg2042 intrate 1cpoy   1.10
sg2042 fpspeed 64      12.9
sg2042 fprate 128copy  35.5
sg2042 fprate 64copy   42.1
sg2042 fprate 32copy   29.4
sg2042 fprate 1copy    1.31
====================== ========

1.2 kunpeng920
^^^^^^^^^^^^^^

========================== ========
测试项目                   测试结果
========================== ========
kunpeng920 intrate 128copy 264
kunpeng920 intrate 128copy 234
kunpeng920 intrate 64copy  152
kunpeng920 fprate 64copy   148
========================== ========
