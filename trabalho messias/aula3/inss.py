vh=int(input("valor que você ganha por hora:"))
nt=int(input("coloque o número de horas trabalhadas:"))
inss=int(input("coloque o percentual de desconto:"))
sb=vh*nt
sl=sb-sb(sb*inss/100)
print("seu saldo líquido é:", sl)