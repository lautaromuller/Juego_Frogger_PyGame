import pygame


class Corazon:
    def __init__(self,x,y) -> None:
        self.imagen = pygame.transform.scale(pygame.image.load("imagenes/corazon.png"),(40,40))
        self.rect = pygame.Rect(x,y,40,40)

    def pintar(self,pantalla):
        #pygame.draw.rect(pantalla,(255,0,0),self.rect)
        pantalla.blit(self.imagen,self.rect)

def crear_lista_corazones(cantidad):
    l_corazones = []
    for i in range(cantidad):
        l_corazones.append(Corazon(755-(i*45),605))
    return l_corazones

def pintar_corazones(l_corazones:list, pantalla):
    for corazon in l_corazones:
        corazon.pintar(pantalla)