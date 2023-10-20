"DICTIONARY"

# O objeto Dictionary em Python é utilizado para armazenar multiplos valores em uma unica variavel em 
# pares (no formato key : value)

# A dictionary em Python é um dos 4 tipos de varaiveis que são utilizados para armazenar coleções de 
# dados

# Criamos uma Dictionary e incializamos seus valores usando as chaves {}. E separemos os pares com 
# dois-pontos

dicionario = {
    "montadora" : "Ford",
    "modelo" : "Mustang",
    "ano" : 1964
}

print(dicionario)

# CARACTERISTICAS

# - São ordenadas: seus valores são ordenados
# - É mutável: é possível alterar, inserir ou remover novos elementos
# - Não permite valores duplicados: não permite valores duplicados sob uma mesma key (valor
# será sobrescrito)
# - Podemos acessar um valor especifico indicado a jey entre colchetes depois do nome do dictionary 
# ou utilizar a função get())
# - Podemos usar a função len() para obter o seu tamanho 
# - Podemos usar o constructor dict(valor) para criar um dictionary
# - Podemos usar a função keys() para obter todas as chaves (key) de um dictionary
# - Podemos usar a função values() para obter todos os valores de um dictionary

dicionario = {
    "montadora" : "Ford",
    "modelo" : "Mustang",
    "ano" : 1964,
    "ano" : 1980
}

print(dicionario)
print(dicionario["modelo"])
print(dicionario.get("montadora"))
print(len(dicionario))
cliente = dict(nome = "Astrogildo", idade = 25, estado = "SP")
print(cliente)
print(cliente.keys())
print(cliente.values())

# - Podemos alterar um valor especifico indicando a key e seu novo valor 
# - Ou podemos usar a função update({key:value}) para alterar um valor especifico
# - Podemos adicionar um novo elemento passando uma nova key e seu valor 
# - Ou podemos usar a função update({key:value}) para adicionar um novo valor (somente 
# se ele não existir)
# - Podemos usar a função pop(key) para remover um elemento 
# - Podemos usar a função popitem() para remover o ultimo elemento

dicionario = {
    "montadora" : "Ford",
    "modelo" : "Mustang",
    "ano" : 1964,
    "ano" : 1980
}
dicionario["ano"] = 2000
print(dicionario)
dicionario.update({"montadora":"Fiat"})
print(dicionario)
dicionario["cor"] = "prata"
print(dicionario)
dicionario.pop("montadora")
dicionario.popitem()
print(dicionario)

# - Podemos navegar pelos elementos de um Dictionary com o comando for-each
# - Mostrar apenas seus valores com a função values() ou apenas suas chaves com a função
# keys()

cliente = dict(nome = "Astrogildo", idade = 25, estado = "SP")
print("Exibindo as cahves do dicionario")
for c in cliente.keys():
    print(c)
print("-" * 40)
print("Exibindo os valores do dicionario")
for c in cliente.values():
    print(c)

# Um dicionario pode conter outros Dictionaries, chamados isto de dicionarios aninhados
# Para acessar um valor especifico, indicamos o dicionario e a key (entre colchetes distintos)
# onde está o valor desejado

clientes = {
    "cliente1" : {"nome" : "Astrogildo", "ano":2000},
    "cliente2" : {"nome" : "Berisvaldo", "ano":2003},
    "cliente3" : {"nome" : "Gumercindo", "ano":1998}
}
print(clientes)
print(clientes["cliente2"]["nome"])
