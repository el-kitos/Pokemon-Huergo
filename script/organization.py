from clases import Pokemon, SinglyLinkedList, Queue, Stack, bubble_sort, insertion_sort, quick_sort
import json

def organization_AZ(pc):
    if pc.tamaño() != 0:
        pc.ordenar()
    else:
        print("La lista esta vacia!")
        return

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
                
        