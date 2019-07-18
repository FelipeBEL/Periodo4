def simplifica():
    global e_prods
    global regras
    global registro
    global v
    global s
    global flag
    global F
    global t
    global arq
    global dicio
    
    handler = open("gramatica.txt","r")

    linhas = handler.readlines()

    handler.close()


    v = linhas[0].split()
    t = linhas[1].split()
    s = linhas[2].split()


    regras = []
    for i in range(3,len(linhas)):                     # Do que foi lido no arquivo, aqui se pega as regras
        regras.append(linhas[i].split())

    for regra in regras:
        regra.remove('-')

        for i in range(1,len(regra)):
            elem = regra[i].split(',')
            del(regra[i])
            regra.insert(i,elem)

    arq = open("simplificado.txt","w")

    arq.write("-----Gramatica original-----\n\n")

    print_gramatica()

    arq.write("\n-----Passo 1: Remover e-producoes-----\n\n")

    e_prods = []

    descobre_e_prod()

    for j in e_prods:
        for i in v:
            substitui_e_producoes(i,j)      # Passo 1
            descobre_e_prod()

        arq.write("\n>> Removendo " + str(j) + " -> E:\n\n")
        print_gramatica()

    elimina_e_prod()

    arq.write("\n>> Removendo E-producoes restantes das regras:\n\n")

    print_gramatica()


    arq.write("\n-----Passo 2: Remover producoes unitarias-----\n\n")

    flag = 0
    F = []

    substitui_unitarios()               # Passo 2

    elimina_unitarios()

    print_gramatica()

    arq.write("\n-----Passo 3: Remover simbolos inuteis-----\n\n")

    arq.write(">> Etapa 1: Remover nao geradores\n\n")

    elimina_nao_geradores()             # Passo 3

    print_gramatica()

    registro = []    

    arq.write("\n>> Etapa 2: Remover nao alcancaveis\n\n")

    elimina_nao_alcancaveis(s[0])

    registro.append(s[0])

    for simb in v:                  # Se a regra não apareceu no registro ela é eliminada
        
        if simb not in registro:
            
            for regra in regras:

                if regra[0] == simb:
                    regras.remove(regra)
                    break

    print_gramatica()

    flag_alfa = 0
    t_aux = t.copy()

    for alfa in t_aux:                  # Remove terminais que so a(s) regra(s) eliminada(s)
        for regra in regras:            # possuia(m)
            for elem in regra[1::]:
                if alfa in elem:
                    
                    flag_alfa = 1
                    break

        if flag_alfa == 0:
            t.remove(alfa)
        
        flag_alfa = 0


    v = registro            # Registro vira o novo conj de simbolos


    arq.write("\n-----Gramatica simplificada-----\n\n")

    print_gramatica()

    dicio =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    Chonsky()    

    arq.close()


# 1 - E-produções


def descobre_e_prod():                      # Descobre todos os simbolos que possuem E-produções
    global e_prods

    for regra in regras:
        for elem in regra[1::]:
            if 'E' in elem and regra[0] not in e_prods:
                e_prods.append(regra[0])

                
def elimina_e_prod():                       # Elimina as E-produções
    global regras

    for regra in regras:
        if ['E'] in regra and regra[0] != s[0]:
            regra.remove(['E'])

def substitui_e_producoes(regraAtual, simbEprod):   # Faz substituicoes necessarias nas outras regras

    reg = []
    aux1 = []
    aux2 = []
    flag = 0
    
    for regra in regras:
        
        if regra[0] == regraAtual:
            for elem in regra[1::]:
                
                if simbEprod in elem:
                    
                    if len(elem) == 1:
                        regra.remove(elem)
                        regra.append(['E'])

                    else:
                        for i in range(1,2 ** len(elem)):                # Gera todos os subconjuntos da regra atual
                            cont = len(elem) - 1
                            aux1[:] = []
                            binario = bin(i)

                            for j in range(len(binario)-1,1,-1):
                                if binario[j] == '1':
                                    aux1.insert(0,elem[cont])
                                    
                                cont = cont - 1
                            aux2.append(list(aux1))                     # Eles sao colocados em aux2

                        for el in elem:                           # Pega o restante dos simbolos/terminais
                            if el != simbEprod:                   # da regra atual que não sejam o que estamos
                                reg.append(el)                    # removendo

                        for subcj in aux2:                        # Para todos os subconjuntos pega aqueles
                            for r in reg:                         # que possuem os outros elementos da regra
                                if r not in subcj:
                                    flag = 1
                                    break
                            
                            if flag == 0:
                                if subcj not in regra:
                                    regra.append(subcj)

                            flag = 0
                        
                        aux2[:] = []
                        reg[:] = []

                
