import pygame
import puntajes
from constantes import *


def pantalla_final():
    fila = "0"
    pos_columna = 200
    primer_vuelta = True
    pos_fila = 190
    ancho = 0
    pygame.init()

    pygame.mixer.music.set_volume(1.0)

    sonido_boton = pygame.mixer.Sound("sonidos/sonido_boton.mp3")
    sonido_boton.set_volume(0.8)

    pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    pygame.display.set_caption("FROGGER")

    fondo = pygame.image.load("imagenes/imagen_laguna.png")
    fondo = pygame.transform.scale(fondo,(800,650))

    cartel = pygame.image.load("imagenes/cartel_grande.png")
    cartel = pygame.transform.scale(cartel,(530,525))

    cartel_menu = pygame.image.load("imagenes/cartel.png")
    cartel_menu = pygame.transform.scale(cartel_menu,(200,70))

    fuente = pygame.font.SysFont("Arial-bold",40)
    texto_lista = fuente.render(f"{fila}",True,(0,0,0))
    titulo_lista = fuente.render(f"JUGADOR  SCORE  TIME",True,(0,0,0))

    t_menu = fuente.render("MENU",True,(0,0,0))

    ejecutar = True
    while ejecutar:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                ejecutar = False
                return True
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = evento.pos
                if 500 >= pos[0] >= 300 and 90 >= pos[1] >= 20:
                    sonido_boton.play()
                    ejecutar = False

        
        if primer_vuelta:
            lista = puntajes.mostrar_datos()
            primer_vuelta = False
            lista_posiciones = []
            for i in range(len(lista)):
                pos_columna += 50
                lista_posiciones.append(pos_columna)


        pantalla.blit(fondo,(0,0,800,650))
        pantalla.blit(cartel,(135,125))
        pantalla.blit(titulo_lista,(233,200))
        pantalla.blit(cartel_menu,(300,20))
        pantalla.blit(t_menu,(360,45))
        for i in range(len(lista)):
            pos_fila = 133
            for pos,elem in enumerate(lista[i]):
                pos_fila += 100 + ancho
                texto_lista = fuente.render(f"{str(elem)}",True,(0,0,0))
                pantalla.blit(texto_lista,(pos_fila,lista_posiciones[i]))
                if pos == 0:
                    ancho = 80
                else:
                    ancho = 0
                

        pygame.display.flip()
pygame.quit()
