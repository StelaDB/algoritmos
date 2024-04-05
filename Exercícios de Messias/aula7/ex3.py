#bublesort
#ordenar a sequencia de numeros
a=[5,4,3,2,1]
for i in range(len(a)-1): #(len(a)-1) quer dizer que o ultimo elemento não precisa ser comparado, se ordenar até o penultimo ja fica ordenado o ultimo
    for j in range(i+1,len(a)): 
        if a[i]>a[j]:           #se colocar < ele vai ordenar de forma decrescente e se colocar > ele vai ordenar de forma crescente
            a[i],a[j]=a[j],a[i]
print(a)