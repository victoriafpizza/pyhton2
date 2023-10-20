import json

usuarios = {
    "astro":{
        "nome": "Astrogildo", "Login": "astro", "senha"
: "123"},
    "beri":{
        "npme":"berisvaldo","login":"beri","senha":"456"
    }
}

# O "D" é porque fica no bloco de notas o que ta salvo pelo jason
try: 
    with open('d:/usuários.json', 'w', encoding='utf-8') as f:
        json.dump(usuarios,f)
except FileExistsError:
    print("Caminho ou arquivo inexistente")