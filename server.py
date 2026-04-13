import socket

# define the host and port
HOST = "127.0.0.1"
PORT = 9000


with socket.socket() as server_sock:
    server_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_sock.bind((HOST,PORT))
    server_sock.listen(5)
    print(f"Linstening on {HOST}:{PORT}...")

    RESPONSE = b"HTTP/1.1 200 OK\r\nContent-type: text/html\r\n"
    with open('resources/index.html','rb') as f:
        body = f.read()
        RESPONSE += f"Content-length: {len(body)}\r\n\r\n".encode()
        RESPONSE += body
    
    while True:
        client_sock, client_addr = server_sock.accept()
        print(f"New connection from {client_addr}.")
        with client_sock:
            client_sock.sendall(RESPONSE)
