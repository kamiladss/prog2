import pygame 
from datetime import datetime 

pygame.init()
screen = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()

# loading the images 
bg_surf = pygame.image.load("main-clock.png")
leftarm_surf = pygame.image.load("left-hand.png")
rightarm_surf = pygame.image.load("right-hand.png")

# Уменьшаем размер стрелок в два раза
leftarm_surf = pygame.transform.scale(leftarm_surf, (leftarm_surf.get_width() , leftarm_surf.get_height() ))
rightarm_surf = pygame.transform.scale(rightarm_surf, (rightarm_surf.get_width() , rightarm_surf.get_height() ))

bg_rect = bg_surf.get_rect(center=(400, 400))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.now().time()

    seconds_angle = -(current_time.second * 6)-270
    minutes_angle = -(current_time.minute * 6)-270

    rotated_leftarm = pygame.transform.rotate(leftarm_surf, seconds_angle)
    rotated_rightarm = pygame.transform.rotate(rightarm_surf, minutes_angle)

    leftarm_rect = rotated_leftarm.get_rect(center=bg_rect.center)
    rightarm_rect = rotated_rightarm.get_rect(center=bg_rect.center)

    screen.blit(bg_surf, bg_rect)
    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    pygame.display.flip()
    clock.tick(60)
