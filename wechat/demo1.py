import itchat
import threading
from time import sleep

# itchat.auto_login(hotReload=True)
# itchat.send('Hello, filehelper', toUserName='filehelper')

# import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return 'hello ' + msg.text

def send_msg(itchat):
    author = itchat.search_friends(nickName='KeBt')[0]
    while True:
        sleep(1)
        author.send('去打球')


itchat.auto_login()
thread = threading.Thread(target = send_msg,args=(itchat,))
thread.daemon = True
thread.start()
itchat.run()