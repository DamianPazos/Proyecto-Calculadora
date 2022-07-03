# Importo el modulo tkinter
from tkinter import *

# Importo las funciones
import funciones

# Creo la ventana principal y la guardo en una variable
root = Tk()

# Nombre de la ventana
root.title('Calculadora - by Damian Pazos')

# Creacion y ubicacion de botones numericos
boton_cero = Button(root, text = '0', padx = 40, pady = 20).grid(row = 4, column = 0, sticky = W+E)
boton_uno = Button(root, text = '1', padx = 40, pady = 20).grid(row = 3, column = 0, sticky = W+E)
boton_dos = Button(root, text = '2', padx = 40, pady = 20).grid(row = 3, column = 1, sticky = W+E)
boton_tres = Button(root, text = '3', padx = 40, pady = 20).grid(row = 3, column = 2, sticky = W+E)
boton_cuatro = Button(root, text = '4', padx = 40, pady = 20).grid(row = 2, column = 0, sticky = W+E)
boton_cinco = Button(root, text = '5', padx = 40, pady = 20).grid(row = 2, column = 1, sticky = W+E)
boton_seis = Button(root, text = '6', padx = 40, pady = 20).grid(row = 2, column = 2, sticky = W+E)
boton_siete = Button(root, text = '7', padx = 40, pady = 20).grid(row = 1, column = 0, sticky = W+E)
boton_ocho = Button(root, text = '8', padx = 40, pady = 20).grid(row = 1, column = 1, sticky = W+E)
boton_nueve = Button(root, text = '9', padx = 40, pady = 20).grid(row = 1, column = 2, sticky = W+E)

# Creacion de botones de operaciones para
boton_suma = Button(root, text = '+', padx = 40, pady = 20).grid(row = 4, column = 3, sticky = W+E)
boton_multiplicacion = Button(root, text = 'X', padx = 40, pady = 20).grid(row = 2, column = 3, sticky = W+E)
boton_resta = Button(root, text = '-', padx = 40, pady = 20).grid(row = 3, column = 3, sticky = W+E)
boton_division = Button(root, text = '/', padx = 40, pady = 20).grid(row = 1, column = 3, sticky = W+E)
boton_igual = Button(root, text = '=', padx = 40, pady = 20).grid(row = 4, column = 2, sticky = W+E)
boton_coma = Button(root, text = '.', padx = 40, pady = 20).grid(row = 4, column = 1, sticky = W+E)

# Creacion de visor
display = Entry(root).grid(row = 0, columnspan = 4, sticky = W+E)

# Ubicacion del visor
#pantalla.grid(row = 0, column = 0)


# Registro que va a llevar la ventana
root.mainloop()


