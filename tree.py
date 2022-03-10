import QueueLinkedList as q

class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def preorder(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preorder(rootnode.left)
    preorder(rootnode.right)

def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.left)
    print(rootnode.data)
    inorder(rootnode.right)
def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.left)
    postorder(rootnode.right)
    print(rootnode.data)

def levelorder(rootnode):
    if not rootnode:
        return
    else:
        customqueue=q.Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            print(root.value.data)
            if (root.value.left is not None):
                customqueue.enqueue(root.value.left)
            if (root.value.right is not None):
                customqueue.enqueue(root.value.right)


def Insert(rootnode,data):
    tree=treenode(data)
    if not rootnode:
        return
    else:
        customqueue=q.Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            if (root.value.left is not None):
                customqueue.enqueue(root.value.left)
            else:
                root.value.left=tree
                return
            if (root.value.right is not None):
                customqueue.enqueue(root.value.right)
            else:
                root.value.right=tree
                return


def searchdata(rootnode,data):
    if not treenode:
        return
    else:
        customq=q.Queue()
        customq.enqueue(rootnode)
        while not (customq.isEmpty()):
            root=customq.dequeue()
            if root.value.data==data:
                return f"Value Found"
            if (root.value.left is not None):
                customq.enqueue(root.value.left)   
            if (root.value.right is not None):
                customq.enqueue(root.value.right)
        return f"Value not found"   

def getdeepnode(rootnode):
    if not rootnode:
        return
    else:
        customqueue=q.Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            if (root.value.left is not None):
                customqueue.enqueue(root.value.left)
            if (root.value.right is not None):
                customqueue.enqueue(root.value.right)
    return root.value

def deldeepnode(rootnode,dnode):
    if not rootnode:
        return
    else:
        customqueue=q.Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value is dnode:
                root.value=None
                return
            if root.value.right:
                if root.value.right is dnode:
                    root.value.right=None
                    return
                else:
                    customqueue.enqueue(root.value.right)
            if root.value.left:
                if root.value.left is dnode:
                    root.value.left=None
                    return
                else:
                    customqueue.enqueue(root.value.left)
                    
def deletenode(rootnode,node):
    if not rootnode:
        return
    else:
        customqueue=q.Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value.data==node:
                dnode=getdeepnode(rootnode)
                root.value.data=dnode.data
                deletenode(rootnode,dnode)
                return f"Node deleted"
            if (root.value.left is not None):
                customqueue.enqueue(root.value.left)
            if (root.value.right is not None):
                customqueue.enqueue(root.value.right)
        return f"Node not found"

def deletetree(rootnode):
    if not rootnode:
        return
    else:
        rootnode.data=None
        rootnode.left=None
        rootnode.right=None



bt=treenode("Drinks")
leftnode=treenode("Hot")
rightnode=treenode("cold")
bt.right=rightnode
bt.left=leftnode
leftnode.left=treenode("Tea")
leftnode.right=treenode("Coffee")
rightnode.left=treenode("Cola")
rightnode.right=treenode("Pepsi")

