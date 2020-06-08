import pygame

# This is my size screen
pygame.init()
screen = pygame.display.set_mode((600, 400))

# loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False