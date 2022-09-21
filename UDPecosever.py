from socket import *

s_ip = 'localhost'
s_port = 9999
s_addr = (s_ip, s_port)

s_sock = socket(AF_INET,SOCK_DGRAM)
s_sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s_sock.bind(s_addr)
data, s_addr = s_sock.recvfrom(1024)

while True:
    if data.decode('UTF-8') == 'q' : 
        break
    print('Received from', s_addr)
    print('Obtained', data.decode('UTF-8'))
    print()
    s_sock.sendto(data, s_addr)
    data, s_addr = s_sock.recvfrom(1024)