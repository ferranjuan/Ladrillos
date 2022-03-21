#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Escrito por Daniel Fuentes B.
# ---------------------------
# Importacion de los módulos
# ---------------------------
import pygame
from pygame.locals import *
import sys
# -----------
# Constantes
# -----------
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
# ------------------------------
# Funcion principal del juego
# ------------------------------
def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 2")
    while True:
    # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()