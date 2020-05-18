class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    
    
class bt:
    def __init__(self):
        self.root = None
        
    def add(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self._add(self.root,data)
                
    def _add(self,root,data):
        if not root.left and data < root.data:
            root.left = Node(data)
            return
        elif not root.right:
            root.right = Node(data)
            return
               
        if root.data > data or root.data == data:
            if not root.left:
                root.left = Node(data)
            self._add(root.left,data)
        else:
            if not root.right:
                root.right = Node(data)
            self._add(root.right,data)
            
    def display(self):
        self._display(self.root)
        
        
    def _display(self,root):
        if root == None:
            return
        self._display(root.left)
        print(root.data)
        self._display(root.right)
            
    def remove(self,data):
        #To remove the root
        if data == self.root.data:
            templ = self.root.left
            if self.root.right:
                tempr = self.root.right
            else:
                self.root = templ
                return
            self.root = tempr
            cur= self.root
            while cur:
                if cur.left == None:
                    cur.left = templ
                    break
                else:
                    cur = cur.left
        #Others
        else:
            self._trav(self.root,data,None)
            
            
            
    def _trav(self,root,data,prev):
        if data == root.data:
            if(root.left==None and root.right == None):
                if prev.left == root:
                    prev.left = None
                    return
                else:
                    prev.right = None
                    return
            else:
                self._remove(root,prev)
                
        
        if data > root.data:
            if root.right:
                self._trav(root.right,data,root)
            else:
                return False
        else:
            if root.left:
                self._trav(root.left,data,root)
            else:
                return False
                
    def _remove(self,root,prev):
        #root with only one branch
        if root.left == None:
            if root == prev.left:
                prev.left = root.right
                del root
                return
            if root == prev.right:
                prev.right = root.right
                del root
                return
        if root.right == None:
            if root == prev.left:
                prev.left = root.left
                del root
                return
            if root == prev.right:
                prev.right = root.left
                
        #Root with two branch
        if root.right and root.left:
            if root==prev.left:
                templ= root.left
                prev.left = root.right
                cur = root.right
                while cur:
                    cur= cur.left
                cur.left = templ
                del root
                return
            if root == prev.right:
                templ=root.left
                prev.right = root.right
                cur = root.right
                while cur:
                    cur = cur.left
                cur.left = templ
                del root
                return
                
        
       
              
t = bt()
t.add(10)
t.add(5)
t.add(19)
t.add(1)
t.add(6)
t.add(17)
t.add(21)
t.display()





