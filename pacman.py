import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
PACMAN_SIZE = 20
PACMAN_SPEED = 5
PELLET_SIZE = 10
WALL_WIDTH = 20

# Set up some colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the player
pacman_x = WIDTH / 2
pacman_y = HEIGHT / 2
pacman_speed_x = 0
pacman_speed_y = 0

# Set up the pellets
pellets = []
for _ in range(100):
    pellets.append([random.randint(0, WIDTH - PELLET_SIZE), random.randint(0, HEIGHT - PELLET_SIZE)])

# Set up the walls
walls = [
    # Top wall
    pygame.Rect(0, 0, WIDTH, WALL_WIDTH),
    # Bottom wall
    pygame.Rect(0, HEIGHT - WALL_WIDTH, WIDTH, WALL_WIDTH),
    # Left wall
    pygame.Rect(0, 0, WALL_WIDTH, HEIGHT),
    # Right wall
    pygame.Rect(WIDTH - WALL_WIDTH, 0, WALL_WIDTH, HEIGHT),
    # Middle wall
    pygame.Rect(WIDTH / 2 - WALL_WIDTH / 2, HEIGHT / 2 - WALL_WIDTH / 2, WALL_WIDTH, HEIGHT / 2),
    # Additional walls to create a maze
    pygame.Rect(WIDTH / 4, HEIGHT / 4, WALL_WIDTH, HEIGHT / 2),
    pygame.Rect(WIDTH / 2, HEIGHT / 4, WALL_WIDTH, HEIGHT / 2),
    pygame.Rect(3 * WIDTH / 4, HEIGHT / 4, WALL_WIDTH, HEIGHT / 2),
    pygame.Rect(WIDTH / 4, 3 * HEIGHT / 4, WALL_WIDTH, HEIGHT / 2),
    pygame.Rect(WIDTH / 2, 3 * HEIGHT / 4, WALL_WIDTH, HEIGHT / 2),
    pygame.Rect(3 * WIDTH / 4, 3 * HEIGHT / 4, WALL_WIDTH, HEIGHT / 2),
]

# Set up the score
score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman_speed_x = 0
                pacman_speed_y = -PACMAN_SPEED
            elif event.key == pygame.K_DOWN:
                pacman_speed_x = 0
                pacman_speed_y = PACMAN_SPEED
            elif event.key == pygame.K_LEFT:
                pacman_speed_x = -PACMAN_SPEED
                pacman_speed_y = 0
            elif event.key == pygame.K_RIGHT:
                pacman_speed_x = PACMAN_SPEED
                pacman_speed_y = 0

    # Move the player
    pacman_x += pacman_speed_x
    pacman_y += pacman_speed_y

    # Keep the player on the screen and away from walls
    for wall in walls:
        if wall.colliderect(pygame.Rect(pacman_x, pacman_y, PACMAN_SIZE, PACMAN_SIZE)):
            pacman_x -= pacman_speed_x
            pacman_y -= pacman_speed_y
            break

    # Check for collisions with pellets
    for pellet in pellets:
        if (pacman_x <= pellet[0] + PELLET_SIZE and
            pacman_x + PACMAN_SIZE >= pellet[0] and
            pacman_y <= pellet[1] + PELLET_SIZE and
            pacman_y + PACMAN_SIZE >= pellet[1]):
            pellets.remove(pellet)
            score += 1

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, YELLOW, (pacman_x, pacman_y, PACMAN_SIZE, PACMAN_SIZE))
    for pellet in pellets:
        pygame.draw.rect(screen, WHITE, (pellet[0], pellet[1], PELLET_SIZE, PELLET_SIZE))
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)
