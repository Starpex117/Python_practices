def mcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida, ingrese otro numero ")
