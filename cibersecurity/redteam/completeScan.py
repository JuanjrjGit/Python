import os
import sys
import getopt
import socket
import ipaddress

def main():
    red = "192.168.10.0/24"
    portScan(pingScan(red))

def pingScan(red):
    listaIps = []
    hosts = ipaddress.IPv4Network(red).hosts()

    for host in hosts:
        print("\rEscaneando la IP:", host, end = "")
        comando = "ping -c 1 -W 0.05 " + str(host) + " > /dev/null"
        resultado = os.system(comando)
        #print(ip, resultado)
        if resultado == 0:
            listaIps.append(str(host))
            print(listaIps)
            print (" Host is up", host)
    return listaIps


def portScan(listaIps):
    puertoMin = 0
    puertoMax = 1023

    for ip in listaIps:
        print("\r Escaneando host:", ip )
        for puerto in range(puertoMin, puertoMax+1):
            print("\rEscaneando puerto - ", puerto, end = "")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)

            respuesta = s.connect_ex((ip,puerto))
            s.close()
            if respuesta == 0:
                print("\nEncontrado un puerto en - " , puerto)

main()
