import socket
import threading

HOST = "127.0.0.1"
PORT = 7777


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                print("\nServer closed the connection.")
                break

            print(f"\n{message}")
            print("You: ", end="", flush=True)

        except OSError:
            break


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to chat server.")
print("Type 'exit' to leave.")

receive_thread = threading.Thread(
    target=receive_messages,
    args=(client_socket,),
    daemon=True
)

receive_thread.start()

while True:
    try:
        message = input("You: ")

        client_socket.send(message.encode())

        if message.lower() == "exit":
            break

    except OSError:
        print("Connection closed.")
        break

client_socket.close()