nome = (input('Qual é seu nome? '))
print (f'Seja bem-vindo {nome}! Obrigado por escolher nosso programa!\n Vamos lá!')
larg = float (input('Qual é a largura da parede? '))
alt = float (input('Qual é a altura da parede? '))
área = larg * alt 
print (f'Sua parede tem a dimensão de {larg} x {alt} e sua área é de {área}m².')
altar = área / 2
print (f'Você precisará de {altar:.1f}l de tinta para pintar a parede por completo!')
