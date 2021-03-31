import socket

ip = input('Enter IP to port scan: ')
ports = input('Enter port range to scan (ex 1-1000): ')

lowport = int(ports.split('-')[0])
highport = int(ports.split('-')[1])

print('Scanning IP ', ip, 'from port',lowport, 'to port', highport)

for port in range(lowport, highport):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   status = s.connect_ex((ip, port))
   if(status == 0):
        print('*** Port',port,'- OPEN ***')
   else:
        print('Port',port,'- CLOSED ***')
s.close()
