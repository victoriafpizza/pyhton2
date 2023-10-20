# Peça pra o usuario digitar um numero inteiro qualquer. 
# Exiba a raiz quadrad (crie uma função com retorno)

def raiz(n1):
    rs = n1 ** (1/2)
    return int(rs)

print("digite um numero inteiro")
num1 = int(input())
resultado = raiz(num1)
print(f"raiz quadrada: {resultado}")