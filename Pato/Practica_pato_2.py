import RPi.GPIO as GPIO
import time

# Definir pines de los LEDs
led_pins = [5, 6, 13, 19, 26]

# Configurar GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Pedir al usuario la velocidad de encendido0.4

try:
    delay = float(input("Ingrese la velocidad de encendido en segundos (ejemplo: 0.5): "))
except ValueError:
    print("Entrada inválida, se usará velocidad por defecto de 0.5s")
    delay = 0.5

def run_sequence(order):
    """
    Función que ejecuta la secuencia de acumulación.
    'order' es la lista de pines en el orden en el que se ejecuta la secuencia.
    """
    n = len(order)
    # Asegurarse de que todos los LED estén apagados
    for pin in order:
        GPIO.output(pin, GPIO.LOW)
    # Ejecutar la secuencia:
    # En cada iteración se encienden temporalmente los LED's desde el principio hasta el último LED sin fijar.
    # Al final de cada iteración se fija (deja encendido) el LED en la posición (n - j - 1).
    for j in range(n):
        for i in range(n - j):
            GPIO.output(order[i], GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(order[i], GPIO.LOW)
        # Fijar el LED en la posición (n - j - 1)
        GPIO.output(order[n - j - 1], GPIO.HIGH)

try:
    while True:
        # Secuencia en orden normal (de izquierda a derecha, según la lista led_pins)
        run_sequence(led_pins)
        time.sleep(1)  # Espera con todos los LED fijos

        # Apagar todos antes de invertir la secuencia
        for pin in led_pins:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(0.5)

        # Secuencia invertida (de derecha a izquierda)
        run_sequence(led_pins[::-1])
        time.sleep(1)

        # Apagar todos y reiniciar
        for pin in led_pins:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Interrumpido por el usuario")
finally:
    GPIO.cleanup()
