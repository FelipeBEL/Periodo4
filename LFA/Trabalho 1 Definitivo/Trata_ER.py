from arvore import Node

# Essa pilha eh usada pra converter pra posfixo
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def infixToPostfix(infixexpr):
    global alfabeto
    global operadores

    prec = {}
    prec["."] = 2
    prec["+"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for chc in infixexpr:
        if chc != '*' and chc != '+' and chc != '(' and chc != ')' and chc != '.' and chc != ' ':
                if chc not in alfabeto:
                        alfabeto.append(chc)

    for chc in infixexpr:
        if chc == '*' or chc == '+' or chc == '(' or chc == ')' or chc == '.':
                if chc not in operadores:
                        operadores.append(chc)

    for token in tokenList:
        if token == '*':
            postfixList.append(token)
        else:
                if token in alfabeto:
                    postfixList.append(token)
                elif token == '(':
                    opStack.push(token)
                elif token == ')':
                    topToken = opStack.pop()
                    while topToken != '(':
                        postfixList.append(topToken)
                        topToken = opStack.pop()
                else:
                    while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                        postfixList.append(opStack.pop())
                    opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

alfabeto = []
operadores = []

def gera_afne(tree, level=1):

        global pilha_iniciais
        global pilha_finais
        global handle
        global cont_est
        global ja_especificados

        p1 = []
        p2 = []

        if tree.left:
                gera_afne(tree.left,level+1)
                        
        if tree.right:
                gera_afne(tree.right,level+1)

        if tree.data in alfabeto:
                ja_especificados.append(cont_est)
                handle.write(str(cont_est) + " " + str(tree.data) + " " + str(cont_est+1) + "\n")

                for alfa in alfabeto:
                        if alfa != tree.data:
                                handle.write(str(cont_est) + " " + alfa + " vazio" + "\n")
                                
                pilha_iniciais.append(cont_est)
                pilha_finais.append(cont_est+1)
                cont_est = cont_est + 2


        if tree.data == '.':
                p1.append(pilha_iniciais.pop())
                p1.append(pilha_finais.pop())
                p2.append(pilha_iniciais.pop())
                p2.append(pilha_finais.pop())

                handle.write(str(cont_est) + " E " + str(p2[0]) + "\n")
                handle.write(str(p2[1]) + " E " + str(p1[0]) + "\n")
                handle.write(str(p1[1]) + " E " + str(cont_est+1) + "\n")

                pilha_iniciais.append(cont_est)
                pilha_finais.append(cont_est+1)

                cont_est = cont_est + 2

        if tree.data == '+':
                p1.append(pilha_iniciais.pop())
                p1.append(pilha_finais.pop())
                p2.append(pilha_iniciais.pop())
                p2.append(pilha_finais.pop())

                handle.write(str(cont_est) + " E " + str(p2[0]) + "\n")
                handle.write(str(cont_est) + " E " + str(p1[0]) + "\n")
                handle.write(str(p2[1]) + " E " + str(cont_est+1) + "\n")
                handle.write(str(p1[1]) + " E " + str(cont_est+1) + "\n")

                pilha_iniciais.append(cont_est)
                pilha_finais.append(cont_est+1)

                cont_est = cont_est + 2

        if tree.data == '*':
                p1.append(pilha_iniciais.pop())
                p1.append(pilha_finais.pop())

                handle.write(str(cont_est) + " E " + str(cont_est+1) + "\n")
                handle.write(str(cont_est) + " E " + str(p1[0]) + "\n")
                handle.write(str(p1[1]) + " E " + str(p1[0]) + "\n")
                handle.write(str(p1[1]) + " E " + str(cont_est+1) + "\n")

                pilha_iniciais.append(cont_est)
                pilha_finais.append(cont_est+1)

                cont_est = cont_est + 2

        return

def ArvoreBinER(expressao):
        if len(expressao) <= 1: 
                return Node(expressao)

        stack = []

        for chc in expressao:
                if chc not in operadores:
                        operandoAtual = Node(chc)
                        stack.append(operandoAtual)
        
                elif chc == '*':
                        parte1 = stack.pop()
                        operandoAtual = Node(chc, parte1)
                        stack.append(operandoAtual)

                else:
                        parte2 = stack.pop()
                        parte1 = stack.pop()
                        operandoAtual = Node(chc, parte1, parte2)
                        stack.append(operandoAtual)
    
        return stack.pop()


def trata_er(exp):
        global handle
        global pilha_iniciais
        global pilha_finais
        global cont_est
        global ja_especificados

        ja_especificados = []
        cont_est = 0
        pilha_iniciais = []
        pilha_finais = []

        handler = open("arvore.txt","w")

        handler.write("----------Expressão inserida:----------\n\n" + exp + "\n\n")

        exp = exp.replace(""," ")

        exp = infixToPostfix(exp)

        exp = exp.replace(" ", "")

        handler.write("----------Expressão na forma posfixa:----------\n\n" + exp + "\n\n")

        arvore = ArvoreBinER(exp)

        handle = open("automato_ndetE.txt","w")

        gera_afne(arvore)

        handle.close()

        handle = open("automato_ndetE.txt","w")
        handle.close()

        handle = open("automato_ndetE.txt","w")

        for item in alfabeto:
                handle.write(item)

        handle.write('\n')

        for item in range(cont_est):
            handle.write(str(item) + " ")

        handle.write('\n')

        handle.write(str(cont_est-2) + "\n")
        handle.write(str(cont_est-1) + "\n")

        cont_est = 0
        ja_especificados[:] = []
        gera_afne(arvore)

        for item in range(cont_est):
                if item not in ja_especificados:
                        for alfa in alfabeto:
                                handle.write(str(item) + " " + alfa + " vazio" + "\n")


        handle.close()

        handler.write("----------Árvore Binária da ER:----------\n\n")

        arvore.view(handler)

        handler.close()