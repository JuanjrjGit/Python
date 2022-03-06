import socket
import sys

serverEscaneado = input("Pon la ip que quieres escanear ")
serverIp = socket.gethostbyname(serverEscaneado)

print(" Escaneando IP: " + serverIp)

try:
    for port in range (1,100): #Escanea los primeros 100 puertos
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((serverEscaneado, port))
        if result == 0:
            print("Puerto {} esta abierto ".format(port))
        sock.close()
except KeyboardInterrupt:
    print("Cerrando")
    sys.exit()
except socket.gaierror:
    sys.exit()
except socket.error:
    sys.exit()





