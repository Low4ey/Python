from random import randint

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None

    def __str__(self):
        return str(self.data)
class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node.data
            node=node.next
    
    def __str__(self):
         values=[str(x) for x in self]
         return "-->".join(values)

    def __len__(self):
        node=self.head
        counter=0
        while node:
            counter+=1
            node=node.next
        return counter
    def add(self,data):
        if self.head is None:
            node=Node(data)
            self.head=node
            self.tail=node
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
        return self.tail
 
    def generate(self,n,min,max):
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(randint(min,max))
        return self



