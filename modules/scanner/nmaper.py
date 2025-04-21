from concurrent.futures import ThreadPoolExecutor
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
    ports = range(1, max_port + 1) ## Set the range of ports to scan
    # Create a ThreadPoolExecutor to scan ports concurrently
    def task(port):
        return scan_port(domain, port)
    output = []
    # Use ThreadPoolExecutor to scan ports concurrently
    with ThreadPoolExecutor(max_workers=500) as executor:
        for result in executor.map(task, ports):
            if result:
                output.append(result)

    return output

