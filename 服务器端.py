import socket    # 导入socket库

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # 调用socket中的socket（）函数来创建一个socket s；with（）代表党代码离开with块时自动调用s.close()来销毁这个socket
    '''
    socket.AF_INET:代表使用的是IPV4的地址家族
    socket.SOCK_STREAM：代表使用的是TCP协议
    '''
    s.bind(('0.0.0.0',1234))    # 关联到主机的某一个网口和端口上；'0.0.0.0'可以通过IP地址指定，此处'0.0.0.0'这个特殊地址代表主机上的任意网口都可以使用这个socket进行通信
    s.listen()    # listen()将socket置为监听状态，并等待客户端的连接
    c, addr = s.accept()    # accept()接受来自任意客户端的连接，并返回一个新的socket c（socket s用于监听，socket c用于与连接的客户端进行通信）
    with c:
        print(addr,'connected.')    # 打印客户端地址

        while True:    # 该循环会一直调用recv()接收客户端传来的信息
            data = c.recv(1024)    # 1024代表一次性接收数据的最大长度为1024个字节
            if not data:
                break
            c.sendall(data)    # 只要数据不为空，就原封不动的将数据回传给客户端