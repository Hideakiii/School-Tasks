import pygame
import random
import time
import os

pygame.init()
#Variabeln:
display_width = 1200
display_height = 700
gameDisplay = pygame.display.set_mode((display_width,display_height))
P1_Img = pygame.image.load('Pixelart_P1.png')
P2_Img = pygame.image.load('Pixelart_P2.png')
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
grey = (65,65,65)
light_grey = (80,80,80)
dark_brown = (90,75,80)
light_brown = (110,95,100)
# Punkt Komma Groß
clock = pygame.time.Clock()
p1_dead_start = 0
p1_dead_start = 0
pause = False
player_P1 = True
player_P2 = False
p1_dead = False
p2_dead = False

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
    
def Lives(p1_lives, p2_lives):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Player 1 Lives: "+ str(p1_lives), True ,black)
    gameDisplay.blit(text, (0,20))
    text = font.render("Player 2 Lives: "+ str(p2_lives), True ,black)
    gameDisplay.blit(text, (0,40))
    
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

def player_1(P1_x,P1_y):
    #hiermit sollte das Bild nun immer am unteren Bildschirmrand sein 
    gameDisplay.blit(pygame.transform.scale(P1_Img, (75, 75)), (P1_x, P1_y))

def player_2(P2_x,P2_y):
    global player_P2
    if player_P2 == True:
        gameDisplay.blit(pygame.transform.scale(P2_Img, (75, 75)), (P2_x, P2_y))
    
def player_P2_true():
    global player_P2
    player_P2 = True

def player_P2_false():
    global player_P2
    player_P2 = False  

def P1_hide():
    global p1_dead
    global P1_x
    global P1_y    
    p1_dead = True
    P1_x = -30000
    P1_y = 20000
    pygame.display.update()
    
def P1_unhide():
    global P1_x
    global P1_y
    global display_height
    global display_width
    P1_x = display_width * 0.5
    P1_y = display_height * 0.8
    pygame.display.update() 
    
def   P2_hide():
	global p2_dead
	global P2_x
	global P2_y
	p2_dead = True
	P2_x = -30000
	P2_y = 20000
	pygame.display.update()

def P2_unhide():
    global P2_x
    global P2_y
    global display_height
    global display_width
    P2_x = display_width * 0.5
    P2_y = display_height * 0.8
    pygame.display.update() 

    
def things(thing_x, thing_y, thing_h, thing_w, color):
    pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_w, thing_h])

def things_3(thing_3_x, thing_3_y, thing_3_h, thing_3_w, color):
    pygame.draw.rect(gameDisplay, color, [thing_3_x, thing_3_y, thing_3_h, thing_3_w])

def things_2(thing_2_x, thing_2_y, thing_2_h, thing_2_w, color):
    pygame.draw.rect(gameDisplay, color, [thing_2_x, thing_2_y, thing_2_h, thing_2_w])

def things_4(thing_4_x, thing_4_y, thing_4_h, thing_4_w, color):
    pygame.draw.rect(gameDisplay, color, [thing_4_x, thing_4_y, thing_4_h, thing_4_w])

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
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
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

