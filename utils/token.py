import os
import json
import time
import requests
from config import APP_ID, APP_SECRET, ACCESS_TOKEN_FILE

class AccessToken:
    def __init__(self):
        self.access_token = None
        self.expires_time = 0
        self.load_token()

    def load_token(self):
        """从文件加载token"""
        if os.path.exists(ACCESS_TOKEN_FILE):
            try:
                with open(ACCESS_TOKEN_FILE, 'r') as f:
                    data = json.load(f)
                    self.access_token = data.get('access_token')
                    self.expires_time = data.get('expires_time', 0)
            except:
                pass

    def save_token(self):
        """保存token到文件"""
        with open(ACCESS_TOKEN_FILE, 'w') as f:
            json.dump({
                'access_token': self.access_token,
                'expires_time': self.expires_time
            }, f)

    def get_token(self):
        """获取有效的access_token"""
        now = time.time()
        if not self.access_token or now >= self.expires_time:
            self.refresh_token()
        return self.access_token

    def refresh_token(self):
        """刷新access_token"""
        url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}'
        try:
            response = requests.get(url)
            result = response.json()
            if 'access_token' in result:
                self.access_token = result['access_token']
                self.expires_time = time.time() + result['expires_in'] - 300  # 提前5分钟过期
                self.save_token()
            else:
                raise Exception(f"获取access_token失败：{result.get('errmsg')}")
        except Exception as e:
            raise Exception(f"刷新access_token失败：{str(e)}")

# 创建全局AccessToken实例
token_manager = AccessToken() 