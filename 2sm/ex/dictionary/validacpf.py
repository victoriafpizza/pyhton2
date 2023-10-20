def valida1(n1, x): 
    soma = digito = resto = 0
    cont = x
    for i in n1 : 
        soma += i * cont
        cont -= 1
    resto = soma % 11
    if resto < 2 :
        digito = 0 
    else : 
        digito = 11 - resto 
    return digito 

# prorgama principal 

cpfnum = []
digiuno = digiduo = cpfd1 = cpfd2 = 0 
cpfval = " "

digiuno = digiduo = 0 
print("digite seu cpf (somente numeros)")
cpf = input()
for i in range(0,9,1):
    cpfnum.append(int(cpf[i:i+1]))
digiuno = valida1(cpfnum, 10)
cpfnum.append(digiuno)
digiduo = valida1(cpfnum, 11)
cpfnum.append(digiduo)
for i in cpfnum :
    cpfval += str(i)
cpfd1 = int(cpf[-2:-1]) #cpf [9:10 ]
cpfd2 = int(cpf[-1]) #cpf[10:11]

if digiuno == cpfd1 and digiduo == cpfd2 :
    print(f"o cpf de um numero {cpf} é válido")
else: 
    print(f"o cpf de um numero {cpf} é inválido")
    print(f"o correto seria {cpfval}")


