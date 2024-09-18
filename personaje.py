import pygame
from constantes import *

l_img_caminar = ["0.png","1.png","2.png","3.png","4.png","5.png","6.png"]

class Personaje:
    def __init__(self,x,y) -> None:
        self.img_caminar = [pygame.image.load("imagenes/0.png"),
                            pygame.image.load("imagenes/1.png"),
                            pygame.image.load("imagenes/2.png"),
                            pygame.image.load("imagenes/3.png"),
                            pygame.image.load("imagenes/4.png"),
                            pygame.image.load("imagenes/5.png"),
                            pygame.image.load("imagenes/6.png")]
        self.img_saltar = [pygame.image.load("imagenes/arriba0.png"),
                           pygame.image.load("imagenes/arriba1.png")]
        self.imagen = self.img_saltar[0]
        self.rect = self.imagen.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.ancho = 40
        self.alto = 45
        self.rect_col = pygame.Rect(x-(40/4),y,(40/2),45)
        self.vidas = 3
        self.frame = 0

    def caminar(self,direccion):
        self.frame += 1
        if self.frame >= len(self.img_caminar):
            self.frame = 0
        if direccion == "izquierda":
            self.imagen = self.img_caminar[self.frame]
        elif direccion == "derecha":
            self.imagen = pygame.transform.flip(self.img_caminar[self.frame],True,False)
    
    def saltar(self,direccion):
        if direccion == "izquierda":
            self.imagen = self.img_saltar[1]
        elif direccion == "derecha":
            self.imagen = pygame.transform.flip(self.img_saltar[1],True,False)
    
    def quieto(self,direccion):
        if direccion == "izquierda":
            self.imagen = self.img_saltar[0]
        elif direccion == "derecha":
            self.imagen = pygame.transform.flip(self.img_saltar[0],True,False)
        self.frame = 0
    
    def pintar(self,pantalla):
        #pygame.draw.rect(pantalla,(255,0,0),self.rect)
        pantalla.blit(self.imagen,self.rect)
        # pygame.draw.rect(pantalla,(255,255,0),self.rect_col)

    def mover_x(self,movimiento):
        if self.rect.x + movimiento <= 0:
            self.rect.x = 0
            self.rect_col.x = 10
        elif self.rect.x + movimiento + 40 >= ANCHO_VENTANA:
            self.rect.x = 760
            self.rect_col.x = 770
        else:
            for i in range(7):
                l_img_caminar[i]
            self.rect.x += movimiento
            self.rect_col.x += movimiento

    def mover_y(self,movimiento):
        self.rect.y += movimiento
        self.rect_col.y += movimiento
        if movimiento < 0:
            if 240 < self.rect.y < 300:
                self.rect.y = 252.5
                self.rect_col.y = 252.5
        else:
            if 350 > self.rect.y > 300:
                self.rect.y = 307.5
                self.rect_col.y = 307.5
            if self.rect.y + 45 > ALTO_VENTANA:
                self.rect.y = ALTO_VENTANA-42
                self.rect_col.y = ALTO_VENTANA-42
    
    def quitar_vida(self):
        self.vidas -= 1

    def colision_auto(self,autos_d,autos_i):
        colisiono = False
        for auto in autos_d: 
            if self.rect_col.colliderect(auto.rect) and auto.tocado:
                colisiono = True
                auto.tocado = False
                break
        for auto in autos_i: 
            if self.rect_col.colliderect(auto.rect) and auto.tocado:
                colisiono = True
                auto.tocado = False
                break
        return colisiono

    def colision_tronco(self,troncos_d,troncos_i):
        colisiono = False
        direccion = False
        for tronco in troncos_d: 
            if self.rect.colliderect(tronco.rect):
                direccion = "derecha"
                colisiono = True
                break
        for tronco in troncos_i: 
            if self.rect.colliderect(tronco.rect):
                direccion = "izquierda"
                colisiono = True
                break
        return [colisiono,direccion]


    def colision_nenufar(self,nenufares):
        retorno = False
        for nenufar in nenufares: 
            if self.rect.colliderect(nenufar.rect_col) and nenufar.visible:
                retorno = nenufar.rect_col.x
                nenufar.visible = False
        return retorno

    def mover_con_tronco(self,direccion,velocidad):
        if self.rect.x + 40 < 800 and direccion == "derecha":
            self.rect.x += velocidad
            self.rect_col.x += velocidad
        elif self.rect.x > 0 and direccion == "izquierda":
            self.rect.x -= velocidad
            self.rect_col.x -= velocidad