# Victoria Franceschini Pizza 
# rm550609

# Definindo a Tuple com os pokémons e seus tipos
pokemons = (
    ("Caterpie", "inseto"),
    ("Pidgey", "voador"),
    ("Geodude", "pedra"),
    ("Squirtle", "água"),
    ("Jigglypuff", "normal"),
    ("Machop", "lutador"),
    ("Abra", "psíquico"),
    ("Ekans", "venenoso"),
    ("Charmander", "fogo"),
    ("Diglett", "terra")
)

# Pedindo ao usuário para digitar um tipo de Pokémon
user_input = input("Digite um tipo de Pokémon: ").lower()

# Inicializando contadores e uma lista para nomes de pokémons
count = 0
pokemon_names = []

# Percorrendo a Tuple e contando e coletando os pokémons do tipo escolhido
for pokemon, tipo in pokemons:
    if tipo == user_input:
        count += 1
        pokemon_names.append(pokemon)

# Exibindo a quantidade de pokémons do tipo escolhido
print("Quantidade de pokémons do tipo", user_input + ":", count)

# Exibindo os nomes dos pokémons do tipo escolhido
print("Lista de pokémons do tipo", user_input + ":")
for name in pokemon_names:
    print(name)
