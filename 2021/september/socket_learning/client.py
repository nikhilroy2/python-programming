import socket
IP = '172.23.176.14'
PORT = 40000
max_msg_size = 1024


max_msg_size = max_msg_size

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((IP, PORT))

print('client online')

while True:
    received_msg = sock.recv(max_msg_size)
    decoded_msg = received_msg.decode('utf-8')
    print(f'\t\t @server: {decoded_msg}')
    if decoded_msg == 'Quit':
        break
    else:
        sending_msg = input()
        encoded_msg = sending_msg.encode('utf-8')
        sock.send(encoded_msg)
        if encoded_msg == 'Quit':
            break
sock.close()


