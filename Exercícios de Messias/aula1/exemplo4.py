#programa com o mesmo intuito do exemplo 3, a diferença é que só roda até o usuário querer e não infinitamente

resposta="sim"
while resposta=="sim":
    x=int(input("Digite um número:"))
    r=x*3
    print(r)
    resposta=input("Deseja continuar:")
    if resposta!="sim":    #se colocar o "Sim" com letra maiuscula não irá ler pois python é case sensitive
        break
print("Fim do programa!")