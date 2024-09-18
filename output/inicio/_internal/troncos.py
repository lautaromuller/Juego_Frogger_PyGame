import calles
import random

def crear_lista_troncos_der(cantidad)-> list:
    l_troncos_der = []
    for i in range(cantidad):
        if i % 2 == 0:
            pos = 0
        else:
            pos = 2
        x = random.randrange(-7000,0,300)
        l_troncos_der.append(calles.crear(x,(102.5+(pos*50)),200,45,"imagenes/tronco.png"))
    return l_troncos_der

def crear_lista_troncos_izq(cantidad)-> list:
    l_troncos_izq = []
    for i in range(cantidad):
        if i % 2 == 0:
            pos = 1
        else:
            pos = 3
        x = random.randrange(800,7800,300)
        l_troncos_izq.append(calles.crear(x,(102.5+(pos*50)),200,45,"imagenes/tronco.png"))
    return l_troncos_izq


def pintar_troncos(l_troncos:list, pantalla):
    for tronco in l_troncos:
        #pygame.draw.rect(pantalla,(255,0,0),tronco["rect"])
        pantalla.blit(tronco["imagen"],tronco["rect"])

def mover_tronco_der(l_troncos:list):
    for tronco in l_troncos:
        if tronco["rect"].x > 800:
            tronco["rect"].x = -7000
        tronco["rect"].x += 10

def mover_tronco_izq(l_troncos:list,):
    for tronco in l_troncos:
        if tronco["rect"].x < -250:
            tronco["rect"].x = 7800
        tronco["rect"].x -= 10