def get_reply_by_keyword(keyword):
    """根据关键词获取回复内容"""
    # 这里可以实现自己的关键词匹配逻辑
    if keyword == '你好':
        return '你好!欢迎关注!'
    elif keyword == '帮助':
        return '这是自动回复系统,请输入关键词获取回复。'
    else:
        return '抱歉,我还不知道怎么回答这个问题。' 