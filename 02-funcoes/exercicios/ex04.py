def simulador_eleicoes():
    candidatos = ["Candidato 1", "Candidato 2", "Candidato 3"]
    votos = [0, 0, 0]

    # Menu de escolha dos cantidatos
    while True:
        print("Escolha um candidato (ou digite 0 para encerrar a votação):")
        print("1. Candidato 1")
        print("2. Candidato 2")
        print("3. Candidato 3")
        escolha = input("Digite o número do candidato desejado: ")
        
        # Registro dos votos 
        if escolha == '0':
            break
        elif escolha in ['1', '2', '3']:
            indice = int(escolha) - 1
            votos[indice] += 1
            print("Voto registrado para", candidatos[indice])
        else:
            print("Opção inválida!")

    # Exibir quantidade de votos para cada candidato
    print("\nResultado da votação:")
    for i in range(len(candidatos)):
        print(f"{candidatos[i]}: {votos[i]} votos")

    vencedor = candidatos[votos.index(max(votos))]
    print("\nO vencedor é o ", vencedor)


# Executando o simulador de eleições
simulador_eleicoes()