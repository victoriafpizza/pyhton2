"TUPLE"

# O objeto Tuple em Python é utilizado para armazenar multiplos valores em uma unica variavel
# A Tuple em Python é um dos 4 tipos de variaveis que são utilizados para armazenar 
# coleções de dados 
# Criamos uma Tuple e incializamos seus valores usando o paranteses ()

frutas = ("maça", "uva", "tomate")
print(frutas)

# CARACTERISTICAS DA TUPLE

# - Possuem indices: seus valores podem ser acessados atraves do indice(inicia em zero)
# - São ordenadas: seus valores etão em uma ordem bem definida, sua ordenação não podem ser 
# alterada
# - É imutavel: não pode sofrer alterações (mudas, inserir ou remover novos itens) depois que 
# for criada
# - Permite valores duplicados: como os valores são acessdaos pelo indice, permite valores duplicados.
# - Podemos usar a função len() para obter o seu tamanho
# - Podemos usar a função count(valor) a quantidade de vezes que o valor é encontrado
# -Pode conter valores de um unico tipo de dado, ou mesmo de varios tipos 

frutas = ("maça", "uva", "tomate", "uva", "kiwi")
print(frutas)
print(len(frutas))
print(frutas.count("uva"))
print(frutas[3])
print(type(frutas))
misto = ("alface", 23, True, 7.33)
print(misto)
print(type(misto))

# Quando criamos uma Tuple e inicializamos com valores, isto é chamado de empacotar uma tuple
# Podemos "desempacotar" os valores de uma Tuple, atribuindo seus valores para um numero igual de v
# variaveis

# Podemos também atribuir os valores apra um nuemro inferior de variaveis se usarmos o * para armazenar
# o restante (sera armazenado no formato de List)

# Caso o * não seja utilizado na ultima variável e sim em outra qualquer (no inicio ou fim), o Python 
# se encarrega de realizar a divisão dos valores

frutas = ("maça", "uva", "tomate")
(a, b, c) = frutas
print(f"{a}\n{b}\n{c}")
(x, *y) = frutas
print(f"{x}\n{y}")
frutas = ("maça", "uva", "tomate", "uva", "kiwi")
(k, *w, z) = frutas
print(f"{k}\n{w}\n{z}")

# Podemos navegar pelos elementos de uma Tuple com o comando for 
frutas = ("maça", "pera", "banana")
for i in range(0, len(frutas), 1):
    print(frutas[1])

# Outra opção é utilizar o for-each
frutas = ("maça", "pera", "banana", "kiwi")
for i in frutas :
    print(i)