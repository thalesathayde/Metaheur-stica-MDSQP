
def fitness(a: list, tabuleiro: int):
    c=len(a)/tabuleiro**2
    return c

#"{:b}".format(decimal_number): passa de decimal para binario sem o 0b na frente
#int(binario, 2): muda o numero binario para base 2/


def dominacao(rainha: tuple, tabuleiro: int):
    lista=[]
    lista.append(rainha)
    # eixo x
    for i in range(0,tabuleiro):
        tupla=(rainha[0],i)
        if tupla not in lista:
            lista.append(tupla)
    # eixo y
    for i in range(0, tabuleiro):
        tupla=(i,rainha[1])
        if tupla not in lista:
            lista.append(tupla)
    #superior esquerda
    for i in range(1,min(rainha[0]-0,rainha[1]-0)+1):
        tupla=(rainha[0]-i,rainha[1]-i)
        if tupla not in lista:
            lista.append(tupla)
    #superior direito
    for i in range(1,min(rainha[0]-0,tabuleiro-rainha[1]-1)+1):
        tupla=(rainha[0]-i,rainha[1]+i)
        if tupla not in lista:
            lista.append(tupla)
    #inferior esquerdo
    for i in range(1,min(tabuleiro-rainha[0]-1,rainha[1]-0)+1):
        tupla=(rainha[0]+i,rainha[1]-i)
        if tupla not in lista:
            lista.append(tupla)
    #inferior direito :erro
    for i in range(1,min(tabuleiro-rainha[0]-1,tabuleiro-rainha[1]-1)+1):
        tupla=(rainha[0]+i, rainha[1]+i)
        if tupla not in lista:
            lista.append(tupla)
    return lista

def totalDaDominacao(rainhas: list, tabuleiro: int):
    resp=dominacao(rainhas[0],tabuleiro)
    for i in range(1,len(rainhas)):
        aux=dominacao(rainhas[i],tabuleiro)
        for j in range(len(aux)):
            if aux[j] not in resp:
                resp.append(aux[j])
    return resp

def imprimir(rainhas: list,tabuleiro: int):
    dominio=totalDaDominacao(rainhas, tabuleiro)
    lista=[]
    for x in range(tabuleiro):
        for y in range(tabuleiro):
            if (x,y) not in dominio and rainhas:
                lista.append("O")
            elif (x,y) not in rainhas:
                lista.append("X")
            else:
                lista.append("R")

    for i in range(0,tabuleiro):
        for j in range(0, tabuleiro):
            print(lista[j + i * tabuleiro],end=' ')
        print()


rainhas=[(3,1)]
imprimir(rainhas,8)
print("\nfitness: "+str(fitness(totalDaDominacao(rainhas, 8),8))+"\n")
rainhas=[(3,1),(2,3)]
imprimir(rainhas,8)
print("\n"+str(fitness(totalDaDominacao(rainhas, 8),8))+"\n")
rainhas=[(0,2),(1,1),(6,0),(7,3),(3,6)]
imprimir(rainhas,8)
print("\nfitness: "+str(fitness(totalDaDominacao(rainhas, 8),8))+"\n")