#programa que apresenta a menor, a maior e a media das temperaturas em graus celsius
a=[]
for i in range(10):
    a.append(float(input(f"Digite a {i+1}ª termperatura em graus celsius: ")))
a.sort #ordena em ordem crescente
print("A menor temperatura é: ",a[0])
print("A maior temperatura é: ",a[9])
print("A média da temperaturas é: ", sum(a)/10)