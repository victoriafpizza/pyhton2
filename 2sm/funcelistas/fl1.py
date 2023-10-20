# Faça um programa que peça para o usuário digitar dois numeros inteiros. Exiba ao final o resto da divisão 
# (crie uma função com retorno)

print("digite dois números inteiros")
num1 = int(input())
num2 = int(input())

# os parametros da funçãopodem existir ou não, pois são as informações que a função pode receber para serem
# processadas. 

def resto(num1,num2):
    rs1 = num1 // num2
    rs2 = num2 * num1
    rs3 = num1 - rs2
    return rs3

resultado = resto(num1,num2)
print(F"RESTO DA DIVISÃO: {resultado}")
# return serve pra quando existir a necessidade de retornar alguma informação para que invovu a função.
