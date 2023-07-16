import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk1 = pygame.image.load('graphics/Player/walk1.png').convert_alpha()
        player_walk2 = pygame.image.load('graphics/Player/walk2.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mpeg')
        self.jump_sound.set_volume(0.4)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -23
            self.jump_sound.play()
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity 
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

#Obstacle Class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'fly':
            fly_frame1 = pygame.image.load('graphics/Fly/Fly3.png').convert_alpha()
            fly_frame2 = pygame.image.load('graphics/Fly/Fly4.png').convert_alpha()
            fly_frame1 = pygame.transform.scale(fly_frame1, (100, 50))
            fly_frame2 = pygame.transform.scale(fly_frame2, (100, 50))
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210
        else:
            snail_frame1 = pygame.image.load('graphics/Snail/snail1.png').convert_alpha()
            snail_frame2 = pygame.image.load('graphics/Snail/snail2.png').convert_alpha()
            self.frames = [snail_frame1, snail_frame1]
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom =(randint (900, 1100), y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]


    def update(self): 
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

#Inducing collisions
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False) == 1:
        return 2
    else:
        return 1

pygame.init()

#Setting the display screen, clock, and fonts
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption("Text Input")
pygame.display.set_caption('Runner') #Naming the title of the window
clock = pygame.time.Clock()
font1 = pygame.font.Font('font/Pixeltype.ttf', 50)
font2 = pygame.font.Font('font/Pixeltype.ttf', 70)
font3 = pygame.font.Font('font/Pixeltype.ttf', 25)

game_active = -1 
start_time = 0
score = 0

background_music = pygame.mixer.Sound('audio/game_music.mp3')
background_music.play(loops = -1)

sky_surface = pygame.image.load('graphics/Sky.jpeg').convert()
ground_surface = pygame.image.load('graphics/Ground.jpeg').convert()

# Setting up sprite Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

#Initializing Player variables

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

#Initializing obstacle variables

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

#Setting up display text
welcome_1 = font2.render("Hi! I'm the Pixel Runner", False, 'Yellow')
welcome_1_rect = welcome_1.get_rect(center = (400, 50))

welcome_2 = font1.render("Press 'ENTER' to start the game", True, 'White')
welcome_2_rect = welcome_2.get_rect(center = (400, 90) )

welcome_3 = font1.render("Press 'SPACE' to jump the obstacles", True, 'White')
welcome_3_rect = welcome_2.get_rect(center = (400, 350) )

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

text = ' '.capitalize()

while True:
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #ends the while True loop so that it cannot continue to update and throw an error
        if game_active == -1:
            '''if event.type == pygame.TEXTINPUT:
                text += event.text'''
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
            obstacle_group.add(Obstacle(choice(['fly', 'snail' , 'snail', 'snail'])))
            
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
        text_input = font2.render(text, True, 'White')
        screen.blit(text_input, (330, 300))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(welcome_1, welcome_1_rect)
        screen.blit(welcome_2, welcome_2_rect)
        screen.blit(welcome_3, welcome_3_rect)

    elif game_active == 1:
        screen.blit(ground_surface, (0,300)) # telling the system we want to place a ground on display surface
        screen.blit(sky_surface, (0,0)) # telling the system we want to place a sky on display surface
        current_time = int(pygame.time.get_ticks() / 1000) - start_time
        game_time = current_time
        score_surf = font1.render(f'SCORE: {current_time}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(400, 50))
        screen.blit(score_surf, score_rect)

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        #player animation
        if player_rect.bottom < 300:
            player_surf = player_jump
        else:
            player_index += 0.1
            if player_index >= len(player_walk):
                player_index = 0
            player_surf = player_walk[int(player_index)]

        #Obstacle movement
        if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
            obstacle_group.empty()
            game_active = 2
        else:
            game_active = 1

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

    else:
        screen.fill('Black')
        screen.blit(game_over, game_over_rect)
        screen.blit(leaderboard, leaderboard_rect)
        final_score = game_time
        player_score = font1.render(f'Your score: {final_score}', False, 'White')
        player_score_rect = player_score.get_rect(center=(400, 350))
        leaderboard = font3.render(f'{players}         {final_score}', False, 'Yellow')
        leaderboard_rect = leaderboard.get_rect(center = (400, 90))
        screen.blit(leaderboard, leaderboard_rect)
        screen.blit(player_score, player_score_rect)
        player_rect.midbottom = (80, 300)
        player_gravity = 0

    # update everything
    pygame.display.update() # updates everything happening in the loop to display

