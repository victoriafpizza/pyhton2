import random
import jkpp

def sorteio():
    opcoes = ['pedra', 'papel', 'tesoura']
    papel = 1
    tesoura = 2
    pedra = 3
    opcao_sorteada = random.choice(opcoes)
    return opcao_sorteada

def ganhador():
    if jogada_usuario == jogada_computador:
        return "Empate"
    elif (jogada_do_usuario == 3 and opcao_sorteada == 2) or \
         (jogada_do_usuario == 1 and opcao_sorteada == 3) or \
         (jogada_do_usuario == 2 and opcao_sorteada == 1):
        return "Usuário"
    else:
        return "Computador"