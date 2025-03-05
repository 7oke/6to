import RPi.GPIO as GPIO
import time
import random

# Mapeo de números de LED a pines de la Raspberry Pi (modo BCM)
LED_PINS = {
    1: 5,
    2: 6,
    3: 13,
    4: 19,
    5: 26
}

def setup():
    # Configura el modo de numeración BCM
    GPIO.setmode(GPIO.BCM)
    # Configura cada pin como salida y lo pone en LOW
    for pin in LED_PINS.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def play_level(level):
    """
    Ejecuta un nivel del juego.
    El nivel determina la velocidad de parpadeo de los LEDs.
    Se genera una secuencia aleatoria, se muestran los LED en ese orden,
    y luego se pide al usuario que ingrese el orden.
    Retorna True si el usuario acierta la secuencia, False en caso contrario.
    """
    # Definimos un retardo que se reduce conforme sube el nivel (nivel 1: 1.0 seg, nivel 10: ~0.1 seg)
    delay = max(0.1, 1.0 - (level - 1) * 0.1)
    
    # Generamos una secuencia aleatoria (una permutación de los números 1 a 5)
    sequence = list(LED_PINS.keys())
    random.shuffle(sequence)
    
    print(f"\nNivel {level}: Observa la secuencia de los LEDs")
    time.sleep(1)
    
    # Se muestra la secuencia: cada LED se enciende y se apaga
    for led in sequence:
        GPIO.output(LED_PINS[led], GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(LED_PINS[led], GPIO.LOW)
        time.sleep(0.2)  # pequeña pausa entre cada LED

    # Se solicita al usuario que ingrese la secuencia
    user_input = input("Introduce el orden de encendido de los LEDs (ejemplo: 1 3 5 2 4): ")
    
    try:
        # Convertimos la entrada en una lista de enteros
        user_sequence = [int(x) for x in user_input.split()]
    except ValueError:
        print("Entrada no válida. Asegúrate de ingresar números separados por espacios.")
        return False

    # Comparamos la secuencia mostrada con la ingresada
    if user_sequence == sequence:
        print("¡Correcto!")
        return True
    else:
        print("Incorrecto. La secuencia correcta era:", sequence)
        return False

def main():
    setup()
    try:
        while True:
            level = 1
            game_won = True

            # El juego consta de 10 niveles
            while level <= 10:
                print("\n===========================")
                print(f"Iniciando nivel {level}")
                if play_level(level):
                    level += 1
                else:
                    game_won = False
                    break

            if game_won:
                print("\n¡Felicidades, ganaste el juego!")
            else:
                print("\nPerdiste el juego.")

            # Preguntamos si quiere volver a jugar
            play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
            if play_again != 's':
                break

    except KeyboardInterrupt:
        print("\nJuego interrumpido por el usuario.")

    finally:
        GPIO.cleanup()
        print("GPIO limpiado. Saliendo del programa.")

if __name__ == "__main__":
    main()
