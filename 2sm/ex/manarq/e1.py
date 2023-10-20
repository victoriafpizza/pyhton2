f = open('batatinha.txt','r', encoding='utf-8')
print(f.read())
f.close()

# Caso o arquivo esteja em pastas diferente do local onde o programa está
# salvo, deve-se informar todo o caminho atéo arquivo
# (recomenda-se utilizar a / na separação das pastas e do arquivo)

try: 
    f = open('batatinha.txt','r', encoding='utf-8')
    print(f.read())
    f.close()
except FileExistsError:
    print("arquivo não encontrado")

# Podemos indicar uma quantidae espeficia de caracteres que desejamos ler 
# do arquivo. Passamos o valor desejado na função read()

try:
    f = open('d:/batatinha.txt','r', encoding='utf-8')
    print(f.read(5))
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")


# Função Readline

try:
    f = open('d:/batatinha.txt', 'r', encoding='utf-8')
    print(f.readline())
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")

# For Each 

try:
    f = open('d:/batatinha.txt', 'r', encoding='utf-8')
    for x in f:
        print(x)
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")

# in range (quando sabemos a quantidae de linhas que o arq possui)
 
try:
    f = open('d:/batatinha.txt', 'r', encoding='utf-8')
    for x in range(0, 3, 1):
        print(f.readline())
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")

# append (acrescenta mais conteudo para um arquivo existente)
# podemos mudar par ao modo "a" (append) e usar write() para escrever

try:
    f = open('d:/batatinha.txt', 'a', encoding='utf-8')
    f.write("\nSou pequenininha")
    f.write("\ndo tamanho de um botão")
    f.close()
    f = open('d:/batatinha.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")

# Função Write

try:
    f = open('d:/batatinha.txt', 'w', encoding='utf-8')
    f.write("\ncarrego papai no bolso")
    f.write("\ne mamãe no coração")
    f.write("\no bolso furou")
    f.write("\ne papai caiu no chão")
    f.write("\nMamãe que é mais querida")
    f.write("\nficou no coração")
    f.close()
    f = open('d:/batatinha.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")

# Para criar um novo arquivo

try:
    f = open('d:/rato.txt', 'x', encoding='utf-8')
    f.close()
    f = open('d:/rato.txt', 'w', encoding='utf-8')
    f.write("O rato roeu")
    f.write("\na roupa do rei de Roma")
    f.close()
    f = open('d:/rato.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")

# Se usarmos o modo "w" e o arquiv não existir, ele será criado