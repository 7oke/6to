import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

BUTTON_PIN = 18

gpio.setup(BUTTON_PIN,gpio.IN, pull_up_down=gpio.PUD_DOWN)
# Configurar la resistencia interna como pull up
# gpio.setup(BUTTON_PIN,gpio.IN, pull_up_down=gpio.PUD_UP)

try:
	while True:
            if gpio.input(BUTTON_PIN) == gpio.HIGH:
                print("Boton presionado")
                time.sleep(1)
except(KeyboardInterrupt):
    print("Programa detenido por el usuario")
finally:
        gpio.cleanup