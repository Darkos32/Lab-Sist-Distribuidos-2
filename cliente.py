from socket import *

HOST = 'localhost'
PORT = 5000

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
arquivo = input("Diga o nome do arquivo")
s.send(str.encode(arquivo))
resposta = s.recv(1024)
print("As palavras mais recorrentes são:")
for palavra in resposta:
    print(palavra+"\n")
s.close()