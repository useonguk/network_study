from socket import *

s_ip = 'localhost'
s_port = 9999

s_sock = socket(AF_INET,SOCK_STREAM)
s_sock.setsockopt(SOL_SOCKET,SO_REUSEADDR)

s_sock.bind(s_ip,s_port)
s_sock.listen(2)
client,c_addr = s_sock.accept()
print(c_addr,'Now connected')

data = 'dummy'
while(len(data)):
    data = client.recv(1024).decode('UTF-8')

    if( data == 'q'):
        print("\n 수신완료")
        break

    print('수신된 자료 : ', data)
    client.send(data.encode('UTF-8'))

client.close()
s_sock.close()
