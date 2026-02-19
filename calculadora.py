import math
from validacion import mcd

class Calculadora:

    def __init__(self):
        self.resultado_actual = 0


    def sumar(self, a, b):
        self.resultado_actual = a + b
        return self.resultado_actual

    def restar(self, a, b):
        self.resultado_actual = a - b
        return self.resultado_actual

    def multiplicar(self, a, b):
        self.resultado_actual = a * b
        return self.resultado_actual

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        self.resultado_actual = a / b
        return self.resultado_actual

    def potencia(self, a, b):
        self.resultado_actual = a ** b
        return self.resultado_actual


    def raiz_enesima(self, a, n):
        if a < 0 and n % 2 == 0:
            raise ValueError("Resultado imaginario.")
        self.resultado_actual = a ** (1/n)
        return self.resultado_actual

    def factorial(self, n):
        if n < 0 or not float(n).is_integer():
            raise ValueError("El factorial solo existe para enteros no negativos.")
        self.resultado_actual = math.factorial(int(n))
        return self.resultado_actual

    def fibonacci(self, n):
        if n < 0 or not float(n).is_integer():
            raise ValueError("Fibonacci solo definido para enteros no negativos.")
        a, b = 0, 1
        for _ in range(int(n)):
            a, b = b, a + b
        self.resultado_actual = a
        return self.resultado_actual

    def seno(self, x):
        self.resultado_actual = math.sin(math.radians(x))
        return self.resultado_actual

    def coseno(self, x):
        self.resultado_actual = math.cos(math.radians(x))
        return self.resultado_actual

    def tangente(self, x):
        self.resultado_actual = math.tan(math.radians(x))
        return self.resultado_actual


    def maximo_comun_divisor(self, a, b):
        self.resultado_actual = mcd(int(a), int(b))
        return self.resultado_actual

    def minimo_comun_multiplo(self, a, b):
        self.resultado_actual = abs(int(a)*int(b)) // mcd(int(a), int(b))
        return self.resultado_actual


    def calcular_iva(self, valor, porcentaje):
        self.resultado_actual = valor * (1 + porcentaje/100)
        return self.resultado_actual

    def reiniciar(self):
        self.resultado_actual = 0
