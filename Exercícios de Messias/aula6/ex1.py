#Ler elementos para uma lista A e criar uma lista B, seguido a seguinte lei de criação
#se o indice de A for par multiplica a 5 e se for impar soma por 5 
a=[]
b=[]
for i in range(1,6):
    a.append(int(input(f"Digite o {i+1}° numero: "))) #f é uma formatação que permite uma variável dentro do print 
    if i-1%2==0:
        b.append(a[i]*5)
    else:
        b.append(a[i]+5)
print(a)
print(b)