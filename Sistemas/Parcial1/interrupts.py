import RPi.GPIO as gpio
import time

BUTTON_PIN = 11

gpio.setmode(gpio.BCM)
gpio.setup(BUTTON_PIN,gpio.IN,pull_up_down=gpio.PUD_DOWN)

def button_callback(chanel):
    print("Boton Presionado")
    
gpio.add_event_detect(BUTTON_PIN,gpio.FALLING,callback=button_callback,bouncetime=200)

try:
    i = 0
    while True:
        print(i)
        time.sleep(1)
        i += 1
        
except KeyboardInterrupt:
        print("Saliendo")

finally:
    gpio.remove_event_detect(BUTTON_PIN)
    gpio.cleanup()
