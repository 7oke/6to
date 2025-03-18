import RPi.GPIO as GPIO
import random
import time

# Configuración de GPIO
BUTTONS = [17, 27, 22]  # Pines GPIO para botones
LEDS = [10, 9, 11]  # Pines GPIO para LEDs
GPIO.setmode(GPIO.BCM)

# Configurar botones como entradas con pull-up
for button in BUTTONS:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Configurar LEDs como salidas
for led in LEDS:
    GPIO.setup(led, GPIO.OUT)

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
        time.sleep(0.5)
        GPIO.output(LEDS[index - 1], GPIO.LOW)
        time.sleep(0.3)

def wait_for_button_press(timeout=3):
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
    
    while True:
        show_sequence(sequence)
        print("Repite la secuencia ahora!")
        
        for correct_button in sequence:
            pressed_button = wait_for_button_press()
            if pressed_button is None:
                print("Tiempo agotado!")
                print(f"Puntaje final: {score}")
                return score
            if pressed_button != correct_button:
                print("Error! Secuencia incorrecta.")
                print(f"Puntaje final: {score}")
                return score
            print("Correcto!")
            time.sleep(0.5)
        
        score += len(sequence)
        sequence.append(random.randint(1, 3))  # Aumentar dificultad
        print("Nivel aumentado!")
        print(f"Puntaje actual: {score}")
        time.sleep(1)
    
# Ejecución del programa
if __name__ == "__main__":
    age, gender = get_user_data()
    score = play_game()
    save_result(age, gender, score)
    GPIO.cleanup()
    print("Datos guardados en 'cognitive_test.txt'")
    print(f"Tu puntaje final fue: {score}")
