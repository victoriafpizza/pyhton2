"NESTED LISTS"

# Um List pode conter outros List, chamamos isto de listas aninhadas. Em outras linguagens listas
# aninhadas tamém são chamadas de variáveis indexadas bidimensionais ou matrizes. 
# Realizamos o acesso a um valor especifico indicando seus dois indices (para facilitar assimilação
# podemos traçar um comparativo com tabelas, primeiro indica a linha e segundo indice a coluna)
# Podemos alterar também um valor na lista aninhada por outro valor passando seu nome, indices e o
# novo valor 

pessoas = [["Astrogildo", "Berisvaldo", "Josenelson"],
           ["Planetario", "Moriartti", "Trancoso"],
           [25, 33, 17]]
print(pessoas)
print(type(pessoas))
print(len(pessoas))
print(len(pessoas[1]))
pessoas[0][2] = "Gumercindo"
print(pessoas[0])
print(pessoas[0][2])

# Exemplo de lista aninhada (matriz 3x2) vazia e preenchimento posterior via estruturas de repetição

matriz = []
qtdelin = 3
qtdecol = 2
for i in range(0, qtdelin, 1) :
    linha = []
    for j in range(0, qtdecol, 1) :
        valor = input(f"Digite valor[{i}][{j}]:")
        linha.append(valor)
    matriz.append(linha[:])
print(matriz)