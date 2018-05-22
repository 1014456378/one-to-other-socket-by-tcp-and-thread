import socket
import threading


def content_thread(new_socket,addr):
    print('\n与%s建立链接\n' %(addr,))
    while True:
        recv_msg = new_socket.recv(1024).decode('utf-8')
        print('\n收到来自%s的信息：%s\n' %(addr,recv_msg))
def send_thread(addr_info):
    while True:
        send_ip = input('\n请输入要发送的地址\n')
        send_msg = input('\n请输入要发送的信息\n')
        addr_info[send_ip].send(send_msg.encode('utf-8'))

def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1',8847))
    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    addr_info = {}
    while True:
        new_socket,addr = server_socket.accept()
        addr_info[addr[0]+':'+str(addr[1])] = new_socket
        content_thread_ = threading.Thread(target=content_thread,args=(new_socket,addr))
        send_thread_ = threading.Thread(target=send_thread,args=(addr_info,))
        content_thread_.start()
        send_thread_.start()




if __name__ == '__main__':
    main()