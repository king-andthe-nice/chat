# 微信公众号自动回复功能

这是一个基于Python的微信公众号自动回复系统，支持关键词自动回复功能。

## 功能特点
- 支持文本消息自动回复
- 关键词精确匹配
- 默认回复功能
- 灵活的配置系统

## 项目结构
```
.
├── README.md
├── requirements.txt
├── config.py          # 配置文件
├── main.py           # 主程序入口
├── reply_rules.py    # 回复规则配置
└── utils/            # 工具函数
    └── token.py      # access_token管理
```

## 使用方法
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 配置config.py：
   - 填入公众号的AppID和AppSecret
   - 配置服务器URL和Token

3. 配置回复规则：
   在reply_rules.py中配置关键词和对应的回复内容

4. 运行服务：
   ```bash
   python main.py
   ```

## 配置说明
在config.py中需要配置以下信息：
- APP_ID：微信公众号的AppID
- APP_SECRET：微信公众号的AppSecret
- TOKEN：用于验证消息的Token
- SERVER_HOST：服务器地址
- SERVER_PORT：服务器端口

## 注意事项
1. 请确保服务器有公网IP或域名
2. 需要在微信公众平台配置服务器地址
3. 建议使用HTTPS协议以提高安全性 