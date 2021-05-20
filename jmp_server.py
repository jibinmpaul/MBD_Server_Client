import socket,select
print("Socket successfully created")
port = 12345
socket_list = []
users = {}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',port))
print("Socket binded to %s" %(port))

s.listen(5)
print("Socket is listening")
socket_list.append(s)
while True:
    ready_to_read,ready_to_write,in_error = select.select(socket_list,[],[],0)
    for sock in ready_to_read:
        if sock == s:
            connect, addr = s.accept()
            socket_list.append(connect)
            print("Got connection from:" + str(addr))
        else:
            try:
                output = sock.recv(1024).decode()
                if not output:
                   break
                print("User: "+str(output))

            except:
                continue
s.close()


