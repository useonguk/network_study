from socket import *

s_ip = 'localhost'
s_port = 54321
s_addr = (s_ip,s_port)

c_sock = socket(AF_INET, SOCK_DGRAM)

data = '안녕, 서버야~~!'
c_sock.sendto(data.encode('UTF-8'), s_addr)

c_sock.close()