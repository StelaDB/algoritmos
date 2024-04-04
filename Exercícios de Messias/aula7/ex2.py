#programa que busca um elemento em uma lista sem usar o comando in
lista=[1,2,3,4,5,6,7,8,9,10]
resp="sim"
achou=False
while True:
    n=int(input("Digite um número para buscar na lista: "))
    for i in range(len(lista)):
        if lista[i]==n:
            achou=True
            break
        
    if achou:
        print("O número", n, "foi encontrado na posição", i)
    else:
        print("O número", n, "não foi encontrado na lista")
    
    resp=input("deseja buscar outro número? (sim/nao): ")
    if resp=="nao":
        break
print("Fim do programa")