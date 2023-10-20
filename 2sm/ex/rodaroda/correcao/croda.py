import csv
import random

# armazenando em um list as opções da roda 
with open('roda.txt','r') as arquivo:
    roda = arquivo.read().split()

# Armazenando em um List as palavras 
palavras = []
with open('palavras.csv','r') as file:
    arq_csv = csv.reader(file)
    for item in arq_csv:
        palavras.append(item)

# armazenando cada palavra em um list independente 
palavra = palavras[0][0]
palavra1 = []
for i in range(len(palavra)):
    palavra1.append(palavra[i])

# palavra 2
palavra = palavras[0][1]
palavra2 = []
for i in range(len(palavra)):
    palavra2.append(palavra[i])
    palavra = palavras[0][1]

# palavra 3 
palavra = palavras[0][2]
palavra3 = []
for i in range(len(palavra)):
    palavra3.append(palavra[i])
nomes = [input("diigite o nome do jogador 1: "),
         input("diigite o nome do jogador 1: "),
         input("diigite o nome do jogador 1: ")]

# exibindo a dica e o painel das palavras 
print("\nDica: AVIÃO")
painel1 = []
for i in range(len(palavra1)):
    painel1.append('_')
    painel2 = []
for i in range(len(palavra2)):
    painel2.append('_')
    painel3 = []
for i in range(len(palavra3)):
    painel3.append('_')
print(*painel1)
print(*painel2)
print(*painel3)

# Lista da pontução e variavel jo jogador atual 
pontos = [0, 0, 0]
jogador_atual = 0 
# Armazenando total de letras do jogo 
total_letras = len(palavra1) + len(palavra2) + len(palavra3)
acertos = 0
ponto_roda = 0 
palpites = {""}
palpites.pop()

# Jogando enquanto total de acertos menor do que total de letras 
while acertos < total_letras:
    input(f"\nJogador: {nomes[jogador_atual].upper()}. Pressione Enter para rodar a roda...")
    sorteio_roda = random.choice(roda)
    print(f"\nA roda parou em: {sorteio_roda}")