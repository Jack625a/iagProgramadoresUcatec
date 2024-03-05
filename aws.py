import tkinter as tk

def borarPantalla():
    pantalla.delete(0, tk.END)

def botonClick(simbolo):
    informacion=pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, informacion + simbolo)

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

ventana=tk.Tk()
ventana.title("Calculadora")

pantalla=tk.Entry(ventana, width=30)
pantalla.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Botones de la calculadora
botones= [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "C", "=", "/"
]
fila_id=1
columna_id=0

for boton in botones:
    if boton == "=":
        boton=tk.Button(ventana, text=boton, width=10, command=calcular).grid(row=fila_id,column=columna_id)
    elif boton == "C":
        boton=tk.Button(ventana, text=boton, width=10, command=borarPantalla).grid(row=fila_id, column=columna_id)
    else:
        boton=tk.Button(ventana, text=boton, width=10, command=lambda boton=boton: botonClick(boton)).grid(row=fila_id, column=columna_id)
    
    columna_id += 1
    if columna_id > 3:
        columna_id=0
        fila_id += 1

  

ventana.mainloop()



#Funcion para sumar 2 numeros
def suma(num1, num2):
    return num1 + num2

