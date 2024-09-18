import pygame
import calles
import autos
import troncos
import personaje
import nenufares
import corazon
import insecto
import puntajes
import pantalla_final
from constantes import *

def nivel_3(nombre,puntos,tiempo_total):

    choco = False
    termino = False
    tiempo_nivel = "120"
    fin_tiempo = False

    pygame.init()
    pygame.mixer.music.set_volume(1.0)
    sonido_fondo = pygame.mixer.Sound("sonidos/musica_fondo.mp3")
    sonido_fondo.set_volume(0.8)
    sonido_fondo.play(-1)

    sonido_boton = pygame.mixer.Sound("sonidos/sonido_boton.mp3")
    sonido_boton.set_volume(0.8)

    punto_simple = pygame.mixer.Sound("sonidos/punto_simple.mp3")
    punto_simple.set_volume(0.8)

    punto_bicho = pygame.mixer.Sound("sonidos/punto_bicho.mp3")
    punto_bicho.set_volume(0.8)

    sonido_game_over = pygame.mixer.Sound("sonidos/game_over.mp3")
    sonido_game_over.set_volume(0.8)

    sonido_fallo = pygame.mixer.Sound("sonidos/fallo.mp3")
    sonido_fallo.set_volume(0.8)

    sonido_next_level = pygame.mixer.Sound("sonidos/next_level.mp3")
    sonido_next_level.set_volume(0.8)

    pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    pygame.display.set_caption("FROGGER")

    reloj = pygame.time.Clock()
    tiempo_objeto = pygame.USEREVENT
    pygame.time.set_timer(tiempo_objeto,35)

    tiempo_bicho = pygame.USEREVENT + 1
    pygame.time.set_timer(tiempo_bicho,3000)

    tiempo_juego = pygame.USEREVENT + 2
    pygame.time.set_timer(tiempo_juego,1000)


    imagen_pasto = pygame.image.load("imagenes/fondo_pasto.jpg")
    imagen_pasto = pygame.transform.scale(imagen_pasto,(800,50))
    imagen_agua = pygame.image.load("imagenes/fondo_agua.jpg")
    imagen_agua = pygame.transform.scale(imagen_agua,(800,400))
    l_calles = calles.crear_lista_calles(5)

    player = personaje.crear(ANCHO_VENTANA/2,ALTO_VENTANA-42,40,45,"imagenes/abajo_1.png")
    bicho = insecto.crear(384, 32, 34, 46, "imagenes/insecto.png")
    l_corazones = corazon.crear_lista_corazones(3)
    l_troncos_der = troncos.crear_lista_troncos_der(32)
    l_troncos_izq = troncos.crear_lista_troncos_izq(32)
    l_autos_der = autos.crear_lista_autos_der(15,18000)
    l_autos_izq = autos.crear_lista_autos_izq(15,18800)
    l_nenufares = nenufares.crear_lista_nenufares(5)

    fuente_punto = pygame.font.SysFont("Arial-bold",30)
    punto = fuente_punto.render(f"Score: {puntos}",True,(0,0,0))

    fuente_tiempo = pygame.font.SysFont("Arial-bold",30)
    tiempo_jugado = fuente_tiempo.render(tiempo_nivel,True,(255,255,255))

    ejecutar = True
    while ejecutar:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sonido_fondo.stop()
                sonido_boton.play()
                ejecutar = False
            
            if evento.type == pygame.USEREVENT:
                if evento.type == tiempo_objeto:
                    autos.mover_auto_der(l_autos_der,18000)
                    autos.mover_auto_izq(l_autos_izq,18800)
                    troncos.mover_tronco_der(l_troncos_der)
                    troncos.mover_tronco_izq(l_troncos_izq)
                    colision_tronco = personaje.colision_tronco(player,l_troncos_der,l_troncos_izq)
                    if colision_tronco[0] and colision_tronco[1] == "derecha":
                        personaje.mover_personaje_der(player)
                    elif colision_tronco[0] and colision_tronco[1] == "izquierda":
                        personaje.mover_personaje_izq(player)
            
            if evento.type == pygame.USEREVENT+1:
                if evento.type == tiempo_bicho:
                    insecto.mover(bicho)
            
            if evento.type == pygame.USEREVENT+2:
                if evento.type == tiempo_juego:
                    tiempo_total += 1
                    tiempo_nivel = int(tiempo_nivel) - 1
                    tiempo_nivel = str(tiempo_nivel)
                    tiempo_nivel = tiempo_nivel.zfill(3)
                    if tiempo_nivel == "000":
                        fin_tiempo = True
                    tiempo_jugado = fuente_tiempo.render(tiempo_nivel,True,(255,255,255))

            if evento.type == pygame.KEYDOWN:
                if player["rect"].y < 300:
                    if evento.key == pygame.K_DOWN:
                        personaje.mover_personaje_y(player,50)
                    if evento.key == pygame.K_UP:
                        if player["rect"].y > 150:
                            personaje.mover_personaje_y(player,-50)
                        else:
                            personaje.mover_personaje_y(player,-70)
                elif player["rect"].y > 300:
                    if evento.key == pygame.K_UP:
                        personaje.mover_personaje_y(player,-60)
                    if evento.key == pygame.K_DOWN:
                        personaje.mover_personaje_y(player,60)

        colision_tronco = personaje.colision_tronco(player,l_troncos_der,l_troncos_izq)
        lista_teclas = pygame.key.get_pressed()
        if True in lista_teclas:
            if lista_teclas[pygame.K_LEFT]:
                if colision_tronco[0] and colision_tronco[1] == "derecha":
                    personaje.mover_personaje_x(player,-35)
                elif colision_tronco[0] and colision_tronco[1] == "izquierda":
                    personaje.mover_personaje_x(player,-10)
                else:
                    personaje.mover_personaje_x(player,-20)
            if lista_teclas[pygame.K_RIGHT]:
                if colision_tronco[0] and colision_tronco[1] == "izquierda":
                    personaje.mover_personaje_x(player,35)
                elif colision_tronco[0] and colision_tronco[1] == "derecha":
                    personaje.mover_personaje_x(player,10)
                else:
                    personaje.mover_personaje_x(player,20)

        if player["rect"].y > 300:
            if personaje.colision_auto(player,l_autos_der,l_autos_izq):
                sonido_fallo.play()
                player["vidas"] -= 1
                choco = True
                l_corazones.pop()
        else:
            colision_tronco = personaje.colision_tronco(player,l_troncos_der,l_troncos_izq)
            colision_nenufar = personaje.colision_nenufar(player,l_nenufares)
            if colision_tronco[0] == False and colision_nenufar == False:
                sonido_fallo.play()
                player["vidas"] -= 1
                choco = True
                l_corazones.pop()
            if colision_nenufar != False:
                bicho["posiciones"].remove(colision_nenufar+36)
                if len(bicho["posiciones"]) > 0:    
                    choco = True
                else:
                    termino = True
                posicion_bicho = insecto.posicion_insecto(bicho,colision_nenufar)
                if posicion_bicho:
                    puntos += 50
                    sonido_fondo.stop()
                    punto_bicho.play()
                    sonido_fondo.play(-1)
                else:
                    puntos += 10
                    sonido_fondo.stop()
                    punto_simple.play()
                    sonido_fondo.play(-1)
                punto = fuente_punto.render(f"Score: {puntos}",True,(0,0,0))
        if choco:
            player["rect"].centerx = ANCHO_VENTANA/2
            player["rect"].y = ALTO_VENTANA-42
            player["rect_col"].centerx = ANCHO_VENTANA/2
            player["rect_col"].y = ALTO_VENTANA-42
            choco = False

        
        if player["vidas"] > 0 and fin_tiempo == False and termino == False:
            pantalla.blit(imagen_agua,(0,0,800,300))
            pantalla.blit(imagen_pasto,(0,600,800,50))
            calles.pintar_calles(l_calles,pantalla)
            troncos.pintar_troncos(l_troncos_der,pantalla)
            troncos.pintar_troncos(l_troncos_izq,pantalla)
            autos.pintar_autos(l_autos_der,pantalla)
            autos.pintar_autos(l_autos_izq,pantalla)
            nenufares.pintar_nenufar(l_nenufares,pantalla)
            corazon.pintar_corazon(l_corazones,pantalla)
            personaje.pintar_personaje(player,pantalla)
            insecto.pintar_insecto(bicho,pantalla)
            reloj.tick(12)
            pantalla.blit(punto,(10,615))
            pantalla.blit(tiempo_jugado,(385,2))
        else:
            if termino:
                sonido_fondo.stop()
                puntos += 300
                punto = fuente_punto.render(f"Score: {puntos}",True,(0,0,0))
            sonido_fondo.stop()
            sonido_game_over.play()
            puntajes.agregar_jugador(nombre,int(puntos),tiempo_total)
            pantalla_final.pantalla_final()
            ejecutar = False
            
        pygame.display.flip()
pygame.quit()