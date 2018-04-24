import pygame
import random
import time
#variabeln:

display_width = 800
display_hight = 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (0,255,0)
blue = (0,0,255)
# Ich würde hier nur einen lokalen Pfad nehmen. Also einfach die Bilddatei in das selbe Verzeichnis wie die Python-Datei
carImg = pygame.image.load('snake.png')
x = (display_width * 0.45)
y = (display_hight * 0.8)
crashed = False

#definitionen:

def car (x,y):
    # Ich habe die Koordinaten mal auf 0,0 gesetzt, weil das Bild sonst halb aus dem Bildschirm ragt...
    gameDisplay.blit(carImg, (0,0))

#Initialisierung:

pygame.init()
pygame.display.set_caption("RaceGame")
gameDisplay = pygame.display.set_mode((display_width,display_hight))

# Punkt Komma Groß
clock = pygame.time.Clock()



while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
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
