import pygame
import nivel_1
import puntajes
import pantalla_final
from constantes import *

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    pygame.display.set_caption("FROGGER")

    pygame.mixer.music.set_volume(1.0)

    sonido_boton = pygame.mixer.Sound("sonidos/sonido_boton.mp3")
    sonido_boton.set_volume(0.8)

    icono = pygame.image.load("imagenes/icono_rana.png")
    icono = pygame.display.set_icon(icono)

    fondo = pygame.image.load("imagenes/imagen_laguna.png")
    fondo = pygame.transform.scale(fondo,(800,650))

    cartel_1 = pygame.image.load("imagenes/cartel.png")
    cartel_1 = pygame.transform.scale(cartel_1,(200,70))

    cartel_2 = pygame.image.load("imagenes/cartel.png")
    cartel_2 = pygame.transform.scale(cartel_2,(200,70))

    cartel_3 = pygame.image.load("imagenes/cartel.png")
    cartel_3 = pygame.transform.scale(cartel_3,(200,70))

    fuente = pygame.font.SysFont("Arial-bold",40)
    t_jugar = fuente.render("JUGAR",True,(0,0,0))
    t_puntajes = fuente.render("PUNTAJES",True,(0,0,0))

    poner_nombre = False
    nombre = "_____"
    nombre_rect = pygame.Rect(355,370,200,410)

    ejecutar = True
    while ejecutar:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                ejecutar = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = list(evento.pos)
                if 300 < pos[0] < 500:
                    if 150 < pos[1] < 220:
                        sonido_boton.play()
                        puntajes.crear_tabla()
                        nivel_1.nivel_1(nombre)
                    if 250 < pos[1] < 320:
                        sonido_boton.play()
                        puntajes.crear_tabla()
                        ranking = pantalla_final.pantalla_final()
                        if ranking:
                            ejecutar = False
                    if 350 < pos[1] < 420:
                        sonido_boton.play()
                        poner_nombre = True
                        nombre = ""
                        nombre_rect = pygame.Rect(335,375,200,410)
                    else:
                        poner_nombre = False

            if evento.type == pygame.KEYDOWN and poner_nombre:
                if evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[0:-1]
                else:
                    if len(nombre) < 8:
                        nombre += evento.unicode
        
        pantalla.blit(fondo,(0,0,800,650))
        pantalla.blit(cartel_1,(300,150,200,70))
        pantalla.blit(cartel_2,(300,250,200,70))
        pantalla.blit(cartel_3,(300,350,200,70))
        pantalla.blit(t_jugar,(350,175))
        pantalla.blit(t_puntajes,(330,275))
        texto_input = fuente.render(nombre,True,(0,0,0))
        pantalla.blit(texto_input,(nombre_rect.x+5, nombre_rect.y))

        pygame.display.flip()
    pygame.quit()

main()