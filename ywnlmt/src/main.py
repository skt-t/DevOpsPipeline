import tkinter as tk
import pygame
from utilidades import obtener_ruta_assets, obtener_ruta_audio, obtener_imagen
from PIL import Image, ImageTk

# ruta principal aqui corre todo
root = tk.Tk()
# inicio de audio
pygame.mixer.init()
# titulo
root.title("Letter")
# color del fondo 
root.configure(background="black")
# propiedades de la ventana
root.minsize(800, 600)
root.maxsize(800,600)
# aun no entiendo esto del todo pero define en donde aparece la ventana cuando lo corro
root.geometry("800x600+350+65")


# rectangulo canvas que usara toda la ventana
canvas = tk.Canvas(root, width=800, height=600, bg='black')
canvas.pack()

# para importar las imagenes usar logica de utilidades
# RECUERDA las capas van en el orden en el que se ejecuta el script (cascada)

# 1.- Background
# variable que guarda la foto para que la memoria no lo borre
background_heart = obtener_imagen("background.png")
# render de la imagen dentro del canvass
# los primeros numeros son las cordenadas de donde se encontrara en el canvas
bg1 = canvas.create_image(400, 300, image=background_heart, tags="background_heart")
bg2 = canvas.create_image(400, 900, image=background_heart, tags="background_heart1")

# esto lo hice con ayuda de gemini... pero el resto lo hare yo, ya entendi como funciona
# i understand it now...
def move_background():

    # Animacion del fondo
    # Velocidad de movimiento

    VELOCIDAD=1 # x pixeles por frame 

    # movemos ambas imágenes hacia ARRIBA (Y negativo)
    canvas.move(bg1, 0, -VELOCIDAD) # toma la imagen, y los numeros son cuanto se moveran, toma: [x,y]
    canvas.move(bg2, 0, -VELOCIDAD)

    # revisamos si alguna salió de la pantalla
    # canvas.coords(item) nos devuelve [x, y] del centro de la imagen
    
    # Revisar bg1
    coords1 = canvas.coords(bg1)
    # Si el centro está en -300 (significa que el borde de abajo ya salió por arriba 0)
    if coords1[1] <= -300: 
        # La teletransportamos debajo de la otra (Posición actual de bg2 + 600)
        canvas.coords(bg1, 400, canvas.coords(bg2)[1] + 600)

    # Revisar bg2
    coords2 = canvas.coords(bg2)
    if coords2[1] <= -300:
        canvas.coords(bg2, 400, canvas.coords(bg1)[1] + 600)

    # el after hace que la funcion se ejecute de nuevo despues de 20ms, repitiendo la animacion una y otra vez
    root.after(20, move_background)

move_background()


# 2.- sticker?

# 3.- CARTA
# imagenes necesarias para la animacion, nos devolvera la imagen 
# las imagenes se guardan en una lista par posteriormente seleccionarlas de la misma
letter_heart_frames = [
    obtener_imagen("letter_closed_f0.png"),
    obtener_imagen("letter_heart_f1.png"),
    obtener_imagen("letter_heart_f2.png"),
    obtener_imagen("letter_heart_f3.png"),
    obtener_imagen("letter_heart_f4.png"),
    obtener_imagen("letter_heart_f5.png"),
    obtener_imagen("letter_heart_f6.png"),
    obtener_imagen("letter_heart_f7.png"),
    obtener_imagen("letter_heart_f8.png"),
    obtener_imagen("letter_heart_f9.png"),
    obtener_imagen("letter_heart_f10.png"),
    obtener_imagen("letter_heart_f11.png"),
    obtener_imagen("letter_heart_f12.png"),
    obtener_imagen("letter_heart_f13.png"),
    obtener_imagen("letter_heart_f14.png"),
    obtener_imagen("letter_heart_f15.png"),
    obtener_imagen("letter_heart_f16.png"),
    obtener_imagen("letter_heart_f17.png"),
    obtener_imagen("letter_heart_f18.png"),
    obtener_imagen("letter_heart_f19.png"),
    obtener_imagen("letter_heart_f20.png"),
    obtener_imagen("letter_heart_f21.png"),
    obtener_imagen("letter_heart_f22.png"),
    obtener_imagen("letter_heart_f23.png"),
    obtener_imagen("letter_heart_f24.png"),
    ]

letter_opening_frames = [
    obtener_imagen("letter_heart_closed.png"),
    obtener_imagen("letter_opening_f1.png"),
    obtener_imagen("letter_opening_f2.png"),
    obtener_imagen("letter_opening_f3.png"),
    obtener_imagen("letter_opening_f4.png"),
    obtener_imagen("letter_opening_f5.png"),
    obtener_imagen("letter_opening_f6.png"),
    obtener_imagen("letter_opening_f7.png"),
    obtener_imagen("letter_opening_f8.png"),
    obtener_imagen("letter_opening_f9.png"),
    obtener_imagen("letter_opening_f10.png"),
    obtener_imagen("letter_opening_f11.png"),
    obtener_imagen("letter_opening_f12.png"),
    obtener_imagen("letter_opening_f13.png"),
    obtener_imagen("letter_opening_f14.png")
]

