import tkinter
from estructuras import Pila
from estructuras import Queue
from estructuras import HashMap

class Graph:
    # Constructor
    def __init__(self, src, dest):
        # asigna memoria para la lista de adyacencia
        self.adjList = [[] for j in range(len(src))]
        
        # agrega bordes al graph dirigido
        for i in range(0,len(src)):
            # asignar nodo en la lista de adyacencia de src a dest
            for j in range(0, len(dest)):
                if src[i] == recetas.get("0" + dest[j]):
                    self.adjList[i].append(dest[j])
 
# Función para imprimir la representación de lista de adyacencia de un graph
    def printGraph(graph,src,p):
            print(src[p])
            for j in range(len(graph.adjList[p])):
                print(graph.adjList[p][j])



# Añadir elementos al menú, y añadirles un precio correspondiente a cada elemento
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
recetas.append("5","Tortilla de acelgas")
recetas.append("Tortilla de acelgas","16000")
recetas.append("6","Hervido valenciano")
recetas.append("Hervido valenciano","17000")
recetas.append("7","Paletilla de cordero al horno asada a las finas hierbas")
recetas.append("Paletilla de cordero al horno asada a las finas hierbas","16000")
recetas.append("8","Fritos de rape o de pixín")
recetas.append("Fritos de rape o de pixín","17000")

recetas.append("0Coliflor al horno con especias","Desayunos")
recetas.append("0Omelette de huevo","Desayunos")
recetas.append("0Cocochas de bacalao al pil pil","Desayunos")
recetas.append("0Zamburiñas al horno","Desayunos")
recetas.append("0Tortilla de acelgas","Desayunos")
recetas.append("0Hervido valenciano","Desayunos")
recetas.append("0Paletilla de cordero al horno asada a las finas hierbas","Desayunos")
recetas.append("0Fritos de rape o de pixín","Desayunos")

#Platos fuertes
recetas.append("9","Pechugas de pollo al horno")
recetas.append("Pechugas de pollo al horno","20000")
recetas.append("10","Tataki de bonito")
recetas.append("Tataki de bonito","21000")
recetas.append("11","Dorada a la sidra")
recetas.append("Dorada a la sidra","23000")
recetas.append("12","Pulpo al horno con patatas")
recetas.append("Pulpo al horno con patatas","24000")
recetas.append("13","Lomo de cerdo al ajillo")
recetas.append("Lomo de cerdo al ajillo","25000")
recetas.append("14","Solomillo de cerdo con salsa hoisin")
recetas.append("Solomillo de cerdo con salsa hoisin","26000")
recetas.append("15","Lenguado a la plancha")
recetas.append("Lenguado a la plancha","27000")
recetas.append("16","Bonito a la plancha")
recetas.append("Bonito a la plancha","28000")
recetas.append("17","Calamares al ajillo")
recetas.append("Calamares al ajillo","29000")
recetas.append("18","Sepia al horno")
recetas.append("Sepia al horno","30000")
recetas.append("19","Dorada al horno con limón")
recetas.append("Dorada al horno con limón","31000")
recetas.append("20","Bacalao rebozado")
recetas.append("Bacalao rebozado","32000")
recetas.append("21","Provolone al horno")
recetas.append("Provolone al horno","33000")
recetas.append("22","Lubina al horno con limón")
recetas.append("Lubina al horno con limón","34000")
recetas.append("23","Lomo de cerdo empanado (rebozado perfecto)")
recetas.append("Lomo de cerdo empanado (rebozado perfecto)","35000")
recetas.append("24","Salmón en salsa de cebolla")
recetas.append("Salmón en salsa de cebolla","36000")
recetas.append("25","Carpaccio de ternera con parmesano")
recetas.append("Carpaccio de ternera con parmesano","37000")
recetas.append("26","Dorada a la plancha")
recetas.append("Dorada a la plancha","38000")
recetas.append("27","Salmón a la plancha fácil")
recetas.append("Salmón a la plancha fácil","39000")
recetas.append("28","Salmón en papillote al horno con verduras")
recetas.append("Salmón en papillote al horno con verduras","40000")
recetas.append("29","Solomillo de cerdo a la pimienta")
recetas.append("Solomillo de cerdo a la pimienta","41000")

