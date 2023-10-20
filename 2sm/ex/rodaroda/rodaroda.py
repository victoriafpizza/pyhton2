# Eric de Carvalho rm: 550249
# Emanuelle Soares rm: 97973
# Murilo Roveri Soares rm: 97893
# Victoria Franceschini rm: 550609


import random

print("*****************************")
print("Bem Vindo ao jogo Roda a Roda")
print("*****************************")

print("dgite o nome do jogador 1")
jogador1 = input()

print("dgite o nome do jogador 2")
jogador2 = input()

print("dgite o nome do jogador 3")
jogador3 = input()

jogadores = ["jogador1","jogador2","jogador3"]
jogador_aleatorio = random.choice(jogadores)

print(f"é a vez do {jogador_aleatorio}")

with open('D:/python/palavraroda.csv', 'r') as lero:
    palavras = lero.read().splitlines()
palavra = random.choice(palavras)

print("agora escolha uma letra")