# guardamos la id de la imagen base para poder usarla con itemconfig
# en image=letter_heart_frames[0] colocamos la posision de la imagen con la carta cerradaa
# la accion tomara lugar cuando se inicie la funcion (con un boton mas abajo)
id_letter = canvas.create_image(400, 180, image=letter_heart_frames[0], tags="letter_heart_animation")
# tomamos el valor num_frame OJO num_frame no tiene valor hasta que el boton llama a la funcion asignandole un numero entero
def heart_animation(num_frame):
    canvas.tag_bind("letter_heart_animation", "<Button-1>", lambda e: error_sound())
    # cuando sea el primer frame: ejecutar este sonido
    if num_frame == 1:
            sfx_heart.play()
    if num_frame == 18:
        sfx_h_disappear.play()
    # se compara el numero dado por el boton (1) y se comparaa con la lista
    # si el numero de frame es menor al de la lista entramos al if
    if num_frame < len(letter_heart_frames):
        # si entramos, le asignamos el nuevo frame a id_letter, avanzando asi al otro frame de la imagen
        # la primera vez sera 1, asi que num_frame sera 1, avanzando asi en un frame
        canvas.itemconfig(id_letter, image=letter_heart_frames[num_frame])
        # root.after, lo mas importante, llama a la funcion otra vez, aumentando en 1 el numero de frame
        # esto es recursion
        # se llama a si misma ejecutandose una y otra vez hasta completar la lista
        # el caso base de esta funcion es el if, al cual entramos una y otra vez hasta quedarnos sin frames.
        # el primer numero son los milisegundos que espera root.after antes de ejecutar nuevamente la funcion
        root.after(100, heart_animation, num_frame + 1)

    else:
        # este else se encarga de cambiar a la otra animacion, cambiamos los parametros para que use la otra lista de frames
        # y le cambiamos el tag para que el boton actualizado use este tag y no el otro antiguo
        # de lo contrario estariamos ejecutando la misma animacion una y otra vez...
        canvas.itemconfig(id_letter, image=letter_opening_frames[0], tags="letter_opening_animation")
        # actualizacion del boton para que ejecute la segunda funcion
        canvas.tag_bind("letter_opening_animation", "<Button-1>", lambda e: opening_animation(1))

# este es el boton que inicia todo, toma el tag de id_letter, ya que esa es la imagen que se convertira en boton
# aqui podemos ver cuando se inica la funcion heart_animation(1), iniciando con el if, si fuera heart_animation(999) no pasaria por el if
# a menos que tenga 999 frames pero... ni que fuera animacion de 60fps
canvas.tag_bind("letter_heart_animation", "<Button-1>", lambda e: heart_animation(1)) 

def opening_animation(num_frame):
    canvas.tag_bind("letter_opening_animation", "<Button-1>", lambda e: open_and_sound())
    if num_frame == 1:
        sfx_l_open.play()
    if num_frame < len(letter_opening_frames):

        canvas.itemconfig(id_letter, image=letter_opening_frames[num_frame])

        root.after(100, opening_animation, num_frame + 1)

# abrimos el sonido y lo guardamos
# sonidos del corazon
sfx_papel = pygame.mixer.Sound(obtener_ruta_audio("paper_out.wav")) # papel fuera
sfx_heart = pygame.mixer.Sound(obtener_ruta_audio("heart_touch.wav")) # efecto de sonido del corazon
sfx_h_disappear = pygame.mixer.Sound(obtener_ruta_audio("heart_disappear.wav"))
# sonidos de la carta
sfx_l_open = pygame.mixer.Sound(obtener_ruta_audio("letter_opening.wav"))
# sonido de error
sfx_error =  pygame.mixer.Sound(obtener_ruta_audio("error.wav"))
# CANCIONES/MUSICA
music = [
    obtener_ruta_audio("ya xuki.mp3")
    # resto de canciones
]
def error_sound():
    sfx_error.play()
# funcion que reproduce el sonido de apertura
def opening_sound():
    sfx_papel.play()

# funcion de la carta, es una ventana hija de root, usando Toplevel creamos la pagina al igual que la ventana madre
def letter_window():
    letter = tk.Toplevel()
    letter.configure(background="pink")
    letter.title("Letter YOU IDIOT")
    letter.minsize(550, 350)
    letter.maxsize(550, 350)
    letter.geometry("550x350+475+130")

    canvas = tk.Canvas(letter, width=550, height=350, bg='black')
    canvas.pack()
    letter_paper = obtener_imagen("letter_paper.jpg", size=(550, 350))
    canvas.create_image(275, 175, image=letter_paper)
    canvas.image = letter_paper

    # Aqui va el contenido de la carta


# funcion con ambas funciones para que al momento de sacar la carta se ejecute el sonido
def open_and_sound():

    letter_window()

    opening_sound()


# REPRODUCCION DE MUSICA
# puntero 0, donde inicia la lista
indice_actual = 0
# variable booleana para saber si esta en pausa o no
esta_pausado = False

# funcion madre que carga la musica

# aqui viene el codigo de la musica

# render de ventana
root.mainloop()

