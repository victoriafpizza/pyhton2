# import statistics 
numeros = []
num = media = 0.0 
soma = 0.0 
for i in range(0,20,1) :
    print("DIGITE U M NUMERO REAL AI")
    num = float(input())
    numeros.append(num)
for i in numeros :
    soma += i 
media = soma /len(numeros)
print(f"Media dos valores é `{media}")
