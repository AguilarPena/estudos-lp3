import random

numero = random.randint(1, 100)

palpite = int(input("Faça um palpite de um número entre 0 e 100 : "))

def verifica_palpite (palpite):

    # Informar ao usuário se valor está alt ou baixo
    if (palpite > numero):
        print("O número está alto")
    elif (palpite < numero):
        print("O número está baixo")
    else:
        print("Parabéns, você adivinhou o número!")

print(verifica_palpite(palpite))

# Verifica se palpite está certo      
while True:
    palpite = int(input("Faça um palpite de um número entre 0 e 100: "))
    verifica_palpite(palpite)
    if palpite == numero:
        break