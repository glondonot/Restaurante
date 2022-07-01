from printy import printy
class NodeTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class AVL:
    def __init__(self):
        self.root = NodeTree(None)
        self.maximun = []
        self.minimun = []
        self.dic = {}
        self.height = 0
        self.cont = 0
        self.X = NodeTree(None)
        self.numberNodeTrees = 0
        self.nodoPiv = None

    def __insertar(self, nodo,  data):
        newRoot = nodo
        if len(self.minimun) == 0:
            self.minimun = data
        if len(self.maximun) != 0 and data[0] > self.maximun[0]:
            self.maximun = data
        if len(self.minimun) != 0 and data[0] < self.minimun[0]:
            self.minimun = data

        if nodo.data == None:
                nodo.data = data
                return nodo
        else:
            if data[0]  < nodo.data[0] :
                if nodo.left is None:
                    nodo.left = NodeTree(data)
                else:
                    nodo.left = self.__insertar(nodo.left, data)
                    if self.__getHeight(nodo.left) - self.__getHeight(nodo.right)  == 2:
                        if data[0]  < nodo.left.data[0] :
                            newRoot = self.__rotSimLeft(nodo)
                        else:
                            newRoot = self.__rotDouLeft(nodo)
                    
            elif data[0]  > nodo.data[0] :
                if nodo.right is None:
                    nodo.right = NodeTree(data)
                else:
                    nodo.right = self.__insertar(nodo.right, data)
                    if self.__getHeight(nodo.right) - self.__getHeight(nodo.left) == 2:
                        if data[0]  > nodo.right.data[0] :
                            newRoot = self.__rotSimRight(nodo)
                        else:
                            newRoot = self.__rotDouRight(nodo)

        return newRoot


    def __preorder(self, nodo, data):
        if nodo is not None:
            if data[0] == nodo.data[0]:
                self.X = nodo
            self.__preorder(nodo.left, data)
            self.__preorder(nodo.right, data)

    def __preorderPrint(self, nodo):
        if nodo is not None:
            self.__preorderPrint(nodo.left)
            self.__preorderPrint(nodo.right)
            print(nodo.data)
    
    def preorderP(self):
        self.__preorderPrint(self.root)

    def __preorderCount(self, nodo):
        if nodo is not None:
            self.numberNodeTrees += 1
            self.__preorderCount(nodo.left)
            self.__preorderCount(nodo.right)

    def __getHeight(self, NodeTree):
        if NodeTree == None:
            return -1
        return 1 + max(self.__getHeight(NodeTree.left), self.__getHeight(NodeTree.right))

    def count(self, data):
        if f"{data}" in self.dic:
            self.dic[f"{data}"] += 1
        else:
            self.dic[f"{data}"] = 1

    def insert(self, data):
        self.root = self.__insertar(self.root, data)

    def FindMax(self):
        print(f"{self.maximun} {self.dic[self.maximun]}")

    def FindMin(self):
        print(f"{self.minimun} {self.dic[self.minimun]}")


    def __findMin(self, node):
            
        if node.left is None:
            printy(f'[b>]{node.data}')
        elif node is None:
            return None
        else:
            self.__findMin(node.left)
    
    def FindMini(self):
        self.__findMin(self.root)

    def Find(self, data):
        if data in self.dic:
            return True
        else:
            return False

    def HeightX(self, data):
        self.X = None
        if data[0]  > self.root.data[0] :
            self.__preorder(self.root.right, data)
        elif data[0] < self.root.data[0]:
            self.__preorder(self.root.left, data)
        else:
            self.__preorder(self.root, data)
        
        print(self.__getHeight(self.X))


    def __rotSimLeft(self, node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        return aux

    def __rotSimRight(self, node):
        aux = node.right
        node.right = aux.left
        aux.left = node
        return aux

    def __rotDouLeft(self, node):
        aux = NodeTree(None)
        node.left = self.__rotSimRight(node.left)
        aux = self.__rotSimLeft(node)
        return aux

    def __rotDouRight(self, node):
        aux = NodeTree(None)
        node.right = self.__rotSimLeft(node.right)
        aux = self.__rotSimRight(node)
        return aux

    def returnNodeTree(self, data):
        self.X = None
        if data > self.root.data:
            self.__preorder(self.root.right, data)
        elif data < self.root.data:
            self.__preorder(self.root.left, data)
        else:
            self.__preorder(self.root, data)

    def NumberNodeTrees(self,NodeTree):
        if(NodeTree==None): return 0
        return 1+self.NumberNodeTrees(NodeTree.left)+self.NumberNodeTrees(NodeTree.right)


# def main():
#     arbol = AVL()
#     #% Lista --> platos = ['nombrePlato', ingredientes = [i1, i2, i3, ...]]

#     platos = [
#         ['Ajiaco',['a','b','c','d']], 
#         ['Mondongo',['e','f','g','h']], 
#         ['Lassagna',['i','j','k','l']], 
#         ['Perro',['m','n','o','p']], 
#         ['Pizza',['q','r','s','t']],
#         ['0Ajiaco',['q','r','s','t']]
#     ]
#     for i in platos:
#         arbol.insert(i)
    
#     arbol.FindMini()

# main()

