import pygame
from sys import exit

pygame.init()


clock = pygame.time.Clock
FPS = 70

win = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Tropic Tussle")
clock = pygame.time.Clock()
test_font = pygame.font.Font("images/font/Pixeltype.ttf", 24)
game_active = True
start_time = 0

#define game variable
counter = 0
start_game = False
score = 0
high_score = 0

#images
sky_surface = pygame.image.load("images/background/sky1.jpg")

ground_surface = pygame.image.load("images/background/ground.png")

bird_surface = pygame.image.load("images/obstacles/Fly2.png").convert_alpha()
bird_rect = bird_surface.get_rect(bottomright = (1000, 270))

tree_surface = pygame.image.load("images/obstacles/small tree.png").convert_alpha()
tree_rect = tree_surface.get_rect(bottomleft = (1500, 300))

spikes_surface = pygame.image.load("images/obstacles/small.png").convert_alpha()
spikes_rect = spikes_surface.get_rect(bottomleft = (470, 300))

shell_surface = pygame.image.load("images/obstacles/shell.png").convert_alpha()
shell_rect = shell_surface.get_rect(bottomleft = (1900, 300))


player_surface = pygame.image.load("images/R9.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (85, 300))
player_gravity = 0

number_image = pygame.image.load("images/numbers.png")
number_image = pygame.transform.scale(number_image, (200, 12))


#music
music = pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play(-1)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -13 

 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: player_rect.bottom >= 0 
            player_gravity = -13 

        if counter % 5 == 0:
            score += 1

    win.blit(sky_surface, (0, 0))
    win.blit(ground_surface, (0, 300))
    win.blit(number_image, (-0, -20))

    bird_rect.x -= 3
    if bird_rect.right <=0 : bird_rect.left = 1778
    win.blit(bird_surface, bird_rect)
    
    tree_rect.x -= 3
    if tree_rect.right <= 0: tree_rect.left = 1790
    win.blit(tree_surface, tree_rect)

    spikes_rect.x -= 2
    if spikes_rect.right <= 0: spikes_rect.left = 1765
    win.blit(spikes_surface, spikes_rect)

    shell_rect.x -= 3
    if shell_rect.right <= 0: shell_rect.left = 1800
    win.blit(shell_surface, shell_rect)   

    player_rect.x += 2
    if player_rect.left >= 0: player_rect.right = 300
    win.blit(player_surface, player_rect)
                 
    string_score = str(score).zfill(5)
    for i, num in enumerate(string_score):
        win.blit(number_image, (520+11*i, 10), (10*int(num), 0, 10, 12))

    
            

    #player    
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300: player_rect.bottom = 300
    win.blit(player_surface, player_rect)

    #collision 
    if bird_rect.colliderect(player_rect):
        pygame.quit()
        exit()
    if shell_rect.colliderect(player_rect):
        pygame.quit()
        exit()
    if tree_rect.colliderect(player_rect):
        pygame.quit()
        exit()
    if spikes_rect.colliderect(player_rect):
        pygame.quit()
        exit()        



    pygame.display.update()
    clock.tick(60) 
