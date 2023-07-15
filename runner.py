import pygame
from sys import exit
from random import randint


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

player_walk1 = pygame.image.load('graphics/Player/walk1.png').convert_alpha()
player_walk2 = pygame.image.load('graphics/Player/walk2.png').convert_alpha()
player_walk = [player_walk1, player_walk2]
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
player_index = 0

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))


player_stand = pygame.image.load('graphics/Player/stand.png')
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

player_gravity = 0

#Obstacles

snail_frame1 = pygame.image.load('graphics/Snail/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('graphics/Snail/snail2.png').convert_alpha()
snail_frames = [snail_frame1, snail_frame1]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

fly_frame1 = pygame.image.load('graphics/Fly/Fly3.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics/Fly/Fly4.png').convert_alpha()
fly_frame1 = pygame.transform.scale(fly_frame1, (100, 50))
fly_frame2 = pygame.transform.scale(fly_frame2, (100, 50))
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

def obstacle_movement(obstacle_list):
    if obstacle_list != []:
        for i in obstacle_list:
            i.x -= 5
            
            if i.bottom == 300:
                screen.blit(snail_surf, i)
            else:
                screen.blit(fly_surf, i)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

'''def collisions(player, obstacles):
    if obstacles:
        for j in obstacles:
            if player.colliderect(j):
                return 2
    return 1'''


welcome_1 = font2.render("Hi! I'm the Pixel Runner", False, 'Yellow')
welcome_1_rect = welcome_1.get_rect(center = (400, 50))

welcome_2 = font1.render("PRESS 'ENTER' to start the game", True, 'White')
welcome_2_rect = welcome_2.get_rect(center = (400, 90) )

game_over = font2.render('Game over', False, 'Red')
game_over_rect = game_over.get_rect(center =(400, 50))

leaderboard = font1.render('LEADERBOARD', False, 'Yellow')
leaderboard_rect = leaderboard.get_rect(center = (400, 90))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
                start_time = int(pygame.time.get_ticks()/1000)
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
        if event.type == obstacle_timer and game_active == 1:
            if randint(0, 2) == 1:
                obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900, 1100) ,300)))
            else:
                obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900, 1100) ,210)))
            
        if event.type == snail_animation_timer:
            if snail_frame_index == 0:
                snail_frame_index = 1
            else:
                snail_frame_index = 0
            snail_surf = snail_frames[snail_frame_index]

        if event.type == fly_animation_timer:
            if fly_frame_index == 0:
                fly_frame_index = 1
            else:
                fly_frame_index = 0
            fly_surf = fly_frames[fly_frame_index]

    if game_active == -1:
        screen.fill('Black')
        screen.blit(player_stand, player_stand_rect)
        screen.blit(welcome_1, welcome_1_rect)
        screen.blit(welcome_2, welcome_2_rect)

    elif game_active == 1:
        screen.blit(ground_surface, (0,300)) # telling the system we want to place a ground on display surface
        screen.blit(sky_surface, (0,0)) # telling the system we want to place a sky on display surface
        current_time = int(pygame.time.get_ticks() / 1000) - start_time
        game_time = current_time
        score_surf = font1.render(f'SCORE: {current_time}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(400, 50))
        screen.blit(score_surf, score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surf, score_rect)
        #screen.blit(by_surf, by_rect)
        #Player
        #Gravity
        player_gravity+=1 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        #player animation
        if player_rect.bottom < 300:
            player_surf = player_jump
        else:
            player_index += 0.1
            if player_index >= len(player_walk):
                player_index = 0
            player_surf = player_walk[int(player_index)]

        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        for j in obstacle_rect_list:
                if player_rect.colliderect(j):
                    game_active = 2 

        #screen.blit(snail_surf, snail_rect)
        '''snail_rect.left -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800'''
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
        '''if snail_rect.colliderect(player_rect) == 1:
            game_active = 2'''

    else:
        screen.fill('Black')
        screen.blit(game_over, game_over_rect)
        screen.blit(leaderboard, leaderboard_rect)
        final_score = game_time
        player_score = font1.render(f'Your score: {final_score}', False, 'White')
        player_score_rect = player_score.get_rect(center=(400, 350))
        screen.blit(player_score, player_score_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0


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

