from logging import exception
from socket import *

HOST = ''
PORT = 5000


def acesso_dados(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'r')
    except:
        raise exception("Arquivo não existente")
    return arquivo.read()


def processamento(nome_arquivo):
    try:
        conteudo = acesso_dados(nome_arquivo)
    except exception as err:
        resposta = err
        return resposta


def parse_conteudo(conteudo):
    palavras = conteudo.split()
    dicio = {}
    for palavra in palavras:
        if dicio.get(palavra) != None:
            dicio[palavra] = dicio.get(palavra) + 1
        else:
            dicio[palavra] = 0
    return dicio


def contar(dicio):
    for palavra in dicio:


def mais_recorrente(conteudo):
    dicio = parse_conteudo(conteudo)


s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
(conect, add) = s.accept()
pedido = conect.recv()
