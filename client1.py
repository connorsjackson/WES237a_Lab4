import socket

sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO: 
# 1: Connect the socket (sock) to the <SERVER-IP> and choosen port <LISTENING-PORT>
# 2: Send the message "Hello world!\n"
# 3: Close the socket

server_name = '192.168.2.1' #Local machine
server_port = 8008
sock_client.connect((server_name, server_port)) #1 socket.connect(servername)
for i in range(5):
    user_input = input("Please type a message:")
    sock_client.sendall(bytes(user_input, 'utf-8'))#2
sock_client.close()#3