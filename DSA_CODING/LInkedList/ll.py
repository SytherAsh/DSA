class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
        
# LinkedList = LinkedList()
# LinkedList.append(1)
# LinkedList.append(2)
# LinkedList.append(3)
# LinkedList.display()  # Output: 1 -> 2 -> 3 -> NoneA
a=2
b=3

# a,b=b,a
# b,a = a, b
print(a,b)  # Output: 3 2
