#programa que recebe numeros pares para lista a e numeros impares para lista b, e junta as 
a,b,c=[], [], []
#atribuindo elementos a lista a 
cont=0
while cont<6:
    n=(int(input("Digite um número par: ")))
    if n%2==0:
        a.append(n)
        cont+=1
    else:
        print("Numero impar")
#atribuindo elementos  lista b
cont=0
while cont<6:
    n=(int(input("Digite um numero impar: ")))
    if n%2!=0:
        b.append(n)
        cont+=1
    else:
        print("Numero par")
c=a+b
print(c)