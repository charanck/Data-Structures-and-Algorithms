class Node:
    def __init__(self):
        self.data = None
        self.prev = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def display(self):
        if self.head == None:
            print("No elements are in the list")
            return
        cur_node =  self.head
        print(cur_node.data)
        while cur_node.next:
            print(cur_node.next.data)
            cur_node = cur_node.next
        
    def add(self, data):
        new_node = Node()
        new_node.data = data
        if self.head == None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node:
            if not cur_node.next:
                cur_node.next = new_node
                new_node.prev = cur_node
                break
            cur_node = cur_node.next
        self.tail = new_node

    def addhead(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        if data == self.head.data:
            self.head = self.head.next
        cur_node = self.head
        while cur_node.next:
            if data == cur_node.next.data:
                if cur_node.next.next:
                    cur_node.next = cur_node.next.next
                    cur_node.next.next.prev = cur_node.next
                    break
                else:
                    cur_node.next = None
                    break             
            cur_node = cur_node.next

    def insertafter(self, after, data):
        cur_node = self.head
        new_node = Node()
        new_node.data = data
        while cur_node:
            if(cur_node.data == after):
                new_node.next = cur_node.next
                new_node.prev = cur_node
                cur_node.next = new_node
                cur_node.next.next.prev = new_node
                break
            cur_node = cur_node.next

    def insertbefore(self, before, data):
        cur_node = self.head
        new_node = Node()
        new_node.data = data
        while cur_node:
            if(cur_node.data == before):
                new_node.next = cur_node
                new_node.prev = cur_node.prev
                cur_node.prev = new_node
                cur_node.prev.prev.next = new_node
                break
            cur_node = cur_node.next
        
        
                
                   
ll=Linked_List()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.addhead(0)
ll.insertbefore(5,4.5)

ll.display()
