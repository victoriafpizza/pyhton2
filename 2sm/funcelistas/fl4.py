# FUPQ peça para o usuáro digitar quatro numeros reais diferentes. Exiba os numeros 
# digitados em ordem decrescente com 3 casas decimais
# (crie uma função sem retorno)

def th(n1):
    n1.sort(reverse = True)
    for i in n1:
        print(f"{i:.3f}")

num = []
print("digite 4 numeros reais")
for i in range(0,4,1):
    valor = float(input())
    num.append(valor)
th(num)