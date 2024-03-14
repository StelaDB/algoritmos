#programa que calcula o valor de fatorial
resp="sim"
while resp=="sim":
    n = int (input("Digite um valor:"))
    f=1
    for c in range(1,n+1):
        f*=c
    print("o fatorial de {} é:", format(n), f)
    resp=str(input("Deseja continuar: "))
print("FIM!")