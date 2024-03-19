# Tipos de dados
# int, float
# string, list, tuple, set
# dict
# None

# int
idade = 20
temperatura = -30

# float
altura = 1.55
PI = 3.14

# string
nome = 'Marie de Silve'
nome = "Maria da Silva"

# não tem char no pyton, é apenas uma forma de declarar char, pois ele é uma string de um caracter
letra = 'A'
letra = 'a'

# obs: é possível acessar cada caracter de uma string, como um array 

print(nome[0]) # acessa um caracter específico 
print(nome[-1]) # acessa um caracter espeífico, última posição
print(nome[0:3]) # vai do caracter 0 até 3

# nome é um objeto da classe string 
# string tem atibutos e métodos, logo nomes têm métodos

print(nome.capitalize())
print(nome)

# interpolação (?) de strings e variáveis
# f-string - isso é interpolar

nome = "Jão"
idade = 22
mensagem = f"Olá {nome}. Votê tem {idade} anos"
print(mensagem)

# list - lista de valores (preferencialment do mesmo tipo) que pode ser alterada
# habilidades = []

habilidades = ['java', 'c#', 'css']
print(habilidades[0])
print(habilidades[2])

habilidades[0] = 'javascript'

habilidades.append('html') #append acrescenta um objeto ao final da lista
habilidades.insert(0, 'kotlin') # insert acrescenta um objeto em um espaço/caractere específico da lista
print(habilidades)

# set - conjunto não indexado que não permite elementos duplicados

# "digite os emails de destino"
# maria@email.com, joao@email.com, maria@email.com

emails = {'maria@email.com', 'joao@email.com', 'maria@email.com'}
emails.add('maria@email.com')
emails.add('pedro@email.com')
print(emails)

# usado quando não se tem controle do que o usuário pode informar

# tuple - 'lista' de valores que NÃO podem ser alterados (adicionar, remoer...) 
# pensada para situações em que não haverá mudanças no espaço de memórias

opcoes = ('sim', 'nao', 'talvez')

# for

for opcao in opcoes:
    print(opcao)

for habilidades in habilidades:
    print(habilidades)

# dict - dicionário (chave: valor / key: value)

# exemplo - site de emprego

empresa = 'Google'
titulo = 'Engenheiro de Software'
salario = 2000.00
remoto = False

# na realidade são caracteristicas de uma vaga, então podemos agrupar em um grande "identificador"

vaga = {
'empresa' : 'Google',
'titulo' : 'Engenheiro de Software',
'salario' : 2000.00,
'remota' : False
}

print(vaga['salario'])
print(vaga['titulo'])

# None - corresponde ao nulo

nome = None