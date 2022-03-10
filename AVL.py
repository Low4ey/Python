import tree as t

class Avl:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1
def getheight(rootnode):
    if not rootnode:
        return 0
    return rootnode.height

def rightrotation(node):
    newroot=node.left
    






avl=Avl(5)
t.levelorder(avl)
