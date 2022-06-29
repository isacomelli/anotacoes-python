# Anotações sobre Coleções em Python
"""
Observações:
- [Ctrl + /] serve para para colocar/tirar todas as linhas com # selecionadas de uma vez
- [Ctrl + Click em algo] abre um documento de help do PyCharm sobre isso que foi clicado
"""
"""
As listas são o tipo de coleção mais versátil, tudo pode ser aplicado nelas. Porém, ainda existem as tuplas (tuple), 
os dicionários (dict), os conjuntos (set) e outras collections. Nessa sessão de anotações vão ser abordadas 
características e vantagens de cada uma delas.
"""
# ---------------------------- 1. listas ----------------------------

# Atributos específicos:
# 1. sort: Coloca a lista na ordem. Listas com strings não fazem sort se tiverem números ou booleanos junto.
# 2. reverse: Inverte a ordem da lista. Aquele "elemento[::-1]" que inverte strings também funciona com listas.
"""
-----Sintaxes/Exemplos-----
lista_frutas = ["babana", "Maçãs", "Morango"]
lista_kgs = [5, 4, 1.5, True]
lista_aleatorios = ["$", "#", " "]

lista_kgs.sort()
print(lista_kgs)
lista_kgs.reverse()
print(lista_kgs)

lista_tudo = lista_frutas + lista_aleatorios
print(lista_tudo)
lista_tudo.sort()
print(lista_tudo)
"""

# 3. append e extend
# O append adiciona dados a uma lista, sendo eles números ou coleções. Porém, caso seja uma coleção, seus valores não
# poderão ser acessados por um índice "linear", e sim como se fosse de uma matriz. É como se fosse adicionar uma caixa
# cheia de objetos dentro de uma caixa maior, não os objetos diretamente.
# Nesse caso, quem adiciona os objetos diretamente é o extend, que funciona como se fosse um nova_lista = lista + lista.
"""
-----Sintaxes/Exemplos-----
lista_frutas = ["babana", "Maçãs", "Morango"]
tupla_frutas = ("limão", "uva")
conjunto_frutas = {"maracujá", "kiwi"}

lista_frutas.extend(tupla_frutas)
print(lista_frutas)
lista_frutas.append(conjunto_frutas)
print(lista_frutas)
"""

# 4. insert
# Adiciona elementos à uma coleção escolhendo qual índice ela vai ocupar, sem substituir o valor que estava nesse índice
# antes.
"""
-----Sintaxe/Exemplo-----
lista = [5, 10, 15]

print(lista)
print(lista[1])
lista.insert(1, "novo valor")
print(lista)
print(lista[1])
print(lista[2])
"""

# ---------------------------- 2. tuplas ----------------------------

# Características:
# - Representadas pelo ().
# - Não podem ser alteradas, são imutáveis, ou seja, não se pode adicionar, remover e nem substituir por novos valores
# nelas.
# - São mais rápidas e seguras que as listas.
# - São interessantes para serem utilizadas como chaves de dicionários.
# - São usadas quando não precisamos alterar os valores de uma coleção.
# - Seus valores podem ser acessados pelo índice.

# Por mais que sejam representadas pelos (), sua criação é definida pelas vírgulas, como pode ser visto abaixo:
"""
tupla = (1, 2, 3)

print(tupla)
outra_tupla = 4, 5,  # também podem ser montadas dessa forma
print(outra_tupla[1])

duvida_tupla = (6)  # se conter somente um número, vai ser uma variável int, não uma tupla
print(f"duvida_tupla é: {type(duvida_tupla)}")

outra_duvida_tupla = (7,)  # porém, se conter uma vírgula, vai ser tupla
print(f"outra_duvida_tupla é: {type(outra_duvida_tupla)}")

# Ou seja:
# (1) = int
# 1, = tupla
# (1,) = tupla 
"""

# Elas não podem ser alteradas, então atributos de adição e remoção não funcionam com tuplas. Porém, elas podem ser
# concatenadas e sobrescritas sem acontecer Shallow Copy (já que não podem ser alteradas):
"""
-----Sintaxes/Exemplos-----
tupla = (1, 2, 3)
outra_tupla = ("oi", "tchau")
nova_tupla = tupla + outra_tupla  # concatenando
tupla = outra_tupla  # sobrescrevendo
print(nova_tupla)
print(tupla)
"""

# ---------------------------- 3. dicionários/mapas (dict) ----------------------------

