#!/bin/bash

# 创建项目目录
mkdir -p /opt/wechat-app
cd /opt/wechat-app

# 安装Python虚拟环境
apt-get update
apt-get install -y python3-venv python3-pip

# 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 启动服务（使用nohup在后台运行）
nohup python main.py > app.log 2>&1 &

# 输出日志位置
echo "应用已启动，日志文件位置：/opt/wechat-app/app.log" 