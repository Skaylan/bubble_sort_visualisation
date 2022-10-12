import pygame
from pygame.locals import *
import sys
import random

colors = {'white': (255,255,255), 'black': (0,0,0)}
WIDTH = 1310
HEIGHT = 600
FPS = 60

def draw_lines(l: list[int], screen: pygame.Surface) -> None:
    s = 13
    for n in l:
        pygame.draw.line(screen, colors['black'], (s, HEIGHT), (s, (HEIGHT-l[n-1]*5)), width=10)
        s+=13


def sort(l: list[int], screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                aux = l[j]
                l[j] = l[j+1]
                l[j+1] = aux
                screen.fill(colors['white'])
                draw_lines(l=l, screen=screen)
                clock.tick(FPS)
                pygame.display.flip()


def generate_random_list(size: int=100, zero: bool=False) -> list[int]:
    l = []
    while len(l) < size:
        if zero:
            n = random.randint(0, size)
        else:
            n = random.randint(1, size)
        if n in l:
            continue
        else:
            l.append(n)
    return l


lista = generate_random_list(size=50)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    is_paused = False

    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    is_paused = False
                    lista = generate_random_list(size=50)
                    print(lista)
                    screen.fill(colors['white'])

                    if is_paused == False:
                        screen.fill(colors['white'])
                        sort(lista, screen, clock=clock)
                        screen.fill(colors['white'])
                        draw_lines(l=lista, screen=screen)
                        is_paused = True


        pygame.display.flip()
if __name__ == '__main__':
    main()
