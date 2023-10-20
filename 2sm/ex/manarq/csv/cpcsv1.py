# rm: 550609 Nome: Victoria Franceschini Pizza

# Monte um programa de cadastro de filmes. Devem ser cadastrados as informações de titulo, genero, duração 
# censura, diretor. (ex: Os Passaros, Terror, 119 minutos, 14 anos, Alfred Hitchock). O usuário deve 
# contunar cadastranddo novos filmes enquanto quiser (defina uma condição de parada). Salve todos os filmes
# digitados em um arquivo no formato CSV

import csv

# Função para cadastrar um filme
def cadastrar_filme():
    titulo = input("Digite o título do filme: ")
    genero = input("Digite o gênero do filme: ")
    duracao = input("Digite a duração do filme (em minutos): ")
    censura = input("Digite a classificação indicativa do filme: ")
    diretor = input("Digite o nome do diretor do filme: ")
    return [titulo, genero, duracao, censura, diretor]


# Lista para armazenar os filmes cadastrados
filmes = []

# Loop para continuar cadastrando filmes
while True:

    filme = cadastrar_filme()
    filmes.append(filme)
    continuar = input("Deseja cadastrar outro filme? (s/n): ").lower()
    if continuar != 's':
        break

# Salvando os filmes em um arquivo CSV
with open('C:/Users/logonrmlocal/Desktop/py/python/2sm/ex/manarq/csv/cpcsv1.py', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Título', 'Gênero', 'Duração', 'Censura', 'Diretor'])
    escritor_csv.writerows(filmes)

print("Filmes cadastrados foram salvos no arquivo 'catalogodefilmes.csv'.")
    