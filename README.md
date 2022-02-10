# SynthesizerV-arm64
ARM平台下 Synth V 加载器，适配CPU：鲲鹏、飞腾

#依赖环境：
Exagear 64位版本：
安装说明：

步骤1：下载安装包：https://mirrors.huaweicloud.com/kunpeng/archive/ExaGear/ExaGear_1.2.1.1.tar.gz

步骤2：解压后进入ExaGear_1.2.1.1目录

步骤3：执行安装命令 sudo apt install ./*.deb

步骤4（鲲鹏平台不需要执行）：复制exagear_hk目录下的文件到/opt/exagear/bin目录下，并替换原文件

安装教程来源：https://www.hu60.cn/q.php/bbs.topic.102147.html

#部署方法：
（1）SynthV Basic版本:
     直接Clone就可以了

（2）SynthV Pro版本：
     下载Linux版本安装文件的zip，并解压到SynthesizerV目录下

#运行方法
执行boot.py即可

#运行框架介绍
通过Exagear模拟X64环境，然后运行SynthV。依赖库已经提取到lib-ext目录并做好了相应调整。
