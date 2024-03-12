import pygame, sys

#General Setup
pygame.init()
clock = pygame.time.Clock()

#Setting up the main window
screen = pygame.display.set_mode((1280,960))
pygame.display.set_caption('Pong')

while True:


    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #Updating the window
        pygame.display.flip()
        clock.tick(60)