class node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_in_ll(self, val, loc):
        newnode = node(val)
        if self.head is None:
            print("List doesn't exist")
        elif loc == 0:
            newnode.ref = self.head
            self.head = newnode
        elif loc == -1:
            self.tail.ref = newnode
            self.tail = newnode
            newnode.ref = None
        else:
            tempnode = self.head
            counter = 0
            while counter < loc - 1:
                tempnode = tempnode.ref
                counter += 1
            nextnode = tempnode.ref
            tempnode.ref = newnode
            newnode.ref = nextnode
            if tempnode == self.tail:
                self.tail = newnode

    def print_ll(self):
        if self.head is None:
            print("List doesn't exist")
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.ref

    def del_item(self, loc):
        if self.head is None:
            print("List doesn't exist")
        else:
            if loc == 0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head = self.head.ref
            elif loc == -1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    tempnode=self.head
                    while tempnode is not None:
                        if tempnode.ref==self.tail:
                            break
                        tempnode=tempnode.ref
                    tempnode.ref=None
                    self.tail=tempnode
              
            else:
                tempnode = self.head
                counter = 0
                while counter < loc - 1:
                    tempnode = tempnode.ref
                    counter += 1
                nextnode = tempnode.ref
                tempnode.ref = nextnode.ref

    def serach_in_ll(self, val):
        if self.head is None:
            print("List is Empty")
        tempnode = self.head
        counter = 0
        while tempnode is not None:
            if tempnode.data == val:
                print(f"Value found at {counter} index")
            else:
                pass
            tempnode = tempnode.ref
            counter += 1

    def len(self):
        tempnode = self.head
        counter = 0
        while tempnode is not None:
            counter += 1
            tempnode = tempnode.ref
        return counter
    def drop_ll(self):
        self.head=None
        self.tail=None



LL = linkedlist()
node1 = node(1)
node2 = node(2)
LL.head = node1
LL.head.ref = node2
LL.tail = node2
LL.print_ll()


