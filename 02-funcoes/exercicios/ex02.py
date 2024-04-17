def tabuada(numero):

    # For multiplica cada numero informado pela sequência numérica da tabuada (de 0 10)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

try:
    numero = int(input("Informe um número inteiro: "))
    tabuada(numero)
    
# Em caso de números não inteiros
except ValueError:
    print("Por favor, digite um número inteiro válido.")
