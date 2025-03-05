import RPi.GPIO as gpio
import sys
import time

print(sys.argv[0])

tiempo = int(sys.argv[1])


gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(25,gpio.OUT)


try:
	while True:
		gpio.output(25,True)
		time.sleep(tiempo)
		gpio.output(25,False)
		time.sleep(tiempo)
except KeyboardInterrupt:
	print("\n adios")

gpio.cleanup()
