import RPi.GPIO as gpio
import time

# Configuración de la Raspberry Pi
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# Pines de los LEDs
LEDS = [26, 19, 13, 6, 5]

# Pines de los botones
BUTTON_LEFT = 11  # Mover a la izquierda
BUTTON_RIGHT = 9  # Mover a la derecha

# Configurar LEDs como salida
for led in LEDS:
    gpio.setup(led, gpio.OUT)
    gpio.output(led, gpio.LOW)  # Apagar todos los LEDs al inicio

# Configurar botones como entrada con pull-up interno
gpio.setup(BUTTON_LEFT, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(BUTTON_RIGHT, gpio.IN, pull_up_down=gpio.PUD_UP)

# Posición inicial del LED encendido
posicion = 2  # Empieza en el LED del centro (índice 2)

def actualizar_leds():
    """Enciende solo el LED en la posición actual y apaga los demás."""
    for i in range(len(LEDS)):
        gpio.output(LEDS[i], gpio.HIGH if i == posicion else gpio.LOW)

# Encender el LED inicial
actualizar_leds()

print("🚀 Control de LEDs iniciado. Usa los botones para mover la luz.")

try:
    while True:
        if gpio.input(BUTTON_LEFT) == gpio.LOW:  # Mover izquierda
            if posicion > 0:
                posicion -= 1
                actualizar_leds()
            print(f"⬅️ Posición: {posicion}")
            time.sleep(0.2)  # Debounce

        if gpio.input(BUTTON_RIGHT) == gpio.LOW:  # Mover derecha
            if posicion < len(LEDS) - 1:
                posicion += 1
                actualizar_leds()
            print(f"➡️ Posición: {posicion}")
            time.sleep(0.2)  # Debounce

except KeyboardInterrupt:
    print("\nSaliendo... Limpieza de GPIO.")
    gpio.cleanup()
