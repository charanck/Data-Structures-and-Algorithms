class queue:
    def __init__(self):
        self.list = []

    def q(self,data):
        self.list.append(data)

    def dq(self,data):
        self.list = [data] + self.list

    def size():
        print(len(self.list))

    def display(self):
        print(self.list)
        
q=queue()
q.q(1)
q.q(2)
q.q(3)
q.q(4)
q.q(5)
q.q(6)
q.q(7)
q.q(8)
q.display()
