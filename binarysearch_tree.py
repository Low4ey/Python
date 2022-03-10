class Tree:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

def insert(rootnode,data):
    if rootnode.data==None:
        rootnode.data=data
    elif rootnode.data<=data:
        if rootnode.left is None:
            rootnode.left=Tree(data)
        else:
            insert(rootnode.left,data)
    else:
        if rootnode.right is None:
            rootnode.right=Tree(data)
        else:
            insert(rootnode.right,data)

    return f"Insertion success"

def traverse(rootnode):
    if rootnode is None:
        return
    else:
        print(rootnode.data)
        traverse(rootnode.left)
        traverse(rootnode.right)

def search(rootnode,data):
    if rootnode.data==data:
        print("DATA Found")
    elif rootnode.data< data:
        if rootnode.left.data==data:
            print("DATA Found")
        else:
            search(rootnode.left,data)
    else:
        if rootnode.right.data==data:
            print("DATA Found")
        else:
            search(rootnode.right,data)
        print("Data Not Found")
        







newbst=Tree()
insert(newbst,80)
insert(newbst,70)
insert(newbst,90)
insert(newbst,60)
insert(newbst,100)
traverse(newbst)
search(newbst,40)

