"SET"

# O objeto Set em Python é utilizado para armazenar multiplos valores em uma unica varaivel 
# Um set em Py é um dos 4 tipos de varaiveis que são utilizados para armazenar coleçoes de dados
# Criamos um Set e incializamos seus valores usadno as chaves {}

frutas = {"maça", "uva", "tomate"}
print(frutas)

# CARACTERISTICAS DO SET

# -Não são ordenadas: seus valores são possuem uma ordem especifica. Os valores podem aparecer
# em um local diferente a cada vez que é utilizada e nãopodemos acessar seu valor por indice
# -É imutável: uma vez criada seus valores não podem ser mudados (porem é possivel inserir um 
# novo valor ou remover um valor existente)
# - Não permite valores duplicados: como não possu indice, não permite que seus valores sejam 
# duplicados
# - Podemos usar a função len() para obter o seu tamanho
# - Pode conter valores de um unico tipo de dado, ou mesmo, de varios tipos.
# - Os valores True e 1 e os valores False e 0 são considerados a mesma coisa

frutas = {"maça", "uva", "tomate", "kiwi", "uva"}
print(frutas)
print(len(frutas))
print(type(frutas))
misto = {"alface", 1, True, False, 0, "pepino", 3.14}
print(misto)
print(len(misto))
print(type(misto))

# Como não possui indice, só podemos navegar pelos elementos de um Set com o comando for-each
frutas = {"maça", "uva", "tomate"}
for i in frutas :
    print(i)

# Ou verificar a existencia de um valor com o comando in 
frutas = {"maça", "uva", "tomate"}
print ("uva" in frutas) 

# Podemos usar a função add() para adicionar novos valores
# Podemos adicionar um conjunto de valores de outro Set (ou mesmo outro objeto) com a função update()
# Podemos remover elementos com a função
# remove() - porem, se o elemento não existir, ocasiona erro
# discard() - porem, se o elemento não existir, não ocasiona erro
# pop() - remove um elemento aleatório
# clear() - esvazia o Set
# del() - elimina o Set completamente 