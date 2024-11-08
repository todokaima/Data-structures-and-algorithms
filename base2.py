import pygame
import sys
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Square Game with Shooting")
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

square_size = 50
square_x, square_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
square_speed = 10

bullet_radius = 5
bullet_speed = 15
bullets = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = square_x + square_size // 2
                bullet_y = square_y
                bullets.append([bullet_x, bullet_y])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed
    if keys[pygame.K_UP]:
        square_y -= square_speed
    if keys[pygame.K_DOWN]:
        square_y += square_speed
    square_x = max(0, min(square_x, SCREEN_WIDTH - square_size))
    square_y = max(0, min(square_y, SCREEN_HEIGHT - square_size))

    for bullet in bullets:
        bullet[1] -= bullet_speed
    bullets = [bullet for bullet in bullets if bullet[1] > 0]
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))
    for bullet in bullets:
        pygame.draw.circle(screen, RED, (bullet[0], bullet[1]), bullet_radius)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
pygame.quit()
sys.exit()