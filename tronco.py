import pygame
import random

class Tronco:
    def __init__(self,x,y) -> None:
        
        self.animacion = [pygame.image.load("imagenes/tronco.png"),
                          pygame.image.load("imagenes/tronco1.png"),
                          pygame.image.load("imagenes/tronco2.png"),
                          pygame.image.load("imagenes/tronco1.png"),
                          pygame.image.load("imagenes/tronco.png")]
        self.imagen = self.animacion[0]
        # self.imagen = pygame.transform.scale(pygame.image.load("imagenes/tronco.png"),(200,45))
        self.rect = pygame.Rect(x,y,200,45)
        self.pos_y = y
        self.frame = 0
        self.vel_animacion = 8
        self.cont_animacion = 0
    
    def animar(self):
        self.cont_animacion += 1
        if self.cont_animacion > self.vel_animacion:
            self.rect.y += 1.5
            self.frame += 1
            if self.frame >= len(self.animacion):
                self.rect.y = self.pos_y
                self.frame = 0
            elif self.frame > 2:
                self.rect.y -= 3
            self.imagen = self.animacion[self.frame]
            self.cont_animacion = 0

    def pintar(self,pantalla):
        #pygame.draw.rect(pantalla,(255,0,0),self.rect)
        pantalla.blit(self.imagen,self.rect)

    def mover_der(self,velocidad):
        if self.rect.x > 800:
            self.rect.x = -7000
        self.rect.x += velocidad

    def mover_izq(self,velocidad):
        if self.rect.x < -250:
            self.rect.x = 7800
        self.rect.x -= velocidad


def crear_lista_troncos_der(cantidad):
    l_troncos_der = []
    for i in range(cantidad):
        if i % 2 == 0:
            pos = 0
        else:
            pos = 2
        x = random.randrange(-7000,0,300)
        l_troncos_der.append(Tronco(x,102.5+(pos*50)))
    return l_troncos_der

def crear_lista_troncos_izq(cantidad):
    l_troncos_izq = []
    for i in range(cantidad):
        if i % 2 == 0:
            pos = 1
        else:
            pos = 3
        x = random.randrange(800,7800,300)
        l_troncos_izq.append(Tronco(x,102.5+(pos*50)))
    return l_troncos_izq

def pintar_troncos(l_troncos:list, pantalla):
    for tronco in l_troncos:
        tronco.animar()
        tronco.pintar(pantalla)

def mover_tronco_der(l_troncos:list, velocidad:int):
    for tronco in l_troncos:
        tronco.mover_der(velocidad)

def mover_tronco_izq(l_troncos:list, velocidad:int):
    for tronco in l_troncos:
        tronco.mover_izq(velocidad)