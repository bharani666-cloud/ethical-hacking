import socket
domain=input("enter domain:")
print(f"IP Address of {domain}:",socket.gethostbyname(domain))
