import socket 
client = socket.socket()
client.connect(("127.0.0.1",5000))
while True:
    message = input("Cient: ")
    client.sendall(message.encode())
    if message == "bye":
        break
    response = client.recv(1024).decode()
    print("Server: ", response)
client.close()