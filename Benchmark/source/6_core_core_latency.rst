core-core latency
------------------

core-core latency工具介绍
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

将两个线程固定在两个不同的 ``CPU`` 内核上,我们可以让它们执行一系列 ``compare-exchange`` 操作,并测量延迟。

core-core latency工具使用方法
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

详细步骤
^^^^^^^^^^^^^^^^^

参考(https://wiki.sophgo.com/display/SW/SG2044-Core2Core-Latency)

.. code:: bash

   sudo apt-get install cargo #安装cargo
   cargo install core-to-core-latency #安装 core-to-core-latency 工具

   # 安装后可执行文件在.cargo/bin目录中
   export PATH=~/.cargo/bin:$PATH #添加环境变量

   #执行benchmark
   core-to-core-latency --csv > c2c-latency.csv

如果需要在另一台机器上用pyhton进行绘图,可以执行以下操作。

.. code:: bash


   git clone https://github.com/nviennot/core-to-core-latency.git

   #将c2c-latency放入core-to-core-latency的results文件夹中
   cp c2c-latency.csv core-to-core-latency/results

python脚本如下

.. code:: python

   import pandas as pd
   import numpy as np
   from matplotlib import pyplot as plt

   def load_data(filename):
      m = np.array(pd.read_csv(filename,header=None))
      return np.tril(m) + np.tril(m).transpose()

   def show_heapmap(m, title=None, subtitle=None, vmin=None,vmax=None, yticks=True, figsize=None):
      vmin = np.nanmin(m) if vmin is None else vmin
      vmax = np.nanmax(m) if vmax is None else vmax
      black_at = (vmin+3*vmax)/4
      subtitle = "Core-to-core latency" if subtitle is None else subtitle

      isnan = np.isnan(m)

   if __name__=="__main__":
      cpu = "SOPHGO SG2044, 2.0GHz, 64 Cores, 2024-Q3"
      fname = "c2c-latency.csv"
      m = load_data(fname)
      show_heapmap(m, title=cpu)

运行结果示例
^^^^^^^^^^^^^^^^^

.. figure:: core_core_latency.png
   :alt: 测试结果
   :scale: 20
   :align: center


core-core latency测试结果
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


测试环境:

- ``SG2042 EVB``
- ``32GB * 4 DDR``
- ``Fedora38``
- ``64 core C920@2.0GHz``

+----------------+---------------+----------------+
| the same Clust | the same Chip | different chip |
+================+===============+================+
| 47~48ns        | 150~210ns     | 700~1000ns     |
+----------------+---------------+----------------+
