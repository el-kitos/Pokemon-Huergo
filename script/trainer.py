from clases import Pokemon, SinglyLinkedList, Queue, Stack, bubble_sort, insertion_sort
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

def historial():
    ultimos5poke = Stack()
    return ultimos5poke

def profesor_oak():
    profe_oak = []
    return profe_oak

def procesar_pokemon(equipo_activo, pc, pokedex):
    while True:    
        nombre = input("Que pokemon desea agregar al equipo activo: ")
        
        for bucket in pokedex.buckets:
            for par in bucket:
                pokemon = par[1]
                if pokemon.nombre == nombre :
                    if len(equipo_activo) < 6:
                        equipo_activo.append(pokemon)
                        print("Se agrego exitosamente.")
                        
                    else:
                        pc.agregar(pokemon)
                        print("El equipo esta lleno!, Se agrego al PC")
                        
                    return
                
        print("Ese pokemon no exite en la pokedex intente nuevamente")
        
def transferir_pc_oak(pc, profe_oak, ultimos5poke):
    pokemon = input("Que pokemon desea transferir al profesor Oak?: ")

    actual = pc.cabeza

    while actual is not None:
        if actual.dato.nombre == pokemon:
            pc.eliminar(actual.dato)
            profe_oak.append(actual.dato)

            if ultimos5poke.size() == 5:
                ultimos5poke.pop()

            ultimos5poke.push(actual.dato)
            return

        actual = actual.siguiente

    print("Ese Pokémon no se encuentra en la PC.")

        
def deshacer_utlima_transferencia(pc, profe_oak, ultimos5poke):
    profe_oak.pop()
    pokemon_ultimo = ultimos5poke.pop()
    pc.agregar(pokemon_ultimo)
    print(f"La ultima tranferencia se restablecio y asi quedo la pc: {pc}")
    


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
            if indice < 0 or indice > 7:
                raise IndexError
        except ValueError:
            print("Elije un numero!")
        except IndexError:
            print("Tiene que ser un numeo entreo 0 y 7!")
        else:
            print("Lider seleccionado:", lideres[indice])
            break
    combate = [lideres[indice], "Usuario"]
    ganador = random.choice(combate)
    if ganador == lideres[indice]:
        print("Perdiste...")
    else:
        print("GANASTE!!")
    

