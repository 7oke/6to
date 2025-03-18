import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

# Análisis y visualización de datos
def show_results():
    try:
        with open("cognitive_test.txt", "r") as file:
            data = [line.strip().split(',') for line in file]
        
        age_scores_m = defaultdict(list)
        age_scores_f = defaultdict(list)
        
        for row in data:
            age = int(row[0])
            gender = row[1].strip().upper()
            score = int(row[2])
            if gender == "M":
                age_scores_m[age].append(score)
            elif gender == "F":
                age_scores_f[age].append(score)
        
        # Obtener todas las edades registradas
        all_ages = sorted(set(age_scores_m.keys()).union(set(age_scores_f.keys())))
        
        # Calcular el promedio de puntaje por edad y género
        avg_scores_m = [sum(age_scores_m[age])/len(age_scores_m[age]) if age in age_scores_m else 0 for age in all_ages]
        avg_scores_f = [sum(age_scores_f[age])/len(age_scores_f[age]) if age in age_scores_f else 0 for age in all_ages]
        
        x = np.arange(len(all_ages))  # Posiciones en el eje X
        width = 0.4  # Ancho de las barras
        
        plt.figure(figsize=(10, 6))
        plt.bar(x - width/2, avg_scores_m, width, color='b', label='Hombres')
        plt.bar(x + width/2, avg_scores_f, width, color='r', label='Mujeres')
        
        plt.xlabel("Edad")
        plt.ylabel("Puntaje Promedio")
        plt.title("Comparación de Desempeño Cognitivo por Edad y Género")
        plt.xticks(x, all_ages)  # Etiquetas del eje X con las edades
        plt.yticks(np.arange(0, max(avg_scores_m + avg_scores_f) + 2, 2))  # Score de 2 en 2
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Guardar la gráfica como imagen
        plt.savefig("cognitive_results.png")
        print("Gráfica guardada como 'cognitive_results.png'")
        
        plt.show()
    except FileNotFoundError:
        print("No hay datos registrados aún.")

# Ejecutar la función si el script se ejecuta directamente
if __name__ == "__main__":
    show_results()
