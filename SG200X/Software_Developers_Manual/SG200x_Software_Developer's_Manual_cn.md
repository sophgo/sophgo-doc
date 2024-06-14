# 目录

[TOC]
# 1. SG200x SDK软件包
## 1.1 概述
SG200x SDK支持Linux、FreeRTOs两个系统，适用于SG200x系列芯片及搭载了此芯片的所有开发板产品。软件包及相关代码将全部开源在官方GitHub平台上，具体获取及使用方法，请参考后续章节。

## 1.2 SDK工程目录介绍
- build: 编译目录，存放编译脚本和板级配置
- buildroot-2021.05: buildroot 开源工具
- host-tools: 工具链
- freertos: freertos 系统
- fsbl: fsbl 启动固件
- isp_tuning: 图像效果调试参数存放路径
- linux_5.10: 开源 Linux 内核
- middleware: 自研多媒体框架，包含 so 与 ko
- opensbi: 开源 opensbi 库
- osdrv: 驱动程序
- oss: 第三方库
- ramdisk: 存放最小文件系统的预编译目录
- u-boot-2021.10: 开源 uboot 代码
- cvimath: 数学运算库
- cvibuilder: 定义tpu cvimodel文件
- cviruntime: 作为 SDK 发布的库，用于开发 TPU 应用程序
- cvikernel: 用于生成TPU指令
- flatbuffers: 第三方开源库
- cnpy: 提供可读写npy、npz数据格式的c++接口
- install: 执行一次完整编译后，镜像的存放路径

# 2. SDK开发环境搭建
本节主要介绍如何在本地搭建SG200x软件所需编译环境。当前SDK只支持在Linux环境下编译，并提供Linux下的编译工具链。

## 2.1 Linux服务器
开发者可选择使用：
- Ubuntu OS计算机
- Windows OS计算机 + 准备Ubuntu环境

