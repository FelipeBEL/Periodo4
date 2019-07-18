import sys, pygame, os
from pygame import gfxdraw
from Gram_To_CHSKY import simplifica

def imprime_menu():                                               # Funcao que imprime menu principal
  screen.fill(WHITE)
  pygame.display.flip()

  basicFont = pygame.font.SysFont(None, 60)                       
  text = basicFont.render("Selecione um botão", True, (0,0,0))
  textRect = text.get_rect()
  textRect.centerx = screen.get_rect().centerx
  textRect.top = screen.get_rect().top + 50

  screen.blit(text, textRect)

  basicFont = pygame.font.SysFont(None, 48)

  text = basicFont.render("Alterar Gramatica:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 150
  textRect.top = screen.get_rect().top + 200

  screen.blit(text, textRect)



  text = basicFont.render("Simplificacao e FNC:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 150
  textRect.top = screen.get_rect().top + 440

  screen.blit(text, textRect)





# main:

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Gramatica to FNC")


WHITE = (255,255,255)
RED = (255, 0, 0)
FIREBRICK = (178,34,34)
BLACK = (0,0,0)

imprime_menu()

while 1:

  for event in pygame.event.get():                      # Definição dos botões do menu
    pygame.draw.rect(screen, BLACK, (250, 250, 120, 80)) 
    pygame.draw.rect(screen, BLACK, (250, 490, 120, 80))
    
    
    pygame.draw.rect(screen, RED, (260, 260, 100, 60))
    pygame.draw.rect(screen, RED, (260, 500, 100, 60))
   
    if event.type == pygame.QUIT: 
      sys.exit()
  
    if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:     # Para cada movimento
                                                                                     # ou clique do mouse
      
      xy = event.pos                                                                 # Pega (x,y) de cada evento

      if xy[0] > 260 and xy[0] < 360 and xy[1] > 260 and xy[1] < 330:                
        pygame.draw.rect(screen, FIREBRICK, (260, 260, 100, 60))

        if pygame.mouse.get_pressed()[0] == 1:                   
          os.system("start ./gramatica.txt")                    
                 
          
      if xy[0] > 260 and xy[0] < 360 and xy[1] > 500 and xy[1] < 560:                
        pygame.draw.rect(screen, FIREBRICK, (260, 500, 100, 60))

        if pygame.mouse.get_pressed()[0] == 1:
          
          simplifica()

          os.system("start ./simplificado.txt")       ##colocar função e abertuda do arquivo            

    pygame.display.update()                                                                                  
