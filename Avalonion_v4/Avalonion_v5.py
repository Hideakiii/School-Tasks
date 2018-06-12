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
        self.game_Display = pygame.display.set_mode((display_width,display_height))
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
           


























objects[1].acceleration = 0.002
for obj in objects:
    obj.Move()




game_intro()
Game_Loop()
pygame.quit()
quit()
