from socket import *

s_ip = 'locallhost'
s_port = 54321

s_sock=socket(AF_INET, SOCK_STREAM)
s_sock.bind((s_ip, s_port))
s_sock.listen(2)

client, c_addr = s_sock.accept()
print(c_addr, 'is connected')

data1 = 'Thank u for connecting'
client.send(data1.encode('utf-8'))
data2 = 'Received data from client : '
print(data2, client.recv(1024).decode('utf-8'))

client.close()
s_sock.close()
