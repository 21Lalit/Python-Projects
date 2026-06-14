import socket

HOST = "127.0.0.1"
PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen(1)
print(f"Echo server running on {HOST}:{PORT}")
print("Waiting for client....")

client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)

while True:
    message = client_socket.recv(1024).decode()

    if message.lower() == "exit":
        print("client disconnected:", client_address)
        break
    
    print("Client:", message)
    
    client_socket.send(message.encode())

client_socket.close()
server_socket.close()