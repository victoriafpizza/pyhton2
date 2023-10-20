# Nome: Victoria Franceschini Pizza r
# rm: 550609

# Monte um programa para acesso a um sistema ficticio. 
# O usuário deve informar login e senha .
# Valide o ligin e senha no arquivo Json criado no exercicio anterior. 
# Exiba as informações de usuário inexistente , senha incorreta ou acesso permitido 
# Exibindo também o nome deste usuário, coforme a situação passada. 


import json

# Função para verificar o login e senha
def verificar_acesso(login, senha, usuarios):
    for usuario in usuarios:
        if usuario["login"] == login:
            if usuario["senha"] == senha:
                return "acesso permitido", usuario["nome"]
            else:
                return "senha incorreta", None
    return "usuário inexistente", None

# Carrega os usuários do arquivo JSON
def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo_json:
            return json.load(arquivo_json)
    except FileNotFoundError:
        return []

# Função principal
def main():
    usuarios = carregar_usuarios()

    while True:
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        resultado, nome = verificar_acesso(login, senha, usuarios)

        if resultado == "acesso permitido":
            print(f"Acesso permitido. Bem-vindo, {nome}!")
            break
        elif resultado == "senha incorreta":
            print("Senha incorreta. Tente novamente.")
        else:
            print("Usuário inexistente. Tente novamente.")

if __name__ == "__main__":
    main()
