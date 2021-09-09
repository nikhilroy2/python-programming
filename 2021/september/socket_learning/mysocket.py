import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind('172.23.176.14', 40000)
soc.listen(5)
clientsocket, clientaddress = soc.accept()

message = "Hello World"

encoded_msg = message.encode('utf-8')

clientsocket.send(encoded_msg)