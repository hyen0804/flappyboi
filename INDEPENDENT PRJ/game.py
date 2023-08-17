import pygame
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Running man')
clock = pygame.time.Clock()

test_surface = pygame.image.load('graphics/sky.png').convert()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  
            
    screen.blit(test_surface,(0,0))
    
    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)
     