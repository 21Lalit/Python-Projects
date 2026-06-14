import socket

HOST = "127.0.0.1"
PORT = 6666

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))
print("Connected to the server.")
print("Type 'exit' to close the chat.")

while True:
    client_message = input("You: ")

    client_socket.send(client_message.encode())

    if client_message.lower() == "exit":
        print("You ended the chat.")
        break

    server_message = client_socket.recv(1024).decode()

    if not server_message:
        print("Server closed the connection.")
        break

    if server_message.lower() == "exit":
        print("Server ended the chat.")
        break
    print("Server:", server_message)

client_socket.close()