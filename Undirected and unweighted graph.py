class Graph:
    def __init__(self):
        self.d = {}
        self.size = 0
        
    def addvertex(self,ver):
        if ver in self.d:
            return False
        else:
            self.d[ver]=[]
            self.size +=1
            return
        
    def addedge(self,v1,v2):
        if v1 in self.d and v2 in self.d:
            self.d[v1].append(v2)
            self.d[v2].append(v1)
            return
        else:
            return False
    def display(self):
        print(self.d)
        return
    
    def bfs(self,start):
        out =[]
        t=[]
        t.append(start)
        cur = start
        while len(out) < self.size:
            for i in self.d[cur]:
                if i in t or i in out:
                    continue
                t.append(i)
            out.append(t[0])
            t.pop(0)
            try:
                cur = t[0]
            except IndexError:
                break
        print(out)
                
            
    
g = Graph()
g.addvertex('a')
g.addvertex('b')
g.addvertex('c')
g.addvertex('d')
g.addvertex('e')
g.addedge('a','b')
g.addedge('b','c')
g.addedge('c','d')
g.addedge('d','e')
g.addedge('e','a')
g.display()
g.bfs("a")
    
