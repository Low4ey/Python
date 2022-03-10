class stack:
    def __init__(self,max_len=None):
        self.list=[]
        self.len=max_len

    def __str__(self):
        value=reversed(self.list)
        return "-".join([str(x) for x in value])

    def pop(self):
        if self.list==[]:
            print(f" stack is empty")
        else:
            self.list.pop()
    def push(self,val):
        if len(self.list)==self.len:
            print(f"stack reached its limit")
        else:
            self.list.append(val)
    
    def isempty(self):
        if self.list==[]:
            print(f"satck is empty")
        else:
            print(f"stack is not empty")
    
    def isfull(self):
        if len(self.list)==self.len:
            print(f"satck is Full")
        else:
            print(f"satck is not Full")
    
    def peek(self):
        return self.list[len(self.list)-1]


custom_stack=stack(4)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(4)
custom_stack.push(5)
print(custom_stack)
custom_stack.isempty()
custom_stack.isfull()
custom_stack.push(5)
# print(custom_stack)
    


