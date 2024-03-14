#LENDO OS VALORES DE A B E C
a=float(input("Primeiro valor:"))
b=float(input("Segundo valor:"))
c=float(input("Terceiro valor:"))
#calculando o delta
delta=b**2-4*a*c
x1=(-b+delta**(1/2))/2*a
x2=(-b-delta**(1/2))/2*a
if a!=0 and b!=0 and c!=0:
    if delta>0:
        print("As raízes da equação são:",x1,"e",x2)
    
    if delta==0:
        print("A raíz desta equação é",x1,x2)
    
    if delta<0:
        print("Esta equação não possui raízes reais")
else:
    print("Esta equação não é do segundo grau")