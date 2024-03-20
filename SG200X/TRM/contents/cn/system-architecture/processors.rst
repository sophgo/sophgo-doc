处理器子系统
------------

本芯片有两个主处理器：RISC-V C906 和 ARM Cortex-A53，通过管脚 GPIO_RTX 的外围电路控制进行切换（具体参考datasheet），有两种工作模式：

- RISC-V C906@1GHz + RISC-V C906@700MHz。

- ARM Cortex-A53@1GHz + RISC-V C906@700MHz。

采用ARM Cortex-A53处理器，具有以下特点：

-  处理器工作频率最高可达 1.0 GHz。

-  支持 Neon。

-  支持浮点运算单元 FPU。

-  L1 Cache 包含 32KB Instruction Cache 和 32KB Data Cache。

-  128KB L2 cache。

-  支持MMU（Memory Management Unit）。

-  处理器内部集成中断控制器。

-  支持 JTAG 调试接口。

采用 RISCV C906 处理器，具有以下特点：

-  处理器工作频率最高可达 1.0GHz。

-  集成矢量执行单元，浮点协处理器。

-  L1 Cache 包含32KB Instruction Cache 和 64KB Data Cache。

-  支持MMU（Memory Management Unit）。

-  处理器内部集成中断控制器。

-  支持 JTAG 调试接口。
