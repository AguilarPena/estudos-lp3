# Exercício 03: Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:

# entre R$ 0,01 e R$ 9,99 - 0% de desconto
# entre R$ 10,00 e R$ 99,99 - 5% de desconto
# entre R$ 100,00 e R$ 499,99 - 10% de desconto
# compras superiores a R$ 500,00 - 15% de desconto

valorcompra = float(input('Informe o valor da compra: '))

if valorcompra >= 0.01 and valorcompra <= 9.99:
    print('O desconto aplicado é de 0%')
    print('O valor final da compra é ', valorcompra)
elif valorcompra >= 10 and valorcompra <= 99.99:
    print('O desconto aplicado é de 5%')
    print('O valor final da compra é ', (valorcompra-valorcompra*5/100))
elif valorcompra >= 100 and valorcompra <= 499.99:
    print('O desconto aplicado é de 10%')
    print('O valor final da compra é ', (valorcompra-valorcompra*10/100))
elif valorcompra > 500:
    print('O desconto aplicado é de 15%')
    print('O valor final da compra é ', (valorcompra-valorcompra*15/100))   