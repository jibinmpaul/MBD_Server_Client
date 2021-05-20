import socket
s = socket.socket()
port = 12345
s.connect(('127.0.0.1',port))

message = input("-> ")
while True:    
    if message == 'exit':
        break;
    else:
        s.send(message.encode())
    message = input("-> ")
s.close()
