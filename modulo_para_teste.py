def dividir(x, y):
    try:
        return int(x) / int(y)
    except ValueError:
        return "Valor incorreto."
    except ZeroDivisionError:
        return "Divisor não pode ser 0."

def quadrado(x):
    try:
        return float(x) ** 2
    except ValueError:
        return "Valor incorreto."

var_teste = 100