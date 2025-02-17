Processor subsystem
-------------------

In addition to one little core processor (RISC-V C906@700MHz), this chip also has two big core main processors: RISC-V C906@1GHz and ARM Cortex-A53@1GHz. There are two combination modes of big core and little core, which are switched through the peripheral circuit control of the pin GPIO_RTX (refer to the datasheet for details):

- Big Core (RISC-V C906@1GHz) + Little Core (RISC-V C906@700MHz).

- Big Core (ARM Cortex-A53@1GHz) + Little Core (RISC-V C906@700MHz).

ARM Cortex-A53@1GHz processor has the following features:

- The processor operating frequency can reach up to 1.0 GHz.

- Support Neon.

- Support floating point unit FPU.

- L1 Cache includes 32KB Instruction Cache and 32KB Data Cache.

- 128KB L2 cache.

- Support MMU (Memory Management Unit).

- The processor has an internal integrated interrupt controller.

- Support JTAG debugging interface.

RISC-V C906@1GHz processor has the following features:

- The processor operating frequency can reach up to 1.0GHz.

- Integrated vector execution unit, floating point coprocessor.

- L1 Cache includes 32KB Instruction Cache and 64KB Data Cache.

- Support MMU (Memory Management Unit).

- The processor has an internal integrated interrupt controller.

- Support JTAG debugging interface.