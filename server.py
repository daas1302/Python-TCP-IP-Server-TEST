import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 5000

server_address = (HOST, PORT)
tcp_socket.bind(server_address)

tcp_socket.listen(1)

while True:
    print('Esperando conexión...')
    connection, client = tcp_socket.accept()

    try:
        while True:
            data = connection.recv(1024).decode('utf-8').upper()
            if data == 'DESCONEXION':
                connection.sendall(data.encode())
                break
            
            if not data:
                break
            print(data)
            connection.sendall(data.encode())

    finally:
        connection.close()

