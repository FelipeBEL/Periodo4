from arvore import Node

# Ignora essa pilha, ela so eh usada pra converter pra posfixo
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
    prec["."] = 3
    prec["+"] = 2
    prec["*"] = 0
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for chc in infixexpr:
        if chc != '*' and chc != '+' and chc != '(' and chc != ')' and chc != '.':
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

'''
print(infixToPostfix("A * . B + C . D"))
print(infixToPostfix("A . ( B + C ) + D"))
print(infixToPostfix("A . ( B + C + D )"))

expressao = infixToPostfix("A . ( A . A + B . B )")
print(expressao)


pilha = []
right = 0
left = 0

for i in range(len(expressao)-1,-1,-1):

        if expressao[i] in operadores:
                if i == len(expressao)-1: root = Node(expressao(len(expressao)-1))
                else:  
                        while right == 0:
                                if expressao[i]
                                root.insert(expressao[i],"right")
                                right = 1
                        elif left == 0:
                                root.insert(expressao[i],"left")
                                left = 1


                if len(pilha) > 0:

        else: pilha.append(expressao[i])
'''

def gera_afne(tree, level=1):

        global temp
        global transicoes
        global pilha_iniciais
        global pilha_finais
        global handle
        global cont_est

        if tree.left:
                gera_afne(tree.left,level+1)
                        
        if tree.right:
                gera_afne(tree.right,level+1)

        if tree.data in alfabeto:
                handle.write(str(cont_est) + " " + str(tree.data) + " " + str(cont_est+1) + "\n")
                pilha_iniciais.append(cont_est)
                pilha_finais.append(cont_est+1)
                cont_est = cont_est + 2

        if tree.data == '.':
                

        if level == 1: 
                print(tree.data)

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
                        parte1 = stack.pop()
                        parte2 = stack.pop()
                        operandoAtual = Node(chc, parte2, parte1)
                        stack.append(operandoAtual)
    
        return stack.pop()

#teste = criaArvore(infixToPostfix("A.(B+C)+D"))
#teste.printEmNivel()
global temp
global transicoes
global handle
global pilha_iniciais
global pilha_finais
global cont_est

cont_est = 0
transicoes = []
temp = []

exp = input("Expressao: ")

exp = exp.replace(""," ")

exp = infixToPostfix("0 . 0 . ( 0 + 1 ) *")

exp = exp.replace(" ", "")

teste = ArvoreBinER(exp)

handle = open("AFN_E_convertido.txt","w")
gera_afne(teste)

pilha_iniciais = []
pilha_finais = []

handle.close()

teste.view()