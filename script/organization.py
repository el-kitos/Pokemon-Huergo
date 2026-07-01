from clases import Pokemon, SinglyLinkedList, Queue, Stack, bubble_sort, insertion_sort, quick_sort
import json

def organization_AZ(pc):
    if pc.tamaño() == 0:
        print("La lista esta vacia!")
        return []

    pc_lista = []
    actual = pc.cabeza

    while actual is not None:
        pc_lista.append(actual.dato)
        actual = actual.siguiente

    pc_lista = insertion_sort(pc_lista, "nombre")
    return pc_lista

def organization_by_type(pc):
    if pc.tamaño() == 0:
        return []

    pc_lista = []
    actual = pc.cabeza

    while actual is not None:
        pc_lista.append(actual.dato)
        actual = actual.siguiente
    pc_lista = insertion_sort(pc_lista,"tipo")

    return pc_lista

def organization_by_pc(pc):
    if pc.tamaño() == 0:
        return []

    pc_lista = []
    actual = pc.cabeza

    while actual is not None:
        pc_lista.append(actual.dato)
        actual = actual.siguiente
    pc_lista = quick_sort(pc_lista, "poder_combate")
    
    return pc_lista            
                
def mostrar_menu_org():
    print("\n--- ORGANIZAR PC ---")
    print("1) Ordenar alfabéticamente")
    print("2) Ordenar por tipo")
    print("3) Ordenar por poder de combate")
    print("4) Volver al menú principal")


def main_org(pc):
    mostrar_menu_org()
    while True:
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            organization_AZ(pc)

        elif opcion == "2":
            lista = organization_by_type(pc)
            print(lista)

        elif opcion == "3":
            lista = organization_by_pc(pc)
            print(lista)

        elif opcion == "4":
            break