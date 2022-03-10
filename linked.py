class node:
    def __init__(self,data):
        self.data=data
        self.ref=None  
#creation of linked list
class LinkedList:
    def __init__(self):
        self.head=None  
        self.tail=None
    #It will make linked list iterable
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.ref

#creation of linked list object
LL=LinkedList()
#creation of two node
node1=node(1)
node2=node(2)
#making connection between nodes
LL.head=node1
LL.head.ref=node2
LL.tail=node2
#printing data of linked list
print([node.data for node in LL])