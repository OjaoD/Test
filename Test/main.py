import pygame
from depends import *

player = Player(x=250,y=300,speed=4,image="player-01.png")
bg = load('background.png')
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        player.events(event)
    screen.blit(bg,(0,0))
    
    player.draw(screen)
    player.walk()

    pygame.display.update()
    clock.tick(60)