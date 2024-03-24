import pygame
import os
pygame.init()


SCREEN_WIDTH = 200
SCREEN_HEIGHT = 150
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

music_dir = "C:\\Users\\LENOVO\\Desktop\\kamilaproga\\music"
songs = [file for file in os.listdir(music_dir) if file.endswith(".mp3")]
current_song_index = 0

pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
joystick_up_img = pygame.image.load("prev.png")
joystick_down_img = pygame.image.load("next.png")
joystick_left_img = pygame.image.load("stop.png")
joystick_right_img = pygame.image.load("play.png")

joystick_up_rect = joystick_up_img.get_rect(center=(50, SCREEN_HEIGHT - 50))
joystick_down_rect = joystick_down_img.get_rect(center=(150, SCREEN_HEIGHT - 50))
joystick_left_rect = joystick_left_img.get_rect(center=(100, SCREEN_HEIGHT - 100))
joystick_right_rect = joystick_right_img.get_rect(center=(100, SCREEN_HEIGHT - 50))

current_song_position = 0  

def play():
    global current_song_position
    pygame.mixer.music.play(start=current_song_position)
def stop():
    global current_song_position
    pygame.mixer.music.stop()
    current_song_position = pygame.mixer.music.get_pos() / 1000

def nexts():
    global current_song_index, current_song_position
    current_song_index = (current_song_index + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
    current_song_position = 0
    play()
def prev():
    global current_song_index, current_song_position
    current_song_index = (current_song_index - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
    current_song_position = 0
    play()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop()
                else:
                    play()
            elif event.key == pygame.K_RIGHT:
                nexts()
            elif event.key == pygame.K_LEFT:
                prev()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if joystick_up_rect.collidepoint(event.pos):
                prev()
            elif joystick_down_rect.collidepoint(event.pos):
                nexts()
            elif joystick_left_rect.collidepoint(event.pos):
                stop()
            elif joystick_right_rect.collidepoint(event.pos):
                play()


    screen.blit(joystick_up_img, joystick_up_rect)
    screen.blit(joystick_down_img, joystick_down_rect)
    screen.blit(joystick_left_img, joystick_left_rect)
    screen.blit(joystick_right_img, joystick_right_rect)

    pygame.display.flip()
    screen.fill(color=(255, 255, 255))

pygame.quit()