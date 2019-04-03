import sys, pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((0,0,0))
pygame.display.flip

white = (255,255,255)

def ROUND(n):
    return int(n+0.5)

def dda (x1,y1,x2,y2):
    x,y = x1,y1
    lenght = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
    dx = (x2-x1)/float(lenght)
    dy = (y2-y1)/float(lenght)
    screen.set_at((ROUND(x), ROUND(y)),white)

    for i in range(lenght):
        x += dx
        y += dy
        screen.set_at((ROUND(x), ROUND(y)),white)
        pygame.display.flip()
        
dda(100,100,100,500)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
