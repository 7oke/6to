import threading
import time

def imprimir_numeros():
    for i in range(1,6):
        print(f"Hilo 1: {i}")
        time.sleep(1)

# letra = ""        
# letra = "abcd"
# print(letra[0])
# print (letra)

def imprimir_letras():
    for letra in "abcdef":
        print(f"Hilo 2: {letra}")
        time.sleep(1)
        
hilo1 = threading.Thread(target = imprimir_numeros)
hilo2 = threading.Thread(target = imprimir_letras)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

