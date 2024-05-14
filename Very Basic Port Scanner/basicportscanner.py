import socket
import time
start = time.time()
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = input("Type the IPv4 address: ")
targetip = socket.gethostbyname(ip)
number = input("How many ports do you want to check? : ")

try:
    number = int(number)

    if number > 65535 or number < 0:
        print("The number of ports must be between 1 and 65535 inclusive.")
    else:
        print(f"Checking {number} ports...")
        def scan_port(port):
                try:
                    soc.connect((targetip, port))
                    return True
                except:
                    return False
        for port in range(number):
                if(scan_port(port)):
                    print("Port ",port," is opened")
                else:
                    print("Port",port," is closed/filtered")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
total_time =  time.time() - start
print("Total time to scan:",total_time,"seconds")
