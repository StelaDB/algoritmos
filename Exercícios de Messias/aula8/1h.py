#construindo uma matriz a com cinco linhas e cinco colunas 
#preenche uma matriz b de mesma dimensão com o dobre
#dos valores de a excerto os elementos da diogonal principal
#e que devem ser o triplo dos elementos correspondentes de a 
import random
a=[[random.randint(1,10) for j in range(5)] for i in range(5)]
b=[]
for i in range(5):
    b.append([])
    for j in range(5):
        if i==j:
            b[i].append(3*a[i][j])
        else:
            b[i].append(2*a[i][j])
print(a)
print(b)