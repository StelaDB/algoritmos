#armazenar a tabuada de um numero informado pelo usuário em uma lista
#exibir a tabuada na tela
a=[]
n=int(input("Digite um numero: "))
for i in range(1,11):
    a.append(n*i)
    print(f"{n} x {i} = {a(i-1)}")