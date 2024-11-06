#这是一个扫描指定 ip 端口的 py 脚本
#一切后果与本人无关，仅供学习使用

#引入标准库
import socket as sk

ip="10.5.255.254"
porks=[1,65535]

#创建连接器
links=sk.socket()

for pork in range(porks[0],porks[1]):
    try:
        links.connect((ip,pork))
        links.send("cs".encode("UTF-8"))
        # 接收服务端的消息
        recv_data = links.recv(1024).decode("UTF-8")    # 1024是缓冲区大小，一般就填1024， recv是阻塞式
        print(f"服务端回复的消息是：{recv_data}")
        links.close()
    except:
        print("error")
        pass

