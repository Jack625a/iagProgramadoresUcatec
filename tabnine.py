import tkinter as tk

#Clase tienda en linea
class TiendaOnline:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title="Tienda Online"

        #Pantalla principal
        self.frame_Principal=tk.Frame(self.ventana)
        self.frame_Principal.pack()

        #Titulo
        self.label_titulo=tk.Label(self.frame_Principal, text="Bienvenido ")
        self.label_titulo.pack()

        self.boton_productos=tk.Button(self.frame_Principal, text="Mostrar Productos", command= self.ver_productos)
        self.boton_productos.pack()

    #Funcion para verProductos
    def ver_productos(self):
        #Datos en lista simple de los productos
        produtos=["Producto1","Producto2","Producto3","Producto4","Producto5"]


        #Ocultar la pantalla principal
        self.frame_Principal.pack_forget()

        self.frame_Productos=tk.Frame(self.ventana)
        self.frame_Productos.pack()

        #Titutlo principal del frame productos con estilos
        self.label_titulo_productos=tk.Label(self.frame_Productos, text="Productos Disponibles", font=("Arial", 20))
        self.label_titulo_productos.pack()
        
        
        #self.label_productos=tk.Label(self.frame_Productos, text="Productos")
        #self.label_productos.pack()

        #Recorrido a los productos
        for producto in produtos:
            tk.Label(self.frame_Productos, text=producto).pack()

#Mostra la ventana
if __name__ == "__main__":
    ventana=tk.Tk()
    tiendaUcatec=TiendaOnline(ventana)
    ventana.mainloop()

    