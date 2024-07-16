from calc import imc, classificacao, peso_ideal

#Exercicio 02:

peso = float(input('Informe o seu peso em quilogramas: '))
altura = float(input('Informe a sua altura em metros: '))

imc = imc(peso, altura)
classificacao = classificacao(imc)
            
print("Seu IMC eh: ", imc)
print("Classificacao: ", classificacao)
        
peso_ideal = peso_ideal(altura)
    
if imc > 24.9:
    peso_perder = peso - peso_ideal
    print("Voce precisa perder ", peso_perder, " quilogramas para atingir o IMC adequado")
elif imc < 18.5:
    peso_ganhar = peso_ideal - peso
    print("Voce precisa ganhar ", peso_ganhar, " quilogramas para atingir o IMC adequado")
else:
    print("Voce ja esta dentro da faixa de peso normal.")