numeros = []
num = soma = 0 
for i in range(0,15,1):
    print("digite um numero inteiro")
    num = int(input())
    numeros.append(num)
# soma = sum(numeros)
for i in numeros: 
    soma += i
print(f"somatoria dos valores é {soma}")
