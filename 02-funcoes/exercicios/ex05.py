def palindromo(texto):

    # Deixar minúsculo e retirar espaços
    texto = texto.lower()
    texto = texto.replace(" ", "")

    # Verifica se o texto é igual ao seu oposto
    return texto == texto[::-1]
    
texto_usuario = input("Digite uma palavra ou frase: ")

# Verifica se é um palíndromo
if palindromo(texto_usuario):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
