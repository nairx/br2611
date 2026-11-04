import socket 
client = socket.socket()
client.connect(("127.0.0.1",5000))
client.sendall("Client: Hello!".encode())
message = client.recv(1024).decode()
print(message)
client.close()