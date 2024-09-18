import pygame
from constantes import *
from jugador import Jugador
from personaje import Personaje
from insecto import Insecto
import calle
import tronco
import nenufar
import auto
import corazon
import puntajes
import nivel_2
import pantalla_final

def nivel_1(nombre):

    choco = False
    termino = False
    tiempo_nivel = "120"
    fin_tiempo = False
    saltar = False
    cont_salto = 0
    cont_caminar = 0
    direccion = "derecha"
    velocidad = 10
    sonido = True

    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.0)
    sonido_fondo = pygame.mixer.Sound("sonidos/musica_fondo.mp3")
    sonido_fondo.set_volume(0.1)
    sonido_fondo.play(-1)

    sonido_boton = pygame.mixer.Sound("sonidos/sonido_boton.mp3")
    sonido_boton.set_volume(0.4)

    punto_simple = pygame.mixer.Sound("sonidos/punto_simple.mp3")
    punto_simple.set_volume(0.3)

    punto_bicho = pygame.mixer.Sound("sonidos/punto_bicho.mp3")
    punto_bicho.set_volume(0.3)

    sonido_game_over = pygame.mixer.Sound("sonidos/game_over.mp3")
    sonido_game_over.set_volume(0.3)

    sonido_fallo = pygame.mixer.Sound("sonidos/fallo.mp3")
    sonido_fallo.set_volume(0.2)

    sonido_next_level = pygame.mixer.Sound("sonidos/next_level.mp3")
    sonido_next_level.set_volume(0.5)


    pygame.init()
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
    l_calles = calle.crear_lista_calles(5)

    jugador = Jugador(nombre,0,0)
    player = Personaje(ANCHO_VENTANA/2,ALTO_VENTANA-42)
    bicho = Insecto(384, 32)
    l_corazones = corazon.crear_lista_corazones(3)
    l_troncos_der = tronco.crear_lista_troncos_der(40)
    l_troncos_izq = tronco.crear_lista_troncos_izq(40)
    l_autos_der = auto.crear_lista_autos_der(5,8000)
    l_autos_izq = auto.crear_lista_autos_izq(5,8800)
    l_nenufares = nenufar.crear_lista_nenufares(5)

    fuente_punto = pygame.font.SysFont("Arial-bold",30)
    punto = fuente_punto.render(f"Score: {jugador.puntos}",True,(0,0,0))

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
                    auto.mover_auto_der(l_autos_der,6000,velocidad)
                    auto.mover_auto_izq(l_autos_izq,6800,velocidad)
                    tronco.mover_tronco_der(l_troncos_der,velocidad)
                    tronco.mover_tronco_izq(l_troncos_izq,velocidad)
                    colision_tronco = player.colision_tronco(l_troncos_der,l_troncos_izq)
                    if colision_tronco[0]:
                        player.mover_con_tronco(colision_tronco[1],velocidad)
            
            if evento.type == pygame.USEREVENT+1:
                if evento.type == tiempo_bicho:
                    bicho.mover()
            
            if evento.type == pygame.USEREVENT+2:
                if evento.type == tiempo_juego:
                    jugador.sumar_tiempo()
                    tiempo_nivel = str(int(tiempo_nivel) - 1)
                    tiempo_nivel = tiempo_nivel.zfill(3)
                    if tiempo_nivel == "000":
                        fin_tiempo = True
                    tiempo_jugado = fuente_tiempo.render(tiempo_nivel,True,(255,255,255))

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    sonido_fondo.stop()
                    ejecutar = False
                if evento.key == pygame.K_m:
                    if sonido:
                        sonido_fondo.stop()
                        sonido = False
                    else:
                        sonido_fondo.play(-1)
                        sonido = True
                if evento.key == pygame.K_DOWN:
                    if player.rect.y < 300:
                        player.mover_y(50)
                    else:
                        player.mover_y(60)
                if evento.key == pygame.K_UP:
                    saltar = True
                    if player.rect.y < 300:
                        player.mover_y(-50)
                    else:
                        player.mover_y(-60)
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    cont_caminar = 0
            
        colision_tronco = player.colision_tronco(l_troncos_der,l_troncos_izq)
        lista_teclas = pygame.key.get_pressed()
        if True in lista_teclas:
            if lista_teclas[pygame.K_LEFT]:
                cont_caminar +=1
                direccion = "izquierda"
                if cont_caminar >= 2:
                    player.caminar(direccion)
                    if colision_tronco[0] and colision_tronco[1] == "derecha":
                        player.mover_x(-35)
                    elif colision_tronco[0] and colision_tronco[1] == "izquierda":
                        player.mover_x(-10)
                    else:
                        player.mover_x(-20)
            if lista_teclas[pygame.K_RIGHT]:
                cont_caminar += 1
                direccion = "derecha"
                if cont_caminar >= 2:
                    player.caminar(direccion)
                    if colision_tronco[0] and colision_tronco[1] == "izquierda":
                        player.mover_x(35)
                    elif colision_tronco[0] and colision_tronco[1] == "derecha":
                        player.mover_x(10)
                    else:
                        player.mover_x(20)   
        else:
            player.quieto(direccion)
        
        if saltar:
            player.saltar(direccion)
            cont_salto += 1
            if cont_salto > 2:
                saltar = False
                cont_salto = 0

        if player.rect.y >= 300:
            if player.colision_auto(l_autos_der,l_autos_izq):
                if sonido:
                    sonido_fallo.play()
                player.quitar_vida()
                choco = True
                l_corazones.pop()
        else:
            colision_tronco = player.colision_tronco(l_troncos_der,l_troncos_izq)
            colision_nenufar = player.colision_nenufar(l_nenufares)
            if colision_tronco[0] == False and colision_nenufar == False:
                if sonido:
                    sonido_fallo.play()
                player.quitar_vida()
                choco = True
                l_corazones.pop()
            if colision_nenufar != False:
                bicho.posiciones.remove(colision_nenufar+36)
                if len(bicho.posiciones) > 0:   
                    choco = True
                else:
                    termino = True
                posicion_bicho = bicho.posicion(colision_nenufar)
                if posicion_bicho:
                    jugador.sumar_puntos(50)
                    if sonido:
                        sonido_fondo.stop()
                        punto_bicho.play()
                        sonido_fondo.play()
                else:
                    jugador.sumar_puntos(10)
                    if sonido:
                        sonido_fondo.stop()
                        punto_simple.play()
                        sonido_fondo.play()
                punto = fuente_punto.render(f"Score: {jugador.puntos}",True,(0,0,0))
        if choco:
            player.rect.centerx = ANCHO_VENTANA/2
            player.rect.y = ALTO_VENTANA-42
            player.rect_col.centerx = ANCHO_VENTANA/2
            player.rect_col.y = ALTO_VENTANA-42
            choco = False

        
        if termino:
            sonido_fondo.stop()
            jugador.sumar_puntos(300)
            punto = fuente_punto.render(f"Score: {jugador.puntos}",True,(0,0,0))
            nivel_2.nivel_2(jugador,sonido)
            ejecutar = False
        elif player.vidas > 0 and fin_tiempo == False:
            pantalla.blit(imagen_agua,(0,0,800,300))
            pantalla.blit(imagen_pasto,(0,600,800,50))
            calle.pintar_calles(l_calles,pantalla)
            tronco.pintar_troncos(l_troncos_der,pantalla)
            tronco.pintar_troncos(l_troncos_izq,pantalla)
            auto.pintar_autos(l_autos_der,pantalla)
            auto.pintar_autos(l_autos_izq,pantalla)
            nenufar.pintar_nenufares(l_nenufares,pantalla)
            corazon.pintar_corazones(l_corazones,pantalla)
            player.pintar(pantalla)
            bicho.pintar(pantalla)
            reloj.tick(12)
            pantalla.blit(punto,(10,615))
            pantalla.blit(tiempo_jugado,(385,2))
        else:
            if sonido:
                sonido_fondo.stop()
                sonido_game_over.play()
            puntajes.agregar_jugador(jugador)
            pantalla_final.pantalla_final()
            ejecutar = False
            
        pygame.display.flip()
pygame.quit()