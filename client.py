import socket

TCP_IP = 'localhost'
TCP_PORT = 5000


def run_client(ip: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f'Connection established {server}')
        message = input(">>")
        while message not in ["exit", "stop", " ", ""]:
            for line in message.split(' '):
                print(f'Send data: {line}')
                sock.send(line.encode())
                response = sock.recv(1024)
                print(f'Response data: {response.decode()}')
                message = input(">>")


if __name__ == '__main__':
    run_client(TCP_IP, TCP_PORT)
