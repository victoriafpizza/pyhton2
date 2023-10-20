# Rm 550609 Nome: Victoria Franceschini Pizza

# Monte um programa que exiba um menu que permita o usuário escolher: titulo, diretor, ou genero. Dependendo
# da escolha busque e exiba apenas essas informações (no  arquivo CSV criado no exrecico anterior) de todos
# os filmes que correspondam a escolha do usuário. 

import csv

def buscar_filmes_por_criterio(criterio):
    with open('seuarquivo.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        if criterio == 'titulo':
            campo = 'Titulo'
        elif criterio == 'diretor':
            campo = 'Diretor'
        elif criterio == 'genero':
            campo = 'Genero'
        else:
            print("Escolha inválida")
            return
        print(f"Listando filmes por {criterio}:")
        for row in reader:
            print(row[campo])
if __name__ == "__main__":
    while True:
        print("\nEscolha uma opção:")
        print("1 - Buscar por Título")
        print("2 - Buscar por Diretor")
        print("3 - Buscar por Gênero")
        print("4 - Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            buscar_filmes_por_criterio('titulo')
        elif opcao == '2':
            buscar_filmes_por_criterio('diretor')
        elif opcao == '3':
            buscar_filmes_por_criterio('genero')
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

