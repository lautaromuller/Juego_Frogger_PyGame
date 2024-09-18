import pygame
import random


def crear(x:int, y:int, ancho:int, alto:int, path:str)-> dict:
    dict_insecto = {}
    dict_insecto["imagen"]  = pygame.image.load(path)
    dict_insecto["imagen"] = pygame.transform.scale(dict_insecto["imagen"] ,(ancho,alto))
    dict_insecto["rect"] = dict_insecto["imagen"].get_rect()
    dict_insecto["rect"].x = x
    dict_insecto["rect"].y = y
    dict_insecto["visible"] = True
    dict_insecto["posiciones"] = [64,224,384,544,704]
    return dict_insecto

def pintar_insecto(insecto, pantalla):
    #pygame.draw.rect(pantalla,(0,0,255),insecto["rect"])
    pantalla.blit(insecto["imagen"],insecto["rect"])

def mover(insecto):
    if len(insecto["posiciones"]) > 0:
        num = random.choice(insecto["posiciones"])
        insecto["rect"].x = num

def posicion_insecto(insecto,x):
    retorno = False
    if x+104 > insecto["rect"].x > x:
        mover(insecto)
        retorno = True
    return retorno
