class Node:
    def __init__(self,val=None,next=None):
        self.data=val
        self.next=next

    def __str__(self):
        string=str(self.data)
        if self.next:
            string+=","+str(self.next)
        return string

class Stack:
    def __init__(self):
        self.top=None
        self.minnode=None

    def min(self):
        if not self.minnode:
            return None
        else:
            return self.minnode.data
    
    def push(self,val):
        if self.minnode and self.minnode.data<val:
            self.minnode=Node(val=self.minnode.data , next=self.minnode)
        else:
            self.minnode=Node(val=val,next=self.minnode)
        self.top=Node(val=val,next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.minnode=self.minnode.next
        item=self.top.data
        self.top=self.top.next
        return item

customstack=Stack()
customstack.push(4)
print(customstack.min())
customstack.push(3)
print(customstack.min())
customstack.push(2)
print(customstack.min())
customstack.push(0)
print(customstack.min())
customstack.push(-1)
print(customstack.min())
customstack.pop()
print(customstack.min())

