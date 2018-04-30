import pygame
import random
import time
import os

pygame.init()
#Variabeln:
display_width = 1200
display_height = 700
gameDisplay = pygame.display.set_mode((display_width,display_height))
P1_Img = pygame.image.load('Pixelart.png')
img_width = 75
img_height = 75
pygame.display.set_icon(P1_Img)
Score = 1
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
yellow = (0,255,0)
blue = (0,0,255)
# Punkt Komma Groß
clock = pygame.time.Clock()
pause = False
#crash = True

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

def Score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+ str(count), True ,black)
    gameDisplay.blit(text, (0,0))
    
def crash():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("You Crashed!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        #buttons:
        button("Play Again",250,550,150,50,green,bright_green,game_loop)
        button("Quit",750,550,150,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def car (x,y):
    #hiermit sollte das Bild nun immer am unteren Bildschirmrand sein 
    gameDisplay.blit(pygame.transform.scale(P1_Img, (75, 75)), (x, y))

def things(thing_x, thing_y, thing_h, thing_w, color):
    pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_w, thing_h])

def things_2(thing_2_x, thing_2_y, thing_2_h, thing_2_w, color):
    pygame.draw.rect(gameDisplay, color, [thing_2_x, thing_2_y, thing_2_h, thing_2_w])

def quitgame():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #button 1:
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
                                  #ac = active color
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    # button 1 text:
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False

def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        #buttons:
        button("Continue",250,550,150,50,green,bright_green,unpause)
        button("Quit",750,550,150,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    pygame.init()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Avalonion", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        #buttons:
        button("Start!",250,550,150,50,green,bright_green,game_loop)
        button("Quit!",750,550,150,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
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
    score = 0
    #thing 1 :

    thing_start_x = random.randrange(0, display_width)
    thing_start_y = -700
    thing_speed = 5
    thing_width = 75
    thing_height = 75

    #thing 2:

    thing_2_start_x = -1200
    thing_2_start_y = random.randrange(0, display_height)
    thing_2_speed = 5
    thing_2_width = 75
    thing_2_height = 75

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
                    x_change = -6
                elif event.key == pygame.K_RIGHT:
                    x_change = 6

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -6
                elif event.key == pygame.K_DOWN:
                    y_change = 6

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

                if event.key == pygame.K_p:
                    pause = True
                    paused()

                
        # variabeln 2 :
        x += x_change
        y += y_change
            # Die folgenden Zeilen sollen alle durch den while-loop wiederholt werden...
            # Sie müssen also die selbe Einrückung haben wie das for.
            # Allerdings nicht wie das if, da sie sonst für jedes event wiederholt würden.
        gameDisplay.fill(white)
        car(x,y)
        Score(score)

        #things(thin_x, thing_y, thing_h, thing_w, color)
        things(thing_start_x, thing_start_y, thing_height, thing_width, black)
        thing_start_y += thing_speed
        things_2(thing_2_start_x, thing_2_start_y, thing_2_height, thing_2_width, black)
        thing_2_start_x += thing_2_speed

        if x > display_width - img_width or x < 0:
            crash()
        if y > display_height - img_height or y < 0:
            crash()

        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)
            score += 1
        if thing_2_start_x > display_width:
            thing_2_start_x = 0 - thing_2_width
            thing_2_start_y = random.randrange(0, display_height)
            score += 1

        if y <= thing_start_y + thing_height and y >= thing_start_y - thing_height:
            if x > thing_start_x and x < thing_start_x + thing_width or x + img_width > thing_start_x and x + img_width < thing_start_x + thing_width:
                crash()
        if x <= thing_2_start_x + thing_2_height and x >= thing_2_start_x - thing_2_height:
            if y > thing_2_start_y and y < thing_2_start_y + thing_2_width or y + img_width > thing_2_start_y and y + img_width < thing_2_start_y + thing_2_width:
                crash()

        pygame.display.update()
        clock.tick(60)
        thing_speed += 0.001
        thing_2_speed += 0.001
        #score()
# Das soll nur einmal am Ende ausgeführt werden, also ist es wieder ganz ausgerückt.

game_intro()
game_loop()
pygame.quit()
quit()
