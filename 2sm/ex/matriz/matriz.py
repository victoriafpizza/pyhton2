matriz = []
qtdelin = 3
qtdecol = 2

for i in range(0,qtdelin,1):
    linha = []
    for j in range (0, qtdecol,1):
        valor = input(f"digite valor {i} e {j}")
        linha.append(valor)
    matriz.append(linha[:])
print(matriz)