# Anotações Gerais sobre Python
"""
Observações:
- [Ctrl + /] serve para para colocar/tirar todas as linhas com # selecionadas de uma vez
- [Ctrl + Click em algo] abre um documento de help do PyCharm sobre isso que foi clicado
"""
# ---------------------------- 1. dir ----------------------------
# Serve para mostrar quais funções ou métodos estão disponíveis para tais variáveis/dados.
"""
-----Sintaxe/Exemplo-----
x = "string"
dir(x)  # esse comando irá mostrar todos os atributos/métodos que podem ser usados com x

y = 1
print(dir(y))
"""

# ---------------------------- 2. help ----------------------------
# Mostra o que é, como funciona e o que pode ser usado na variável/método/atributo determinado.
"""
-----Sintaxe/Exemplo-----
x = [0, 1, 2]
help(x)  # abrirá uma página mostrando detalhadamente tudo que pode ser usado com o x

# Tanto dir quanto help podem também ser usados direto no console.
"""
# ---------------------------- 3. Divisão de Strings (slice e split) ----------------------------
# As strings também funcionam como uma lista (com cada letra/espaço/símbolo tendo um índice), mesmo que pareçam
# concretas.
"""
----Exemplos com Slice e Split de Strings-----
variavel = "nome composto"

print("# Slice:  # funciona também com listas e tuplas")
print(variavel[0:4])  # vai printar as letras/espaços/símbolos que estiverem de 0 a 3
print(variavel[5:13])
print(variavel[::-1])  # vai printar a string invertida *pythônico
# no geral, pode escrever também x: quando quer de um índice até o final ou :x quando quer do começoaté um ponto.

print("\n# Split")
nova_variavel = variavel.split()  # o split transforma string em uma lista de fato, de acordo com seu'argumento'
print(nova_variavel)  # argumento vazio = split no backspace, mas podem ser definidos outros símbolos também
print(nova_variavel[0])
print(nova_variavel[1])
"""

# ---------------------------- 4. Atributos de String ----------------------------

# 4.1 join
# Faz o contrário do split, atribui carácteres entre elementos de uma lista para formar uma string.
"""
-----Sintaxes/Exemplos-----
lista = ["Faz", "o", "contrário", "do", "split"]
variavel = " ".join(lista)
print(lista)
print(variavel)
"""

# 4.2 replace
# Substitui letras/espaços/símbolos por outras letras/espaços/símbolos.
"""
-----Sintaxes/Exemplos-----
variavel = "nome composto teste"
nova_variavel = variavel.replace(" ", ", ")
print(nova_variavel)
print(variavel.replace("o", "0"))
"""

# ---------------------------- 5. Uso do is como "pergunta" ----------------------------
# O is também pode ser usado como uma pergunta, onde ele verifica se a condição é True ou False.
"""
-----Sintaxes/Exemplos-----
print("# Exemplo is puro")
variavel = True
outra_variavel = False

print(variavel is True)  # é como se fosse 'a variável é True?'; o que printar vai ser a resposta dessa pergunta
print(variavel == True)  # aqui funciona da mesma forma
print(outra_variavel is True)

print("\n# Exemplo is + atributos")
# capitalize = só a primeira letra da frase é maiúscula; title = todas as primeiras letras da frase são maiúsculas
nome = "Morango"  # está capitalize e title
outro_nome = "banana"  # está lower
mais_um_nome = "Batata Frita"  # está title

print(nome.istitle())
print(outro_nome.istitle())
print(outro_nome.islower())
print(mais_um_nome.istitle())
print(mais_um_nome.isupper())
# não existe iscapitalize
"""

# ---------------------------- 6. Uso do in ----------------------------

# 6.1 in como "pergunta"
# Assim como o is, o in também pode ser usado como uma pergunta, verificando também se a condição é True ou False.
# Funciona em: listas, tuplas, dicionários (procurando as chaves) e conjuntos
"""
-----Sintaxe/Exemplo-----
dicionario = {"born": 1989}
print("born" in dicionario)
"""

