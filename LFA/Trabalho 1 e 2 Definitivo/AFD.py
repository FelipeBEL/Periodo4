# Este programa pode ser utilizado para qualquer automato finito deterministico,
# apenas deve-se especificar o arquivo que diz como ele vai funcionar

def afd(caso_teste):

    handle = open("automato_det.txt","r")
    
    linhas = handle.readlines()

    handle.close()

    resultado = open("resultado.txt","w")

    alfabeto = []
    for elemento in linhas[0]:
        if elemento != '\n':
            alfabeto.append(elemento)

    estados = linhas[1].split()

    estIni = linhas[2].split()

    estFin = linhas[3].split()

    qnt_regras = len(linhas) - 4

    regras = []
    for i in range(4,len(linhas)):                     # Do que foi lido no arquivo, aqui se pega as regras
        regras.append(linhas[i].split())

    resultado.write("----------Passo a passo para o caso teste no AFD:----------\n\n")
    
    for i in range(0,len(caso_teste)):                  # Percorre os elementos do caso teste atual
        elemAtual = caso_teste[i]
        if elemAtual not in alfabeto:
                                                     # Verifica se todos os elementos do caso atual 
                                                     # pertencem ao alfabeto
            
            resultado.write("O caso teste possui elemento(s) que nao esta(o) no alfabeto!")
            resultado.close()
            return

    estAtual = estIni[0]                           
    resultado.write("-> Para " + caso_teste + ":\n")
    for i in range(0,len(caso_teste)):              # Percorre os elementos do caso teste atual
        elemAtual = caso_teste[i]


        for i in range(0,qnt_regras):              # Pra cada elemento verifica se ele se encaixa em
            aux_regras = regras[i]                 # alguma regra
            if estAtual == aux_regras[0]:
                if elemAtual == aux_regras[1]:     # O elemento se encaixou em alguma regra
                    resultado.write("\n" + str(elemAtual) + " - Estado alterado de " + str(estAtual) + " para " + aux_regras[2])
                    estAtual = aux_regras[2]       # Altera o estado de acordo com a regra
                        
                    break

    if estAtual not in estFin:
        resultado.write("\n\n" + str(estAtual) + " nao eh estado final, logo: Rejeitado pelo automato!\n\n")
    else:
        resultado.write("\n\n" + str(estAtual) + " eh estado final, logo: Aceito pelo automato!\n\n")

    resultado.close()