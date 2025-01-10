import hashlib
import xmltodict
import time
from flask import Flask, request, make_response

app = Flask(__name__)

# 直接在代码中设置TOKEN，因为Vercel环境变量设置方式不同
TOKEN = "king210"

def check_signature(signature, timestamp, nonce):
    """验证消息真实性"""
    if not signature or not timestamp or not nonce:
        print("Missing required parameters")
        return False
        
    print(f"Received validation request:")
    print(f"signature: {signature}")
    print(f"timestamp: {timestamp}")
    print(f"nonce: {nonce}")
    print(f"token: {TOKEN}")
    
    # 按照微信的规则进行签名验证
    tmp_list = [TOKEN, timestamp, nonce]
    tmp_list.sort()
    tmp_str = ''.join(tmp_list)
    print(f"String to hash: {tmp_str}")
    
    hash_obj = hashlib.sha1()
    hash_obj.update(tmp_str.encode('utf-8'))
    calculated_signature = hash_obj.hexdigest()
    print(f"Calculated signature: {calculated_signature}")
    print(f"Received signature: {signature}")
    
    if calculated_signature == signature:
        print("Signature verification successful")
        return True
    print("Signature verification failed")
    return False

def get_reply_by_keyword(keyword):
    """根据关键词获取回复内容"""
    if keyword == '你好':
        return '你好!欢迎关注!'
    elif keyword == '帮助':
        return '这是自动回复系统,请输入关键词获取回复。'
    else:
        return '抱歉,我还不知道怎么回答这个问题。'

@app.route('/', methods=['GET', 'POST'])
def wechat():
    print(f"\nReceived {request.method} request")
    print(f"Request args: {request.args}")
    
    # 微信服务器进行URL验证时使用GET请求
    if request.method == 'GET':
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        
        if not all([signature, timestamp, nonce, echostr]):
            print("Missing required parameters in GET request")
            return 'Missing parameters'
            
        if check_signature(signature, timestamp, nonce):
            print(f"Returning echostr: {echostr}")
            return echostr
        return 'Invalid signature'
    
    # 处理微信服务器发来的消息
    elif request.method == 'POST':
        try:
            # 解析XML消息
            xml_data = request.data
            msg = xmltodict.parse(xml_data)['xml']
            
            # 提取消息信息
            msg_type = msg.get('MsgType')
            from_user = msg.get('FromUserName')
            to_user = msg.get('ToUserName')
            
            # 只处理文本消息
            if msg_type == 'text':
                content = msg.get('Content', '').strip()
                # 获取回复内容
                reply_content = get_reply_by_keyword(content)
                
                # 构造回复消息
                reply_msg = f"""
                <xml>
                <ToUserName><![CDATA[{from_user}]]></ToUserName>
                <FromUserName><![CDATA[{to_user}]]></FromUserName>
                <CreateTime>{int(time.time())}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{reply_content}]]></Content>
                </xml>
                """
                response = make_response(reply_msg)
                response.content_type = 'application/xml'
                return response
            
            # 其他类型消息返回默认回复
            return make_response('success')
            
        except Exception as e:
            print(f"Error processing message: {str(e)}")
            return make_response('success')

# Vercel需要这个
app.debug = True 