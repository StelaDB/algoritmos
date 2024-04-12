#ler duas matrizes a e b de uma dimensão com 12 elementos 
#contruir uma matriz c onde a primeira coluna a ser formada pelos 
#elementos da matriz a multiplicados por 2 e a segunda coluna pelo 
#elementos da matriz b subtraidos de 5
a=[1,2,3,4,5,6,7,8,9,10,11,12]
b=[12,11,10,9,8,7,6,5,4,3,2,1]
c=[]
for i in range(12):
    c.append([a[i]*2])
    c[i].append(b[i]-5)
print(c)