# 2 - Produções Unitárias:

def elimina_unitarios():
    for regra in regras:
        for elem in regra[1::]:
            if len(elem) == 1 and elem[0] in v:
                regra.remove(elem)

def substitui_unitarios():
    global F
    global regras

    index = 0

    for regra in regras:
        aux = regra

        transitividade(regra[0])
        
        for f in F:
            
            for regra_t in regras:
                
                if regra_t[0] == f:
                    regra = regra + regra_t[1::]
                    break
                    
        
        regras.remove(aux)
        regras.insert(index,regra)

        index = index + 1

        F[:] = []


def transitividade(simbolo):
    global F

    for regra in regras:
        if regra[0] == simbolo:
            for elem in regra[1::]:
                if len(elem) == 1:
                    if elem[0] in v and elem[0] not in F and elem[0] != regra[0]:
                        F.append(elem[0])
                        transitividade(elem[0])
                    


# 3 - Símbolos inúteis:

def elimina_nao_geradores():
    global flag
    global registro
    global regras

            
    for regra in regras:
        for elem in regra[1::]:
            
            for i in range(0,len(elem)):
                
                if elem[i] in v:
                    
                    
                    for reg in regras:

                        if reg[0] == elem[i]:
                            
                            flag = 1
                            break
                            
                    
                    if flag == 0:
                       
                        regra.remove(elem)
                        aux = regra
                        regras.remove(regra)
                        regras.append(aux)

                        flag = 0
                        break

                    
                    flag = 0


def elimina_nao_alcancaveis(simbAtual):
    global regras
    global registro
   
    for regra in regras:
        if regra[0] == simbAtual:
            for elem in regra[1::]:
                for i in range(0,len(elem)):
                    if elem[i] in v:

                        if elem[i] not in registro:
                            registro.append(elem[i])
                        
                            elimina_nao_alcancaveis(elem[i])

def print_gramatica():
    global arq

    cont = 1
    for regra in regras:
        arq.write(str(regra[0]) + " -> ")
        for elem in regra[1::]:
            for i in range(len(elem)):
                arq.write(str(elem[i]))
            cont = cont + 1

            if cont < len(regra):
                arq.write(" | ")
        
        cont = 1
        arq.write("\n")

def Chonsky():
    global regras
    global v
    global s
    global flag
    global F
    global t
    global cont_v
    global arq

    cont_v = 0

    for i in v:
        if i in dicio:
            dicio.remove(i)

    elimina_terminais()

    elimina_duplov()

    arq.write("\n-----Forma Normal de Chomsky-----\n\n")

    print_gramatica()


def elimina_terminais():
    global t
    global cont_v
    global regras
    global dicio
    reg = []
    equivalencia = []
    aux = []
    aux_lista = []

    for regra in regras:
        for elem in regra[1::]:
            if len(elem)>1:
                for i in range(0,len(elem)):
                    if elem[i] in t and elem[i] not in reg:
                        v.append(dicio[0])
                        aux.append(dicio[0])
                        reg.append(elem[i])
                        aux.append([elem[i]])
                        regras.append(aux)
                        aux_lista.append(elem[i])
                        aux_lista.append(dicio[0])
                        equivalencia.append(aux_lista)
                        elem[i] = dicio[0]
                        aux = []
                        aux_lista = []
                        dicio.remove(dicio[0])

                    
                    if elem[i] in t and elem[i] in reg:
                        for parte in equivalencia:
                            if elem[i] == parte[0]:
                                elem[i] = parte[1]


def elimina_duplov():
    global cont_v
    global regras

    reg = []
    aux = []
    aux_lista = []
    aux_lista2 = []
    equivalencia = []
    for regra in regras:
        for elem in regra[1::]:
            while len(elem)>2:
            
                aux_lista.append(elem[0])
                aux_lista.append(elem[1])
                if aux_lista not in reg:
                    v.append(dicio[0])
                    aux.append(dicio[0])    
                    aux.append(aux_lista)
                    regras.append(aux) 
                    reg.append(aux_lista)
                    v.append(aux_lista)
                    elem[1] = dicio[0]
                    del(elem[0])
                    aux_lista2.append(aux_lista)
                    aux_lista2.append(dicio[0])
                    equivalencia.append(aux_lista2)
                    aux = []
                    aux_lista2 = []
                    aux_lista = []
                    dicio.remove(dicio[0])

                elif aux_lista in reg:
                    for parte in equivalencia:
                            if str((parte[0])[0]) == str(elem[0]) and str((parte[0])[1]) == str(elem[1]):
                                elem[1] = parte[1]
                                aux_lista = []
                                del(elem[0])
