import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

win_width = 900
win_height = 500

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("scrolling ground")

#define game variable
ground_scroll = 0
scroll_speed = 4

#load images
background = pygame.image.load("images/background/sky5.jpg")
ground = pygame.image.load("images/background/ground (1).png")

run = True
while run:

    clock.tick(FPS)
    #draw background
    win.blit(background, (0, -133))



    #draw scrolling ground
    win.blit(ground, (ground_scroll, 340))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            pygame.quit()
