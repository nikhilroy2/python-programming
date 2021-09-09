import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('172.20.163.203', 40000))
received_msg = sock.recv(1024)



received_msg.decode('utf-8')
print(received_msg)