import sys, pygame, os
from pygame import gfxdraw
from AFN import afn
from AFN_to_AFD import afn_to_afd
from AFD import afd

def imprime_menu():                                               # Funcao que imprime menu principal
  screen.fill(WHITE)
  pygame.display.flip()

  basicFont = pygame.font.SysFont(None, 60)                       
  text = basicFont.render("Selecione um botão", True, (0,0,0))
  textRect = text.get_rect()
  textRect.centerx = screen.get_rect().centerx
  textRect.top = screen.get_rect().top + 100

  screen.blit(text, textRect)

  basicFont = pygame.font.SysFont(None, 48)

  text = basicFont.render("Alterar AFN:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 100
  textRect.top = screen.get_rect().top + 280

  screen.blit(text, textRect)

  text = basicFont.render("Alterar AFD:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 400
  textRect.top = screen.get_rect().top + 280

  screen.blit(text, textRect)

  text = basicFont.render("AFD:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 760
  textRect.top = screen.get_rect().top + 280

  screen.blit(text, textRect)

  text = basicFont.render("AFN sem conversão:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 100
  textRect.top = screen.get_rect().top + 520

  screen.blit(text, textRect)

  text = basicFont.render("AFN com conversão:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 600
  textRect.top = screen.get_rect().top + 520

  screen.blit(text, textRect)

  pygame.display.update()

def imprime_tela_caso_teste():                                      # Funcao que imprime menu que solicita caso
  screen.fill(WHITE)                                                # teste
  pygame.display.flip()

  basicFont = pygame.font.SysFont(None, 60)
  text = basicFont.render("Escreva seu caso teste:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.centerx = screen.get_rect().centerx
  textRect.top = screen.get_rect().top + 100

  screen.blit(text, textRect)

  pygame.display.update()


def trataAFNKeyboard():                                             # Funcao que trata entradadas de dados do
  global aux                                                        # teclado
  global trata_shift
  i = 100
  j = 350
  aux = ""
  
  while 1:
    
    for event in pygame.event.get():
  
      if event.type == pygame.QUIT: 
        sys.exit()
    
      if event.type == pygame.KEYDOWN:                            # Se apertar ENTER a leitura encerra
        if event.key == 13:
          return

        if event.key == 8:                                        # Ao apertar BACKSPACE apaga e recomeça
          imprime_tela_caso_teste()                               # a entrada

          aux = ""
          i = 100
          j = 350

        if event.key == 270:
          teclaAtual = "+"
        elif event.key == 268:
          teclaAtual = "*"
        elif (trata_shift == 303 or trata_shift == 304) and event.key == 57:
          teclaAtual = "("
        elif (trata_shift == 303 or trata_shift == 304) and event.key == 48:
          teclaAtual = ")"
        elif event.key == 46:
          teclaAtual = "."
        else:
          teclaAtual = str(chr(event.key))

        trata_shift = event.key

        if event.key == 303 or event.key == 304:
          break

        if(j < 700):                                              # Impede que texto saia da tela no eixo Y
              
          basicFont = pygame.font.SysFont(None, 40)
          text = basicFont.render(teclaAtual, True, (0,0,0))
          textRect = text.get_rect()
            
          textRect.left = screen.get_rect().left + i
          textRect.top = screen.get_rect().top + j

          if event.key != 8:
            screen.blit(text, textRect)
        
          pygame.display.update()

          i = textRect.right

          if(i > 900):                                             # Impede que texto saia da tela no eixo X
            j = j + 25
            i = 100

        if event.key != 8:
          aux = aux + teclaAtual


# main:

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Automatos Finitos")


WHITE = (255,255,255)
RED = (255, 0, 0)
FIREBRICK = (178,34,34)
BLACK = (0,0,0)

imprime_menu()

while 1:

  for event in pygame.event.get():
    pygame.draw.rect(screen, BLACK, (740, 350, 120, 80))                      # Definição dos botões do menu
    pygame.draw.rect(screen, BLACK, (190, 590, 120, 80))                      
    pygame.draw.rect(screen, BLACK, (690, 590, 120, 80))
    pygame.draw.rect(screen, BLACK, (140, 350, 120, 80))
    pygame.draw.rect(screen, BLACK, (440, 350, 120, 80))
    pygame.draw.rect(screen, RED, (200, 600, 100, 60))
    pygame.draw.rect(screen, RED, (700, 600, 100, 60))
    pygame.draw.rect(screen, RED, (150, 360, 100, 60))
    pygame.draw.rect(screen, RED, (750, 360, 100, 60))
    pygame.draw.rect(screen, RED, (450, 360, 100, 60))
  

    if event.type == pygame.QUIT: 
      sys.exit()
  
    if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:     # Para cada movimento
                                                                                     # ou clique do mouse
      
      xy = event.pos                                                                 # Pega (x,y) de cada evento
      
      # Para o botao da esquerda:
      if xy[0] > 200 and xy[0] < 300 and xy[1] > 600 and xy[1] < 660:                # Se o mouse estiver
        pygame.draw.rect(screen, FIREBRICK, (200, 600, 100, 60))                     # entre as cordenadas do
                                                                                     # botao N: botao escurece
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1:                   
          imprime_tela_caso_teste()
          
          trataAFNKeyboard()
          imprime_menu()

          # Aqui o codigo fonte do AFN sem conversao eh chamado (caso teste esta em aux)
          afn(aux)
          # Abre arquivo com resultado:
          os.system("xdg-open resultado.txt")                                                               

      if xy[0] > 750 and xy[0] < 850 and xy[1] > 360 and xy[1] < 420:                # Se o mouse estiver
        pygame.draw.rect(screen, FIREBRICK, (750, 360, 100, 60))                     # entre as cordenadas do
                                                                                     # botao N: botao escurece
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1:                   
          imprime_tela_caso_teste()
          
          trataAFNKeyboard()
          imprime_menu()

          # Aqui o codigo fonte do AFN sem conversao eh chamado (caso teste esta em aux)
          afd(aux)
          # Abre arquivo com resultado:
          os.system("xdg-open resultado.txt")

      # Para o botao de cima:
      if xy[0] > 150 and xy[0] < 250 and xy[1] > 360 and xy[1] < 420:
        pygame.draw.rect(screen, FIREBRICK, (150, 360, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1:
          os.system("xdg-open automato_ndet.txt")

      if xy[0] > 450 and xy[0] < 550 and xy[1] > 360 and xy[1] < 420:
        pygame.draw.rect(screen, FIREBRICK, (450, 360, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1:
          os.system("xdg-open automato_det.txt")
      
      # Para do botao da direita:
      if xy[0] > 700 and xy[0] < 800 and xy[1] > 600 and xy[1] < 660:
        pygame.draw.rect(screen, FIREBRICK, (700, 600, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1:
          imprime_tela_caso_teste()

          trataAFNKeyboard()
          imprime_menu()
          # Aqui o codigo fonte do AFN com conversao eh chamado (caso teste esta em aux)
          afn_to_afd(aux)
         
          # Abre arquivo com resultado e abre o arquivo com o AFN convertido:
          os.system("xdg-open AFN_convertido.txt && xdg-open resultado.txt")

    pygame.display.update()