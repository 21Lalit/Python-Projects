import socket

HOST = "127.0.0.1"
PORT = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

print("Connected to echo server.")
print("Type 'exit' to close connection.")

while True:
    message = input("You: ")

    client_socket.send(message.encode())

    if message.lower() == "exit":
        break

    response = client_socket.recv(1024).decode()

    print("Server:", response)

client_socket.close()

