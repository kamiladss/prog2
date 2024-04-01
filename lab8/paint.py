import pygame
import sys
import pygame.draw
import pygame.freetype

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
            elif event.key == pygame.K_UP:  # Increase brush size
                brush_size = min(brush_size + 1, 50)
            elif event.key == pygame.K_DOWN:  # Decrease brush size
                brush_size = max(1, brush_size - 1)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos# where start
                if tool in ['rectangle', 'circle']:
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
                    pygame.draw.rect(screen, current_color, pygame.Rect(shape_start, (event.pos[0] - shape_start[0], event.pos[1] - shape_start[1])))
                elif tool == 'circle':
                    radius = int(((event.pos[0] - shape_start[0]) ** 2 + (event.pos[1] - shape_start[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, shape_start, radius)
                pygame.display.flip()
        
        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == 'eraser':
                pygame.draw.rect(screen, WHITE, pygame.Rect(event.pos[0], event.pos[1], 10, 10))
                pygame.display.flip()
                
    # Draw color selection palette
        for i, col in enumerate(colors):
            pygame.draw.rect(screen, col, pygame.Rect(screen.get_width() - 70, i * 70, 70, 70))
    draw_text("To draw rectangle - R; to draw circle - R; to draw - B; to erase - E.", (10, 40), BLACK)


    if drawing and tool == 'brush':
        pygame.draw.circle(screen, current_color, event.pos, brush_size)
        pygame.display.flip()