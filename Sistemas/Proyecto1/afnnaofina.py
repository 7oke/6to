import RPi.GPIO as GPIO
import random
import time
import signal
import sys
import os

# Desactivar advertencias de GPIO
GPIO.setwarnings(False)

# Configuración de GPIO
BUTTONS = [17, 27, 22]  # Pines GPIO para botones
LEDS = [10, 9, 11]  # Pines GPIO para LEDs de la secuencia
GREEN_LED = 20  # LED verde para aciertos
RED_LED = 21  # LED rojo para errores
BUZZER = 16  # Pin GPIO para el buzzer
GPIO.setmode(GPIO.BCM)

# Configurar botones como entradas con pull-up
for button in BUTTONS:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Configurar LEDs y buzzer como salidas y asegurarse de que inicien en LOW
for led in LEDS + [GREEN_LED, RED_LED]:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)  # Asegurar que los LEDs inicien apagados

GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.LOW)  # Asegurar que el buzzer inicie apagado

buzzer = GPIO.PWM(BUZZER, 1)  # Frecuencia inicial baja
buzzer.start(0)

# Manejo de interrupción con Ctrl+C
def exit_handler(signal, frame):
    print("\nInterrupción detectada. Apagando LEDs y limpiando GPIO...")
    for led in LEDS + [GREEN_LED, RED_LED]:
        GPIO.output(led, GPIO.LOW)
    GPIO.output(BUZZER, GPIO.LOW)
    GPIO.cleanup()
    print("Ejecutando Graficador.py...")
    os.system("python3 Graficador.py")
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

def play_sound(frequency, duration):
    buzzer.ChangeFrequency(frequency)
    buzzer.start(90)  # 90% de ciclo de trabajo para mayor volumen
    time.sleep(duration)
    buzzer.stop()

def save_result(age, gender, score):
    with open("cognitive_test.txt", "a") as file:
        file.write(f"{age},{gender},{score}\n")

# Captura de datos del usuario
def get_user_data():
    age = int(input("Ingrese su edad: "))
    gender = input("Ingrese su género (M/F): ").strip().upper()
    return age, gender

# Encender LED correspondiente a la secuencia
def show_sequence(sequence):
    print("Observa la secuencia...")
    for index in sequence:
        GPIO.output(LEDS[index - 1], GPIO.HIGH)
        play_sound(1000, 0.1)  # Sonido corto
        time.sleep(0.5)
        GPIO.output(LEDS[index - 1], GPIO.LOW)
        time.sleep(0.3)

def wait_for_button_press(timeout):
    start_time = time.time()
    while time.time() - start_time < timeout:
        remaining_time = timeout - (time.time() - start_time)
        print(f"Tiempo restante: {remaining_time:.1f} segundos", end="\r")
        for i, button in enumerate(BUTTONS):
            if GPIO.input(button) == GPIO.LOW:  # Cambio por PULL-UP
                time.sleep(0.3)  # Evitar rebote
                return i + 1
    print("Tiempo agotado!            ")
    return None  # Si el usuario no responde a tiempo

# Juego de memoria con dificultad progresiva
def play_game():
    sequence = [random.randint(1, 3) for _ in range(3)]  # Iniciar con 3 elementos
    score = 0
    attempts = 3  # Vidas extra
    timeout = 3  # Tiempo límite inicial
    combo = 0
    
    while True:
        print("Repite la secuencia ahora!")
        
        index = 0  # Índice para recorrer la secuencia
        while index < len(sequence):
            show_sequence([sequence[index]])  # Mostrar solo el LED actual
            pressed_button = wait_for_button_press(timeout)
            
            if pressed_button is None:
                print("Tiempo agotado!")
                attempts -= 1
            elif pressed_button != sequence[index]:
                print("Error! Secuencia incorrecta. Reiniciando desde el primer LED...")
                attempts -= 1
                GPIO.output(RED_LED, GPIO.HIGH)  # Encender LED rojo por error
                play_sound(400, 0.5)  # Sonido de error
                time.sleep(0.5)
                GPIO.output(RED_LED, GPIO.LOW)  # Apagar LED rojo
                index = 0  # Reiniciar al primer LED
                continue
            else:
                print("Correcto!")
                GPIO.output(GREEN_LED, GPIO.HIGH)  # Encender LED verde por acierto
                play_sound(1500, 0.2)  # Sonido de acierto
                time.sleep(0.5)
                GPIO.output(GREEN_LED, GPIO.LOW)  # Apagar LED verde
                index += 1
            
            if attempts == 0:
                print(f"Juego terminado! Puntaje final: {score}")
                return score
        
        score += len(sequence)
        combo += 1
        if combo % 3 == 0:
            score += 5  # Bonus por combo de 3
            print("¡Combo x3! Bonus de 5 puntos")
        sequence.append(random.randint(1, 3))  # Aumentar dificultad
        timeout = max(1.5, timeout - 0.2)  # Reducir tiempo límite con un mínimo de 1.5s
        print("Nivel aumentado!")
        print(f"Puntaje actual: {score}, Vidas restantes: {attempts}")
        play_sound(2000, 0.3)  # Sonido de nivel superado
        time.sleep(1)
    
# Ejecución del programa
if __name__ == "__main__":
    age, gender = get_user_data()
    score = play_game()
    save_result(age, gender, score)
    
    # Apagar todos los LEDs y el buzzer al finalizar
    for led in LEDS + [GREEN_LED, RED_LED]:
        GPIO.output(led, GPIO.LOW)
    GPIO.output(BUZZER, GPIO.LOW)
    GPIO.cleanup()
    
    print("Datos guardados en 'cognitive_test.txt'")
    print(f"Tu puntaje final fue: {score}")
    print("Ejecutando Graficador.py...")
    os.system("python3 Graficador.py")