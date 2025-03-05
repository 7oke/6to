import RPi.GPIO as gpio
import time

gpio.setmode (gpio.BCM)
gpio.setwarnings(False)

BUTTON_LEFT = 15
BUTTON_RIGHT = 18

gpio.setup(BUTTON_LEFT, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(BUTTON_RIGHT, gpio.IN, pull_up_down=gpio.PUD_DOWN)

max_contador = int(input("Hasta que numero quieres contar?"))
paso= int(input("De cuanto en cuanto quieres contar?"))

contador = 0 

print(f"Contador: {contador}")

try:
  while True:
	if gpio.input(BUTTON_LEFT) == GPIO.HIGH:
	  time.sleep(1)
	  if contador == 0:
	   contador =  max_contador
	 else:
	  contador -= paso
	  if contador < 0 
