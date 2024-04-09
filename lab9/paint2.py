import pygame
import sys
import pygame.draw
import pygame.freetype
import math
pygame.init()

screen_width, screen_height = 900, 700
screen = pygame.display.set_mode((screen_width, screen_height))

brush_size =5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
current_color = BLACK
colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (143, 0, 255), (255, 255, 255), (128, 128, 128),(0, 0, 0) ]  # List of colors

font_size = 20
font = pygame.freetype.SysFont("Verdana", font_size)

tool = None
drawing = False  

def draw_text(text, position, color):
    font.render_to(screen, position, text, color)

screen.fill(WHITE)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = 'rectangle'
            elif event.key == pygame.K_c:
                tool = 'circle'
            elif event.key == pygame.K_e:
                tool = 'eraser'
            elif event.key == pygame.K_b:
                tool = 'brush'
            elif event.key == pygame.K_s:
                tool = 'square'
            elif event.key == pygame.K_p:
                tool = 'rigtr'
            elif event.key == pygame.K_q:
                tool = 'equtr'
            elif event.key == pygame.K_h:
                tool = 'rhombus'
            elif event.key == pygame.K_UP:  # Increase brush size
                brush_size = min(brush_size + 1, 50)
            elif event.key == pygame.K_DOWN:  # Decrease brush size
                brush_size = max(1, brush_size - 1)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos# where start
                if tool in ['rectangle', 'circle','square','rigtr','equtr','rhombus']:
                    shape_start = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                # For switching color when cursor click on palette
                for i, col in enumerate(colors):
                        if pygame.Rect(screen.get_width() - 70, i * 70, 70, 70).collidepoint(event.pos):
                            current_color = col
                            break
                #draw rect or circle when mousebutton up
                if tool == 'rectangle':
                    pygame.draw.rect(screen, current_color, pygame.Rect(shape_start, (event.pos[0] - shape_start[0], event.pos[1] - shape_start[1])),4)
                elif tool == 'circle':
                    radius = int(((event.pos[0] - shape_start[0]) ** 2 + (event.pos[1] - shape_start[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, shape_start, radius)
                elif tool == 'square':
                    pygame.draw.rect(screen, current_color, pygame.Rect(shape_start, (event.pos[0] - shape_start[0], event.pos[0] - shape_start[0])),4)
                elif tool == 'rigtr':
                    points = [(shape_start[0], event.pos[1]), (event.pos[0], shape_start[1]), (shape_start[0], shape_start[1])]
                    pygame.draw.polygon(screen, current_color, points, 4)
                elif tool == 'equtr':
                        #радиус равнтреуг по началу и концу клика
                    radius = math.sqrt((event.pos[0] - shape_start[0]) ** 2 + (event.pos[1] - shape_start[1]) ** 2)
                    #коорды вершин равн треуг
                    x1 = shape_start[0] #начало клик по х
                    y1 = shape_start[1] #начало клик по у
                    x2 = x1 + radius #сдвигаем на радиус вправо это 2 вершина
                    y2 = y1          #остается на том же уровне
                    x3 = x1 + (radius / 2)  #сдвигаем на радиус/2 вправо это 3 вершина
                    y3 = y1 - (math.sqrt(3) * (radius / 2))  #сдвигаем вверх тоже 3 вершина

                    points = [(x1, y1), (x2, y2), (x3, y3)]
                    pygame.draw.polygon(screen, current_color, points, 4)
                elif tool == 'rhombus':
                    #центр ромба == середина по х и по у
                    center_x, center_y = (shape_start[0] + event.pos[0]) // 2, (shape_start[1] + event.pos[1]) // 2
                    #длина половины стороны ромба == расстоянию от центра до начало клик
                    half_side_length = abs(center_x - shape_start[0])
                    #вершины ромба
                    vertices = [
                        (center_x, center_y - half_side_length),
                        (center_x + half_side_length, center_y),
                        (center_x, center_y + half_side_length),
                        (center_x - half_side_length, center_y)
                    ]
                    pygame.draw.polygon(screen, current_color, vertices, 4)
                
                pygame.display.flip()
        
        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == 'eraser':
                pygame.draw.rect(screen, WHITE, pygame.Rect(event.pos[0], event.pos[1], 10, 10))
                pygame.display.flip()
                
    # Draw color selection palette
        for i, col in enumerate(colors):
            pygame.draw.rect(screen, col, pygame.Rect(screen.get_width() - 70, i * 70, 70, 70))
    draw_text("To draw rectangle-R; to draw circle-С; to draw-B; to erase-E, to draw square-S,", (10, 20), BLACK)
    draw_text("to draw rig triangle-P, to draw equil triangle-Q, to draw rhombus-H.", (10, 38), BLACK)

    if drawing and tool == 'brush':
        pygame.draw.circle(screen, current_color, event.pos, brush_size)
        pygame.display.flip()