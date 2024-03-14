a=float(input("Primeira nota:"))
b=float(input("Segunda nota:"))
c=float(input("Terceira nota:"))
d=float(input("Quarta nota:"))

soma=(a+b+c+d)/4

if soma>7:
    print("aprovado",soma)
else:
    print("reprovado",soma)
    