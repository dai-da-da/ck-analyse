#这是一个扫描指定 ip 端口的 py 脚本
#一切后果与本人无关，仅供学习使用

#引入标准库
import socket as sk
import threading as th
import time as t

ip="10.5.255.254"
# ip="10.5.131.118"
porks=[1,65535]

#创建连接器


def check_pork(pork):
    try:
        links=sk.socket()
        links.connect((ip,pork))
        print(str(pork)+":have")
        links.send("GET".encode("UTF-8"))
        # 接收服务端的消息
        recv_data = links.recv(1024).decode("UTF-8")
        print(str(pork)+f"服务端回复的消息是：{recv_data}")
    except:
        # print(str(pork)+":NULL",end='  ')
        pass
    
    links.close()
    if pork%100==0:
        print("")

for pork in range(porks[0],porks[1]):
    checks=th.Thread(target=check_pork,args=(pork,))
    checks.start()
    t.sleep(0.001)