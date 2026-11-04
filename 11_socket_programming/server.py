#server.py
import socket 
server = socket.socket()
server.bind(("127.0.0.1",5000))
server.listen()
while True:
    print("Waiting for client....")
    client,address = server.accept()
    print("Client Connected: ",address)
    while True:
        message = client.recv(1024).decode()
        if message=="bye":
            break
        print("Client: ",message)
        response = input("Server: ")
        client.sendall(response.encode())
client.close() 
server.close()