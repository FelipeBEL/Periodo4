import sys, pygame
from pygame import gfxdraw

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

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((0,0,0))
pygame.display.flip

white = (255,255,255)
    
event = pygame.event.wait()

xy1 = []
xy2 = []

while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # prints on the console the pressed button and its position at that moment
            print u'button {} pressed in the position {}'.format(event.button, event.pos)
            xy1 = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            # prints on the console the button released and its position at that moment
            print u'button {} released in the position {}'.format(event.button, event.pos)
            xy2 = event.pos
            dda(xy1[0],xy1[1],xy2[0],xy2[1])

        if event.type == pygame.QUIT: sys.exit()