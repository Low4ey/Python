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
        
    def __iter__(self):
        node=self.head
        while self.head:
            yield node
            node=node.next


    def __str__(self):
        value=[str(x.data) for x in self.head]
        return "<-".join(value)


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

    def deleteDll(self,loc):
        if self.head==None:
            print("Linked List is empty")
        else:
            if loc==0:
                if self.tail==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head.next
                    node.prev=None
                    self.head=node
            elif loc==-1:
                if self.tail==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.tail.prev
                    node.next=None
                    self.tail=node
            else:
                tempnode=self.head
                c=0
                while c < loc-1:
                    tempnode=tempnode.next
                    c+=1
                tempnode.next=tempnode.next.next
                tempnode.next.prev=tempnode
    def dropDll(self):
        self.head=None
        self.tail=None
        print("Linked List dropped")
   
    def printDll(self):
        if self.head==None:
            print("Linked List is Empty")
        else:
            node=self.head
            while node:
                print(node.data,end=" ")
                node=node.next

    def revprintDll(self):
        if self.head==None:
            print("Linked List is Empty")
        else:
            node=self.tail
            while node:
                print(node.data, end=" ")
                node=node.prev
    def peek(self):
        return self.head.data
                 

Dll=doublyLinkedList()
Dll.createDll(3)
Dll.insertDll(2,-1)
Dll.insertDll(1,1)
Dll.printDll()
Dll.dropDll()
Dll.printDll()
# Dll.revprintDll()

