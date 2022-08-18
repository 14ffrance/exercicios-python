name = input ('Qual é seu nome? ')
day = float (input('Quantos dias alugou o carro? '))
km = float (input('Quantos KM o carro percorreu? '))
car = 60 * day + 0.15 * km
print (f'O total a se pagar é R${car:.2f}')