import socket
import tqdm
import os

# 设置服务器的IP和端口
SERVER_HOST = "172.20.47.169"    # 服务器iP地址
SERVER_PORT = 1234    # 服务器端口号

# 设置文件读写的缓冲区大小,此处设置为16KB
BUFFER_SIZE = 16384
# 传输数据分隔符
SEPARATOR = "<SEPARATOR>"

# 创建的Server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # 调用socket中的socket（）函数来创建一个socket s；with（）代表党代码离开with块时自动调用s.close()来销毁这个socket
    '''
    socket.AF_INET:代表使用的是IPV4的地址家族
    socket.SOCK_STREAM：代表使用的是TCP协议
    '''
    s.bind((SERVER_HOST, SERVER_PORT))    # 关联到主机的某一个网口和端口上；'0.0.0.0'可以通过IP地址指定，此处'0.0.0.0'这个特殊地址代表主机上的任意网口都可以使用这个socket进行通信
    s.listen(5)    # listen()将socket置为监听状态，并等待客户端的连接
    print(f"服气器端监听{SERVER_HOST}:{SERVER_PORT}")
    # 接收客户端连接
    client_socket, address = s.accept()    # accept()接受来自任意客户端的连接，并返回一个新的socket c（socket s用于监听，socket c用于与连接的客户端进行通信）
    # 接受客户端信息
    with client_socket:
        print(f"客户端{address}连接")    # 打印客户端的IP
        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, file_size = received.split(SEPARATOR)
        filename = os.path.basename(filename)  # 获取文件名，剔除路径信息
        file_size = int(file_size)
        # 文件接收处理
        progress = tqdm.tqdm(range(file_size), f"接收{filename}", unit="B", unit_divisor=1024, unit_scale=True)
        with open(filename, "wb") as f:
            for _ in progress:
                # 从客户端读取数据
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not received:
                    break
                # 读取写入
                f.write(bytes_read)
                    # 更新进度条
                progress.update(len(bytes_read))
