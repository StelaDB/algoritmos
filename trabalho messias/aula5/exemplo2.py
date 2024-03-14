a=float(input("Primeira nota:"))
b=float(input("Segunda nota:"))
c=float(input("Terceira nota:"))
d=float(input("Quarta nota:"))

soma=(a+b+c+d)/4

if soma>=7:
    print("aprovado", soma)
else:
    print("reprovado", soma)
    e=float(input("Nota da prova final:"))
    media=(soma+e)/2
    if media>=5:
        print("aprovado", media)
    else:
        print("reprovado", media)