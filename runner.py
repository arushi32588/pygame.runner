import pygame
from sys import exit


pygame.init() #Initiates pygame
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Runner') #Naming the title of the window
clock = pygame.time.Clock()
font1 = pygame.font.Font('font/Pixeltype.ttf', 50)
font2 = pygame.font.Font('font/Pixeltype.ttf', 70)
game_active = -1
start_time = 0
score = 0
sky_surface = pygame.image.load('graphics/Sky.jpeg').convert()
ground_surface = pygame.image.load('graphics/Ground.jpeg').convert()

player_surf = pygame.image.load('graphics/Player/walk1.png')
player_rect = player_surf.get_rect(midbottom = (80, 300))

player_stand = pygame.image.load('graphics/Player/stand.png')
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

player_gravity = 0

snail_surf = pygame.image.load('graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (700,300))

welcome_1 = font2.render("Hi! I'm the Pixel Runner", False, 'Yellow')
welcome_1_rect = welcome_1.get_rect(center = (400, 50))

welcome_2 = font1.render("PRESS 'ENTER' to start the game", True, 'White')
welcome_2_rect = welcome_2.get_rect(center = (400, 90) )

game_over = font2.render('Game over', False, 'Red')
game_over_rect = game_over.get_rect(center =(400, 50))

leaderboard = font1.render('LEADERBOARD', False, 'Yellow')
leaderboard_rect = leaderboard.get_rect(center = (400, 90))


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
        if game_active == -1:
            if event.type == pygame.KEYDOWN and pygame.K_RETURN:
                game_active = 1
        if game_active == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -23
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -23
        #if game gets over
        elif game_active == 2:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = -1
                snail_rect.left = 700
                start_time = int(pygame.time.get_ticks()/1000)

    if game_active == 1:
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
        #Collision
        if snail_rect.colliderect(player_rect) == 1:
            game_active = 2
            score += score
        
    elif game_active == -1:
        screen.fill('Black')
        screen.blit(player_stand, player_stand_rect)
        screen.blit(welcome_1, welcome_1_rect)
        screen.blit(welcome_2, welcome_2_rect)
    else:
        screen.fill('Black')
        screen.blit(game_over, game_over_rect)
        screen.blit(leaderboard, leaderboard_rect)
        player_score = font1.render(f'Your score: {current_time}', False, 'White')
        player_score_rect = player_score.get_rect(center = (400, 350))
        screen.blit(player_score, player_score_rect)


    '''keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('jump')'''

    # update everything
    pygame.display.update() # updates everything happening in the loop to display
    #clock.tick(60) # telling the while loop it should not run more than 60 times/second
    '''if current_time<= 10:
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
        clock.tick(240)'''

