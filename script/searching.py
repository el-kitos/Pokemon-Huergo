from clases import busqueda_binaria, busqueda_lineal

def busqueda_pokemon_equipo_activo(equipo_activo):
    pokemon_buscado = input("\n Que pokemon desea buscar en el equipo?: ")
    busqueda = busqueda_lineal(equipo_activo, pokemon_buscado)
    if busqueda != -1:
        print(f"Tu pokemon fue encontrado en la posicion: {busqueda}")
    else:
        print("Tu pokemon no fue encontrado en el equipo, lo siento...")
    return
    
def busqueda_pokemon_pokedex():
    pass


