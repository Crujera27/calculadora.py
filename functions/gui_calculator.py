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

import tkinter as tk
from tkinter import messagebox
import re
from functions.calculator_functions import suma, resta, multiplicacion, division, potencia, raiz_cuadrada

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.operation_label = tk.Label(master, text="Operación:")
        self.operation_label.pack()

        self.operation_var = tk.StringVar()
        self.operation_entry = tk.Entry(master, textvariable=self.operation_var, width=50, font=("Arial", 14))
        self.operation_entry.pack()

        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack()

        self.calculate_button = tk.Button(master, text="Calcular", command=self.calculate, font=("Arial", 14))
        self.calculate_button.pack()

    def calculate(self):
        operation = self.operation_var.get()
        operation = operation.replace(" ", "")
        if not re.match(r'^[-+*/^()0-9.]+$', operation):
            messagebox.showerror("Error", "Operación no válida. Por favor, ingrese una operación válida.")
            return

        try:
            result = eval(operation)
            self.result_label.config(text="El resultado es: " + str(result))
        except Exception as e:
            messagebox.showerror("Error", "Ocurrió un error al calcular: " + str(e))

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
