import random

# Função que define palavras e escolhe uma aleatória
def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogo", "desenvolvimento"]
    return random.choice(palavras)

def jogar():
    palavra = escolher_palavra()
    letras_corretas = set(palavra)
    tentativas = 6
    letras_descobertas = set()

    print("Bem-vindo ao jogo de Forca!")

    # Verifica se letras digitadas estão na palavra oculta
    while tentativas > 0:
        palavra_oculta = ''.join(letra if letra in letras_descobertas else '_' for letra in palavra)
        print(palavra_oculta)

        palpite = input("Digite uma letra ou a palavra completa: ").lower()

        # Verifica se palavra ou letras estão corretas
        if palpite == palavra:
            print("Parabéns! Você adivinhou a palavra.")
            break
        elif palpite in letras_corretas:
            letras_descobertas.add(palpite)
            if letras_descobertas == letras_corretas:
                print("Parabéns! Você adivinhou a palavra.")
                break
        # Subtrair quantidade de tentativas
        else:
            tentativas -= 1
            print("Essa letra não está na palavra. Você tem {} tentativas restantes.".format(tentativas))

    if tentativas == 0:
        print("Game over! A palavra correta era '{}'.".format(palavra))

jogar()
