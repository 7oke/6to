import threading
import time









suma1, suma2, suma3 , suma4 , suma5 = 0,0,0,0,0
suma6 , suma7, suma8 , suma9 , suma10 = 0,0,0,0,0
res = 0

def imprimir_numeros1():
    global suma1
    for i1 in range(1, 1001):
        suma1 += i1
        #print(f"Hilo 1: {i1}")
        time.sleep(0.001)

def imprimir_numeros2():
    global suma2
    for i2 in range(1001, 2001):
        suma2 += i2
        #print(f"Hilo 2: {i2}")
        time.sleep(0.001)

def imprimir_numeros3():
    global suma3
    for i3 in range(2001, 3001):
        suma3 += i3
        #print(f"Hilo 3: {i3}")
        time.sleep(0.001)

def imprimir_numeros4():
    global suma4
    for i4 in range(3001, 4001):
        suma4 += i4
        #print(f"Hilo 4: {i4}")
        time.sleep(0.001)

def imprimir_numeros5():
    global suma5
    for i5 in range(4001, 5001):
        suma5 += i5
        #print(f"Hilo 5: {i5}")
        time.sleep(0.001)

def imprimir_numeros6():
    global suma6
    for i6 in range(5001, 6001):
        suma6 += i6
        #print(f"Hilo 6: {i6}")
        time.sleep(0.001)

def imprimir_numeros7():
    global suma7
    for i7 in range(6001, 7001):
        suma7 += i7
        #print(f"Hilo 7: {i7}")
        time.sleep(0.001)

def imprimir_numeros8():
    global suma8
    for i8 in range(7001, 8001):
        suma8 += i8
        #print(f"Hilo 8: {i8}")
        time.sleep(0.001)  

def imprimir_numeros9():
    global suma9
    for i9 in range(8001, 9001):
        suma9 += i9
        #print(f"Hilo 9: {i9}")
        time.sleep(0.001) 

def imprimir_numeros10():
    global suma10
    for i10 in range(9001, 10001):
        suma10 += i10
        #print(f"Hilo 10: {i10}")
        time.sleep(0.001)       


hilos = [
    threading.Thread(target=imprimir_numeros1),
    threading.Thread(target=imprimir_numeros2),
    threading.Thread(target=imprimir_numeros3),
    threading.Thread(target=imprimir_numeros4),
    threading.Thread(target=imprimir_numeros5),
    threading.Thread(target=imprimir_numeros6),
    threading.Thread(target=imprimir_numeros7),
    threading.Thread(target=imprimir_numeros8),
    threading.Thread(target=imprimir_numeros9),
    threading.Thread(target=imprimir_numeros10),
]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

res = suma1 + suma2 + suma3 + suma4 + suma5 + suma6 + suma7 + suma8 + suma9 + suma10

print("Todos los hilos han finalizado.")
print(f"Resultado final: {res}")

