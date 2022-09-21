from socket import *

s_ip = 'localhost'
s_port = 9999

c_sock = socket(AF_INET,SOCK_STREAM)

c_sock.connect( (s_ip, s_port) )

while (True):
    indata = input('전송할 문자 입력 :')
    c_sock.send(indata.encode('UTF-8'))
    print(c_sock.recv(1024).decode('UTF-8'))

    if(indata == 'q'):
        print('송신 종료')
        break

c_sock.close()