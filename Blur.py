class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublyLinkedList:
    def __init_(self):
        self.head=None
        self.tail=None
    def createDll(self,data):
        node=Node(data)
        node.next=None
        node.prev=None
        self.head=node
        self.tail=node
    def insertDll(self,data,loc):
        node=Node(data)
        if loc==0:
            node.prev=None
            node.next=self.head
            self.head.prev=node
            self.head=node
        elif loc==-1:
            node.prev=self.tail
            node.next=None
            self.tail.next=node
            self.tail=node
        else:
            tempnode=self.head
            c=0
            while c < loc -1 :
                tempnode=tempnode.next
                c+=1
            newnode=tempnode.next
            node.prev=tempnode
            node.next=newnode
            tempnode.next=node
            newnode.prev=node
Dll=doublyLinkedList()
Dll.createDll(3)
Dll.insertDll(2,-1)
Dll.insertDll(1,2)
Dll.insertDll(4,0)
Dll.insertDll(7,3)

