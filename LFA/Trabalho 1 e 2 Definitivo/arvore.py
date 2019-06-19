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

    def view(self, handler, level=1):
        arrow = "---" * level
        handler.write("|" + arrow + ">" + self.data + "\n")

        if self.left:
            self.left.view(handler,level+1)
        if self.right:
            self.right.view(handler,level+1)
        return

    