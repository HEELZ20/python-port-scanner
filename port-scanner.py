import socket
from datetime import datetime

# Display banner
print("_" * 50)
print("Simple Port Scanner")
print("_" * 50)

# Ask for target IP Address or domain name
target = input("Enter the target IP address or domain name: ")
print("_" * 50)

# Convert domain name to IP address
try:
   target_ip = socket.gethostbyname(target)
except socket.gaierror:
   print(Invalid hostname)
   exit()

print(f"\nScanning target: {target_ip}")
print("Scanning started at: ", datetime.now())
print("_" * 50)

open_ports = []

# Port range to scan
start_port = 1
end_port  = 1024

try:
   for port in range(start_port, end_port + 1)

      # Create a socket object
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   # Set timeout for the socket(1 second)
   s.settimeout(1)

   # Attempt to connect to the port
   result = s.connect_ex((target_ip, port))
   if result == 0:
      open_ports.append(port)
      print(f"Port {port} is OPEN")
   s.close()

except KeyboardInterrupt
   print("\nScan stopped by user.")
   exit()

except socket.error:
   print("\nCould not connect to the server.")
   exit()

# Print the list of open ports and save to file
with open("open_ports.txt", "w") as file:
   file.write(f"Open ports for {target_ip}:\n")
   for port in open_ports:
      file.write(f"{port}\n")


print("_" * 50)
print("Scan Completed!")
print("Results saved to open_ports.txt")

