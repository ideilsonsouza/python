import socket
import threading
import datetime

def server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Servidor escutando em {host}:{port}")
        conn, addr = server_socket.accept()
        with conn:
            print(f"Conexão recebida de {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Dados recebidos: {data.decode()}")
                conn.sendall(b"Dados recebidos com sucesso!")


def server_on(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Servidor escutando em {host}:{port}")
        while True:  # Mantém o servidor sempre escutando por novas conexões
            conn, addr = server_socket.accept()
            with conn:
                print(f"Conexão recebida de {addr}")
                while True:  # Loop para tratar os dados da conexão atual
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Dados recebidos: {data.decode()}")
                    conn.sendall(b"Dados recebidos com sucesso!")

def handle_client(conn, addr):
    print(f"Conexão recebida de {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break            
            response = process_request(data.decode())
            conn.sendall(response.encode())
        except KeyboardInterrupt:
            print("Servidor encerrado.")
            break
    conn.close()
    print(f"Conexão com {addr} fechada.")


def process_request(request):
    current_datetime = datetime.datetime.now()
    print(f'Data:{current_datetime}|')  
    print(f'       Messagem:{request}')    
    
    return "Comando não reconhecido."


def server_handle( port=8085, host=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        if not host:
            host = socket.gethostbyname(socket.gethostname())
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Servidor escutando em {host}:{port}")
        while True:
            try:
                conn, addr = server_socket.accept()
                client_thread = threading.Thread(target=handle_client, args=(conn, addr))
                client_thread.start()
            except KeyboardInterrupt:
                print("Servidor encerrado.")
                break


# Exemplo de uso
server_handle()