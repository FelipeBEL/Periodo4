def remove_repetidos(lista):                            # Funcao que remove elementos repetidos do conjunto
    l = []                                              # gerados apos o processo de uniao
    for i in lista:
        if i not in l:
            l.append(i)
    return l
                    
def e_fecho(estados):
    global regras

    efecho = []
    temp = estados

    for est in temp:
        efecho.append(est)
        for regra in regras:
            if regra[0] == est:
                if regra[1] == 'E':
                    efecho = efecho + regra[2]
                    for r in regra[2]:          # for garante que nao vai ser comparado lista com string
                        if r not in temp:
                            temp.append(r)

    efecho = remove_repetidos(efecho)
    
    return efecho

def gera_ram(estado,entrada):                   
    global index
    global estAtual_2
    global flag
    global estFin
    global handler

    
    handler.write("Chegou em: "+ estado+ "\n")
    handler.write("e_fecho de:"+ estado+ " ="+ str(e_fecho([estado]))+"\n")

    estAtual_2 = estado
    for i in range(len(estFin)):
        if estFin[i] in e_fecho([estado]) and index == len(entrada):
                flag = 1
                handler.write("E - Estado alterado de " + str(estado) + " para " + estFin[i]+ "\n")
                return

    if index != len(entrada):
        
        for regra in regras:
            
            if entrada[index] == regra[1]:
                if estado == regra[0]:
                    handler.write(str(entrada[index]) + " - Estado alterado de " + str(estado) + " para " + str(regra[2])+"\n")

                    estAtual = regra[2]
                    
                    for k in range(len(estAtual)):
                        estAtual_2 = estAtual[k]
                        index = index + 1
                        gera_ram(estAtual_2,entrada)
                        index = index - 1
                    handler.write("\nBacktrack\n")
            if  regra[1] == 'E':
                if estado == regra[0]:
                    handler.write("E - Estado alterado de " + str(estado) + " para " + str(regra[2]))

                    estAtual = regra[2]

                    for k in range(len(estAtual)):
                        estAtual_2 = estAtual[k]
                        gera_ram(estAtual_2,entrada)
                    handler.write("\nBacktrack\n")

    elif estAtual_2 in estFin:
        flag = 1
        return
                    


def afne(entrada):
    global handler
    global estFin
    global index
    global flag
    global regras

    handler = open("automato_ndetE.txt","r")
        
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


    for i in range(0,len(entrada)):                  # Percorre os elementos do caso teste atual
            elemAtual = entrada[i]
            if elemAtual not in alfabeto:
                                                         # Verifica se todos os elementos do caso atual 
                                                         # pertencem ao alfabeto
                
                handler.write("O caso teste possui elemento(s) que nao esta(o) no alfabeto!")
                handler.close()
                exit()

    handler.write(entrada + "\n")

    handler.write('\n')
    
    index = 0
    flag = 0
    
    gera_ram(estIni[0],entrada)

    if flag == 0:
        handler.write(entrada+ " -> Rejeitado pelo automato!")
    elif flag == 1:
        handler.write(entrada+ " -> Aceito pelo automato!")


    handler.close()