recetas.append("0Pechugas de pollo al horno","Platos fuertes")
recetas.append("0Tataki de bonito","Platos fuertes")
recetas.append("0Dorada a la sidra","Platos fuertes")
recetas.append("0Pulpo al horno con patatas","Platos fuertes")
recetas.append("0Lomo de cerdo al ajillo","Platos fuertes")
recetas.append("0Solomillo de cerdo con salsa hoisin","Platos fuertes")
recetas.append("0Lenguado a la plancha","Platos fuertes")
recetas.append("0Bonito a la plancha","Platos fuertes")
recetas.append("0Calamares al ajillo","Platos fuertes")
recetas.append("0Sepia al horno","Platos fuertes")
recetas.append("0Dorada al horno con limón","Platos fuertes")
recetas.append("0Bacalao rebozado","Platos fuertes")
recetas.append("0Provolone al horno","Platos fuertes")
recetas.append("0Lubina al horno con limón","Platos fuertes")
recetas.append("0Lomo de cerdo empanado (rebozado perfecto)","Platos fuertes")
recetas.append("0Salmón en salsa de cebolla","Platos fuertes")
recetas.append("0Carpaccio de ternera con parmesano","Platos fuertes")
recetas.append("0Dorada a la plancha","Platos fuertes")
recetas.append("0Salmón a la plancha fácil","Platos fuertes")
recetas.append("0Salmón en papillote al horno con verduras","Platos fuertes")
recetas.append("0Solomillo de cerdo a la pimienta","Platos fuertes")

#Acompañamientos
recetas.append("30","Bruschetta")
recetas.append("Bruschetta","4000")
recetas.append("31","Puré de zanahoria")
recetas.append("Puré de zanahoria","4000")
recetas.append("32","Patatas rellenas de jamón y queso al horno")
recetas.append("Patatas rellenas de jamón y queso al horno","5000")
recetas.append("33","Flan de plátano")
recetas.append("Flan de plátano","5000")
recetas.append("34","Ensaladilla rusa")
recetas.append("Ensaladilla rusa","6000")
recetas.append("35","Casabe")
recetas.append("Casabe","6000")
recetas.append("36","Ensalada de atún y huevo con mayonesa")
recetas.append("Ensalada de atún y huevo con mayonesa","7000")
recetas.append("37","Barquitas de endivias")
recetas.append("Barquitas de endivias","7000")
recetas.append("38","Frijoles")
recetas.append("Frijoles","8000")
recetas.append("39","Muslos de pollo al horno")
recetas.append("Muslos de pollo al horno","7000")
recetas.append("40","Parmentier de patata")
recetas.append("Parmentier de patata","6000")
recetas.append("41","Uvas rellenas de queso")
recetas.append("Uvas rellenas de queso","7000")

recetas.append("0Bruschetta","Acompañamientos")
recetas.append("0Puré de zanahoria","Acompañamientos")
recetas.append("0Patatas rellenas de jamón y queso al horno","Acompañamientos")
recetas.append("0Flan de plátano","Acompañamientos")
recetas.append("0Ensaladilla rusa","Acompañamientos")
recetas.append("0Casabe","Acompañamientos")
recetas.append("0Ensalada de atún y huevo con mayonesa","Acompañamientos")
recetas.append("0Barquitas de endivias","Acompañamientos")
recetas.append("0Frijoles","Acompañamientos")
recetas.append("0Muslos de pollo al horno","Acompañamientos")
recetas.append("0Parmentier de patata","Acompañamientos")
recetas.append("0Uvas rellenas de queso","Acompañamientos")

#Bebidas
recetas.append("42","Batido de sandía")
recetas.append("Batido de sandía","10000")
recetas.append("43","Batido de melón")
recetas.append("Batido de melón","11000")
recetas.append("44","Batido de fresa y plátano")
recetas.append("Batido de fresa y plátano","12000")

recetas.append("0Batido de sandía","Bebidas")
recetas.append("0Batido de melón","Bebidas")
recetas.append("0Batido de fresa y plátano","Bebidas")

