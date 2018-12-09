from random import randint
from random import uniform
from operator import itemgetter
import time

def keyToSortQueens(e):
    return str(e[0])+str(e[1])

def fitness(dominio: list, tabuleiro: int):
    dominio.sort(key=keyToSortQueens)
    #print(dominio)
    resp=len(dominio)/tabuleiro**2
    #print("len(dominio): "+str(len(dominio))+"\ntabuleiro: "+str(tabuleiro**2)+"\nfitness:"+str(resp))
    return resp

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
    #inferior direito
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
        '''print("| "+lista[0+i*tabuleiro],"| "+lista[1+i*tabuleiro],"| "+lista[2+i*tabuleiro],"| "+lista[3+i*tabuleiro],
              "| "+lista[4+i*tabuleiro],"| "+lista[5+i*tabuleiro],"| "+lista[6+i*tabuleiro],"| "+lista[7+i*tabuleiro]+" |")'''

#"{:b}".format(decimal_number): passa de decimal para binario sem o 0b na frente
#int(binario, 2): muda o numero binario para base 2/
#int("10011101", base=2)

def allQueensToBinaryString(rainhas: list, tamanho: int):
    maxBinary="{:b}".format(tamanho)
    strResp = ""
    for i in range(len(rainhas)):
        auxBin=queenToBinaryString(rainhas[i],tamanho)
        strResp+=auxBin
    return strResp

def queenToBinaryString(queen: list, board: int):
    maxBinary = "{:b}".format(board)
    maxSizeBinary = len(maxBinary)
    strResp = ""
    for i in range(2):
        auxBin = "{:b}".format(queen[i])
        for k in range(maxSizeBinary - len(auxBin)):
            strResp += "0"
        strResp += auxBin
    return strResp


def sameSpotCorrection(x: str, y: str, queens: list, board: int):
    #print("sameSpot")
    list1 = list(x)
    list2 = list(y)
    while (int(''.join(list1), base=2),int(''.join(list2), base=2)) in queens:
        i=randint(0,1)
        j=randint(0,len(x)-1)
        if i==0:
            if list1[j]=="0":
                list1[j]="1"
            else:
                list1[j]="0"
        else:
            if list2[j]=="0":
                list2[j]="1"
            else:
                list2[j]="0"
        list1 = list(outOfBoundBinaryCorrection(''.join(list1), board))
        list2 = list(outOfBoundBinaryCorrection(''.join(list2), board))
    x= ''.join(list1)
    y= ''.join(list2)
    ##Gambiarra para corrigir o nao estar deixando de ser binario
    return (int(x, base=2),int(y, base=2))


def BinaryStringToQueensArray(bin: str, tamanho: int):
    maxBinary = "{:b}".format(tamanho)
    maxSizeBinary = len(maxBinary)
    auxlist=split_every(maxSizeBinary,bin)
    resp=[]
    for i in range(0, len(auxlist), 2):
        auxlist[i]=outOfBoundBinaryCorrection(auxlist[i], tamanho)
        auxlist[i+1]=outOfBoundBinaryCorrection(auxlist[i+1], tamanho)
        if (int(auxlist[i], base=2),int(auxlist[i+1], base=2)) in resp:
            auxTuple = sameSpotCorrection(auxlist[i],auxlist[i+1],resp, tamanho)
        else:
            auxTuple=(int(auxlist[i], base=2),int(auxlist[i+1], base=2))
        resp.append(auxTuple)
    return resp

#endireitar, TA BUGADOOOO
def outOfBoundBinaryCorrection(auxlist, board):
    '''maxBinary = "{:b}".format(board)
    maxSizeBinary = len(maxBinary)
    decimal=int(auxlist,base=2)
    decimal=decimal%board
    auxBin = "{:b}".format(decimal)
    strResp = ""
    for k in range(maxSizeBinary - len(auxBin)):
        strResp += "0"
    strResp += auxBin
    return strResp'''
    j = 0
    resp = list(auxlist)
    binStr = list(auxlist)
    while (int(''.join(binStr),base=2) >= board):
        #print("outofbound")
        if (binStr[j] == "0"):
            binStr[j] = "1"
        else:
            binStr[j] = "0"
        if (int(''.join(binStr),base=2) < board):
            resp = binStr
            break
        else:
            binStr = resp
        j += 1
    resp=''.join(resp)
    return resp

