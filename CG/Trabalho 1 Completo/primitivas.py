import sys, pygame,numpy
import math

def floodfill(x,y,nova_cor,cor_fundo):
    pilha = [(x,y)]                                 # Inicializa a pilha com o (x,y) inicial

    if screen.get_at((x,y)) == nova_cor:
        return

    while len(pilha)>0:
        x,y = pilha.pop()                           # Enquanto ainda tiver elementos na pilha, desempilhe cada (x,y)

        if screen.get_at((x,y)) != cor_fundo:       # Se a cor do pixel (x,y) for diferente da cor de fundo passada por parametro continue 
            continue

        screen.set_at((x,y),nova_cor)               # Pinta o pixel atual
        
        # Aqui é o processo em que cada pixel de todas as direcoes vao sendo empilhados e desempilhados da pilha e nesse
        # processo verifica-se (a partir do if acima) se aquele pixel deve ou nao ser pintado
        if((x+1)<=1049):
            pilha.append((x+1,y))
        if((x-1)>= 0):
            pilha.append((x-1,y))
        if((y+1)<=799):
            pilha.append((x,y+1))
        if((y-1)>=0):
            pilha.append((x,y-1))


# O algoritmo de Breseham foi adaptado em tres funcoes (abaixo) para conseguir desenhar a linha em todas as direcoes

def linhaH(x0, y0, x1, y1, cor):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0
    for x in range(dx):
        
        screen.set_at((x + x0, y), cor)
        
       
        if D > 0:
            y = y + yi
            D = D - 2*dx
        D = D + 2*dy


def linhaV(x0, y0, x1, y1, cor):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0
    for y in range(dy):
        
        screen.set_at((x, y + y0), cor)
        
        
        if D > 0:
            x = x + xi
            D = D - 2*dy
        D = D + 2*dx


def reta(x0, y0, x1, y1, cor):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            linhaH(x1, y1, x0, y0, cor)
        else:
            linhaH(x0, y0, x1, y1, cor)
    else:
        if y0 > y1:
            linhaV(x1, y1, x0, y0, cor)
        else:
            linhaV(x0, y0, x1, y1, cor)


def linha(x0, y0, x1, y1, cor):
    reta(x0, y0, x1, y1, cor)
    pygame.display.flip()

# Algoritmo de ponto medio foi adaptado para desenhar o circulo a partir o ponto central dado pela posicao do mouse
# e para se tornar regulavel junto do ponteiro do mesmo foi utilizado o calculo da distancia entre dois pontos para
# determinar cada raio
def circulo(x0, y0, r, cor):

    x = 0
    y = r
    d = 1 - r
    circulo_aux (x, y, x0, y0, cor)
    while y > x :
        if d < 0 :
            d = d + ( 2 * x ) + 3
        else:
            d = d + 2 * ( x - y ) + 5
            y = y - 1
        x = x + 1
        circulo_aux(x, y, x0, y0, cor)
    
def distancia(x0,y0,x1,y1):
    a = (x1 - x0)**2
    b = (y1-y0)**2
    raiz = a+b

    raio = int(math.sqrt(raiz))

    return raio

def circulo_aux(x, y, x0, y0, cor):
    
    screen.set_at((x + x0, y + y0), cor)
    screen.set_at((x0 - y, x + y0), cor)
    screen.set_at((x0 - y, y0 - x), cor)
    screen.set_at((x0 - x, y0 - y), cor)
    screen.set_at((x0 - x, y + y0), cor)
    screen.set_at((x + x0, y0 - y), cor)
    screen.set_at((y + x0, y0 - x), cor)
    screen.set_at((y + x0, x + y0), cor)

def retangulo(x, y, w, h, cor):
    reta(x, y, w, y, cor)
    reta(w, y, w, h, cor)
    reta(w, h, x, h, cor)
    reta(x, h, x, y, cor)
    pygame.display.flip()

def quadrado(x, y, w, h, cor):
    reta(x, y, w, y, cor)
    reta(w, y, w, h, cor)
    reta(w, h, x, h, cor)
    reta(x, h, x, y, cor)
    pygame.display.flip()



