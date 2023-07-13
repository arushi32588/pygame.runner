import pygame
from sys import exit

pygame.init() #Initiates pygame
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Runner') #Naming the title of the window
clock = pygame.time.Clock()
font1 = pygame.font.Font('font/Pixeltype.ttf', 50)
font2 = pygame.font.Font('font/Pixeltype.ttf', 25)
game_active = True
start_time = 0

sky_surface = pygame.image.load('graphics/Sky.jpeg').convert()
ground_surface = pygame.image.load('graphics/Ground.jpeg').convert()

player_surf = pygame.image.load('graphics/Player/walk1.png')
player_rect = player_surf.get_rect(midbottom = (80, 300))

player_gravity = 0

snail_surf = pygame.image.load('graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (700,300))

#score_surf = font1.render('Runner', False, (64, 64, 64))
#score_rect = score_surf.get_rect(center = (400, 50))

#by_surf = font2.render('By Arushi', False, 'Black')
#by_rect = by_surf.get_rect(center = (400, 80))

while True:
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #ends the while True loop so that it cannot continue to update and throw an error
        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -23
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 700
                start_time = int(pygame.time.get_ticks()/1000)

        # draw all our elements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_gravity = -23
    if game_active == True:
        screen.blit(ground_surface, (0,300)) # telling the system we want to place a ground on display surface
        screen.blit(sky_surface, (0,0)) # telling the system we want to place a sky on display surface
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surf, score_rect)
        #screen.blit(by_surf, by_rect)

        current_time = int(pygame.time.get_ticks()/1000) - start_time
        score_surf = font1.render(f'SCORE: {current_time}', False, (64,64,64))
        score_rect = score_surf.get_rect(center = (400,50))
        screen.blit(score_surf, score_rect)
        #Player
        #Gravity
        player_gravity+=1 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
        screen.blit(snail_surf, snail_rect)
        snail_rect.left -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        #Collision
        if snail_rect.colliderect(player_rect) == 1:
            game_active = False
    else:
        screen.fill('Yellow')

    '''keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('jump')'''

    # update everything
    pygame.display.update() # updates everything happening in the loop to display
    #clock.tick(60) # telling the while loop it should not run more than 60 times/second
    if current_time<= 10:
        clock.tick(60)
    elif current_time in range (10, 20):
        clock.tick(80)
    elif current_time in range (20, 30):
        clock.tick(100)
    elif current_time in range (30, 40):
        clock.tick(120)
    elif current_time in range (40, 50):
        clock.tick(140)
    elif current_time in range (50, 60):
        clock.tick(160)
    elif current_time in range (60, 70):
        clock.tick(180)
    elif current_time in range (70, 80):
        clock.tick(200)
    elif current_time in range (80, 90):
        clock.tick(220)
    else:
        clock.tick(240)

