
class Node:
    def __init__(self,val=None):
        self.data=val
        self.next=None

class linked:
    def __init__(self):
        self.head=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class Stack:
    def __init__(self):
        self.stack=linked()

    def __str__(self):
        value=[str(x.data) for x in self.stack]
        return "<-".join(value)

    def isempty(self):
        if self.stack.head==None:
            return True
        else:
            return False

    
    def push(self,val):
        node=Node(val)
        node.next=self.stack.head
        self.stack.head=node

    def pop(self):
        if self.isempty():
            return "Stack is empty"
        else:
            self.stack.head=self.stack.head.next
            return self.stack.head

    def peek(self):
        return self.stack.head.data

    

stck=Stack()
stck.push(3)
stck.push(4)
stck.push(5)
stck.push(6)
print(stck)
print(stck.isempty())
# print(stck)




