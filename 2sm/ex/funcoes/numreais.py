# Peça para o usuário digitar quatro nueros reais diferetntes 
# Exiba os numeros digitados em ordem decrescentes com 3 casas
# decimais (crie uma função sem retorno)

def trihousedesc (n1):
    n1.sort(reverse = True)
    for i in n1 :
        print(f"{1:.3f}")

num = []
print("digite 4 numeros reais")
for i in range(0,4,1):
    valor  = float(input())
    num.append(valor)
trihousedesc(num)