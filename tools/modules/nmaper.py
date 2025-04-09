import socket

def scan_port(domain: str, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "unknown"
        
        result = sock.connect_ex((domain, port))
        if result == 0:
            return (domain, port, service)
        else:
            return None

def scan_ports(domain: str, max_port=1000):
    output = []
    for port in range(1, max_port + 1):
        result = scan_port(domain, port)
        if result:
            output.append(result)
    return output

