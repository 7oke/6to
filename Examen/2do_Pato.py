import time
import os

import RPi.GPIO as GPIO

# Define LED pins
LEDS = [26, 19, 13, 6, 5]
LED_FOLDERS = [f"/home/admin/Desktop/Examen/archivos{pin}" for pin in LEDS]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for pin in LEDS:
    GPIO.setup(pin, GPIO.OUT)

# Ensure folders exist
for folder in LED_FOLDERS:
    if not os.path.exists(folder):
        os.makedirs(folder)

try:
    while True:
        for pin, folder in zip(LEDS, LED_FOLDERS):
            # Check if the folder exists
            if os.path.exists(folder):
                # Count the number of files in the folder
                file_count = len(os.listdir(folder))
                # Blink the LED file_count times
                for _ in range(file_count):
                    GPIO.output(pin, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pin, GPIO.LOW)
                time.sleep(0.5)
            else:
                print(f"Folder {folder} does not exist.")
        # Wait for 3 seconds before repeating
        time.sleep(3)
        # Ensure all LEDs are turned off after blinking
        for pin in LEDS:
            GPIO.output(pin, GPIO.LOW)
        # Wait for 3 seconds before repeating
    GPIO.cleanup()
finally:
    GPIO.cleanup()
    