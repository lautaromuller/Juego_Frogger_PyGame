import pygame
import random

lista_autos_der = ["imagenes/c_amarillo_der.png","imagenes/c_azul_der.png","imagenes/c_negro_der.png","imagenes/c_rojo_der.png","imagenes/c_rosa_der.png"]
lista_autos_izq = ["imagenes/c_amarillo_izq.png","imagenes/c_azul_izq.png","imagenes/c_negro_izq.png","imagenes/c_rojo_izq.png","imagenes/c_rosa_izq.png"]

class Auto:
    def __init__(self,x,y,imagen) -> None:
        self.imagen = pygame.transform.scale(pygame.image.load(imagen),(100,50))
        self.rect = pygame.Rect(x,y,100,50)
        self.ancho = 100
        self.alto = 50
        self.tocado = True
    
    def pintar(self,pantalla):
        #pygame.draw.rect(pantalla,(255,0,0),self.rect)
        pantalla.blit(self.imagen,self.rect)

    def mover_der(self,pos_siguiente,velocidad):
        if self.rect.x > 800:
            self.rect.x = -pos_siguiente
        else:
            self.rect.x += velocidad 
    
    def mover_izq(self,pos_siguiente,velocidad):
        if self.rect.x < -150:
            self.rect.x = pos_siguiente
        else:
            self.rect.x -= velocidad

def crear_lista_autos_der(cantidad,margen):
    l_autos_der = []
    for i in range(int(cantidad)):
        for i in range(3):
            x = random.randrange(-margen,0,350)
            auto = random.randint(0,4)
            l_autos_der.append(Auto(x,305+(i*120),lista_autos_der[auto]))
    return l_autos_der

def crear_lista_autos_izq(cantidad,margen):
    l_autos_izq = []
    for i in range(int(cantidad)):
        for i in range(2):
            x = random.randrange(800,margen,250)
            auto = random.randint(0,4)
            l_autos_izq.append(Auto(x,365+(i*120),lista_autos_izq[auto]))
    return l_autos_izq

def pintar_autos(l_autos,pantalla):
    for auto in l_autos:
        auto.pintar(pantalla)

def mover_auto_der(l_autos,pos_siguiente,velocidad):
    for auto in l_autos:
        auto.mover_der(pos_siguiente,velocidad)

def mover_auto_izq(l_autos,pos_siguiente,velocidad):
    for auto in l_autos:
        auto.mover_izq(pos_siguiente,velocidad)