import socket
import threading

def thread_hello(new_sock):
    while True:
        recv_data_1 = new_sock.recv(1024)
        recv_data = recv_data_1.decode('utf-8')
        print("接收到的消息:", recv_data)
        if recv_data:
            print("接收到的客户端信息:", recv_data)
            new_sock.send(recv_data.encode('utf-8'))
        else:
            print("客户端已经下线...")
            break
    new_sock.close()
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(5)

    while True:
        new_sock, client_addr = server_socket.accept()
        print("有新的客户端请求，来自", client_addr)
        t1 = threading.Thread(target=thread_hello,args=(new_sock,))
        t1.start()

if __name__ == '__main__':
    main()
