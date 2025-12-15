print("Hola desde Python 🚀")

# Ejemplo usando variables de entorno (opcional)
import os

var_str = os.getenv("VAR_STR", "sin valor")
print(f"VAR_STR recibido desde Jenkins: {var_str}")
