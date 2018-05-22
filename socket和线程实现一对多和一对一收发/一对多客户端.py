import socket


def main():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ('127.0.0.1', 8888)  # 元组类型
    tcp_client_socket.connect(server_addr)
    while True:
        send_data = input("请输入要发送的数据:")
        tcp_client_socket.send(send_data.encode('utf-8'))
        recv_data = tcp_client_socket.recv(1024)
        s_data = recv_data.decode('utf-8')
        print("接收到的数据:", s_data)
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
