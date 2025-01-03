# SG2042 Benchmark测试方法

## 测试环境

### 1.SG2042 x8 EVB评估板

- 内存：DDR RDIMM 3200 128G
- CPU：2.0GHz

### 2.kunpeng920服务器

- 内存：DDR RDIMM 2933 512G
- CPU：2.6GHz

## 测试项目

| 测试项目 | 测试状态 | 现存问题和进展|
| ---- | ---- | ---- |
|  spec2017    |  DONE     | |
|  spec2006    |  DOING    | fprate未测试 |
|  unixbench    |  DONE    | |
|  coremark    |  DONE     | |
|  stream       |  DONE    | |
|  cache latency    |  DONE    | |
|  core-core latency    |  DONE    | |
|  litmus    |  DOING    | Failure: ISA-DEP-WR-ADDR，除此测试项，其他测试项已经完成，无问题。|
|  sysbench    |  DONE    | |
|  ltp    |  DOING    | full test已经跑完，失败项分析中 |
|  stress-ng    |  DOING    | 只压测了cpu、vm，其他测试项待测 |
|  fio    |  DONE    | |
|  redis benchmark    |  DONE    | |

## 测试方法

### 1.spec2017 & spec2006

Standard Performance Evaluation Corporation公司提供测试,测试结果示例如下所示

![测试结果](2024-12-02-13-29-00.png)

### 2.unixbench

测试结果示例如下<font color=red>测试方法待补充</font>
![测试结果](2024-12-02-13-30-41.png)

### 3.coremark

测试结果示例如下<font color=red>测试方法待补充</font>
![测试结果](2024-12-02-13-32-09.png)

### 4.stream

4种测试模式

| 测试模式 | SG2042 | kunpeng920 |
| ---- | ---- | ---- |
|  copy    |  37630.3 MB/s     | 105829.1 MB/s |
|  Scale    |  37922.4 MB/s    | 93430.6 MB/s |
|  Add    |  39089.5 MB/s    | 97665.0 MB/s |
|  Triad    |  38931.9 MB/s    | 91497.5 MB/s |

根据不同的CPU节点设置不同参数

| 测试设置 | copy | scale | add | triad |
| ---- | ---- | ---- | ---- | ---- |
|  cpu0_node0|  8518 MB/s     | 8784 MB/s |  8394 MB/s    | 8377 MB/s |
|  cpu0_node4    |  2680 MB/s     | 2693 MB/s |  2345 MB/s    | 2359 MB/s |
|  cpu0-63_node0-3    |  32037 MB/s  | 42554 MB/s |  36749 MB/s    | 35151 MB/s |
|  cpu0-63_node4-7    |  6854 MB/s     | 10086 MB/s |  9598 MB/s	| 10024 MB/s |
|  cpu0-127    |  53568 MB/s  | 53368 MB/s |  58949 MB/s	| 59681 MB/s |

测试结果示例如下

<span style="color: red;">测试方法待补充，图中编译参数有乱码</span>


![测试结果](2024-12-02-13-35-30.png)

### 5.cache bench

使用套间[Phoronix Test Suite](https://github.com/phoronix-test-suite/phoronix-test-suite/)
使用例程
<span style="color: red;">可能的测试方法如下</span>
```bash
git clone https://github.com/phoronix-test-suite/phoronix-test-suite.git
cd phoronix-test-suite
phoronix-test-suite benchmark cachebench
```

### 6.core-core latency

测试结果示例如下

<span style="color: red;">测试方法待补充</span>

![测试结果](2024-12-02-14-08-23.png)

### 7.litmus

#### 7.1测试准备

 [RISCV Litmus 标准测试仓库](https://github.com/litmus-tests/litmus-tests-riscv)

#### 7.2安装工具

-  `herdtools7`:编译Litmus的的过程需要使用herdtools7工具，根据herdtools7说明文档安装，其中可能需要安装Ocaml 和Opam 等包管理工具
```bash
sudo apt-get install opam
opam init && opam update && opam upgrade
opam install herdtools7
```

- `fedora`
```bash
sudo dnf install glibc-static
```

#### 7.3编译测试用例

```bash
git clone https://github.com/litmus-tests/litmus-tests-riscv
cd litmus-tests-riscv
make CORES=64 hw-tests
```
### 8.sysbench

测试结果示例如下

<span style="color: red;">测试方法待补充</span>

![测试结果](2024-12-02-13-55-33.png)

### 9.ltp


### 10.stress-ng

| 压测项 | 运行命令 | 测试结果|
| ---- | ---- | ---- |
|  CPU    |  stress-ng --cpu 64 -t 30m     | PASS |
|  VM    |  stress-ng --vm 64 -t 30m    | PASS |

### 11.fio

- 读
```bash
sudo fio -filename=/dev/nvme0n1 -direct=1 -iodepth 1 -thread -rw=read -ioengine=psync -bs=1M -size=10G -numjobs=64 -runtime=60 -group_reporting -name=nvme
```

- 写
```bash
sudo fio -filename=/dev/nvme0n1 -direct=1 -iodepth 1 -thread -rw=wirte -ioengine=psync -bs=1M -size=10G -numjobs=64 -runtime=60 -group_reporting -name=nvme
```

### 12.redis

```bash
redis-benchmark -n 100000  -q
```

### 13.DMIPS

下载源码https://github.com/ARM-software/workload-automation/tree/master/wa/workloads/dhrystone/src

进入目录
```bash
make
./dhrystone -I 100
```

### 14.网卡测试

