import socket


def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn = server_socket.accept()[0]  # wait for client

    request = conn.recv(4096).decode()
    print(f"Received request:\n{request}")

    lines = request.split("\r\n")  # Split request into lines
    request_line = lines[0]
    headers = lines[1:]

    # Example: request_line = "GET /user-agent HTTP/1.1"
    path = request_line.split(" ")[1]

    if path == "/user-agent":
        # Look for the User-Agent header
        user_agent = ""
        for header in headers:
            if header.lower().startswith("user-agent:"):
                user_agent = header[len("User-Agent:"):].strip()
                break

        body = user_agent
        content_length = len(body.encode())

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {content_length}\r\n"
            "\r\n"
            f"{body}"
        )
        conn.sendall(response.encode())

    elif path == "/":
        conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")

    else:
        conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")


if __name__ == "__main__":
    main()
