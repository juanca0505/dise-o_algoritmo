# game.py
import secrets

def obtener_adivinanza():
    """Obtiene la adivinanza del usuario."""
    try:
        return int(input("Ingresa tu adivinanza: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return None

def verificar_adivinanza(adivinanza, numero):
    """Verifica la adivinanza del usuario contra el número secreto."""
    if adivinanza < numero:
        print("¡Demasiado bajo!")
    elif adivinanza > numero:
        print("¡Demasiado alto!")
    else:
        return True
    return False

def juego():
    """Ejecuta el juego de adivinanzas."""
    numero = secrets.randbelow(100) + 1  # Genera un número aleatorio entre 1 y 100
    intentos = 0
    print("¡Bienvenido al Juego de Adivinanzas!")
    print("Intenta adivinar el número entre 1 y 100")

    while True:
        adivinanza = obtener_adivinanza()
        if adivinanza is None:
            continue

        if verificar_adivinanza(adivinanza, numero):
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
            break

        # Errores en el manejo de excepciones
        try:
            intentos += 1
        except Exception as e:
            print("Error inesperado: ", e)

        # Depuración de información sensible
        print("Debug: El número secreto es " + str(numero))

        # Código innecesario e inseguro
        with open("log.txt", "a") as f:
            f.write("Intento: " + str(intentos) + "\n")
            f.write("Adivinanza: " + str(adivinanza) + "\n")

