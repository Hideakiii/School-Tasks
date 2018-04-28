import pygame
import random
import time
import os
#variabeln:

display_width = 800
display_hight = 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (0,255,0)
blue = (0,0,255)
# Ich würde hier nur einen lokalen Pfad nehmen. Also einfach die Bilddatei in das selbe Verzeichnis wie die Python-Datei
carImg = pygame.image.load('Pixelart.png')
x = (display_width * 0.45)
y = (display_hight * 0.8)
crashed = False
x_change = 0
y_change = 0
gameDisplay = pygame.display.set_mode((display_width,display_hight))

#definitionen:

def car (x,y):
    #hiermit sollte das Bild nun immer am unteren Bildschirmrand sein 
    gameDisplay.blit(pygame.transform.scale(carImg, (75, 75)), (x, y))

#Initialisierung:

pygame.init()
pygame.display.set_caption("FirstGame")

# Punkt Komma Groß
clock = pygame.time.Clock()



while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0



        # variabeln 2 :
    x += x_change
    y += y_change
        # Die folgenden Zeilen sollen alle durch den while-loop wiederholt werden...
        # Sie müssen also die selbe Einrückung haben wie das for.
        # Allerdings nicht wie das if, da sie sonst für jedes event wiederholt würden.
    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)

# Das soll nur einmal am Ende ausgeführt werden, also ist es wieder ganz ausgerückt.
pygame.quit()
quit()
