
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Create cycle
node4.next = node2

class solution:
    def cycle(self,head):
        temp = head
        my_set = set()
        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp= temp.next
        return False
            
obj = solution()
print(obj.cycle(node1))


#length of loop in linked list
class length:
    def le(self,head):
        temp = head
        my_dict = dict()
        travel = 0
        while temp is not None:
            if temp in my_dict:
                return travel - my_dict[temp]
            my_dict[temp]= travel
            travel +=1
            temp= temp.next
        return 0
    
obj2 =length()
print(obj2.le(node1))
  
        

        