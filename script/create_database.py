from clases import HashMap, Pokemon, HashSet
import json


def create_pokedex_data():
    pokedex_nacional = HashMap(size =150)
    with open("jsons/Pokedex_db.json", "r") as archivo:
        data = json.load(archivo)

    for dato in data.values():
        pokemon = Pokemon(dato["id"], dato["nombre"], dato["tipo"], dato["poder_combate"])
        pokedex_nacional.agregar(pokemon.id, pokemon)

    return pokedex_nacional

def create_medals_data():
    medallas_obtenidas = HashSet(size=8)

    with open("jsons/Medals_db.json") as archivo:
        data = json.load(archivo)

    medallas_obtenidas.agregar(data[0])
    medallas_obtenidas.agregar(data[1])
    
    return medallas_obtenidas


