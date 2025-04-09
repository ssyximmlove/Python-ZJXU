import socket

# 服务端主机 IP 地址和端口号
HOST = '127.0.0.1'
PORT = 50007  # 与服务端端口保持一致

# 创建 UDP 套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 输入要发送的内容
    message = input("Input the content you want to send: ")
    # 发送数据
    s.sendto(message.encode(), (HOST, PORT))

    # 接收服务端的回复
    data, addr = s.recvfrom(1024)
    print(f"Received: {data.decode()}")

    # 如果输入 "bye"，退出
    if message.lower() == 'bye':
        break

# 关闭套接字
s.close()
