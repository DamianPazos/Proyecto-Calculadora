# Desarrollo de funciones de la Calculadora

# Operaciones
def suma(valor_uno, valor_dos):
    resultado = valor_uno + valor_dos
    return str(resultado)

def resta(valor_uno, valor_dos):
    resultado = valor_uno - valor_dos
    return str(resultado)

def multiplicacion(valor_uno, valor_dos):
    resultado = valor_uno * valor_dos
    return str(resultado)

def division(valor_uno, valor_dos):
    if valor_dos == 0:
        return 'No se puede dividir por cero (0)'
    else:
        resultado = valor_uno / valor_dos
        return str(resultado)

# Validador de numeros float
def validar_float(numero):
    contador = 0
    if numero[0] == '.' or numero[-1] == '.':
        return False
    for i in numero:
        if i == '.':
            contador += 1
    if contador == 0 or contador == 1:
        return True
    else:
        return False