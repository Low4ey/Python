
class stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        value=reversed(self.list)
        return "-".join([str(x) for x in value])

    def isempty(self):
        if self.list==[]:
            return f"{self} is empty"
        else:
            return f"{self} is not empty"
    
    def peek(self):
        if self.list==[]:
            return f"{self} is empty"
        else:
            return self.list[len(self.list)-1]
   
    def pop(self):
        if self.list==[]:
            return f"{self} is empty"
        else:
            self.list.pop()
            # return f"Popped item is{self.list[len(self.list)]}"
    
    def push(self,val):
        self.list.append(val)
        return f"{val} appended in stack"

    
custom_stack=stack()
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(4)
custom_stack.push(5)
print(custom_stack)
custom_stack.pop()
print(custom_stack)



