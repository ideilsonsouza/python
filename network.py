import netifaces
import subprocess

def get_active_interface():
    """
    Obter interface de rede
    Compativel com sistemas Unix
    """
    try:
        result = subprocess.run(['ip', 'route', 'get', '1'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')
        for line in output_lines:
            if 'dev' in line:
                parts = line.split('dev')
                if len(parts) >= 2:
                    return parts[1].split()[0].strip()
    except Exception:
        pass
    return None

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

def get_mac_address():
    """Obtém o endereço MAC da interface de rede."""
    try:
        interfaces = netifaces.interfaces()
        for iface in interfaces:
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_LINK in addrs:
                mac = addrs[netifaces.AF_LINK][0]['addr']
                if mac != '00:00:00:00:00:00':
                    return mac
    except Exception:
        pass
    return None