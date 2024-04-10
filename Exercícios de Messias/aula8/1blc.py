#criar duas matrizes com numeros aleatorios a e b com 7 elementos cada
#criar uma matriz c em quea primeira coluna sera os elementos de a e a segunda coluna sera os elementos de b
a=[1,2,3,4,5,6,7]
b=[8,9,10,11,12,13,14]
c=[[a[i],b[i]] for i in range(7)]
print(c)