categorias = ["Desayunos","Platos fuertes","Acompañamientos","Bebidas"]
platos =  ["Coliflor al horno con especias", "Omelette de huevo", "Cocochas de bacalao al pil pil", "Zamburiñas al horno",
"Pechugas de pollo al horno", "Tataki de bonito", "Dorada a la sidra", "Pulpo al horno con patatas", "Lomo de cerdo al ajillo",
"Solomillo de cerdo con salsa hoisin", "Lenguado a la plancha", "Bonito a la plancha", "Calamares al ajillo",
"Batido de sandía", "Sepia al horno", "Bruschetta", "Dorada al horno con limón", "Puré de zanahoria",
"Bacalao rebozado", "Provolone al horno", "Lubina al horno con limón", "Tortilla de acelgas", "Lomo de cerdo empanado (rebozado perfecto)",
"Batido de melón", "Patatas rellenas de jamón y queso al horno", "Salmón en salsa de cebolla", "Flan de plátano",
"Ensaladilla rusa", "Batido de fresa y plátano", "Casabe", "Hervido valenciano", "Ensalada de atún y huevo con mayonesa",
"Carpaccio de ternera con parmesano", "Dorada a la plancha", "Paletilla de cordero al horno asada a las finas hierbas",
"Salmón a la plancha fácil", "Barquitas de endivias", "Frijoles", "Fritos de rape o de pixín", "Muslos de pollo al horno",
"Parmentier de patata", "Salmón en papillote al horno con verduras", "Solomillo de cerdo a la pimienta", "Uvas rellenas de queso"]

grafo_categorias = Graph(categorias,platos)
pedidos = Queue()
ventas = Pila()
dinero = 0

def limpiarMenu():
    tituloMenu.pack_forget()
    tituloTomarPedido.pack_forget()
    tomarPedidoBot.pack_forget()
    administrarPedidosBot.pack_forget()
    administrarVentasBot.pack_forget()
    coliflorBot.pack_forget()
    menuPrincipalBot.pack_forget()
    omeletteBot.pack_forget()
    cocochasBot.pack_forget()
    zamburiñasBot.pack_forget()
    TortillaBot.pack_forget()
    hervidoBot.pack_forget()
    listaPedidosTitulo.pack_forget()
    listaPedidos.pack_forget()
    entregarPedidoBot.pack_forget()
    pedidoEntregado.pack_forget()
    administrarVentas.pack_forget()
    borrarVentaBot.pack_forget()
    borrarVentasText.pack_forget()
    agregarPedidoText.pack_forget()
    eliminarPedidoBot.pack_forget()
    pedidoEliminado.pack_forget()
    siguientePagBot.pack_forget()
    anteriorPagBot.pack_forget()
    verMenuBot.pack_forget()
    verRecestasBot.pack_forget()
    pechugasBot.pack_forget()
    tatakiBot.pack_forget()
    doradaBot.pack_forget()
    pulpoBot.pack_forget()
    lomoBot.pack_forget()
    solomilloBot.pack_forget()
    menuDesayunos.pack_forget()
    menuAlmuerzos.pack_forget()


def tomarPedido():
    limpiarMenu()
    tituloTomarPedido.pack(padx=10, pady=10)
    coliflorBot.pack(padx=10, pady=5)
    omeletteBot.pack(padx=10, pady=5)
    cocochasBot.pack(padx=10, pady=5)
    zamburiñasBot.pack(padx=10, pady=5)
    TortillaBot.pack(padx=10, pady=5)
    hervidoBot.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)
    siguientePagBot.pack(padx=10, pady=5)


def agregarPedido(a):
    global dinero
    limpiarMenu()
    agregarPedidoText["text"] = (
        "Agregando "
        + "\n"
        + recetas.get(str(a))
        + " de $"
        + str(recetas.get(recetas.get(str(a))))
        + " \n a la lista de pedidos"
    )
    agregarPedidoText.pack(padx=10, pady=5)
    tomarPedidoBot.pack(padx=10, pady=5)
    administrarPedidosBot.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)
    pedidos.enqueue(recetas.get(str(a)))
    ventas.apilar(int(recetas.get(recetas.get(str(a)))))
    ventas.apilar(recetas.get(str(a)))
    dinero += int(recetas.get(recetas.get(str(a))))