# 6.2 for ... in
# "Para o que tiver dentro dessa variável/lista, faça..."
"""
-----Sintaxes/Exemplos-----
variavel = "nome composto"
lista = [1, 2, 5, 3]

for letra in variavel:
    print(letra)

for numeros in lista:
    print(numeros)

soma = " "    
lista_strings = ["n", "o", "m", "e", " ", "c", "o", "m", "p", "o", "s", "t", "o"]
for letras in lista_strings:
    soma += letras
print(soma)
"""

# 6.3 if ... in
# "Se tiver x coisa dentro dessa variável/lista, faça..."
"""
-----Sintaxes/Exemplos-----
variavel = "nome composto"
lista = [1, 2, 5, 3]

if "o" in variavel:
    print("Tem essa letra na string.")
else:
    print("Não tem essa letra na string.")

if 6 in lista:
    print("Tem esse número na lista.")
else:
    print("Não tem esse número na lista.")
"""

# 6.4 enumerate
# O enumerate serve para criar como se fosse uma lista com a variável que o for vai verificar.
# Funciona em: listas, tuplas, dicionários (considerando o valor como índice) e conjuntos
"""
-----Sintaxes/Exemplos-----
variavel = "nome composto"

for i in enumerate(variavel):  # se tiver só um argumento, vai printar exatamente como o enumerate se apresenta
    print(i, end=" ")
print()
for indice, letra in enumerate(variavel):
    print(indice, end=" ")
print()
for indice, letra in enumerate(variavel):
    print(letra, end=" ")
for indice, letra in enumerate(variavel):
    print(indice, letra)

print("# Outro exemplo")
dicionario = {"a": 1, "b": 2, "c": 3}
for indice, numero in enumerate(dicionario):
    print(indice, numero)
"""

# ---------------------------- 7. Atributos gerais de Coleções ----------------------------
# *Nem todas funcionam com todas as coleções

# 7.1 list/tuple
# Criação de listas/tuplas a partir de range ou até mesmo strings. Pode ser usado também para transformar listas em
# tuplas e vice-versa.
# Funciona em: listas, tuplas
"""
-----Sintaxes/Exemplos-----
tupla = tuple(range(4))
lista = list(range(5, 10))
outra_lista = list("nome composto")
outra_tupla = tuple(lista)

print(tupla)
print(lista)
print(outra_lista)
print(outra_tupla)
"""

# 7.1.1 set
# O set pode ser usado para criar um conjunto a partir de uma lista ou tupla já existente
"""
-----Sintaxes/Exemplos-----
lista = [1, 2, 2, 3, 4, 5, 7, 5, 4, 6]
tupla = (1, 2, 2, 3, 4, 5, 7, 5, 4, 6)
dicio = {"teste": 1, "teste2": 1, "teste3": 1, "teste4": 2}
print(set(lista))
print(set(tupla))
print(set(dicio.values()))
print(set(dicio))  # como as chaves de um dicionário não podem ser repetidas, então o set de chaves sempre retornará
# todas as chaves do dicionário em questão
"""

# 7.2 count
# Conta quantas vezes um valor/elemento aparece dentro de uma lista. Funciona com string também, já que é uma "lista".
# Funciona em: listas, tuplas
"""
-----Sintaxe/Exemplo-----
variavel = "nome composto"
tupla = (8, 88, 8, 9, 10, 8, False)
print(tupla.count(8))
print(variavel.count("o"))
"""

