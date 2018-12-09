from random import randint
from random import uniform
from random import shuffle
from copy import deepcopy
import time

def fitness(dominio: list, tabuleiro: int):
    c=len(dominio)/tabuleiro**2
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
        tupla=[rand1,rand2]
        resp.append(tupla)
    return resp

def moveUp(queen: list, board:int, queens:list):
    if queen[0] > 0:
        if [queen[0]-1,queen[1]] not in queens:
            queen[0] = queen[0] - 1
    return queen

def moveDown(queen: list, board:int, queens:list):
    if queen[0] < board - 1:
        if [queen[0]+1, queen[1]] not in queens:
            queen[0] = queen[0]+1
    return queen

def moveRight(queen: list, board:int, queens:list):
    if queen[1] < board - 1:
        if [queen[0], queen[1]+1] not in queens:
            queen[1] = queen[1]+1
    return queen

def moveLeft(queen:list, board:int, queens:list):
    if queen[1] > 0:
        if [queen[0], queen[1]-1] not in queens:
            queen[1] = queen[1]-1
    return queen

def moveUpRight(queen: list, board:int, queens:list):
    if [queen[0]-1, queen[1]+1] not in queens:
        if queen[0] > 0:
            queen[0] = queen[0] - 1
        if queen[1] < board - 1:
            queen[1] = queen[1] + 1
    return queen

def moveUpLeft(queen: list, board:int, queens:list):
    if [queen[0] - 1, queen[1] - 1] not in queens:
        if queen[0] > 0:
            queen[0] = queen[0] - 1
        if queen[1] > 0:
            queen[1] = queen[1] - 1
    return queen

def moveDownRight(queen: list, board:int, queens:list):
    if [queen[0] + 1, queen[1] + 1] not in queens:
        if queen[0] < board - 1:
            queen[0] = queen[0]+1
        if queen[1] < board - 1:
            queen[1] = queen[1] + 1
    return queen

def moveDownLeft(queen: list, board:int, queens:list):
    if [queen[0] + 1, queen[1] - 1] not in queens:
        if queen[0] < board - 1:
            queen[0] = queen[0]+1
        if queen[1] > 0:
            queen[1] = queen[1] - 1
    return queen

#greed search
def old_localSearch(queens: list, board: int):
    listBase = []
    listMoves = [0,1,2,3,4,5,6,7]
    queensAux = queens.copy()
    best = deepcopy(queens)
    for i in range(len(queens)):
        listBase.append(i)
    lista = listBase.copy()
    shuffle(lista)
    while(lista):
        index=lista.pop()
        shuffle(listMoves)
        for i in range(len(listMoves)):
            if listMoves[i]==0:
                queensAux[index]=moveUp(queensAux[index],board,queensAux)
            if listMoves[i]==1:
                queensAux[index]=moveRight(queensAux[index],board,queensAux)
            if listMoves[i]==2:
                queensAux[index]=moveDown(queensAux[index],board,queensAux)
            if listMoves[i]==3:
                queensAux[index]=moveLeft(queensAux[index], board,queensAux)
            if listMoves[i]==4:
                queensAux[index]=moveUpRight(queensAux[index], board,queensAux)
            if listMoves[i]==5:
                queensAux[index]=moveUpLeft(queensAux[index], board,queensAux)
            if listMoves[i]==6:
                queensAux[index]=moveDownRight(queensAux[index], board,queensAux)
            if listMoves[i]==7:
                queensAux[index]=moveDownLeft(queensAux[index], board,queensAux)

            '''melhorFitness = fitness(totalDaDominacao(best,board), board)
            atualFitness = fitness(totalDaDominacao(queensAux, board),board)
            print("novo eh " + str(atualFitness) + " velho eh " + str(melhorFitness))
            a = atualFitness - melhorFitness
            print("a:"+str(a))
            imprimir(queensAux, board)
            print("----------")'''
            if fitness(totalDaDominacao(queensAux, board),board) > fitness(totalDaDominacao(best,board), board):
                best = deepcopy(queensAux)
                lista = listBase.copy()
                shuffle(lista)
                break
            else:
                queensAux = deepcopy(best)

    return best

