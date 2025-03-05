import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(25,gpio.OUT)

gpio.output(25, True)
time.sleep(1)
gpio.output(25, False)
time.sleep(1)

gpio.cleanup()