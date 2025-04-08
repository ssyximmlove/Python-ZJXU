import socket
import sys

# 服务端主机 IP 地址和端口号
HOST = '127.0.0.1'
PORT = 50007  # 与服务端端口保持一致
# 修正 socket 模块的参数分隔符
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # 连接服务器
    s.connect((HOST, PORT))
except Exception as e:
    print('Server not found or not open')
    sys.exit()

while True:
    c = input('Input the content you want to send:')
    # 发送数据
    s.sendall(c.encode())
    # 从服务端接收数据
    data = s.recv(1024)
    data = data.decode()
    print(f'Received: {data}')
    if c.lower() == 'bye':
        break

# 关闭连接
s.close()