def administrarPedidos():
    limpiarMenu()
    if pedidos.length() == 0:
        listaPedidos["text"] = "Aún no hay pedidos"
        listaPedidos.pack(padx=10, pady=10)
    else:
        listaPedidos["text"] = "Los pedidos pendientes son: " + "\n" + pedidos.string()
        listaPedidos.pack(padx=10, pady=10)
        eliminarPedidoBot.pack(padx=10, pady=10)
        entregarPedidoBot.pack(padx=10, pady=10)
    menuPrincipalBot.pack(padx=10, pady=5)


def eliminarPedido():
    limpiarMenu()
    pedidoEliminado["text"] = "Pedido eliminado: " + pedidos.dequeue()
    pedidoEliminado.pack(padx=10, pady=5)
    administrarPedidosBot.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)


def entregarPedido():
    limpiarMenu()
    pedidoEntregado["text"] = "Entregando " + pedidos.head1()
    pedidoEntregado.pack(padx=10, pady=5)
    administrarPedidosBot.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)
    pedidos.dequeue()


def administrarVentas():
    global dinero
    limpiarMenu()
    if dinero == 0:
        administrarVentas["text"] = """Aún no hay ventas, el chuzo se cae a pedazos"""
        administrarVentas.pack(padx=10, pady=5)
        menuPrincipalBot.pack(padx=10, pady=5)
    else:
        administrarVentas["text"] = (
            "Las ventas son de " + str(dinero) + " $" + "\n" + ventas.string()
        )
        administrarVentas.pack(padx=10, pady=5)
        borrarVentaBot.pack(padx=10, pady=5)
        menuPrincipalBot.pack(padx=10, pady=5)


def borrarVentas():
    global dinero
    limpiarMenu()
    borrarVentasText["text"] = (
        "Borrando la ultima venta: " + "\n" + str(ventas.tope()) + "\n"
    )
    ventas.desapilar()
    borrarVentasText["text"] += str(ventas.tope())
    borrarVentasText.pack(padx=10, pady=5)
    administrarVentas.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)
    dinero -= ventas.tope()
    ventas.desapilar()


def menuPrincipal():
    limpiarMenu()
    tituloMenu.pack(padx=10, pady=10)
    tomarPedidoBot.pack(padx=10, pady=10)
    verMenuBot.pack(padx=10, pady=10)
    verRecestasBot.pack(padx=10, pady=10)
    administrarPedidosBot.pack(padx=10, pady=10)
    administrarVentasBot.pack(padx=10, pady=10)

def paginaSiguiente():
    limpiarMenu()
    pechugasBot.pack(padx=10, pady=10)
    tatakiBot.pack(padx=10, pady=10)
    doradaBot.pack(padx=10, pady=10)
    pulpoBot.pack(padx=10, pady=10)
    lomoBot.pack(padx=10, pady=10)
    solomilloBot.pack(padx=10, pady=10)
    menuPrincipalBot.pack(padx=10, pady=10)
    anteriorPagBot.pack(padx=10, pady=10)

def verMenu():
    limpiarMenu()
    menuDesayunos.pack(padx=10, pady=10)
    menuAlmuerzos.pack(padx=10, pady=10)
    menuPrincipalBot.pack(padx=10, pady=10)

fondoVentana = "#49A"
fondoBotones = "#FFA833"
ventana = tkinter.Tk()
ventana.geometry("500x600+400+100")
ventana.resizable(width=0, height=0)
ventana["bg"] = fondoVentana

tituloMenu = tkinter.Label(
    ventana, text="Bienvenido", font="Amaranth 20", bg=fondoBotones
)
tituloTomarPedido = tkinter.Label(ventana, text="TOMAR UN PEDIDO", font="Amaranth 20")
tomarPedidoBot = tkinter.Button(
    ventana,
    text="Tomar pedido",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=tomarPedido,
)
administrarPedidosBot = tkinter.Button(
    ventana,
    text="Administrar encargos",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=administrarPedidos,
    bd=5,
)

