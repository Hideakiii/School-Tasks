import pygame
import random
import time
import os

pygame.init()

### game class enthält alle wichtigen variabeln

class Game:
    def __init__(self):
        self.display_width = 800
        self.display_height = 600
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


### game wurde erstellt um später auf dinge daraus zu zugreifen
game = Game()



class Player(pygame.sprite.Sprite):
    def __init__(self, Img, dead, exists, died_at_time, lives, score, pos_x, pos_y, x_change, y_change, game):
        pygame.sprite.Sprite.__init__(self)
        # https://stackoverflow.com/questions/14449320/attributeerror-sprite-object-has-no-attribute-image
        self.image = pygame.image.load("pixelart-klein.jpg")
        self.rect = self.image.get_rect()
        print(self.rect)

        self.dead = False
        self.exists = True
        self.dead_change = False
        # Das hier ist so der Zeitpunkt zu dem der Spieler startet. nicht stirbt.
        self.dead_end = time.time()
        self.died_at_time = None
        # Das kann natürlich erst berechnet werden, wenn der Spieler gestorben ist...
        #self.dead_diff = self.dead_end - died_at_time
        self.lives = max(3,lives)
        self.score = score
        ### Player position x/y
        self.pos = [pos_x,pos_y]
        self.game = game
        self.x_change = x_change
        self.y_change = y_change

    def P_update(self):
        speed = [0,-0.2]
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            speed[0] = -5
        if keystate[pygame.K_RIGHT]:
            speed[0] = 5
        if keystate[pygame.K_UP]:
            speed[1] = -5
        if keystate[pygame.K_DOWN]:
            speed[1] = 5

        # Hier muss eventuell nicht das pos von dem Player verändert werden,
        # sondern direkt die angabe in rect. Man versucht immer die Daten nur
        # einmal zu haben, um zu vermeiden, dass man einzelne bei aktualisierungen
        # vergisst. z.B: https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move
        self.pos[0] += speed[0]
        self.pos[1] += speed[1]
        self.rect[0] = self.pos[0]
        self.rect[1] = self.pos[1]

    def DrawScore(self):
        font = pygame.font.SysFont(None, 25)
        self.text = font.render("Score : "+ str(self.score), True, black)
        self.game.game_Display.blit(text, (0,0))

      ### P = Player 1/2 ,lives, l_xy = anzeige Position(x,y)
    def DrawLives(self,P,P_lives,l_xy):
        font = pygame.font.SysFont(None, 25)
        self.text = font.render(str(P)+ str(P_lives),True, black )
        self.game_Display.blit(text, (l_xy))

# Auch Object soll ein ein Sprite sein
class Object(pygame.sprite.Sprite):
    #Hinzufügen der Standardfarbe schwarz
    def __init__(self,objekt_x, objekt_y, objekt_h, objekt_w, speed, color=game.black):
        pygame.sprite.Sprite.__init__(self)
        self.pos = [objekt_x,objekt_y]
        self.objekt_h = objekt_h
        self.objekt_w = objekt_w
        self.speed = [0,1]
        self.acceleration = 0.001
        self.color=color
        pygame.draw.rect(game.game_Display,self.color,[objekt_x,objekt_y,objekt_h,objekt_w])

    def Move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        self.speed += self.acceleration


def Game_start():
                ### spieler 1 und 2 parameter/erstellung
    p1 = Player(pygame.image.load('Pixelart_P1.png'),False,True,None,3,0,game.display_width * 0.4,game.display_height * 0.8 ,0,0,game)
    p2 = Player(pygame.image.load('Pixelart_P1.png'),False,False,None,3,0,game.display_width * 0.5,game.display_height * 0.8 ,0,0,game)
            ### Players ist eine sprite gruppe die p1 und p2 enthält
    players = pygame.sprite.Group()
    players.add(p1)
    players.add(p2)
            ### objects ist eine sprite gruppe die objekt 1-4 enthält
    objects = pygame.sprite.Group()
    objects.add(Object(random.randrange(0,game.display_width),-700,75,75, 5))
    objects.add(Object(random.randrange(0,game.display_width),-700,45,45, 4))
    objects.add(Object(-1300,(random.randrange(0,game.display_height)),75,75, 5))
    objects.add(Object(1300,(random.randrange(0,game.display_height)),100,100, 3))

    gameExit = False
    while not gameExit:
        # Da jetzt die Spieler in einer Liste Sind muss nicht mehr immer alles doppelt geschrieben werden.
        for p in players:
            if p.dead:
                # Vielleicht sowas?
                p.exists = False
                players.remove(p)
                if p1.dead_diff > 2:
                    players.add(p1)
                    p1.dead_change = True
                if p1.dead_diff > 5:
                    p1.dead = False
                    p1.dead_change = False
        ### checkt ob der User auf das X gedrückt hat ,wenn ja endet das programm
        for event in pygame.event.get():
            if event.type == pygame.QUIT or not p1.exists and not p2.exists:
                pygame.quit()
                quit()
            #TODO
            #if event.key == pygame.K_p:
            #    pause = True
            #    paused()

        game.game_Display.fill(game.black)
        for p in players:
            if p.exists and not p.dead:
                p.P_update()
                print(p.rect)
        players.update()
        players.draw(game.game_Display)

        pygame.display.update()

Game_start()
pygame.quit()
quit()
