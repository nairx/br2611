import socket 

server = socket.socket()

server.bind(("127.0.0.1",5000))

server.listen()

print("Waiting for client....")

client,address = server.accept()

print("Client Connected: ",address)

client.close() 
server.close()