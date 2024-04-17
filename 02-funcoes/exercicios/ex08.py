def contar_palavras(frase):
    
    contagem = {}
    
    # Divide a frase em palavras separadas por espaço
    palavras = frase.split()
    
    for palavra in palavras:
        # Se a palavra já existir no dicionário, incrementa o contador
        if palavra in contagem:
            contagem[palavra] += 1
        # Senão, significa que é uma nova palavra, então acrescenta-se a palavra no dicionário
        else:
            contagem[palavra] = 1

    return contagem

# Teste com o texto do usuário
texto = input("Digite uma frase: ")
resultado = contar_palavras(texto)
print(resultado)
