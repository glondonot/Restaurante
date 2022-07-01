class Node:
    def __init__(self, elemento):
        self.point = None
        self.data = elemento
    def getData(self):
        return self.data
    def setPoint(self, point):
        self.point = point
    def getPoint(self):
        return self.point


class LinkedList:
    def __init__(self):
        self.sizeLinked = 0
        self.head = None

    def length(self):
        return self.sizeLinked

    def vacio(self):
        if self.head is None:
            return True
        else:
            return False

    def append(self, data):
        if self.vacio():
            self.head = Node(data)
        else:
            locator = self.head
            while locator.getPoint() is not None:
                locator = locator.getPoint()
            locator.setPoint(Node(data))
        self.sizeLinked += 1

    def elementoEn(self, index):
        locator = self.head
        for i in range(index):
            locator = locator.getPoint()
        return locator.getData()

    def string(self):
        stringtofill = "["
        locator = self.head
        while locator is not None:
            stringtofill += str(locator.getData())
            if locator.getPoint() is not None:
                stringtofill += ", "
            locator = locator.getPoint()
        return stringtofill + "]"

class Queue:
    def __init__(self):
        self.sizeQueue = 0
        self.head = None
        self.tail = None
    def length(self):
        return self.sizeQueue
    def vacio(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False
    def enqueue(self, data):
        temporal = Node(data)
        if self.vacio():
            self.head = self.tail = temporal
        else:
            self.tail.point = temporal
            self.tail = self.tail.getPoint()
        self.sizeQueue += 1

    def dequeue(self):
        data = self.head.getData()
        if self.vacio() == False and self.sizeQueue > 1:
            self.head = self.head.getPoint()
        if self.sizeQueue == 1:
            self.head = None
            self.tail = None
        self.sizeQueue -= 1
        return data

    def elementoEn(self, index):
        locator = self.head
        for i in range(0, index):
            locator = locator.getPoint()
        return locator.data
    def head1(self):
        return self.head.getData()
    def string(self):
        stringtofill = ""
        locator = self.head
        while locator is not None:
            stringtofill += (str(locator.getData())+ '\n')
            locator = locator.getPoint()
        return stringtofill
class Pila:
    def __init__(self):
        self.superior = None

    def apilar(self, dato):
        #print(f"Agregando {dato} en la cima de la pila")
        # Si no hay datos, agregamos el valor en el elemento superior y regresamos
        if self.superior == None:
            self.superior = Node(dato)
            return
        nuevo_nodo = Node(dato)
        nuevo_nodo.setPoint(self.superior)
        self.superior = nuevo_nodo

    def desapilar(self):
        # Si no hay datos en el nodo superior, regresamos
        if self.superior == None:
            print("No hay ningún elemento en la pila para desapilar")
            return

        #print(f"Desapilar {self.superior.dato}")
        self.superior = self.superior.getPoint()

    def string(self):
        stringtofill = ""
        locator = self.superior
        while locator is not None:
            stringtofill += (str(locator.getData())+ '\n')
            locator = locator.getPoint()
        return stringtofill
    def tope(self):
        return self.superior.getData()

class HashMap:
        def __init__(self):
                self.size = 6
                self.map = [None] * self.size
		
        def _get_hash(self, key):
                hash = 0
                for char in str(key):
                        hash += ord(char)
                return hash % self.size
		
        def append(self, key, value):
                key_hash = self._get_hash(key)
                key_value = [key, value]
		
                if self.map[key_hash] is None:
                        self.map[key_hash] = list([key_value])
                        return True
                else:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        return True
                        self.map[key_hash].append(key_value)
                        return True
			
        def get(self, key):
                key_hash = self._get_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        return pair[1]
                return None
