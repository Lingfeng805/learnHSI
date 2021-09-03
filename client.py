import socket
import tqdm    # 进度条库
import os    # 文件名、文件路径

# 传输数据分隔符
SEPARATOR = "<SEPARATOR>"
# 服务器信息
host = "172.20.47.169"    # 主机iP地址
port = 1234    # 1~1024基本已被系统占用

# 设置文件传输的缓冲区，保证传输效率,此处设置为16KB
BUFFER_SIZE = 16384

# 传输的文件名
filename = "C:/Users/user/Desktop/测试文件夹/20210902.pdf"
# 文件大小
file_size = os.path.getsize(filename)

# 创建socket连接
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"服务器连接中{host}:{port}")
    s.connect((host, port))    # 连接服务器
    print("与服务器连接成功！")
    # 发送文件名与文件大小，必须进行编码处理encode（）
    s.send(f"{filename}{SEPARATOR}{file_size}".encode())
    # 文件传输
    progress = tqdm.tqdm(range(file_size), f"发送{filename}", unit="B", unit_divisor=1024)
    with open(filename,"rb") as f:
        for _ in progress:
            # 读取文件
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            # sendall()确保即使网络忙碌时，数据仍然可以传输，即保证数据传输完
            s.sendall(bytes_read)
            progress.update(len(bytes_read))