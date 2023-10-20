import random

def imprime_mensagem_abertura():
    print("**********************************")
    print("*** Bem Vindo ao Jogo da Forca ***")
    print("**********************************")

def carrega_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def imprime_mensagem_vencedor():
    print("Parabens, voce ganhou!")
    print("        ____________      ")
    print("       '._==_==_= _.'     ")
    print("       .-\\:        /=.   ")
    print("      |  (|:.      |) |   ")
    print("       '-|:.       |-'    ")
    print("         \\::.     /      ")
    print("           '::.  .'       ")
    print("            )   (         ")
    print("           _.' '._        ")
    print("          '_______'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, voce foi enforcado")
    print("A palavra era {}".format(palavra_secreta))
    print("     ______________             ")
    print("    /               \           ")
    print("   /                 \          ")
    print("  /                   \         ")
    print("  |   XXX       XXX    |        ")
    print("  |   XXX       XXX    |        ")
    print("  |                    |        ")
    print("  \_       XXX        _/        ")
    print("    |\     xxx      /|         ")
    print("    | |            | |         ")
    print("    |  I I I I I I I |         ")
    print("    |    I I I I I   |         ")
    print("     \_             _/         ")
    print("       \__________/            ")
 
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

if (__name__ == "__main__"):
    jogar()