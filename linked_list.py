class node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
# node1 = node(5)
# node2 = node(6)
# node3 = node(7)
# node4 = node(8)

# node1.next  = node2
# node2.next = node3
# node4.next = node1

# #when you print an object its add will show in terminal
# print(node1)

# print(node1.val)
# print(node1.next.val)


"""the above method is not efficient to use"""

class sinlyll:
    def __init__(self):
        self.head= None
    def append(self,val):
        new_node= node(val)
        if self.head==None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next =  new_node

#traverse
    def traverse(self):
        if not self.head:
            print("sll is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr = curr.next
            print()




sll = sinlyll()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()


