import pygame, sys
from game_functions import draw_base, create_pipe, move_pipes, draw_pipes, check_collision, rotate_bird

pygame.init()


screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('pic/background-day.png').convert()
# Convert makes picture better for pygame using
bg_surface = pygame.transform.scale2x(bg_surface)

base_surface_1 = pygame.image.load('pic/base.png').convert()
base_surface_1 = pygame.transform.scale2x(base_surface_1)
base_surface_start_1 = 0

bird_surface = pygame.image.load('pic/yellowbird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect()
bird_rect.centerx = 288
bird_rect.centery = 512

gravity = 1
bird_movement = 0


pipe_surface = pygame.image.load('pic/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
PIPESPAWN = pygame.USEREVENT
pygame.time.set_timer(PIPESPAWN, 1900)
pipes_height = [390, 430, 510, 550, 700]


game_active = True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 15
            elif event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                bird_movement = 0
                pipe_list.clear()
                bird_rect.centerx = 288
                bird_rect.centery = 512
        elif event.type == PIPESPAWN:
            pipe_list.extend(create_pipe(pipe_surface, pipes_height))

    screen.blit(bg_surface, (0, 0))

    if game_active:
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list, screen, pipe_surface)

        if base_surface_start_1 < -576:
            base_surface_start_1 = 0
            draw_base(screen, base_surface_1, base_surface_start_1)
        else:
            base_surface_start_1 -= 3
            draw_base(screen, base_surface_1, base_surface_start_1)

        bird_movement += gravity
        rotated_birt = rotate_bird(bird_surface, bird_movement)
        bird_rect.centery += bird_movement

        screen.blit(rotated_birt, bird_rect)

    game_active = check_collision(bird_rect, pipe_list)

    pygame.display.flip()
    clock.tick(50)
