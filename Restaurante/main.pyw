import tkinter
from PIL import Image, ImageTk
from estructuras import Pila
from estructuras import Queue


recetas = [
    ["id", "comida", "precio"],
    ["1", "Hamburguesa", 5000],
    ["2", "HotDog", 5000],
    ["3", "Lasaña", 13000],
    ["4", "Fritanga", 15000],
    ["5", "Ajiaco", 18000],
    ["6", "FelipeGod", 99999999999999],
]

pedidos = Queue()
ventas = Pila()
dinero = 0


# Función para cambiar el icono del programa
# No olvidar agregar la ruta de su pc
def icon():
    ventana.title("Restaurantetas")
    ventana.iconbitmap(
        "C:\\Users\\nicol\\OneDrive\\Data Structures 2022-01\\Data Structures\\Proyecto\\-Restaurante\\Restaurante\\Images\\IconMain.ico"
    )


def destroyTop(top):
    top.destroy()


# No olvidar agregar la ruta de su pc
def FelipeGod():
    imagen = ImageTk.PhotoImage(
        Image.open(
            "C:\\Users\\nicol\\OneDrive\\Data Structures 2022-01\\Data Structures\\Proyecto\\-Restaurante\\Restaurante\\Images\\FelipeGod1.png"
        )
    )

    fondoVentana = "#49A"
    fondoBotones = "#FFA833"

    top = tkinter.Toplevel()

    top.geometry(
        "300x400+900+100"
    )  # Esos valores de '+900+100' sirven para posicionar la ventana en el centro de la pantalla
    top.resizable(0, 0)
    top.title("FelipeGod")
    label1 = tkinter.Label(
        top, text="FelipeGod", font="Amaranth 20", width=30, height=1
    ).pack()
    label2 = tkinter.Label(
        top, text="Precio: Invaluable", font="Amaranth 20", width=30, height=1
    ).pack()
    label3 = tkinter.Label(top, image=imagen, height=100, width=222).pack()

    button1 = tkinter.Button(
        top,
        text="Añadir a carrito",
        font="Amaranth 20",
        width=15,
        # height=1,
        bg=fondoBotones,
        command=lambda: [agregarPedido(6), destroyTop(top)],
        bd=5,
    ).pack()

    top.mainloop()


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
        + recetas[a][1]
        + " de $"
        + str(recetas[a][2])
        + " \n a la lista de pedidos"
    )
    agregarPedidoText.pack(padx=10, pady=5)
    tomarPedidoBot.pack(padx=10, pady=5)
    administrarPedidosBot.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)
    pedidos.enqueue(recetas[a][1])
    ventas.apilar(recetas[a][2])
    ventas.apilar(recetas[a][1])
    dinero += recetas[a][2]


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
icon()
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
    command=FelipeGod,
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
