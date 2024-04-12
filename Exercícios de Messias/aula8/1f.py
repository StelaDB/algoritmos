#Ler uma matriz com 5 linhas e 4 colunas 
#e construir uma matriz b de mesma dimensão
#em que cada elemento é o fatorial do respectivo elemento de a
import random
a=[[random.randint(1,10) for j in range(4)] for i in range (5)]
b=[]
for i in range(5):
    b.append([])
    fatorial=1
    for j in range(4):
        fatorial=1
        for k in range(1,a[i][j]+1):
            fatorial*=k
        b[i].append(fatorial)
print(a)
print(b)