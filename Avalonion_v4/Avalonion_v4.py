import pygame
import random
import time
import os

pygame.init()
# Variabeln:
display_width = 1200
display_height = 700
game_Display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_icon(pygame.image.load('Pixelart_P1.png'))
clock = pygame.time.Clock()
pause = False
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
grey = (65,65,65)
light_grey = (80,80,80)
dark_brown = (90,75,80)
light_brown = (110,95,100)
# Klassen:
class Player:
    def __init__(self, Img, dead, exists, died_at_time, lives, score, pos_x, pos_y):
        self.Img = 0
        self.dead = False
        self.exists = True
        self.died_at_time = None
        self.lives = 3
        self.score = 0
        self.pos_x
        self.pos_y

class Objekts:
    def __init__(self,objekt_x, objekt_y, objekt_h, objekt_w):
        self.objekt_x
        self.objekt_y
        self.objekt_h
        self.objekt_w
        pygame.draw.rect(gameDisplay,color,[objekt_x,objekt_y,objekt_h,objekt_w])

p1 = Player(pygame.image.load('Pixelart_P1.png'),False,True,None,3,0,display_height * 0.8,display_width * 0.4)
p2 = Player(pygame.image.load('Pixelart_P2.png'),False,False,None,3,0,display_height * 0.8,display_width * 0.5)

object1 = Objekts(random.randint(0,1200),0)


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

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
                                  #ac = active color
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)




