#!/bin/bash

# 安装Docker（如果没有）
sudo apt-get update
sudo apt-get install -y docker.io docker-compose

# 创建应用目录
sudo mkdir -p /opt/wechat-app
cd /opt/wechat-app

# 复制配置文件
sudo cp docker-compose.yml .env ./

# 启动服务
sudo docker-compose up -d