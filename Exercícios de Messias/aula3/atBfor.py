#tabuada da multiplicação de um numero qualquer com for
while True:
    n = int(input("Digite um numero pra ver a tabuada: "))
    print("Tabuada de uma multiplicação de um numero", n)
    for i in range(1,11):
        print(n, "x", i, "=", n*i)
    continua=input("Deseja continuar? (sim/nao)")
    if continua=="nao":
        break