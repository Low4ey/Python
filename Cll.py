
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def createCll(self,data):
        node=Node(data)
        node.ref=node
        self.head=node
        self.tail=node

    def insertCll(self,data,loc):
        node=Node(data)
        if loc==0:
            node.ref=self.head
            self.head=node
        elif loc==-1:
            tempnode=self.tail
            tempnode.ref=node
            self.tail=node
            node.ref=self.head
        else:
            tempnode=self.head
            c=0
            while c < loc-1:
                tempnode=tempnode.ref
                c+=1
            newnode=tempnode.ref
            tempnode.ref=node
            node.ref=newnode
    
    def deleteCll(self,loc):
        if self.head==None:
            print("Linked List is empty")
        else:
            if loc==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.ref
                    self.tail.ref=self.head
            elif loc==-1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    tempnode=self.head
                    while self.head is not None:
                        if tempnode.ref==self.tail:
                            self.tail=tempnode
                            tempnode.ref=self.head
                            break
                        tempnode=tempnode.ref
            else:
                tempnode=self.head
                c=0
                while c < loc-1:
                    tempnode=tempnode.ref
                    c+=1
                node=tempnode.ref
                tempnode.ref=node.ref

    def printCll(self):
        tempnode=self.head
        while self.head is not None:
            print(tempnode.data,end=" ")
            
            if tempnode.ref==self.head:
                break
            tempnode=tempnode.ref
    def __iter__(self):
        node=self.head
        while node:
            yield node
            if node.ref==self.head:
                break
            node=node.ref
    def dropCll(self):
        self.head=None
        self.tail=None
        print("LL dropped")
    

Cll=CircularSinglyLinkedList()
Cll.createCll(4)
Cll.insertCll(2,0)
Cll.insertCll(3,1)
Cll.insertCll(4,-1)
Cll.dropCll()
Cll.printCll()

# print([i.data for i in Cll])  