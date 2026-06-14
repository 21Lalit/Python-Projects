import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 4444))

message = input("Enter message for server: ")
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print("server:", response)

client_socket.close()
