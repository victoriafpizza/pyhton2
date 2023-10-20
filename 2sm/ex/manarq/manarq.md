"Manupilando Arquivos"

# A função chave para se manipular arquivos em Python é a função open()
# A função open() utiliza dois parametros: o nome do arquivo e o modo de edição

"temos 4 diferentes modos par ase abrir um arquivo"

# "r" - read - Valor padrão. Abre um arquivo para leitura, exibe erro se o arquivo não existir
# "a" - append - Abre um arquivo para adicionar conteúdo, cria o arquivo para dicionar conteudo, cria o 
#  arquivo caso ele não exista
# "w" - write - Abre um arquivo para escrever, cria o arquivo caso ele não exista. 
# "x" -  create - Cria um arquivo especifico, retorna erro se o arquivo já existir. 

# Fique atento a codificação do seu arquivo, podemos indicar o tipo de
# codificação como o parâmetro encoding (na função open() após o modo
# escolhido). Uma boa codificação para se utilizar é a utf-8

# O arquivo a ser acessado deve estar na mesma pasta do arquivo do
# programa em Python. Ou, se estiver em pasta diferente, seu caminho de ser
# especificado junto ao nome do arquivo na função open()

# Após a abetura do arquivo podemos realizar sua leitura com a função read() que permite 
# a leitura completa do arquivo na função open()

# IMPORTANTE: É uma boa prática de programação fechar a manipulação com o arquivo com a função close()
# ao final das modificações efetuadas.

# NOTA: Infelizmetne não funciona no vscode, é necessário usar o pycharm. 

Utilizamos a função readline() podemos realizar leitura de linhas inteiras 
(a leitrua encerra quando encontrando o "Enter")
Para eltirua de novas linhas, basta utlizar novamente a função readline()

Para apargar arquivos, devemos importar o modulo os e utilizar a função remove()
Uma boa pratica de programção é verificar antes se o arquivo existe, com a fnção path.exists()