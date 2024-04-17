import socket
import netifaces

def get_ip_address():
    """Obtém o endereço IP local do dispositivo."""
    try:
        interfaces = netifaces.interfaces()
        for iface in interfaces:
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addrs:
                ip = addrs[netifaces.AF_INET][0]['addr']
                if ip != '127.0.0.1':
                    return ip
    except Exception:
        pass
    return '127.0.0.1'

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))              
        
        if result == 0:
            print(f"Porta {port} aberta em {ip}")
            try:
                # Obtém o hostname associado ao endereço IP
                hostname = socket.gethostbyaddr(ip)[0]
                print(f"Hostname: {hostname}")
            except socket.herror:
                print("Não foi possível obter o hostname")
        
        sock.close()
                
    except socket.error as e:
        print(f"Erro ao escanear porta {port} em {ip}: {e}")