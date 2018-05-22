from socket import *
import threading


def recv_thread(clint_socket):
    while True:
        msg_recv = clint_socket.recv(1024).decode('utf-8')
        print('收到来自服务端的消息%s' %msg_recv)

def main():

    clint_socket = socket(AF_INET,SOCK_STREAM)
    clint_socket.connect(('127.0.0.1',8848))
    recv_thread_ = threading.Thread(target=recv_thread,args=(clint_socket,))
    recv_thread_.start()
    while True:
        msg_send = input('请输入要发送的信息:')
        clint_socket.send(msg_send.encode('utf-8'))



if __name__ == '__main__':
    main()
