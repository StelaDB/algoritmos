#ler cinco elementos em uma lista "a" implicando em o somatório de cada elemneto de "a" em uma lista "b"
a=[]
b=[]
for i in range (5):
    a.append(int(input("Digite um numero: ")))
    somatorio=0
    for j in range(a[i]+1):
        somatorio+=j
    b.append(somatorio)
print(a)
print(b)