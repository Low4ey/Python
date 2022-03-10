from Linked_list import linkedList

def remove_dupe(ll):
    if ll.head==ll.tail:
        return
    else:
        node=ll.head
        custom=set([node.data])
        while node.next:
            if node.next.data  in custom:
                node.next=node.next.next
            else:
                custom.add(node.next.data)
                node=node.next

        return custom

def search(ll,loc):
    node=ll.head
    c=0
    while node.next:
        if c==loc:
            return f"VALUE AT INDEX {loc} IS {node.next.data}"
        else:
            c+=1
            node=node.next

        

l1=linkedList()
l1.generate(10,0,99)
print(l1)
print(search(l1,3))
