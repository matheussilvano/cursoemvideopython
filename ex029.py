v = float(input('Qual a velocidade do carro? '))
pm = (v * 7) - 560
if(v > 80):
    print('A velocidade está acima do limite, a multa é de R${:.2f}.'.format(pm))
else:
    print('A velocidade está dentro do limite.')