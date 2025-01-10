#!/bin/bash

# 创建部署包
tar -czf wechat-app.tar.gz \
    main.py \
    config.py \
    requirements.txt \
    reply_rules.py \
    .env \
    deploy_server.sh

# 上传到服务器
scp wechat-app.tar.gz root@142.4.124.236:/root/

echo "文件已上传到服务器，请执行以下命令完成部署："
echo "1. ssh root@142.4.124.236"
echo "2. cd /root"
echo "3. tar -xzf wechat-app.tar.gz"
echo "4. bash deploy_server.sh" 