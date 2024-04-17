from collections import Counter

frase_usuario = input("Digite uma frase sem acentuações: ")

def contar_vogais_consoantes(frase):
    vogais = 'aeiou'
    
    # Deixar minúsculo e retirar os espaços
    frase = frase.lower()
    frase = frase.replace(" ","")

    # Conta quantas vezes cada caracter aparece na frase
    contador = Counter(frase)
    # Conta a quantidade de vogais e soma
    qtd_vogais = sum(contador[c] for c in vogais)
    # Conta a quantidade de consoantes subtraindo os caracteres totais da quantidade de vogais
    qtd_consoantes = len(frase) - qtd_vogais

    return qtd_vogais, qtd_consoantes

vogais, consoantes = contar_vogais_consoantes(frase_usuario)
print(f"Quantidade de vogais: {vogais}")
print(f"Quantidade de consoantes: {consoantes}")