def bezierIngenuo(p1, p4, cor):
    default = screen.copy()
    while 1:
        for e in pygame.event.get():

            if (e.type == pygame.MOUSEBUTTONDOWN):
                screen.blit(default, (0, 0))
                aux = pygame.mouse.get_pressed()

                if aux[2] == 1: 
                    screen.blit(teste, (0, 0))

                    return
                else:
                    p3 = pygame.mouse.get_pos()
                    for t in numpy.arange(0, 1, 0.0001):
                        omt = 1 - t
                        omt2 = omt * omt
                        omt3 = omt2 * omt
                        t2 = t * t
                        t3 = t2 * t
                        x = omt3 * p1[0] + ((3 * omt2) * t * p1[0]) + (3 * omt * t2 * p3[0]) + t3 * p4[0]
                        y = omt3 * p1[1] + ((3 * omt2) * t * p1[1]) + (3 * omt * t2 * p3[1]) + t3 * p4[1]
                        x = int(numpy.floor(x))
                        y = int(numpy.floor(y))
                        if (x < 1050):
                            screen.set_at((x, y), cor)

                    pygame.display.flip()
                    teste = screen.copy()

# Imprime todas as informacoes basicas da tela
def info_tela():
    

    pygame.draw.rect(screen, slateGrey, (1050, 0, 150, 800))
    pygame.draw.rect(screen, black, (1050, 0, 5, 800))

    # Botao clear
    pygame.draw.rect(screen, white, (1070, 35, 115, 20))
    basicFont = pygame.font.SysFont(None, 15)                       
    text = basicFont.render("CLEAR", True, (0,0,0))
    textRect = text.get_rect()
    textRect.left = screen.get_rect().left + 1110
    textRect.top = screen.get_rect().top + 40
    screen.blit(text, textRect)

    # Botao linha
    pygame.draw.rect(screen, white, (1070, 80, 50, 50))
    linha(1075,85,1115,125,black)

    # Botao polilinha
    pygame.draw.rect(screen, white, (1135, 145, 50, 50))
    linha(1150,150,1140,190,black)
    linha(1150,150,1165,190,black)
    linha(1165,190,1175,150,black)

    # Botao quadrado
    pygame.draw.rect(screen, white, (1135, 80, 50, 50))
    quadrado(1144,88,1175,120,black)

    # Botao retangulo
    pygame.draw.rect(screen, white, (1070, 145, 50, 50))
    retangulo(1074,158,1115,183,black)

    # Botao balde
    pygame.draw.rect(screen, white, (1100, 700, 50, 50))
    screen.blit(balde,(1105,705))

    # botao circulo
    pygame.draw.rect(screen, white, (1070, 210, 50, 50))
    circulo(1095,235,20,black)

    # botao curva
    pygame.draw.rect(screen, white, (1135, 210, 50, 50))
    screen.blit(img_curva,(1138,212))

    # botoes das cores

    pygame.draw.rect(screen, black, (1085, 410, 20, 20))
    pygame.draw.rect(screen, deepSkyBlue, (1105, 410, 20, 20))
    pygame.draw.rect(screen, greenYellow, (1125, 410, 20, 20))
    pygame.draw.rect(screen, orange, (1145, 410, 20, 20))
    
    #2linha de cor
    pygame.draw.rect(screen, magenta, (1085, 430, 20, 20))
    pygame.draw.rect(screen,yellow , (1105, 430, 20, 20))
    pygame.draw.rect(screen,white , (1125, 430, 20, 20))
    pygame.draw.rect(screen,darkGoldenrod , (1145, 430, 20, 20))

    #3linha de cor
    pygame.draw.rect(screen,salmon , (1085, 450, 20, 20))
    pygame.draw.rect(screen,purple4 , (1105, 450, 20, 20))
    pygame.draw.rect(screen,darkGreen , (1125, 450, 20, 20))
    pygame.draw.rect(screen,red , (1145, 450, 20, 20))

    #4linha de cor
    pygame.draw.rect(screen,navyBlue , (1085, 470, 20, 20))
    pygame.draw.rect(screen,deepPink , (1105, 470, 20, 20))
    pygame.draw.rect(screen,dimGrey , (1125, 470, 20, 20))
    pygame.draw.rect(screen,darkRed , (1145, 470, 20, 20))

# MAIN:

size = (1200, 800)
white=(255,255,255,255)

black=(0,0,0,255)
deepSkyBlue = (0,191,255,255)
greenYellow = (173,255,47,255)
orange = (255,165,0,255)
magenta = (255,0,255,255)
yellow = (255,255,0,255)
deepPink = (255,20,147,255)
darkGoldenrod = (184,134,11,255)
salmon = (250,128,114,255)
purple4 = (85,26,139,255)
darkGreen = (0,100,0,255)
red = (255,0,0,255)
navyBlue = (0,0,128,255)
slateGrey = (112,128,144,255)
dimGrey = (105,105,105,255)
darkRed = (139,0,0,255)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Python-Paint")
screen.fill(white)


cor_at = black
balde = pygame.image.load('balde.png')
img_curva = pygame.image.load('curva.png')
info_tela()

pygame.display.flip()