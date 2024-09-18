import pygame
from constantes import *


def crear(x:int, y:int, ancho:int, alto:int, path:str)-> dict:
    dict_personaje = {}
    dict_personaje["imagen"] = pygame.image.load(path)
    dict_personaje["imagen"] = pygame.transform.scale(dict_personaje["imagen"],(ancho,alto))
    # dict_personaje["rect"] = pygame.Rect(x-(ancho/4),y,(ancho/4)*2,alto)
    dict_personaje["rect"] = dict_personaje["imagen"].get_rect()
    dict_personaje["rect"].centerx = x
    dict_personaje["rect"].y = y
    dict_personaje["ancho_img"] = ancho
    dict_personaje["rect_col"] = pygame.Rect(x-(ancho/4),y,(ancho/4)*2,alto)
    dict_personaje["vidas"] = 3
    return dict_personaje

def pintar_personaje(personaje,pantalla):
    pantalla.blit(personaje["imagen"],personaje["rect"])
    #pygame.draw.rect(pantalla,(255,0,255),personaje["rect_col"])

def mover_personaje_x(personaje,movimiento):
    personaje["rect"].x += movimiento
    personaje["rect_col"].x += movimiento
    if personaje["rect"].x <= 0:
        personaje["rect"].x = 0
        personaje["rect_col"].x = personaje["ancho_img"]/4
    elif personaje["rect"].x + 40 >= ANCHO_VENTANA:
        personaje["rect"].x = 760
        personaje["rect_col"].x = personaje["rect"].x + personaje["ancho_img"]/4

def mover_personaje_y(personaje,movimiento):
    personaje["rect"].y += movimiento
    personaje["rect_col"].y += movimiento
    if movimiento < 0:
        if 240 < personaje["rect"].y < 300:
            personaje["rect"].y = 252.5
            personaje["rect_col"].y = 252.5
    else:
        if 350 > personaje["rect"].y > 300:
            personaje["rect"].y = 307.5
            personaje["rect_col"].y = 307.5
        if personaje["rect"].y + 45 > ALTO_VENTANA:
            personaje["rect"].y = ALTO_VENTANA-42
            personaje["rect_col"].y = ALTO_VENTANA-42

def colision_auto(personaje,autos_d,autos_i):
    colisiono = False
    for auto in autos_d: 
        if personaje["rect_col"].colliderect(auto["rect"]) and auto["tocado"]:
            colisiono = True
            auto["tocado"] = False
    for auto in autos_i: 
        if personaje["rect_col"].colliderect(auto["rect"]) and auto["tocado"]:
            colisiono = True
            auto["tocado"] = False
    return colisiono

def colision_tronco(personaje,troncos_d,troncos_i):
    colisiono = False
    direccion = False
    for tronco in troncos_d: 
        if personaje["rect"].colliderect(tronco["rect"]):
            direccion = "derecha"
            colisiono = True
    for tronco in troncos_i: 
        if personaje["rect"].colliderect(tronco["rect"]):
            direccion = "izquierda"
            colisiono = True
    return [colisiono,direccion]

def colision_nenufar(personaje,nenufares):
    retorno = False
    for nenufar in nenufares: 
        if personaje["rect"].colliderect(nenufar["rect_col"]) and nenufar["visible"]:
            retorno = nenufar["rect_col"].x
            nenufar["visible"] = False
            # colisiono = True
    return retorno

def mover_personaje_der(personaje):
    if personaje["rect"].x + 40 < 800:
        personaje["rect"].x += 10
        personaje["rect_col"].x += 10

def mover_personaje_izq(personaje):
    if personaje["rect"].x > 0:
        personaje["rect"].x -= 10
        personaje["rect_col"].x -= 10