eliminarPedidoBot = tkinter.Button(
    ventana,
    text="Eliminar pedido",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=eliminarPedido,
)
entregarPedidoBot = tkinter.Button(
    ventana,
    text="Entregar pedido",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=entregarPedido,
)

administrarVentasBot = tkinter.Button(
    ventana,
    text="Administrar ventas",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=administrarVentas,
)

menuPrincipalBot = tkinter.Button(
    ventana,
    text=" Menú Principal",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=menuPrincipal,
)

coliflorBot = tkinter.Button(
    ventana,
    text="Coliflor al horno con especias: 5000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(1),
)
omeletteBot = tkinter.Button(
    ventana,
    text="Omelette de huevo: 5000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(2),
)
cocochasBot = tkinter.Button(
    ventana,
    text="Cocochas de bacalao al pil pil: 13000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(3),
)
zamburiñasBot = tkinter.Button(
    ventana,
    text="Zamburiñas al horno: 15000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(4),
)
TortillaBot = tkinter.Button(
    ventana,
    text="Tortilla de acelgas: 16000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(5),
)

hervidoBot = tkinter.Button(
    ventana,
    text="Hervido valenciano: 17000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(6),
)
pechugasBot = tkinter.Button(
    ventana,
    text="Pechugas de pollo al horno: 20000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(9),
)

tatakiBot = tkinter.Button(
    ventana,
    text="Tataki de bonito: 21000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(10),
)


doradaBot = tkinter.Button(
    ventana,
    text="Dorada a la sidra: 23000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(11),
)


pulpoBot = tkinter.Button(
    ventana,
    text="Pulpo al horno con patatas: 24000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(12),
)

lomoBot = tkinter.Button(
    ventana,
    text="Lomo de cerdo al ajillo: 25000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(13),
)

recetas.append("14","Solomillo de cerdo con salsa hoisin")
recetas.append("Solomillo de cerdo con salsa hoisin","26000")

solomilloBot = tkinter.Button(
    ventana,
    text="Solomillo de cerdo con salsa hoisin: 26000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(14),
)



siguientePagBot = tkinter.Button(
    ventana,
    text="Siguiente pagina",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=paginaSiguiente
)

anteriorPagBot = tkinter.Button(
    ventana,
    text="Pagina anterior",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=tomarPedido
)

verMenuBot = tkinter.Button(
    ventana,
    text="Observar menu",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=verMenu
)
verRecestasBot = tkinter.Button(
    ventana,
    text="Observar recetas",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones
)
xd = "Desayunos\nColiflor al horno con especias\nOmelette de huevo\nCocochas de bacalao al pil pil\nZamburiñas al horno\nTortilla de acelgas\nHervido valenciano"
menuDesayunos = tkinter.Label(
    ventana, text= xd, font="Amaranth 20"
)

Almuerzos = "Platos fuertes\nPechugas de pollo al horno\nTataki de bonito\nDorada a la sidra\nPulpo al horno con patatas\nLomo de cerdo al ajillo   \nSolomillo de cerdo con salsa hoisin"

menuAlmuerzos = tkinter.Label(
    ventana, text= Almuerzos, font="Amaranth 20"
)



listaPedidosTitulo = tkinter.Label(
    ventana, text="ESTOS SON LOS PEDIDOS", font="Amaranth 20"
)
listaPedidos = tkinter.Label(ventana, font="Amaranth 20")
pedidoEntregado = tkinter.Label(ventana, font="Amaranth 20")
pedidoEliminado = tkinter.Label(ventana, font="Amaranth 20")
administrarVentas = tkinter.Label(ventana, font="Amaranth 20")
borrarVentaBot = tkinter.Button(
    ventana,
    text="Borrar Venta",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=borrarVentas,
)
borrarVentasText = tkinter.Label(ventana, font="Amaranth 20")

agregarPedidoText = tkinter.Label(ventana, font="Amaranth 20")

tituloMenu.pack(padx=10, pady=10)
tomarPedidoBot.pack(padx=10, pady=10)
verMenuBot.pack(padx=10, pady=10)
verRecestasBot.pack(padx=10, pady=10)
administrarPedidosBot.pack(padx=10, pady=10)
administrarVentasBot.pack(padx=10, pady=10)


ventana.mainloop()