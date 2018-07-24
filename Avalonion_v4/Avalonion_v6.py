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
        self.Background = pygame.image.load('Avalonion_Hintergrund.png').convert()
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
        self.FPS = 60


### game wurde erstellt um später auf dinge daraus zu zugreifen
game = Game()



class Player(pygame.sprite.Sprite):
    def __init__(self, Img, dead, exists, died_at_time, lives, score, pos_x, pos_y, x_change, y_change,playerid ,game):
        pygame.sprite.Sprite.__init__(self)
        # https://stackoverflow.com/questions/14449320/attributeerror-sprite-object-has-no-attribute-image
        self.image = pygame.image.load("pixelart-klein.png")
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
        self.playerid = playerid

    def P_update(self,playerid):
                ### jetzt habe ich für beide spieler je ein key-setup
        self.playerid = playerid
        if playerid == 1:
            keys = [pygame.K_UP,
                        pygame.K_DOWN,
                        pygame.K_LEFT,
                        pygame.K_RIGHT]
        if playerid == 2:
            keys = [pygame.K_w,
                        pygame.K_s,
                        pygame.K_a,
                        pygame.K_d]
        keystate = pygame.key.get_pressed()
        if keystate[keys[2]]:
            self.rect.move_ip(-5,0)
        if keystate[keys[3]]:
            self.rect.move_ip(5,0)
        if keystate[keys[0]]:
            self.rect.move_ip(0,-5)
        if keystate[keys[1]]:
            self.rect.move_ip(0,5)

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
    def __init__(self,objekt_x, objekt_y, speed, color=game.black,image=pygame.image.load("pixelart-klein.png")):
        pygame.sprite.Sprite.__init__(self)
        self.start_pos = [objekt_x, objekt_y]
        self.speed = speed
        self.acceleration = [0 ,-0.001]

        self.image = image
        self.rect = self.image.get_rect()



    def Move(self):
        self.speed += self.acceleration
        self.rect.move_ip((self.speed[0],self.speed[1]))


def Game_start():
                ### spieler 1 und 2 parameter/erstellung
    p1 = Player(pygame.image.load('Pixelart_P1.png'),False,True,None,3,0,game.display_width * 0.5,game.display_height * 0.8 ,0,0,1, game)
    p2 = Player(pygame.image.load('Pixelart_P2.png'),False,False,None,3,0,game.display_width * 0.4,game.display_height * 0.8 ,0,0,2, game)
            ### Players ist eine sprite gruppe die p1 und p2 enthält
    players = pygame.sprite.Group()
    players.add(p1)
    players.add(p2)
    p1.rect.move_ip(p1.pos)
    p2.rect.move_ip(p2.pos)
            ### objects ist eine sprite gruppe die objekt 1-4 enthält
    objects = pygame.sprite.Group()
    objects.add(Object(random.randrange(0,game.display_width),0, [0,5]))
    objects.add(Object(random.randrange(0,game.display_width),0, [0 ,-4]))
    objects.add(Object(0,(random.randrange(0,game.display_height)), [5 ,0]))
    objects.add(Object(1300,(random.randrange(0,game.display_height)), [-3 ,0]))
    for object in objects:
        object.rect.move_ip(object.start_pos[0] ,object.start_pos[1])


    gameExit = False
    while not gameExit:
        # Da jetzt die Spieler in einer Liste Sind muss nicht mehr immer alles doppelt geschrieben werden.
        for p in players:
            if p.dead:
                # Vielleicht sowas?
                p.exists = False
                players.remove(p)
                if p.dead_diff > 2:
                    players.add(p)
                    p.dead_change = True
                if p.dead_diff > 5:
                    p.dead = False
                    p.dead_change = False
        ### checkt ob der User auf das X gedrückt hat ,wenn ja endet das programm
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.key.get_pressed == pygame.K_p:
                pause = True
                paused()


        game.game_Display.fill(game.black)
        game.game_Display.blit(game.Background,(0,0))    ### hierbei wird das programm immernoch stark verlangsamt
                                                         ### ---> habe das problem lösen können indem ich hinter das "pygame.image.load('Avalonion_Hintergrund.png')" ein ".convert()" gesetzt habe

        for p in players:
            if p.exists and not p.dead:
                p.P_update(p.playerid)


        for o in objects:
            o.Move()


        for object in objects:
            if object.rect[0] > game.display_width + 50 or object.rect[1] > game.display_height + 50:
                object.rect.move_ip(object.start_pos[0] ,object.start_pos[1])                               ### Sollte die objekte nach verlassen des Bildschirmes wieder auf ihre 
                                                                                                            ### Start position zurück setzen ,tuts aber nicht ^_^
        players.update()
        objects.update()
        players.draw(game.game_Display)
        objects.draw(game.game_Display)


        pygame.display.update()
        game.clock.tick(game.FPS)

Game_start()
pygame.quit()
quit()
