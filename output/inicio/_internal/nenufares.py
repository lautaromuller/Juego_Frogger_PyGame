import pygame

def crear(x:int, y:int, ancho:int, alto:int, path:str)-> dict:
    dict_calle = {}
    dict_calle["imagen"]  = pygame.image.load(path)
    dict_calle["imagen"] = pygame.transform.scale(dict_calle["imagen"] ,(ancho,alto))
    dict_calle["rect"] = dict_calle["imagen"] .get_rect()
    dict_calle["rect"].x = x
    dict_calle["rect"].y = y
    dict_calle["rect_col"] = pygame.Rect(x+ancho/10,y+20,104,60)
    dict_calle["visible"] = True
    return dict_calle

def crear_lista_nenufares(cantidad):
    l_nenufares = []
    for i in range(cantidad):
        l_nenufares.append(crear((15+(i*160)),5,130,100,"imagenes/nenufar.png"))
    return l_nenufares

def pintar_nenufar(l_nenufares:list, pantalla):
    for nenufar in l_nenufares:
        if nenufar["visible"]:
            pantalla.blit(nenufar["imagen"],nenufar["rect"])
            #pygame.draw.rect(pantalla,(255,0,0),nenufar["rect_col"])