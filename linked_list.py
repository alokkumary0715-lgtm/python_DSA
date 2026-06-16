class node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
node1 = node(5)
node2 = node(6)
node3 = node(7)
node4 = node(8)

node1.next  = node2
node2.next = node3
node4.next = node1

#when you print an object its add will show in terminal
print(node1)

print(node1.val)
print(node1.next.val)


"""the above method is not efficient to use"""

