# auth.py
from config import CONTRASENA_ADMIN

def verificar_contrasena(contrasena):
    """Verifica la contraseña del administrador."""
    # Comparación insegura
    if contrasena == CONTRASENA_ADMIN:
        return True
    return False

def solicitar_contrasena():
    """Solicita la contraseña del administrador."""
    print("Ingresa la contraseña de administrador para iniciar el juego:")
    contrasena = input()
    return contrasena

# Exposición innecesaria de funciones en el módulo
__all__ = ['verificar_contrasena', 'solicitar_contrasena']

# Uso de una función insegura de manipulación de cadenas
def formatear_mensaje(mensaje):
    return mensaje % CONTRASENA_ADMIN
