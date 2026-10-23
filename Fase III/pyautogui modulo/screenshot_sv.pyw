from pathlib import Path
import pyautogui
from datetime import datetime

# Carpeta donde está el script
ruta_script = Path(__file__).parent

# Nombre del archivo con fecha y hora para evitar sobreescrituras
nombre_archivo = f"ss_{datetime.now():%Y%m%d_%H%M%S}.png"

# Ruta completa del screenshot
ruta_screenshot = ruta_script / nombre_archivo

# Captura y guarda
im = pyautogui.screenshot()
im.save(ruta_screenshot)

print(f"Screenshot guardado en: {ruta_screenshot}")
