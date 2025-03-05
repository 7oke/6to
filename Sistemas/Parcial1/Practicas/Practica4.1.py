
import RPi.GPIO as gpio
import time

# Configuración de GPIO
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

# Definir pines de botones
BUTTON_LEFT = 18
BUTTON_RIGHT = 15

# Configurar botones como entrada con pull-down
gpio.setup(BUTTON_LEFT, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(BUTTON_RIGHT, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# Pedir valores iniciales al usuario
inicio = int(input("Ingrese el valor inicial: "))
fin = int(input("Ingrese el valor final: "))
salto = int(input("Ingrese el valor del salto: "))

# Variables del contador
contador = inicio

print(f"Contador iniciado en: {contador}")

try:
    while True:
        # Si se presiona el botón derecho, aumenta el contador
        if gpio.input(BUTTON_RIGHT) == gpio.HIGH:
            contador += salto
            if contador > fin:  # Si pasa el límite superior, regresa al inicio
                contador = inicio

            print(f"Contador: {contador}")
            time.sleep(0.2)  # Pequeño retardo para evitar rebotes

        # Si se presiona el botón izquierdo, disminuye el contador
        if gpio.input(BUTTON_LEFT) == gpio.HIGH:
            contador -= salto
            if contador < inicio:  # Si pasa el límite inferior, regresa al final
                contador = fin

            print(f"Contador: {contador}")
            time.sleep(0.2)  # Pequeño retardo para evitar rebotes

except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario")

finally:
    gpio.cleanup()  # Limpieza de pines GPIO