# Características:
# - Representados por {chave:valor}. As chaves e os valores podem ser de qualquer tipo de dado.
# - Seus valores não podem ser acessados pelo índice, e sim pelas chaves.
# - As chaves não podem ser repetidas.
# - As coleções ficam mais detalhadas e definidas.

"""
dados = {"singer": "Taylor Swift", "gender": "female", "born": 1989}
mesmo_dicionario = dict(singer="Taylor Swift", gender="female", born=1989)
"""
# os dois são iguais, mas o segundo funciona como se fosse com variáveis em vez de definir o tipo exato como no
# primeiro. O python mesmo detecta.
"""
print(dados)
print(mesmo_dicionario)
"""

# Valores sendo são acessados pelas chaves:
"""
print(dados["singer"])  # "Seco": se a chave não existir, vai dar keyError
print(dados.get("album"))  # Por isso, o get é mais recomendado para acessar valores, pois dará None em vez de erro
print(dados.get("album", "Esse dado não foi encontrado."))  # Retorna essa mensagem se não encontrar essa chave

print("singer" in dados)
print(1989 in dados)
"""

# for i in dicio: O que vai printar com print(i)?
"""
-----Sintaxe/Exemplo-----
for i in dados:
    print(i)  # vai printar as chaves
print()
for i in dados:
    print(dados[i])  # vai printar os valores
"""

# Usando os atributos keys e values, esses processos acima podem ser feitos de outra maneira
"""
print(dados.keys())  # para printar as chaves
print(dados.values())  # para printar os valores
"""

# Adicionando/Atualizando elementos (possuem a mesma sintaxe):
"""
dados["last_album"] = "evermore"  # Forma mais comum

# Usando o update:
novo_dado = {"best_album": "reputation"}

dados.update(novo_dado)
dados.update({"most_popular_album": "1989"})

print(dados)
"""

# Para remover elementos, além do pop (que é mais comum), pode ser usado o del:
"""
del dados["most_popular_album"]  # Nesse modo o valor não é retornado e se a chave não existir, vai dar keyError
print(dados)
"""

# Criando dicionários com fromkeys:
"""
-----Sintaxes/Exemplos-----
outro_dicionario = {}.fromkeys("a", "b")
print(outro_dicionario)

mais_um_dicionario = {}.fromkeys(range(1, 11), "vazio")
print(mais_um_dicionario)

mais_outro_dicionario = {}.fromkeys(["singer", "gender", "born"], "vazio")
print(mais_outro_dicionario)
"""

# O desempacotamento de dicionários é feito com o atributo items:
"""
-----Sintaxe/Exemplo-----
nova_cesta = {"banana": 5, "uva": 4, "pera": 3}
print("\nEm dicionários, o desempacotamento é pelo for:")
for chave, valor in nova_cesta.items():
    print(f"fruta: {chave}, quantidade: {valor}")
"""

# ---------------------------- 3. conjuntos (set) ----------------------------

# Características:
# - Representados pelos {}.
# - Não possuem valores ordenados e nem duplicados.
# - Não são indexados, pois possuem ordem aleatória.

# Adicionando elementos aos conjuntos:
"""
-----Sintaxes/Exemplos-----
conjunto = {3, 6, 9}

conjunto.add(10)
print(conjunto)
conjunto.add(3)  # Como o valor 3 já existe nesse conjunto, ele não será adicionado
print(conjunto)
"""

# Para remover elementos dos conjuntos, além do pop, temos o remove e o discard:
"""
-----Sintaxe/Exemplo-----
conjunto = {3, 6, 9}
conjunto.remove(6)  # se o valor não existir dentro do conjunto, dará keyError
conjunto.discard(66)  # se o valor não existir dentro do conjunto, não vai gerar erro, o python ignora
print(conjunto)
"""

# Teoria dos Conjuntos:
"""
-----Sintaxe/Exemplo-----
conjunto = {3, 6, 9}
outro_conjunto = {6, 9, 12, 15}

# union
print(conjunto.union(outro_conjunto))
print(outro_conjunto | conjunto)

# intersection
print(conjunto.intersection(outro_conjunto))
print(outro_conjunto & conjunto)

# difference
# Deixa somente os números que só tem no primeiro conjunto, removendo tudo que o outro conjunto tem e pode ser comum
print(conjunto.difference(outro_conjunto))
print(outro_conjunto.difference(conjunto))
"""
