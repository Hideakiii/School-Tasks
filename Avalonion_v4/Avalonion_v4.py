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
    def __init__(self, color, objekt_x, objekt_y, objekt_h, objekt_w, speed):
        self.objekt_x = 0
        self.objekt_y = 0
        self.objekt_h = 0 
        self.objekt_w = 0
        self.speed = 0
        self.color = color
        pygame.draw.rect(game_Display,
                         self.color,
                         [self.objekt_x,
                          self.objekt_y,
                          self.objekt_h,
                          self.objekt_w])

class Score:                       ########### mit Score und count gab es probleme .....    
    def __init__(self,count):
        self.font = pygame.font.SysFont(None, 25)
        self.text = font.render("Score: "+ str(count), True,black)
        self.game_Display.blit(text, (0,0))

class Lives:
         ### P = Player 1/2 ,lives, l_xy = anzeige Position(x,y)
    def __init__(self,P,P_lives,l_xy):
        self.font = pygame.font.SysFont(None, 25)     #### und mit font gab es probleme .....
        self.text = self.font.render(str(P)+ str(P_lives),True, black )
        game_Display.blit(self.text, (l_xy))

class resurrection:
    def __init__(self,pos_x,pos_y):
        self.dead = 0
        pass
    def Hide(self,pos_x,pos_y):
        self.pos_x = -30000
        self.pos_y = 20000
        self.pygame.display.update()

    def Unhide(self,pos_x,pos_y):
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
    game_Display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    Game_Loop()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
                                  #ac = active color
        pygame.draw.rect(game_Display, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(game_Display,ic,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    game_Display.blit(textSurf, textRect)

def player_P2_true():
    player_P2 = True
def player_P2_false():
    global player_P2
    player_P2 = False
def unpause():
    global pause
    pause = False

def paused():
    while pause:
        global player_P2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        game_Display.blit(TextSurf, TextRect)
        #buttons:
        button("Continue",250,550,150,50,green,bright_green,unpause)
        button("Quit",750,550,150,50,red,bright_red,quitgame)
        button("Player 2 Aktive",375,450,175,50,dark_brown,light_brown,player_P2_true)
        button("Player 2 Deactive",600,450,175,50,dark_brown,light_brown,player_P2_false)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    pygame.init()
    intro = True
    while intro:
        global player_P2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_Display.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Avalonion", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        game_Display.blit(TextSurf, TextRect)
        #buttons:
        button("Start!",250,550,150,50,green,bright_green,Game_Loop)
        button("Quit!",750,550,150,50,red,bright_red,quitgame)
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
        game_Display.blit(TextSurf, TextRect)
        #buttons:
        button("Play Again",250,550,150,50,green,bright_green,Game_Loop)
        button("Quit",750,550,150,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()


### Diese Funktion wir für jedes Update ausgeführt.
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

    #score1 = Score(count)
    #score2 = Score(count)

    P1_lives = Lives("Player 1 Lives: ", 3,(0,20))
    P2_lives = Lives("Player 2 Lives: ", 3,(0,40))

    object1 = Objekts((0,0,0), random.randrange(0,display_width),-700,75,75, 5)
    object2 = Objekts((0,0,0), random.randrange(0,display_width),-700,45,45, 5)
    object3 = Objekts((0,0,0), -1300,(random.randrange(0,display_height)),75,75, 5)
    object4 = Objekts((0,0,0), 1300,(random.randrange(0,display_height)),100,100, 3)

    pygame.init()
    pygame.display.set_caption("Avalonion")

    if player_P2:
        p2.exists = True
    if not player_P2:
        p2.exists = False
    p1.exists = True

    while not gameExit:
        if p1.dead == True:  ## Kürzen : if p1.dead:
            p1_dead_end = time.time()
            p1_dead_diff = p1_dead_end - p1_dead_start
            if not p1_dead_change:
                if p1_dead_diff > 2:
                    re_p1.Unhide()  ## re_p1 = resurrection
                    p1_dead_change = True
            if p1_dead_diff > 5:
                p1_dead = False
                p1_dead_change = False
        if p2.dead == True:  ## Kürzen : if p2.dead:
            p2_dead_end = time.time()
            p2_dead_diff = p2_dead_end - p2_dead_start
            if not p2_dead_change:
                if p2_dead_diff > 2:
                    re_p2.Unhide()  ## re_p2 = resurrection
                    p2_dead_change = True
            if p2_dead_diff > 5:
                p2_dead = False
                p2_dead_change = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #player_1 1 controls:
            
            if p1.exists:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        p1.x_change = -6.5
                    elif event.key == pygame.K_RIGHT:
                        p1.x_change = 6.5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        p1.x_change = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        p1.y_change = -6.5
                    elif event.key == pygame.K_DOWN:
                        p1.y_change = 6.5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        p1.y_change = 0

                    if event.key == pygame.K_p:
                        pause = True
                        paused()
            #Player 2 controls:
            if p2.exists:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                       p2.x_change = -6.5
                    elif event.key == pygame.K_d:
                        p2.x_change = 6.5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        p2.x_change = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        p2.y_change = -6.5
                    elif event.key == pygame.K_s:
                        p2.y_change = 6.5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        p2.y_change = 0

                    if event.key == pygame.K_p:
                        pause = True
                        paused()
                
        # variabeln Player:
        p1.pos_x += p1.x_change
        p1.pos_y += p1.y_change

        p2.pos_x += p2.x_change
        p2.pos_y += p2.y_change

        game_Display.fill(white)

        score1 = 0
        score2 = 0

        P1_lives = 3
        P2_lives = 3

        object1
        object1.objekt_y += object1.speed
        object2
        object2.objekt_x += object2.speed
        object3
        object3.objekt_y += object3.speed
        object4
        object4.objekt_x -= object4.speed

        if p1.exists and not p1.dead:
            if p1.pos_x > display_width - img_width or p1.pos_x < 0:
                p1.dead = True
                p1_dead_start = time.time()
                re_p1.Hide()    ########## Wichtig: P1_Hide wird hier ausgeführt und startet damit die dead loop!
                p1.lives -= 1
                if p1.lives == 0:
                    crash()

            if p1.pos_y > display_height - img_height or p1.pos_y < 0:
                p1.dead = True
                p1_dead_start = time.time()
                re_p1.Hide()
                p1.lives -= 1
                if p1.lives == 0:
                    crash()
        #Player 2:
        if p2.exists and not p2.dead:
            if p2.pos_x > display_width - img_width or p2.pos_x < 0:
                p2.dead = True
                p2_dead_start = time.time()
                re_p2.Hide()
                p2.lives -= 1
                if p2.lives == 0:
                    crash()
            if p2.pos_y > display_height - img_height or p2.pos_y < 0:
                p2.dead = True
                p2_dead_start = time.time()
                re_p2.Hide()
                p2.lives -= 1
                if p2.lives == 0:
                    crash()

        if object1.objekt_y > display_height:
            ### objekt1_y vielleicht ändern auf objekt1_y_start (andere variabel erstellen!!)
            object1.objekt_y = 0 - thing_height
            object1.objekt_x = random.randrange(0, display_width)
            score1 += 1
            score2 += 1

        if object2.objekt_x > display_width:
            object2.objekt_x = 0 - thing_2_width
            object2.objekt_y = random.randrange(0, display_height)
            score1 += 1
            score2 += 1

        if object3.objekt_y > display_height:
            object3.objekt_y = 0 - thing_3_width
            object3.objekt_x = random.randrange(0, display_height)
            score1 += 1
            score2 += 1

        if object4.objekt_x < 0 - thing_4_width:
            object4.objekt_x = display_width + thing_4_width
            object4.objekt_y = random.randrange(0, display_height)
            score1 += 1
            score2 += 1




        ######################################################





        pygame.display.update()
        clock.tick(60)
        object1.speed += 0.001
        object2.speed += 0.002
        object3.speed += 0.001
        object4.speed += 0.001



game_intro()
Game_Loop()
pygame.quit()
quit()