def localSearch(queens: list, board: int):
    queensAux = queens.copy()
    best = deepcopy(queens)
    oldBest = []
    while(oldBest!=best):
        oldBest=deepcopy(best)
        for j in range(len(queens)):
            for i in range(8):
                if i==0:
                    queensAux[j]=moveUp(queensAux[j],board,queensAux)
                if i==1:
                    queensAux[j]=moveRight(queensAux[j],board,queensAux)
                if i==2:
                    queensAux[j]=moveDown(queensAux[j],board,queensAux)
                if i==3:
                    queensAux[j]=moveLeft(queensAux[j], board,queensAux)
                if i==4:
                    queensAux[j]=moveUpRight(queensAux[j], board,queensAux)
                if i==5:
                    queensAux[j]=moveUpLeft(queensAux[j], board,queensAux)
                if i==6:
                    queensAux[j]=moveDownRight(queensAux[j], board,queensAux)
                if i==7:
                    queensAux[j]=moveDownLeft(queensAux[j], board,queensAux)

            '''melhorFitness = fitness(totalDaDominacao(best,board), board)
            atualFitness = fitness(totalDaDominacao(queensAux, board),board)
            print("novo eh " + str(atualFitness) + " velho eh " + str(melhorFitness))
            a = atualFitness - melhorFitness
            print("a:"+str(a))
            imprimir(queensAux, board)
            print("----------")'''

            if fitness(totalDaDominacao(queensAux, board),board) > fitness(totalDaDominacao(best,board), board):
                best = deepcopy(queensAux)
            else:
                queensAux = deepcopy(oldBest)

    return best

def perturbation(queens: list, times: int, board: int):
    for i in range(times):
        index=randint(0,len(queens)-1)
        randOp=randint(0,7)
        aux = []
        if randOp == 0:
            aux = moveUp(queens[index], board, queens)
            if queens[index]==aux:
                i-=1
            else:
                queens[index] = aux
        if randOp == 1:
            aux = moveRight(queens[index], board, queens)
            if queens[index]==aux:
                i-=1
            else:
                queens[index] = aux
        if randOp == 2:
            aux = moveDown(queens[index], board, queens)
            if queens[index]==aux:
                i-=1
            else:
                queens[index] = aux
        if randOp == 3:
            aux = moveLeft(queens[index], board, queens)
            if queens[index]==aux:
                i-=1
            else:
                queens[index] = aux
        if randOp == 4:
            aux = moveUpRight(queens[index], board, queens)
            if queens[index]==aux:
                i-=1
            else:
                queens[index] = aux
        if randOp == 5:
            aux = moveUpLeft(queens[index], board, queens)
            if queens[index]==aux:
                i-=1
            else:
                queens[index] = aux
        if randOp == 6:
            aux = moveDownRight(queens[index], board, queens)
            if queens[index]==aux:
                i-=1
            else:
                queens[index] = aux
        if randOp == 7:
            aux = moveDownLeft(queens[index], board, queens)
            if queens[index]==aux:
                i-=1
            else:
                queens[index] = aux
    return queens

'''rainhas=[[3,1]]
imprimir(rainhas,8)
print("\nfitness: "+str(fitness(totalDaDominacao(rainhas, 8),8))+"\n")
rainhas=[[3,1],[2,3]]
imprimir(rainhas,8)
print("\n"+str(fitness(totalDaDominacao(rainhas, 8),8))+"\n")
rainhas=[[0,2],[1,1],[6,0],[7,3],[3,6]]
imprimir(rainhas,8)
print("\nfitness: "+str(fitness(totalDaDominacao(rainhas, 8),8))+"\n")'''


'''rainhas=[[1,1],[1,2],[1,3]]
imprimir(rainhas,8)
print("Meu fitness eh " + str(fitness(totalDaDominacao(rainhas, 8), 8)))
rainhas = localSearch(rainhas, 8)
print(rainhas)
imprimir(rainhas,8)
print("Meu fitness eh " + str(fitness(totalDaDominacao(rainhas, 8), 8)))
rainhas= perturbation(rainhas,6,8)
imprimir(rainhas,8)
print("Meu fitness eh perturbado" + str(fitness(totalDaDominacao(rainhas, 8), 8)))
rainhas = localSearch(rainhas, 8)
print(rainhas)
imprimir(rainhas,8)
print("Meu fitness eh " + str(fitness(totalDaDominacao(rainhas, 8), 8)))'''

start=time.time()

tabuleiro = 8
quantidadeDeRainhas = 5
perturbationTimes = 10 #5~10
maxIterations = 1000

rainhas=randomIndividual(quantidadeDeRainhas,tabuleiro)
#print("Meu fitness inicial eh " + str(fitness(totalDaDominacao(rainhas, tabuleiro), tabuleiro)))
rainhas=localSearch(rainhas,tabuleiro)
best = deepcopy(rainhas)
count=1
for i in range(maxIterations):
    if fitness(totalDaDominacao(best,tabuleiro),tabuleiro) == 1:
        break
    #oldBest=deepcopy(best)
    rainhas=perturbation(rainhas,perturbationTimes,tabuleiro)
    rainhas=localSearch(rainhas,tabuleiro)
    count+=1
    if fitness(totalDaDominacao(rainhas,tabuleiro),tabuleiro)>fitness(totalDaDominacao(best,tabuleiro),tabuleiro):
        best = deepcopy(rainhas)

print("iterações: "+str(count))
imprimir(best,tabuleiro)
print("Meu fitness eh " + str(fitness(totalDaDominacao(best, tabuleiro), tabuleiro)))
print("tempo:"+str(time.time()-start)+"s")