import os
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

# 微信公众号配置
APP_ID = os.getenv('APP_ID', '')  # 你的AppID
APP_SECRET = os.getenv('APP_SECRET', '')  # 你的AppSecret
TOKEN = os.getenv('TOKEN', 'your_token')  # 你的Token

# 服务器配置
SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
SERVER_PORT = int(os.getenv('SERVER_PORT', '5000')) 