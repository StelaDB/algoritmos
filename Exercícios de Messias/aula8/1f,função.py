#Ler uma matriz com 5 linhas e 4 colunas 
#e construir uma matriz b de mesma dimensão
#em que cada elemento é o fatorial do respectivo elemento de a
import random
import math
a=[[random.randint(1,10) for j in range(4)] for i in range (5)]
b=[[math.factorial(a[i][j]) for i in range(4)] for j in range(5)]
print(a)
print(b)