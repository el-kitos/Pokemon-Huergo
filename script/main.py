from create_database import create_pokedex_data, create_medals_data
from organization import organization_AZ, organization_by_type, organization_by_pc
from searching import crear_lista_ids_ordenada , busqueda_pokemon_equipo_activo, busqueda_pokemon_pokedex
from trainer import create_equipo_activo, create_cajas_pc, create_centro_pokemon, historial, profesor_oak, procesar_pokemon, transferir_pc_oak, deshacer_utlima_transferencia, desafiar_lider_gimnasio

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
    
    while True:
        print("\n --> BIENVENIDO AL MEJOR JUEGO DEL MUNDO DE POKEMON...")
        time.sleep(0.5)
        print("-> A continuacion se le mostrara el menu de acciones del juego")
        time.sleep(0.5)
        mostrar_menu()
        time.sleep(1)
        try:
            opcion = int(input(""))
            if opcion < 1 or opcion > 12:
                raise IndexError
        except:
            pass
            
    