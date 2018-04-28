import pygame
import random
import time
import os

#Variabeln:
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
carImg = pygame.image.load('Pixelart.png')
img_width = 75
img_height = 75
black = (0,0,0)
#definitionen:

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display("You Crashed!")

def car (x,y):
    #hiermit sollte das Bild nun immer am unteren Bildschirmrand sein 
    gameDisplay.blit(pygame.transform.scale(carImg, (75, 75)), (x, y))

def things(thing_x, thing_y, thing_h, thing_w, color):
    pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_w, thing_h])


def game_loop():
    #variabeln_2:
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    yellow = (0,255,0)
    blue = (0,0,255)
    # Ich würde hier nur einen lokalen Pfad nehmen. Also einfach die Bilddatei in das selbe Verzeichnis wie die Python-Datei
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    gameExit = False

    thing_start_x = random.randrange(0, display_width)
    thing_start_y = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100



    #Initialisierung:
    pygame.init()
    pygame.display.set_caption("FirstGame")

    # Punkt Komma Groß
    clock = pygame.time.Clock()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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
        #things(thin_x, thing_y, thing_h, thing_w, color)
        things(thing_start_x, thing_start_y, thing_height, thing_width, black)
        thing_start_y += thing_speed


        if x > display_width - img_width or x < 0:
            crash()
        if y > display_height - img_height or y < 0:
            crash()

        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)

        if y < thing_start_y + thing_height:
            print("y crossover")
            if x > thing_start_x and x < thing_start_x + thing_width or x + img_width > thing_start_x and x + img_width < thing_start_x + thing_width:
                print("x crossover")
                crash()



        pygame.display.update()
        clock.tick(60)

# Das soll nur einmal am Ende ausgeführt werden, also ist es wieder ganz ausgerückt.
game_loop()
pygame.quit()
quit()
