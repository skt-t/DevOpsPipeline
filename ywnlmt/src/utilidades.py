import os
import sys
from PIL import Image, ImageTk

# RECORDATORIO: al momento de empaquetar CAMBIAR la funcion
def obtener_ruta_assets(nombre_archivo):

    # opcion para programar
    # -------------------------------------------------------------------------------------------
    # tdos los arvhicos py son un __file__ una variable invisible que tiene cada archivo py. 
    # en este caso, __file__ es utilidades.py por lo tanto os.path.abspath toma la ruta
    # exacta de donde se encuentra utilidades.py

    # aqui os.path.dirname corta la ubicacion actual y nos deja exactamente en /ywnlmt
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # -------------------------------------------------------------------------------------------

    # opcion para el .exe
    
    # -------------------------------------------------------------------------------------------
    #MEIPASS es simplemente la variable de donde se guarda en el temp

    # BASE_DIR = sys._MEIPASS

    # -------------------------------------------------------------------------------------------
    # esto lo une todo para tomar la ruta correcta del archivo deseado
    # de \ywnlmt a \ywnlmt\assets\images\nombre_archivo
    ruta_final = os.path.join(BASE_DIR, "assets\images" , nombre_archivo)

    return ruta_final # devolvemos la ruta con la imagen

# funcionamiento exactamente igual que el anterior
def obtener_ruta_audio(nombre_asrchivo):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # BASE_DIR = sys._MEIPASS

    ruta_final = os.path.join(BASE_DIR, "assets", "audio", nombre_asrchivo)

    return ruta_final


# soluciona el problema del ruido visual en main, aqui buscamos la imagen y la entregamos
def obtener_imagen(nombre_archivo, size= None):
    
    ruta = obtener_ruta_assets(nombre_archivo) # esto es texto se lo pasamos a imagen para que lo abra

    img_pillow = Image.open(ruta) # de la ruta que tomamos, obtenemos la imagen

    # si en main le cambiamos el tamaño este if se encarga de cambiarlo
    if size is not None:
        # size llega como tupla ej:(800, 600) viene con parentesis incluido, se necesita una tupla para que resize tome los valores correctamente
        img_pillow = img_pillow.resize(size, Image.Resampling.LANCZOS) # resampling es para que tenga bordes bonitos es una operacion matematica

    return ImageTk.PhotoImage(img_pillow) # retornamos la imagen con PhotoImage
