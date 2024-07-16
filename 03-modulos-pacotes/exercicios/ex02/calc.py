def imc(peso, altura):
    return peso/(altura**2)

def classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif (imc > 18.5 and imc < 24.9):
        return "Peso adequado"
    elif (imc > 25,0 and imc < 29,9):
        return "Excesso de peso"
    elif (imc > 30,0 and imc < 34,9):
        return "Obesidade Classe 1"
    elif (imc > 35,0 and imc < 39,9):
        return "Obesidade Classe 2"
    else:
        return "Obesidade Classe 3"

def peso_ideal(altura):
    return 24.9 * (altura ** 2)