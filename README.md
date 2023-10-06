
# Port Scanner
A python script that allows you to scan a target for open ports within a specified range and provides the option to display detailed information about the open ports and their associated services.
## Features

- Target Resolution: It can accept either an IP address or a hostname as the target. It uses socket.gethostbyaddr and socket.gethostbyname to resolve the target to an IP address, and it handles cases where the input might be an invalid IP address or hostname.

- Port Scanning: It scans a range of ports specified in the port_range parameter to check for open ports on the target. It uses the socket library to create socket connections and checks if the connection was successful (i.e., the port is open) using s.connect_ex.

- Timeout Handling: It sets a timeout of 5 seconds for each socket connection attempt. This means that if a connection to a particular port takes longer than 5 seconds, it will be considered closed.

- Verbose Output: If the verbose parameter is set to True, the function provides detailed output that includes the hostname (if available) and a table of open ports with their associated services, as defined in the common_ports dictionary.

- Error Handling: It handles errors such as invalid IP addresses or hostnames and provides appropriate error messages.

- Port-Service Mapping: It uses a common_ports dictionary to map known port numbers to their corresponding services, which can be included in the verbose output.

- Port Range Specification: It allows specifying a range of ports to scan using the port_range parameter, making it flexible for different scanning needs.

- Result Return: It returns either a list of open ports or the verbose output string, depending on the verbose parameter.


## Technologies used
- Python
## App demo

https://replit.com/@niangamadou888/boilerplate-port-scanner
