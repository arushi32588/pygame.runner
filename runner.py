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

snail_surf = pygame.image.load('graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (700,300))

score_surf = font1.render('Runner', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50))

by_surf = font2.render('By Arushi', False, 'Black')
by_rect = by_surf.get_rect(center = (400, 80))

while True:
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #ends the while True loop so that it cannot continue to update and throw an error
    # draw all our elements
    screen.blit(ground_surface, (0,300)) # telling the system we want to place a ground on display surface
    screen.blit(sky_surface, (0,0)) # telling the system we want to place a sky on display surface
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surf, score_rect)
    screen.blit(by_surf, by_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(snail_surf, snail_rect)
    snail_rect.left -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    # update everything
    pygame.display.update() # updates everything happening in the loop to display
    clock.tick(60) # telling the while loop it should not run more than 60 times/second


