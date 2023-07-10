#CREATING A BLANK WINDOW
import pygame
from sys import exit

pygame.init() #Initiates pygame
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner') #Naming the title of the window
clock = pygame.time.Clock()

while True:
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #ends the while True loop so that it cannot continue to update and throw an error
    # draw all our elements
    # update everything
    pygame.display.update() # updates everything happening in the loop to display
    clock.tick(60) # telling the while loop it should not run more than 60 times/second
