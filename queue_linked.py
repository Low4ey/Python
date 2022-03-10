
class Node:
    def __init__(self,val=None):
        self.value=val
        self.next=None


    def __str__(self):
        return str(self.value)

class linked:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class Queue:
    def __init__(self):
        self.queue=linked()

    def __str__(self):
        values=[str(x.value) for x in self.queue]
        return "<-".join(values)
    
    def isempty(self):
        if self.queue.head==None:
            return True
        else:
            return False
        
    def enque(self,val):
        node=Node(val)
        if self.queue.head==None:
            self.queue.head=node
            self.queue.tail=node
        else:
            self.queue.tail.next=node
            self.queue.tail=node
    
    def deque(self):
        if self.isempty():
            return "Queue is empty"
        elif self.queue.head==self.queue.tail:
            self.queue.head=None
            self.queue.tail=None
        else:
            self.queue.head=self.queue.head.next
        return self.queue.tail

    def peek(self):
        if self.isempty():
            return "Queue is empty"
        else:
            return self.queue.head.value
    
    def delete(self):
        self.queue.head=None
        self.queue.tail=None


customqueue=Queue()
customqueue.enque(4)
customqueue.enque(5)
customqueue.enque(6)
print(customqueue)