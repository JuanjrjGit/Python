import socket

def main():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(local_ip)
    #host = input("Ponga en que servidor ")
    port = input("En que puerto escucha: ")
    #print(host)
    print(port)
    listen(hostname, port)

def listen(host,port):
    try:
        port = int(port)
        while True:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen(5)
            conn, direccion = server.accept()
            print('Conectado con ' + direccion[0] + ':' + str(direccion[1]))
    except KeyboardInterrupt:
        sys.exit()
main()
