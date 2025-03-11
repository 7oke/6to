import os



if __name__ == "__main__":
    
        carpeta = "archivos3"
        os.makedirs(carpeta, exist_ok=True)
        usuario = input("Introduce tu nombre: ")
        
        letra_carpeta = os.path.join(carpeta, usuario[0].lower())
        os.makedirs(letra_carpeta, exist_ok=True)
        ruta = os.path.join(letra_carpeta, f'{usuario}.txt')
        add = 0
        
        while os.path.exists(ruta):
            add += 1
            ruta = os.path.join(letra_carpeta, f'{usuario}_{add}.txt')
            
        with open(ruta, 'w') as f:
            f.write(f"Nombre del usuario: {usuario}")