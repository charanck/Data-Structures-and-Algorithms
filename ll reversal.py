class Node:
    def __init__(self):
        self.data = None
        self.next = None
class Linked_List:
    def __init__(self):
        self.head=None
        
    def add(self, data):
        new_node = Node()
        new_node.data = data
        if self.head == None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
    
    def display(self):
        node = self.head
        print(self.head.data)
        while node.next:
            print(node.next.data)
            node = node.next
            
    def addhead(self,data):
        cur_node = Node()
        cur_node.data = data
        cur_node.next = self.head
        self.head = cur_node
        
   
    def reverse(self):
        cur_node=self.head
        prev =None
        nxt=None
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt
        self.head = prev
                  
ll=Linked_List()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.display()
ll.reverse()
ll.display()
        
