# Peça para o usuario didigtar varios numeros inteiros, deve continuar 
# digitando até que digite o valor 0 para encerrar. 
# Exiba para cada numero que ele digitar se o numeor é par ou impar
# (crie uma função sem retorno)

def parimpar(n1):
    rs = n1 % 2
    if rs == 0:
        print("este numero é par")
    else:
        print("este numero é impar")

num = 1
while(num != 0):
    print("digite um numero inteiro ou zero")
    num = int(input())
    parimpar(num)
print("fim de programa")
