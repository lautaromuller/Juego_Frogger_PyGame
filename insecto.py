import pygame
import random

class Insecto:
    def __init__(self,x,y) -> None:
        self.animacion = [pygame.image.load("imagenes/mosca0.png"),
                          pygame.image.load("imagenes/mosca1.png"),
                          pygame.image.load("imagenes/mosca2.png")]
        # self.imagen = pygame.transform.scale(pygame.image.load("imagenes/insecto.png"),(34,46))
        self.imagen = self.animacion[0]
        self.rect = pygame.Rect(x,y,34,46)
        self.visible = True
        self.posiciones = [64,224,384,544,704]
        self.frame = 0
        self.vel_animacion = 2
        self.cont_animacion = 0
    
    def animar(self):
        self.cont_animacion += 1
        if self.cont_animacion > self.vel_animacion:
            self.frame += 1
            if self.frame >= len(self.animacion):
                self.frame = 0
            self.imagen = self.animacion[self.frame]
            self.cont_animacion = 0


    def pintar(self, pantalla):
        self.animar()
        #pygame.draw.rect(pantalla,(0,0,255),self.rect)
        pantalla.blit(self.imagen,self.rect)

    def mover(self):
        if len(self.posiciones) > 0:
            num = random.choice(self.posiciones)
            self.rect.x = num

    def posicion(self,x):
        retorno = False
        if x+104 > self.rect.x > x:
            self.mover()
            retorno = True
        return retorno
