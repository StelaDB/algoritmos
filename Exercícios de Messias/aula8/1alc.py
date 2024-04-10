#atribuind elemento aleatoriamente a duas matrizes de 5 linhas e 3 colunas
#e atruibindo a soma de cada elemento correspondente a uma terceira matriz utiliza 
import random
a=[[random.randint(1,10) for j in range(3)] for i in range(5)]
b=[[random.randint(1,10) for j in range(3)] for i in range(5)]
c=[[a[i][j]+b[i][j] for j in range(3)] for i in range(5)]
print(a)
print(b)
print(c)