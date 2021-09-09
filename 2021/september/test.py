import socket
#soc = socket.socket(socket_family, socket_type)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('172.20.163.203', 40000))
#172.20.163.203
soc.listen(5)

clientsocket, clientaddress = soc.accept()
message = "Hello Nikhil Sir" 
encoded_msg = message.encode('utf-8')
clientsocket.send(encoded_msg)
