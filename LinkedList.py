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
        stringtofill = ""
        locator = self.head
        while locator is not None:
            stringtofill += str(locator.getData())
            if locator.getPoint() is not None:
                stringtofill += "\n"
            locator = locator.getPoint()
        return stringtofill + ""
