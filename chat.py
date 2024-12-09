import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(1)
    print("Server is listening for connections...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        message = conn.recv(1024).decode()
        if message.lower() == "exit":
            print("Chat ended by the client.")
            break
        print(f"Client: {message}")
        reply = input("You: ")
        conn.send(reply.encode())
    conn.close()

if __name__ == "__main__":
    start_server()
