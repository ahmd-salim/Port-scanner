import sys
import socket 
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid input") 
    print("Check your syntax")
print("." * 30)
print("Time started " + str(datetime.now()))
print("Scanning " + target)
print("." * 30)
try:
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting program\n")
    sys.exit()
except socket.gaierror:
    print("\nError resolving hostname\n")
    sys.exit()
except socket.error:
    print("\nCould not connect to server\n")
    sys.exit()
