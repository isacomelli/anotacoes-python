# Anotações sobre None
"""
Observações:
- [Ctrl + /] serve para para colocar/tirar todas as linhas com # selecionadas de uma vez
- [Ctrl + Click em algo] abre um documento de help do PyCharm sobre isso que foi clicado
"""
# O tipo None é um tipo sem tipo. Ele não é vazio, ele só é sem tipo. Ele serve para quando é necessário criar uma
# variável sem um tipo ou valor final. É melhor trabalhar com None do que o código retornar algum erro.

# Exemplos soltos com o None:
"""
-----Sintaxes/Exemplos-----
frutas = dict(ban="banana", mor="morango", lim="limão")

print("# get com dicionário")
print(frutas["ban"])  # Nesse método de encontrar o valor, se a chave não existir, vai dar keyError
print(frutas.get("lar"))  # Com o get é retornado None em vez de keyError se a chave não existir

print("# if")
fruta = frutas.get("lar")  # = None
if fruta:
    print(f"Encontrei {fruta}!")
else:
    print("Não encontrei a fruta...")  # None retorna False
print("\n# Nas anotações sobre Coleções há uma forma de retornar uma frase sem precisar da estrutura do if. 

fruta = frutas.get("mor")  # = morango
if fruta:
    print(f"Encontrei {fruta}!")  # pega o valor armazenado na chave correspondente
else:
    print("Não encontrei a fruta...")
"""
