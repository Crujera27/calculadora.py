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
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_calculation_request(operation):
    url = os.getenv('WEB_SERVER_URL')
    params = {'operation': operation}
    auth = (os.getenv('WEB_USERNAME'), os.getenv('WEB_PASSWORD'))
    
    response = requests.get(url, params=params, auth=auth)
    
    if response.status_code == 200:
        result = response.text
        print("Resultado:", result)
    elif response.status_code == 401:
        print("Erorr del servidor: ", response.text)
        print("Autentificación fallida (HTTP 401)")
        print(os.getenv('USERNAME'), os.getenv('PASSWORD'))
    else:
        print("Error:", response.text)

def main():
    print("Continuando en el modo Online...")

    while True:
        operation = input("\nIngrese la operación ('exit' para salir): ")
        if operation.lower() == 'exit':
            print("Gracias por utilizar la calculadora online. ¡Hasta luego!")
            break
        else:
            send_calculation_request(operation)