import sys, pygame, os
from pygame import gfxdraw
from AFN import afn
from AFN_to_AFD import afn_to_afd
from AFD import afd
from Trata_ER import trata_er
from AFNE_To_AFD import afne_to_afd
from AFNE import afne, gera_ram

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

  text = basicFont.render("Alterar AFN:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 70
  textRect.top = screen.get_rect().top + 200

  screen.blit(text, textRect)

  text = basicFont.render("Alterar AFD:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 380
  textRect.top = screen.get_rect().top + 200

  screen.blit(text, textRect)

  text = basicFont.render("AFD:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 770
  textRect.top = screen.get_rect().top + 200

  screen.blit(text, textRect)

  text = basicFont.render("AFN sem conversão:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 20
  textRect.top = screen.get_rect().top + 440

  screen.blit(text, textRect)

  text = basicFont.render("AFN com conversão:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 630
  textRect.top = screen.get_rect().top + 440

  screen.blit(text, textRect)

  text = basicFont.render("AFN-E sem conversão:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 10
  textRect.top = screen.get_rect().top + 650

  screen.blit(text, textRect)

  text = basicFont.render("Inserir ER:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 400 
  textRect.top = screen.get_rect().top + 650

  screen.blit(text, textRect)

  text = basicFont.render("AFN-E com conversão:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 600 
  textRect.top = screen.get_rect().top + 650

  screen.blit(text, textRect)

  pygame.display.update()

  text = basicFont.render("Alterar AFN-E:", True, (0,0,0))
  textRect = text.get_rect()
  textRect.left = screen.get_rect().left + 370 
  textRect.top = screen.get_rect().top + 440

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

def imprime_tela_er():
  screen.fill(WHITE)                                                # teste
  pygame.display.flip()

  basicFont = pygame.font.SysFont(None, 60)
  text = basicFont.render("Escreva sua ER:", True, (0,0,0))
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
screen = pygame.display.set_mode((970, 800))
pygame.display.set_caption("Automatos Finitos")


WHITE = (255,255,255)
RED = (255, 0, 0)
FIREBRICK = (178,34,34)
BLACK = (0,0,0)

imprime_menu()

while 1:

  for event in pygame.event.get():                      # Definição dos botões do menu
    pygame.draw.rect(screen, BLACK, (120, 250, 120, 80)) 
    pygame.draw.rect(screen, BLACK, (420, 250, 120, 80))
    pygame.draw.rect(screen, BLACK, (750, 250, 120, 80))  
    pygame.draw.rect(screen, BLACK, (120, 490, 120, 80))
    pygame.draw.rect(screen, BLACK, (420, 490, 120, 80))   
    pygame.draw.rect(screen, BLACK, (750, 490, 120, 80))                    
    pygame.draw.rect(screen, BLACK, (120, 700, 120, 80)) 
    pygame.draw.rect(screen, BLACK, (420, 700, 120, 80)) 
    pygame.draw.rect(screen, BLACK, (750, 700, 120, 80)) 
    

    
    
    pygame.draw.rect(screen, RED, (130, 260, 100, 60))
    pygame.draw.rect(screen, RED, (430, 260, 100, 60))
    pygame.draw.rect(screen, RED, (760, 260, 100, 60))
    pygame.draw.rect(screen, RED, (130, 500, 100, 60))
    pygame.draw.rect(screen, RED, (430, 500, 100, 60))
    pygame.draw.rect(screen, RED, (760, 500, 100, 60))
    pygame.draw.rect(screen, RED, (130, 710, 100, 60)) 
    pygame.draw.rect(screen, RED, (430, 710, 100, 60)) 
    pygame.draw.rect(screen, RED, (760, 710, 100, 60)) 
  

    if event.type == pygame.QUIT: 
      sys.exit()
  
    if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:     # Para cada movimento
                                                                                     # ou clique do mouse
      
      xy = event.pos                                                                 # Pega (x,y) de cada evento

      if xy[0] > 130 and xy[0] < 230 and xy[1] > 710 and xy[1] < 770:                
        pygame.draw.rect(screen, FIREBRICK, (130, 710, 100, 60))

        if pygame.mouse.get_pressed()[0] == 1:                   
          imprime_tela_caso_teste()
          
          trataAFNKeyboard()
          imprime_menu()

          # Aqui o codigo fonte do AFN sem conversao eh chamado (caso teste esta em aux)
          afne(aux)
          # Abre arquivo com resultado:
          os.system("xdg-open resultado.txt")                    
                                                                                     
        # Se clicar em cima do botao: 
        #if pygame.mouse.get_pressed()[0] == 1:                   
          
      if xy[0] > 430 and xy[0] < 530 and xy[1] > 710 and xy[1] < 770:                
        pygame.draw.rect(screen, FIREBRICK, (430, 710, 100, 60))

        if pygame.mouse.get_pressed()[0] == 1:
          imprime_tela_er()
          
          trataAFNKeyboard(1)
          imprime_menu()

          trata_er(aux)

          os.system("xdg-open arvore.txt && xdg-open automato_ndetE.txt")                   
                                                                                     
        # Se clicar em cima do botao: 
        #if pygame.mouse.get_pressed()[0] == 1: 

      if xy[0] > 760 and xy[0] < 860 and xy[1] > 710 and xy[1] < 770:                
        pygame.draw.rect(screen, FIREBRICK, (760, 710, 100, 60))

        if pygame.mouse.get_pressed()[0] == 1:                   
          imprime_tela_caso_teste()
          
          trataAFNKeyboard()
          imprime_menu()

          # Aqui o codigo fonte do AFN sem conversao eh chamado (caso teste esta em aux)
          afne_to_afd(aux)
          # Abre arquivo com resultado:
          os.system("xdg-open AFN_E_convertido.txt && xdg-open resultado.txt")                    
                                                                                     
        # Se clicar em cima do botao: 
        #if pygame.mouse.get_pressed()[0] == 1:     

      # Para o botao da esquerda:
      if xy[0] > 130 and xy[0] < 230 and xy[1] > 500 and xy[1] < 560:                # Se o mouse estiver
        pygame.draw.rect(screen, FIREBRICK, (130, 500, 100, 60))                     # entre as cordenadas do
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

      if xy[0] > 760 and xy[0] < 860 and xy[1] > 260 and xy[1] < 320:                # Se o mouse estiver
        pygame.draw.rect(screen, FIREBRICK, (760, 260, 100, 60))                     # entre as cordenadas do
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
      if xy[0] > 130 and xy[0] < 230 and xy[1] > 260 and xy[1] < 320:
        pygame.draw.rect(screen, FIREBRICK, (130, 260, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1:
          os.system("xdg-open automato_ndet.txt")

      if xy[0] > 430 and xy[0] < 530 and xy[1] > 260 and xy[1] < 320:
        pygame.draw.rect(screen, FIREBRICK, (430, 260, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1:
          os.system("xdg-open automato_det.txt")

      if xy[0] > 430 and xy[0] < 530 and xy[1] > 500 and xy[1] < 560:
        pygame.draw.rect(screen, FIREBRICK, (430, 500, 100, 60))
        # Se clicar em cima do botao: 
        if pygame.mouse.get_pressed()[0] == 1:
          os.system("xdg-open automato_ndetE.txt")
      
      # Para do botao da direita:
      if xy[0] > 760 and xy[0] < 860 and xy[1] > 500 and xy[1] < 560:
        pygame.draw.rect(screen, FIREBRICK, (760, 500, 100, 60))
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