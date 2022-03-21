'''
Author: Hansson Li
Date: 2022-03-21 10:39:16
LastEditTime: 2022-03-21 10:41:29
LastEditors: Hansson Li
Description: use to test wechat api interface

'''

import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
    
itchat.auto_login()
itchat.run()
