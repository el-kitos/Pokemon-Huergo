from clases import Pokemon, SinglyLinkedList, Queue, Stack
import random
import time

def create_equipo_activo():
    equipo_activo = []
    return equipo_activo

def create_cajas_pc():
    pc = SinglyLinkedList()
    return pc

def create_centro_pokemon():
    centro_pokemon = Queue()
    return centro_pokemon

def deshacer_transferencia():
    ultimos5poke = Stack()
    return ultimos5poke

def procesar_pokemon(pokemon, equipo_activo, pc, ultimos5poke):
    if len(equipo_activo) < 6:
        equipo_activo.append(pokemon)
        print("Se agrego exitosamente.")
    else:
        pc.agregar(pokemon)
        print("El equipo esta lleno!, Se agrego al PC")
        if len(ultimos5poke) < 5:
            ultimos5poke.push(pokemon)
        else:
            ultimos5poke.pop()
            ultimos5poke.push(pokemon)
 
def desafiar_lider_gimnasio():
    lideres = ["Brock", "Misty", "Lt. Surge", "Erika", "Koga", "Sabrina", "Blaine", "Giovanni"]
    print("\n Bienvenido a la pelea")
    j = 0
    for i in lideres:
        print(j, i)
        j+=1
        time.sleep(0.5)
    while True:
        try:
            indice = int(input("Elija uno de estos lideres con el cual pelear(0-7):  "))
            if indice > 7:
                raise IndexError
        except TypeError:
            print("Elije un numero!")
        except IndexError:
            print("Tiene que ser un numeo entreo 0 y 7!")
        else:
            print("Lider seleccionado:", lideres[i])
            break
    combate = [lideres[i], "Usuario"]
    ganador = random.choice(combate)
    if ganador == lideres[i]:
        print("Perdiste...")
    else:
        print("GANASTE!!")
    

