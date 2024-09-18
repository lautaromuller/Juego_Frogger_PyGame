import pygame


class Nenufar:
    def __init__(self,x,y) -> None:
        self.imagen = pygame.transform.scale(pygame.image.load("imagenes/nenufar.png"),(130,100))
        self.rect = pygame.Rect(x,y,130,100)
        self.rect_col = pygame.Rect(x+(130/10),y+20,104,60)
        self.visible = True
    
    def pintar(self, pantalla):
        if self.visible:
            pantalla.blit(self.imagen,self.rect)
            #pygame.draw.rect(pantalla,(255,0,0),self.rect_col)

def crear_lista_nenufares(cantidad):
    l_nenufares = []
    for i in range(cantidad):
        l_nenufares.append(Nenufar(15+(i*160),5))
    return l_nenufares

def pintar_nenufares(l_nenufares,pantalla):
    for nenufar in l_nenufares:
        nenufar.pintar(pantalla)