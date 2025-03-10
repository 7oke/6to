import RPi.GPIO as GPIO
import time
import argparse

led_pins = [26, 19, 13, 6] 

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configurar pines como salida y apagarlos inicialmente
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Configuración de argumentos
parser = argparse.ArgumentParser(description="Control de 4 LEDs en secuencia.")
parser.add_argument("--direccion", choices=["izquierda", "derecha"], default="derecha", help="Dirección de llenado de LEDs.")
parser.add_argument("--timer", type=float, default=0.5, help="Tiempo en segundos entre cambios de LED.")

args = parser.parse_args()

# Invertir el orden si la dirección es izquierda
if args.direccion == "izquierda":
    led_pins.reverse()

def secuencia_leds(timer):
    # Fase 1: Encender de 1 a 4 con apagado del anterior
    for i in range(len(led_pins)):
        if i > 0:
            GPIO.output(led_pins[i-1], GPIO.LOW)  # Apagar el anterior
        GPIO.output(led_pins[i], GPIO.HIGH)  # Encender el actual
        time.sleep(timer)
    
    # LED 4 se queda prendido
    GPIO.output(led_pins[3], GPIO.HIGH)
    
    # Fase 2: Encender 1 → 2 → 3 (con LED 4 prendido)
    for i in range(3):
        GPIO.output(led_pins[i], GPIO.HIGH)
        time.sleep(timer)
        if i > 0:
            GPIO.output(led_pins[i-1], GPIO.LOW)  # Apagar el anterior
    
    # LED 3 y LED 4 quedan prendidos
    GPIO.output(led_pins[2], GPIO.HIGH)
    
    # Fase 3: Encender 1 → 2 con LED 3 y 4 prendidos
    for i in range(2):
        GPIO.output(led_pins[i], GPIO.HIGH)
        time.sleep(timer)
        if i > 0:
            GPIO.output(led_pins[i-1], GPIO.LOW)  # Apagar el anterior
    
    # Apagar todos los LEDs al finalizar
    time.sleep(timer)
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)

try:
    secuencia_leds(args.timer)
    GPIO.cleanup()  # Limpiar configuración de GPIO

except KeyboardInterrupt:
    GPIO.cleanup()
