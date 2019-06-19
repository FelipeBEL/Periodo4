import sys, pygame, os
from pygame import gfxdraw
from AP_Empty import ap_vazia
from AP_Final import ap_final
from Empty_To_Final import empty_to_final
from Final_To_Empty import final_to_empty

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

  text = basicFont.render("Alterar AP:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 400
  textRect.top = screen.get_rect().top + 190

  screen.blit(text, textRect)

  text = basicFont.render("AP pilha vazia:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 40
  textRect.top = screen.get_rect().top + 300

  screen.blit(text, textRect)

  text = basicFont.render("AP estado final:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 680
  textRect.top = screen.get_rect().top + 300

  screen.blit(text, textRect)

  text = basicFont.render("PV -> EF:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 90
  textRect.top = screen.get_rect().top + 490

  screen.blit(text, textRect)

  text = basicFont.render("EF -> PV:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 740
  textRect.top = screen.get_rect().top + 490

  screen.blit(text, textRect)


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


def trataAFNKeyboard(flag=None):                                             # Funcao que trata entradadas de dados do
  global aux                                                                 # teclado
  
  i = 100
  j = 350
  aux = ""

  trata_shift = -1
  
  while 1:
    
    for event in pygame.event.get():
  
      if event.type == pygame.QUIT: 
        sys.exit()
    
      if event.type == pygame.KEYDOWN:                            # Se apertar ENTER a leitura encerra
        if event.key == 13:
          return

        if event.key == 101:
          event.key = 69

        if event.key == 8:                                        # Ao apertar BACKSPACE apaga e recomeça
          if flag != 1: imprime_tela_caso_teste()                               # a entrada
          else: imprime_tela_er() 

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
screen = pygame.display.set_mode((970, 650))
pygame.display.set_caption("Automatos Finitos")


WHITE = (255,255,255)
RED = (255, 0, 0)
FIREBRICK = (178,34,34)
BLACK = (0,0,0)

imprime_menu()

while 1:

  for event in pygame.event.get():                      # Definição dos botões do menu
    
    pygame.draw.rect(screen, BLACK, (425, 240, 120, 80)) 
    pygame.draw.rect(screen, BLACK, (100, 350, 120, 80))
    pygame.draw.rect(screen, BLACK, (100, 540, 120, 80)) 
    pygame.draw.rect(screen, BLACK, (750, 350, 120, 80))
    pygame.draw.rect(screen, BLACK, (750, 540, 120, 80)) 


    pygame.draw.rect(screen, RED, (435, 250, 100, 60)) 
    pygame.draw.rect(screen, RED, (110, 360, 100, 60))
    pygame.draw.rect(screen, RED, (110, 550, 100, 60))
    pygame.draw.rect(screen, RED, (760, 360, 100, 60)) 
    pygame.draw.rect(screen, RED, (760, 550, 100, 60)) 

    if event.type == pygame.QUIT: 
      sys.exit()
  
    if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:     # Para cada movimento
                                                                                     # ou clique do mouse
      
      xy = event.pos                                                                 # Pega (x,y) de cada evento
      
      if xy[0] > 435 and xy[0] < 535 and xy[1] > 250 and xy[1] < 310:
        pygame.draw.rect(screen, FIREBRICK, (435, 250, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1: 
          os.system("start ./automato_pilha.txt")

      if xy[0] > 110 and xy[0] < 210 and xy[1] > 360 and xy[1] < 420:
        pygame.draw.rect(screen, FIREBRICK, (110, 360, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1: 
          imprime_tela_caso_teste()

          trataAFNKeyboard()
          imprime_menu()
          ap_vazia(aux,"automato_pilha.txt")

          os.system("start ./resultado.txt")
      

      if xy[0] > 110 and xy[0] < 210 and xy[1] > 550 and xy[1] < 610:
        pygame.draw.rect(screen, FIREBRICK, (110, 550, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1:
          imprime_tela_caso_teste()

          trataAFNKeyboard()
          imprime_menu()
           
          empty_to_final()
          ap_final(aux,"automato_pilha_final.txt")

          os.system("start ./automato_pilha_final.txt | start ./resultado.txt")

      if xy[0] > 760 and xy[0] < 860 and xy[1] > 550 and xy[1] < 610:
        pygame.draw.rect(screen, FIREBRICK, (760, 550, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1:
          imprime_tela_caso_teste()

          trataAFNKeyboard()
          imprime_menu()
           
          final_to_empty()
          ap_vazia(aux,"automato_pilha_vazia.txt")

          os.system("start ./automato_pilha_vazia.txt | start ./resultado.txt")

      if xy[0] > 760 and xy[0] < 860 and xy[1] > 360 and xy[1] < 420:
        pygame.draw.rect(screen, FIREBRICK, (760, 360, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1: 
          imprime_tela_caso_teste()

          trataAFNKeyboard()
          imprime_menu()
          ap_final(aux,"automato_pilha.txt")

          os.system("start ./resultado.txt")


    pygame.display.update()