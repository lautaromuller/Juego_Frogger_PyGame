import pygame

class Calle:
    def __init__(self,x,y) -> None:
        self.imagen = pygame.transform.scale(pygame.image.load("imagenes/calle.png"),(800,60))
        self.rect = pygame.Rect(x,y,800,60)


    def pintar(self, pantalla):
        #pygame.draw.rect(pantalla,(255,0,0),self.rect)
        pantalla.blit(self.imagen,self.rect)

def crear_lista_calles(cantidad):
    l_calles = []
    for i in range(cantidad):
        l_calles.append(Calle(0,300+(i*60)))
    return l_calles

def pintar_calles(l_calles:list, pantalla):
        for calle in l_calles:
            calle.pintar(pantalla)