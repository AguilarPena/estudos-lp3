pontuacao_usuario = float(input("Informe sua pontuação escolar na escala de 0 a 100: "))

def converter_nota(pontuacao):
    
    # Converter cada pontuação numérica para conceitos 
    if pontuacao >= 90:
        return "A"
    elif pontuacao >= 80:
        return "B"
    elif pontuacao >= 70:
        return "C"
    elif pontuacao >= 60:
        return "D"
    else:
        return "F"

nota = converter_nota(pontuacao_usuario)
print(f"O conceito escolar correspondente à pontuação informada é: {nota}")