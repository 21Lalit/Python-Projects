import socket
import threading

HOST = "127.0.0.1"
PORT = 7777

clients = []


def broadcast(message, sender_socket):
    disconnected_clients = []

    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except OSError:
                disconnected_clients.append(client)

    for client in disconnected_clients:
        if client in clients:
            clients.remove(client)
        client.close()


def handle_client(client_socket, client_address):
    print("New client connected:", client_address)

    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                print("Client disconnected:", client_address)
                break

            if message.lower() == "exit":
                print("Client ended chat:", client_address)
                break

            print(f"{client_address}: {message}")

            broadcast_message = f"{client_address}: {message}"
            broadcast(broadcast_message, client_socket)

        except OSError as e:
            print("Error with client:", client_address)
            print("Error:", e)
            break

    if client_socket in clients:
        clients.remove(client_socket)

    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server running on {HOST}:{PORT}")
print("Waiting for clients...")

while True:
    client_socket, client_address = server_socket.accept()

    clients.append(client_socket)

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )

    thread.start()