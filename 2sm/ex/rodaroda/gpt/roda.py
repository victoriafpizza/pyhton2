import random

# Leitura das opções da roda do arquivo .txt
with open('opcoes_roda.txt', 'r') as file:
    opcoes_roda = file.read().splitlines()

# Lista de palavras
palavras = ["Janela", "Campainha", "Dormitorio"]

# Escolher aleatoriamente uma das três palavras
palavra_escolhida = random.choice(palavras)

# Pedir nomes dos jogadores
jogadores = []
for i in range(3):
    jogador = input(f"Digite o nome do jogador {i + 1}: ")
    jogadores.append({'nome': jogador, 'pontos': 0})

# Iniciar o jogo
jogador_atual = 0
letras_descobertas = set()
letras_palpites = set()
palavra_corrente = ['_' for _ in palavra_escolhida]
tentativas_restantes = 3

while True:
    print(f"\nVez de {jogadores[jogador_atual]['nome']}.")

    # Rodar a roda e escolher uma opção aleatória
    opcao_escolhida = random.choice(opcoes_roda)
    print(f"\nOpção da roda: {opcao_escolhida}")

    if opcao_escolhida == "Perde tudo":
        jogador_atual = (jogador_atual + 1) % 3
        continue  # Pula o restante da iteração para passar a vez
    elif opcao_escolhida == "Passa a vez":
        jogador_atual = (jogador_atual + 1) % 3
        continue  # Pula o restante da iteração para passar a vez
    else:
        letra = input("Escolha uma letra: ").lower()

        if len(letra) == 1 and letra.isalpha():
            if letra in letras_palpites:
                print("Você já escolheu essa letra antes.")
            elif letra in palavra_escolhida.lower():
                letras_descobertas.add(letra)
                letras_palpites.add(letra)

                for i, char in enumerate(palavra_escolhida):
                    if char.lower() == letra:
                        palavra_corrente[i] = char

                # Converta a opção da roda para um número inteiro, exceto "Passa a Vez" e "Perde Tudo"
                if opcao_escolhida != "Passa a Vez" and opcao_escolhida != "Perde tudo":
                    pontos_rodada = int(opcao_escolhida)
                    jogadores[jogador_atual]['pontos'] += palavra_corrente.count(letra) * pontos_rodada
                print(f"Palavra corrente: {' '.join(palavra_corrente)}")
            else:
                letras_palpites.add(letra)
                print("Letra não encontrada na palavra. Passando a vez.")
        else:
            print("Entrada inválida. Digite apenas uma letra.")

    # Exibir informações da rodada
    for jogador in jogadores:
        print(f"{jogador['nome']}: {jogador['pontos']} pontos")

    if len(letras_descobertas) == len(set(palavra_escolhida.lower())):
        print(f"\nParabéns, {jogadores[jogador_atual]['nome']}! Você descobriu todas as letras!")

        # Adicione a lógica para ganhar todo o dinheiro da pontuação
        jogador_ganhador = jogadores[jogador_atual]
        for jogador in jogadores:
            if jogador != jogador_ganhador:
                jogador_ganhador['pontos'] += jogador['pontos']
                jogador['pontos'] = 0

        break

    if tentativas_restantes == 0:
        print(f"\n{jogadores[jogador_atual]['nome']} perdeu todas as tentativas. A palavra era: {palavra_escolhida}")
        jogador_atual = (jogador_atual + 1) % 3
        tentativas_restantes = 3  # Reinicia as tentativas para o próximo jogador

    jogador_atual = (jogador_atual + 1) % 3

# Exibir a pontuação final de cada jogador
print("\nPontuação Final:")
for jogador in jogadores:
    print(f"{jogador['nome']}: {jogador['pontos']} pontos")

# Encontrar e exibir o vencedor
vencedor = max(jogadores, key=lambda x: x['pontos'])
print(f"\nParabéns, {vencedor['nome']}! Você é o vencedor com {vencedor['pontos']} pontos.")
