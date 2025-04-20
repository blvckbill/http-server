import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn = server_socket.accept()[0] # wait for client
    # conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")

    path = conn.recv(4096).decode().split(" ")[1]
    if path == "/":
        conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    
    elif path.startswith("/echo/"):
        echo_str = path[len("/echo/"):]
        content_length = len(echo_str.encode()) 
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {content_length}\r\n"
            "\r\n"
            f"{echo_str}"
        )
        conn.sendall(response.encode())

    else:
        conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")



    
if __name__ == "__main__":
    main()
