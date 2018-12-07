from random import randint
from random import uniform
from random import shuffle

def fitness(a: list, tabuleiro: int):
    c=len(a)/tabuleiro**2
    return c

#"{:b}".format(decimal_number): passa de decimal para binario sem o 0b na frente
#int(binario, 2): muda o numero binario para base 2/


def dominacao(rainha: list, tabuleiro: int):
    lista=[]
    lista.append(rainha)
    # eixo x
    for i in range(0,tabuleiro):
        tupla=[rainha[0],i]
        if tupla not in lista:
            lista.append(tupla)
    # eixo y
    for i in range(0, tabuleiro):
        tupla=[i,rainha[1]]
        if tupla not in lista:
            lista.append(tupla)
    #superior esquerda
    for i in range(1,min(rainha[0]-0,rainha[1]-0)+1):
        tupla=[rainha[0]-i,rainha[1]-i]
        if tupla not in lista:
            lista.append(tupla)
    #superior direito
    for i in range(1,min(rainha[0]-0,tabuleiro-rainha[1]-1)+1):
        tupla=[rainha[0]-i,rainha[1]+i]
        if tupla not in lista:
            lista.append(tupla)
    #inferior esquerdo
    for i in range(1,min(tabuleiro-rainha[0]-1,rainha[1]-0)+1):
        tupla=[rainha[0]+i,rainha[1]-i]
        if tupla not in lista:
            lista.append(tupla)
    #inferior direito :erro
    for i in range(1,min(tabuleiro-rainha[0]-1,tabuleiro-rainha[1]-1)+1):
        tupla=[rainha[0]+i, rainha[1]+i]
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
            if [x,y] not in dominio and rainhas:
                lista.append("O")
            elif [x,y] not in rainhas:
                lista.append("X")
            else:
                lista.append("R")

    for i in range(0,tabuleiro):
        for j in range(0, tabuleiro):
            print(lista[j + i * tabuleiro],end=' ')
        print()
        '''print("| "+lista[0+i*tabuleiro],"| "+lista[1+i*tabuleiro],"| "+lista[2+i*tabuleiro],"| "+lista[3+i*tabuleiro],
              "| "+lista[4+i*tabuleiro],"| "+lista[5+i*tabuleiro],"| "+lista[6+i*tabuleiro],"| "+lista[7+i*tabuleiro]+" |")'''

def randomIndividual(queenQuantity: int, tabuleiro: int):
    resp=[]
    for i in range(queenQuantity):
        rand1=randint(0,tabuleiro-1)
        rand2=randint(0,tabuleiro-1)
        while (rand1,rand2) in resp:
            rand1 = randint(0, tabuleiro-1)
            rand2 = randint(0, tabuleiro-1)
        tupla=(rand1,rand2)
        resp.append(tupla)
    return resp

def localSearch(queens: list, board: int):
    listBase = []
    listMoves = [0,1,2,3]
    queensAux = queens.copy()
    best = queens.copy()
    for i in range(len(queens)):
        listBase.append(i)
    lista = listBase.copy()
    shuffle(lista)
    while(lista):
        index=lista.pop()
        shuffle(listMoves)
        for i in range(len(listMoves)):
            if i==0:
                #SEMPRE DIMINUI SÓ UMA VEZ CADA RAINHA
                if queensAux[index][0]<board-1:
                    queensAux[index][0]=queensAux[index][0]-1
                    print("\n\n\n\n\n\n")
                    print(queens[index][0])
                    print(queensAux[index][0])
                    print("\n\n\n\n\n\n")
                #NÃO ESTAO FAZENDO NADA
            if i==1:
                if queensAux[index][1]<board-1:
                    queensAux[index][1]+=1
            if i==2:
                if queensAux[index][0]>0:
                    queensAux[index][0]-=1
            if i==3:
                if queensAux[index][1]>0:
                    queensAux[index][1]-=1

            #ESTÁ DANDO SEMPRE QUE O FITNESS DOS DOIS É IGUAL
            a=fitness(queensAux,board) - fitness(best,board)
            print("a:"+str(a))
            if fitness(queensAux,board) > fitness(best,board):
                best = queensAux.copy()
                lista = listBase.copy()
                shuffle(lista)
                break

    return best

rainhas=[[3,1]]
imprimir(rainhas,8)
print("\nfitness: "+str(fitness(totalDaDominacao(rainhas, 8),8))+"\n")
rainhas=[[3,1],[2,3]]
imprimir(rainhas,8)
print("\n"+str(fitness(totalDaDominacao(rainhas, 8),8))+"\n")
rainhas=[[0,2],[1,1],[6,0],[7,3],[3,6]]
imprimir(rainhas,8)
print("\nfitness: "+str(fitness(totalDaDominacao(rainhas, 8),8))+"\n")
rainhas=[[7,1],[1,2],[1,3]]
imprimir(rainhas,8)
print(localSearch(rainhas,8))
imprimir(rainhas,8)