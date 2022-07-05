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