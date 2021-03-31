import socket

ADDR = input("Enter IP Address: ")
PORT = input("Enter Port: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDR, int(PORT)))
s.sendall(b'hacked')
data = s.recv(1024)

print('Recieved', repr(data))
