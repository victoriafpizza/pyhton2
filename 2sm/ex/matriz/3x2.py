def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = float(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def somar_matrizes(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    soma_matriz = []
    for i in range(linhas):
        linha_soma = []
        for j in range(colunas):
            valor_soma = matriz1[i][j] + matriz2[i][j]
            linha_soma.append(valor_soma)
        soma_matriz.append(linha_soma)
    return soma_matriz

def exibir_matriz(matriz, nome):
    print(f"{nome}:")
    for linha in matriz:
        print(linha)

linhas = 3
colunas = 2

print("Digite os valores para a primeira matriz:")
matriz1 = criar_matriz(linhas, colunas)

print("\nDigite os valores para a segunda matriz:")
matriz2 = criar_matriz(linhas, colunas)

exibir_matriz(matriz1, "Matriz 1")
exibir_matriz(matriz2, "Matriz 2")

soma = somar_matrizes(matriz1, matriz2)
exibir_matriz(soma, "Soma das Matrizes")
