import pygame

def crear(x:int, y:int, ancho:int, alto:int, path:str)-> dict:
    dict_corazon = {}
    dict_corazon["imagen"]  = pygame.image.load(path)
    dict_corazon["imagen"] = pygame.transform.scale(dict_corazon["imagen"] ,(ancho,alto))
    dict_corazon["rect"] = dict_corazon["imagen"] .get_rect()
    dict_corazon["rect"].x = x
    dict_corazon["rect"].y = y
    return dict_corazon

def crear_lista_corazones(cantidad):
    l_corazones = []
    for i in range(cantidad):
        l_corazones.append(crear((755-(i*45)),605,40,40,"imagenes/corazon.png"))
    return l_corazones

def pintar_corazon(l_corazones:list, pantalla):
    for corazon in l_corazones:
        #pygame.draw.rect(pantalla,(255,0,0),corazon["rect"])
        pantalla.blit(corazon["imagen"],corazon["rect"])