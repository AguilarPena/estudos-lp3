# For (ir do zero até o final)
# se quiser ir de par em par no vetor usa range 

palavra ='python'
for letra in palavra:
    print(letra)

numeros = [1, 3, 4, 6, 8]
for numero in numeros:
    print(numero)

#estudante1@debian:~$ python3
#Python 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] on linux
#Type "help", "copyright", "credits" or "license" for more information.
#>>> range(5)
#range(0, 5)
#>>> list(range(5))
#[0, 1, 2, 3, 4]

# range 
# range(stop)
# range(5) - 0,1,2,3,4

# range (start, stop)
# range(4,10) - 4, 5, 6, 7, 8, 9

# range(start, stop, step)
# range (3,10,2) - 3,5,7,9

for i in range(10):
    print(i)

# lista = list(range(1001)) - gera numeros até 1000
# type(5) - retorna o tipo

# While

contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Break
# break pula o loop
# imprimir o primeiro numero par

numeros = [1, 3, 3, 4, 6]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break

# Continue
# pula a interação

for numero in numeros:
    if numero <= 0:
        continue
    print(numero)
    
for numero in numeros:
    if numero > 0:
        print(numero)
        
# Compreensao de lista

numeros = [2, 3, 4]
quadrados = []

for numeros in numeros:
    quadrados.append(numero ** 2)
    
# LEMBRE-SE: append acrescente um valor ao fim da lista
# isso é equivalente a seguinte linha:

quadrados = [numero ** 2 for numero in numeros]

numeros = [1, 3, 4, 5, 4, 6]
pares = []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
        
# isso é equivalente a seguinte linha:
        
pares = [numero for numero in numeros if numero % 2 == 0]   

# exemplo: deixar tudo em maiúsculo

palavras = ['ola', 'mundo', 'teste']

# criar uma nova lista
palavras2 = [palavra.upper() for palavra in palavras]