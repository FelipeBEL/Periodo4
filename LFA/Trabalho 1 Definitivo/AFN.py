def gera_ram(estado):                   
    global index
    global estAtual_2
    global flag
    global casoAtual
    global handler
  
    if index != len(casoAtual):
        for regra in regras:
            if casoAtual[index] == regra[1]:
                if estado == regra[0]:
                    estAtual = regra[2]
                    
                    for k in range(len(estAtual)):   
                        estAtual_2 = estAtual[k]
                        handler.write(casoAtual[index] + " -> Estado alterado de " + str(estado) + " para " + str(estAtual[k]) + "\n")
                        index = index + 1
                        gera_ram(estAtual_2)
                        index = index - 1
                        
                        if estAtual_2 in estFin:
                            flag = 1
                            return

                        else:
                            if index == len(casoAtual)-1:
                                handler.write("Fim da ramificacao\n")
                                handler.write("Estado " + estAtual[k] + " nao eh final\n\n")
                        handler.write("Backtrack do estado " + str(estAtual[k]) + " para " + str(estado) + "\n\n")          

def afn(entrada):
    
    global regras
    global estFin
    global index
    global flag
    global casoAtual
    global handler

    handler = open("automato_ndet.txt","r")
    
    linhas = handler.readlines()

    handler.close()

    alfabeto = []
    for elemento in linhas[0]:
        if elemento != '\n':
            alfabeto.append(elemento)

    estados = linhas[1].split()                        # Leitura de dados

    estIni = linhas[2].split()

    estFin = linhas[3].split()

    qnt_regras = len(linhas) - 4

    regras = []
    for i in range(4,len(linhas)):                     # Do que foi lido no arquivo, aqui se pega as regras
        regras.append(linhas[i].split())

    for i in range(0,qnt_regras):
        aux = regras[i]
        aux2 = aux[2].split(",")
        del(aux[2])
        aux.append(aux2)
        regras[i] = aux

    handler = open("resultado.txt","w")
    
    handler.write("Alfabeto: " + str(alfabeto) + "\n" + "Estados: " +
        str(estados) + "\n" + "Estado Inicial: " + str(estIni) + "\n" + 
        "Estado(s) Final(is): " + str(estFin) + "\n" + "\nRegras: " + "\n")

    for i in range(0,qnt_regras):
        aux = regras[i]
        handler.write(str(i+1) + ") " + "(" + str(aux[0]) + "," + str(aux[1]) + ") = " + str(aux[2]) + "\n")

    handler.write("\n")

    handler.write("----------Passo a passo caso teste atual:----------\n\n")

    
    for i in range(0,len(entrada)):                  # Percorre os elementos do caso teste atual
        elemAtual = entrada[i]
        if elemAtual not in alfabeto:
                                                     # Verifica se todos os elementos do caso atual 
                                                     # pertencem ao alfabeto
            
            handler.write("O caso teste possui elemento(s) que nao esta(o) no alfabeto!")
            handler.close()
            return

    casoAtual = entrada
    index = 0
    flag = 0
    flag_aux = 0

    gera_ram(estIni[0])

    if flag == 1:
        handler.write("\nEstado " + estAtual_2 + " eh final, logo: " + casoAtual + " -> Aceito pelo automato!\n\n")
    else:
        handler.write("\nEstado " + estIni[0] + " nao eh final, logo: " + casoAtual + " -> Rejeitado pelo automato!\n\n")

    handler.close()