#Algorithm
'''
1.Make a queue class.
2.Initialize a list in the class.
3.Make a enqueue method to add item or work in the list.
4.To make enqueue method we will use standard append method to add item.
5.To dequeue to items we will make a dequeue method in the claas.
6.We will use standard method pop and pass 0 as the arguement, to remove items from start.
7.We'll make a peek method to get the first element of queue. 
8.We'll make a  Action method to empty all the Queue.
9.End of algotithm.
'''
#Code
class queue:
    def __init__(self):
        self.list=[]

    def __str__(self):
        value=[str(x) for x in self.list]
        return "<-".join(value)
    
    def enqueue(self,val):
        self.list.append(val)
        return f"{val} has been added to the Queue"
    
    def dequeue(self):
        if self.isempty():
            return f"Queue is Empty"
        else:
            self.list.pop(0)
    
    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False
    
    def peek(self):
        if self.isempty():
            return f"Queue is Empty"
        else:
            return self.list[0]
    
    def action(self):
        while True:
            if self.list!=[]:
                self.list.pop(0)
            else:
                break
        return f"All the work of Queue is done"
        
        

printer=queue()
printer.enqueue(4)
printer.enqueue(5)
printer.enqueue(6)
print(printer)
print(printer.peek())
print(printer.action())
print(printer)






