#  Faça um programa que peça para o usuário digitarvários numeros
# inteiros, deve continuar digitando até que digite o valor 0 para encerrar. 
# Exiba para cad numero que ele digitar se o numero é par ou impar 
# (crie uma função sem retorno) 

def parimpar (num):
    rs = n1 % 2
    if rs == 0:
        print("este numero é par")
    else:
        print("este numero é impar")

num = 1
while(num != 0):
    print("digite um numero inteiro (ou zero)")
    num = int(input())
    parimpar(num)
print("fim de programa")