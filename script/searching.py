from clases import busqueda_binaria, busqueda_lineal

def crear_lista_ids_ordenada(pokedex):
    ids = []

    for bucket in pokedex.buckets:
        for par in bucket:
            pokemon = par[1]
            ids.append(pokemon.id)

    ids_ordenados = sorted(ids)
    return ids_ordenados

def busqueda_pokemon_equipo_activo(equipo_activo):
    pokemon_buscado = input("\n¿Qué pokemon desea buscar en el equipo?: ").lower().capitalize()
    busqueda = busqueda_lineal(equipo_activo, pokemon_buscado)
    if busqueda != -1:
        print(f"Tu pokemon fue encontrado en la posicion: {busqueda}")
    else:
        print("Tu pokemon no fue encontrado en el equipo, lo siento...")
    
def busqueda_pokemon_pokedex(ids_ordenados, pokedex):
    id_pokemon_buscado = input("\n Ingrese el ID del pokemon buscado: ")
    busqueda = busqueda_binaria(ids_ordenados, id_pokemon_buscado)
    if busqueda != -1:
        pokemon = pokedex.buscar(id)
        print(f"Tu pokemon fue encontrado en la posicion: {busqueda} y es {pokemon.nombre}")
    else:
        print("Tu pokemon no fue encontrado en el equipo, lo siento...")
    return


