'''ler uma matriz de uma dimensão com 10 elementos e atribui a uma matriz
b de 10 linhas e tres colunas, onde a primeira coluna sera os elementos de
a somando a 5 a segunda fatorial dos elementos de a e a quadrado dos elementos de a'''
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in range (10):
    b.append((a[i])+5)
    fatorial=1
    for j in range(1):
        fatorial*=j+1
        b[i].append(a[i]**2)
        b[i].append(fatorial)
print(b)