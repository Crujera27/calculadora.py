#   ____      _            _           _
#  / ___|__ _| | ___ _   _| | __ _  __| | ___  _ __ __ _   _ __  _   _
# | |   / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` | | '_ \| | | |
# | |__| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |_| |_) | |_| |
#  \____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_(_) .__/ \__, |
#                                                        |_|    |___/
#   Copyright (c) 2024 Ángel Crujera (angel.c@galnod.com)
# 
#       GitHub: https://github.com/Crujera27
#       Web: https://crujera.galnod.com
#       Licencia del proyecto: MIT
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from functions.calculator_functions import suma, resta, multiplicacion, division, potencia, raiz_cuadrada

def main():
    print("Continuando en el modo CLI...")

    while True:
        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz Cuadrada")
        print("0. Salir")

        opcion = input("Seleccione una operación (0-6): ")

        if opcion == "0":
            print("Gracias por utilizar la calculadora. ¡Hasta luego!")
            break
        elif opcion == "1":
            operand1 = float(input("Ingrese el primer operando: "))
            operand2 = float(input("Ingrese el segundo operando: "))
            print("El resultado es:", suma(operand1, operand2))
        elif opcion == "2":
            operand1 = float(input("Ingrese el primer operando: "))
            operand2 = float(input("Ingrese el segundo operando: "))
            print("El resultado es:", resta(operand1, operand2))
        elif opcion == "3":
            operand1 = float(input("Ingrese el primer operando: "))
            operand2 = float(input("Ingrese el segundo operando: "))
            print("El resultado es:", multiplicacion(operand1, operand2))
        elif opcion == "4":
            operand1 = float(input("Ingrese el primer operando: "))
            operand2 = float(input("Ingrese el segundo operando: "))
            try:
                print("El resultado es:", division(operand1, operand2))
            except ValueError as e:
                print("Error:", e)
        elif opcion == "5":
            operand1 = float(input("Ingrese la base: "))
            operand2 = float(input("Ingrese el exponente: "))
            print("El resultado es:", potencia(operand1, operand2))
        elif opcion == "6":
            operand = float(input("Ingrese el número: "))
            try:
                print("El resultado es:", raiz_cuadrada(operand))
            except ValueError as e:
                print("Error:", e)
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")