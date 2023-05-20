import random

def obtener_eleccion_jugador():
    while True:
        eleccion = input("Elige Piedra (R), Papel (P) o Tijeras (T): ").lower()
        if eleccion in ["r", "p", "t"]:
            return eleccion
        else:
            print("Por favor, elige una opción válida.")

def obtener_eleccion_computadora():
    opciones = ["r", "p", "t"]
    return random.choice(opciones)

def determinar_resultado(eleccion_jugador, eleccion_computadora):
    if eleccion_jugador == eleccion_computadora:
        return "Empate"
    elif (
        (eleccion_jugador == "r" and eleccion_computadora == "t")
        or (eleccion_jugador == "p" and eleccion_computadora == "r")
        or (eleccion_jugador == "t" and eleccion_computadora == "p")
    ):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar_piedra_papel_tijeras():
    print("¡Bienvenido a Piedra, Papel o Tijeras!")
    while True:
        eleccion_jugador = obtener_eleccion_jugador()
        eleccion_computadora = obtener_eleccion_computadora()

        print("Tú elegiste:", eleccion_jugador)
        print("La computadora eligió:", eleccion_computadora)

        resultado = determinar_resultado(eleccion_jugador, eleccion_computadora)
        print("Resultado:", resultado)

        jugar_nuevamente = input("¿Deseas jugar nuevamente? (s/n): ")
        if jugar_nuevamente.lower() != "s":
            break

    print("¡Gracias por jugar!")

jugar_piedra_papel_tijeras()
