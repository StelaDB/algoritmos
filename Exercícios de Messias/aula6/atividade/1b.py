#ler 8 elementos de uma matriz e criara uma matris b
a=[]
b=[]
for i in range(0,10):
    a.append(int(input(f"Digite o {i-1} elemento do numero A: ")))
    b.append(a[i]*3)
    b[i]*=a[i]
    print(f"O vetor B é: {b}")