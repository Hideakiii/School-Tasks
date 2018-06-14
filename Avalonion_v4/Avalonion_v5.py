import pygame
import random
import time
import os

pygame.init()

### game class enthält alle wichtigen variabeln

class Game:
    def __init__(self):
        self.display_width = 1200
        self.display_height = 700
        self.game_Display = pygame.display.set_mode((self.display_width,self.display_height))
        self.clock = pygame.time.Clock()
        self.pause = False
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (200,0,0)
        self.bright_red = (255,0,0)
        self.green = (0,200,0)
        self.bright_green = (0,255,0)
        self.grey = (65,65,65)
        self.light_grey = (80,80,80)
        self.dark_brown = (90,75,80)
        self.light_brown = (110,95,100)
        self.font = pygame.font.SysFont(None, 25)
        self.largeText = pygame.font.Font("freesansbold.ttf",115)
        pygame.TextSurf, pygame.TextRect = text_objects("Paused", largeText)
        pygame.TextRect.center = ((self.display_width/2),(self.display_height/2))
        
    def button(self,msg,x,y,w,h,ic,ac,action=None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if x + w > self.mouse[0] > x and y + h > self.mouse[1] > y:
                                      #ac = active color
            pygame.draw.rect(game_Display, ac, (x,y,w,h))
            if self.click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(self,game_Display,ic,(x,y,w,h))
            smallText = pygame.font.Font("freesansbold.ttf", 20)
            pygame.textSurf, pygame.textRect = text_objects(msg, smallText)
            pygame.textRect.center = ((x+(w/2)), (y+(h/2)))
            game_Display.blit(pygame.textSurf, pygame.textRect)
        
    def text_objects(self,text, font):
        self.textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(self,text):
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (self.display_width/2),(self.display_height/2))
        game_Display.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)
        Game_Loop()
        
    def quitgame(self):
        pygame.quit()
        quit()
        
    def paused(self):
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            game_Display.blit(self.TextSurf, TextRect)
            #buttons:
            self.button("Continue",250,550,150,50,green,bright_green,unpause)
            self.button("Quit",750,550,150,50,red,bright_red,quitgame)
            self.button("Player 2 Aktive",375,450,175,50,dark_brown,light_brown,player_P2_true)
            self.button("Player 2 Deactive",600,450,175,50,dark_brown,light_brown,player_P2_false)

            pygame.display.update()
            clock.tick(15)

    def game_intro(self):
        pygame.init()
        self.intro = True
        while self.intro:
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
            self.button("Start!",250,550,150,50,green,bright_green,Game_Loop)
            self.button("Quit!",750,550,150,50,red,bright_red,quitgame)
            self.button("Player 2 Aktive",375,450,175,50,dark_brown,light_brown,player_P2_true)
            self.button("Player 2 Deactive",600,450,175,50,dark_brown,light_brown,player_P2_false)
            pygame.display.update()
            clock.tick(15)

    def crash(self):

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
            self.button("Play Again",250,550,150,50,green,bright_green,Game_Loop)
            self.button("Quit",750,550,150,50,red,bright_red,quitgame)

            pygame.display.update()
            clock.tick(15)
    


### game wurde erstellt um später auf dinge daraus zu zugreifen
game = Game



class Player(pygame.sprite.Sprite):
    def __init__(self, Img, dead, exists, died_at_time, lives, score, pos_x, pos_y, x_change, y_change, game):
        pygame.sprite.Sprite.__init__(self)
        self.Img = 0
        self.dead = False
        self.dead_change = False
        self.exists = True
        self.died_at_time = None
        self.lives = max(3,lives)
        self.score = score
        ### Player position x/y
        self.pos = [pos_x,pos_y]
        self.game = game
        self.x_change = x_change
        self.y_change = y_change

    def DrawScore(self):
        font = pygame.font.SysFont(None, 25)
        self.text = font.render("Score : "+ str(self.score), True, black)
        self.game.game_Display.blit(text, (0,0))

      ### P = Player 1/2 ,lives, l_xy = anzeige Position(x,y)
    def DrawLives(self,P,P_lives,l_xy):
        font = pygame.font.SysFont(None, 25)
        self.text = font.render(str(P)+ str(P_lives),True, black )
        self.game_Display.blit(text, (l_xy))

    def Hide(self,pos_x,pos_y):
        self.pos_x = -30000
        self.pos_y = 20000
        pygame.display.update()

    def Unhide(self,pos_x,pos_y):
        self.pos_x = display_width * 0.45
        self.pos_y = display_height * 0.8
        pygame.display,update()

class Object:
    def __init__(self,objekt_x, objekt_y, objekt_h, objekt_w, speed):
        self.pos = [objekt_x,objekt_y]
        self.objekt_h = objekt_h 
        self.objekt_w = objekt_w
        self.speed = [0,1]
        self.acceleration = 0.001
        pygame.draw.rect(game_Display,color,[objekt_x,objekt_y,objekt_h,objekt_w]) 

    def Move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        self.speed += self.acceleration
        

    
        ### spieler 1 und 2 parameter/erstellung
p1 = Player(pygame.image.load('Pixelart_P1.png'),False,True,None,3,0,display_width * 0.4,display_height * 0.8 ,0,0,game)
p2 = Player(pygame.image.load('Pixelart_P1.png'),False,False,None,3,0,display_width * 0.5,display_height * 0.8 ,0,0,game)
        ### Players ist eine sprite gruppe die p1 und p2 enthält
players = pygame.sprite.Group()
players.add(p1)
players.add(p2)
        ### objects ist eine sprite gruppe die objekt 1-4 enthält
objects = pygame.sprite.Group()
objects.add(Object(random.randrange(0,display_width),-700,75,75, 5))
objects.add(Object(random.randrange(0,display_width),-700,45,45, 4))
objects.add(Object(-1300,(random.randrange(0,display_height)),75,75, 5))
objects.add(Object(1300,(random.randrange(0,display_height)),100,100, 3))

hit_list = pygame.sprite.spritecollide(players, objects, True)


           


























objects[1].acceleration = 0.002
for obj in objects:
    obj.Move()




game_intro()
Game_Loop()
pygame.quit()
quit()
