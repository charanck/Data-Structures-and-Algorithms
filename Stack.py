class Stack:
    def __init__(self):
        self.list=[]

    def add(self,data):
        self.list.append(data)

    def remove(self):
        return self.list.pop()

    def display(self):
        return self.list

    def size(self):
        return len(self.list)


s = Stack()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
s.add(7)
s.remove()
print(s.display())


    
    
