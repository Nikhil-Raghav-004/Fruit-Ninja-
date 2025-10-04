import pygame


pygame.init()

width = 1000
height = 700

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame basics")



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    pygame.display.flip()