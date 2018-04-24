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
carImg = pygame.image.load('C:\Users\daeda\source\repos\First game\Bild\Pixelart.png')
x = (display_width * 0.45)
y = (display_hight * 0.8)
crashed = False

#definitionen:

def car (x,y):
    gameDisplay.blit(carImg, (x,y))





#Initialisierung:

pygame.init()
pygame.display.set_caption("RaceGame")
gameDisplay = pygame.display.set_mode((display_width,display_hight))
clock = pygame,time.clock()



while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

gameDisplay.fill(white)
car(x,y)

pygame.display.update()
clock.tick(60)
pygame.quit()
quit()