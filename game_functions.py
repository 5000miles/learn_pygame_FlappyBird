import random, pygame

def draw_base(screen, base_surface_1, base_surface_start_1):
    screen.blit(base_surface_1, (base_surface_start_1, 800))
    screen.blit(base_surface_1, (base_surface_start_1 + 672, 800))


def create_pipe(pipe_surface, pipes_heights):
    random_height = random.choice(pipes_heights)
    bottom_pipe = pipe_surface.get_rect(midtop=(576, random_height))
    top_pipe = pipe_surface.get_rect(midbottom=(576, random_height - 300))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes_list, screen, pipe_surface):
    for pipe in pipes_list:
        if pipe.top < 0:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
        else:
            screen.blit(pipe_surface, pipe)


def check_collision(bird_rect, pipes_list):
    for pipe in pipes_list:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= 1024:
        return False
    else:
        return True


def rotate_bird(bird, bird_movement):
    new_bird = pygame.transform.rotozoom(bird, bird_movement, 1)
    return new_bird