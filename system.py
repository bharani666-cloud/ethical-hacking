import platform
import socket
print("system:",platform.system())
print("node name",platform.node())
print("Release:",platform.release())
print("Version:",platform.version())
print("Machine:",platform.machine())
print("Processor:",platform.processor())
print("IP Address:",socket.gethostbyname(socket.gethostname()))

