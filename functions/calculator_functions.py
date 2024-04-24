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

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("¡No se puede dividir por cero!")
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("¡No se puede calcular la raíz cuadrada de un número negativo!")
    return a ** 0.5