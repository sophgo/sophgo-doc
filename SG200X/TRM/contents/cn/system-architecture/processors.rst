处理器子系统
------------

本芯片除了一个小核处理器 (RISC-V C906@700MHz) 外, 还有两个大核主处理器: RISC-V C906@1GHz 和 ARM Cortex-A53@1GHz。大核与小核有两种组合模式, 通过管脚 GPIO_RTX 的外围电路控制进行切换 (具体参考 datasheet):

- 大核 (RISC-V C906@1GHz) + 小核 (RISC-V C906@700MHz)。

- 大核 (ARM Cortex-A53@1GHz) + 小核 (RISC-V C906@700MHz)。

ARM Cortex-A53@1GHz 处理器具有以下特点：

-  处理器工作频率最高可达 1.0 GHz。

-  支持 Neon。

-  支持浮点运算单元 FPU。

-  L1 Cache 包含 32KB Instruction Cache 和 32KB Data Cache。

-  128KB L2 cache。

-  支持 MMU (Memory Management Unit) 。

-  处理器内部集成中断控制器。

-  支持 JTAG 调试接口。

RISC-V C906@1GHz 处理器具有以下特点：

-  处理器工作频率最高可达 1.0GHz。

-  集成矢量执行单元，浮点协处理器。

-  L1 Cache 包含32KB Instruction Cache 和 64KB Data Cache。

-  支持 MMU (Memory Management Unit) 。

-  处理器内部集成中断控制器。

-  支持 JTAG 调试接口。
