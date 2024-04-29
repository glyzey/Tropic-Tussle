import pygame
import random

pygame.init()

screen_width = 800
screen_height = 400
win = pygame.display.set_mode(screen_width, screen_height, pygame.NOFRAME)

clock = pygame.time.Clock()
FPS = 60

#colors
white = ((255, 255, 255))
black = ((0, 0, 0))
gray = ((32, 33, 36))

#image

game_over_image = pygame.image.load("images/GameOver.")
game_over_image = pygame.transform.scale(game_over_image, (200, 60))

replay_image = pygame.image.load("images/")
replay_image = pygame.transform.scale(replay_image, (40, 36))
replay_rect = replay_image.get_rect()
replay_image.x = screen_width // 2 - 20
replay_image.y = 100









