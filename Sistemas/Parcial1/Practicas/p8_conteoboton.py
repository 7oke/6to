import RPi.GPIO as gpio
import time

# Configuración de la Raspberry Pi
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# Pines de los botones
BUTTON_UP = 11   # Botón para sumar
BUTTON_DOWN = 9  # Botón para restar

# Configurar pines como entradas con pull-up interno
gpio.setup(BUTTON_UP, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(BUTTON_DOWN, gpio.IN, pull_up_down=gpio.PUD_UP)

contador = 0  # Valor inicial

print("🚀 Contador iniciado. Presiona los botones para modificar el valor.")

try:
    while True:
        if gpio.input(BUTTON_UP) == gpio.LOW:  # Botón de suma presionado
            contador += 1
            print(f"➕ Contador: {contador}")
            time.sleep(0.2)  # Pequeño debounce para evitar lecturas dobles

        if gpio.input(BUTTON_DOWN) == gpio.LOW:  # Botón de resta presionado
            contador -= 1
            print(f"➖ Contador: {contador}")
            time.sleep(0.2)  # Pequeño debounce para evitar lecturas dobles

except KeyboardInterrupt:
    print("\nSaliendo... Limpieza de GPIO.")
    gpio.cleanup()
