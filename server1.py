import socket
sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO:
# 1: Bind the socket to the pynq board <CLIENT-IP> at port <LISTENING-PORT>
# 2: Accept connections
# 3: Receive bytes from the connection
# 4: Print the received message

#server_name = ''
server_name = '0.0.0.0' #accept any ip address
server_port = 8009 #create the port that will be used. I decided to use 8000
x=0

sock_server.bind((server_name,server_port)) #1 socket.bind(address)
print('Waiting for connection.')
sock_server.listen() # socket.listen()
while True:
    connection, address = sock_server.accept() #2 return value is a pair (conn, address)
    while True:
        if x==0:
            print('Client Connected.')
            x=1
        receive_bytes = connection.recv(1024) #3
        if receive_bytes is None:
            break
        print('The message was: ',receive_bytes)#4
