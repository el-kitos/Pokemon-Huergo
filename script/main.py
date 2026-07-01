from create_database import create_pokedex_data, create_medals_data
from organization import main_org
from searching import crear_lista_ids_ordenada , busqueda_pokemon_equipo_activo, busqueda_pokemon_pokedex
from trainer import create_equipo_activo, create_cajas_pc, create_centro_pokemon, historial, profesor_oak, procesar_pokemon, transferir_pc_oak, deshacer_utlima_transferencia, desafiar_lider_gimnasio, enviar_centro_pokemon

import time
import os


def mostrar_menu():
    print("1) Ver Pokédex")
    time.sleep(0.5)
    print("2) Ver Equipo Principal")
    time.sleep(0.5)
    print("3) Ver PC")
    time.sleep(0.5)
    print("4) Ver Medallas")
    time.sleep(0.5)
    print("5) Capturar nuevo Pokémon (Deriva a Equipo o PC automáticamente)")
    time.sleep(0.5)
    print("6) Ordenar PC (Submenú: Alfabético, Por Tipo, Por PC)")
    time.sleep(0.5)
    print("7) Buscar Pokémon en Equipo")
    time.sleep(0.5)
    print("8) Enviar Pokémon al Centro Pokémon")
    time.sleep(0.5)
    print("9) Transferir Pokémon al Profesor Oak")
    time.sleep(0.5)
    print("10) Deshacer última transferencia")
    time.sleep(0.5)
    print("11) Desafiar Líder de Gimnasio")
    time.sleep(0.5)
    print("12) Salir del sistema")
    time.sleep(0.5)

def main():
    pokedex_nacional = create_pokedex_data()
    medallas_obtenidas = create_medals_data()
    equipo_activo = create_equipo_activo()
    pc = create_cajas_pc()
    centro_pokemon = create_centro_pokemon()
    ultimos5poke = historial()
    profe_oak = profesor_oak()
    ids_ordenados = crear_lista_ids_ordenada(pokedex_nacional)
    print("========================================================================")
    print("\n --> BIENVENIDO AL MEJOR JUEGO DEL MUNDO DE POKEMON...")
    print("=======================================================================")
    time.sleep(1)
    print("Inicializando motor de base de datos... OK.")
    time.sleep(0.5)
    print("Cargando Pokédex Nacional... OK.")
    time.sleep(0.5)
    print("Validando registros de medallas... OK.")
    time.sleep(1)
    while True:
        time.sleep(0.5)
        print("-> A continuacion se le mostrara el menu de acciones del juego")
        time.sleep(0.5)
        mostrar_menu()
        time.sleep(1)
        while True:
            try:
                opcion = int(input("Elija que accion realizar presionando numeros del 1 al 12: "))
                if opcion < 1 or opcion > 12:
                    raise IndexError
            except ValueError:
                print("Eso no es un numero! Intentelo nuevamente")
            except IndexError:
                print("Ingrese un numero del 1 al 12!")
            else:
                break
        if opcion == 1:
            print("Bienvenido a la POKEDEX NACIONAL")
            print("1) Buscar Pokémon por ID")
            print("2) Ver todos los Pokémones")
            while True:
                try:
                    sub_opcion = int(input("Elija que accion realizar presionando numeros del 1 al 2: "))
                    if sub_opcion < 1 or sub_opcion > 2:
                        raise IndexError
                except ValueError:
                    print("Eso no es un numero! Intentelo nuevamente")
                except IndexError:
                    print("Ingrese un numero del 1 al 2!")
                else:
                    break
            if sub_opcion == 1:
                busqueda_pokemon_pokedex(ids_ordenados, pokedex_nacional)
            else:
                print("Mostrando todos los Pokémones de la POKEDEX NACIONAL...")
                pokedex_nacional.mostrar()
            time.sleep(1)
            input("Presione enter para volver: ")
        elif opcion == 2:
            if len(equipo_activo) == 0:
                print("El equipo activo está vacío.")
            else:
                print("\n--- EQUIPO ACTIVO ---")
                for pokemon in equipo_activo:
                    print(pokemon)
            input("Presione enter para salir: ")
        elif opcion == 3:
            pc.imprimir()
            time.sleep(1)
            input("Presione enter para volver: ")
        elif opcion == 4:
            medallas_obtenidas.mostrar()
            time.sleep(1)
            input("Presione enter para volver: ")
        elif opcion == 5:
            procesar_pokemon(equipo_activo, pc, pokedex_nacional)
        elif opcion == 6:
            main_org(pc)
        elif opcion == 7:
            busqueda_pokemon_equipo_activo(equipo_activo)
            
        elif opcion == 8:
            enviar_centro_pokemon(equipo_activo, centro_pokemon)
        elif opcion == 9:
            transferir_pc_oak(pc, profe_oak, ultimos5poke)    
        elif opcion == 10:
            deshacer_utlima_transferencia(pc, profe_oak, ultimos5poke)
        elif opcion == 11:
            if len(equipo_activo) <= 0:
                print("No hay pokemones para pelear!!")
            else:
                desafiar_lider_gimnasio(medallas_obtenidas)
        elif opcion == 12:
            print("GRACIAS POR HABER JUGADO!!")
            print("Esperamos verte pronto devuelta por aqui")
            break
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()