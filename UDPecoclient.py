from socket import *

s_ip = 'localhost'
s_port = 9999
s_addr = (s_ip, s_port)

c_sock = socket(AF_INET,SOCK_DGRAM)

indata = input('전송할 문자열 입력 : ')

c_sock.sendto(indata.encode('UTF-8'), s_addr)

while True:
    if(indata == 'q'):
        break
    data, addr = c_sock.recvfrom(1024)
    print('ecodata : ',data.decode('UTF-8'))
    indata = input('Enter string : ')
    c_sock.sendto(indata.encode('UTF-8'), s_addr)

c_sock.close()