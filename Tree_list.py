class Binarytree:
    def __init__(self,size):
        self.customtree=size * [None]
        self.lastindex=0
        self.maxsize=size

    def insert(self,data):
        if self.lastindex+1==self.size:
            return f"Tree is full"
        self.customtree[self.lastindex+1]=data
        self.lastindex+=1
        return f"Data inserted"

    def lvlorder(self,index):
        for i in range(index,self.lastindex+1):
            print(self.customtree[i])

    def delete_node(self,data):
        if self.lastindex==0:
            return
        else:
            for i in range(1,self.lastindex+1):
                if self.customtree[i]==data:
                    self.customtree[i]=self.customtree[self.lastindex]
                    self.customtree[self.lastindex]=None
                    self.lastindex-=1
                    return f"Node deleted successfully"

    def delete_tree(self):
        self.customtree=[]




