
import tkinter
def extract():
    a = entry.get()
    print(a)
    
ventana = tkinter.Tk()
entry = tkinter.Entry()
entry.pack()
btnEntry = tkinter.Button(ventana, text='Buscar', command=extract)
btnEntry.pack()

ventana.mainloop()
# f = open("C:/Users/nicol/OneDrive/Data Structures 2022-01/Data Structures/Restaurante/RecetasTXT/Bacalao rebozado.txt", "r")
# array = []
# for linea in f:
#     if linea[-1] == '\n':
#         array.append(linea[:-1])
#     else:
#         array.append(linea)
# print(array)
# f.close()