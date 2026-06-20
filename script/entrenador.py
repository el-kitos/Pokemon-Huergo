from clases import Pokemon, SinglyLinkedList, Queue, Stack

def create_equipo_activo():
    equipo_activo = []
    return equipo_activo

def create_cajas_pc():
    pc = SinglyLinkedList()
    return pc

def procesar_pokemon(pokemon, equipo_activo, pc):
    if len(equipo_activo) < 6:
        equipo_activo.append(pokemon)
        print("Se agrego exitosamente.")
    else:
        pc.agregar(pokemon)
        print("El equipo esta lleno!, Se agrego al PC")

def create_centro_pokemon():
    centro_pokemon = Queue()
    return centro_pokemon
 
