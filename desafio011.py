largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = 2
necessario = area / tinta
print ('Seria necessario {}L de tinta para pintar essa parede'.format(necessario))
