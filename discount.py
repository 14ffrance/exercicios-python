price = float (input('Qual é o preço do produto? '))
discount = int (input('Quantos porcento de desconto? '))
desct1 = float (price - price * discount / 100)
print (f'Este produto está valendo agora R${desct1:.2f} reais')