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

def procesar_pokemon(equipo_activo, pc, pokedex_nacional):
    print("[SISTEMA DE CAPTURA]")
    while True:    
        nombre = input("--> Que pokemon desea capturar?: ").lower().capitalize()
        
        for bucket in pokedex_nacional.buckets:
            for par in bucket:
                pokemon = par[1]
                if pokemon.nombre == nombre :
                    if len(equipo_activo) < 6:
                        equipo_activo.append(pokemon)
                        print("Se agrego exitosamente al equipo activo.")
                        
                    else:
                        pc.agregar(pokemon)
                        print("El equipo esta lleno(6/6)!")
                        print("Derivando a Almacenamiento de PC... Registro añadido exitosamente.")
                    return
                
        print("Ese pokemon no exite en la pokedex intente nuevamente")
        
def transferir_pc_oak(pc, profe_oak, ultimos5poke):
    pokemon = input("Que pokemon desea transferir al profesor Oak?: ").strip().lower().capitalize()

    actual = pc.cabeza

    while actual is not None:
        if actual.dato.nombre == pokemon:
            pokemon_a_transferir = actual.dato
            pc.eliminar(pokemon_a_transferir)
            profe_oak.append(pokemon_a_transferir)
            print(f"{pokemon_a_transferir.nombre} ha sido transferido al profesor Oak.")

            if ultimos5poke.size() == 5:
                ultimos5poke.pop()

            ultimos5poke.push(pokemon_a_transferir)
            return

        actual = actual.siguiente

    print("Ese Pokémon no se encuentra en la PC.")

        
def deshacer_utlima_transferencia(pc, profe_oak, ultimos5poke):
    print("Deshaciendo la última transferencia...")
    if len(profe_oak) <= 0:
        print("El profesor oak no tiene ningun pokemon!")
        return

    pokemon_ultimo = ultimos5poke.pop()
    if pokemon_ultimo is None:
        print("No hay transferencias recientes para deshacer.")
        return

    profe_oak.pop()
    pc.agregar(pokemon_ultimo)
    time.sleep(1)
    print(f"La ultima tranferencia se restablecio y asi quedo la pc: {pc}")
        


def desafiar_lider_gimnasio(medallas_obtenidas):
    lideres = ["Brock", "Misty", "Lt. Surge", "Erika", "Koga", "Sabrina", "Blaine", "Giovanni"]
    medallas = [
        "Medalla Roca",
        "Medalla Cascada",
        "Medalla Trueno",
        "Medalla Arcoiris",
        "Medalla Alma",
        "Medalla Pantano",
        "Medalla Volcan",
        "Medalla Tierra"
    ]
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
    for i in range(3):
        print("Peleando...")
        time.sleep(1)
    if ganador == lideres[indice]:
        print("Perdiste...")
    else:
        print("GANASTE!!")
        if medallas_obtenidas.buscar(medallas[indice]) is None:
            medallas_obtenidas.agregar(medallas[indice])
            print(f"Obtuviste la {medallas[indice]}.")
        else:
            print(f"Ya tenías la {medallas[indice]}.")

        
def enviar_centro_pokemon(equipo_activo, centro_pokemon):
    print("[CENTRO POKÉMON - COLA DE SANACIÓN]")
    while True:
        nombre = input("¿Qué Pokémon desea enviar al Centro Pokémon?: ").lower().capitalize()
        print(|f"Enviando a", {nombre}, "al Centro Pokémon...")
        time.sleep(1)
        for pokemon in equipo_activo:
            if pokemon.nombre == nombre:
                equipo_activo.remove(pokemon)
                centro_pokemon.enqueue(pokemon)

                print(f"{pokemon.nombre} está siendo curado...")
                time.sleep(1)

                print(f"{pokemon.nombre} ya fue curado y volvió al equipo.")

                equipo_activo.append(pokemon)
                centro_pokemon.dequeue()  
                return

        print("Ese Pokémon no está en el equipo activo. Intente nuevamente.")