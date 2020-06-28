import itchat
import time

def lc():
    print("Finish Login")
def ec():
    print("exit")

itchat.auto_login(hotReload=True,loginCallback=lc, exitCallback=ec)  #扫码登录
#time.sleep()
#itchat.logout()    #强制退出登录
#users=itchat.search_friends("赵宇灏")
#userName= users[0]['UserName']
users=itchat.search_chatrooms(name='测试')
userName= users[0]['UserName']

print(userName)
for i in range(5):  
    itchat.send(msg=str(i),toUserName=userName)
#check=itchat.check_login()
#print(check)

