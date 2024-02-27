**设计笔记（Design Notes）**

<!-- TOC -->

- [Sphnix 开发环境搭建](#sphnix-开发环境搭建)
	- [安装 Sphnix 以及相关软件](#安装-sphnix-以及相关软件)
	- [编辑器设置](#编辑器设置)
- [项目设计](#项目设计)
	- [本项目的基本需求:](#本项目的基本需求)
	- [SG200X 顶层项目文件组织架构](#sg200x-顶层项目文件组织架构)
	- [TRM 项目工程目录说明](#trm-项目工程目录说明)
	- [工程中章节级别源码的设计](#工程中章节级别源码的设计)
- [代码编写说明](#代码编写说明)
	- [RST 中插入图片的编写方式：](#rst-中插入图片的编写方式)
	- [有关表格](#有关表格)
	- [其他注意事项](#其他注意事项)
- [编译方法](#编译方法)
	- [自动化脚本 `build.sh` 方式](#自动化脚本-buildsh-方式)
	- [手动 make 方式](#手动-make-方式)

<!-- /TOC -->

# Sphnix 开发环境搭建


## 安装 Sphnix 以及相关软件

参考 ["Installing Sphinx"][4]。推荐采用 [PyPI 的方式][5] 安装，这种方式安装的 Sphinx 的版本比较新，而且跨平台。

安装完成后，查看 Sphinx 的版本。在命令提示符下键入 `sphinx-build --version`。 如果一切正常，您将看到刚安装的 Sphinx 软件包的版本号。以我本地安装的情况为例：

```shell
$ sphinx-build --version
sphinx-build 7.1.2
```

如果要做 pdf，则要继续安装 texlive，texlive 是制作 pdf 的前提，因为 sphinx 首先是生成 tex 再转 pdf。

Ubuntu 上可以采用 apt 方式安装 `sudo apt-get install texlive-full`。这样安装的是完整版本，会安装所有的国家的字体。

Windows 上可以参考："Windows下TeXLive 环境的安装与配置": <https://www.cnblogs.com/mqingqing123/p/16057591.html>，这里利用的是 iso 方式，注意在安装过程中可以选择支持的字体，我们不用支持所有的，这样会小一些。

Ubuntu 上也可以用 iso 方式安装 texlive。参考 <https://cloud.tencent.com/developer/article/1831654>。


## 编辑器设置

Latex 中存在中英文混排时特别要注意确保设置等宽字体显示，方便编辑时对齐操作。

以 VSCode 为例，可以参考 [网上经验总结][3]。

其他本项目代码编写中和编辑有关的注意事项：

- 代码缩进统一采用 tab，注意不要在保存文件时自动将 tab 转空格（这个一般有编辑器的选项控制）
- 1 个 tab 统一对应 8 个空格
- 表格中的排版统一用空格，不要用 tab。

# 项目设计

## 本项目的基本需求:

- SG200X 包含两个子项目 SG2002 和 SG2000。这两个项目采用的芯片有一些微小的差别，但绝大部分内容是一样的。
- 目前需要实现 TRM，也许以后会实现 datasheet。
- TRM 需要提供中文和英文版本
- TRM 的特点是表格特别多，而且表格主要是用于定义控制寄存器的使用。

## SG200X 顶层项目文件组织架构

```bash
$ tree -L 4 SG200X/
.
├── build.sh
├── doc
└── TRM
    ├── conf.py
    ├── contents
    │   ├── cn
    │   │   ├── audio
    │   │   └── ......
    │   └── en
    │       ├── audio
    │       └── ......
    ├── media
    │   ├── image100.png
    │   └── ......
    ├── sg2000_cn
    │   ├── make.bat
    │   ├── Makefile
    │   └── source
    │       ├── conf.py -> ../../conf.py
    │       ├── contents -> ../../contents/cn/
    │       └── index.rst
    ├── sg2000_en
    │   ├── make.bat
    │   ├── Makefile
    │   └── source
    │       ├── conf.py -> ../../conf.py
    │       ├── contents -> ../../contents/en
    │       ├── contents-share -> ../../contents/cn
    │       └── index.rst
    ├── sg2002_cn
    │   ├── make.bat
    │   ├── Makefile
    │   └── source
    │       ├── conf.py -> ../../conf.py
    │       ├── contents -> ../../contents/cn/
    │       └── index.rst
    └── sg2002_en
        ├── make.bat
        ├── Makefile
        └── source
            ├── conf.py -> ../../conf.py
            ├── contents -> ../../contents/en
            ├── contents-share -> ../../contents/cn
            └── index.rst
```

- `build.sh`: 用于构建的自动化 bash 脚本
- `doc`: 设计文档目录
- `TRM`: 该目录下存放 TRM 的工程项目源码，安排如下：
  - `conf.py`: 每个 sphinx 项目共享的配置文件，每个项目中会采用符号链接 `conf.py` 指向这个文件
  - `contents`: 这是一个目录，下面存放每个 sphinx 项目共享的源码，分为 cn（中文）和 en（英文）两个版本对应的子目录。每个子目录中按照一个章节对应一个子目录的方式安排。具体章节子目录的设计见下文 [工程中章节级别源码的设计](#工程中章节级别源码的设计)。每个工程会采用符号链接分别指向该目录下的 cn 或者 en 子目录。
  - `media`: 这是一个目录，下面存放每个 sphinx 项目共享的图片资源。图片文件格式统一为 png。为简化中英文双语处理，要求所有的图片中的文字都是英文，不出现中文。工程源码会引用该目录下的图片文件。
  - 工程目录。目前一共有四个工程，分别是：
    - `sg2000_cn`: SG2000 的中文版本
    - `sg2000_en`: SG2000 的英文版本
    - `sg2002_cn`: SG2002 的中文版本
    - `sg2002_en`: SG2002 的英文版本
    这些目录安排符合 Sphinx 工程的基本要求，但也根据我们自身项目的需求做了定制。具体参考下文 [TRM 项目工程目录说明](#trm-项目工程目录说明)。
    更多有关 SG2002 和 SG2000 条件编译的设计笔记参考 [《SG2000 和 SG2002 的条件编译编码设计笔记》](./design_conditional_sg200x.md)。

## TRM 项目工程目录说明

以 sg2002_cn 为例：

```bash
......
    ├── sg2002_cn
    │   ├── make.bat
    │   ├── Makefile
    │   └── source
    │       ├── conf.py -> ../../conf.py
    │       ├── contents -> ../../contents/cn/
    │       └── index.rst
......
```
- `make.bat`: Windows 环境下的 make 文件
- `Makefile`: Linux 环境下的 make 文件
- `source`：源码目录
  - `conf.py`: 这是一个符号链接，指向共享的 `conf.py` 文件。里面定义了 Sphinx 的工程配置。
  - `contents`: 这是一个符号链接，指向共享的中文版本的项目源码。注意对于英文版本的项目，譬如 `sg2002_en`，除了包含一个指向共享的英文版本源码的符号链接 `contents` 外，还会有一个额外的指向共享的中文版本源码的符号链接 `contents-share`。这主要是因为中英文版本共享了同一份英文的表格文件（后缀名为 `*.table.rst`）。而这些表格文件目前都是放在 `SG200X/TRM/contents/cn` 中。基于此设计，英文版本的源码可以通过如下方式和中文版本代码复用同一份表格。以 `SG200X/TRM/sg2002_en/source/contents/audio/audio_codec.rst` 为例：
    ```rst
    .. include:: ../../contents-share/audio/audio_dac_adc_registers_overview.table.rst
    ```
    **注意这里相对路径的写法**。
  - `index.rst`: 工程源码的总入口。


## 工程中章节级别源码的设计

TRM 的每个章节对应 `contents` 下的一个子目录，譬如 “系统概述” 对应 `SG200X/TRM/sg2002_cn/source/contents/system-overview`。同样以该章节为例，该章节目录中的文件安排例子如下

```bash
$ tree SG200X/TRM/sg2002_cn/source/contents/system-overview
SG200X/TRM/sg2002_cn/source/contents/system-overview
├── 0.index.rst
├── features.rst
├── introduction.rst
└── system-block-diagram.rst

0 directories, 4 files
```

大致就是每个章节有个入口文件 `0.index.rst`, 二级章节按文件分。目前暂时就不往下分了。

`0.index.rst` 里面采用 toctree 方式来包含二级章节的 rst 文件（参考 ["How to correctly include other ReST-files in a sphinx-project?"][1], 采用 include 方式有可能会引入重复定义等问题）。

# 代码编写说明

## RST 中插入图片的编写方式：

参考 `SG200X/TRM/contents/cn/system-overview/system-block-diagram.rst` 中插入图片的写法。

代码例子如下：

```rst
.. _diagram_system_block:
.. figure:: ../../../../media/image1.png
	:align: center

	系统框架
```

其中：
- `_diagram_system_block` 为锚点定义，规则：`_` + 前缀 `diagram` + `_` + `项目全局唯一的 id`；字符全部用小写。如果要引用该图片锚点可以使用如下语法，见下面代码例子, 注意不要带上开头的 `_`：
  ```rst
  :ref:`diagram_system_block`
  ``````

注意：
- 采用 figure 而不是 image，方式更灵活，参考 ["figure"][2]。

## 有关表格

从 WORD 直接转化来的 RST 中的表格存在以下问题：
- 字符串因为对齐被强制拆分换行了，很难阅读理解
- GRID 的制表方式当列较多时转化为 pdf 后容易造成超出页宽

建议修改后的代码例子如下：

```rst
.. _table_dmac_idreg:
.. table:: DMAC_IDREG, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 63:0 | DMAC_IDREG           | RO    | DMAC ID Number         |      |
	+------+----------------------+-------+------------------------+------+
```

其中：
- `_table_dmac_idreg` 为锚点定义，规则：`_` + 前缀 `table` + `_` + `项目全局唯一的 id`；字符全部用小写。如果要引用该图片锚点可以使用如下语法，见下面代码例子, 注意不要带上开头的 `_`：
  ```rst
  :ref:`table_dmac_idreg`
  ``````
- `:widths:` 是 table 的属性，可以用于控制表格每个列的相对宽度，数值表示的是比例关系，注意个数要和表格的列数一致。建议为表格都加上这个属性，好处是加上后，表格宽度会保持和页宽一致，这样整个文档的表格风格看上去会比较一致，不会有的宽有的窄，而且能够避免表格宽度超过页宽的问题。
- 表格的缩进采用 TAB，并且请注意 **不要** 设置编辑器自动将 TAB 转换为空格。

## 其他注意事项

- 文字中存在繁体的中文，需要修改为简体中文。
- 文字中有些表达是台湾的习惯，建议改为大陆的习惯。
- 中文字符和英文字符之间要加上空格隔开。例子：`中 zhong 文 wen`
- 中文字符和数字字符之间要加上空格隔开。例子：`中 123 文 456`
- 编译过程中的告警要尽量清除掉。
  - RST 转 latex 过程中的告警必须（MUST）清除
  - latex 转 pdf 过程中的告警尽量清除（FIXME：这部分有些机制还不清除，欢迎补充和完善）
- 注意中文的标点符号，譬如应该用 `。`，而不是 `.`
- 其他（FIXME）


# 编译方法

有两种构建方式可供选择。

## 自动化脚本 `build.sh` 方式

```bash
$ cd SG200X
$ ./build.sh
```

执行该命令将自动构建所有工程，并且在 SG200X 下输出对应的 pdf 文件如下：

```bash
......
├── out
│   └── TRM
│       ├── sg2000_cn
│       │   └── sg2000_trm_cn.pdf
│       ├── sg2000_en
│       │   └── sg2000_trm_en.pdf
│       ├── sg2002_cn
│       │   └── sg2002_trm_cn.pdf
│       └── sg2002_en
│           └── sg2002_trm_en.pdf
......
```

**注意 out 这个目录在 git 仓库中不存在，它是在构建过程中动态创建出来的。**

如果只想构建某一个工程，譬如 `sg2000_en`，可以输入命令如下：

```bash
$ cd SG200X
$ ./build.sh TRM/sg2000_en
```


## 手动 make 方式

以编译 SG2002 的 TRM 的中文版本为例：

- 在 Linux 下
```bash
cd SG200X/TRM/sg2002_cn
make clean
make pdf
```
生成的 pdf 文件的位置是：`SG200X/TRM/sg2002_cn/build/sg2002_trm_cn.pdf`

- 在 Windows 下

```powershell
cd SG200X/TRM/sg2002_cn
.\make.bat clean
.\make.bat latexpdf
```

生成的 pdf 文件的位置是：`SG200X/TRM/sg2002_cn/build/latex/sg2002.pdf`(FIXME: Windows 下还没有和 Linux 下操作统一。)


[1]: https://stackoverflow.com/questions/44563794/how-to-correctly-include-other-rest-files-in-a-sphinx-project
[2]: https://documatt.com/restructuredtext-reference/element/figure.html
[3]: https://www.liujiajia.me/2022/5/31/visual-studio-code-fixed-width-font
[4]: https://www.sphinx-doc.org/en/master/usage/installation.html
[5]: https://www.sphinx-doc.org/en/master/usage/installation.html#installation-from-pypi
