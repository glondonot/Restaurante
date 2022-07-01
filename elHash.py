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
			
        def print(self):
                print('---PHONEBOOK----')
                for item in self.map:
                        if item is not None:
                                print(str(item))

recetas = HashMap()
#Desayunos
recetas.append("1","Coliflor al horno con especias")
recetas.append("Coliflor al horno con especias","5000")
recetas.append("2","Omelette de huevo")
recetas.append("Omelette de huevo","5000")
recetas.append("3","Cocochas de bacalao al pil pil")
recetas.append("Cocochas de bacalao al pil pil","13000")
recetas.append("4","Zamburiñas al horno")
recetas.append("Zamburiñas al horno","15000")

#Platos fuertes
recetas.append("5","Pechugas de pollo al horno")
recetas.append("Pechugas de pollo al horno","18000")
recetas.append("6","Tataki de bonito")
recetas.append("Tataki de bonito","99999999999999")
#Acompañamientos y ensaladas

#Bebidas






recetas.append("7","Dorada a la sidra")
recetas.append("Dorada a la sidra","99999999999999")
recetas.append("8","Pulpo al horno con patatas")
recetas.append("Pulpo al horno con patatas","99999999999999")
recetas.append("9","Lomo de cerdo al ajillo")
recetas.append("Lomo de cerdo al ajillo","99999999999999")
recetas.append("10","Solomillo de cerdo con salsa hoisin")
recetas.append("Solomillo de cerdo con salsa hoisin","99999999999999")
recetas.append("11","Lenguado a la plancha")
recetas.append("Lenguado a la plancha","99999999999999")
recetas.append("12","Bonito a la plancha")
recetas.append("Bonito a la plancha","99999999999999")
recetas.append("13","Calamares al ajillo")
recetas.append("Calamares al ajillo","99999999999999")
recetas.append("14","Batido de sandía")
recetas.append("Batido de sandía","99999999999999")
recetas.append("15","Sepia al horno")
recetas.append("Sepia al horno","99999999999999")
recetas.append("16","Bruschetta")
recetas.append("Bruschetta","99999999999999")
recetas.append("7","Dorada al horno con limón")
recetas.append("Dorada al horno con limón","99999999999999")
recetas.append("7","Puré de zanahoria")
recetas.append("Puré de zanahoria","99999999999999")
recetas.append("7","Bacalao rebozado")
recetas.append("Bacalao rebozado","99999999999999")
recetas.append("7","Provolone al horno")
recetas.append("Provolone al horno","99999999999999")
recetas.append("7","Lubina al horno con limón")
recetas.append("Lubina al horno con limón","99999999999999")
recetas.append("7","Tortilla de acelgas")
recetas.append("Tortilla de acelgas","99999999999999")
recetas.append("7","Lomo de cerdo empanado (rebozado perfecto)")
recetas.append("Lomo de cerdo empanado (rebozado perfecto)","99999999999999")
recetas.append("7","Batido de melón")
recetas.append("Batido de melón","99999999999999")
recetas.append("7","Patatas rellenas de jamón y queso al horno")
recetas.append("Patatas rellenas de jamón y queso al horno","99999999999999")
recetas.append("7","Salmón en salsa de cebolla")
recetas.append("Salmón en salsa de cebolla","99999999999999")
recetas.append("7","Flan de plátano")
recetas.append("Flan de plátano","99999999999999")
recetas.append("7","Ensaladilla rusa")
recetas.append("Ensaladilla rusa","99999999999999")
recetas.append("7","Batido de fresa y plátano")
recetas.append("Batido de fresa y plátano","99999999999999")
recetas.append("7","Casabe")
recetas.append("Casabe","99999999999999")
recetas.append("7","Hervido valenciano")
recetas.append("Hervido valenciano","99999999999999")
recetas.append("7","Ensalada de atún y huevo con mayonesa")
recetas.append("Ensalada de atún y huevo con mayonesa","99999999999999")
recetas.append("7","Carpaccio de ternera con parmesano")
recetas.append("Carpaccio de ternera con parmesano","99999999999999")
recetas.append("7","Dorada a la plancha")
recetas.append("Dorada a la plancha","99999999999999")
recetas.append("7","Paletilla de cordero al horno asada a las finas hierbas")
recetas.append("Paletilla de cordero al horno asada a las finas hierbas","99999999999999")
recetas.append("7","Salmón a la plancha fácil")
recetas.append("Salmón a la plancha fácil","99999999999999")
recetas.append("7","Barquitas de endivias")
recetas.append("Barquitas de endivias","99999999999999")
recetas.append("7","Frijoles")
recetas.append("Frijoles","99999999999999")
recetas.append("7","Fritos de rape o de pixín")
recetas.append("Fritos de rape o de pixín","99999999999999")
recetas.append("7","Muslos de pollo al horno")
recetas.append("Muslos de pollo al horno","99999999999999")
recetas.append("7","Parmentier de patata")
recetas.append("Parmentier de patata","99999999999999")
recetas.append("7","Salmón en papillote al horno con verduras")
recetas.append("Salmón en papillote al horno con verduras","99999999999999")
recetas.append("7","Solomillo de cerdo a la pimienta")
recetas.append("Solomillo de cerdo a la pimienta","99999999999999")
recetas.append("7","Uvas rellenas de queso")
recetas.append("Uvas rellenas de queso","99999999999999")

recetas.append("0Coliflor al horno con especias","Comidas Rápidas")

a = input("Elija una opcion: ")

######recordar que "a" es el NUMERO del plato en el menu
######para sacar el NOMBRE DE LOS PLATOS
Nombre_del_plato = recetas.get(str(a))
print(Nombre_del_plato)

######para el PRECIO DE LOS PLATOS
precio = int(recetas.get(recetas.get(str(a))))
print(precio) #así se saca el int del precio osea "recetas[a][2]"

#sacarle CATEGORIA DE LOS PLATOS
categoria = recetas.get("0" + recetas.get(str(a)))
print(categoria)
