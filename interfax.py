# Importo el modulo tkinter
import tkinter

# Importo las funciones
import funciones

# Creo la ventana y la guardo en una variable
ventana_principal = tkinter.Tk()

# Dimesiono la ventana
ventana_principal.geometry('500x500')

# Creacion de botones numericos
boton_cero = tkinter.Button(ventana_principal, text = '0')
boton_uno = tkinter.Button(ventana_principal, text = '1')
boton_dos = tkinter.Button(ventana_principal, text = '2')
boton_tres = tkinter.Button(ventana_principal, text = '3')
boton_cuatro = tkinter.Button(ventana_principal, text = '4')
boton_cinco = tkinter.Button(ventana_principal, text = '5')
boton_seis = tkinter.Button(ventana_principal, text = '6')
boton_siete = tkinter.Button(ventana_principal, text = '7')
boton_ocho = tkinter.Button(ventana_principal, text = '8')
boton_nueve = tkinter.Button(ventana_principal, text = '9')

# Creacion de botones de operaciones para
boton_suma = tkinter.Button(ventana_principal, text = '+')
boton_multipliacion = tkinter.Button(ventana_principal, text = 'X')
boton_resta = tkinter.Button(ventana_principal, text = '-')
boton_division = tkinter.Button(ventana_principal, text = '/')
boton_igual = tkinter.Button(ventana_principal, text = '=')
boton_coma = tkinter.Button(ventana_principal, text = '.')

# Etiqueta
etiqueta_principal = tkinter.Label(ventana_principal, text = 'Hola mundo', bg = 'green')
etiqueta_principal.pack() # La ingreso a la ventana

# Registro que va a llevar la ventana
ventana_principal.mainloop()


