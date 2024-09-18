import pygame

def crear(x:int, y:int, ancho:int, alto:int, path:str)-> dict:
    dict_calle = {}
    dict_calle["imagen"] = pygame.image.load(path)
    dict_calle["imagen"] = pygame.transform.scale(dict_calle["imagen"],(ancho,alto))
    dict_calle["rect"] = dict_calle["imagen"].get_rect()
    dict_calle["rect"].x = x
    dict_calle["rect"].y = y
    return dict_calle

def pintar_calles(l_calles:list, pantalla):
    for calle in l_calles:
        #pygame.draw.rect(pantalla,(255,0,0),calle["rect"])
        pantalla.blit(calle["imagen"],calle["rect"])

def crear_lista_calles(cantidad):
    l_calles = []
    for i in range(cantidad):
        l_calles.append(crear(0,(300+(i*60)),800,60,"imagenes/calle.png"))
    return l_calles