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


import pyfiglet
import os
import time
from dotenv import load_dotenv

load_dotenv()

reqvar = ['WEB_USERNAME', 'WEB_PASSWORD', "WEB_SERVER_URL"]
varasuentes = [var for var in reqvar if os.getenv(var) is None]

def main(enableonline):
    print(pyfiglet.figlet_format("Calculadora.py"))
    print("Bienvenido al programa principal")

    while True:
        if(enableonline==True):
            mode = input("Por favor, elija el modo de calculadora (CLI, GUI u Online): ").lower()
        else:
             mode = input("Por favor, elija el modo de calculadora (CLI o GUI): ").lower()
        if mode == "cli":
            import functions.cli_calculator as cli_calculator
            cli_calculator.main()
            break
        elif mode == "gui":
                import functions.gui_calculator as gui_calculator
                gui_calculator.main()
                break
        elif mode == "online" and not varasuentes:
                import functions.online_calc as online_calculator
                online_calculator.main()
                break
        else:
                print("Modo no válido. Por favor, elija CLI, GUI u online.")

if varasuentes:
    print(pyfiglet.figlet_format("ERROR"))
    print("El archivo .env no ha sido configurado correctamente. Los siguientes saltos no están presentes:", ", ".join(varasuentes))
    print("Si aún no has configurado el archivo .env, renombra el archivo .env.example a .env y rellana los datos con tu URL de la calculadora externa.")
    print("Voy a intentar seguir ejecutándome, pero la funcionalidad de la calculadora online no estará disponible.")
    print("Continuando en tres segundos...")
    time.sleep(3)
    main(False)
else:
    main(True)
