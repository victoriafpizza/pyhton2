import jokenpo

while True:
    print ('''escolha seu movimento:
        1 - para papel
        2 - para tesoura
        3 - para pedra''')
    jogada_do_usuário = input()

    # possibilidade 1
    if jogada_do_usuário == 1 and jokenpo.opcao_sorteada == 2:
        print("o computador ganhou")
    elif jogada_do_usuário == 1 and jokenpo.opcao_sorteada == 3:
        print("voce ganhou!")
    elif jogada_do_usuário == 1 and jokenpo.opcao_sorteada == 1:
        print("empate!!")
    else:
        print("digite uma opção valida")
    # possibilidade 2
    if jogada_do_usuário == 2 and jokenpo.opcao_sorteada == 1:
        print("o computador ganhou")
    elif jogada_do_usuário == 2 and jokenpo.opcao_sorteada == 3:
        print("voce ganhou!")
    elif jogada_do_usuário == 2 and jokenpo.opcao_sorteada == 2:
        print("empate!!")
    else:
        print("digite uma opção valida")
    # possibilidade 3
    if jogada_do_usuário == 3 and jokenpo.opcao_sorteada == 1:
        print("o computador ganhou")
    elif jogada_do_usuário == 3 and jokenpo.opcao_sorteada == 1:
        print("voce ganhou!")
    elif jogada_do_usuário == 3 and jokenpo.opcao_sorteada == 3:
        print("empate!!")
    else:
        print("digite uma opção valida")
