#atribuindo elementos aleatoriaamente a duas matrizes de 5 linhas e 3 colunas 
#e atribuido a soma de cada elemento correspondente a uma terceira matriz
import  random
a=[]
b=[]
c=[]
for i in range(5):
    a.append([])
    b.append([])
    c.append([])
    for j in range (3):
        a[i].append(random.randint(0, 10))
        b[i].append(random.randint(0, 10))
        c[i].append(a[i][j] + b[i][j])
print(a)
print(b)
print(c)