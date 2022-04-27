from logging import exception
from socket import *

HOST = ''
PORT = 5000


def acesso_dados(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'r')
    except:
        raise RuntimeError("Arquivo não existente")
    return arquivo.read()


def processamento(nome_arquivo):
    try:
        conteudo = acesso_dados(nome_arquivo)
    except RuntimeError as err:
        print(err)
        resposta = err
        return resposta
    palavras = conteudo.split()
    dicio = contar(palavras)
    mais_recorrente = mais_recorrente(dicio)


def contar(palavras):
    dicio = {}
    for palavra in palavras:
        if dicio.get(palavra) != None:
            dicio[palavra] = dicio.get(palavra) + 1
        else:
            dicio[palavra] = 0
    return dicio


def insere(elemento, vetor, pos):
    temp = []

    for i in range(0, len(vetor)):
        if i == pos:
            temp.append(elemento)
        if i != len(vetor)-1:
            temp.append(vetor[i])
    return temp


def mais_recorrente(dicio):
    top5 = [None, None, None, None, None]
    for palavra in dicio:
        for i in range(0, len(dicio)):
            if top5[i] == None:
                top5[i] = palavra
                break
            elif dicio.get(palavra) > dicio.get(top5[i]):
                top5 = insere(palavra, top5, i)
                break
    return top5


s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
    (connect, add) = s.accept()
    pedido = connect.recv(1024)
    resposta = processamento(str(pedido))
    connect.send(str.encode( resposta))
    #connect.recv()
    s.close()

