import RPi.GPIO as gpio
import time

# Desactivar advertencias y usar numeración BCM
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

# Definir pines de LEDs y botones
LEDS = [1, 7, 8, 25]
BUTTON_LEFT = 18
BUTTON_RIGHT = 15

# Configurar LEDs como salida y apagarlos
for led in LEDS:
    gpio.setup(led, gpio.OUT)
    gpio.output(led, gpio.LOW)
    
# Configurar botones como entrada con pull-down
gpio.setup(BUTTON_LEFT, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(BUTTON_RIGHT, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# Inicializar la posición del LED encendido
current_index = 0
gpio.output(LEDS[current_index], gpio.HIGH)

try:
    while True:
        # Si se presiona el botón derecho y no está en el último LED
        if gpio.input(BUTTON_RIGHT) == gpio.HIGH and current_index < len(LEDS) - 1:
            gpio.output(LEDS[current_index], gpio.LOW)  # Apagar LED actual
            current_index += 1  # Mover a la derecha
            gpio.output(LEDS[current_index], gpio.HIGH)  # Encender nuevo LED
            time.sleep(0.2)  # Pequeño retardo para evitar rebotes

        # Si se presiona el botón izquierdo y no está en el primer LED
        if gpio.input(BUTTON_LEFT) == gpio.HIGH and current_index > 0:
            gpio.output(LEDS[current_index], gpio.LOW)  # Apagar LED actual
            current_index -= 1  # Mover a la izquierda
            gpio.output(LEDS[current_index], gpio.HIGH)  # Encender nuevo LED
            time.sleep(0.2)  # Pequeño retardo para evitar rebotes

except KeyboardInterrupt:
    print("Programa detenido por el usuario")

finally:
    gpio.cleanup()  # Apagar todo al salir