import pygame
import random

lista_autos_der = ["imagenes/c_amarillo_der.png","imagenes/c_azul_der.png","imagenes/c_negro_der.png","imagenes/c_rojo_der.png","imagenes/c_rosa_der.png"]
lista_autos_izq = ["imagenes/c_amarillo_izq.png","imagenes/c_azul_izq.png","imagenes/c_negro_izq.png","imagenes/c_rojo_izq.png","imagenes/c_rosa_izq.png"]

def crear(x:int, y:int, ancho:int, alto:int, path:str)-> dict:
    dict_auto = {}
    dict_auto["imagen"] = pygame.image.load(path)
    dict_auto["imagen"] = pygame.transform.scale(dict_auto["imagen"],(ancho,alto))
    dict_auto["rect"] = dict_auto["imagen"].get_rect()
    dict_auto["rect"].x = x
    dict_auto["rect"].y = y
    dict_auto["tocado"] = True
    return dict_auto

def crear_lista_autos_der(cantidad,margen):
    l_autos_der = []
    for i in range(int(cantidad)):
        for i in range(3):
            x = random.randrange(-margen,0,250)
            auto = random.randint(0,4)
            l_autos_der.append(crear(x,(305+(i*120)),100,50,lista_autos_der[auto]))
    return l_autos_der

def crear_lista_autos_izq(cantidad,margen):
    l_autos_izq = []
    for i in range(int(cantidad)):
        for i in range(2):
            x = random.randrange(800,margen,250)
            auto = random.randint(0,4)
            l_autos_izq.append(crear(x,(365+(i*120)),100,50,lista_autos_izq[auto]))
    return l_autos_izq

def pintar_autos(l_autos:list,pantalla):
    for auto in l_autos:
        #pygame.draw.rect(pantalla,(255,0,0),auto["rect"])
        pantalla.blit(auto["imagen"],auto["rect"])

def mover_auto_der(l_autos:list,pos_siguiente):
    for auto in l_autos:
        if auto["rect"].x > 800:
            auto["rect"].x = -pos_siguiente
        else:
            auto["rect"].x += 10

def mover_auto_izq(l_autos:list,pos_siguiente):
    for auto in l_autos:
        if auto["rect"].x < -150:
            auto["rect"].x = pos_siguiente
        else:
            auto["rect"].x -= 10