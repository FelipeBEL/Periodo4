def empty_to_final():

    handler = open("automato_pilha.txt","r")
        
    linhas = handler.readlines()
    handler.close()

    estados = linhas[1].split()
    estIni = linhas[2].split()


    linhas[4] = "x0\n"                          # Substitui z0 por x0 no arquivo

    linhas[1] = linhas[1].replace("\n","")
    linhas[1] = linhas[1] + " p0 p\n"           # Adiciona os novos estados ao conj de estados
    
    linhas[2] = "p0\n"    # Insere estado inicial
    linhas[3] = "p\n"  # Insere estado final

    linhas[len(linhas)-1] = linhas[len(linhas)-1] + "\n"    # Coloca pulo de linha no fim do arquivo
        
    linhas.append("p0 E x0 " + str(estIni[0]) + " z0,x0\n") # (p0,E,x0) = (q0,z0x0)
 
    for i in range(len(estados)):                           # (q,E,x0) = (p,E)
                                                            # para todos os estados
        if i < len(estados)-1:
            linhas.append(str(estados[i]) + " E x0 p E\n")
        else:
            linhas.append(str(estados[i]) + " E x0 p E")

    handler = open("automato_pilha_final.txt","w")

    for linha in linhas:
        handler.write(linha)

    handler.close()

