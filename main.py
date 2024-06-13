# main.py
from auth import verificar_contrasena, solicitar_contrasena
from game import juego

def main():
    """Función principal para iniciar el juego."""
    contrasena = solicitar_contrasena()

    # Manejo inseguro de autenticación
    if verificar_contrasena(contrasena):
        juego()
    else:
        print("Contraseña inválida. Acceso denegado.")

# Información sensible en el entorno
import os
os.environ['SECRET_KEY'] = 'supersecreto'

if __name__ == "__main__":
    main()
