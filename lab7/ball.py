import pygame

pygame.init()

widthscr = 800
heightscr = 600
screen = pygame.display.set_mode((widthscr,heightscr))


WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_radius = 25
ball_x = widthscr // 2
ball_y = heightscr // 2
ball_speed = 20

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                ball_x += ball_speed
    
    ball_x = max(ball_radius, min(widthscr - ball_radius, ball_x))
    ball_y = max(ball_radius, min(heightscr - ball_radius, ball_y))
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()

