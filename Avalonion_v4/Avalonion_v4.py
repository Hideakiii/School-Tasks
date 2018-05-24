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
player_P2 = False
pause = False
p1_dead_start = 0
p1_dead_start = 0
p1_dead_change = False
p2_dead_change = False


def player_P2_true():
    global player_P2
    player_P2 = True
def player_P2_false():
    global player_P2
    player_P2_false
def unpause():
    global pause
    pause = False

# Klassen:
class Player:
    def __init__(self, Img, dead, exists, died_at_time, lives, score, pos_x, pos_y, x_change, y_change):
        self.Img = 0
        self.dead = False
        self.exists = True
        self.died_at_time = None
        self.lives = 3
        self.score = 0
        self.pos_x = 0
        self.pos_y = 0
        self.x_change = 0
        self.y_change = 0

class Objekts:
    def __init__(self,objekt_x, objekt_y, objekt_h, objekt_w, speed):
        self.objekt_x = 0
        self.objekt_y = 0
        self.objekt_h = 0 
        self.objekt_w = 0
        self.speed = 0
        self.pygame.draw.rect(gameDisplay,color,[objekt_x,objekt_y,objekt_h,objekt_w])

class Score:
    def __init__(self,count):
        self.font = pygame.font.SysFont(None, 25)
        self.text = font.render("Score: "+ str(count), True,black)
        self.game_Display.blit(text, (0,0))

class Lives:
         ### P = Player 1/2 ,lives, l_xy = anzeige Position(x,y)
    def __init__(self,P,P_lives,l_xy):
        self.font = pygame.font.SysFont(None, 25)
        self.text = font.render(str(P)+ str(P_lives),True, black )
        self.game_Display.blit(text, (l_xy))

class resurrection:
    def __init__(self,pos_x,pos_y):
        self.dead = 0
        self.pos_x
        self.pos_y
    def Hide(self):
            self.pos_x = -30000
            self.pos_y = 20000
            self.pygame.display.update()

    def Unhide(self):
            self.pos_x = display_width * 0.45
            self.pos_y = display_height * 0.8
            self.pygame.display,update()

def quitgame():
    pygame.quit()
    quit()

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

def paused():
    while pause:
        global player_P2
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
        button("Player 2 Aktive",375,450,175,50,dark_brown,light_brown,player_P2_true)
        button("Player 2 Deactive",600,450,175,50,dark_brown,light_brown,player_P2_false)

        pygame.display.update()
        clock.tick(15)

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

def quitgame():
    pygame.quit()
    quit()

def Game_Loop():
    global pause
    gameExit = False
    global p1_dead_change
    global p2_dead_change
    global p1_dead_start
    global p2_dead_start

    clock = pygame.time.Clock()

    p1 = Player(pygame.image.load('Pixelart_P1.png'),False,True,None,3,0,display_width * 0.4,display_height * 0.8 ,0,0)
    p2 = Player(pygame.image.load('Pixelart_P2.png'),False,False,None,3,0,display_width * 0.5,display_height * 0.8 ,0,0)

    re_p1 = resurrection(0, 0)
    re_p2 = resurrection(0, 0)

    score1 = Score(count)
    score2 = Score(count)

    P1_lives = Lives("Player 1 Lives: ", 3,(0,20))
    P2_lives = Lives("Player 2 Lives: ", 3,(0,40))

    object1 = Objekts(random.randrange(0,display_width),-700,75,75, 5)
    object2 = Objekts(random.randrange(0,display_width),-700,45,45, 5)
    object3 = Objekts(-1300,(random.randrange(0,display_height)),75,75, 5)
    object4 = Objekts(1300,(random.randrange(0,display_height)),100,100, 3)

    pygame.init()
    pygame.display.set_caption("Avalonion")

    if player_P2:
        p2.exists = True
    if not player_P2:
        p2.exists = False

    while not gameExit:
        if p1.dead == True:
            p1_dead_end = time.time()
            p1_dead_diff = p1_dead_end - p1_dead_start
            if not p1_dead_change:
                if p1_dead_diff > 2:
                    re_p1.Unhide()  ## re_p1 = resurrection
                    p1_dead_change = True
            if p1_dead_diff > 5:
                p1_dead = False
                p1_dead_change = False
        if p2.dead == True:
            p2_dead_end = time.time()
            p2_dead_diff = p2_dead_end - p2_dead_start
            if not p2_dead_change:
                if p2_dead_diff > 2:
                    re_p2.Unhide()  ## re_p2 = resurrection
                    p2_dead_change = True
            if p2_dead_diff > 5:
                p2_dead = False
                p2_dead_change = False

