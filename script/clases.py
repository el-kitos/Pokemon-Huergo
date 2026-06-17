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
            print(i, ":", self.buckets[i])

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
            print(i, ":", self.buckets[i])

class Pokemon:
    def __init__(self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate
        