以上两种方式，推荐安装**Ubuntu 22.04 LTS**以上系统版本进行编译。
- Virtualbox VM 安装: Windows环境下可以通过安装虚拟机来安装Linux环境， [VM下载地址](https://www.virtualbox.org/wiki/Downloads)
- Docker 安装：Windows环境下可以安装Docker Desktop for Windows，通过拉取ubuntu镜像得到Linux环境，[docker下载地址](https://docs.docker.com/desktop/install/windows-install/)
Ubuntu 22.04 LTS下载网址: https://www.releases.ubuntu.com/22.04/ubuntu-22.04.3-desktop-amd64.iso

### 2.1.1 于VirtualBox VM安装Ubuntu
- 建立新的 VM，并加以命名
  [![pFBTKFx.png](https://s11.ax1x.com/2024/03/04/pFBTKFx.png)](https://imgse.com/i/pFBTKFx)

- 规划8GB内存供VM使用
  [![pFBTQfK.png](https://s11.ax1x.com/2024/03/04/pFBTQfK.png)](https://imgse.com/i/pFBTQfK)

- 预留200GB硬盘空间，供后续存放SDK用
  [![pFBTakt.png](https://s11.ax1x.com/2024/03/04/pFBTakt.png)](https://imgse.com/i/pFBTakt)

- 第一次开机需要挂在安装光盘ISO档案
  [![pFBTBp8.png](https://s11.ax1x.com/2024/03/04/pFBTBp8.png)](https://imgse.com/i/pFBTBp8)

- 开始安装
    [![pFBLHFs.png](https://s11.ax1x.com/2024/03/04/pFBLHFs.png)](https://imgse.com/i/pFBLHFs)
- 设定VirtualBox Host-only Ethernet Adapter以便Host与VirtualBox沟通（终端服务以及档案分享）

注：示例图以Ubuntu20.04，实际请安装推荐版本。

### 2.1.1.1 安装Samba Server
Ubuntu VB需要安装Samba套件，方便后续Host PC与其做挡案分享。
安装Samba前，先用ifconfig获取IP 资讯，第一次安装会发现没有net-tool支持，需要安装net-tool
```
sudo apt install net-tools
sudo apt-get install samba samba-common
```
建立账号的samba 密码
`sudo smbpasswd -a sophgo`

修改/etc/samba/smb.conf，增加以下的内容
```
[sophgo]
path = /home/sophgo
writable = yes
browseable= yes
valid users = sophgo
```
启动samba server
`sudo service smbd restart`

WINDOW PC端连接到Samba server，然后参考2.2 安装编译依赖即可进行编译。


### 2.1.2 于docker安装Ubuntu
- 安装好docker后，在命令行中输入`docker pull ubuntu:22.04`，即可拉取ubuntu22.04的镜像
- 使用`docker images`，查看拉取到的镜像
- 输入`docker run -it ubuntu:22.04 /bin/bash`，即可创建并运行一个容器，当终端中出现`root@<string>:/#`时，则表示容器创建完成且已经进入容器，其中，string是容器的id，即containerId；

若需要退出在容器内退出容器，输入`exit`即可，若需要在容器外再次进入容器，则在终端中依次输入`docker start <containerId>`，`docker attach <containerId>`即可。（更多指令可参考docker官方教程）

### 2.1.3 安装SSH Server
SSH Server安装
```
sudo apt-get install ssh
sudo apt-get install openssh-server
```
安装后可以修改一些 ssh 的设定, 如port, 密码认证, root登入等
```
vim /etc/ssh/sshd_config
```
然后添加
```
Port 22
PasswordAuthentication yes
PermitRootLogin yes  //是否开放 root 登入
```
修改后要重启SSH
`/etc/init.d/ssh restart`


## 2.2 安装编译依赖
在准备好的Linux环境下，编译 SDK 环境搭建所依赖的软件包安装命令如下：

```
sudo apt update
sudo apt install -y pkg-config build-essential ninja-build automake autoconf libtool wget curl git gcc libssl-dev bc slib squashfs-tools android-sdk-libsparse-utils jq python3-distutils scons parallel tree python3-dev python3-pip device-tree-compiler ssh cpio fakeroot libncurses5 flex bison libncurses5-dev genext2fs rsync unzip dosfstools mtools tcl openssh-client cmake expect
```
- 注意：cmake 最低版本要求为 `3.16.5`，请检查您的版本，若不满足 SDK 的最低版本要求，请手动安装最新版本。若编译遇到报错，可以视报错信息，安装对应的软件包。
```
wget https://github.com/Kitware/CMake/releases/download/v3.27.6/cmake-3.27.6-linux-x86_64.sh
chmod +x cmake-3.27.6-linux-x86_64.sh
sudo sh cmake-3.27.6-linux-x86_64.sh --skip-license --prefix=/usr/local/
```
- 手动安装的 cmake 在 `/usr/local/bin` 目录下，使用 `cmake --version` 命令可查看其版本号。

# 3. SDK安装准备工作
## 3.1 Git配置
在拉取仓库前，请配置自己的Git信息，以防碰到hook检查的报错：
```
git config --global user.name "your name"
git config --global user.email "your mail"
```
设置git的全局`postBuffer`为一个足够大的值，以免在拉取仓库时出现EOF错误。
```
git config --global http.postBuffer 2147483648
```

## 3.2 SDK获取
### 3.2.1 自动化脚本拉取
- 本 SDK 仓库采用自动化脚本的方式管理子仓库，在拉取 SDK 时请使用如下的命令：
```
git clone https://github.com/sophgo/sophpi.git -b sg200x-evb
cd sophpi
./scripts/repo_clone.sh --gitclone scripts/subtree.xml
```
脚本默认使用SSH拉取子仓库，请确保您已经添加密钥到您的Github账户中，否则将碰到SSH认证失败的报错。
相关方法请参考文档：[新增 SSH 密钥到 GitHub 帐户](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

或者，您可以使用HTTPS URL来克隆仓库，将`scritps/repo_clone.sh`脚本中SSH部分
`REMOTE_URL=$(grep -o '<remote.*/>' ${dir} | sed 's/.*fetch="\([^"]*\)".*/\1/' | sed "s/ssh:\/\/\(.*\)/ssh:\/\/$USERNAME@\1/")`
修改为
`REMOTE_URL=$(grep -o '<remote.*/>' ${dir} | sed 's/.*fetch="\([^"]*\)".*/\1/' | sed "s/git@\(.*\):/https:\/\/\1\//")` 即可。

在修改脚本后，请对照SDK工程目录章节，确保是否成功克隆了所有的子仓库。如果您的GitHub账户启用了2FA，可能需要额外使用Personal Access Token来代替密码进行认。在这种情况下，Git 会提示你输入用户名和密码，你的用户名就是你的 GitHub 用户名，密码则是你的 PAT。

> 注意：我们更推荐您使用SSH的方式拉取代码，SSH协议在发送数据时会对数据进行加密操作，数据传输更安全，有效减少拉取失败的风险。

### 3.2.2 分别拉取子仓库
如果您无法使用自动化脚本的方式拉取代码，也可以使用如下命令分别拉取各个子仓库：

```
mkdir sophpi -p && cd sophpi
git clone https://github.com/sophgo/host-tools.git
git clone https://github.com/sophgo/build -b sg200x-dev
git clone https://github.com/sophgo/freertos -b sg200x-dev
git clone https://github.com/sophgo/FreeRTOS-Kernel -b sg200x-dev freertos/Source
git clone https://github.com/sophgo/Lab-Project-FreeRTOS-POSIX -b sg200x-dev freertos/Source/FreeRTOS-Plus-POSIX
git clone https://github.com/sophgo/fsbl -b sg200x-dev
git clone https://github.com/sophgo/isp_tuning -b sg200x-dev
git clone https://github.com/sophgo/linux_5.10 -b sg200x-dev
git clone https://github.com/sophgo/middleware -b sg200x-dev
git clone https://github.com/sophgo/SensorSupportList middleware/v2/component/isp
git clone https://github.com/sophgo/opensbi -b sg200x-dev
git clone https://github.com/sophgo/osdrv -b sg200x-dev
git clone https://github.com/sophgo/oss
git clone https://github.com/sophgo/ramdisk -b sg200x-dev
git clone https://github.com/sophgo/u-boot-2021.10 -b sg200x-dev
git clone https://github.com/sophgo/buildroot-2021.05.git
git clone https://github.com/sophgo/cvimath.git
git clone https://github.com/sophgo/cvibuilder.git
git clone https://github.com/sophgo/cviruntime.git
git clone https://github.com/sophgo/cvikernel.git
git clone https://github.com/sophgo/cnpy.git
git clone https://github.com/sophgo/flatbuffers.git
```
之后按照即可按照正常程序获取 SDK 并编译。

## 3.3 SDK更新
1. 如果您按照自动化脚本的方式获取sophpi SDK, 可以通过命令：
`./scripts/repo_clone.sh --gitpull scripts/subtree.xml`
来统一对子仓库进行更新。

2. 如果您分别拉取的子仓库，可以通过以下示例脚本来对所有仓库进行管理更新：
```bash
#!/bin/bash

repos_dir="./"

for dir in "$repos_dir"/*; do
    if [ -d "$dir" ]; then
        cd "$dir" || exit
        if [ -d ".git" ]; then
            echo "Updating $(basename "$dir")"
            git pull
        else
            echo "$(basename "$dir") is not a Git repository, skipping..."
        fi
        cd - > /dev/null || exit
    fi
done
```
并通过以下命令来给予此脚本执行权限：
`chmod +x yourscript.sh`

## 3.4 SDK问题反馈
如果您对仓库有任何的疑问或者反馈，请通过邮箱联系：
- [kenneth.liu@sophgo.com](kenneth.liu@sophgo.com)
- [sijie.wang@sophgo.com](sijie.wang@sophgo.com)
- [runze.lin@sophgo.com](runze.lin@sophgo.com)
仓库维护者会及时对问题进行维护和处理，帮助客户更好的进行开发工作。

# 4. SDK编译
SDK基于操作系统可分为ARM和RISC-V两种版本。用户可以根据需求对应选择配置进行编译使用。

## 4.1 环境变量说明
编译前置动作最主要是为了设置两个环境变量：`$CHIP`, `$BOARD`,
`$CHIP` 变量是需要根据用户的 SOC 来做设置。
`$BOARD` 变数是针对每张 EVB, 有不同的驱动，必须要正确设置。
注：BOARD可以直接看 EVB 上镭射型号得知。

## 4.2 配置软件包
- 首先切换到 SDK 的根目录

- 设定环境变量前需要先透过下列命令初始化环境，系统会列出目前SDK支持的IC以及EVB版号：
```
source build/envsetup_soc.sh
```
- 会出现以下的提示：
```
  -------------------------------------------------------------------------------------------------------
    Usage:
    (1) menuconfig - Use menu to configure your board.
        ex: $ menuconfig

    (2) defconfig $CHIP_ARCH - List EVB boards($BOARD) by CHIP_ARCH.
       ** cv181x ** -> ['cv181x', 'cv1811h', 'cv1811c', 'cv1810c', 'cv1810h', 'cv1812cp', 'cv1812h', 'cv1813h', 'sg2000', 'sg2002']
       ** cv180x ** -> ['cv180x', 'cv1800b', 'cv1800c', 'cv1801b', 'cv1801c', 'cv180zb']
        ex: $ defconfig cv181x

    (3) defconfig $BOARD - Choose EVB board settings.
        ex: $ defconfig cv1813h_wevb_0007a_spinor
        ex: $ defconfig cv1812cp_wevb_0006a_spinor
  -------------------------------------------------------------------------------------------------------
```
初始化之后，可以下列两种方式进行编译组态的设定。

### 4.2.1 通过defconfig设定（一键选定）
- 根据以上的提示，输入 `defconfig cv181x`，就会列出当前支持的开发板列表:
```
* cv181x * the avaliable cvitek EVB boards
 cv1811h - cv1811h_wevb_0007a_emmc [C906B + EMMC 512MB + BGA SIP 128MB]
           cv1811h_wevb_0007a_spinand [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1811h_wevb_0007a_spinor [C906B + SPINOR 16MB + BGA SIP 128MB]
 cv1811c - cv1811c_wdmb_0006a_spinor [C906B + SPINOR 16MB + BGA SIP 128MB]
           cv1811c_wevb_0006a_emmc [C906B + EMMC 8192MB + BGA SIP 128MB]
           cv1811c_wevb_0006a_spinand [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1811c_wevb_0006a_spinor [C906B + SPINOR 16MB + BGA SIP 128MB]
 cv1810c - cv1810c_wdmb_0006a_spinor [C906B + SPINOR 8MB + QFN SIP 64MB]
           cv1810c_wevb_0006a_spinand [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1810c_wevb_0006a_spinor [C906B + SPINOR 16MB + QFN SIP 64MB]
 cv1810h - cv1810h_wevb_0007a_spinor [C906B + SPINOR 8MB + BGA SIP 64MB]
cv1812cp - cv1812cp_sophpi_duo_sd [C906B + EMMC 8192MB + BGA SIP 256MB]
           cv1812cp_wevb_0006a_emmc [C906B + EMMC 8192MB + BGA SIP 256MB]
           cv1812cp_wevb_0006a_spinand [C906B + SPINAND 256MB + BGA SIP 256MB]
           cv1812cp_wevb_0006a_spinor [C906B + SPINOR 16MB + QFN SIP 256MB]
 cv1812h - cv1812h_wevb_0007a_emmc [C906B + EMMC 512MB + BGA SIP 256MB]
           cv1812h_wevb_0007a_emmc_huashan [C906B + EMMC 512MB + BGA SIP 256MB]
           cv1812h_wevb_0007a_spinand [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1812h_wevb_0007a_spinand_huashan [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1812h_wevb_0007a_spinor [C906B + SPINOR 16MB + BGA SIP 256MB]
           cv1812h_wevb_0007a_spinor_huashan [C906B + SPINOR 16MB + BGA SIP 256MB]
 cv1813h - cv1813h_wevb_0007a_emmc [C906B + EMMC 512MB + BGA SIP 256MB]
           cv1813h_wevb_0007a_spinand [C906B + SPINAND 256MB + BGA SIP 128MB]
           cv1813h_wevb_0007a_spinor [C906B + SPINOR 16MB + BGA SIP 256MB]
  sg2000 - sg2000_wevb_arm64_sd [CA53 + SPINOR 16MB + BGA SIP 128MB]
           sg2000_wevb_riscv64_sd [C906B + EMMC 8192MB + DDR 512MB]
  sg2002 - sg2002_wevb_arm64_sd [CA53 + SPINOR 16MB + BGA SIP 128MB]
           sg2002_wevb_riscv64_sd [C906B + EMMC 8192MB + DDR 256MB]
```
再次输入对应的开发板型号及所需的架构即可完成SDK编译组态的一键选定，如`defconfig sg2000_wevb_riscv64_sd`。

### 4.2.2 通过menuconfig设定 （单独配置）
- 输入`menuconfig`进入以下页面，即可选择各种SDK内部设定，包含CHIP，EVB板号等。
```
(Top)
                          CViTek MediaSDK Configuration
(generic) Customer define
    Chip selection (sg2002)  --->
    Board selection (duo_sd (C906B + EMMC 512MB + BGA SIP 256MB))  --->
    DDR configuration selection (ddr3_1866_x16)  --->
(riscv) Arch define
    Compile-time checks and compiler options  --->
    SDK options  --->
    FIP setting  --->
    Storage settings  --->
    Sensor settings  --->
    Panel settings  --->
    uboot options  --->
    Kernel options  --->
    ROOTFS options  --->
    Turnkey options  --->
    RTOS options  --->
    Rootfs packages  --->


[Space/Enter] Toggle/enter  [ESC] Leave menu           [S] Save
[O] Load                    [?] Symbol info            [/] Jump to symbol
[F] Toggle show-help mode   [C] Toggle show-name mode  [A] Toggle show-all mode
[Q] Quit (prompts for save) [D] Save minimal config (advanced)
```
按照下方提示，配置过程可以通过[Enter] [Space] [ESC] 等进行进入/设置/返回的动作
配置完毕后, 按下[S]储存配置文件, 接着按下[Q]离开图形化接口
(或者按下 ESC, 会自动弹出是否需要储存的图形)

- 选择芯片：进入Chip selection，对应选择芯片型号
- 切换架构：进入Arch define, 输入对应架构riscv或者arm即可切换
- ROOTFS设置：进入ROOTFS Options， 请注意勾选`Enable buildroot generate rootfs`来确保镜像的成功构建


## 4.3 编译完整SDK文档
完成以上编译组态的设定后，输入 `clean_all && build_all` 开始自动编译，编译成功后即可在install目录下看到可用于烧录的upgrade.zip压缩包。 若继续执行`pack_burn_image`即可直接生成镜像sophpi-duo-XXX.img。若编译出现问题，请检查是否有文件缺失，重新拉取相应仓库，并重新按步骤编译。

```
clean_all && build_all
pack_burn_image
```
> 注意：无论用以上哪种方式进行组态设定，都请使用`menuconfig`来确认您已经勾选`Enable buildroot generate rootfs`，否则系统可能会启动失败。

## 4.4 编译部分SDK文档
### 4.4.1 U-boot单独编译
每个EVB板会在特定位置定义进入U-Boot之前，EVB需要采取的初始化动作或是定义特定PINMUX，路径在
`./build/boards/sg200x/$CHIP_$BOARD/u-boot/cvi_board_init.c`，
其对应的u-boot组态，路径在：
`./build/boards/sg200x/$CHIP_$BOARD/u-boot/$CHIP_$BOARD _defconfig`

以图形化接口修改Uboot Config `$ menuconfig_uboot`, 退出后会把设定储存在:
`./u-boot-2021.10/build/"$CHIP"_"$BOARD"/.config`

进入工程根目录，执行编译
`$ build_uboot`
完成后会在instal路径下生成flip.bin

### 4.4.2 Kernel单独编译
修改 kernel (ex: *.dts, *.c), 重新编译 Linux kernel image。

每张EVB都有对应的dts档案来定义其device tree，路径在:
`./build/boards/sg200x/"$CHIP"_"$BOARD"/dts_riscv/"$CHIP"_"$BOARD".dts`

其相对应的linux组态，路径在：
`./build/boards/sg200x/"$CHIP"_"$BOARD"/linux/"$CHIP"_"$BOARD"_defconfig`

以图形化接口修改Kernel Config `$ menuconfig_kernel`,退出后会把设定储存在：
`./linux/build/"$CHIP"_"$BOARD"/.config`

进入工程根目录，执行编译
`$ build_kernel`
完成后会在instal路径下生成boot.sd

### 4.4.3 Middleware单独编译
进入工程根目录，执行编译：
`$ build_middleware; pack_rootfs`

`build_middleware` 会针对Sensor driver（位于`middleware/v2/component/isp/`下）以及sample application（位于`middleware/v2/sample/`下）重新编译，最终pack_rootfs会将变更后的driver以及application包装成可烧录映像档。

## 4.5.分区档案修改
分区档案放置于`build/boards/<CHIP>/<EVB_Name>/partition/partion_<physical_partition>.xml`
例如，sg2002_duo_sd的分区档案，陈列如下：
```xml
<physical_partition type="sd">
    <partition label="BOOT" size_in_kb="80960" readonly="false" file="boot.sd"/>
    <partition label="ROOTFS" size_in_kb="204800" readonly="false" file="rootfs.sd" />
    <partition label="DATA"  size_in_kb="512000" readonly="false" file="data.sd" mountpoint="/mnt/data" type="ext4" />
</physical_partition>
```
- physical_partition type：flash 种类。
- partition label： 分区名称。
- size_in_kb：分区大小。
- file：所指向的image file名称。
- type：（在partition label栏位中） 文件系统格式。
- mountpoint：分区挂载路径。

# 5.SDK固件升级
本章节主要介绍如何将构建完整的文件烧写并运行在设备上。提供SD卡烧裸烧和USB烧录两种方法介绍。

## 5.1 SD卡烧录
### 5.1.1.裸烧流程解释
[![pFBLIeg.png](https://s11.ax1x.com/2024/03/04/pFBLIeg.png)](https://imgse.com/i/pFBLIeg)


### 5.1.2 使用前准备
- 前述章节产生的烧录档案
- FAT32格式的Micro SD卡。

### 5.1.3 操作过程
> 注意：烧录过程中会清除 SD 卡中的全部内容，请务必提前做好备份！
- 将烧录档案放到SD卡中。(可选择直接使用镜像，或者使用upgrade.zip两种方式)
- 将SD卡插入EVB的SD卡槽中。
- 将平台重开机。

#### 5.1.3.1 使用镜像
- 在 Windows 下，可以使用 `balenaEtcher`，`Rufus` 或 `Win32 Disk Imager` 等工具将生成的镜像写入 SD 卡中。
- 在 Linux 下，可以使用 dd 命令将镜像写入 SD 卡中:
```
sudo dd if=sophpi-duo-XXX.img of=/dev/sdX
```

#### 5.1.3.2 使用upgrade.zip
- 接好 EVB 板的串口线
- 将 `install` 目录下的 `upgrade.zip` 压缩包解压缩并放入 SD 卡根目录，取决于具体开发板型号，压缩包中的文件可能不同：
```
soc_sg2002_duo_sd
.
├── boot.sd
├── META/
├── partition_sd.xml
├── rootfs.sd
└── utils/
```
- 将 SD 卡插入卡槽中
- 给开发板上电，开机就会自动进入烧录。
- 等待烧录成功后，拔掉 SD 卡，重新给开发板上电，即可进入系统。

## 5.2 USB烧录
### 5.2.1 使用前准备
- 安装python3
- 使用下列步骤安装 Pip
  - 下载 https://bootstrap.pypa.io/get-pip.py
  - 使用”python get-pip.py”安装 pip
- 使用“python -m pip install pyserial”安装 pyseria
- 前述章节产生的烧录档案

### 5.2.2 操作过程
请参考cvitek系列芯片裸烧手册：[裸烧与非裸烧升级使用手册](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Cvitek_Bare_and_Non-Bare_Chip_Burning_Upgrade_Operation_Guide/build/html/index.html)

#### 5.2.2.1 Windows
1. 准备好固件目录 (由平台对应 upgrade.zip 解压出来)
2. 将平台的 Uart 连上 Host 并且将平台断电, 并在命令提示字符下执行以下命令
3. cd <path\to\project\>\build\tools\cv181x\usb_dl\
4. py cv181x_dl.py –libusb –image_dir <firmware path>
5. 执行成功后，将平台上电

#### 5.2.2.2 Linux
1. 准备好固件目录 (由平台对应 upgrade.zip 解压出来)
2. 将平台的 Uart 连上 Host 并且将平台断电, 并在终端机执行
3. cd <path/to/project>/build/tools/cv181x/usb_dl/
4. py cv181x_dl.py –libusb –image_dir <firmware path>
5. 执行成功后，将平台上电

### 5.2.3 注意事项
1. 使用 USB 烧录时，请使用 USB 供电，并确认移除 DC 供电。
2. 如果遇到脚本无法正常执行完成, 可以用 ctrl+c 中断脚本, 并将平台断电后, 重新执行 USB刻录

## 5.3 根文件系统(rootfs)
### 5.3.1 根文件系统介绍
内核是 Linux 操作系统的核心，文件系统是用户和操作系统沟通的主要工具。所以要使用 Linux时，要先了解文件系统原理。
根文件系统结构是以”/”为“根 (root)”起始的树状目录结构，当内核程序映像 (uImage) 启动会挂载一个设备 (ex:eMMC) 在根目录上，根文件系统通常存放在内部存储器 (DRAM) 或非挥发内存 (FLASH) 中，或是透过网络存取的文件系统 (NFS)。所有应用程序和函式库都会按照分类放入文件系统中，以下列出根文件系统目录结构图。
```
/ 根目录
├── bin可执行文件
├── dev设备文件
├── etc系统配置文件(ex: 启动文件)
├── home用户目录
├── init开机执行script
├── kdump内核除错目录
├── lib函式库包含glibc, shared library和内核模块
├── mnt临时文件系统的挂载点
├── proc内核和行程信息的虚拟文件系统
├── sbin系统管理的可执行文件
├── sys系统设备和文件层次结构，提供内核数据数据
├── usr此目录下包含用户自定义应用程序和文文件
└── var存放系统日志和服务程序文件
```

### 5.3.2 Rootfs
本章节是描述文件系统之组成方式，详细路径于 `ramdisk/rootfs/`

### 5.3.3 Pre-build rootfs架构
文件系统之结构目录主要拆了三个类型，且逐层迭加于 Rootfs，将于下方分别描述:
- __Basic rootfs__:
现阶段本公司提供了基于以下四种 Arch 产生之 pre-build rootfs 档案

| Arch | Libc |	Pre-build ramdisk path |
|:--------| :---------|:--------|
| Arm | glibc |ramdisk/rootfs/common_arm/|
| Arm | uclibc |ramdisk/rootfs/common_uclibc/|
| Aarch64 | glibc |ramdisk/rootfs/common_arm64/|
| Riscv64| glibc |ramdisk/rootfs/common_riscv64/|
| Riscv64 | musl |ramdisk/rootfs/common_musl64/|
- __Processor configuration rootfs__:
本公司将所有 Processorset 相依之开机设置均放置于 ramdisk/rootfs/overlay/$CHIP
- __Third-party rootfs__:
本公司将所有第三方软件编译出来之 library、utility、related file 均放置于ramdisk/rootfs/public/

# 6. SDK开发网络安全
本节主要的目的在于从网络安全的角度针对这些网络安全威胁问题提供相应的解决方案。
## 6.1 u-boot 使用注意事项
### 6.1.1 串口
u-boot 串口功能默认是开启的。在 u-boot 的执行流程中，u-boot 会等待一秒的时间让研发人员可以在执行阶段通过敲击按键的方式中断 u-boot 执行过程以停留在 u-boot阶段进行调试。若过程中没有任何敲击按键的事件发生，一秒后则会继续 u-boot 的开机流程。在正式发布的产品，可以将此配置取消，以达到无法在 u-boot 阶段通过串口调试的目的，具体实现方法如下：
步骤 1. 开启 `build/boards/{processor_name}/{board_name}/u-boot/{board_name}_defconfig`
修改 CONFIG_BOOTDELAY 的配置值为`-2`。
```
CONFIG_IDENT_STRING="soph"
CONFIG_BOOTDELAY=-2
```
步骤 2. 重新编译 u-boot

### 6.1.2 u-boot 指令
u-boot 下提供许多研发人员进行开发与调试的指令, 例如：`md`, `mw`, `setenv`, `saveenv` 等。但这些指令在正式产品中并非是必须的。可以选择保留无关乎系统安全的指令，并将其他指令删除。
例如欲删除`md`/`mw` 指令，具体实现方式如下：
开启`/u-boot-2021.10/cmd/Makefile`, 因为`md`/`mw` 具体实现代码是在 `mem.c` 中，所以直接将下面示例中的 `obj-$(CONFIG_CMD_MEMORY) += mem.o` 注释掉或删除
```
obj-$(CONFIG_LOGBUFFER) += log.o
obj-$(CONFIG_ID_EEPROM) += mac.o
obj-$(CONFIG_CMD_MD5SUM) += md5sum.o
#obj-$(CONFIG_CMD_MEMORY) += mem.o
obj-$(CONFIG_CMD_IO) += io.o
obj-$(CONFIG_CMD_MFSL) += mfsl.o
```
或是修改 `/u-boot-2021.10/cmd/Kconfig`, 将 default 配置为`n`。
```
config CMD_MEMORY
  bool "md, mm, mw, cp, cmp, base, loop, ip_update"
  default n
  help
    Memory commands.
      md - memory display
      mm - memory modify (auto-incrementing address)
      mw - memory write (fill)
      cp - memory copy
      cmp - memory compare
      base - print or set address offset
      loop - initialize loop on address range
      ip_update - sync ip from mem 0x400038C/900 to uboot env
```
其他命令删除方法与上面的操作类似。

## 6.2 Linux 使用网络安全注意事项
### 6.2.1 root 帐户
在实际产品中，需要对 root 用户做安全性修改，用户可决定更改默认密码或是禁止 root 通过shell 登录。具体方法如下：
- 修改密码
步骤 1. 执行 shell 指令`passwd`更改密码。
步骤 2. 将`/etc/shadow` 拷贝出来（可通过挂载 SD 卡或是网络）
步骤 3. 将 `shadow` 文件拷贝至`/ramdisk/rootfs/overlay/{processor_name}/etc` 下。
步骤 4. 重新编译rootfs文件系统 (指令：`pack_rootfs`)，并将 `rootfs.spinor` 重新烧入进平台。

- 禁止 root 通过 shell 登录
步骤 1. 修改 SDK 包里的`/ramdisk/rootfs/overlay/{processor_name}/etc/passwd`，将内容`root:x:0:0:root:/root:/bin/sh`
修改成：
`root:x:0:0:root:/root:/bin/false`
步骤 2. 重新编译rootfs文件系统 (指令：`pack_rootfs`)，并將`rootfs.sd`重新烧入进平台。

### 6.2.2 文件权限
SG200x SDK 默认使用 SquashFS 文件系统，用户无法对预载的文件系统进行写或删除的动作，藉此来保护系统的稳定性。

## 6.3 Linux 驱动使用网络安全注意事项
### 6.3.1 串口
研发人员在 linux 中可通过串口来做调试，若要避免串口被非法接入的风险，确定串口在产品中不再使用，则在出厂时可以关闭串口。具体实现方法如下：
步骤 1. 开启 `build/boards/{processor_name}/{board_name}/dts_{arch}/{processor_name}/ {processor_name}.dtsi`, 修改如下示例的代码，
```
uart0: serial@04140000 {
compatible = "snps,dw-apb-uart";
reg = <0x0 0x04140000 0x0 0x1000>;
clock-frequency = <25000000>;
reg-shift = <2>;
reg-io-width = <4>;
- status = "okay";
+ status = "disabled";
};
```
步骤 2. 重新编译 linux

## 6.4 应用开发安全注意事项
### 6.4.1 Cipher 驱动
CIPHER是SG智能数字媒体处理平台提供的安全算法模块，提供对称式加解密算法包括AES/DES/SM4, 不对称加解密算法 RSA 随机数生成, 以及摘要算法包括 HASH, HMAC, 客户可用于对音视频码流进行加解密保护, 认证用户合法性等场景。
具体请参考[《CVITEK CIPHER API 参考》](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/CIPHER_API_Reference/build/CIPHERAPIReference_zh.pdf)。

## 6.5 其他安全注意事项
### 6.5.1 裸片烧写
CVITEK SDK 包提供 SD，USB 裸片烧写功能，建议在实际产品中将裸片烧写功能关闭。SD，USB 裸烧功能可以通过硬件上的设计进行关闭。

### 6.5.2 SD 卡/U 盘挂载权限
若开发的产品具备 SD card 或是 U 盘等可插拔储存设备接口时，建议挂载储存设备文件系统前加上”-o noexec”参数，以避免恶意第三方程序的运行进而造成系统的损坏。

### 6.5.3 JTAG
建议在实际产品上移除 JTAG 接口，以避免恶意窜改系统配置而造成系统损坏。

## 6.6 Alios 开发使用注意事项
参考 Alios 开源文档 https://github.com/alibaba/AliOS-Things/tree/master/documentation


# 7. 附录--文档资料
本章节提供芯片平台文档如Datasheet和TRM等，同时提供各类可能相关的学习资源。

## 7.1 芯片平台文档
### 7.1.1 Datasheet
- SG2000 [Datasheet](https://github.com/sophgo/sophgo-doc/releases/tag/sg2000-datasheet-v1.0-alpha)

- SG2002 [Datasheet](https://github.com/sophgo/sophgo-doc/releases/tag/sg2002-datasheet-v1.0-alpha)

### 7.1.2 Technical Reference Manual
- SG2000 [TRM](https://github.com/sophgo/sophgo-doc/releases/tag/sg2000-trm-v1.0-alpha)

- SG2002 [TRM](https://github.com/sophgo/sophgo-doc/releases/tag/sg2002-trm-v1.0-alpha)

同时我们也为SG200x TRM提供beta双语版本，将手册的 RST 源码进行开源，鼓励用户在使用过程中对手册的内容提 issue 或者 PR，使其更丰富完整。
- SG2000 [v1.0-beta双语版本](https://github.com/sophgo/sophgo-doc/releases/tag/sg2000-trm-v1.0-beta)

- SG2002 [v1.0-beta双语版本](https://github.com/sophgo/sophgo-doc/releases/tag/sg2002-trm-v1.0-beta)

### 7.1.3硬件开发指南
通用硬件开发文档目录下主要介绍芯片硬件板基本功能特点、硬件接口和使用方法等，旨在帮助相关开发人员更准确地使用该EVB。具体资料请详见[sophgo-github](https://github.com/sophgo/sophgo-hardware/tree/master/SG200X) /sophgo-hardware/SG200X/芯片名称/目录下的相关文档。
<table>
   <tr>
        <td>目录</td>
        <td>对应文档</td>
        <td>备注</td>
   </tr>
   <tr>
        <td>01_文档说明</td>
        <td>SG200x HDK说明</td>
        <td></td>
    </tr>
    <tr>
        <td rowspan="12">02_SG200X_Common_HW_DOC</td>
  		  <td>01_SOPHGO EMI问题常见分析思路与措施</td>
        <td></td>
    </tr>
    <tr>
        <td>02_SOPHGO 音频硬件、结构设计以及器件选用说明</td>
        <td></td>
    </tr>
    <tr>
        <td>03_SOPHGO关键元器件清单</td>
        <td></td>
    </tr>
    <tr>
        <td>04_硬件测试报告模板</td>
        <td></td>
    </tr>
    <tr>
        <td>05_SOPHGO PCBA贴片厂生产注意事项</td>
        <td></td>
    </tr>
    <tr>
        <td>06_SMT炉温曲线图</td>
        <td></td>
    </tr>
    <tr>
        <td>07_EMMC测试方法</td>
        <td></td>
    </tr>
    <tr>
        <td>08_SPINAND测试方法</td>
        <td></td>
    </tr>
    <tr>
        <td>09_SG200x_VO_VI 接口場景详细说明</td>
        <td></td>
    </tr>
    <tr>
        <td>10_SOPHGO_WiFi_支持列表</td>
        <td></td>
    </tr>
    <tr>
        <td>11_SOPHGO_Sensor_支持列表</td>
        <td></td>
    </tr>
    <tr>
        <td>12_SOPHGO_Flash_支持列表</td>
        <td></td>
    </tr>
    <tr>
        <td rowspan="11">03_SG2000</td>
  		  <td>01_SG2000_数据手册</td>
        <td></td>
    </tr>
    <tr>
        <td>02_SG2000_硬件设计指南</td>
        <td>硬件设计指南</td>
    </tr>
    <tr>
        <td>03_SG2000_BGA_EVB板硬件指南</td>
        <td>EVB板硬件设计指南</td>
    </tr>
    <tr>
        <td>04_SG2000_PINOUT</td>
        <td>PIN_OUT</td>
    </tr>
    <tr>
        <td>05_SG2000_BGA_GPIO清单</td>
        <td></td>
    </tr>
    <tr>
        <td>06_SOPHGO_Demo_SCH&PCB_4L</td>
        <td></td>
    </tr>
    <tr>
        <td>07_EVB&开发板 SCH&PCB位号图</td>
        <td></td>
    </tr>
    <tr>
        <td>08_SG2000_4L_6L_PCB_Layout指南</td>
        <td></td>
    </tr>
    <tr>
        <td>09_SG2000 BGA芯片阻抗测试参考表</td>
        <td></td>
    </tr>
    <tr>
        <td>10_SG2000_原理图symbol</td>
        <td></td>
    </tr>
    <tr>
        <td>11_SG2000_PCB封装</td>
        <td></td>
    </tr>
    <tr>
        <td rowspan="11">04_SG2002</td>
  		  <td>01_SG2002_数据手册</td>
        <td></td>
    </tr>
    <tr>
        <td>02_SG2002_硬件设计指南</td>
        <td>硬件设计指南</td>
    </tr>
    <tr>
        <td>03_SG2002_QFN_EVB板硬件指南</td>
        <td></td>
    </tr>
    <tr>
        <td>04_SG2002_PINOUT</td>
        <td></td>
    </tr>
    <tr>
        <td>05_SG2002_QFN_38板GPIO清单</td>
        <td></td>
    </tr>
    <tr>
        <td>06_SG2002_38板_2L_SCH&PCB</td>
        <td></td>
    </tr>
    <tr>
        <td>07_SG2002_38板_4L_SCH&PCB</td>
        <td></td>
    </tr>
    <tr>
        <td>08_SG2002_4L_PCB38x38mm2_Layout指南</td>
        <td></td>
    </tr>
    <tr>
        <td>09_SG2002_QFN88芯片阻抗测试参考表</td>
        <td></td>
    </tr>
    <tr>
        <td>10_SG2002_原理图symbol</td>
        <td></td>
    </tr>
    <tr>
        <td>11_SG2002_PCB封装</td>
        <td></td>
    </tr>
</table>

## 7.2 Linux开发文档
此文档主要介绍 Linux 开发环境。Linux 开发环境的搭建 U-boot、Linux 内核、根文件系统 (rootfs)以及内核和根文件系统的烧写，以及创建网络开发环境和启动 Linux 开发。
- [LINUX 开发环境用户指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Linux_Development_Environment_User_Guide/build/LinuxDevelopmentEnvironmentUserGuide_zh.pdf)

## 7.3 U-boot移植应用开发
SG200x列处理器在主板上 Bootloader 采用 U-boot-2021.10。当配置的不同外围处理器的(亦即开发版和公版上相异)，需要修改 U-boot 相关程序代码，主要包括缓存器 (registers), 系统配置档 (configuration) 和驱动程序 (drivers)。
- 其他操作细节请参考文档：[U-BOOT 移植应用开发指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/U-boot_Porting_Development_Guide/build/U-bootPortingDevelopmentGuide_zh.pdf)

## 7.4 IVE 软件开发
IVE(Intelligent Video Engine)是一种使用应减去加速电脑视觉算法的模块，用户利用IVE 开发智能分析方案可以加速智能分析的运算，降低 RISC-V 占用。当前 IVE 所提供的算子可以支撑开发影像或视频的智能分析方案。
- 具体操作细节请参考文档[IVE 软件开发指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/IVEAPI_Reference/build/IVEAPIReference_zh.pdf)

## 7.5 LDC 调试
LDC（镜头畸变校正系统）为实现校正和展宽功能，针对桶状畸变 (Barrel Distortion) 及枕型畸变(Pincushion Distortion) 的一帧图像做校正，能将此两类别变形的影像画面修正。
- 各应用场景的参数调试说明请参考文档[LDC 调试指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/LDC_Debugging_Guide/build/LDCDebuggingGuide_zh.pdf)

## 7.6 MIPI使用
MIPI Rx 可接收差分与 DC(TTL) 接口数据, 并将数据转换成 pixel 数据后传给下一级的 ISP
模块。差分讯号支持 SubLVDS(Sub Low-Voltage Differential Signal), MIPI-CSI 与 HiSPi(High Speed Serial Pixel Interface) 等视频输入。DC 讯号支持 Sensor RAW12, BT1120, BT656 与BT601。
- 更多功能描述和使用说明请参考文档[MIPI使用指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/MIPI_User_Guide/build/MIPIUserGuide_zh.pdf)

## 7.7 AliOS Sensor调试
此文档将介绍关于Sensor驱动、处理器规格、图像输出调试等资讯。
- [AliOS Sensor调试指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Sensor_Debugging_Guide/build/AliOS_Sensor_Debugging_Guide_zh.pdf)

## 7.8 开机画面
此文档将说明如何在uboot及AliOS下，显示出开机画面。
- [开机画面使用指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Startup_Screen_User_Guide/build/StartupScreenUserGuide_zh.pdf)

## 7.9 MMF媒体软件开发
MMF是多媒体软件架构（Multimedia Framework）的简称，用以缩短应用程序开发所需的时间，包含了以下功能：ISP影像前处理（包含HDR、去噪、边缘锐化等）、输入影像截取及输出、图像几何校正、H.265/H.264/JPEG 编解码、音频撷取及输出、音频编解码等。各功能的具体使用说明，请参考文档。
- [MMF媒体软件开发指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Media_Processing_Software_Development_Reference/build/MediaProcessingSoftwareDevelopmentReference_zh.pdf)

## 7.10 屏幕对接
此文档将详细说明MIPI DSI和LVDS两种屏幕在处理器上的配置和调试。
- [屏幕对接使用指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Screen_Docking_Guide/build/ScreenDockingGuide_zh.pdf)。

## 7.11 处理器码率控制
此文档将介绍码率控制参数、GOP结构参数意义和使用方法，同时将对码率控制的各项专题进行说明。
- [处理器码率控制使用说明](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Bit_Rate_Control_Application_Notes/build/BitRateControlApplicationNotes_zh.pdf)

## 7.12 智能编码
此文档将对GOP的结构和使用场景，编码器输入、输出讯息进行说明。
- [智能编码使用指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Smart_Coding_User_Guide/build/SmartCodingUserGuide_zh.pdf)


## 7.13 音频质量调试
此文档将对VQE（语音音质增强模块）算法及模块内各功能做详细介绍，并重点说明线性回声消除（AEC）的调试步骤。
- [音频质量调试指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Audio_Quality_Tuning_Guide/build/AudioQualityTuningGuide_zh.pdf)


## 7.14 eFuse
处理器内部集成eFuse空间，可供安全启动和和 448 bits 的用户自定义区域。此文档内介绍具体的eFuse分区、安全启动eFuse的设置流程等。
- [eFuse 使用指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/eFuse_User_Guide/build/eFuseUserGuide_zh.pdf)

## 7.15 Flash分区工具
此文档主要介绍不同版本SDK（SPINOR / SPINAND / EMMC）应该如何对Flash进行分区规划。
- [Flash 分区工具使用指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Cvitek_Flash_Partition_Tool_User_Guide/build/CvitekFlashPartitionToolUserGuide_zh.pdf)

## 7.16 SPI NAND烧录器
此文档对使用SPI NAND文件的烧写进行了说明。
- [SPI NAND 烧录器预烧手册](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/SPI_NAND_Programmer_Burn-in_User_Guide/build/SPINANDProgrammerBurn-inUserGuide_zh.pdf)

## 7.17 Wi-Fi使用
Linux平台上对于不同WiFi处理器的驱动与操作方式有通用性，此文档将分别介绍在不同接口上（如USB或是SDIO）如何使用Realtek解决方案进行驱动移植与调试，及相关的操作。
- [Wi-Fi使用指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Wi-Fi_User_Guide/build/Wi-FiUserGuide_zh.pdf)

## 7.18 安全启动
此文档对如何生成安全惊醒以及安全启动处理器进行了说明。
- [安全启动使用指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Secure_Boot_User_Guide/build/SecureBootUserGuide_zh.pdf)

## 7.19 外围设备驱动
此文档对Ethernet、USB、SD/MMC卡、GPIO、UART、Watchdog、PWM、ADC等外设分别进行了操作说明。
- 具体请参考文档[外围设备驱动操作指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Peripheral_Driver/build/PeripheralDriver_zh.pdf)

## 7.20 RTC
RTC(Real time clock)是硬件时钟，用于给系列提供并记录时间。Linux 内核将 RTC 作为时间与日期维护器，当 Linux 系统启动时，内核读取 RTC 时间以初始化系统（软件）时钟达成时间同步。
- 具体的操作及命令请参考文档[RTC 操作指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/RTC_Application_Guide/build/RTCApplicationGuide_zh.pdf)

## 7.21 ISP开发
此文档主要介绍ISP的用户接口，将从系统控制、3A、ISP模块三个部分进行说明。
- 请参考文档[ISP 开发参考](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/ISP/ISP_Development_Reference/build/ISPDevelopmentReference_zh.pdf)

## 7.22 ISP图像调优
此文档是为引导用户进行图像调优进行的说明，内容包含基本概念和步骤，可结合下方【图像质量调试工具使用指南】配合参考。
- [图像调优指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/ISP/ISP_Tuning_Guide/build/ISPTuningGuide_zh.pdf)

## 7.23 图像质量调试
CviPQ Tool是专业的图像质量调试工具，提供用户可在线调试ISP各模块的参数调节，并能实时观看参数设置效果；同时提供ISP标定功能，对需要标定的模块产生各类数据，提供给客户调节参数，以获得更佳图像质量。此文档是对CviPQ Tool进行的详细使用说明。
- [图像质量调试工具使用指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/ISP/PQ_Tools_User_Guide/build/PQToolsUserGuide_zh.pdf)

## 7.24 量产烧写
此文档介绍如何使用 cviDownloadTool 工具烧录整个单板系统文件，该方案通过 USB 通信来完成烧录，具有成本低，烧录速度快等特点。
- [量产烧写使用指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/BSP/Production_Burning_User_Guide/build/ProductionBurningUserGuide_zh.pdf)


# 8. 附录--工具下载
## 8.1 MIPI 屏幕时钟时序计算器
[请点击此链接下载–MIPI 屏幕时钟时序计算器](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Clock_Timing_Calculator_for_MIPI_Panels/build/MIPI_Time_Calculator.csv)

## 8.2 CviPQ Tool
[请点击此链接下载 – CviPQ Tool](https://github.com/jzlynn/sg-accessories/blob/master/CAM-GC2083/Software/CviPQtool_20230306.zip)

## 8.3 CviDownload Tool
[请点击此链接下载 – CviDownload Tool](https://github.com/jzlynn/sg-accessories/blob/master/CAM-GC2083/Software/cviDownloadTool.zip)