# 7.3 pop
# Remove através de índice/chave e retorna o elemento removido de uma coleção. Se a coleção não chegar a esse índice,
# vai dar indexError (lista), keyError (dicionários) ou typeError (conjuntos, porque é aleatório então não tem argumento
# pro atributo nesse caso).
# Funciona em: listas (ou o último elemento ou o do índice existente indicado), dicionários (sempre informando a chave)
# e conjuntos (aleatoriamente).
"""
-----Sintaxes/Exemplos-----
lista = [7, 6, 9, 32, 643, True, 9.6]
dicionario = {"singer": "Taylor Swift", "gender": "female", "born": 1989, 6:"reputation"}

print(lista)
lista.pop(4)
print(lista)

print(dicionario)
removido = dicionario.pop("born")
print(dicionario)
print(removido)
"""

# 7.4 clear
# Remove todos os elementos de uma coleção.
# Funciona em: listas, dicionários e conjuntos
"""
-----Sintaxe/Exemplo-----
dicionario = {"singer": "Taylor Swift", "gender": "female", "born": 1989, 6:"reputation"}

print(dicionario)
dicionario.clear()
print(dicionario)
"""

# 7.5 index
# Serve para, através de uma procura pelo elemento, mostrar em que índice ele se encontra. Se o elemento não existir,
# vai dar ValueError.
# Funciona em: listas, tuplas
"""
-----Sintaxe/Exemplo-----
lista = [7, 6, 9, 32, 643, True, 9.6]
tupla = (8, 88, 8, 9, 10, 8, False)

print(lista)
print(tupla)
print(lista.index(9))  # "Em que índice se encontra o número 9 nessa lista?"
print(tupla.index(8, 0))  # "E o número 8 nessa tupla a partir do índice 0?"
print(tupla.index(8, 1, 6))  # "E o número 8 nessa tupla incluindo do índice 1 ao 5?"
"""
# 7.6 sum, max, min, len
# Servem para mostrar a soma dos elementos, o maior valor, o menor valor e o tamanho da coleção, respectivamente.
# Funciona em: listas, tuplas, dicionários (as operações podem ser feitas tanto com as chaves quanto com os valores (
# pelo .values()), desde que sejam números) e conjuntos
"""
-----Sintaxe/Exemplo-----
lista = [7, 6, 9, 32, 643, True, 9.6]
tupla = (8, 88, 8, 9, 10, 8, False)
dicionario = {"singer": "Taylor Swift", "gender": "female", "born": 1989, 6:"reputation"}
conjunto = {4, 5, 9, 1}

print(sum(lista))  # só em coleções com strings não funciona
print(max(dicionario))
print(min(tupla))
print(len(conjunto))

print("\nExemplo com Dicionário:")
dicio = {1: 10, 2: 20, 3: 30}
print(sum(dicio))
print(max(dicio))
print(min(dicio))
print(len(dicio))
print()
print(sum(dicio.values()))
print(max(dicio.values()))
print(min(dicio.values()))
print(len(dicio.values()))
"""

# 7.7 Atributos de cópia de lista

# 7.7.1 Deep Copy
# Usando o copy, as mudanças na nova lista não são realizadas na lista antiga.
# Funciona em: listas, dicionários e conjuntos
"""
-----Sintaxe/Exemplo-----
lista = [1, 2, 3]
outra_lista = [4, 5, 6]

outra_lista = lista.copy()
outra_lista.append(7)
print(lista)
print(outra_lista)
"""

# 7.7.2 Shallow Copy
# As duas listas são atualizadas simultaneamente.
# Funciona em: listas, dicionários e conjuntos
"""
-----Sintaxe/Exemplo-----
lista = [1, 2, 3]
outra_lista = [4, 5, 6]

nova_lista = lista
print(lista)
print(nova_lista)
lista.append("adicionando na velha")  # obs: esse append de teste só funciona em listas
nova_lista.append("adicionando na nova")
print(lista)
print(nova_lista)
"""

# ---------------------------- 8. Desempacotanto Coleções ----------------------------
# Funciona em: listas, tuplas e conjuntos
"""
-----Sintaxe/Exemplo-----
cesta = ("banana", 5)
fruta, quantidade = cesta
print(fruta)
print(quantidade)
"""
