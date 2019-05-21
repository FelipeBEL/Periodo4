class Node:

    def __init__(self, data=None, esquerda=None, direita=None):

        if data == None:
            self.data = None
        else:
            self.data = data

        if esquerda == None:
            self.left = None
        else:
            self.left = esquerda

        if direita == None:
            self.right = None
        else:
            self.right = direita

    def view(self, level=1):
        arrow = "---" * level
        print ("|" + arrow + ">" + self.data)

        if self.right:
            self.right.view(level+1)
        if self.left:
            self.left.view(level+1)

        return

    