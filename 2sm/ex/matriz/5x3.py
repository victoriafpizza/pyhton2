def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def encontrar_menor_valor(matriz):
    menor_valor = matriz[0][0]
    posicao = (0, 0)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < menor_valor:
                menor_valor = matriz[i][j]
                posicao = (i, j)
    
    return menor_valor, posicao

def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

linhas = 5
colunas = 3

print("Digite os valores para a matriz 5x3:")
matriz = criar_matriz(linhas, colunas)

exibir_matriz(matriz)

menor_valor, posicao = encontrar_menor_valor(matriz)
print("\nMenor valor encontrado:", menor_valor)
print("Posição na matriz (índices):", posicao)
