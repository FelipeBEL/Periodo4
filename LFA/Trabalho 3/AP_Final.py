def trataPilha(pilha):
    global registro

    atual = registro.pop()

    if atual[1] == 'E':
        pilha.append(atual[2])

    elif len(atual) >= 3:
        for i in range(1,len(atual)-1):
            pilha.pop()



def gera_ram(estado,entrada):                   
    global index
    global flag
    global estFin
    global handler
    global registro
    global pilha

    estAtual_2 = estado

    for regra in regras:
        if index < len(entrada) or regra[1] == 'E':

            if regra[1] == 'E':
                if estado == regra[0]:
                    if len(pilha) > 0:
                        if pilha[len(pilha)-1] == regra[2]:
                            
                            altPilha = regra[3]

                        
                            handler.write("E - Estado alterado de " + str(estado) + " para " + str(altPilha[0]) + "\n")

                            if altPilha[1] == 'E':
                                pilha.pop()

                                altPilha.append(regra[2])
                                registro.append(altPilha)

                            else:

                                if len(altPilha) >= 3:
                                    for i in range(1,len(altPilha)-1):
                                        pilha.append(altPilha[i])
                                    
                                registro.append(altPilha)

                            handler.write("Pilha: " + str(pilha) + "\n\n")


                            estAtual_2 = altPilha[0]
                            
                            
                            gera_ram(estAtual_2,entrada)

                            
                            trataPilha(pilha)

                            handler.write("Backtrack para o estado " + str(estado) + " com pilha " + str(pilha) + "\n\n")


            elif entrada[index] == regra[1]: 
                if estado == regra[0]:
                    if len(pilha) > 0:
                        if pilha[len(pilha)-1] == regra[2]:

                            altPilha = regra[3]
                            
                            handler.write(str(entrada[index]) + " - Estado alterado de " + str(estado) + " para " + str(altPilha[0]) + "\n")
                            
                            
                            if altPilha[1] == 'E':
                                pilha.pop()

                            elif len(altPilha) >= 3:
                                for i in range(1,len(altPilha)-1):
                                    pilha.append(altPilha[i])

                            if altPilha[1] == 'E':
                                altPilha.append(regra[2])
                                registro.append(altPilha)
                            else:
                                registro.append(altPilha)

                            handler.write("Pilha: " + str(pilha) + "\n\n")
                            
                            estAtual_2 = altPilha[0]

                            index = index + 1
                            gera_ram(estAtual_2,entrada)
                            index = index - 1
                            
                            trataPilha(pilha)

                            handler.write("Backtrack para o estado " + str(estado) + " com pilha " + str(pilha) + "\n\n")

        elif estAtual_2 in estFin:
            flag = 1

            handler.write("Estado " + str(estAtual_2) + " eh final\n\n")

            handler.write("------FOI ACEITO AQUI!------\n\n")

            return
                
                    
def ap_final(entrada,arquivo):
    global handler
    global estFin
    global index
    global flag
    global regras
    global registro
    global pilha

    handler = open(arquivo,"r")
        
    linhas = handler.readlines()
    handler.close()

    alfabeto = []
    for elemento in linhas[0]:
        if elemento != '\n':
            alfabeto.append(elemento)


    estados = linhas[1].split()                        # Leitura de dados

    estIni = linhas[2].split()

    estFin = linhas[3].split()

    simbPilha = linhas[4].split()

    pilha = [simbPilha[0]]


    qnt_regras = len(linhas) - 5

    regras = []
    for i in range(5,len(linhas)):                     # Do que foi lido no arquivo, aqui se pega as regras
        regras.append(linhas[i].split())

    for i in range(0,qnt_regras):
        aux = regras[i]
        aux2 = aux[4].split(",")
        aux2.insert(0,aux[3])
        del(aux[4])
        del(aux[3])
        aux.append(aux2)
        regras[i] = aux

    

    handler = open("resultado.txt","w")
     
    handler.write("Alfabeto: " + str(alfabeto) + "\n" + "Estados: " +
            str(estados) + "\n" + "Estado Inicial: " + str(estIni) + "\n" + 
            "Estado(s) Final(is): " + str(estFin) + "\n" + "Simbolo de inicio da pilha: " + str(simbPilha[0])
            + "\n\nRegras: " + "\n")


    for i in range(0,qnt_regras):
        aux = regras[i]
        handler.write(str(i+1) + ") " + "(" + str(aux[0]) + "," + str(aux[1]) + "," + str(aux[2]) + ") = " + str(aux[3]) + "\n")

    handler.write("\n")

    
    for i in range(0,len(entrada)):                  # Percorre os elementos do caso teste atual
            elemAtual = entrada[i]
            if elemAtual not in alfabeto:
                                                         # Verifica se todos os elementos do caso atual 
                                                         # pertencem ao alfabeto
                
                handler.write("O caso teste possui elemento(s) que nao esta(o) no alfabeto!")
                handler.close()
                exit()

    handler.write("\n----------Ramificacoes geradas---------\n\n")
    handler.write("Entrada inserida: " + entrada + "\n")

    handler.write('\n')

    index = 0
    flag = 0

    registro = []

    gera_ram(estIni[0],entrada)

    if flag == 0:
        handler.write(entrada+ " -> Rejeitado pelo automato!")
    elif flag == 1:
        handler.write(entrada+ " -> Aceito pelo automato!")
    
    handler.close()