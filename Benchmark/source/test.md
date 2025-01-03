# SG2042 Benchmark

## 测试环境

### 1.SG2042 x8 EVB评估板

- 内存：DDR RDIMM 3200 128G
- CPU：2.0GHz

### 2.kunpeng920服务器

- 内存：DDR RDIMM 2933 512G
- CPU：2.6GHz

## 测试项目

| 测试项目 | 测试状态 | 现存问题和进展
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

### 1.spec2017

> 测量和比较计算机处理器的性能




#### 1.1 sg2042
>`float rate`+`f9_base`+`64-bit base pointers`=`fprate 64copy`
`interger rate`+`int_base`+`64-bit base pointers`=`intrate 64cpoy`
`interger speed`+`int_base`+`64-bit`=`intspeed 64`
`float speed`+`fp_base`+`64-bit`=`fpspeed 64`




| 测试项目 | 测试结果 |
| ---- | ---- |
|  sg2042 intspeed 64    |  1.55    |
|  sg2042 intrate 128cpoy    |  45.5    |
|  sg2042 intrate 64cpoy    |  45.6    |
|  sg2042 intrate 32cpoy    |  28.5    |
|  sg2042 intrate 1cpoy    |  1.10    |
|  sg2042 fpspeed 64    |  12.9    |
|  sg2042 fprate 128copy    |  35.5    |
|  sg2042 fprate 64copy    |  42.1    |
|  sg2042 fprate 32copy    |  29.4    |
|  sg2042 fprate 1copy    |  1.31    |

<font color=red>有几张pdf图里上述表格中没有涉及到</font>

#### 1.2 kunpeng920

| 测试项目 | 测试结果 |
| ---- | ---- |
|  kunpeng920 intrate 128copy     |  264    |
|  kunpeng920 intrate 128copy     |  234    |
|  kunpeng920 intrate 64copy    |  152    |
|  kunpeng920 fprate 64copy    |  148    |

### 2.spec2006

| 测试项目 | 测试结果 |
| ---- | ---- |
|  SG2042-EVB intrate 128copy     |  264    |
|  kunpeng920 intrate 128copy     |  234    |
|  kunpeng920 intrate 64copy    |  152    |
|  kunpeng920 fprate 64copy    |  148    |

 