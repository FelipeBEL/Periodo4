def final_to_empty():

    handler = open("automato_pilha.txt","r")
        
    linhas = handler.readlines()
    handler.close()


    alfabeto = []
    for elemento in linhas[0]:
        if elemento != '\n':
            alfabeto.append(elemento)

    estados = linhas[1].split()
    estIni = linhas[2].split()
    estFin = linhas[3].split()

    simbPilha = linhas[4].split()

    linhas[4] = "x0\n"                      # Substitui z0 por x0 no arquivo

    linhas[1] = linhas[1].replace("\n","")
    linhas[1] = linhas[1] + " p0 p\n"       # Adiciona os novos estados ao conj de estados

    linhas[2] = "p0\n"                      # Insere estado inicial
    
    linhas[len(linhas)-1] = linhas[len(linhas)-1] + "\n"    # Coloca pulo de linha no fim do arquivo

    linhas.append("p0 E x0 " + str(estIni[0]) + " z0,x0\n") # (p0,E,x0) = (q0,z0x0)
    
    for fin in estFin:          # Todos os q's dos comentarios pertencem aos estados finais

        linhas.append(str(fin) + " E " + str(simbPilha[0]) + " p E\n")  # (q,E,z0) = (p,E)
        linhas.append(str(fin) + " E x0 p E\n")     # (q,E,x0) = (p,E)

        for alfa in alfabeto:
            linhas.append(str(fin) + " E " + str(alfa) + " p E\n")

    for alfa in alfabeto:
        linhas.append("p E " + str(alfa) + " p E\n")    # (p,E,Y) = (p,E) com Y simbolo qq do alfabeto

    linhas.append("p E " + str(simbPilha[0]) + " p E\n") # (p,E,z0) = (p,E)
    linhas.append("p E x0 p E")                          # (p,E,x0) = (p,E)

    
    handler = open("automato_pilha_vazia.txt","w")

    for linha in linhas:
        handler.write(linha)

    handler.close()


final_to_empty()