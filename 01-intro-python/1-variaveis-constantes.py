# Identificadores: identificam variáveis

# não pode usar: letra, numero e _
# palavras reservadas: def, if, for

# python é case sensitive
nome = "Jão"
Nome = "Jão"

# no java: tipo de identificador = valor (literal)
# no java: float altura = 1.8f;

# no python: tipo de identificador = valor (literal) 
# no python: altura = 1.8

# obs: python tem tipo, mas não precisa ser definido
# tipagem dinâmica

# Constantes: letras maiúsculas (convenção)
pi = 3.14
PI = 3.14 

# hastag para comentários de linha única

"""
aspas para comentários de multiplas linhas 
"""

# docstring
# documentação de códigos, funções, classes, módulos
# o python obriga a identação do código

def somar(n1, n2):


#Função que soma dois números

#:param n1: primeiro número
#:param n2: segundo número
#:return: a soma de parâmetros

    return n1 + n2

somar(10.2, 20.5)