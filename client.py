import socket

HOST = 'localhost'
PORT = 5000
server_address = (HOST, PORT)
disconnect = False

while True:
    #tcp_socket = socket.create_connection(server_address)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(server_address)
    try:
        data = input('Ingrese un mensaje por favor\n')
        data = data.encode()
        tcp_socket.sendall(data)
        res = tcp_socket.recv(1024).decode('utf-8')
        if res == 'DESCONEXION':
            disconnect = True
        print(res)

    finally:
        tcp_socket.close()
        if disconnect:
            exit()