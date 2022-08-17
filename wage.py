wage = float (input('Quanto você recebe? '))
increase = int (input('Quanto porcento de aumento?'))
value = float (wage + (wage * increase / 100))
print (f'Seu antigo salário era R$ {wage}, o seu novo salário é R$ {value:.2f}!')