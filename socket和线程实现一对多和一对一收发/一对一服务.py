import socket
import threading

def recv_thread(new_socket,addr):
    while True:
        recv_msg = new_socket.recv(1024).decode('utf-8')
        print('收到来自%s的信息：%s' %(addr,recv_msg))
def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1',8848))
    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    while True:
        new_socket,addr = server_socket.accept()
        recv_thread_ = threading.Thread(target=recv_thread,args=(new_socket,addr,))
        recv_thread_.start()
        while True:
            send_msg = input('请输入要发送的信息')
            new_socket.send(send_msg.encode('utf-8'))


        # send_thread_ = threading.Thread(target=send_thread, args=(new_socket,))
        # send_thread_.start()

if __name__ == '__main__':
    main()