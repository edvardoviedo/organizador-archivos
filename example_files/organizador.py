import os
import shutil

# Ruta a la carpeta que quieres organizar
ruta_base = "C:/Users/Eduardo Oviedo/Desktop/organizar_estos"

# Diccionario de categorías y sus extensiones
categorias = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Música": [".mp3", ".wav"],
    "Python": [".py"]
}

# Crear las carpetas si no existen
for categoria in categorias:
    ruta_categoria = os.path.join(ruta_base, categoria)
    if not os.path.exists(ruta_categoria):
        os.makedirs(ruta_categoria)

# Recorrer archivos y mover según extensión
for archivo in os.listdir(ruta_base):
    ruta_archivo = os.path.join(ruta_base, archivo)

    if os.path.isfile(ruta_archivo):
        _, extension = os.path.splitext(archivo)
        for categoria, extensiones in categorias.items():
            if extension.lower() in extensiones:
                shutil.move(ruta_archivo, os.path.join(
                    ruta_base, categoria, archivo))
                break
