#  Linked list for Cracking the Coding Interview

class Node :
    """A node in a linked list"""
    def __init__(self, state, next=None) :
        self.state = state
        self.next = next
        
#  Some code to remember how to make a linked list in python
#head = Node(1)
#head.next = Node(2)
#p.next.next = Node(3)
#
#p = head
##while p.next != None :
#while p :
#    print(p.state)
#    p = p.next

s = list((1,2,3,4,5,3,6,6,7,1,1))
print(s)
l = None
for i in s :
    if l == None :
        l = Node(i)
        #l.next = None    
    else :
        p = l
        while p.next :
            p = p.next
        p.next = Node(i)

p = l
print("From the linked list: ", end= " ")
while p:
    print(p.state, end=" ")
    p = p.next
print()

print("Removing duplicates: ")
#  Needs three pointers, one to advance and two to search ahead to remove duplicates
r = l
#  For each node
while r :
    p = q = r
    #  As long as the list continues
    p = p.next
    while p :
        #  Store state and advance pointer p one ahead
        val = r.state
        #  If node is duplicate remove node
        if val == p.state :
            #remove p
            print(val, "==", p.state, "is", val == p.state)
            q.next = p.next
            #  Do we need to release the node somehow?
            # you fucker :q = p
            p = p.next
        #  Otherwise advance p and q
        else :
            q = p
            p = p.next
        
    r = r.next
    
p = l
print("From the linked list: ", end= " ")
while p:
    print(p.state, end=" ")
    p = p.next
print()
    

print("And if my grandmother had wheels, she'd be a wagon.")

