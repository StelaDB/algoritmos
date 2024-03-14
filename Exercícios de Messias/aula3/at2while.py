#tabuada de uma multiplicação de um número
while True:
    n = int(input("Digite um numero pra ver a tabuada: "))
    print("Tabuada de uma multiplicação de um numero", n)
    i = 1
    while i <= 10:
        print(n, "x", i, "=", n*i)
        i += 1
    continua=input("Deseja continuar? (sim/nao)")
    if continua=="nao":
        break