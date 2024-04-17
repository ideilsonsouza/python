import socket

def client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Conectado ao servidor em {host}:{port}")
        message = input("Digite a mensagem para enviar: ")
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Resposta do servidor: {data.decode()}")


def client_on(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Conectado ao servidor em {host}:{port}")
        while True:
            message = input("Digite a mensagem para enviar ('quit' para sair): ")
            if message.lower() == 'quit':
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Resposta do servidor: {data.decode()}")
        
        print("Fechando conexão com o servidor.")

client_on("127.0.0.1", 8088)