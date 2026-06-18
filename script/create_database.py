from clases import HashMap, Pokemon, HashSet
import json


def crear_pokedex_data():
    pokedex_nacional = HashMap(size =150)
    with open("Pokedex_db.json", "r") as archivo:
        data = json.load(archivo)
    
    for dato in data.values():
        pokemon = Pokemon(dato["id"], dato["nombre"], dato["tipo"], dato["poder_combate"])
        pokedex_nacional.agregar(pokemon.id, pokemon)

    return pokedex_nacional

def crear_medallas_data():
    medallas = HashSet(size=8)
    

def main():
    pokedex_nacional = crear_pokedex_data()



main()
