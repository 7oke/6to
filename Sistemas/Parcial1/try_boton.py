import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

BUTTON_LEFT = 11
BUTTON_RIGHT = 9

# Cambia de pull-down a pull-up
gpio.setup(BUTTON_LEFT, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(BUTTON_RIGHT, gpio.IN, pull_up_down=gpio.PUD_UP)

print("Prueba de botones con PULL-UP")

try:
    while True:
        if gpio.input(BUTTON_LEFT) == gpio.LOW:  # Ahora LOW indica que el botón está presionado
            print("🔴 Botón Izquierdo (GPIO 21) presionado!")
            time.sleep(0.2)

        if gpio.input(BUTTON_RIGHT) == gpio.LOW:
            print("🟢 Botón Derecho (GPIO 20) presionado!")
            time.sleep(0.2)

except KeyboardInterrupt:
    print("\nSaliendo...")
    gpio.cleanup()
