import socket
from os.path import commonprefix

# 服务端主机 IP 地址和端口号
HOST = '127.0.0.1'
PORT = 50007  # 服务端端口号

words = {
    'how are you?': 'Fine, thank you.',
    'how old are you?': '38',
    'what is your name?': 'Zhang Shan',
    "what's your name?": 'Zhang Shan',
    'where do you work?': 'University',
    'bye': 'Bye'
}

# 创建 UDP 套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定地址和端口
s.bind((HOST, PORT))
print(f"Server is running on {HOST}:{PORT}")

while True:
    data, addr = s.recvfrom(1024)

    if not data:
        break

    print(f'Received message: {data}')
    # 尽量猜测对方要表达的真正意思
    m = 0
    key = ''
    data = data.decode()
    for k in words.keys():
        # 删除多余的空白字符
        message = ''.join(data.split())
        # 与某个“键”非常接近，就直接返回
        if len(commonprefix([k.replace(" ", ""), message])) > len(k.replace(" ", "")) * 0.7:
            key = k
            break
        # 使用选择法，选择一个重合度较高的“键”
        length = len(set(data.split()) & set(k.split()))
        if length > m:
            m = length
            key = k
    # 选择合适的信息进行回复
    s.sendto(words.get(key, 'Sorry.').encode(), addr)

    if key == 'bye':
        s.sendto("Bye".encode(), addr)
        break

s.close()
