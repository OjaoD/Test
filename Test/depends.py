import pygame
from sys import exit

#deixar mais facil para dar load em imagens
def load(name):
    return pygame.image.load(f'files/{name}').convert_alpha()

pygame.init()
#nome da janela
pygame.display.set_caption('Test')
#screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN, vsync=1)
screen = pygame.display.set_mode((1280,1024),)

class Player:
    def __init__(self, x, y,speed,image):
        self.x = x
        self.y = y
        self.speed = speed
        #carregar imagens e tratar delas
        self.image_R = load('player-R.png')
        self.image_R = pygame.transform.scale(self.image_R,(64,64))
        self.image_R_rect = self.image_R.get_rect(center=(self.image_R.get_width()/2, self.image_R.get_height()/2))

        self.image_L = load('player-L.png')
        self.image_L = pygame.transform.scale(self.image_L,(64,64))
        self.image_L_rect = self.image_L.get_rect(center=(self.image_L.get_width()/2, self.image_L.get_height()/2))
        
        self.image_U = load('player-U.png')
        self.image_U = pygame.transform.scale(self.image_U,(64,64))
        self.image_U_rect = self.image_U.get_rect(center=(self.image_U.get_width()/2, self.image_U.get_height()/2))

        
        #variaveis de direcoes rw=right_walk
        self.rw = False
        self.lw = False
        self.uw = False
        self.dw = False
        self.direction = 1

    def events(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.rw = True
            elif event.key == pygame.K_a:
                self.lw = True
            elif event.key == pygame.K_w:
                self.uw = True
            elif event.key == pygame.K_s:
                self.dw = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.rw = False
            elif event.key == pygame.K_a:
                self.lw = False
            elif event.key == pygame.K_w:
                self.uw = False
            elif event.key == pygame.K_s:
                self.dw = False

    def draw(self,screen):
        if self.direction == 1:
            screen.blit(self.image_R,(self.x,self.y), self.image_R_rect)
        elif self.direction == 2:
            screen.blit(self.image_L,(self.x,self.y), self.image_L_rect)
        elif self.direction == 3:
            screen.blit(self.image_U,(self.x,self.y), self.image_U_rect)
        


    
    def walk(self):
        if self.rw:
            self.x += self.speed
            self.direction = 1
        elif self.lw:
            self.x -= self.speed
            self.direction = 2
        elif self.uw:
            self.y -= self.speed
            self.direction = 3
        elif self.dw:
            self.y += self.speed