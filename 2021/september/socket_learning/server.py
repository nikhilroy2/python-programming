import socket
IP = '172.23.176.14'
PORT = 40000
max_msg_size = 1024
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((IP,PORT))
soc.listen(5)
client, addr = soc.accept()
print('server online')

while True:
    sending_msg = input()
    encoded_msg = sending_msg.encode('utf-8')
    client.send(encoded_msg)
    if encoded_msg == 'Quit':
        break
    else:
        received_msg = client.recv(max_msg_size)
        decoded_msg = received_msg.decode('utf-8')
        print('\t\t@client: {decoded_msg}')

        if decoded_msg == 'Quit':
            break
soc.close()