def split_every(n: int, s: str):
    return [ s[i:i+n] for i in range(0, len(s), n) ]

def randomStart(individualQuantity: int, queenQuantity: int, tabuleiro: int):
    resp=[]
    for i in range(individualQuantity):
        rand=randomIndividual(queenQuantity,tabuleiro)
        while (0,rand) in resp:
            rand = randomIndividual(queenQuantity, tabuleiro)
        list = [0, rand]  # fitness(começando como 0) e individuo
        resp.append(list)
    return resp

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

def naturalSelection(population: list, procriatorQuantity: int,tabuleiro: int, mutationChance: float, mutationQuantity: int):
    population.sort(reverse=True, key=itemgetter(0))
    kills=len(population)-procriatorQuantity
    for i in range(kills):
        population.pop()
    #print(population)
    population=procriate(population,kills,tabuleiro,mutationChance,mutationQuantity)
    #print(population)
    return population

def procriate(population: list, times: int,board: int, mutationChance: float, mutationQuantity: int):
    maxBinary = "{:b}".format(board)
    maxSizeBinary = len(maxBinary)
    procriator=len(population)
    for i in range(times):
        rand1=randint(0,procriator-1)
        rand2 = randint(0, procriator - 1)
        while(rand1==rand2):
            rand2 = randint(0, procriator - 1)
        queen1=allQueensToBinaryString(population[rand1][1],board)
        queen2=allQueensToBinaryString(population[rand2][1],board)
        rand=randint(0,len(queen1)-1)
        newqueen=""
        for j in range(0,len(queen1)):
            if j<rand:
                newqueen+=queen1[j]
            else:
                newqueen+=queen2[j]

        #Fazer a mutação
        mutation=uniform(0,1)#float randomico entre 0 e 1
        if(mutationChance>mutation):
            newqueen=list(newqueen)
            for k in range(mutationQuantity):
                #print("mutation")
                rand=randint(0,len(newqueen)-1)
                if newqueen[rand]=="0":
                    newqueen[rand]="1"
                else:
                    newqueen[rand]=="0"
        newqueen=''.join(newqueen)
        newqueen=BinaryStringToQueensArray(newqueen,board)
        individual=[0,newqueen]
        population.append(individual)

    return population








'''tamanho=8
rainhas=[(3,1)]
imprimir(rainhas,tamanho)
print("\nfitness: "+str(fitness(totalDaDominacao(rainhas, tamanho),tamanho))+"\n")
rainhas=[(3,1),(2,3)]
imprimir(rainhas,tamanho)
print("\n"+str(fitness(totalDaDominacao(rainhas, tamanho),tamanho))+"\n")
rainhas=[(0,2),(1,1),(6,0),(7,3),(3,6)]
imprimir(rainhas,tamanho)
print("\nfitness: "+str(fitness(totalDaDominacao(rainhas, tamanho),tamanho))+"\n")
print(rainhas)
a=allQueensToBinaryString(rainhas, tamanho)
print(a)
print(BinaryStringToQueensArray(a,tamanho))
print(randint(0, tamanho-1))'''

start = time.time()

individualQuantity = 100
queensQuantity = 8
tabuleiro = 14
mutationChance = 0.05
mutationQuantity= 2 #quantos bits mudam por ver
procriatorQuantity=int(individualQuantity/2)
iterations=1000

population=randomStart(individualQuantity,queensQuantity,tabuleiro)


'''for i in range(individualQuantity):
    population[i][0]=fitness(totalDaDominacao(population[i][1],tabuleiro),tabuleiro)
    imprimir(population[i][1],tabuleiro)
    print()

#population.sort(reverse=True,key=itemgetter(0))
print(population)
population=naturalSelection(population,procriatorQuantity, tabuleiro,mutationChance,mutationQuantity)'''

for i in range(iterations):
    for j in range(individualQuantity):
        population[j][0] = fitness(totalDaDominacao(population[j][1], tabuleiro), tabuleiro)
    if (population[0][0]==1):
        print("iterações: "+str(i))
        break
    population = naturalSelection(population, procriatorQuantity, tabuleiro, mutationChance, mutationQuantity)

for j in range(individualQuantity):
    population[j][0] = fitness(totalDaDominacao(population[j][1], tabuleiro), tabuleiro)

imprimir(population[0][1],tabuleiro)
print(population[0])
print("tempo:"+str(time.time()-start)+"s")