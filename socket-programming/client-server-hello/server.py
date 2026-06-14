import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 4444))

server_socket.listen(1)
print("Server is waiting on port 4444...")

client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)

message = client_socket.recv(1024).decode()
print("Client:", message)

client_socket.send("Message received by server".encode())

client_socket.close()
server_socket.close()

