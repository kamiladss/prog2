import pygame as pg
from pygame.font import Font
import random
import time
pg.init()
WINDOW= 800
TILE_SIZE = 40
RANGE = (TILE_SIZE//2, WINDOW - TILE_SIZE//2,TILE_SIZE)
getrandpos= lambda:[random.randrange(*RANGE),random.randrange(*RANGE)]
snake=pg.rect.Rect([0,0,TILE_SIZE-2, TILE_SIZE-2])
snake.center = getrandpos()
length = 1
segments = [snake.copy()]
snake_dir=(0,0)
time_0, time_step = 0,120
food = snake.copy()
food.center= getrandpos()
screen = pg.display.set_mode([WINDOW]*2)
clock = pg.time.Clock()
dirs={pg.K_UP:1, pg.K_DOWN:1, pg.K_LEFT:1, pg.K_RIGHT:1}
#font and counter for food also level and speed
font = pg.font.SysFont("Verdana", 18)  
food_eaten = 0
level= 1
food_time = time.time()# WHEN food apears

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and dirs[pg.K_UP]:
                snake_dir = (0, -TILE_SIZE)
                dirs={pg.K_UP:1, pg.K_DOWN:0, pg.K_LEFT:1, pg.K_RIGHT:1, }
            if event.key == pg.K_DOWN and dirs[pg.K_DOWN]:
                snake_dir = (0, TILE_SIZE)
                dirs={pg.K_UP:0, pg.K_DOWN:1, pg.K_LEFT:1, pg.K_RIGHT:1, }
            if event.key == pg.K_LEFT and dirs[pg.K_LEFT]:
                snake_dir = (-TILE_SIZE, 0)
                dirs={pg.K_UP:1, pg.K_DOWN:1, pg.K_LEFT:1, pg.K_RIGHT:0, }
            if event.key == pg.K_RIGHT and dirs[pg.K_RIGHT]:
                snake_dir = (TILE_SIZE, 0)
                dirs={pg.K_UP:1, pg.K_DOWN:1, pg.K_LEFT:0, pg.K_RIGHT:1, }
    screen.fill('black')
    #check borders and selfeating
    selfeat=pg.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or selfeat:
            snake.center,food.center = getrandpos(), getrandpos()
            length, snake_dir = 1, (0,0)
            segments=[snake.copy()]
            food_eaten = 0
            level = 1
            time_step = 120
    # IF FOOD WERENT EATEN FOR 3 SECS CHOOSE NEW ONE
    if time.time() - food_time > 3:
        food.center = getrandpos()
        food_weight = random.choice([1,2,3,4])
        food_time = time.time()
    #check food
    if snake.center == food.center:
        food.center = getrandpos()
        length += 1
        #adding points to score
        food_weight = random.choice([1,2,3,4])
        food_eaten +=food_weight
        
    
        #level up with increasing speed each 3 points
        if food_eaten % 3 == 0:
            level+=1
            time_step =time_step - 8
    #draw food
    pg.draw.rect(screen, 'red', food)
    # draw snake
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    # move snake
    time_now = pg.time.get_ticks() 
    if time_now - time_0 > time_step:
        time_0 = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    #output of score
    text_surf = font.render(f"Eaten: {food_eaten}", True, pg.Color('white'))
    screen.blit(text_surf, (10, 10))
    
    text_level = font.render(f"Level: {level}", True, pg.Color('white'))
    screen.blit(text_level, (WINDOW - text_level.get_width() - 10, 10))
    
    pg.display.flip()
    clock.tick(60)