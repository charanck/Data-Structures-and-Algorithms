class Node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:

    def __init__(self):
        self.head=None

    def add(self,data):
        new_node = Node()
        new_node.data = data
        if(self.head ==None):
            self.head = new_node
            return
        cur_node=self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def print(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node =cur_node.next

    def reverse(self):
        cur_node = self.head
        prev=None
        nxt=None
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node= nxt
        self.head = prev

    def nth_to_last(self,no):
        self.reverse()
        count=1
        cur_node= self.head
        while cur_node:
            cur_node=cur_node.next
            count +=1
            if(count == no):
                print("The nth from last is %d" %(cur_node.data))
                self.reverse()
                return
                
        
        


ll =LinkedList()

ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)

ll.nth_to_last(2)

ll.print()
