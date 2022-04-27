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

d = {"a":158,"b":35,"c":45}
print(mais_recorrente(d))