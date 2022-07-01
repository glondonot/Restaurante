import tkinter
from estructuras import Pila
from estructuras import Queue

                                #!!!!!!!!!!!!!!!!!!!!!!no se si quieran poner esta estructura del hash en otro archivo o si acá nomás :v
                                #como sea que lo pongan recuerden borrar estos comentarios
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

# Añadir elementos al menú, y añadirles un precio correspondiente a cada elemento
recetas = HashMap()
recetas.append("1","Hamburguesa")
recetas.append("Hamburguesa","5000")
recetas.append("2","HotDog")
recetas.append("HotDog","5000")
recetas.append("3","Lasaña")
recetas.append("Lasaña","13000")
recetas.append("4","Fritanga")
recetas.append("Fritanga","15000")
recetas.append("5","Ajiaco")
recetas.append("Ajiaco","18000")
recetas.append("6","FelipeGod")
recetas.append("FelipeGod","99999999999999")

pedidos = Queue()
ventas = Pila()
dinero = 0

def limpiarMenu():
    tituloMenu.pack_forget()
    tituloTomarPedido.pack_forget()
    tomarPedidoBot.pack_forget()
    administrarPedidosBot.pack_forget()
    administrarVentasBot.pack_forget()
    hamburguesaBot.pack_forget()
    menuPrincipalBot.pack_forget()
    perroCalienteBot.pack_forget()
    lasagnaBot.pack_forget()
    fritangaBot.pack_forget()
    ajiacoBot.pack_forget()
    felipeBot.pack_forget()
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


def tomarPedido():
    limpiarMenu()
    tituloTomarPedido.pack(padx=10, pady=10)
    hamburguesaBot.pack(padx=10, pady=5)
    perroCalienteBot.pack(padx=10, pady=5)
    lasagnaBot.pack(padx=10, pady=5)
    fritangaBot.pack(padx=10, pady=5)
    ajiacoBot.pack(padx=10, pady=5)
    felipeBot.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)


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
    administrarPedidosBot.pack(padx=10, pady=10)
    administrarVentasBot.pack(padx=10, pady=10)


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

hamburguesaBot = tkinter.Button(
    ventana,
    text="1. Hamburguesa : $5.000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(1),
)
perroCalienteBot = tkinter.Button(
    ventana,
    text="2. Perro Caliente : $5.000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(2),
)
lasagnaBot = tkinter.Button(
    ventana,
    text="3. Lasaña : $13.000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(3),
)
fritangaBot = tkinter.Button(
    ventana,
    text="4. Fritanga : $5.000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(4),
)
ajiacoBot = tkinter.Button(
    ventana,
    text="5. Ajiaco : $18.000",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
    command=lambda: agregarPedido(5),
)

felipeBot = tkinter.Button(
    ventana,
    text="6. FelipeGod : invaluable",
    font="Amaranth 20",
    width=30,
    height=1,
    bg=fondoBotones,
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
administrarPedidosBot.pack(padx=10, pady=10)
administrarVentasBot.pack(padx=10, pady=10)


ventana.mainloop()
