from calculadora import Calculadora
from validacion import pedir_numero

def mostrar_menu(calc):
    print("\n CALCULADORA ")
    print("Resultado actual:", calc.resultado_actual)
    print("\n 0) Salir, 1) Sumar, 2) Restar, 3) Multiplicar")
    print("\n 4) Dividir, 5) Potencia, 6) Raiz enesima")
    print("\n 7) Factorial, 8) Fibonacci, 9) Seno")
    print("\n 10) Coseno, 11) Tangente, 12) MCD")
    print("\n 13) MCM, 14) Calcular IVA, 15) Reiniciar")
    
def main():
    calc = Calculadora()

    while True:
        mostrar_menu(calc)
        opcion = input("\n Seleccione una opción: ")

        try:

            if opcion == "0":
                print("Cerrando calculadora ")
                break

            elif opcion in ["1","2","3","4","5"]:
                a = pedir_numero("Ingrese el primer número: ")
                b = pedir_numero("Ingrese el segundo número: ")

                match opcion:
                    case "1": calc.sumar(a, b)
                    case "2": calc.restar(a, b)
                    case "3": calc.multiplicar(a, b)
                    case "4": calc.dividir(a, b)
                    case "5": calc.potencia(a, b)

            elif opcion == "6":
                a = pedir_numero("Ingrese el número: ")
                n = pedir_numero("Ingrese el índice de la raíz: ")
                calc.raiz_enesima(a, n)

            elif opcion == "7":
                n = pedir_numero("Ingrese el número: ")
                calc.factorial(n)

            elif opcion == "8":
                n = pedir_numero("Ingrese el valor de n: ")
                calc.fibonacci(n)

            elif opcion == "9":
                x = pedir_numero("Ingrese el ángulo en grados: ")
                calc.seno(x)

            elif opcion == "10":
                x = pedir_numero("Ingrese el ángulo en grados: ")
                calc.coseno(x)

            elif opcion == "11":
                x = pedir_numero("Ingrese el ángulo en grados: ")
                calc.tangente(x)

            elif opcion == "12":
                a = pedir_numero("Ingrese el primer número: ")
                b = pedir_numero("Ingrese el segundo número: ")
                calc.maximo_comun_divisor(a, b)

            elif opcion == "13":
                a = pedir_numero("Ingrese el primer número: ")
                b = pedir_numero("Ingrese el segundo número: ")
                calc.minimo_comun_multiplo(a, b)

            elif opcion == "14":
                valor = pedir_numero("Ingrese el valor base: ")
                porcentaje = pedir_numero("Ingrese el porcentaje de IVA: ")
                calc.calcular_iva(valor, porcentaje)

            elif opcion == "15":
                calc.reiniciar()

            else:
                print("Opción inválida.")
                continue

            print("Resultado:", calc.resultado_actual)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
