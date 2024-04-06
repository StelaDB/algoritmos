#ordenar em ordem crescente e dps imprimir a ordem decrescente 
a=[10,9,8,7,6,5,4,3,2,1]
for i in range(len(a)-1):
    for j in range (i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a[::-1])