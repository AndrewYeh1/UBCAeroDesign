import pypokedex


def getPokemon():
    f = open("pokemonList.txt", "w")

    for i in range(1010):
        pokemon = pypokedex.get(dex=i + 1)
        print(pokemon.dex, pokemon.name)
        f.write(f"{pokemon.name} {pokemon.base_stats.defense}\n")

    f.close()


getPokemon()
