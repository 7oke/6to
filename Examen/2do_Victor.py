import os
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

LEDS = [26, 19, 13, 6, 5]

for led in LEDS:
    gpio.setup(led, gpio.OUT)
    gpio.output(led, gpio.LOW)

main = "archivos"

c1 = input("Introduce la 1er carpeta: ")
c2 = input("Introduce la 2da carpeta: ")
c3 = input("Introduce la 3er carpeta: ")
c4 = input("Introduce la 4ta carpeta: ")
c5 = input("Introduce la 5ta carpeta: ")

folders = [c1, c2, c3, c4, c5]
    
try:
    while True:
        index = 0
        
        for folder in folders:
            ruta = os.path.join(main, folder)
            
            if os.path.exists(ruta) and os.path.isdir(ruta):
                cuenta = len(os.listdir(ruta))  
                
                print(f"Carpeta {folder}: {cuenta} archivos")
                
                for _ in range(cuenta):
                    gpio.output(LEDS[index], gpio.HIGH)
                    time.sleep(0.5)
                    gpio.output(LEDS[index], gpio.LOW)
                    time.sleep(0.5)
            else:
                print(f"La carpeta {folder} no existe en {main}")
                
            index += 1
            
        time.sleep(2)  

except KeyboardInterrupt:
    print("\n Saliste prro")
    gpio.cleanup()