def game_intro():
    pygame.init()
    intro = True
    while intro:
        global player_P2
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
        button("Player 2 Aktive",375,450,175,50,dark_brown,light_brown,player_P2_true)
        button("Player 2 Deactive",600,450,175,50,dark_brown,light_brown,player_P2_false)
        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    global player_P2
    global player_P1
    global p1_dead
    global p2_dead
    global p1_dead_start
    global p2_dead_start
    global P1_x
    global P1_y
    global P2_x
    global P2_y
    global p1_lives
    global p2_lives
    #variabeln_2:
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    yellow = (0,255,0)
    blue = (0,0,255)
    dark_brown = (100,75,75)
    grey = (65,65,65)
    light_grey = (130,130,130)
    # Ich würde hier nur einen lokalen Pfad nehmen. Also einfach die Bilddatei in das selbe Verzeichnis wie die Python-Datei
    #player_1 1:
    P1_x = (display_width * 0.50)
    P1_y = (display_height * 0.8)
    P1_x_change = 0
    P1_y_change = 0
    #player 2:
    P2_x = (display_width * 0.40)
    P2_y = (display_height * 0.8)
    P2_x_change = 0
    P2_y_change = 0
    gameExit = False
    score = 0
    p1_lives = 3
    p2_lives = 3
    
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

    #thing 3:

    thing_3_start_x = random.randrange(0, display_width)
    thing_3_start_y = -700
    thing_3_speed = 5
    thing_3_width = 45
    thing_3_height = 45

    #thing 4:

    thing_4_start_x = 1300
    thing_4_start_y = random.randrange(0, display_height)
    thing_4_speed = 3
    thing_4_width = 100
    thing_4_height = 100


    #Initialisierung:
    pygame.init()
    pygame.display.set_caption("Avalonion")

    # Punkt Komma Groß
    clock = pygame.time.Clock()

    while not gameExit:
        if p1_dead == True:
            p1_dead_end = time.time()
            p1_dead_diff = p1_dead_end - p1_dead_start
            if p1_dead_diff < 3000:
                P1_unhide()
            if p1_dead_diff < 6000:
                p1_dead = False
        if p2_dead == True:
            p2_dead_end = time.time()
            p2_dead_diff = p2_dead_end - p2_dead_start
            if p2_dead_diff < 30000:
                P2_unhide()
            if p2_dead_diff < 6000:
                p2_dead = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #player_1 1 controls:
            
            if player_P1 == True and p1_dead == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        P1_x_change = -6.5
                    elif event.key == pygame.K_RIGHT:
                        P1_x_change = 6.5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        P1_x_change = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        P1_y_change = -6.5
                    elif event.key == pygame.K_DOWN:
                        P1_y_change = 6.5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        P1_y_change = 0

                    if event.key == pygame.K_p:
                        pause = True
                        paused()
            #Player 2 controls:
            if player_P2 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        P2_x_change = -6.5
                    elif event.key == pygame.K_d:
                        P2_x_change = 6.5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        P2_x_change = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        P2_y_change = -6.5
                    elif event.key == pygame.K_s:
                        P2_y_change = 6.5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        P2_y_change = 0

                    if event.key == pygame.K_p:
                        pause = True
                        paused()
                
        # variabeln 2 :
        P1_x += P1_x_change
        P1_y += P1_y_change

        P2_x += P2_x_change
        P2_y += P2_y_change
            # Die folgenden Zeilen sollen alle durch den while-loop wiederholt werden...
            # Sie müssen also die selbe Einrückung haben wie das for.
            # Allerdings nicht wie das if, da sie sonst für jedes event wiederholt würden.
        gameDisplay.fill(white)

        if player_P1 == True:
            player_1(P1_x,P1_y)
        if player_P2 == True:
            player_2(P2_x,P2_y)

        Score(score)
        Lives(p1_lives, p2_lives)
        #things(thin_x, thing_y, thing_h, thing_w, color)
        things(thing_start_x, thing_start_y, thing_height, thing_width, black)
        thing_start_y += thing_speed
        things_2(thing_2_start_x, thing_2_start_y, thing_2_height, thing_2_width, light_grey)
        thing_2_start_x += thing_2_speed
        things_3(thing_3_start_x, thing_3_start_y, thing_3_height, thing_3_width, dark_brown)
        thing_3_start_y += thing_3_speed
        things_4(thing_4_start_x, thing_4_start_y, thing_4_height, thing_4_width, grey)
        thing_4_start_x -= thing_4_speed
        #player_1 1:
        if player_P1 == True and p1_dead == False:
            if P1_x > display_width - img_width or P1_x < 0:
                p1_dead = True
                p1_dead_start = time.time()
                P1_hide()
                p1_lives -= 1
                if p1_lives == 0:
                    crash()

            if P1_y > display_height - img_height or P1_y < 0:
                p1_dead = True
                p1_dead_start = time.time()
                P1_hide()
                p1_lives -= 1
                if p1_lives == 0:
                    crash()
        #Player 2:
        if player_P2 == True:
            if P2_x > display_width - img_width or P2_x < 0:
                p2_dead = True
                p2_dead_start = time.time()
                P2_hide()
                p2_lives -= 1
                if p2_lives == 0:
                    crash()
            if P2_y > display_height - img_height or P2_y < 0:
                p2_dead = True
                p2_dead_start = time.time()
                P2_hide()
                p2_lives -= 1
                if p2_lives == 0:
                    crash()

        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)
            score += 1

        if thing_2_start_x > display_width:
            thing_2_start_x = 0 - thing_2_width
            thing_2_start_y = random.randrange(0, display_height)
            score += 1

        if thing_3_start_y > display_height:
            thing_3_start_y = 0 - thing_3_width
            thing_3_start_x = random.randrange(0, display_height)
            score += 1

        if thing_4_start_x < 0 - thing_4_width:
            thing_4_start_x = display_width + thing_4_width
            thing_4_start_y = random.randrange(0, display_height)
            score += 1
        #Player 1 Kollisionen:
        if player_P1 == True and p1_dead == False:
            if P1_y <= thing_start_y + thing_height and P1_y >= thing_start_y - thing_height:
                if P1_x > thing_start_x and P1_x < thing_start_x + thing_width or P1_x + img_width > thing_start_x and P1_x + img_width < thing_start_x + thing_width:
                    p1_dead = True
                    p1_dead_start = time.time()
                    P1_hide()
                    p1_lives -= 1
                    if p1_lives == 0:
                        crash()
            if P1_x <= thing_2_start_x + thing_2_height and P1_x >= thing_2_start_x - thing_2_height:
                if P1_y > thing_2_start_y and P1_y < thing_2_start_y + thing_2_width or P1_y + img_width > thing_2_start_y and P1_y + img_width < thing_2_start_y + thing_2_width:
                    p1_dead = True
                    p1_dead_start = time.time()
                    P1_hide()
                    p1_lives -= 1
                    if p1_lives == 0:
                        crash()
            if P1_x <= thing_3_start_x + thing_3_height and P1_x >= thing_3_start_x - thing_3_height:
                if P1_y > thing_3_start_y and P1_y < thing_3_start_y + thing_3_width or P1_y + img_width > thing_3_start_y and P1_y + img_width < thing_3_start_y + thing_3_width:
                    p1_dead = True
                    p1_dead_start = time.time()
                    P1_hide()
                    p1_lives -= 1
                    if p1_lives == 0:
                        crash()
            if P1_x <= thing_4_start_x + thing_4_height and P1_x >= thing_4_start_x - thing_4_height:
                if P1_y > thing_4_start_y and P1_y < thing_4_start_y + thing_4_width or P1_y + img_width > thing_4_start_y and P1_y + img_width < thing_4_start_y + thing_4_width:
                    p1_dead = True
                    p1_dead_start = time.time()
                    P1_hide()
                    p1_lives -= 1
                    if p1_lives == 0:
                        crash()
        #Player 2 Kollisionen:
        if player_P2 == True:        
            if P2_y <= thing_start_y + thing_height and P2_y >= thing_start_y - thing_height:
                if P2_x > thing_start_x and P2_x < thing_start_x + thing_width or P2_x + img_width > thing_start_x and P2_x + img_width < thing_start_x + thing_width:
                    p2_dead = True
                    p2_dead_start = time.time()
                    P2_hide()
                    p2_lives -= 1
                    if p2_lives == 0:
                        crash()
            if P2_x <= thing_2_start_x + thing_2_height and P2_x >= thing_2_start_x - thing_2_height:
                if P2_y > thing_2_start_y and P2_y < thing_2_start_y + thing_2_width or P2_y + img_width > thing_2_start_y and P2_y + img_width < thing_2_start_y + thing_2_width:
                    p2_dead = True
                    p2_dead_start = time.time()
                    P2_hide()
                    p2_lives -= 1
                    if p2_lives == 0:
                        crash()
            if P2_x <= thing_3_start_x + thing_3_height and P2_x >= thing_3_start_x - thing_3_height:
                if P2_y > thing_3_start_y and P2_y < thing_3_start_y + thing_3_width or P2_y + img_width > thing_3_start_y and P2_y + img_width < thing_3_start_y + thing_3_width:
                    p2_dead = True
                    p2_dead_start = time.time()
                    P2_hide()
                    p2_lives -= 1
                    if p2_lives == 0:
                        crash()
            if P2_x <= thing_4_start_x + thing_4_height and P2_x >= thing_4_start_x - thing_4_height:
                if P2_y > thing_4_start_y and P2_y < thing_4_start_y + thing_4_width or P2_y + img_width > thing_4_start_y and P2_y + img_width < thing_4_start_y + thing_4_width:
                    p2_dead = True
                    p2_dead_start = time.time()
                    P2_hide()
                    p2_lives -= 1
                    if p2_lives == 0:
                    	crash()

        pygame.display.update()
        clock.tick(60)
        thing_speed += 0.001
        thing_2_speed += 0.001
        thing_3_speed += 0.002
        thing_4_speed += 0.001
        #score()
# Das soll nur einmal am Ende ausgeführt werden, also ist es wieder ganz ausgerückt.
game_intro()
game_loop()
pygame.quit()
quit()
