import json
usuarios = {
    "astro": {
    "nome": "Astrogildo",
    "login": "astro",
    "senha": "12345"
    },
    "beri": {
    "nome": "Berisvaldo",
    "login": "beri",
    "senha": "09876"
    }
}

try:
    with open('d:/usuarios.json', 'w') as f:
        json.dump(usuarios, f)
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")

# Para ler de um arquivo Json e transformar em um objeto do Python utilizamos
# a função loads() do módulo json