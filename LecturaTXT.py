from LinkedList import LinkedList
from AVL import AVL
arbol = AVL()
# linked = LinkedList()

# diccionario = {}
dicc = {}

recetas = [
    "Coliflor al horno con especias",
    "Omelette de huevo",
    "Cocochas de bacalao al pil pil",
    "Zamburiñas al horno",
    "Pechugas de pollo al horno",
    "Tataki de bonito",
    "Dorada a la sidra",
    "Pulpo al horno con patatas",
    "Lomo de cerdo al ajillo",
    "Solomillo de cerdo con salsa hoisin",
    "Lenguado a la plancha",
    "Bonito a la plancha",
    "Calamares al ajillo",
    "Batido de sandía",
    "Sepia al horno",
    "Bruschetta",
    "Dorada al horno con limón",
    "Puré de zanahoria",
    "Bacalao rebozado",
    "Provolone al horno",
    "Lubina al horno con limón",
    "Tortilla de acelgas",
    "Lomo de cerdo empanado (rebozado perfecto)",
    "Batido de melón",
    "Patatas rellenas de jamón y queso al horno",
    "Salmón en salsa de cebolla",
    "Flan de plátano",
    "Ensaladilla rusa",
    "Batido de fresa y plátano",
    "Casabe",
    "Hervido valenciano",
    "Ensalada de atún y huevo con mayonesa",
    "Carpaccio de ternera con parmesano",
    "Dorada a la plancha",
    "Paletilla de cordero al horno asada a las finas hierbas",
    "Salmón a la plancha fácil",
    "Barquitas de endivias",
    "Frijoles",
    "Fritos de rape o de pixín",
    "Muslos de pollo al horno",
    "Parmentier de patata",
    "Salmón en papillote al horno con verduras",
    "Solomillo de cerdo a la pimienta",
    "Uvas rellenas de queso",
]

def crearAVL():
    arbol = AVL()
    dicc = {}

    recetas = [
        "Coliflor al horno con especias",
        "Omelette de huevo",
        "Cocochas de bacalao al pil pil",
        "Zamburiñas al horno",
        "Pechugas de pollo al horno",
        "Tataki de bonito",
        "Dorada a la sidra",
        "Pulpo al horno con patatas",
        "Lomo de cerdo al ajillo",
        "Solomillo de cerdo con salsa hoisin",
        "Lenguado a la plancha",
        "Bonito a la plancha",
        "Calamares al ajillo",
        "Batido de sandía",
        "Sepia al horno",
        "Bruschetta",
        "Dorada al horno con limón",
        "Puré de zanahoria",
        "Bacalao rebozado",
        "Provolone al horno",
        "Lubina al horno con limón",
        "Tortilla de acelgas",
        "Lomo de cerdo empanado (rebozado perfecto)",
        "Batido de melón",
        "Patatas rellenas de jamón y queso al horno",
        "Salmón en salsa de cebolla",
        "Flan de plátano",
        "Ensaladilla rusa",
        "Batido de fresa y plátano",
        "Casabe",
        "Hervido valenciano",
        "Ensalada de atún y huevo con mayonesa",
        "Carpaccio de ternera con parmesano",
        "Dorada a la plancha",
        "Paletilla de cordero al horno asada a las finas hierbas",
        "Salmón a la plancha fácil",
        "Barquitas de endivias",
        "Frijoles",
        "Fritos de rape o de pixín",
        "Muslos de pollo al horno",
        "Parmentier de patata",
        "Salmón en papillote al horno con verduras",
        "Solomillo de cerdo a la pimienta",
        "Uvas rellenas de queso",
    ]

    for i in range(44):
        temp = recetas[i]
        f = open("C:/Users/gabri/Desktop/-Restaurante-main/RecetasTXT/"+temp+'.txt', "r")
        linked = LinkedList()
        
        for linea in f:
            if linea[-1] == '\n':
                linked.append(linea[:-1])
            else:
                linked.append(linea)
        dicc.setdefault(temp, linked)
        arbol.insert(temp)
        arbol.count(temp)
    return arbol, dicc

arbol, dicc = crearAVL() 
bo = arbol.Find('Coliflor al horno con especias')
# print(dicc)
if bo:
    print(dicc['Coliflor al horno con especias'].string())


