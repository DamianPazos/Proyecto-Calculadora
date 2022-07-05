# Importo el modulo tkinter
from tkinter import *

# Importo las funciones
from funciones import *

# Creo la ventana principal y la guardo en una variable
root = Tk()

# Variables de GUI
input_text_numero_display_uno = StringVar()
input_text_numero_display_dos = StringVar()
input_text_operacion = StringVar()
input_text_resultado = StringVar()
operador_numerico = ''
operador_operacion = ''

# funciones de la interfaz

# Ingreso de numeros
def click_boton_numero_display_uno(valor):
    global operador_numerico
    if operador_numerico == '' and operador_operacion == '':
        operador_numerico += str(valor)
        input_text_numero_display_uno.set(operador_numerico)
    elif operador_numerico != '' and operador_operacion == '':
        operador_numerico += str(valor)
        input_text_numero_display_uno.set(operador_numerico)

def click_boton_numero_display_dos(valor):
    global operador_numerico
    if operador_numerico == '' and operador_operacion != '':
        operador_numerico += str(valor)
        input_text_numero_display_dos.set(operador_numerico)
    elif operador_numerico != '' and operador_operacion != '':
        operador_numerico += str(valor)
        input_text_numero_display_dos.set(operador_numerico)

# Ingreso de operador
def click_boton_operacion(valor):
    global operador_operacion
    global operador_numerico
    operador_numerico = ''
    operador_operacion = str(valor)
    input_text_operacion.set(operador_operacion)

# Operacion
def click_boton_igual():
    resultado = None
    valor_uno = float(input_text_numero_display_uno.get())
    valor_dos = float(input_text_numero_display_dos.get())
    if operador_operacion == '':
        pass
    elif operador_operacion == '+':
        resultado = suma(valor_uno, valor_dos)
        input_text_resultado.set(resultado)
    elif operador_operacion == '-':
        resultado = resta(valor_uno, valor_dos)
        input_text_resultado.set(resultado)
    elif operador_operacion == '*':
        resultado = multiplicacion(valor_uno, valor_dos)
        input_text_resultado.set(resultado)
    elif operador_operacion == '/':
        resultado = division(valor_uno, valor_dos)
        input_text_resultado.set(resultado)

# Elementos de la interfaz

# Nombre de la ventana
root.title('Calculadora - by Damian Pazos')

# Creacion y ubicacion de botones numericos
boton_cero = Button(root, text = '0', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno(0), click_boton_numero_display_dos(0)]).grid(row = 6, column = 0, sticky = W+E)
boton_uno = Button(root, text = '1', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno(1), click_boton_numero_display_dos(1)]).grid(row = 5, column = 0, sticky = W+E)
boton_dos = Button(root, text = '2', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno(2), click_boton_numero_display_dos(2)]).grid(row = 5, column = 1, sticky = W+E)
boton_tres = Button(root, text = '3', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno(3), click_boton_numero_display_dos(3)]).grid(row = 5, column = 2, sticky = W+E)
boton_cuatro = Button(root, text = '4', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno(4), click_boton_numero_display_dos(4)]).grid(row = 4, column = 0, sticky = W+E)
boton_cinco = Button(root, text = '5', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno(5), click_boton_numero_display_dos(5)]).grid(row = 4, column = 1, sticky = W+E)
boton_seis = Button(root, text = '6', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno(6), click_boton_numero_display_dos(6)]).grid(row = 4, column = 2, sticky = W+E)
boton_siete = Button(root, text = '7', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno(7), click_boton_numero_display_dos(7)]).grid(row = 3, column = 0, sticky = W+E)
boton_ocho = Button(root, text = '8', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno(8), click_boton_numero_display_dos(8)]).grid(row = 3, column = 1, sticky = W+E)
boton_nueve = Button(root, text = '9', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno(9),click_boton_numero_display_dos(9)]).grid(row = 3, column = 2, sticky = W+E)

# Creacion y ubicacion de botones de operaciones
boton_suma = Button(root, text = '+', padx = 40, pady = 20, command = lambda:click_boton_operacion('+')).grid(row = 6, column = 3, sticky = W+E)
boton_multiplicacion = Button(root, text = 'X', padx = 40, pady = 20, command = lambda:click_boton_operacion('*')).grid(row = 4, column = 3, sticky = W+E)
boton_resta = Button(root, text = '-', padx = 40, pady = 20, command = lambda:click_boton_operacion('-')).grid(row = 5, column = 3, sticky = W+E)
boton_division = Button(root, text = '/', padx = 40, pady = 20, command = lambda:click_boton_operacion('/')).grid(row = 3, column = 3, sticky = W+E)
boton_igual = Button(root, text = '=', padx = 40, pady = 20, command = lambda:click_boton_igual()).grid(row = 6, column = 2, sticky = W+E)
boton_coma = Button(root, text = '.', padx = 40, pady = 20, command = lambda:[click_boton_numero_display_uno('.'),click_boton_numero_display_dos('.')]).grid(row = 6, column = 1, sticky = W+E)

# Creacion de visor
display_uno = Entry(root, textvariable = input_text_numero_display_uno).grid(row = 0, column = 1, columnspan = 3, sticky = W+E)
display_dos = Entry(root, textvariable = input_text_numero_display_dos).grid(row = 1, column = 1, columnspan = 3, sticky = W+E)
display_total = Entry(root, textvariable = input_text_resultado).grid(row = 2, column = 1, columnspan = 3, sticky = W+E)
display_operacion = Entry(root, textvariable = input_text_operacion).grid(row = 0, rowspan = 3, column =0, sticky = W+E)

# Registro que va a llevar la ventana
root.mainloop()