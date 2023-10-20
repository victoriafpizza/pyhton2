
matriz = []

for i in range(5):
        nome = input("Digite o nome da pessoa: ")
        estado = input("Digite o estado onde nasceu: ")
        matriz.append([nome, estado])

estado_escolhido = input("Digite um estado brasileiro: ")

pessoas_estado_escolhido = []
for pessoa in matriz:
        if pessoa[1].lower() == estado_escolhido.lower():
            pessoas_estado_escolhido.append(pessoa[0])

if pessoas_estado_escolhido:
        print(f"Pessoas nascidas em {estado_escolhido}:")
        for nome in pessoas_estado_escolhido:
            print(nome)
else:
        print(f"Nenhuma pessoa nasceu em {estado_escolhido}.")

