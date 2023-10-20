# Nome: Victoria Franceschini Pizza r
# rm: 550609

# Monte um progama de cadastos de usuários. Devem se cadastrados as ifnormações de nome, login e senha.
# O usuário deve continuar cadastrando usuários enquanto quiser (defina um padrão para parar)
# Salve todos os usuários digitados em um arquivo no formato JSON

import json

# Função para cadastrar um usuário
def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    login = input("Digite o login do usuário: ")
    senha = input("Digite a senha do usuário: ")
    return {"nome": nome, "login": login, "senha": senha}

# Inicializa uma lista vazia para armazenar os usuários
usuarios = []

while True:
    novo_usuario = cadastrar_usuario()
    usuarios.append(novo_usuario)

    continuar = input("Deseja cadastrar outro usuário? (S/N): ").strip().lower()
    if continuar != 's':
        break

# Salva os usuários em um arquivo JSON
with open("usuarios.json", "w") as arquivo_json:
    json.dump(usuarios, arquivo_json)

print("Usuários cadastrados com sucesso. Os dados foram salvos no arquivo usuarios.json.")
