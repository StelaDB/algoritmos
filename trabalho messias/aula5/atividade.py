#utilizando operadores lógicos
#lendo os lados de um Triângulo
a=int(input("Primeiro lado do triângulo: "))
b=int(input("Segundo lado do triângulo: "))
c=int(input("Terceiro lado do triângulo: "))
#testando se os lados formam um triângulo
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print("triângulo equilátero ")
    elif a==b or a==c or c==b:
        print("Triângulo isóceles ")
    else:
        print("Triângulo escaleno ")
else:
    print("não é um Triângulo")