import socket

HOST = "127.0.0.1"
PORT = 6666

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server running on {HOST}:{PORT}")
print("Waiting for client....")

client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)
print("Type 'exit' to close the chat.")

while True:
    client_message = client_socket.recv(1024).decode()

    if not client_message:
        print("Client closed the connection.")
        break

    if client_message.lower() == "exit":
        print("Client ended the chat.")
        break
    
    print("Client:", client_message)
    
    server_message = input("You: ")

    client_socket.send(server_message.encode())

    if server_message.lower() == "exit":
        print("You ended the chat.")
        break

client_socket.close()
server_socket.close()