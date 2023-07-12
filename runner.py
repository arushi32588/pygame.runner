import pygame
from sys import exit

pygame.init() #Initiates pygame
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Runner') #Naming the title of the window
clock = pygame.time.Clock()
font1 = pygame.font.Font('font/Pixeltype.ttf', 50)
font2 = pygame.font.Font('font/Pixeltype.ttf', 25)

sky_surface = pygame.image.load('graphics/Sky.jpeg').convert()
ground_surface = pygame.image.load('graphics/ground.jpeg').convert()

player_surf = pygame.image.load('graphics/Player/walk1.png')
player_rect = player_surf.get_rect(midbottom = (80, 300))

text_surface1 = font1.render('Runner', False, 'Black')
text_surface2 = font2.render('By Arushi', False, 'Black')

while True:
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #ends the while True loop so that it cannot continue to update and throw an error
    # draw all our elements
    screen.blit(ground_surface, (0,300)) # telling the system we want to place a ground on display surface
    screen.blit(sky_surface, (0,0)) # telling the system we want to place a sky on display surface
    screen.blit(text_surface1, (325, 50))
    screen.blit(text_surface2, (335, 80))
    screen.blit(player_surf, player_rect)


    # update everything
    pygame.display.update() # updates everything happening in the loop to display
    clock.tick(60) # telling the while loop it should not run more than 60 times/second

