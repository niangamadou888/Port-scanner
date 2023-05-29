import socket
import re
from common_ports import ports_and_services as portnames

def get_open_ports(target, port_range, verbose=False):
    try:
        host = None
        try:
            host = socket.gethostbyaddr(target)[0]
        except socket.herror:
            pass
        ip = socket.gethostbyname(target)
    except:
        return 'Error: Invalid IP address' if re.match('\d{3}\.\d{1,3}.\d{1,3}.\d{1,3}',target) else 'Error: Invalid hostname'

    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        s.close()

    if verbose:
        verb = 'Open ports for {} ({})\nPORT     SERVICE\n'.format(host, ip) if host else 'Open ports for {}\nPORT     SERVICE\n'.format(target)
        for port in open_ports:
            verb += '{0:<9}{1}\n'.format(port, portnames.get(port, ''))
        return verb.rstrip()

    return open_ports
