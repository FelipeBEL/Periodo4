from AFD_Adaptado import afd

def remove_repetidos(lista):                            # Funcao que remove elementos repetidos do conjunto
    l = []                                              # gerados apos o processo de uniao
    for i in lista:
        if i not in l:
            l.append(i)
    return l
                    
def e_fecho(estados):

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

def uniao(conjEst):
    global aux

    aux = []
    aux2 = []
    concatenado = []

    for i in range(0,len(alfabeto)):
        for j in range(0,len(conjEst)):
            for k in range(0,len(regras)):
                aux = regras[k]
                
                if conjEst[j] == aux[0] and aux[1] == alfabeto[i]:
                    aux2 = aux2 + aux[2]
                    break

        while "vazio" in aux2:
            aux2.remove("vazio")

        aux2 = remove_repetidos(aux2)

        if len(aux2) == 0:
            aux2.append("vazio")

        concatenado.append(list(aux2))
      
        aux2[:] = []
    return concatenado


def gera_r(conj):                                   # Funcao recursiva que utiliza o teorema de conversão de AFN para AFD
    global registro
    global handler

    for i in range(len(conj)):
        efecho_conj = e_fecho(conj[i])

        if efecho_conj not in registro and efecho_conj != ['vazio']:        # vazio eh um estado mas não deve 
                                                                            # ser considerado como uma nova ocorrencia
            print_uniao = uniao(efecho_conj)
            handler.write("E-fecho do novo estado = " + str(efecho_conj) + " -> Nova ocorrencia\n\n")
            handler.write(str(efecho_conj) + " gera " + str(print_uniao) + "\n")

            registro.append(efecho_conj)
            gera_r(uniao(efecho_conj))

            handler.write("\n" + str(print_uniao) + ": Nenhuma nova ocorrencia -> Backtrack para " + str(efecho_conj))     

def afne_to_afd(entrada):
    
    global alfabeto
    global registro
    global regras
    global estFin
    global estFinD
    global handler


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
      

    handler.write("\n----------Convertido para AFD:---------- \n\n" + "Estados D: Todos os subconjuntos de " + str(estados))


    handler.write("\n\nEstados Finais D: Todos os conjuntos do total de conjuntos que possuem o(s) estado(s) ")

    for e in estFin:
        handler.write(str(e) + " ")

    handler.write("\n\n----------Passo a passo do teorema:----------\n\n")

    registro = []
    gera_r([estIni])            # registro eh setado aqui

    estFinD = []
    for k in range(0,len(estFin)):
        for i in range(0,len(registro)):
            if estFin[k] not in registro[i]:
                continue
            else:
                estFinD.append(registro[i])

    registro.append(['vazio'])          # Vazio sera tratado como estado

    handler.write("\n\n----------Conjuntos gerados pelo teorema que utilizaremos no AFD:----------\n\n" + str(registro))

# Comeca processo de escrita do AFN-E convertido no arquivo AFN_E_convertido.txt

    handle = open("AFN_E_convertido.txt","w")

    for item in alfabeto:
        handle.write(item)

    handle.write('\n')

    handle.write("2^" + str(len(estados)) + "subconjuntos")

    handle.write('\n')

    handle.write('(')
    for item in e_fecho(estIni):
        handle.write(str(item))
        if item != e_fecho(estIni)[len(e_fecho(estIni))-1]:
            handle.write(',')
        else:
            handle.write(')')

    handle.write('\n')

    for item in estFinD:
        if item in registro:
            if type(item) == str:
                handle.write('(' + str(item) + ') ')
            else:    
                handle.write('(')
                for elem in item:
                    handle.write(str(elem))
                    if elem != item[len(item)-1]:
                        handle.write(',')
                    else:
                        handle.write(') ')

    handle.write('\n')

    for reg in registro:
        uniao_aux = uniao(reg)

        for i in range(0,len(alfabeto)):
            handle.write('(')
            for item in reg:
                handle.write(str(item))
                if item != reg[len(reg)-1]:
                    handle.write(',')
                else:
                    handle.write(') ')

            handle.write(alfabeto[i] + ' ')
            handle.write('(')
            item = e_fecho(uniao_aux[i])

            for elem in item:
                handle.write(str(elem))
                if elem != item[len(item)-1]:
                    handle.write(',')
                else:
                    handle.write(')')
    
            handle.write('\n')
    handle.close()

    # Fim da escrita em arquivo
    afd("AFN_E_convertido.txt",entrada,handler)                  # Chama codigo do AFD enviando como parametro o AFN convertido e seus casos teste

    handler.close()