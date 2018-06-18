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
        self.Img = pygame.Surface((75,75))
        self.Img.fill(green)
        self.dead = False
        self.exists = True
        self.dead_change = False
        self.dead_end = time.time()
        self.died_at_time = None
        self.dead_diff = dead_end - died_at_time
        self.lives = max(3,lives)
        self.score = score
        ### Player position x/y
        self.pos = [pos_x,pos_y]
        self.game = game
        self.x_change = x_change
        self.y_change = y_change
        self.rect = self.Img.get_rect()

    def P_update(self):
        self.P_speed = self.pos[0,1]
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.P_speed[0] = -5
        if keystate[pygame.K_RIGHT]:
            self.P_speed[0] = 5
        if keystate[pygame.K_UP]:
            self.P_speed[1] = -5
        if keystate[pygame.K_DOWN]:
            self.P_speed[1] = 5
        self.rect.pos[0,1] += P_speed

    def DrawScore(self):
        font = pygame.font.SysFont(None, 25)
        self.text = font.render("Score : "+ str(self.score), True, black)
        self.game.game_Display.blit(text, (0,0))

      ### P = Player 1/2 ,lives, l_xy = anzeige Position(x,y)
    def DrawLives(self,P,P_lives,l_xy):
        font = pygame.font.SysFont(None, 25)
        self.text = font.render(str(P)+ str(P_lives),True, black )
        self.game_Display.blit(text, (l_xy))


class Object:
    def __init__(self,objekt_x, objekt_y, objekt_h, objekt_w, speed):
        self.pos = [objekt_x,objekt_y]
        self.objekt_h = objekt_h 
        self.objekt_w = objekt_w
        self.speed = [0,1]
        self.acceleration = 0.001
        pygame.draw.rect(game.game_Display,color,[objekt_x,objekt_y,objekt_h,objekt_w]) 

    def Move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        self.speed += self.acceleration


def Game_start():
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


    while not gameExit:

        if p1.dead:
            p1.dead = True
            players.remove(p1)
            if p1.dead_diff > 2:
                players.add(p1)
                p1.dead_change = True
            if p1.dead_diff > 5:
                p1.dead = False
                p1.dead_change = False
        if p2.dead:
            p2.dead = True
            players.remove(p2)
            if p2.dead_diff > 2:
                players.add(p2)
                p2.dead_change = True
            if p2.dead_diff > 5:
                p2.dead = False
                p2.dead_change = False
            ### checkt ob der User auf das X gedrückt hat ,wenn ja endet das programm
        for event in pygame.event.get():
            if event.type == pygame.QUIT or not player_P1 and not player_P2:
                pygame.quit()
                quit()

        if p1.exists and not p1.dead:
            p1.P_update()

        if p2.exists and not p2.dead:
            p2.P_update()

        if event.key == pygame.K_p:
            pause = True
            paused()
        ### player und objekte werden hier hinzugefügt
        players()
        objects()




        
           


























    objects[1].acceleration = 0.002
    for obj in objects:
        obj.Move()




game_intro()
Game_Loop()
pygame.quit()
quit()
