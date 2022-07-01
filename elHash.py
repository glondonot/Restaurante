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

Recetas_Hash = HashMap()
Recetas_Hash.append("1","Hamburguesa")
Recetas_Hash.append("Hamburguesa","5000")
Recetas_Hash.append("2","HotDog")
Recetas_Hash.append("HotDog","5000")
Recetas_Hash.append("3","Lasaña")
Recetas_Hash.append("Lasaña","13000")
Recetas_Hash.append("4","Fritanga")
Recetas_Hash.append("Fritanga","15000")
Recetas_Hash.append("5","Ajiaco")
Recetas_Hash.append("Ajiaco","18000")
Recetas_Hash.append("6","FelipeGod")
Recetas_Hash.append("FelipeGod","99999999999999")

recetas = [
    ["id", "comida", "precio"],
    ["1", "Hamburguesa", 5000],
    ["2", "HotDog", 5000],
    ["3", "Lasaña", 13000],
    ["4", "Fritanga", 15000],
    ["5", "Ajiaco", 18000],
    ["6", "FelipeGod", 99999999999999],
]

a = input("Elija una opcion 1 a 6: ")
print(Recetas_Hash.get(a)) #Así se saca el str de la comida osea "recetas[a][1]"
print(int(Recetas_Hash.get(Recetas_Hash.get(a)))) #así se saca el int del precio osea "recetas[a][2]"
