import pygame
from pygame.locals import *
import sys
import random

colors = {'white': (255,255,255), 'black': (0,0,0)}
WIDTH = 1310
HEIGHT = 600
LIST_SIZE = 50
FPS = 60

def draw_lines(l: list[int], screen: pygame.Surface, font: pygame.font) -> None:
    s = 13
    for n in range(len(l)):
        pygame.draw.line(screen, colors['black'], ((WIDTH/2)*.5+s, HEIGHT), ((WIDTH/2)*.5+s, (HEIGHT-l[n]*5)), width=10)
        s+=13
        text_list = font.render(f"Array = {str(l)}", True, colors['black'], colors['white'])
        screen.blit(text_list, (50, 100))


def sort(l: list[int], screen: pygame.Surface, clock: pygame.time.Clock, font: pygame.font) -> None:
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                aux = l[j]
                l[j] = l[j+1]
                l[j+1] = aux
                screen.fill(colors['white'])
                draw_lines(l=l, screen=screen, font=font)
                clock.tick(FPS)
                pygame.display.flip()


def generate_random_list(size: int=100, zero: bool=False, unique: bool=True) -> list[int]:
    l = []
    while len(l) < size:
        if zero:
            n = random.randint(0, size)
        else:
            n = random.randint(1, size)
        if unique:
            if n in l:
                continue
            else:
                l.append(n)
        else:
            l.append(n)

    return l


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bubble Sort Visualisation")
    clock = pygame.time.Clock()
    is_paused = False
    pygame.font.init()
    font_space = pygame.font.Font('freesansbold.ttf', 32)
    text = font_space.render('Press SPACE to load a new random array.', True, colors['black'], colors['white'])
    font_list = pygame.font.Font('freesansbold.ttf', 15)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    is_paused = False

            if is_paused == False:
                random_list = generate_random_list(size=LIST_SIZE)
                sort(random_list, screen, clock=clock, font=font_list)
                draw_lines(l=random_list, screen=screen, font=font_list)
            is_paused = True
            screen.blit(text, ((WIDTH/2)*.5, HEIGHT/4))
            
        pygame.display.flip()
if __name__ == '__main__':
    main()
