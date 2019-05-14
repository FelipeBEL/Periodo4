import sys, pygame, numpy
from pygame import gfxdraw
from primitivas import *

# MAIN 2:

flag = 0
sinal_linha = 0
sinal_quadrado = 0
sinal_retangulo = 0
sinal_polilinha = 0
sinal_circulo = 0
sinal_curva = 0 

screenCopy = screen.copy()
whiteCopy = screen.copy()   # Copia em branco da tela usada para o CLEAR

while 1:
    for event in pygame.event.get():

        pygame.draw.rect(screen,cor_at, (1100,535 , 50, 50))


        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            xy = event.pos

        # Tratamento de limpeza de tela ao pressionar CLEAR
            if xy[0] >= 1070 and xy[0] <= 1185 and xy[1] >= 35 and xy[1] <= 55:
                
                screen.blit(whiteCopy,(0,0))

                if flag == 1:
                    pygame.draw.rect(screen, dimGrey, (1065, 75, 60, 60))
                    pygame.draw.rect(screen, white, (1070, 80, 50, 50))
                    linha(1075,85,1115,125,black)
                if flag == 2:
                    pygame.draw.rect(screen, dimGrey, (1130, 75, 60, 60))
                    pygame.draw.rect(screen, white, (1135, 80, 50, 50))
                    quadrado(1144,88,1175,120,black)

                if flag == 3:
                    pygame.draw.rect(screen, dimGrey, (1065, 140, 60, 60))
                    pygame.draw.rect(screen, white, (1070, 145, 50, 50))
                    retangulo(1074,158,1115,183,black)

                if flag == 4:
                    pygame.draw.rect(screen, dimGrey, (1130, 140, 60, 60))
                    pygame.draw.rect(screen, white, (1135, 145, 50, 50))
                    linha(1150,150,1140,190,black)
                    linha(1150,150,1165,190,black)
                    linha(1165,190,1175,150,black)

                if flag == 5:
                    pygame.draw.rect(screen, dimGrey, (1065, 205, 60, 60))
                    pygame.draw.rect(screen, white, (1070, 210, 50, 50))
                    circulo(1095,235,20,black)

                if flag == 6:
                    pygame.draw.rect(screen, dimGrey, (1130, 205, 60, 60))
                    pygame.draw.rect(screen, white, (1135, 210, 50, 50))
                    screen.blit(img_curva,(1138,212))


                if flag == -1:
                    pygame.draw.rect(screen, dimGrey, (1095, 695, 60, 60))
                    pygame.draw.rect(screen, white, (1100, 700, 50, 50))
                    screen.blit(balde,(1105,705))


            # Animacao e aplicando funcao ao botao linhas
            if xy[0] >= 1070 and xy[0] <= 1120 and xy[1] >= 80 and xy[1] <= 130:

                
                if flag != 1:
                    info_tela()
                    pygame.draw.rect(screen, dimGrey, (1065, 75, 60, 60))
                    pygame.draw.rect(screen, white, (1070, 80, 50, 50))
                    linha(1075,85,1115,125,black)

                    flag = 1
                  

                else:
                    pygame.draw.rect(screen, slateGrey, (1065, 75, 60, 60))
                    pygame.draw.rect(screen, white, (1070, 80, 50, 50))
                    linha(1075,85,1115,125,black)
                    flag = 0

            # Animacao e aplicando funcao ao botao quadrado
            if xy[0] >= 1135 and xy[0] <= 1185 and xy[1] >= 80 and xy[1] <= 130:
                
                
                if flag != 2:
                    info_tela()
                    pygame.draw.rect(screen, dimGrey, (1130, 75, 60, 60))
                    pygame.draw.rect(screen, white, (1135, 80, 50, 50))
                    quadrado(1144,88,1175,120,black)

                    flag = 2
                    
                else:
                    pygame.draw.rect(screen, slateGrey, (1130, 75, 60, 60))
                    pygame.draw.rect(screen, white, (1135, 80, 50, 50))
                    quadrado(1144,88,1175,120,black)
                    flag = 0

            # Animacao e aplicando funcao ao botao retangulo
            if xy[0] >= 1070 and xy[0] <= 1120 and xy[1] >= 145 and xy[1] <= 195:
                
                if flag != 3:
                    info_tela()
                    pygame.draw.rect(screen, dimGrey, (1065, 140, 60, 60))
                    pygame.draw.rect(screen, white, (1070, 145, 50, 50))
                    retangulo(1074,158,1115,183,black)

                    flag = 3
                   
                else:
                    pygame.draw.rect(screen, slateGrey, (1065, 140, 60, 60))
                    pygame.draw.rect(screen, white, (1070, 145, 50, 50))
                    retangulo(1074,158,1115,183,black)
                    flag = 0
            # Animacao e aplicando funcao ao botao polilinha
            if xy[0] >= 1135 and xy[0] <= 1185 and xy[1] >= 145 and xy[1] <= 195:
                
                if flag != 4:
                    info_tela()
                    pygame.draw.rect(screen, dimGrey, (1130, 140, 60, 60))
                    pygame.draw.rect(screen, white, (1135, 145, 50, 50))
                    linha(1150,150,1140,190,black)
                    linha(1150,150,1165,190,black)
                    linha(1165,190,1175,150,black)

                    flag = 4
                
                else:
                    pygame.draw.rect(screen, slateGrey, (1130, 140, 60, 60))
                    pygame.draw.rect(screen, white, (1135, 145, 50, 50))
                    linha(1150,150,1140,190,black)
                    linha(1150,150,1165,190,black)
                    linha(1165,190,1175,150,black)
                    flag = 0


            # Animacao e aplicando funcao ao botao circulo
            if xy[0] >= 1070 and xy[0] <= 1120 and xy[1] >= 210 and xy[1] <= 260:

                if flag != 5:
                    info_tela()
                    pygame.draw.rect(screen, dimGrey, (1065, 205, 60, 60))
                    pygame.draw.rect(screen, white, (1070, 210, 50, 50))
                    circulo(1095,235,20,black)

                    flag = 5
                else:
                    pygame.draw.rect(screen, slateGrey, (1065, 205, 60, 60))
                    pygame.draw.rect(screen, white, (1070, 210, 50, 50))
                    circulo(1095,235,20,black)

                    flag = 0
            # Animacao e aplicando funcao ao botao curva
            if xy[0] >= 1135 and xy[0] <= 1185 and xy[1] >= 210 and xy[1] <= 260:
                
                if flag != 6:
                    info_tela()
                    pygame.draw.rect(screen, dimGrey, (1130, 205, 60, 60))
                    pygame.draw.rect(screen, white, (1135, 210, 50, 50))
                    screen.blit(img_curva,(1138,212))


                    flag = 6
                   
                else:
                    pygame.draw.rect(screen, slateGrey, (1130, 205, 60, 60))
                    pygame.draw.rect(screen, white, (1135, 210, 50, 50))
                    screen.blit(img_curva,(1138,212))


                    flag = 0

            # Animacao e aplicando funcao das cores
            if xy[0] >= 1085 and xy[0] <= 1105 and xy[1] >= 410 and xy[1] <= 430:
                pygame.draw.rect(screen,black , (1100,535 , 50, 50))
                cor_at = black

            if xy[0] >= 1105 and xy[0] <= 1125 and xy[1] >= 410 and xy[1] <= 430:
                pygame.draw.rect(screen,deepSkyBlue , (1100,535 , 50, 50))
                cor_at = deepSkyBlue

            if xy[0] >= 1125 and xy[0] <= 1145 and xy[1] >= 410 and xy[1] <= 430:
                pygame.draw.rect(screen,greenYellow , (1100,535 , 50, 50))
                cor_at = greenYellow

            if xy[0] >= 1145 and xy[0] <= 1165 and xy[1] >= 410 and xy[1] <= 430:
                pygame.draw.rect(screen,orange , (1100,535 , 50, 50))
                cor_at = orange

            if xy[0] >= 1085 and xy[0] <= 1105 and xy[1] >= 430 and xy[1] <= 450:
                pygame.draw.rect(screen,magenta , (1100,535 , 50, 50))
                cor_at = magenta
            if xy[0] >= 1105 and xy[0] <= 1125 and xy[1] >= 430 and xy[1] <= 450:
                pygame.draw.rect(screen,yellow , (1100,535 , 50, 50))
                cor_at = yellow
            if xy[0] >= 1125 and xy[0] <= 1145 and xy[1] >= 430 and xy[1] <= 450:
                pygame.draw.rect(screen,white , (1100,535 , 50, 50))
                cor_at =  white
            if xy[0] >= 1145 and xy[0] <= 1165 and xy[1] >= 430 and xy[1] <= 450:
                pygame.draw.rect(screen, darkGoldenrod , (1100,535 , 50, 50))
                cor_at = darkGoldenrod
            

            

            if xy[0] >= 1085 and xy[0] <= 1105 and xy[1] >= 450 and xy[1] <= 470:
                pygame.draw.rect(screen,salmon , (1100,535 , 50, 50))
                cor_at = salmon
            if xy[0] >= 1105 and xy[0] <= 1125 and xy[1] >= 450 and xy[1] <= 470:
                pygame.draw.rect(screen,purple4 , (1100,535 , 50, 50))
                cor_at = purple4
            if xy[0] >= 1125 and xy[0] <= 1145 and xy[1] >= 450 and xy[1] <= 470:
                pygame.draw.rect(screen,darkGreen , (1100,535 , 50, 50))
                cor_at =  darkGreen
            if xy[0] >= 1145 and xy[0] <= 1165 and xy[1] >= 450 and xy[1] <= 470:
                pygame.draw.rect(screen, red , (1100,535 , 50, 50))
                cor_at = red

            if xy[0] >= 1085 and xy[0] <= 1105 and xy[1] >= 470 and xy[1] <= 490:
                pygame.draw.rect(screen,navyBlue , (1100,535 , 50, 50))
                cor_at = navyBlue
            if xy[0] >= 1105 and xy[0] <= 1125 and xy[1] >= 470 and xy[1] <= 490:
                pygame.draw.rect(screen,deepPink , (1100,535 , 50, 50))
                cor_at = deepPink
            if xy[0] >= 1125 and xy[0] <= 1145 and xy[1] >= 470 and xy[1] <= 490:
                pygame.draw.rect(screen,dimGrey , (1100,535 , 50, 50))
                cor_at =  dimGrey
            if xy[0] >= 1145 and xy[0] <= 1165 and xy[1] >= 470 and xy[1] <= 490:
                pygame.draw.rect(screen, darkRed , (1100,535 , 50, 50))
                cor_at = darkRed

            # Animacao e aplicando funcao ao botao flood fill
            if xy[0] >= 1100 and xy[0] <= 1150 and xy[1] >= 700 and xy[1] <= 750:
                
                if flag != -1:

                    info_tela()
                    pygame.draw.rect(screen, dimGrey, (1095, 695, 60, 60))
                    pygame.draw.rect(screen, white, (1100, 700, 50, 50))
                    screen.blit(balde,(1105,705))

                    flag = -1
                   
                else:
                    pygame.draw.rect(screen, slateGrey, (1095, 695, 60, 60))
                    pygame.draw.rect(screen, white, (1100, 700, 50, 50))
                    screen.blit(balde,(1105,705))                    
                    flag = 0
            
            
            # Flag indica qual botao foi pressionado e esses if's dizem qual funcao foi ativada pelo botao
            if flag == -1 and xy[0] <= 1050:
                cor_f =  screen.get_at((xy[0],xy[1]))
                floodfill(xy[0],xy[1],cor_at,cor_f)

            if flag == 1 and xy[0] <= 1050:
                sinal_linha = 1      
                    
            if flag == 2 and xy[0] <= 1050:
                sinal_quadrado = 1          

            if flag == 3 and xy[0] <= 1050:
                sinal_retangulo = 1

            if flag == 4 and xy[0] <= 1050:
                screenCopy = screen.copy()
                sinal_polilinha = 1
                if pygame.mouse.get_pressed()[2] == 1:
                    sinal_polilinha = 0

            if flag == 5 and xy[0] <= 1050:
                sinal_circulo = 1

            if flag == 6 and xy[0] <= 1050:
                sinal_curva = 1


        if event.type == pygame.MOUSEMOTION:
            xy2 = event.pos
            
            if sinal_linha == 1:                                                    # Se o botão de desenhar linhas estiver pressionado
                if xy[0] <= 1050 and xy2[0] <= 1050:
                    screen.blit(screenCopy,(0,0))
                    linha(xy[0],xy[1],xy2[0],xy2[1],cor_at)

                    
        
            if sinal_quadrado == 1:                                                 # Se o botão de desenhar quadrados estiver pressionado
                if xy[0] <= 1050:
                    lado1 = abs(xy[1] - xy2[1])
                    lado2 = abs(xy2[0] - xy[0])
                    diferenca = abs(lado2 - lado1)

                    if xy2[0] + diferenca <= 1050:
                        screen.blit(screenCopy,(0,0))

                        if lado2 > lado1:                                            # Se o lado2 > lado1 entao eh necessario alterar y2
                            if xy[1] < xy2[1]:          
                                quadrado(xy[0],xy[1],xy2[0],xy2[1]+diferenca,cor_at)     # Soma diferenca com y2 se ele for > y1
                            else:
                                quadrado(xy[0],xy[1],xy2[0],xy2[1]-diferenca,cor_at)     # Subtrai y2 com a diferenca se ele for <= y1
                        
                        if lado1 > lado2:                                               # Se o lado2 < lado1 entao eh necessario alterar x2
                        
                            if xy2[0] > xy[0]:      
                                quadrado(xy[0],xy[1],xy2[0]+diferenca,xy2[1],cor_at)     # Soma diferenca com x2 se ele for > x1
                            else:
                                quadrado(xy[0],xy[1],xy2[0]-diferenca,xy2[1],cor_at)     # Subtrai x2 com a diferenca se ele for <= x1
            
            if sinal_retangulo == 1:                                                # Se o botão de desenhar retangulos estiver pressionado
                if xy[0] <= 1050 and xy2[0] <= 1050:
                    screen.blit(screenCopy,(0,0))
                    retangulo(xy[0],xy[1],xy2[0],xy2[1],cor_at)

            if sinal_circulo == 1:                                                    # Se o botão de desenhar circulos estiver pressionado
                if xy[0] <= 1050 and xy2[0] <= 1050:
            
                    r = distancia(xy[0],xy[1],xy2[0],xy2[1])

                    if xy[0] + r <= 1050:
                        screen.blit(screenCopy,(0,0))
                        circulo(xy[0],xy[1],r,cor_at)

            if sinal_polilinha == 2:                                                    # Se o botão de desenhar polilinhas estiver pressionado
                if xy[0] <= 1050 and xy2[0] <= 1050:
                    screen.blit(screenCopy,(0,0))
                    linha(xy[0],xy[1],xy2[0],xy2[1],cor_at)

            if sinal_curva == 1:
                if xy[0] <= 1050 and xy2[0] <= 1050:
                    screen.blit(screenCopy,(0,0))
                    bezierIngenuo(xy,xy2,cor_at)



        if event.type == pygame.MOUSEBUTTONUP:
            sinal_circulo = 0
            sinal_quadrado = 0
            sinal_linha = 0
            sinal_retangulo = 0
            sinal_curva = 0
            if sinal_polilinha == 1:
                sinal_polilinha = 2
            screenCopy = screen.copy()

        pygame.display.flip()