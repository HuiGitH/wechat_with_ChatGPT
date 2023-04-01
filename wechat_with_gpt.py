# -*- coding: utf-8 -*-

import itchat
import requests

from gpt_chat import chat_gpt_reply


@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def text_reply(msg):
    if msg.User.RemarkName in ['张海']:
        receive_username = msg.User.RemarkName
        receive_meg = msg.text
        print("收到'{}',发来的:'{}';".format(receive_username, receive_meg))
        while True:
            try:
                reply_meg = chat_gpt_reply(receive_meg)
                break
            except requests.exceptions.ProxyError as e:
                print(e)
                reply_meg = receive_meg
                continue
        print("回复{}:{}".format(receive_username, reply_meg))
        return reply_meg


# hotReload=True
itchat.auto_login(hotReload=True)

itchat.run()
