import socket

TCP_IP = 'localhost'
TCP_PORT = 5000


def run_server(ip, port):
    def handle(sock: socket.socket, address: str):
        print(f'Connection established {address}')
        while True:
            received = sock.recv(1024)
            if not received:
                break
            data = received.decode()
            print(f'Data received: {data}')
            to_send = input(">>")
            sock.send(to_send.encode())
            print(f"Data sent: {to_send}")
        print(f'Socket connection closed {address}')
        sock.close()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(10)
    print(f'Start echo server {server_socket.getsockname()}')
    try:
        while True:
            new_sock, address = server_socket.accept()
            handle(new_sock, address)
    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        server_socket.close()


if __name__ == '__main__':
    run_server(TCP_IP, TCP_PORT)
