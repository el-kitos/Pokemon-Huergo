import json


class HashSet:

    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def agregar(self, key):
        indice = self.hash_function(key)

        if key not in self.buckets[indice]:
            self.buckets[indice].append(key)

    def eliminar(self, key):
        indice = self.hash_function(key)

        if key in self.buckets[indice]:
            self.buckets[indice].remove(key)

    def buscar(self, key):
        indice = self.hash_function(key)

        return key in self.buckets[indice]

    def mostrar(self):
        for i in range(self.size):
            print(i, ":" , self.buckets[i])

class HashMap:

    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def agregar(self, key, value):
        indice = self.hash_function(key)

        for par in self.buckets[indice]:
            if par[0] == key:
                par[1] = value
                return

        self.buckets[indice].append([key, value])

    def buscar(self, key):
        indice = self.hash_function(key)

        for par in self.buckets[indice]:
            if par[0] == key:
                return par[1]

        return None

    def eliminar(self, key):
        indice = self.hash_function(key)

        for par in self.buckets[indice]:
            if par[0] == key:
                self.buckets[indice].remove(par)
                return

    def modificar(self, key, nuevo_valor):
        indice = self.hash_function(key)

        for par in self.buckets[indice]:
            if par[0] == key:
                par[1] = nuevo_valor
                return

    def mostrar(self):
        for i in range(self.size):
            print(str(self.buckets[i]))


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class SinglyLinkedList:
    def __init__(self):
        self.cabeza = None

    # Agregar un nodo al final
    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo

    # Buscar un nodo
    def buscar(self, dato):
        actual = self.cabeza

        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False

    # Eliminar un nodo
    def eliminar(self, dato):
        if self.cabeza is None:
            return

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return

        actual = self.cabeza

        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    # Recorrer e imprimir la lista
    def imprimir(self):
        actual = self.cabeza

        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print("La pc esta vacia.")

    # Devolver el tamaño de la lista
    def tamaño(self):
        contador = 0
        actual = self.cabeza

        while actual:
            contador += 1
            actual = actual.siguiente

        return contador

    # Chequear si está vacía
    def esta_vacia(self):
        return self.cabeza is None

    # Ordenar de menor a mayor (Bubble Sort)
    def ordenar(self):
        if self.cabeza is None:
            return

        cambiado = True

        while cambiado:
            cambiado = False
            actual = self.cabeza

            while actual.siguiente:
                if actual.dato.nombre > actual.siguiente.dato.nombre:
                    actual.dato, actual.siguiente.dato = (
                        actual.siguiente.dato,
                        actual.dato
                    )
                    cambiado = True

                actual = actual.siguiente

    # Invertir la lista (cambiando punteros)
    def invertir(self):
        anterior = None
        actual = self.cabeza

        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente

        self.cabeza = anterior

    # Detectar si hay un ciclo (Floyd tortuga y liebre)
    def tiene_ciclo(self):
        tortuga = self.cabeza
        liebre = self.cabeza

        while liebre and liebre.siguiente:
            tortuga = tortuga.siguiente
            liebre = liebre.siguiente.siguiente

            if tortuga == liebre:
                return True

        return False
    def insertar_despues_de(self, dato_objetivo, nuevo_dato):
        actual = self.cabeza

        while actual:
            if actual.dato == dato_objetivo:
                nuevo = Nodo(nuevo_dato)
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                return True
            actual = actual.siguiente

        return False


class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)
    
    def peek(self):
        print("Peek: ", self.queue[0])
    
    def isEmpty(self):
        if not self.queue:
            print("True")
        else:
            print("False")
    
    def size(self):
        print(len(self.queue))
    
        
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    
    def peek(self):
        print(self.stack[-1])
    
    def isEmpty(self):
        if not self.stack:
            print("True")
        else:
            print("False")
    
    def size(self):
        return len(self.stack)
    
    def transfer(S, T):
        while not S.isEmpty():
            T.push(S.pop())
        
class Pokemon:
    def __init__(self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate  

    def __str__(self):
        return f"{self.id}: nombre: {self.nombre} - tipo: {self.tipo} - pc: {self.poder_combate}"   

    def __repr__(self):
        return f"| id: {self.id} - nombre: {self.nombre} - tipo: {self.tipo} - pc: {self.poder_combate}"


def bubble_sort(lista):
    arr = lista[:]
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def insertion_sort(lista, atributo):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1

        if atributo == "tipo":
            while j >= 0 and lista[j].tipo > actual.tipo:
                lista[j + 1] = lista[j]
                j -= 1

        elif atributo == "poder_combate":
            while j >= 0 and lista[j].poder_combate > actual.poder_combate:
                lista[j + 1] = lista[j]
                j -= 1

        elif atributo == "nombre":
            while j >= 0 and lista[j].nombre > actual.nombre:
                lista[j + 1] = lista[j]
                j -= 1

        lista[j + 1] = actual

    return lista

def quick_sort(arr, atributo):
    if len(arr) <= 1:
        return arr

    pivote = arr[len(arr) // 2]

    if atributo == "tipo":
        menores = [x for x in arr if x.tipo < pivote.tipo]
        iguales = [x for x in arr if x.tipo == pivote.tipo]
        mayores = [x for x in arr if x.tipo > pivote.tipo]

    elif atributo == "poder_combate":
        menores = [x for x in arr if x.poder_combate < pivote.poder_combate]
        iguales = [x for x in arr if x.poder_combate == pivote.poder_combate]
        mayores = [x for x in arr if x.poder_combate > pivote.poder_combate]

    elif atributo == "nombre":
        menores = [x for x in arr if x.nombre < pivote.nombre]
        iguales = [x for x in arr if x.nombre == pivote.nombre]
        mayores = [x for x in arr if x.nombre > pivote.nombre]

    return quick_sort(menores, atributo) + iguales + quick_sort(mayores, atributo)


def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i].nombre == x:
            return i
    return -1


def busqueda_binaria(arr, x):
    izq = 0
    der = len(arr) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if arr[medio] == x:
            return medio
        elif arr[medio] < x:
            izq = medio + 1
        else:
            der = medio - 1
    return -1


