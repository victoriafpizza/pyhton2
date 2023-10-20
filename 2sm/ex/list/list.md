"LIST"

# O objeto List em Python é utilizado para armazenar múltiplos valores 
# em uma única variável.
# O List em Python é um dos 4 tipos de variáveis que são utilizados para 
# armazenar coleções de dados (outros tipos veremos futuramente).
# Criamos um List e inicializamos seus valores usamos o colchetes [ ]. 
# Exemplo:

frutas = ["maça","uva","tomate"]
print(frutas)

# O list em Python ordena seus valores por indices (começando em 0)
# Não possui um tamanho fixo (seu tamanho muda de acordo com os elementos 
# que possui)

# Os valores de um List podem ser duplicados, ja que o acesso a eles é pelo 
# indice. Para verificar o tamanho de um List utilizamos a função len(). Para
# adicionar novos valores em um LIst ja existente utilizamos a função append()

# Podemos ter List de tipos diversos de dados e inclusive List com elementos dos 
# mais variados tipos 

frutinhas = ["maça","uva","tomate"]
numeros = [21, 45, 73, 12, 45, 1, 45]
logicos = [True, True, False, True]
misto = ["Lero-Lero", True, 23, "Geronimo", 4.77]
print(frutas, numeros, logicos, misto)

# Podemos verificar se um elemento existe em um List com o comando if em conjunto com
# o comando in

frutas = ["maça", "uva", "kiwi", "cereja", "pera", "manga"]
if "cereja" in frutas :
    print("sim somos cerejas")

# Podemos inserir um novo elemento no List em uma posição especifica com a função 
# insert() e o indice onde desejamos incluir o elemento 

frutas = ["maça", "uva", "kiwi"]
frutas.insert(1,"banana")

# Outra forma de remover um elemento de um List é utilizando a função pop() e indicar
# seu indice

frutas = ["maça", "pera", "banana", "kiwi"]
frutas.pop(2)
print(frutas)

# Se utilizar a função pop() sem indice ele irá remover o ultimo elemento do List

frutas = ["maça", "pera", "banana", "kiwi"]
frutas.pop()
print(frutas)

# Podemos ordenar os elemetnos de um list com a funaõ sort()
frutas = ["maça", "pera", "banana", "kiwi"]
frutas.sort(2)
print(frutas)

# A função sort também funciona com List numerico 

frutas = [50, 10, 15, 20]
frutas.sort()
print(frutas)

# Para ordenar de forma descentes os elementos de um List com a função sort()
# usamos o argumento reverse (indicando seu valor como True)

frutas = ["maça", "pera", "Banana", "kiwi"]
frutas.sort(reverse = True)
print(frutas)

numeros = [50, 10, 33, 40, 15, 60, 20]
numeros(reverse = True)
print(numeros)