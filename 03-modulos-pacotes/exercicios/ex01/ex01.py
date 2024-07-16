from calc import volume, potencia, filtragem

# Exercíco 01:

comprimento = float(input('Informe a comprimento do aquario em centimetros: '))
altura = float(input('Informe a altura do aquario em centimetros: '))
largura = float(input('Informe a largura do aquario em centimetros: '))


temp_desejada = float(input('Informe a tempera desejada da agua: '))
temp_ambiente = float(input('Informe a temperatura ambiente da agua: '))

volume = volume(comprimento, altura, largura)
print("O volume do aquario eh igual a", volume, "litros")

potencia = potencia(volume, temp_desejada, temp_ambiente)
print("A potencia necessaria do termostato eh de", potencia, "watts")

filtragem = filtragem(volume)
print("A quantidade minima de agua que deve ser filtrada eh de", filtragem, "litros")